# ==============================================================================
# Static Site Generator for Amit Kumar Shukla's Technical Blog
# Reads _data/categories.yml and _data/articles.yml to build all HTML pages & search index
# Usage: .\build.ps1
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host " Building Amit Kumar Shukla Website from YAML configs..." -ForegroundColor Cyan
Write-Host "========================================================`n" -ForegroundColor Green

# ------------------------------------------------------------------------------
# 1. UTF-8 YAML Parser for List of Objects
# ------------------------------------------------------------------------------
function Parse-YamlFile([string]$FilePath) {
    if (-not (Test-Path $FilePath)) {
        Write-Error "Config file not found: $FilePath"
        return @()
    }
    $lines = Get-Content $FilePath -Encoding UTF8
    $items = @()
    $currentItem = $null
    $currentListProp = $null

    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed.StartsWith('#') -or $trimmed -eq '') { continue }

        if ($line -match '^\s*-\s+([a-zA-Z0-9_-]+):\s*(.*)$') {
            if ($currentItem) { $items += [PSCustomObject]$currentItem }
            $currentItem = [ordered]@{}
            $currentListProp = $null
            $propName = $matches[1].Trim()
            $propVal = $matches[2].Trim()
            if ($propVal.StartsWith('"') -and $propVal.EndsWith('"')) {
                $propVal = $propVal.Substring(1, $propVal.Length - 2)
            } elseif ($propVal.StartsWith("'") -and $propVal.EndsWith("'")) {
                $propVal = $propVal.Substring(1, $propVal.Length - 2)
            }
            $currentItem[$propName] = $propVal
        }
        elseif ($currentItem -ne $null -and $line -match '^\s{2,4}([a-zA-Z0-9_-]+):\s*(.*)$') {
            $propName = $matches[1].Trim()
            $propVal = $matches[2].Trim()
            if ($propVal -eq '') {
                $currentListProp = $propName
                $currentItem[$propName] = @()
            } else {
                $currentListProp = $null
                if ($propVal.StartsWith('"') -and $propVal.EndsWith('"')) {
                    $propVal = $propVal.Substring(1, $propVal.Length - 2)
                } elseif ($propVal.StartsWith("'") -and $propVal.EndsWith("'")) {
                    $propVal = $propVal.Substring(1, $propVal.Length - 2)
                }
                $currentItem[$propName] = $propVal
            }
        }
        elseif ($currentItem -ne $null -and $currentListProp -ne $null -and $line -match '^\s+-\s*(.*)$') {
            $val = $matches[1].Trim()
            if ($val.StartsWith('"') -and $val.EndsWith('"')) {
                $val = $val.Substring(1, $val.Length - 2)
            } elseif ($val.StartsWith("'") -and $val.EndsWith("'")) {
                $val = $val.Substring(1, $val.Length - 2)
            }
            $currentItem[$currentListProp] += $val
        }
    }
    if ($currentItem) { $items += [PSCustomObject]$currentItem }
    return $items
}

# Load configurations
$categoriesFile = Join-Path $PSScriptRoot "_data\categories.yml"
$articlesFile = Join-Path $PSScriptRoot "_data\articles.yml"

$categories = Parse-YamlFile $categoriesFile
$articles = Parse-YamlFile $articlesFile

Write-Host "-> Loaded $($categories.Count) categories from _data/categories.yml" -ForegroundColor Yellow
Write-Host "-> Loaded $($articles.Count) articles from _data/articles.yml" -ForegroundColor Yellow

# Helper to find category by slug
function Get-CategoryObj($catSlug) {
    foreach ($c in $categories) {
        if ($c.slug -eq $catSlug) { return $c }
    }
    return $null
}

# ------------------------------------------------------------------------------
# 2. Shared HTML Header & Footer Generators
# ------------------------------------------------------------------------------
function Get-HtmlHead($title, $description, $relPrefix = ".") {
    return @"
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>$title | Amit Kumar Shukla</title>
  <meta name="description" content="$description">
  <meta name="author" content="Amit Kumar Shukla">

  <!-- Open Graph -->
  <meta property="og:title" content="$title | Amit Kumar Shukla">
  <meta property="og:description" content="$description">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://amitkrshukla.github.io/">

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Favicon & Styles -->
  <link rel="icon" type="image/svg+xml" href="$relPrefix/assets/images/favicon.svg">
  <link rel="stylesheet" href="$relPrefix/assets/css/style.css">
  <link rel="stylesheet" href="$relPrefix/assets/css/syntax.css">

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
"@
}

function Get-HtmlNavbar($activeNav, $relPrefix = ".") {
    $homeActive = if ($activeNav -eq 'home') { 'active' } else { '' }
    $articlesActive = if ($activeNav -eq 'articles') { 'active' } else { '' }
    $categoriesActive = if ($activeNav -eq 'categories') { 'active' } else { '' }
    $resumeActive = if ($activeNav -eq 'resume') { 'active' } else { '' }
    $aboutActive = if ($activeNav -eq 'about') { 'active' } else { '' }

    return @"
    <header class="site-header">
      <div class="site-header-container">
        <a class="site-brand" href="$relPrefix/">
          <div class="brand-avatar"><span>AS</span></div>
          <div class="brand-text">
            <span class="brand-name">Amit Kumar Shukla</span>
            <span class="brand-tagline">Senior Digital Architect</span>
          </div>
        </a>

        <nav class="site-nav" id="site-nav">
          <ul class="nav-links">
            <li><a href="$relPrefix/" class="nav-link $homeActive">Home</a></li>
            <li><a href="$relPrefix/articles/" class="nav-link $articlesActive">Articles</a></li>
            <li><a href="$relPrefix/categories/" class="nav-link $categoriesActive">Categories</a></li>
            <li><a href="$relPrefix/resume/" class="nav-link $resumeActive">Resume</a></li>
            <li><a href="$relPrefix/about/" class="nav-link $aboutActive">About</a></li>
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
          <a href="$relPrefix/resume/" class="btn btn-sm btn-outline-primary resume-quick-btn">
            <i class="fa-solid fa-file-pdf"></i>
            <span>Resume</span>
          </a>
          <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Toggle menu" aria-expanded="false">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>
"@
}

function Get-HtmlFooter($relPrefix = ".") {
    $catLinks = ""
    foreach ($cat in $categories) {
        $catLinks += "              <li><a href=""$relPrefix/categories/$($cat.slug)/"">$($cat.icon) $($cat.name)</a></li>`n"
    }

    return @"
    <footer class="site-footer">
      <div class="footer-container">
        <div class="footer-grid">
          <div class="footer-col footer-about">
            <h3 class="footer-title">Amit Kumar Shukla</h3>
            <p class="footer-bio">
              Senior Digital Architect with 20+ years of experience architecting and delivering enterprise-scale digital banking, telecom, and cloud-native solutions.
            </p>
            <div class="footer-social">
              <a href="https://linkedin.com/in/amit-kr-shukla" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="social-icon"><i class="fa-brands fa-linkedin-in"></i></a>
              <a href="mailto:amit_kr_shukla@yahoo.com" aria-label="Email" class="social-icon"><i class="fa-solid fa-envelope"></i></a>
              <a href="https://github.com/amitkrshukla" target="_blank" rel="noopener noreferrer" aria-label="GitHub" class="social-icon"><i class="fa-brands fa-github"></i></a>
            </div>
          </div>

          <div class="footer-col">
            <h4 class="footer-heading">Navigation</h4>
            <ul class="footer-links">
              <li><a href="$relPrefix/">Home</a></li>
              <li><a href="$relPrefix/articles/">All Articles</a></li>
              <li><a href="$relPrefix/categories/">Browse by Category</a></li>
              <li><a href="$relPrefix/resume/">Interactive Resume</a></li>
              <li><a href="$relPrefix/AmitShukla_Resume_SeniorDigitalArchitect.pdf" target="_blank">Download Resume PDF</a></li>
              <li><a href="$relPrefix/about/">About Me</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4 class="footer-heading">Architecture Topics</h4>
            <ul class="footer-links">
$catLinks            </ul>
          </div>

          <div class="footer-col">
            <h4 class="footer-heading">Contact & Location</h4>
            <p class="footer-contact-item"><i class="fa-solid fa-location-dot"></i> Burnaby, BC, Canada</p>
            <p class="footer-contact-item"><i class="fa-solid fa-envelope"></i> <a href="mailto:amit_kr_shukla@yahoo.com">amit_kr_shukla@yahoo.com</a></p>
            <p class="footer-contact-item"><i class="fa-solid fa-phone"></i> +1 (236) 863-4703</p>
          </div>
        </div>

        <div class="footer-bottom">
          <p>&copy; 2026 Amit Kumar Shukla. All rights reserved. Hosted on GitHub Pages.</p>
          <button class="back-to-top" id="back-to-top" title="Back to top" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>
        </div>
      </div>
    </footer>
"@
}

function Get-HtmlSearchModal() {
    return @"
  <div class="search-modal" id="search-modal" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="search-modal-backdrop" id="search-backdrop"></div>
    <div class="search-modal-box">
      <div class="search-modal-header">
        <i class="fa-solid fa-magnifying-glass search-modal-icon"></i>
        <input type="text" id="search-input" class="search-modal-input" placeholder="Search articles by topic, Java, Spring..." autocomplete="off">
        <button class="search-modal-close" id="search-modal-close" aria-label="Close search"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="search-modal-status" id="search-status"><span class="search-hint">Type to start searching... Press <kbd>ESC</kbd> to exit</span></div>
      <div class="search-modal-results" id="search-results"></div>
    </div>
  </div>
"@
}
# Helper to test if article belongs to category
function Test-ArticleInCategory($art, $catSlug) {
    if ($art.category -eq $catSlug) { return $true }
    if ($art.categories -and ($art.categories -contains $catSlug)) { return $true }
    return $false
}

# Helper to render an article card
function Render-ArticleCard($art, $relPrefix = ".") {
    $cat = Get-CategoryObj $art.category
    $catIcon = if ($cat) { $cat.icon } else { "📄" }
    $catName = if ($cat) { $cat.name } else { $art.category }

    $tagHtml = ""
    if ($art.tags) {
        foreach ($t in $art.tags) {
            $tagHtml += "<span class=""tag-pill"">#$t</span> "
        }
    }

    $allCats = @()
    if ($art.category) { $allCats += $art.category }
    if ($art.categories) { foreach ($c in $art.categories) { if ($allCats -notcontains $c) { $allCats += $c } } }
    $catAttr = $allCats -join " "

    $readTimeHtml = if ($art.read_time) { "<span class=""post-reading-time""><i class=""fa-regular fa-clock""></i> $($art.read_time)</span>" } else { "" }

    $cardHtml = @"
            <article class="post-card filterable-card" data-categories="$catAttr" data-title="$($art.title.ToLower())">
              <div class="post-card-meta">
                <span class="post-category-tag">$catIcon $catName</span>
                <span class="post-date"><i class="fa-regular fa-calendar"></i> $($art.display_date)</span>
                $readTimeHtml
              </div>
              <h3 class="post-card-title">
                <a href="$relPrefix/articles/$($art.slug)/">$($art.title)</a>
              </h3>
              <p class="post-card-excerpt">
                $($art.description)
              </p>
              <div class="post-card-tags">
                $tagHtml
              </div>
              <div class="post-card-footer">
                <a href="$relPrefix/articles/$($art.slug)/" class="read-more-link">
                  Read Article <i class="fa-solid fa-arrow-right"></i>
                </a>
              </div>
            </article>
"@
    return "`n$cardHtml`n"
}

# ------------------------------------------------------------------------------
# 3. Generate Dedicated HTML Page for Each Category: categories/<slug>/index.html
# ------------------------------------------------------------------------------
Write-Host "`n-> Generating dedicated category HTML pages..." -ForegroundColor Cyan

foreach ($cat in $categories) {
    $catSlug = $cat.slug
    $catName = $cat.name
    $catIcon = $cat.icon
    $catDesc = $cat.description

    # Find articles in this category
    $catArticles = @($articles | Where-Object { Test-ArticleInCategory $_ $catSlug })
    $catCount = $catArticles.Count

    $catDir = Join-Path $PSScriptRoot "categories\$catSlug"
    if (-not (Test-Path $catDir)) {
        New-Item -ItemType Directory -Path $catDir -Force | Out-Null
    }
    $catFile = Join-Path $catDir "index.html"

    # Render category articles
    $articlesGridHtml = ""
    if ($catCount -gt 0) {
        foreach ($a in $catArticles) {
            $articlesGridHtml += Render-ArticleCard $a "../.."
        }
    } else {
        $articlesGridHtml = @"
          <div class="empty-state" style="grid-column: 1 / -1; padding: 4rem 1rem;">
            <i class="fa-solid fa-pen-nib" style="font-size: 2.5rem; color: var(--accent-primary); margin-bottom: 1rem;"></i>
            <h3>Articles under $catName are being drafted!</h3>
            <p>Check back shortly or explore our other architectural categories below.</p>
          </div>
"@
    }

    # Other categories jump pills
    $otherCatsHtml = ""
    foreach ($other in $categories) {
        $activeClass = if ($other.slug -eq $catSlug) { 'active' } else { '' }
        $otherCatsHtml += "          <a href=""../$($other.slug)/"" class=""category-jump-pill $activeClass""><span>$($other.icon)</span> $($other.name)</a>`n"
    }

    $pageHtml = @"
<!DOCTYPE html>
<html lang="en">
$(Get-HtmlHead "$catName Architecture Articles" $catDesc "../..")
<body class="site-body">
  <div class="site-wrapper">
$(Get-HtmlNavbar "categories" "../..")

    <main class="site-main" id="main-content">
      <div class="page-container">
        <!-- Breadcrumb -->
        <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: 1.5rem;">
          <a href="../../">Home</a>
          <span class="breadcrumb-separator">/</span>
          <a href="../">Categories</a>
          <span class="breadcrumb-separator">/</span>
          <span class="breadcrumb-current">$catName</span>
        </nav>

        <!-- Category Banner -->
        <header class="category-dedicated-header" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 2.5rem; margin-bottom: 2.5rem;">
          <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
            <div style="font-size: 3.5rem; width: 80px; height: 80px; display: flex; align-items: center; justify-content: center; background: var(--bg-tertiary); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              $catIcon
            </div>
            <div style="flex: 1; min-width: 250px;">
              <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem; flex-wrap: wrap;">
                <h1 style="font-size: 2rem; margin: 0;">$catName</h1>
                <span class="category-group-badge" style="background: var(--accent-subtle); color: var(--accent-primary); font-weight: 600; padding: 0.25rem 0.8rem; border-radius: var(--radius-full); font-size: 0.85rem; border: 1px solid var(--accent-primary);">
                  $catCount $(if ($catCount -eq 1) { 'Article' } else { 'Articles' })
                </span>
              </div>
              <p style="color: var(--text-secondary); margin: 0; font-size: 1.05rem; line-height: 1.6;">
                $catDesc
              </p>
            </div>
          </div>
        </header>

        <!-- Category Articles Grid -->
        <div class="section-header" style="margin-bottom: 1.5rem;">
          <div>
            <h2 class="section-title">Articles in $catName</h2>
            <p class="section-subtitle">Deep dives, code implementations, and architectural best practices</p>
          </div>
          <a href="../../articles/" class="section-link">All Articles <i class="fa-solid fa-arrow-right"></i></a>
        </div>

        <div class="posts-grid" style="margin-bottom: 3rem;">
$articlesGridHtml
        </div>

        <!-- Other Categories Jump Nav -->
        <div style="border-top: 1px solid var(--border-color); padding-top: 2.5rem; margin-top: 2rem;">
          <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: var(--text-primary); text-align: center;">Explore Other Architecture Categories</h3>
          <div class="category-jump-nav">
$otherCatsHtml          </div>
        </div>
      </div>
    </main>

$(Get-HtmlFooter "../..")
  </div>

$(Get-HtmlSearchModal)

  <script src="../../assets/js/main.js"></script>
  <script src="../../assets/js/search.js"></script>
</body>
</html>
"@

    [System.IO.File]::WriteAllText($catFile, $pageHtml, [System.Text.Encoding]::UTF8)
    Write-Host "   Created category page: categories/$catSlug/index.html ($catCount articles)" -ForegroundColor DarkGreen
}

# ------------------------------------------------------------------------------
# 4. Generate Master Categories Directory: categories/index.html
# ------------------------------------------------------------------------------
Write-Host "`n-> Generating master category directory: categories/index.html..." -ForegroundColor Cyan

$masterJumpPills = ""
$masterSections = ""

foreach ($cat in $categories) {
    $catSlug = $cat.slug
    $catName = $cat.name
    $catIcon = $cat.icon
    $catDesc = $cat.description

    $catArticles = @($articles | Where-Object { Test-ArticleInCategory $_ $catSlug })
    $catCount = $catArticles.Count

    $masterJumpPills += "      <a href=""#$catSlug"" class=""category-jump-pill""><span>$catIcon</span> $catName</a>`n"

    $secArticlesHtml = ""
    if ($catCount -gt 0) {
        foreach ($a in $catArticles) {
            $secArticlesHtml += Render-ArticleCard $a ".."
        }
    } else {
        $secArticlesHtml = @"
          <div class="empty-category-box">
            <p>Articles under this topic are currently being prepared. Stay tuned!</p>
          </div>
"@
    }

    $masterSections += @"
      <section class="category-group-section" id="$catSlug">
        <div class="category-group-header">
          <div class="category-group-icon">$catIcon</div>
          <div class="category-group-info">
            <h2 class="category-group-title">
              <a href="./$catSlug/" style="color: inherit; text-decoration: none;">$catName</a>
            </h2>
            <p class="category-group-desc">$catDesc</p>
          </div>
          <a href="./$catSlug/" class="category-group-badge" style="text-decoration: none;">
            $catCount $(if ($catCount -eq 1) { 'Article' } else { 'Articles' }) &rarr;
          </a>
        </div>
        <div class="posts-grid">
$secArticlesHtml
        </div>
      </section>

"@
}

$masterCategoriesHtml = @"
<!DOCTYPE html>
<html lang="en">
$(Get-HtmlHead "Article Categories & Topics" "Browse technical topics and architectural disciplines covering modern Java 17/21, Spring Boot, Reactive Microservices, Kafka, and Cloud-Native systems." "..")
<body class="site-body">
  <div class="site-wrapper">
$(Get-HtmlNavbar "categories" "..")

    <main class="site-main" id="main-content">
      <div class="page-container">
        <header class="page-header text-center">
          <h1 class="page-title">Browse Topics & Disciplines</h1>
          <p class="page-subtitle">Categorized knowledge base covering modern Java, enterprise architecture, and distributed cloud computing.</p>
        </header>

        <!-- Category Nav Pills -->
        <div class="category-jump-nav">
$masterJumpPills        </div>

        <!-- Category Sections -->
        <div class="category-sections-list">
$masterSections        </div>
      </div>
    </main>

$(Get-HtmlFooter "..")
  </div>

$(Get-HtmlSearchModal)

  <script src="../assets/js/main.js"></script>
  <script src="../assets/js/search.js"></script>
</body>
</html>
"@

$categoriesIndexFile = Join-Path $PSScriptRoot "categories\index.html"
[System.IO.File]::WriteAllText($categoriesIndexFile, $masterCategoriesHtml, [System.Text.Encoding]::UTF8)
Write-Host "   Generated categories/index.html successfully." -ForegroundColor DarkGreen

# ------------------------------------------------------------------------------
# 5. Generate Home Page: index.html
# ------------------------------------------------------------------------------
Write-Host "`n-> Generating home page: index.html..." -ForegroundColor Cyan

# Category grid for Home page
$homeCatGrid = ""
foreach ($cat in $categories) {
    $catSlug = $cat.slug
    $catArticles = @($articles | Where-Object { Test-ArticleInCategory $_ $catSlug })
    $catCount = $catArticles.Count
    $homeCatGrid += @"
            <a href="./categories/$catSlug/" class="category-card" data-category="$catSlug">
              <div class="category-icon">$($cat.icon)</div>
              <div class="category-info">
                <h3 class="category-name">$($cat.name)</h3>
                <p class="category-desc">$($cat.description)</p>
                <span class="category-count">$catCount $(if ($catCount -eq 1) { 'Article' } else { 'Articles' }) &bull; View &rarr;</span>
              </div>
            </a>
"@
}

# Category filter pills for Home page
$homeCatFilterPills = "<button class=""filter-btn active"" data-filter=""all"">All Articles ($($articles.Count))</button>`n"
foreach ($cat in $categories) {
    $catArticles = @($articles | Where-Object { Test-ArticleInCategory $_ $cat.slug })
    if ($catArticles.Count -gt 0) {
        $homeCatFilterPills += "              <button class=""filter-btn"" data-filter=""$($cat.slug)"">$($cat.icon) $($cat.name)</button>`n"
    }
}

# Articles list for Home page
$homeArticlesList = ""
foreach ($a in $articles) {
    $homeArticlesList += Render-ArticleCard $a "."
}

$homePageHtml = @"
<!DOCTYPE html>
<html lang="en">
$(Get-HtmlHead "Enterprise Architecture, Modern Java & Distributed Systems" "Architectural insights, Java 17/21 innovations, Spring Boot, Reactive Microservices, Cloud-Native AWS/Kubernetes, and Enterprise Systems Design by Amit Kumar Shukla." ".")
<body class="site-body">
  <div class="site-wrapper">
$(Get-HtmlNavbar "home" ".")

    <main class="site-main" id="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-container">
          <div class="hero-content">
            <div class="hero-badge">
              <span class="badge-dot"></span>
              <span>Senior Digital Architect &bull; 20+ Years Enterprise Experience</span>
            </div>
            <h1 class="hero-title">
              Enterprise Architecture, <br>
              <span class="hero-highlight">Modern Java</span> & Distributed Systems
            </h1>
            <p class="hero-description">
              Hi, I'm <strong>Amit Kumar Shukla</strong>. I design and lead resilient, enterprise-scale digital platforms across banking and cloud ecosystems (17 years inside HSBC's global banking estate). Here I share practical engineering insights on Java 17/21, Spring Boot, reactive microservices, Kafka event streaming, and cloud-native architecture.
            </p>

            <div class="hero-actions">
              <a href="./articles/" class="btn btn-primary">
                <i class="fa-solid fa-book-open"></i> Read Articles
              </a>
              <a href="./resume/" class="btn btn-secondary">
                <i class="fa-solid fa-file-lines"></i> Interactive Resume
              </a>
              <a href="./AmitShukla_Resume_SeniorDigitalArchitect.pdf" target="_blank" class="btn btn-ghost" title="Download PDF Resume">
                <i class="fa-solid fa-file-arrow-down"></i> Download PDF
              </a>
              <a href="mailto:amit_kr_shukla@yahoo.com" class="btn btn-ghost">
                <i class="fa-solid fa-envelope"></i> Contact Me
              </a>
            </div>

            <!-- Quick Metrics Grid -->
            <div class="hero-stats">
              <div class="stat-card">
                <span class="stat-number">20+</span>
                <span class="stat-label">Years Designing Systems</span>
              </div>
              <div class="stat-card">
                <span class="stat-number">17</span>
                <span class="stat-label">Years at HSBC Global Banking</span>
              </div>
              <div class="stat-card">
                <span class="stat-number">400+</span>
                <span class="stat-label">Business Functions Unified</span>
              </div>
              <div class="stat-card">
                <span class="stat-number">100+</span>
                <span class="stat-label">Engineers & Leads Mentored</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Knowledge Base by Technology (Categories Section) -->
      <section class="section categories-section">
        <div class="section-container">
          <div class="section-header">
            <div>
              <h2 class="section-title">Knowledge Base by Technology</h2>
              <p class="section-subtitle">Curated architectural guides, patterns, and deep-dives across the Java & cloud ecosystem</p>
            </div>
            <a href="./categories/" class="section-link">
              View All Topics & Deep Dives <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>

          <div class="category-grid">
$homeCatGrid          </div>
        </div>
      </section>

      <!-- Featured Articles Section with Live Interactive Filtering -->
      <section class="section articles-section">
        <div class="section-container">
          <div class="section-header">
            <div>
              <h2 class="section-title">Featured & Latest Architectural Articles</h2>
              <p class="section-subtitle">Real-world engineering patterns and production lessons from 20+ years of high-scale enterprise systems</p>
            </div>
            <a href="./articles/" class="section-link">
              Browse All Articles <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>

          <!-- Quick Interactive Category Filter Bar -->
          <div class="filter-controls" style="margin-bottom: 2rem;">
            <div class="category-filters" id="home-category-filters">
$homeCatFilterPills            </div>

            <div class="article-search-bar" style="margin-top: 1rem;">
              <i class="fa-solid fa-filter"></i>
              <input type="text" id="home-article-search" placeholder="Quick filter by topic, keyword, or technology (e.g. JWT, Kafka, WebFlux, DDD)...">
            </div>
          </div>

          <div class="posts-grid" id="home-articles-list">
$homeArticlesList          </div>

          <div id="home-no-articles" class="empty-state" style="display: none;">
            <i class="fa-solid fa-magnifying-glass"></i>
            <h3>No matching articles found</h3>
            <p>Try filtering by another topic or clearing your search term.</p>
          </div>
        </div>
      </section>

      <!-- Architect Profile & Resume Callout -->
      <section class="section summary-callout-section">
        <div class="section-container">
          <div class="summary-card">
            <div class="summary-content">
              <span class="summary-tag">About The Architect</span>
              <h2 class="summary-title">Amit Kumar Shukla</h2>
              <p class="summary-text">
                Senior Digital Architect with 20+ years of hands-on experience designing and delivering enterprise-scale digital solutions across heavily regulated banking and distributed cloud estates (17 years inside HSBC's global banking architecture). Experienced in leading 100+ resource cross-functional Agile teams, unifying 400+ business functions, and modernizing legacy core banking systems into high-throughput, cloud-native microservices.
              </p>
              <div class="summary-badges">
                <span class="badge-item"><i class="fa-solid fa-certificate"></i> Generative AI Leader &bull; Google</span>
                <span class="badge-item"><i class="fa-solid fa-cloud"></i> KCNA &bull; Linux Foundation</span>
                <span class="badge-item"><i class="fa-solid fa-award"></i> Professional Scrum Master I & II &bull; Scrum.org</span>
                <span class="badge-item"><i class="fa-solid fa-trophy"></i> HSBC RISE, TEAM, STARS & SPOT Awards</span>
              </div>
              <div class="summary-actions">
                <a href="./resume/" class="btn btn-primary">
                  <i class="fa-solid fa-file-lines"></i> View Interactive Resume
                </a>
                <a href="./AmitShukla_Resume_SeniorDigitalArchitect.pdf" target="_blank" class="btn btn-secondary">
                  <i class="fa-solid fa-file-arrow-down"></i> Download PDF Resume
                </a>
                <a href="./about/" class="btn btn-outline-primary">
                  <i class="fa-solid fa-user"></i> Full Career Story & Bio
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

$(Get-HtmlFooter ".")
  </div>

$(Get-HtmlSearchModal)

  <script src="./assets/js/main.js"></script>
  <script src="./assets/js/search.js"></script>

  <!-- Interactive Filtering Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const filterBtns = document.querySelectorAll('#home-category-filters .filter-btn');
      const searchInput = document.getElementById('home-article-search');
      const cards = document.querySelectorAll('#home-articles-list .filterable-card');
      const emptyState = document.getElementById('home-no-articles');

      let currentCat = 'all';
      let currentQuery = '';

      function filterArticles() {
        let count = 0;
        cards.forEach(card => {
          const cats = card.getAttribute('data-categories') || '';
          const title = card.getAttribute('data-title') || '';
          
          const matchCategory = (currentCat === 'all') || cats.includes(currentCat);
          const matchQuery = !currentQuery || title.includes(currentQuery);

          if (matchCategory && matchQuery) {
            card.style.display = '';
            count++;
          } else {
            card.style.display = 'none';
          }
        });

        if (emptyState) {
          emptyState.style.display = count === 0 ? 'block' : 'none';
        }
      }

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentCat = btn.getAttribute('data-filter');
          filterArticles();
        });
      });

      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          currentQuery = e.target.value.trim().toLowerCase();
          filterArticles();
        });
      }
    });
  </script>
</body>
</html>
"@

$homeIndexFile = Join-Path $PSScriptRoot "index.html"
[System.IO.File]::WriteAllText($homeIndexFile, $homePageHtml, [System.Text.Encoding]::UTF8)
Write-Host "   Generated index.html successfully." -ForegroundColor DarkGreen

# ------------------------------------------------------------------------------
# 6. Generate Articles Catalog: articles/index.html
# ------------------------------------------------------------------------------
Write-Host "`n-> Generating articles catalog: articles/index.html..." -ForegroundColor Cyan

$articlesFilterPills = "<button class=""filter-btn active"" data-filter=""all"">All Articles ($($articles.Count))</button>`n"
foreach ($cat in $categories) {
    $catArticles = @($articles | Where-Object { Test-ArticleInCategory $_ $cat.slug })
    if ($catArticles.Count -gt 0) {
        $articlesFilterPills += "              <button class=""filter-btn"" data-filter=""$($cat.slug)"">$($cat.icon) $($cat.name)</button>`n"
    }
}

$articlesGridHtml = ""
foreach ($a in $articles) {
    $articlesGridHtml += Render-ArticleCard $a ".."
}

$articlesIndexHtml = @"
<!DOCTYPE html>
<html lang="en">
$(Get-HtmlHead "All Articles & Insights" "Technical architecture guides, Java 17/21 deep dives, reactive systems, Kafka event streaming, and enterprise design patterns." "..")
<body class="site-body">
  <div class="site-wrapper">
$(Get-HtmlNavbar "articles" "..")

    <main class="site-main" id="main-content">
      <div class="page-container">
        <header class="page-header text-center">
          <h1 class="page-title">Articles & Architectural Insights</h1>
          <p class="page-subtitle">Explorations in Java 17/21, Spring Boot, Reactive Microservices, Kafka, and Cloud-Native Systems</p>

          <!-- Filter bar -->
          <div class="filter-controls">
            <div class="category-filters" id="category-filters">
$articlesFilterPills            </div>

            <div class="article-search-bar">
              <i class="fa-solid fa-filter"></i>
              <input type="text" id="article-filter-input" placeholder="Quick filter by keyword, tag, or title (e.g. WebFlux, JWT, Kafka, DDD)...">
            </div>
          </div>
        </header>

        <div class="posts-grid" id="articles-list">
$articlesGridHtml        </div>

        <div id="no-articles-found" class="empty-state" style="display: none;">
          <i class="fa-solid fa-magnifying-glass"></i>
          <h3>No matching articles found</h3>
          <p>Try searching for other terms like "Spring", "Kafka", "WebFlux", or "Kubernetes".</p>
        </div>
      </div>
    </main>

$(Get-HtmlFooter "..")
  </div>

$(Get-HtmlSearchModal)

  <script src="../assets/js/main.js"></script>
  <script src="../assets/js/search.js"></script>

  <!-- Interactive Filtering Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const filterBtns = document.querySelectorAll('.category-filters .filter-btn');
      const filterInput = document.getElementById('article-filter-input');
      const articles = document.querySelectorAll('#articles-list .filterable-card');
      const emptyState = document.getElementById('no-articles-found');

      let currentCategory = 'all';
      let currentKeyword = '';

      function applyFilters() {
        let visibleCount = 0;
        articles.forEach(article => {
          const title = article.getAttribute('data-title') || '';
          const cats = article.getAttribute('data-categories') || '';

          const matchesCategory = (currentCategory === 'all') || cats.includes(currentCategory);
          const matchesKeyword = !currentKeyword || title.includes(currentKeyword);

          if (matchesCategory && matchesKeyword) {
            article.style.display = '';
            visibleCount++;
          } else {
            article.style.display = 'none';
          }
        });

        if (emptyState) {
          emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
        }
      }

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentCategory = btn.getAttribute('data-filter');
          applyFilters();
        });
      });

      if (filterInput) {
        filterInput.addEventListener('input', (e) => {
          currentKeyword = e.target.value.trim().toLowerCase();
          applyFilters();
        });
      }
    });
  </script>
</body>
</html>
"@

$articlesIndexFile = Join-Path $PSScriptRoot "articles\index.html"
[System.IO.File]::WriteAllText($articlesIndexFile, $articlesIndexHtml, [System.Text.Encoding]::UTF8)
Write-Host "   Generated articles/index.html successfully." -ForegroundColor DarkGreen

# ------------------------------------------------------------------------------
# 7. Check/Scaffold Each Article Page: articles/<slug>/index.html
# ------------------------------------------------------------------------------
Write-Host "`n-> Checking article HTML files in articles/..." -ForegroundColor Cyan

foreach ($art in $articles) {
    $artSlug = $art.slug
    $artTitle = $art.title
    $artDesc = $art.description
    $artCat = Get-CategoryObj $art.category
    $catSlug = if ($artCat) { $artCat.slug } else { $art.category }
    $catName = if ($artCat) { $artCat.name } else { $art.category }
    $catIcon = if ($artCat) { $artCat.icon } else { "📄" }

    $artDir = Join-Path $PSScriptRoot "articles\$artSlug"
    if (-not (Test-Path $artDir)) {
        New-Item -ItemType Directory -Path $artDir -Force | Out-Null
    }
    $artFile = Join-Path $artDir "index.html"

    if (-not (Test-Path $artFile)) {
        # Scaffold new article HTML file
        $tagHtml = ""
        if ($art.tags) {
            foreach ($t in $art.tags) {
                $tagHtml += "<span class=""tag-pill"">#$t</span>`n                  "
            }
        }

        $newArtHtml = @"
<!DOCTYPE html>
<html lang="en">
$(Get-HtmlHead $artTitle $artDesc "../..")
<body class="site-body">
  <div class="site-wrapper">
$(Get-HtmlNavbar "articles" "../..")

    <main class="site-main" id="main-content">
      <article class="post-layout">
        <header class="post-header-hero">
          <div class="post-header-container">
            <nav class="breadcrumb-nav" aria-label="Breadcrumb">
              <a href="../../">Home</a>
              <span class="breadcrumb-separator">/</span>
              <a href="../../articles/">Articles</a>
              <span class="breadcrumb-separator">/</span>
              <a href="../../categories/$catSlug/">$catName</a>
            </nav>

            <div class="post-header-meta">
              <span class="post-category-tag">$catIcon $catName</span>
              <span class="post-header-date"><i class="fa-regular fa-calendar"></i> $($art.display_date)</span>
              <span class="post-header-readtime"><i class="fa-regular fa-clock"></i> $($art.read_time)</span>
            </div>

            <h1 class="post-main-title">$artTitle</h1>
            <p class="post-main-lead">$artDesc</p>

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

              <div class="post-footer-tags">
                <span class="tags-label"><i class="fa-solid fa-tags"></i> Tags:</span>
                <div class="tags-list">
                  $tagHtml
                </div>
              </div>

              <div class="post-share-section">
                <h4 class="share-title">Found this insightful? Share with your network:</h4>
                <div class="share-buttons">
                  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://amitkrshukla.github.io/articles/$artSlug/" target="_blank" rel="noopener noreferrer" class="btn-share btn-linkedin">
                    <i class="fa-brands fa-linkedin"></i> LinkedIn
                  </a>
                  <a href="mailto:?subject=$artTitle&body=Read this article by Amit Kumar Shukla: https://amitkrshukla.github.io/articles/$artSlug/" class="btn-share btn-email">
                    <i class="fa-solid fa-envelope"></i> Email
                  </a>
                </div>
              </div>

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

$(Get-HtmlFooter "../..")
  </div>

$(Get-HtmlSearchModal)

  <script src="../../assets/js/main.js"></script>
  <script src="../../assets/js/search.js"></script>
</body>
</html>
"@
        [System.IO.File]::WriteAllText($artFile, $newArtHtml, [System.Text.Encoding]::UTF8)
        Write-Host "   Scaffolded new article: articles/$artSlug/index.html" -ForegroundColor Yellow
    } else {
        Write-Host "   Article exists: articles/$artSlug/index.html" -ForegroundColor DarkGreen
    }
}

# ------------------------------------------------------------------------------
# 8. Generate search.json for live modal search
# ------------------------------------------------------------------------------
Write-Host "`n-> Generating search.json index..." -ForegroundColor Cyan

$searchList = @()
foreach ($a in $articles) {
    $cat = Get-CategoryObj $a.category
    $catName = if ($cat) { $cat.name } else { $a.category }

    $searchList += [ordered]@{
        title = $a.title
        url = "/articles/$($a.slug)/"
        date = $a.display_date
        category = $catName
        tags = @($a.tags)
        description = $a.description
    }
}

$searchJson = $searchList | ConvertTo-Json -Depth 5
$searchJsonPath = Join-Path $PSScriptRoot "search.json"
[System.IO.File]::WriteAllText($searchJsonPath, $searchJson, [System.Text.Encoding]::UTF8)
Write-Host "   Generated search.json ($($searchList.Count) indexed items)." -ForegroundColor DarkGreen

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host " Site build completed successfully! " -ForegroundColor Cyan
Write-Host " Categories: $($categories.Count) | Articles: $($articles.Count)" -ForegroundColor Green
Write-Host " Run .\preview.ps1 to preview the live site." -ForegroundColor Yellow
Write-Host "========================================================`n" -ForegroundColor Green
