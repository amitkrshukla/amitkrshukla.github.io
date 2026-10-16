# Amit Kumar Shukla — Technical Blog & Digital Architecture Portfolio

A modern, responsive, high-performance static website and technical architecture blog designed for **Amit Kumar Shukla** (Senior Digital Architect), optimized for zero-maintenance hosting on **GitHub Pages** (`amitkrshukla.github.io`).

---

## 🌟 Key Architectural Features

- **Ready for GitHub Pages:** Pure static HTML/CSS/JS architecture with `.nojekyll` and GitHub Actions deployment workflow. No Ruby or npm required—deploy directly to GitHub Pages with instant page loads.
- **Modern Java & Enterprise Focus:** Pre-configured topics for Java 17/21, Spring Boot 3, Spring WebFlux, Apache Kafka, AWS, Kubernetes (KCNA), and Domain-Driven Design (DDD).
- **Fast Content Publishing:** Publish a new article in seconds using `.\new-article.ps1` or by creating a new article folder under `articles/`.
- **Intuitive Category Traversal on Home Page:**
  - 6 prominent technology category cards with icons, descriptions, and article count badges.
  - Interactive category filter buttons right on the home page for instant filtering without reloading.
  - Quick keyword search bar on both Home and Articles catalog pages.
  - Dedicated `/categories/` topic index with anchor jump pills.
  - Instant client-side search modal (<kbd>Ctrl + K</kbd>) across titles, tags, and content.
- **Interactive Resume & PDF Access:**
  - Full executive resume page at `/resume/` with professional summary, core competencies matrix, work history (Infinite, Cognizant, HSBC, Cybage), certifications (Google GenAI Leader, KCNA, Scrum Master), and education.
  - Direct "Download PDF" links on the Home hero, navbar, and resume toolbar pointing directly to `AmitShukla_Resume_SeniorDigitalArchitect.pdf`.
  - Built-in print stylesheet for clean, professional paper/PDF printing (`window.print()`).
- **Modern UI & Aesthetics:**
  - Architectural Dark & Light mode toggle with automatic OS preference detection and persistent local storage.
  - Syntax highlighting for Java, XML, YAML, JSON, and Bash.
  - One-click code snippet copy buttons.
  - Sticky header with glassmorphism blur and smooth responsive mobile navigation.
  - SEO meta tags, OpenGraph social cards, and RSS feed support.

---

## 📂 Project Structure

├── _data/
│   ├── categories.yml        # Configure categories: icons, names, descriptions & slugs
│   └── articles.yml          # Configure articles: titles, category tags, metadata & summaries
├── build.ps1                 # Static site generator: compiles YAML configs into HTML pages
├── preview.ps1               # Local preview server for Windows: runs build.ps1 & opens browser
├── new-article.ps1           # Interactive article scaffolding assistant
├── index.html                # Home page with hero, stats, category browser & latest articles
├── .nojekyll                 # Bypasses Jekyll on GitHub Pages to serve static files instantly
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Pages automated static deployment workflow
├── assets/
│   ├── css/
│   │   ├── style.css         # Modern responsive CSS, Dark/Light mode, print styles
│   │   └── syntax.css        # Syntax highlighting theme
│   ├── js/
│   │   ├── main.js           # Theme toggle, mobile menu, code copy, TOC
│   │   └── search.js         # Instant client-side search engine
│   ├── images/
│   │   ├── avatar.svg        # Vector profile avatar
│   │   └── favicon.svg       # Brand icon
│   └── AmitShukla_Resume_SeniorDigitalArchitect.pdf  # Downloadable resume PDF
├── articles/
│   ├── index.html            # All articles catalog with real-time category & keyword filter
│   ├── securing-cloud-native-java-microservices-jwt-and-zero-trust/index.html
│   ├── event-driven-architecture-with-kafka-and-idempotent-consumers/index.html
│   ├── enterprise-domain-driven-design-and-openapi-contracts/index.html
│   └── building-high-throughput-reactive-microservices-spring-webflux/index.html
├── categories/
│   ├── index.html            # Master category directory
│   ├── java/index.html       # Dedicated category HTML page for Java Core
│   ├── spring/index.html     # Dedicated category HTML page for Spring Boot
│   ├── reactive/index.html   # Dedicated category HTML page for Reactive Systems
│   ├── cloud/index.html      # Dedicated category HTML page for Cloud & K8s
│   ├── architecture/index.html # Dedicated category HTML page for Architecture & DDD
│   └── security-observability/index.html # Dedicated category HTML page for Security
├── resume/
│   └── index.html            # Dedicated interactive web resume & printable profile
├── about/
│   └── index.html            # Author bio, architectural pillars & tech spectrum
├── search.json               # Pre-indexed search data for instant modal search
├── 404.html                  # Custom 404 error page
├── PUBLISHING_GUIDE.md       # Step-by-step configuration & publishing instructions
└── README.md
```

---

## 💻 Local Preview on Windows

To preview your site locally on Windows without installing Ruby, Node, or gems:

1. Open PowerShell in this folder:
   ```powershell
   .\preview.ps1
   ```
2. Your default web browser will automatically open at `http://localhost:4000/`.
3. Press `Ctrl + C` in PowerShell whenever you want to stop the server.

---

## 📝 Creating a New Article

To write a new article:
```powershell
.\new-article.ps1
```
Follow the prompt for title, category, tags, and summary. It will create `articles/<slug>/index.html` and update `search.json` automatically.

Refer to [PUBLISHING_GUIDE.md](file:///c:/Amit/work/amitkrshukla/PUBLISHING_GUIDE.md) for more details.

---

## 🚀 Publishing to GitHub Pages

1. Commit and push your code to GitHub:
   ```bash
   git add .
   git commit -m "Update site and articles"
   git push origin main
   ```
2. In your GitHub repository:
   - Go to **Settings** &rarr; **Pages**.
   - Under **Build and deployment > Source**, ensure **GitHub Actions** is selected (it will use `.github/workflows/deploy.yml`).
   - Your site will be live at `https://amitkrshukla.github.io/`.
