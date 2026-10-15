# Quick Publishing Guide for Amit Kumar Shukla

Publishing a new article on your GitHub Pages site is designed to be frictionless and straightforward. Follow these steps:

---

## 🚀 How to Publish a New Article in 3 Steps

### Step 1: Create a Markdown File in `_posts/`
Name your file using the standard date-slug format:
```text
_posts/YYYY-MM-DD-your-article-title.md
```
*Example:* `_posts/2026-11-05-mastering-virtual-threads-java-21.md`

### Step 2: Add Front Matter Metadata
Paste this block at the top of your markdown file:

```yaml
---
layout: post
title: "Mastering Virtual Threads & Structured Concurrency in Java 21"
date: 2026-11-05 10:00:00 -0700
categories: [Java, Architecture]
tags: [Java 21, Virtual Threads, Project Loom, Concurrency, High Throughput]
description: "How Project Loom and Virtual Threads redefine concurrency in high-throughput enterprise Java services."
read_time: 7
---
```

#### Field Explanations:
| Field | Description | Example |
| :--- | :--- | :--- |
| `layout` | Keep as `post` | `post` |
| `title` | The full title of your article | `"Mastering Virtual Threads in Java 21"` |
| `date` | Publication date and time | `2026-11-05 10:00:00 -0700` |
| `categories` | 1 or 2 main categories (see list below) | `[Java, Architecture]` |
| `tags` | Keywords for search & filtering | `[Java 21, Concurrency, Spring]` |
| `description` | 1-2 sentence summary (used for cards, SEO, and search) | `"Deep dive into JVM virtual threads..."` |
| `read_time` | Estimated minutes to read | `7` |

---

### Step 3: Write Your Content in Markdown
Write your article using standard Markdown. Code blocks, callouts, tables, and lists are automatically styled.

#### Writing Code Blocks with Syntax Highlighting:
Use triple backticks followed by the language (`java`, `xml`, `yaml`, `json`, `sql`, `bash`):

````markdown
```java
public record TransferRequest(
    String sourceAccountId,
    String destinationAccountId,
    BigDecimal amount
) {}
```
````

#### Adding Alerts & Callouts:
```markdown
> [!NOTE]
> Virtual threads do not replace OS threads for CPU-bound computations; they excel at high-volume I/O-bound tasks.

> [!TIP]
> Use `Executors.newVirtualThreadPerTaskExecutor()` in Java 21 for immediate gains on non-blocking HTTP clients.
```

---

## 🏷️ Pre-Configured Categories

The website has pre-configured categories defined in `_data/categories.yml`:

| Category Name | Slug | Primary Focus |
| :--- | :--- | :--- |
| **Java Core & Modern APIs** | `java` | Java 17/21+, Virtual Threads (Loom), Memory & GC |
| **Spring Boot & Cloud** | `spring` | Spring Boot 3, Spring Cloud, Spring Data |
| **Reactive & Event-Driven** | `reactive` | Spring WebFlux, Project Reactor, Kafka, IBM MQ |
| **Cloud & Kubernetes** | `cloud` | AWS, Kubernetes (KCNA), Docker, Microservices |
| **Enterprise Architecture & DDD** | `architecture` | Domain-Driven Design, OpenAPI Contracts, System Design |
| **Security & Observability** | `security-observability` | JWT, RBAC, Splunk, AppDynamics, Kibana, Jenkins CI/CD |

*Tip:* You can also add any new custom category anytime by adding an entry in `_data/categories.yml`!

---

## 📄 Updating Your Resume & Details

### 1. Update the Web Resume:
Open `resume/index.html` and update any work experience, responsibilities, or skills.

### 2. Update the Downloadable PDF:
Replace `assets/AmitShukla_Resume_SeniorDigitalArchitect.pdf` with your latest PDF file using the same filename.

### 3. Update Contact & Social Details:
Open `_config.yml` to update email, phone, LinkedIn URL, location, or bio. Changes will automatically update across the entire site (header, footer, home hero, and about page).

---

## 🌐 Publishing to GitHub

When you commit and push to your `main` branch on GitHub:
1. GitHub Pages immediately detects the changes.
2. The site rebuilds automatically in less than 60 seconds.
3. Your new article appears on the homepage, category list, search index, and RSS feed!
