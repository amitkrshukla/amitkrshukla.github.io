# Configuration & Publishing Guide for Amit Kumar Shukla

Your website is fully **configuration-driven** using YAML files in `_data/`. Every category and article has its **own dedicated HTML file**, and everything stays in sync automatically.

---

## 📁 Configuration Files Overview

| File | Purpose |
| :--- | :--- |
| `_data/categories.yml` | Add, edit, or reorder article categories and their icons/descriptions. |
| `_data/articles.yml` | Add, edit, or configure article titles, category mappings, tags, and summaries. |
| `build.ps1` | Reads both YAML files and builds/updates all HTML pages & search index in seconds. |
| `preview.ps1` | Runs `build.ps1` automatically and launches the local preview at `http://localhost:4000/`. |
| `new-article.ps1` | Interactive assistant to scaffold a new article and update `_data/articles.yml`. |

---

## 🏷️ 1. How to Add or Edit Categories

Open `_data/categories.yml`. Each category is defined with 5 properties:

```yaml
- name: "Artificial Intelligence & LLMs"
  slug: "ai-llms"
  description: "Enterprise GenAI architectures, LangChain4j, RAG systems, and LLM integrations with Spring Boot."
  icon: "🤖"
  badge_color: "#8338ec"
```

### What happens when you run `.\build.ps1`:
1. A **dedicated category page** is automatically generated:
   - `categories/ai-llms/index.html`
   - Displays the category hero banner, icon, description, total article count, and cards for all articles in that category.
2. The **master categories directory** (`categories/index.html`) is updated with the new category section and jump navigation.
3. The **Home page** (`index.html`) automatically updates:
   - Adds the new category card in the **Knowledge Base by Technology** section linking to `categories/ai-llms/`.
   - Adds a filter button in the **Featured Articles** filter bar.
4. The **Articles catalog** (`articles/index.html`) adds the new category filter button.

---

## 📝 2. How to Add or Edit Articles

### Method A: Edit `_data/articles.yml` Directly
Open `_data/articles.yml` and add a new block:

```yaml
- slug: "mastering-java-21-virtual-threads"
  title: "Mastering Virtual Threads & Structured Concurrency in Java 21"
  category: "java"
  categories:
    - "java"
    - "spring"
  date: "2026-11-05"
  display_date: "November 05, 2026"
  read_time: "7 min read"
  tags:
    - "Java21"
    - "VirtualThreads"
    - "ProjectLoom"
    - "Concurrency"
  description: "How Project Loom and Virtual Threads redefine concurrency in high-throughput enterprise Java services."
  featured: true
```

Then run in PowerShell:
```powershell
.\build.ps1
```
The script will automatically create `articles/mastering-java-21-virtual-threads/index.html` with:
- Full header, theme switcher, search trigger
- Breadcrumbs linking to its category page (`../../categories/java/`)
- Title, category badge, publication date, reading time
- Author bar (Amit Kumar Shukla, Senior Digital Architect)
- Content template ready for you to add your paragraphs and code blocks
- Tags, social sharing buttons, author bio box, and footer

### Method B: Use the Interactive Script
Run in PowerShell:
```powershell
.\new-article.ps1
```
Follow the prompts for Title, Category, Summary, and Tags. It will append the entry to `_data/articles.yml` and run `build.ps1` for you in one step!

---

## 📄 3. Dedicated HTML Pages Structure

Each category and article has its own physical HTML page on the filesystem:

```text
categories/
├── index.html                    # Master directory of all categories
├── java/index.html               # Dedicated page for Java Core & Modern APIs
├── spring/index.html             # Dedicated page for Spring Boot & Cloud
├── reactive/index.html           # Dedicated page for Reactive & Event-Driven
├── cloud/index.html              # Dedicated page for Cloud & Kubernetes
├── architecture/index.html       # Dedicated page for Enterprise Architecture & DDD
└── security-observability/index.html # Dedicated page for Security & Observability

articles/
├── index.html                    # Searchable & filterable catalog of all articles
├── securing-cloud-native-java-microservices-jwt-and-zero-trust/index.html
├── event-driven-architecture-with-kafka-and-idempotent-consumers/index.html
├── enterprise-domain-driven-design-and-openapi-contracts/index.html
└── building-high-throughput-reactive-microservices-spring-webflux/index.html
```

---

## 💻 4. Local Testing with `preview.ps1`

Run in PowerShell:
```powershell
.\preview.ps1
```
- It automatically runs `build.ps1` to synchronize all YAML changes into HTML.
- It starts the local HTTP server at `http://localhost:4000/`.
- It opens your default browser directly to the Home page.
- Press `Ctrl + C` in PowerShell to stop the server.

---

## 🌐 5. Deploying to GitHub Pages

Once you've previewed your changes locally:

```bash
git add .
git commit -m "Add new category and articles"
git push origin main
```

GitHub Actions will deploy your changes directly to **https://amitkrshukla.github.io** within seconds!
