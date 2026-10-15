<#
.SYNOPSIS
    Creates a new architectural article scaffold with all metadata, styling, and search index updates.

.EXAMPLE
    .\new-article.ps1 -Title "Mastering Java 21 Virtual Threads in Spring Boot" -Category "Java Core & Modern APIs" -Tags "Java21, Loom, SpringBoot" -Summary "A deep-dive into how Project Loom virtual threads improve throughput in enterprise Spring microservices."
#>

param(
    [string]$Title,
    [string]$Category,
    [string]$Tags,
    [string]$Summary
)

# Interactive prompts if not passed via parameters
if ([string]::IsNullOrWhiteSpace($Title)) {
    $Title = Read-Host "Enter Article Title"
}
if ([string]::IsNullOrWhiteSpace($Category)) {
    Write-Host "`nSelect Category:" -ForegroundColor Cyan
    Write-Host "1. Java Core & Modern APIs (☕)"
    Write-Host "2. Spring Boot & Cloud (🍃)"
    Write-Host "3. Reactive & Event-Driven (⚡)"
    Write-Host "4. Cloud & Kubernetes (☁️)"
    Write-Host "5. Enterprise Architecture & DDD (🏛️)"
    Write-Host "6. Security & Observability (🛡️)"
    $catChoice = Read-Host "Enter Choice (1-6)"
    $Category = switch ($catChoice) {
        "1" { "Java Core & Modern APIs" }
        "2" { "Spring Boot & Cloud" }
        "3" { "Reactive & Event-Driven" }
        "4" { "Cloud & Kubernetes" }
        "5" { "Enterprise Architecture & DDD" }
        "6" { "Security & Observability" }
        default { "Java Core & Modern APIs" }
    }
}
if ([string]::IsNullOrWhiteSpace($Summary)) {
    $Summary = Read-Host "Enter Short Summary / Excerpt"
}
if ([string]::IsNullOrWhiteSpace($Tags)) {
    $Tags = Read-Host "Enter Tags (comma separated, e.g. Java, Microservices, Spring)"
}

# Generate Slug from Title
$slug = $Title.ToLower() -replace '[^a-z0-9\s-]', '' -replace '\s+', '-' -replace '-+', '-'
$slug = $slug.Trim('-')

$dateStr = (Get-Date).ToString("yyyy-MM-dd")
$displayDate = (Get-Date).ToString("MMMM dd, yyyy")
$jsonDate = (Get-Date).ToString("MMM dd, yyyy")

$tagArray = $Tags -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
$tagHtml = ($tagArray | ForEach-Object { "<span class=""tag-pill"">#$_</span>" }) -join "`n                  "
$tagJson = ($tagArray | ForEach-Object { "`"$_`"" }) -join ", "

# Determine Category Icon & Slug
$catIcon = switch -Wildcard ($Category) {
    "*Java*" { "☕" }
    "*Spring*" { "🍃" }
    "*Reactive*" { "⚡" }
    "*Cloud*" { "☁️" }
    "*Architecture*" { "🏛️" }
    "*Security*" { "🛡️" }
    default { "📝" }
}

$articleDir = Join-Path $PSScriptRoot "articles\$slug"
if (-not (Test-Path $articleDir)) {
    New-Item -ItemType Directory -Path $articleDir -Force | Out-Null
}

$articleFile = Join-Path $articleDir "index.html"

# Article Template
$htmlContent = @"
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>$Title | Amit Kumar Shukla</title>
  <meta name="description" content="$Summary">
  <meta name="author" content="Amit Kumar Shukla">

  <!-- Open Graph -->
  <meta property="og:title" content="$Title">
  <meta property="og:description" content="$Summary">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://amitkrshukla.github.io/articles/$slug/">

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <link rel="icon" type="image/svg+xml" href="../../assets/images/favicon.svg">
  <link rel="stylesheet" href="../../assets/css/style.css">
  <link rel="stylesheet" href="../../assets/css/syntax.css">

  <script>
    (function() {
      const savedTheme = localStorage.getItem('theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.documentElement.setAttribute('data-theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
      }
    })();
  </script>
</head>
<body class="site-body">
  <div class="site-wrapper">
    <!-- Header -->
    <header class="site-header">
      <div class="site-header-container">
        <a class="site-brand" href="../../">
          <div class="brand-avatar"><span>AS</span></div>
          <div class="brand-text">
            <span class="brand-name">Amit Kumar Shukla</span>
            <span class="brand-tagline">Senior Digital Architect</span>
          </div>
        </a>

        <nav class="site-nav" id="site-nav">
          <ul class="nav-links">
            <li><a href="../../" class="nav-link">Home</a></li>
            <li><a href="../../articles/" class="nav-link active">Articles</a></li>
            <li><a href="../../categories/" class="nav-link">Categories</a></li>
            <li><a href="../../resume/" class="nav-link">Resume</a></li>
            <li><a href="../../about/" class="nav-link">About</a></li>
          </ul>
        </nav>

        <div class="header-actions">
          <button class="action-btn search-trigger" id="search-trigger" title="Search articles (Ctrl+K)" aria-label="Search">
            <i class="fa-solid fa-magnifying-glass"></i>
            <span class="search-key-hint">Ctrl K</span>
          </button>
          <button class="action-btn theme-toggle" id="theme-toggle" title="Toggle Dark/Light Mode" aria-label="Toggle theme">
            <i class="fa-solid fa-moon dark-icon"></i>
            <i class="fa-solid fa-sun light-icon"></i>
          </button>
          <a href="../../resume/" class="btn btn-sm btn-outline-primary resume-quick-btn">
            <i class="fa-solid fa-file-pdf"></i>
            <span>Resume</span>
          </a>
          <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Toggle menu" aria-expanded="false">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>

    <!-- Main Article -->
    <main class="site-main" id="main-content">
      <article class="post-layout">
        <header class="post-header-hero">
          <div class="post-header-container">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../../">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="../../articles/">Articles</a>
              <span class="breadcrumb-separator">/</span>
              <span class="breadcrumb-current">$Category</span>
            </nav>

            <div class="post-header-meta">
              <span class="post-category-tag">$catIcon $Category</span>
              <span class="post-header-date"><i class="fa-regular fa-calendar"></i> $displayDate</span>
              <span class="post-header-readtime"><i class="fa-regular fa-clock"></i> 6 min read</span>
            </div>

            <h1 class="post-main-title">$Title</h1>
            <p class="post-main-lead">$Summary</p>

            <div class="post-author-bar">
              <div class="author-avatar-sm"><span>AS</span></div>
              <div class="author-details-sm">
                <span class="author-name-sm">Amit Kumar Shukla</span>
                <span class="author-title-sm">Senior Digital Architect</span>
              </div>
              <div class="post-actions-sm">
                <button class="share-btn-sm" id="copy-article-link" title="Copy article link">
                  <i class="fa-solid fa-link"></i> <span class="share-btn-text">Share</span>
                </button>
              </div>
            </div>
          </div>
        </header>

        <div class="post-body-container">
          <div class="post-layout-grid">
            <div class="post-content-column">
              <div class="post-entry-content" id="article-content">
                <p>
                  Write your article introduction here...
                </p>

                <h2>1. Core Architectural Concepts</h2>
                <p>
                  Explain the main concept and architectural tradeoffs here...
                </p>

                <pre><code class="language-java">// Code demonstration
public class ExampleService {
    public void execute() {
        // Implementation
    }
}</code></pre>

                <h2>2. Production Considerations & Tradeoffs</h2>
                <p>
                  Lessons learned from enterprise deployment...
                </p>
              </div>

              <!-- Tags -->
              <div class="post-footer-tags">
                <span class="tags-label"><i class="fa-solid fa-tags"></i> Tags:</span>
                <div class="tags-list">
                  $tagHtml
                </div>
              </div>

              <!-- Share -->
              <div class="post-share-section">
                <h4 class="share-title">Found this insightful? Share with your network:</h4>
                <div class="share-buttons">
                  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://amitkrshukla.github.io/articles/$slug/" target="_blank" rel="noopener noreferrer" class="btn-share btn-linkedin">
                    <i class="fa-brands fa-linkedin"></i> LinkedIn
                  </a>
                  <a href="mailto:?subject=$Title&body=Read this article by Amit Kumar Shukla: https://amitkrshukla.github.io/articles/$slug/" class="btn-share btn-email">
                    <i class="fa-solid fa-envelope"></i> Email
                  </a>
                </div>
              </div>

              <!-- Author Box -->
              <div class="post-author-box">
                <div class="author-box-avatar">AS</div>
                <div class="author-box-content">
                  <h4 class="author-box-name">Amit Kumar Shukla</h4>
                  <p class="author-box-title">Senior Digital Architect | Enterprise Architecture & Java Technologist</p>
                  <p class="author-box-bio">
                    Over 20 years architecting enterprise-scale digital platforms across global banking and cloud ecosystems. Experienced in leading 100+ resource engineering teams and unifying 400+ business functions.
                  </p>
                  <div class="author-box-links">
                    <a href="../../resume/" class="btn btn-sm btn-primary">View Interactive Resume</a>
                    <a href="../../about/" class="btn btn-sm btn-secondary">About Me</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </article>
    </main>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-container">
        <div class="footer-bottom">
          <p>&copy; 2026 Amit Kumar Shukla. All rights reserved. Hosted on GitHub Pages.</p>
          <button class="back-to-top" id="back-to-top" title="Back to top" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>
        </div>
      </div>
    </footer>
  </div>

  <script src="../../assets/js/main.js"></script>
  <script src="../../assets/js/search.js"></script>
</body>
</html>
"@

[System.IO.File]::WriteAllText($articleFile, $htmlContent, [System.Text.Encoding]::UTF8)

# Update search.json
$searchJsonPath = Join-Path $PSScriptRoot "search.json"
if (Test-Path $searchJsonPath) {
    try {
        $searchData = Get-Content $searchJsonPath -Raw | ConvertFrom-Json
        $newEntry = [PSCustomObject]@{
            title = $Title
            url = "/articles/$slug/"
            date = $jsonDate
            category = $Category
            tags = @($tagArray)
            description = $Summary
        }
        $updatedData = @($newEntry) + @($searchData | Where-Object { $_.url -ne "/articles/$slug/" })
        $updatedJson = $updatedData | ConvertTo-Json -Depth 5
        [System.IO.File]::WriteAllText($searchJsonPath, $updatedJson, [System.Text.Encoding]::UTF8)
        Write-Host "Updated search.json index successfully." -ForegroundColor Green
    } catch {
        Write-Host "Notice: could not automatically update search.json: $_" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host " Article Created Successfully! " -ForegroundColor Cyan
Write-Host " Path: $articleFile" -ForegroundColor Yellow
Write-Host " URL:  /articles/$slug/" -ForegroundColor Yellow
Write-Host " Run .\preview.ps1 to review your new article locally." -ForegroundColor Cyan
Write-Host "========================================================`n" -ForegroundColor Green
