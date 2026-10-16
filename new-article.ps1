<#
.SYNOPSIS
    Interactive article creator for Amit Kumar Shukla's website.
    Adds the article to _data/articles.yml, runs build.ps1 to generate HTML files and search index.

.EXAMPLE
    .\new-article.ps1 -Title "Mastering Java 21 Virtual Threads in Spring Boot" -Category "java" -Tags "Java21, Loom, SpringBoot" -Summary "A deep-dive into how Project Loom virtual threads improve throughput in enterprise Spring microservices."
#>

param(
    [string]$Title,
    [string]$Category,
    [string]$Tags,
    [string]$Summary,
    [string]$ReadTime = "6 min read"
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Interactive prompts if not passed via parameters
if ([string]::IsNullOrWhiteSpace($Title)) {
    $Title = Read-Host "Enter Article Title"
}

if ([string]::IsNullOrWhiteSpace($Category)) {
    Write-Host "`nSelect Primary Category:" -ForegroundColor Cyan
    Write-Host "1. Java Core & Modern APIs (java)"
    Write-Host "2. Spring Boot & Cloud (spring)"
    Write-Host "3. Reactive & Event-Driven (reactive)"
    Write-Host "4. Cloud & Kubernetes (cloud)"
    Write-Host "5. Enterprise Architecture & DDD (architecture)"
    Write-Host "6. Security & Observability (security-observability)"
    $catChoice = Read-Host "Enter Choice (1-6)"
    $Category = switch ($catChoice) {
        "1" { "java" }
        "2" { "spring" }
        "3" { "reactive" }
        "4" { "cloud" }
        "5" { "architecture" }
        "6" { "security-observability" }
        default { "java" }
    }
} else {
    # Normalize slug
    $Category = switch -Wildcard ($Category) {
        "*java*" { "java" }
        "*spring*" { "spring" }
        "*reactive*" { "reactive" }
        "*cloud*" { "cloud" }
        "*arch*" { "architecture" }
        "*sec*" { "security-observability" }
        default { $Category.ToLower() }
    }
}

if ([string]::IsNullOrWhiteSpace($Summary)) {
    $Summary = Read-Host "Enter Short Summary / Excerpt"
}
if ([string]::IsNullOrWhiteSpace($Tags)) {
    $Tags = Read-Host "Enter Tags (comma separated, e.g. Java 21, Loom, Microservices)"
}

# Generate Slug from Title
$slug = $Title.ToLower() -replace '[^a-z0-9\s-]', '' -replace '\s+', '-' -replace '-+', '-'
$slug = $slug.Trim('-')

$dateStr = (Get-Date).ToString("yyyy-MM-dd")
$displayDate = (Get-Date).ToString("MMMM dd, yyyy")

$tagArray = $Tags -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }

# Append to _data/articles.yml
$articlesYml = Join-Path $PSScriptRoot "_data\articles.yml"

$tagYamlLines = ""
foreach ($t in $tagArray) {
    $tagYamlLines += "    - `"$t`"`n"
}

$entryYaml = @"

- slug: "$slug"
  title: "$Title"
  category: "$Category"
  categories:
    - "$Category"
  date: "$dateStr"
  display_date: "$displayDate"
  read_time: "$ReadTime"
  tags:
$tagYamlLines  description: "$Summary"
  featured: true
"@

[System.IO.File]::AppendAllText($articlesYml, $entryYaml, [System.Text.Encoding]::UTF8)
Write-Host "`n-> Added article '$Title' to _data/articles.yml" -ForegroundColor Green

# Run build.ps1 to generate HTML files, category listings, and search index
$buildScript = Join-Path $PSScriptRoot "build.ps1"
if (Test-Path $buildScript) {
    & $buildScript
}

$articleHtmlPath = Join-Path $PSScriptRoot "articles\$slug\index.html"

Write-Host "========================================================" -ForegroundColor Green
Write-Host " Article Created & Synchronized Successfully! " -ForegroundColor Cyan
Write-Host " Config: _data/articles.yml" -ForegroundColor Yellow
Write-Host " Page:   $articleHtmlPath" -ForegroundColor Yellow
Write-Host " URL:    /articles/$slug/" -ForegroundColor Yellow
Write-Host " Open the article HTML file to write your paragraphs & code snippets." -ForegroundColor Cyan
Write-Host " Run .\preview.ps1 to preview the live site." -ForegroundColor Yellow
Write-Host "========================================================`n" -ForegroundColor Green
