# Quick Publishing Guide for Amit Kumar Shukla

Publishing a new article on your GitHub Pages site is designed to be frictionless and straightforward.

---

## 🚀 How to Publish a New Article

### Method 1: Automated Scaffold (Recommended)
Open PowerShell in the project directory and run:
```powershell
.\new-article.ps1
```
The script will prompt you for:
1. **Title** (e.g. `Mastering Java 21 Virtual Threads & Structured Concurrency`)
2. **Category** (select from the 6 pre-configured architecture categories)
3. **Summary** (1-2 sentence excerpt used for search and cards)
4. **Tags** (e.g. `Java 21, Loom, Concurrency, SpringBoot`)

The script will automatically:
- Create `articles/<slug>/index.html` with all formatting, breadcrumbs, tags, and author card.
- Automatically update `search.json` so your new article is instantly searchable!

Then simply open `articles/<slug>/index.html` in your editor, add your paragraphs and code snippets, and save!

---

### Method 2: Manual Creation
1. Create a folder inside `articles/` with your article slug:
   ```text
   articles/my-new-article-title/index.html
   ```
2. Copy any existing article file (e.g. `articles/securing-cloud-native-java-microservices-jwt-and-zero-trust/index.html`) as a starting template.
3. Update the Title, Category tag, Date, and content.
4. Add an entry to `search.json` with the title, URL, date, category, tags, and description.

---

## 💻 Previewing Locally

To test your site locally in your web browser:
```powershell
.\preview.ps1
```
This starts a local lightweight preview server at `http://localhost:4000/` and automatically opens the Home page in your default browser.
- All CSS styles, dark/light mode toggle, category filters, and search modal will be 100% active and functional.
- Press `Ctrl + C` in the PowerShell terminal whenever you want to stop the preview server.

---

## 🌐 Publishing to GitHub Pages

Once you're satisfied with your changes locally, deploy them to GitHub Pages with standard Git commands:

```bash
git add .
git commit -m "Publish new article and update site content"
git push origin main
```

Your GitHub Actions workflow (`.github/workflows/deploy.yml`) will automatically deploy the static content directly to **https://amitkrshukla.github.io** within seconds!

---

## 🏷️ Pre-Configured Categories

The website has 6 pre-configured categories:

| Category Name | Slug | Primary Focus |
| :--- | :--- | :--- |
| **Java Core & Modern APIs** | `java` | Java 17/21+, Virtual Threads (Loom), Memory & GC |
| **Spring Boot & Cloud** | `spring` | Spring Boot 3, Spring Cloud, Spring Data |
| **Reactive & Event-Driven** | `reactive` | Spring WebFlux, Project Reactor, Kafka, IBM MQ |
| **Cloud & Kubernetes** | `cloud` | AWS, Kubernetes (KCNA), Docker, Microservices |
| **Enterprise Architecture & DDD** | `architecture` | Domain-Driven Design, OpenAPI Contracts, System Design |
| **Security & Observability** | `security-observability` | JWT, RBAC, Splunk, AppDynamics, Kibana, Jenkins CI/CD |

---

## 📄 Updating Your Resume & Profile Details

### 1. Update the Web Resume:
Open `resume/index.html` and update any work experience, responsibilities, or skills.

### 2. Update the Downloadable PDF:
Replace `AmitShukla_Resume_SeniorDigitalArchitect.pdf` (and `assets/AmitShukla_Resume_SeniorDigitalArchitect.pdf`) with your latest PDF file using the same filename.

### 3. Update Contact & Social Details:
Open `_config.yml` or the header/footer of `index.html` to update email, phone, LinkedIn URL, or bio.
