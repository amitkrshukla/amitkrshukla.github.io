# Amit Kumar Shukla — Technical Blog & Digital Architecture Portfolio

A modern, responsive, high-performance static website and technical blog designed for **Amit Kumar Shukla** (Senior Digital Architect), optimized for zero-maintenance hosting on **GitHub Pages**.

---

## 🌟 Key Features

- **Built for GitHub Pages:** Native Jekyll architecture. No complex local runtime or npm dependencies required—push to GitHub and it deploys automatically.
- **Java & Distributed Systems Focus:** Pre-configured topics for Java 17/21, Spring Boot 3, Spring WebFlux, Apache Kafka, AWS, Kubernetes, and Domain-Driven Design (DDD).
- **Fast Content Publishing:** Publish a new article in under 2 minutes by dropping a standard `.md` file into `_posts/`.
- **Comprehensive Topic Categorization:**
  - Dynamic category index with article count badges.
  - Interactive keyword/tag filter on the articles index.
  - Instant client-side search modal (<kbd>Ctrl + K</kbd> or <kbd>/</kbd>) across titles, tags, and content.
- **Interactive Resume & PDF Access:**
  - Dedicated `/resume/` page featuring full executive summary, skills matrix, chronological work history (Infinite, Cognizant, HSBC, Cybage), certifications (Google Gen AI Leader, KCNA, Scrum Master), and education.
  - One-click "Download PDF" button linking directly to `assets/AmitShukla_Resume_SeniorDigitalArchitect.pdf`.
  - Built-in print stylesheet for clean, professional paper/PDF printing.
- **Modern UI & Developer Experience:**
  - Dark & Light mode toggle with automatic OS preference detection and persistence.
  - Syntax highlighting for Java, XML, YAML, JSON, and Bash.
  - One-click code snippet copy buttons.
  - Automatic sticky Table of Contents (TOC) with ScrollSpy for long-form technical deep-dives.
  - SEO meta tags, OpenGraph social cards, and RSS feed (`feed.xml`).

---

## 📂 Project Structure

```text
├── _config.yml               # Site metadata, author information, social links & plugins
├── _data/
│   ├── categories.yml        # Topic definitions, icons, descriptions & slugs
│   └── navigation.yml        # Navigation menu items
├── _layouts/
│   ├── default.html          # Base layout (HTML shell, header, footer, search modal)
│   ├── home.html             # Homepage layout (hero, metrics, categories, recent posts)
│   ├── post.html             # Technical article layout (TOC, author card, share buttons)
│   └── page.html             # Standard page layout
├── _includes/
│   ├── head.html             # Fonts (Inter & Fira Code), SEO, styles
│   ├── header.html           # Sticky navbar, search trigger, theme switcher
│   ├── footer.html           # Footer, social links, topics & copyright
│   ├── post-card.html        # Reusable card component for post listings
│   └── search.html           # Instant modal search dialog
├── _posts/                   # Articles repository (drop new Markdown files here)
│   ├── 2026-10-01-building-high-throughput-reactive-microservices-spring-webflux.md
│   ├── 2026-09-15-enterprise-domain-driven-design-and-openapi-contracts.md
│   ├── 2026-08-20-event-driven-architecture-with-kafka-and-idempotent-consumers.md
│   └── 2026-07-10-securing-cloud-native-java-microservices-jwt-and-zero-trust.md
├── assets/
│   ├── css/
│   │   ├── style.css         # Modern responsive CSS, Dark/Light mode, print styles
│   │   └── syntax.css        # Syntax highlighting theme
│   ├── js/
│   │   ├── main.js           # Theme toggle, TOC generator, code copy, mobile menu
│   │   └── search.js         # Instant client-side search engine
│   ├── images/
│   │   ├── avatar.svg        # Vector profile avatar
│   │   └── favicon.svg       # Brand icon
│   └── AmitShukla_Resume_SeniorDigitalArchitect.pdf  # Downloadable resume PDF
├── articles/
│   └── index.html            # All articles page with real-time category filter
├── categories/
│   └── index.html            # Category index page
├── resume/
│   └── index.html            # Dedicated interactive resume page
├── about/
│   └── index.html            # Author bio & architectural philosophy
├── search.json               # JSON search feed
├── 404.html                  # Custom 404 page
├── preview.ps1               # Zero-dependency local preview server for Windows PowerShell
├── PUBLISHING_GUIDE.md       # Step-by-step publishing instructions
└── README.md
```

---

## 🚀 Step-by-Step: Hosting on GitHub Pages

### Method 1: Using GitHub Web (Quickest & No Git Installation Required)

1. **Log in to GitHub:** Go to [github.com](https://github.com).
2. **Create a New Repository:**
   - Click the **+** icon in the top right &rarr; **New repository**.
   - If you want the site URL to be `https://<your-username>.github.io`:
     - Name the repository: `<your-username>.github.io` (e.g., `amit-kr-shukla.github.io`).
   - If you want it as a project site (e.g., `https://<your-username>.github.io/tech-blog`):
     - Name it `tech-blog` and set `baseurl: "/tech-blog"` in `_config.yml`.
   - Set visibility to **Public**.
3. **Upload the Files:**
   - In the repository, click **Upload files** and drag the contents of this folder into GitHub.
   - Commit the files to the `main` branch.
4. **Enable GitHub Pages:**
   - In your repository, click **Settings** &rarr; **Pages** (in the left sidebar).
   - Under **Build and deployment > Source**:
     - Choose **Deploy from a branch**.
     - Select Branch: `main`, Folder: `/ (root)`.
     - Click **Save**.
5. **Done!** In 1-2 minutes, GitHub Pages will deploy your site and provide your live URL.

---

### Method 2: Using Git Command Line

If you have Git installed:

```bash
cd c:\Amit\work\gemini

# Initialize git repository
git init -b main

# Add files and commit
git add .
git commit -m "Initial commit: Amit Kumar Shukla Technical Blog & Portfolio"

# Link to your remote GitHub repository
git remote add origin https://github.com/<your-username>/<your-username>.github.io.git

# Push to GitHub
git push -u origin main
```

---

## 💻 Local Testing on Windows

To preview your site locally on Windows without installing Ruby or Node:

1. Open PowerShell in this folder (`c:\Amit\work\gemini`).
2. Run the included preview script:
   ```powershell
   .\preview.ps1
   ```
3. Your default web browser will open at `http://localhost:4000/resume/`.
4. Press `Ctrl + C` in PowerShell whenever you want to stop the server.

---

## 📝 Writing New Content

Refer to [PUBLISHING_GUIDE.md](file:///c:/Amit/work/gemini/PUBLISHING_GUIDE.md) for complete details on creating new articles, configuring front matter, and code highlighting.
