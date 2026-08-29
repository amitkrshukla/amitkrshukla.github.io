import base64

# Read base64 fallback string if needed
with open('profile_unblurred_b64.txt', 'r') as f:
    img_b64 = f.read().strip()

html_code = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Amit Kumar Shukla - Solution Architect & Senior Technical Lead</title>
  <meta name="description" content="Executive Resume of Amit Kumar Shukla - Senior Technical Lead & Solution Architect with 20+ years of experience." />
  
  <!-- Modern Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- html2pdf Library for PDF Generation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

  <style>
    :root {{
      --bg-body: #090d16;
      --bg-surface: #111827;
      --bg-card: #1f293d;
      --bg-card-hover: #26334d;
      --bg-accent-subtle: rgba(59, 130, 246, 0.12);
      
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      
      --accent-blue: #3b82f6;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-purple: #8b5cf6;
      --accent-amber: #f59e0b;
      
      --border-color: #334155;
      --border-light: #1e293b;
      
      --gradient-brand: linear-gradient(135deg, #06b6d4 0%, #3b82f6 50%, #8b5cf6 100%);
      --gradient-card: linear-gradient(180deg, rgba(31,41,61,0.8) 0%, rgba(17,24,39,0.9) 100%);
      
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 14px rgba(0,0,0,0.4);
      --shadow-lg: 0 10px 30px rgba(0,0,0,0.5);
      
      --chip-bg: rgba(59, 130, 246, 0.12);
      --chip-text: #60a5fa;
      --chip-border: rgba(96, 165, 250, 0.25);
      
      --sidebar-width: 310px;
    }}

    [data-theme="light"] {{
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --bg-accent-subtle: #eff6ff;
      
      --text-primary: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      
      --accent-blue: #2563eb;
      --accent-cyan: #0891b2;
      --accent-emerald: #059669;
      --accent-purple: #7c3aed;
      --accent-amber: #d97706;
      
      --border-color: #cbd5e1;
      --border-light: #e2e8f0;
      
      --gradient-brand: linear-gradient(135deg, #0891b2 0%, #2563eb 50%, #7c3aed 100%);
      --gradient-card: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 8px rgba(0,0,0,0.07);
      --shadow-lg: 0 10px 25px rgba(0,0,0,0.1);
      
      --chip-bg: #eff6ff;
      --chip-text: #1d4ed8;
      --chip-border: #bfdbfe;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-primary);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Outfit', sans-serif;
    }}

    code, .font-mono {{
      font-family: 'Fira Code', monospace;
    }}

    /* Top Action Bar */
    .top-bar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}

    .top-bar-inner {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
    }}

    .brand-logo {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
      text-decoration: none;
      flex-shrink: 0;
    }}

    .brand-avatar-sm {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--accent-blue);
    }}

    .brand-name {{
      font-size: 1.1rem;
      font-weight: 800;
      background: var(--gradient-brand);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .search-box {{
      position: relative;
      flex: 1;
      max-width: 340px;
    }}

    .search-input {{
      width: 100%;
      padding: 0.45rem 0.85rem 0.45rem 2.2rem;
      border-radius: 20px;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-primary);
      font-size: 0.85rem;
      outline: none;
    }}

    .search-icon {{
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      color: var(--text-muted);
    }}

    .action-btns {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-shrink: 0;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-primary);
      text-decoration: none;
      min-height: 38px;
    }}

    .btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-blue);
    }}

    .btn-primary {{
      background: var(--gradient-brand);
      color: #ffffff;
      border: none;
    }}

    /* Mobile Nav Bar Strip */
    .mobile-nav-strip {{
      display: none;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      overflow-x: auto;
      white-space: nowrap;
      padding: 0.5rem 1rem;
    }}
    
    .mobile-nav-chip {{
      display: inline-block;
      padding: 0.35rem 0.85rem;
      margin-right: 0.4rem;
      border-radius: 16px;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      text-decoration: none;
    }}
    
    .mobile-nav-chip.active {{
      background: var(--gradient-brand);
      color: #ffffff;
      border-color: transparent;
    }}

    /* Main App Layout */
    .app-layout {{
      max-width: 1400px;
      margin: 1.5rem auto;
      padding: 0 1.25rem;
      display: grid;
      grid-template-columns: var(--sidebar-width) 1fr;
      gap: 1.75rem;
      align-items: start;
    }}

    /* Sidebar Navigation */
    .sidebar {{
      position: sticky;
      top: 4.5rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.5rem 1.25rem;
      box-shadow: var(--shadow-md);
    }}

    .profile-header-card {{
      text-align: center;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 1.25rem;
    }}

    .profile-photo-lg {{
      width: 120px;
      height: 120px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid var(--accent-blue);
      box-shadow: var(--shadow-md);
      margin: 0 auto 0.85rem auto;
      display: block;
    }}

    .profile-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--text-primary);
    }}

    .profile-title {{
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--accent-cyan);
      margin-top: 0.25rem;
    }}

    .contact-links-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      font-size: 0.85rem;
      margin-top: 1rem;
    }}

    .contact-links-list li {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-secondary);
      word-break: break-word;
    }}

    .contact-links-list a {{
      color: var(--accent-blue);
      text-decoration: none;
      font-weight: 500;
    }}

    .toc-nav {{
      margin-top: 1.25rem;
    }}

    .toc-nav-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      margin-bottom: 0.6rem;
    }}

    .toc-links {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .toc-links a {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 0.75rem;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-secondary);
      text-decoration: none;
    }}

    .toc-links a:hover, .toc-links a.active {{
      background: var(--bg-accent-subtle);
      color: var(--accent-blue);
      font-weight: 600;
    }}

    /* Main Content Area */
    .main-content {{
      display: flex;
      flex-direction: column;
      gap: 1.75rem;
    }}

    /* Hero Summary & Key Metrics Banner */
    .hero-banner {{
      background: var(--gradient-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.75rem;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }}

    .hero-banner::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--gradient-brand);
    }}

    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 0.85rem;
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-color);
    }}

    .metric-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 0.85rem;
      text-align: center;
    }}

    .metric-value {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--accent-blue);
      font-family: 'Outfit', sans-serif;
    }}

    .metric-label {{
      font-size: 0.75rem;
      color: var(--text-secondary);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 0.2rem;
    }}

    /* Section Cards */
    .content-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.75rem;
      box-shadow: var(--shadow-md);
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--border-color);
    }}

    .card-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .card-title svg {{
      width: 22px;
      height: 22px;
      color: var(--accent-blue);
    }}

    /* Executive Summary Text */
    .summary-p {{
      margin-bottom: 1rem;
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.7;
    }}
    .summary-p:last-child {{
      margin-bottom: 0;
    }}

    /* Skills Grid & Filters */
    .skill-filters {{
      display: flex;
      gap: 0.45rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }}

    .skill-filter-btn {{
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
    }}

    .skill-filter-btn.active, .skill-filter-btn:hover {{
      background: var(--gradient-brand);
      color: #ffffff;
      border-color: transparent;
    }}

    .skills-category-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 1.1rem;
    }}

    .skill-cat-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.1rem;
    }}

    .skill-cat-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 0.75rem;
    }}

    .skill-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }}

    .skill-pill {{
      background: var(--chip-bg);
      color: var(--chip-text);
      border: 1px solid var(--chip-border);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 500;
    }}

    /* Experience Timeline */
    .timeline-wrapper {{
      position: relative;
      padding-left: 1.25rem;
    }}

    .timeline-wrapper::before {{
      content: '';
      position: absolute;
      left: 5px;
      top: 10px;
      bottom: 10px;
      width: 2px;
      background: var(--border-color);
    }}

    .role-card {{
      position: relative;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.4rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }}

    .role-card::before {{
      content: '';
      position: absolute;
      left: -1.68rem;
      top: 1.5rem;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--accent-blue);
      border: 2px solid var(--bg-surface);
      box-shadow: 0 0 0 2px var(--accent-blue);
    }}

    .role-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-bottom: 0.65rem;
    }}

    .role-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .company-name {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--accent-blue);
    }}

    .role-dates {{
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.2rem 0.65rem;
      background: var(--chip-bg);
      color: var(--chip-text);
      border-radius: 12px;
      border: 1px solid var(--chip-border);
    }}

    .project-banner {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent-cyan);
      margin: 0.5rem 0;
      padding: 0.35rem 0.75rem;
      background: rgba(6, 182, 212, 0.08);
      border-left: 3px solid var(--accent-cyan);
      border-radius: 0 6px 6px 0;
    }}

    .role-details p {{
      color: var(--text-secondary);
      font-size: 0.92rem;
      line-height: 1.65;
      margin-bottom: 0.55rem;
    }}

    .role-details ul {{
      list-style-type: none;
      margin-top: 0.55rem;
      margin-bottom: 0.75rem;
    }}

    .role-details li {{
      position: relative;
      padding-left: 1.2rem;
      margin-bottom: 0.5rem;
      font-size: 0.91rem;
      color: var(--text-secondary);
      line-height: 1.6;
    }}

    .role-details li::before {{
      content: '▹';
      position: absolute;
      left: 0;
      color: var(--accent-blue);
      font-weight: bold;
    }}

    .customization-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 0.75rem 0.9rem;
      margin: 0.75rem 0;
    }}

    .customization-box-title {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--accent-amber);
      margin-bottom: 0.35rem;
    }}

    .role-tech-stack {{
      margin-top: 0.85rem;
      padding-top: 0.65rem;
      border-top: 1px solid var(--border-color);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.35rem;
    }}

    .tech-title {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-right: 0.25rem;
      text-transform: uppercase;
    }}

    /* Certifications Grid */
    .certs-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1rem;
    }}

    .cert-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .cert-icon-box {{
      width: 40px;
      height: 40px;
      border-radius: 8px;
      background: var(--chip-bg);
      color: var(--accent-blue);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      flex-shrink: 0;
    }}

    .cert-info h4 {{
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .cert-info p {{
      font-size: 0.8rem;
      color: var(--text-secondary);
    }}

    /* Education Grid */
    .edu-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
    }}

    .edu-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.1rem;
    }}

    .edu-degree {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .edu-inst {{
      font-size: 0.85rem;
      color: var(--accent-blue);
      margin-top: 0.2rem;
    }}

    .edu-year {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    /* Footer */
    footer {{
      text-align: center;
      padding: 2rem 1rem;
      color: var(--text-muted);
      font-size: 0.82rem;
      border-top: 1px solid var(--border-color);
      margin-top: 2.5rem;
    }}

    /* Responsive Breakpoints & Mobile Optimization */
    @media (max-width: 1024px) {{
      .app-layout {{
        grid-template-columns: 1fr;
        padding: 0 1rem;
        margin: 1rem auto;
      }}
      .sidebar {{
        position: relative;
        top: 0;
        margin-bottom: 1rem;
      }}
      .mobile-nav-strip {{
        display: block;
      }}
      .toc-nav {{
        display: none;
      }}
    }}

    @media (max-width: 768px) {{
      .top-bar-inner {{
        padding: 0.6rem 0.85rem;
        gap: 0.5rem;
      }}
      .brand-name {{
        font-size: 0.98rem;
      }}
      .search-box {{
        max-width: 160px;
      }}
      .btn {{
        padding: 0.4rem 0.6rem;
        font-size: 0.78rem;
      }}
      .btn-text-full {{
        display: none;
      }}
      .hero-banner, .content-card {{
        padding: 1.25rem;
      }}
      .metrics-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .role-card {{
        padding: 1.1rem;
      }}
    }}

    @media (max-width: 480px) {{
      .top-bar-inner {{
        flex-wrap: wrap;
      }}
      .search-box {{
        max-width: 100%;
        width: 100%;
        order: 3;
      }}
      .action-btns {{
        margin-left: auto;
      }}
      .metrics-grid {{
        grid-template-columns: 1fr;
      }}
      .skills-category-grid, .certs-grid, .edu-grid {{
        grid-template-columns: 1fr;
      }}
      .timeline-wrapper {{
        padding-left: 0.85rem;
      }}
      .role-card::before {{
        left: -1.28rem;
      }}
    }}

    /* Print Stylesheet */
    @media print {{
      @page {{
        margin: 10mm;
        size: letter;
      }}

      body {{
        background: #ffffff !important;
        color: #0f172a !important;
        font-size: 9.5pt;
      }}

      .top-bar, .mobile-nav-strip, .sidebar, .skill-filters, .btn {{
        display: none !important;
      }}

      .app-layout {{
        display: block !important;
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
      }}

      .content-card, .hero-banner, .role-card, .skill-cat-box, .cert-card, .edu-card, .metric-card {{
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: none !important;
      }}

      .hero-banner {{
        padding: 1rem !important;
        margin-bottom: 1rem !important;
      }}

      .role-card {{
        page-break-inside: avoid;
        margin-bottom: 1rem !important;
        padding: 1rem !important;
      }}

      .timeline-wrapper::before, .role-card::before {{
        display: none !important;
      }}

      .timeline-wrapper {{
        padding-left: 0 !important;
      }}

      .role-title {{
        color: #0f172a !important;
      }}

      .company-name {{
        color: #1d4ed8 !important;
      }}

      .project-banner {{
        background: #f1f5f9 !important;
        color: #0369a1 !important;
        border-left-color: #0284c7 !important;
      }}

      .skill-pill, .role-dates {{
        background: #f1f5f9 !important;
        color: #334155 !important;
        border: 1px solid #cbd5e1 !important;
      }}

      footer {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Action Bar -->
  <header class="top-bar">
    <div class="top-bar-inner">
      <a href="#" class="brand-logo">
        <img src="profile_unblurred.jpg" onerror="this.onerror=null; this.src='IMG_7611.JPG';" alt="Amit Kumar Shukla" class="brand-avatar-sm" />
        <span class="brand-name">Amit Kumar Shukla</span>
      </a>

      <!-- Real-time Search Box -->
      <div class="search-box">
        <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
        </svg>
        <input type="text" id="searchInput" class="search-input" placeholder="Search skills, projects..." onkeyup="performSearch()" />
      </div>

      <div class="action-btns">
        <button class="btn" id="themeToggle" aria-label="Toggle theme">
          <span id="themeIcon">🌙</span> <span id="themeText" class="btn-text-full">Dark</span>
        </button>
        <button class="btn btn-primary" id="downloadPdfBtn" onclick="downloadPDF()" aria-label="Download PDF">
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
          </svg>
          <span id="downloadPdfText" class="btn-text-full">Download PDF</span>
        </button>
        <button class="btn" onclick="window.print()" aria-label="Print resume">
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>
          </svg>
          <span class="btn-text-full">Print</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Sticky Mobile Navigation Strip -->
  <div class="mobile-nav-strip">
    <a href="#summary" class="mobile-nav-chip active">Summary</a>
    <a href="#skills" class="mobile-nav-chip">Skills</a>
    <a href="#experience" class="mobile-nav-chip">Experience</a>
    <a href="#certifications" class="mobile-nav-chip">Certs</a>
    <a href="#education" class="mobile-nav-chip">Education</a>
  </div>

  <!-- Main App Layout -->
  <div class="app-layout">

    <!-- Left Sticky Sidebar -->
    <aside class="sidebar">
      <div class="profile-header-card">
        <img src="profile_unblurred.jpg" onerror="this.onerror=null; this.src='IMG_7611.JPG';" alt="Amit Kumar Shukla" class="profile-photo-lg" />
        <h1 class="profile-name">Amit Kumar Shukla</h1>
        <div class="profile-title">Architect | Sr. Technical Lead</div>
      </div>

      <ul class="contact-links-list">
        <li>
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          Burnaby, BC, Canada
        </li>
        <li>
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h32a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5l9 6 9-6"/></svg>
          <a href="mailto:amit_kr_shukla@yahoo.com">amit_kr_shukla@yahoo.com</a>
        </li>
        <li>
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          <a href="tel:236-863-4703">236-863-4703</a>
        </li>
        <li>
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.64 1.64 0 1 0 0 3.28 1.64 1.64 0 0 0 0-3.28z"/></svg>
          <a href="https://linkedin.com/in/amit-kr-shukla" target="_blank">linkedin.com/in/amit-kr-shukla</a>
        </li>
      </ul>

      <!-- Table of Contents Navigation for Desktop -->
      <nav class="toc-nav">
        <div class="toc-nav-title">Navigation</div>
        <ul class="toc-links">
          <li><a href="#summary" class="active">Executive Summary</a></li>
          <li><a href="#skills">Technical Skills</a></li>
          <li><a href="#experience">Work Experience</a></li>
          <li><a href="#certifications">Certifications & Awards</a></li>
          <li><a href="#education">Education</a></li>
        </ul>
      </nav>
    </aside>

    <!-- Main Content Stream -->
    <main class="main-content" id="pdf-container">

      <!-- Executive Hero Banner -->
      <section class="hero-banner" id="summary">
        <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem;">Executive Summary</h2>
        <div class="summary-p">
          A results-driven <strong>Senior Technical Lead | Solution Architect | Cloud Technologist</strong> with <strong>20+ years of experience</strong> delivering enterprise-scale digital transformation initiatives across the financial services domain. Proven expertise in designing and leading the implementation of secure, resilient, and highly scalable multi-tier, cloud-native applications using Java, AWS, Microservices, SOA, APIs, and event-driven architectures.
        </div>
        <div class="summary-p">
          Experienced in translating complex business strategies into pragmatic technology solutions while leading cross-functional engineering teams through the full software delivery lifecycle using Agile, Scrum, and SAFe. Strong track record of modernizing legacy platforms, defining enterprise and solution architectures, and delivering high-quality solutions that improve customer experience, operational efficiency, scalability, and regulatory compliance.
        </div>
        <div class="summary-p">
          Passionate about leveraging AI-enabled development practices, Generative AI, intelligent automation, and cloud innovation to accelerate software delivery, improve engineering productivity, and build future-ready digital platforms. Recognized for engineering excellence, mentoring high-performing teams, influencing technology strategy, and building strong partnerships with business and executive stakeholders.
        </div>

        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-value">20+</div>
            <div class="metric-label">Years Experience</div>
          </div>
          <div class="metric-card">
            <div class="metric-value">Banking & FinTech</div>
            <div class="metric-label">Domain Mastery</div>
          </div>
          <div class="metric-card">
            <div class="metric-value">Cloud & AI</div>
            <div class="metric-label">AWS / GCP / GenAI</div>
          </div>
          <div class="metric-card">
            <div class="metric-value">400+</div>
            <div class="metric-label">APIs Unified</div>
          </div>
        </div>
      </section>

      <!-- Technical Skills Section -->
      <section class="content-card" id="skills">
        <div class="card-header">
          <h2 class="card-title">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
            Technical Skills & Core Competencies
          </h2>
        </div>

        <div class="skill-filters">
          <button class="skill-filter-btn active" onclick="filterSkills('all')">All Skills</button>
          <button class="skill-filter-btn" onclick="filterSkills('arch')">Architecture</button>
          <button class="skill-filter-btn" onclick="filterSkills('cloud')">Cloud & DevOps</button>
          <button class="skill-filter-btn" onclick="filterSkills('lang')">Languages & Frameworks</button>
          <button class="skill-filter-btn" onclick="filterSkills('db')">Databases & Messaging</button>
          <button class="skill-filter-btn" onclick="filterSkills('lead')">Leadership</button>
        </div>

        <div class="skills-category-grid">
          <div class="skill-cat-box" data-cat="arch">
            <div class="skill-cat-title">Architectural Paradigms</div>
            <div class="skill-pills">
              <span class="skill-pill">Domain-Driven Design (DDD)</span>
              <span class="skill-pill">Microservices Architecture</span>
              <span class="skill-pill">Service-Oriented Architecture (SOA)</span>
              <span class="skill-pill">Event-Driven Architecture</span>
              <span class="skill-pill">Test-Driven Development (TDD)</span>
              <span class="skill-pill">Behavior-Driven Development (BDD)</span>
              <span class="skill-pill">Open API Specifications</span>
              <span class="skill-pill">Enterprise Integration Patterns</span>
            </div>
          </div>

          <div class="skill-cat-box" data-cat="cloud">
            <div class="skill-cat-title">Cloud, DevOps & Tools</div>
            <div class="skill-pills">
              <span class="skill-pill">AWS (IAM, S3, CloudFront, EC2)</span>
              <span class="skill-pill">Google Cloud Platform (GCP)</span>
              <span class="skill-pill">Pivotal Cloud Foundry (PCF)</span>
              <span class="skill-pill">Kubernetes</span>
              <span class="skill-pill">Docker</span>
              <span class="skill-pill">Jenkins CI/CD</span>
              <span class="skill-pill">Git & GitLab</span>
              <span class="skill-pill">Splunk</span>
              <span class="skill-pill">Kibana</span>
              <span class="skill-pill">AppDynamics</span>
              <span class="skill-pill">JMeter</span>
              <span class="skill-pill">Swagger / OpenAPI</span>
            </div>
          </div>

          <div class="skill-cat-box" data-cat="lang">
            <div class="skill-cat-title">Languages & Frameworks</div>
            <div class="skill-pills">
              <span class="skill-pill">Java (8, 17 / J2EE)</span>
              <span class="skill-pill">Spring Boot</span>
              <span class="skill-pill">Spring Cloud</span>
              <span class="skill-pill">Spring MVC & Security</span>
              <span class="skill-pill">Spring Integration & JPA</span>
              <span class="skill-pill">Spring WebFlux</span>
              <span class="skill-pill">REST & SOAP Web Services</span>
              <span class="skill-pill">RxJava / Reactive Java</span>
              <span class="skill-pill">React.js</span>
              <span class="skill-pill">Next.js</span>
              <span class="skill-pill">Node.js</span>
              <span class="skill-pill">Angular</span>
              <span class="skill-pill">Hystrix</span>
              <span class="skill-pill">Adobe Experience Manager (AEM)</span>
            </div>
          </div>

          <div class="skill-cat-box" data-cat="db">
            <div class="skill-cat-title">Databases & Messaging</div>
            <div class="skill-pills">
              <span class="skill-pill">Apache Cassandra</span>
              <span class="skill-pill">PostgreSQL</span>
              <span class="skill-pill">IBM DB2</span>
              <span class="skill-pill">Apache Kafka</span>
              <span class="skill-pill">IBM MQ</span>
            </div>
          </div>

          <div class="skill-cat-box" data-cat="lead">
            <div class="skill-cat-title">Methodologies & Leadership</div>
            <div class="skill-pills">
              <span class="skill-pill">SAFe Agile Framework</span>
              <span class="skill-pill">Scrum & Kanban</span>
              <span class="skill-pill">Cross-Functional Leadership</span>
              <span class="skill-pill">Global Stakeholder Management</span>
              <span class="skill-pill">CI/CD Pipeline Governance</span>
              <span class="skill-pill">Technical Mentorship</span>
              <span class="skill-pill">Generative AI Integration</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Work Experience Section -->
      <section class="content-card" id="experience">
        <div class="card-header">
          <h2 class="card-title">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            Professional Experience
          </h2>
        </div>

        <div class="timeline-wrapper">

          <!-- Role 1 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Architect</h3>
                <div class="company-name">Infinite Computer Solutions (Canada) Ltd</div>
              </div>
              <span class="role-dates">Oct 2024 – Jul 2026</span>
            </div>
            <div class="project-banner">Key Project: Verizon | Value (Prepaid) Journey Enhancement</div>
            <div class="role-details">
              <p>This project is to enhance the Agent landing page to display the national offers so that they can create a cross-sell opportunity with the customer, connect the flow with the service onboarding journey, and send the customer an enrolment or offer details link via SMS or Email.</p>
              <ul>
                <li><strong>Architectural Scope:</strong> Managed the full API lifecycle across all layers for national offer displays and cross-sell customer journeys.</li>
                <li><strong>Leadership & Delivery:</strong> Collaborated closely with UX and frontend teams to establish robust API contracts that matched UX designs, successfully accelerating solution delivery from scratch to production within 3 months.</li>
                <li><strong>API Lifecycle & Governance:</strong> Managed the full API lifecycle across all layers and collaborated closely with the frontend team to establish API contracts that matched UX designs.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java 17/J2EE</span>
                <span class="skill-pill">AWS</span>
                <span class="skill-pill">Microservices</span>
                <span class="skill-pill">Spring Flux</span>
                <span class="skill-pill">Spring Core</span>
                <span class="skill-pill">Spring Boot</span>
                <span class="skill-pill">React</span>
                <span class="skill-pill">JUnit</span>
                <span class="skill-pill">Mockito</span>
                <span class="skill-pill">Jenkins</span>
                <span class="skill-pill">Kibana</span>
                <span class="skill-pill">GitLab</span>
                <span class="skill-pill">Agile</span>
                <span class="skill-pill">JIRA</span>
                <span class="skill-pill">BDD</span>
              </div>
            </div>
          </article>

          <!-- Role 2 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Architect</h3>
                <div class="company-name">Cognizant (Canada) Ltd</div>
              </div>
              <span class="role-dates">Mar 2024 – Oct 2024</span>
            </div>
            <div class="project-banner">Key Project: Verizon | Digital Sales Flow & Postpaid Journey Enhancement</div>
            <div class="role-details">
              <p>Worked with Verizon (US) on their digital sales flow and the E2E flow for the postpaid journey to implement new requirements. Involved in requirements analysis, E2E HLD design discussions, and finalizing the API contract across systems. Examining the requirements for implementing three different channels (Digital, Assisted and POS journeys) gave deep insight into differences in the implementation and journey behaviours.</p>
              <ul>
                <li><strong>Solution Design:</strong> Spearheaded End-to-End (E2E) High-Level Design (HLD) discussions and finalized system-to-system API contracts for postpaid journeys.</li>
                <li><strong>Omnichannel Analysis:</strong> Evaluated requirements across Assisted, POS, and Digital Sales channels to analyse behavioural differences and streamline multi-channel implementation strategies.</li>
                <li><strong>Mentorship:</strong> Acted as the primary technical point of contact for offshore teams, driving code quality and accelerating development velocity.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java 17/J2EE</span>
                <span class="skill-pill">Cassandra</span>
                <span class="skill-pill">AWS</span>
                <span class="skill-pill">Microservices</span>
                <span class="skill-pill">Spring Flux</span>
                <span class="skill-pill">Spring Core</span>
                <span class="skill-pill">Spring Boot</span>
                <span class="skill-pill">React</span>
                <span class="skill-pill">JUnit</span>
                <span class="skill-pill">Mockito</span>
                <span class="skill-pill">Jenkins</span>
                <span class="skill-pill">Kibana</span>
                <span class="skill-pill">GitLab</span>
                <span class="skill-pill">Agile</span>
                <span class="skill-pill">JIRA</span>
                <span class="skill-pill">BDD</span>
              </div>
            </div>
          </article>

          <!-- Role 3 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Sr. Technical Lead</h3>
                <div class="company-name">HSBC Global Services (Canada) Ltd</div>
              </div>
              <span class="role-dates">2021 – Sep 2023</span>
            </div>
            <div class="project-banner">Key Project: “MyWorkspace” (Multi-year Change the Bank initiative unifying 400+ business functions)</div>
            <div class="role-details">
              <p>In this multi-year Change the Bank (CTB) initiative, the objective was to create a unified user experience for more than 400+ business functions used by HSBC's staff globally. This was built using React & microservices that communicate with the bank's core system via MQ to fulfil the business requirements. Our scrum team owns the Staff Landing module for this project and delivers customer search, account list, account details, transaction history, transaction details, etc., business functions.</p>
              <ul>
                <li><strong>Enterprise Solution Architecture:</strong> Defined low-level application architectures and domain-driven design (DDD) principles for microservices, establishing Open API specifications that empowered regional teams to seamlessly extend core components and accelerate market delivery.</li>
                <li><strong>Distributed System Resilience & Security:</strong> Architected asynchronous microservices utilizing RxJava and integrated Hystrix for fault tolerance, while implementing robust JWT token security for secure, real-time customer data transactions across core systems.</li>
                <li><strong>Global Program Leadership:</strong> Navigated complex global project dynamics by aligning business stakeholders with technical teams, orchestrating development efforts across 100+ resources and multiple multi-country Scrum teams to unify 400+ business functions.</li>
                <li><strong>Full-Stack Delivery & DevOps:</strong> Guided code management and deployment processes, contributing directly to the modular React-based staff landing page and automated deployments on AWS via Jenkins.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java 8.0/J2EE</span>
                <span class="skill-pill">AWS</span>
                <span class="skill-pill">Microservices</span>
                <span class="skill-pill">RxJava</span>
                <span class="skill-pill">Spring Core</span>
                <span class="skill-pill">Spring Boot</span>
                <span class="skill-pill">React</span>
                <span class="skill-pill">NodeJS</span>
                <span class="skill-pill">Hystrix</span>
                <span class="skill-pill">JMeter</span>
                <span class="skill-pill">JUnit</span>
                <span class="skill-pill">Mockito</span>
                <span class="skill-pill">Kubernetes</span>
                <span class="skill-pill">Docker</span>
                <span class="skill-pill">Jenkins</span>
                <span class="skill-pill">Splunk</span>
                <span class="skill-pill">AppDynamics</span>
                <span class="skill-pill">Git</span>
                <span class="skill-pill">Scaled Agile</span>
                <span class="skill-pill">JIRA</span>
                <span class="skill-pill">BDD</span>
              </div>
            </div>
          </article>

          <!-- Role 4 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Architect / Team Lead</h3>
                <div class="company-name">HSBC Global Services (Canada) Ltd</div>
              </div>
              <span class="role-dates">2018 – 2021</span>
            </div>
            <div class="project-banner">Key Project: “RBB Onboarding” (Retail Business Banking STP Onboarding)</div>
            <div class="role-details">
              <p>This project aims to deliver a Retail Business Banking (RBB) onboarding journey for NTB customers. The objective was to build a state-through-process (STP) journey for a business (partnership or corporation) customer. This includes business, customer identity & fraud validation during the flow.</p>
              <ul>
                <li><strong>Requirement Mapping & API Design:</strong> Clarified business requirements and seamlessly mapped them to Backend (BE) Systems and APIs. Finalized solution designs involving intricate integration with third-party APIs and BE Systems. Specialized in designing and building REST and SOAP microservices deployed on Pivotal Cloud Foundry (PCF).</li>
                <li><strong>Team Leadership & End-to-End Delivery:</strong> Led a team of developers in successfully delivering the Retail Business Banking (RBB) Onboarding solution for HSBC Canada, overseeing the end-to-end development process, from conceptualization to implementation, infrastructure setup, and ensuring alignment with HSBC's high standards.</li>
                <li><strong>Production Support & Release Management:</strong> Managed critical aspects of production support and releases for RBB Onboarding, designing and building robust solutions and actively participating in their ongoing maintenance and evolution in a production environment.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java 8.0/J2EE</span>
                <span class="skill-pill">PCF</span>
                <span class="skill-pill">Spring Boot/Core</span>
                <span class="skill-pill">Microservices</span>
                <span class="skill-pill">Hystrix</span>
                <span class="skill-pill">RxJava</span>
                <span class="skill-pill">React</span>
                <span class="skill-pill">JMeter</span>
                <span class="skill-pill">JUnit</span>
                <span class="skill-pill">Jenkins</span>
                <span class="skill-pill">Splunk</span>
                <span class="skill-pill">AppDynamics</span>
                <span class="skill-pill">Git</span>
                <span class="skill-pill">Scaled Agile</span>
                <span class="skill-pill">JIRA</span>
                <span class="skill-pill">BDD</span>
              </div>
            </div>
          </article>

          <!-- Role 5 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Lead Consultant Specialist</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">2016 – Mar 2018</span>
            </div>
            <div class="project-banner">Key Project: “Banking & Services”</div>
            <div class="role-details">
              <p>This project aims to build a new UI for retail customers backed by a new in-house cloud infrastructure in HSBC. The primary objective was to create a solution for one market that could be rapidly scaled to multiple markets/regions.</p>
              <ul>
                <li><strong>API Dependency Mapping:</strong> Responsible for analyzing business requirements and UX design and comprehensively examining various backend (BE) system dependencies to map API to fulfil business needs.</li>
                <li><strong>REST Microservices Servicing:</strong> Worked with multiple scrum teams to develop REST microservices to expedite time-to-market delivery, emphasizing efficiency and responsiveness to market demands. Built several microservices to fulfill account landing and servicing functions for retail customers (e.g., Account List, Transaction List, Account Details) integral in enhancing customer experiences and streamlining operations.</li>
                <li><strong>Coding Standards & Guidelines:</strong> Collaborated with teams to establish development guidelines and coding standards to enhance the overall quality of outputs and foster a culture of continuous improvement within the development process.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java 8.0/J2EE</span>
                <span class="skill-pill">PCF</span>
                <span class="skill-pill">Spring Boot/Core</span>
                <span class="skill-pill">Microservices</span>
                <span class="skill-pill">RxJava</span>
                <span class="skill-pill">Angular 2</span>
                <span class="skill-pill">AEM</span>
                <span class="skill-pill">Hystrix</span>
                <span class="skill-pill">JMeter</span>
                <span class="skill-pill">JUnit</span>
                <span class="skill-pill">Mockito</span>
                <span class="skill-pill">BDD</span>
                <span class="skill-pill">Jenkins</span>
                <span class="skill-pill">Splunk</span>
                <span class="skill-pill">AppDynamics</span>
                <span class="skill-pill">Git</span>
                <span class="skill-pill">JSP</span>
                <span class="skill-pill">Servlets</span>
                <span class="skill-pill">Dojo</span>
                <span class="skill-pill">Fiddler</span>
              </div>
            </div>
          </article>

          <!-- Role 6 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Sr. Consultant Specialist</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">2013 to 2015</span>
            </div>
            <div class="project-banner">Key Project: “GSP (Global Services Platform)”</div>
            <div class="role-details">
              <p>Global Services Platform is an application platform that provides universal banking experience and services across the HSBC group. It aims to develop and deploy as single logical, multiple physical instances to standardize the group retail customer channel application and minimize future development, upgrade, and maintenance costs.</p>
              <ul>
                <li><strong>Tech Lead - Landing Page:</strong> As a tech lead in the "Landing Page" workstream, I contributed to design changes to enhance performance and optimize logging implementation.</li>
                <li><strong>Scrum Master Leadership:</strong> As a scrum master, I demonstrated a profound understanding of Agile and Scrum methodologies. I led a cross-functional team of 10-12 members across various application layers to successfully deliver Account Servicing and dashboard functions. My responsibilities included analyzing requirements, facilitating Scrum ceremonies, providing insights for design enhancements, and actively participating in code reviews.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Spring Core</span>
                <span class="skill-pill">Spring MVC</span>
                <span class="skill-pill">Spring Integration</span>
                <span class="skill-pill">JAX-WS</span>
                <span class="skill-pill">Rest WS</span>
                <span class="skill-pill">Dojo</span>
              </div>
            </div>
          </article>

          <!-- Role 7 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Consultant Specialist</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">2012 to 2013</span>
            </div>
            <div class="project-banner">Key Project: “Assisted FSA Coexistence”</div>
            <div class="role-details">
              <p>This staff-facing application helps the bank user perform banking functions efficiently. Built on WAS 6.1.5, which needed to be migrated to future state technology (Spring 3.1.2, Dojo, and Spring Servlet MVC). Involved in designing the framework of the application based on the FSA architecture defined by HSBC and making required changes for this application.</p>
              <ul>
                <li><strong>Framework Component Design:</strong> Defined framework-level components focusing on state management, exception handling, and seamless integration with Spring.</li>
                <li><strong>Portal Migration & Shared Cache:</strong> Tackled critical aspects such as transitioning control from portal to servlet applications, data-sharing methodologies, and optimizing utilization of a shared instance of DynaCache.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">WebSphere Application Server 7</span>
                <span class="skill-pill">Spring 3.1.2</span>
                <span class="skill-pill">Dojo</span>
                <span class="skill-pill">Spring Integration</span>
              </div>
            </div>
          </article>

          <!-- Role 8 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Consultant Specialist</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">Aug 2011 to 2012</span>
            </div>
            <div class="project-banner">Key Project: “GIPOS 2.0 – 2.5 (Client: HSBC Canada)”</div>
            <div class="role-details">
              <p>The GIPOS program has been mandated to build sales and distribution solutions for insurance product lines using various in-house-developed business components customized for specific business lines. Capabilities deployed on multiple channels: staff (bank branches), customers (internet), call centres, etc.</p>
              <ul>
                <li><strong>Quotes Stream Team Leadership:</strong> As the team leader for the Quotes stream, I guided a group of 8 individuals in the development process. Responsible for conceptualizing and designing the Quotation portlet and establishing a reusable design for the quotation list and Quotation Details page, subsequently utilized across more than 20 insurance products to streamline development efforts and ensure consistency in user experience.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">WebSphere Portal 6.1.5</span>
                <span class="skill-pill">JSR 168 portlets</span>
                <span class="skill-pill">JSF</span>
                <span class="skill-pill">Spring</span>
              </div>
            </div>
          </article>

          <!-- Role 9 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Consultant Specialist</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">Dec 2010 to 2011</span>
            </div>
            <div class="project-banner">Key Project: “Account Opening Deployment (Client: HSBC First Direct UK)”</div>
            <div class="role-details">
              <p>This project was the regional deployment of the “Account Opening” product for HSBC’s “First Direct” entity in the UK.</p>
              <ul>
                <li><strong>Regional Deployment & Journey Customization:</strong> Provided support to the First Direct entity utilizing the product. Responsibilities involved advising on business requirements managed by the core system, offering guidance on page customization, journey creation, and implementing view state logic.</li>
                <li><strong>Core & Regional Team Liaison:</strong> Acted as a liaison between regional teams and the core development team, facilitating effective communication and collaboration.</li>
              </ul>
            </div>
          </article>

          <!-- Role 10 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Sr. Software Engineer</h3>
                <div class="company-name">HSBC Software Development (India) Pvt Ltd</div>
              </div>
              <span class="role-dates">2006 to 2009</span>
            </div>
            <div class="project-banner">Key Project: “Account Opening (Client: HSBC Software House (USA))”</div>
            <div class="role-details">
              <p>This web portal was developed to allow customers to open their accounts online without visiting the branch. This core product can be customized with minimal effort and used by multiple regions to add regional flavour. This is a channel-agnostic product, supporting three channels: online, branch, and call center.</p>
              
              <div class="customization-box">
                <div class="customization-box-title">Significant Platform Customizations Allowed:</div>
                <ul>
                  <li>Different journeys created for the product depending on customer type and channel.</li>
                  <li>Moving the position of pages within the journey.</li>
                  <li>Moving the position of data blocks within the pages and across the pages.</li>
                  <li>Fields omitted or marked read-only based on journey type, customer type, or any other configurable condition.</li>
                </ul>
              </div>

              <ul>
                <li><strong>Module Ownership & Deliverables:</strong> Oversee all aspects of the decision and applicant data modules for the account opening project, ensuring timely delivery of all related deliverables. Role encompassed requirement gathering, analysis, estimation, and devising solutions to address business challenges.</li>
                <li><strong>Mentorship & Onsite Collaboration:</strong> Mentored the team, assisting in their development and resolving project or team-related issues. Onsite throughout requirement analysis and development phases, facilitating smooth communication and stakeholder collaboration.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">WebSphere Portal 6.0</span>
                <span class="skill-pill">JSR 168 portlets</span>
                <span class="skill-pill">JSF</span>
                <span class="skill-pill">Spring</span>
              </div>
            </div>
          </article>

          <!-- Role 11 -->
          <article class="role-card search-target">
            <div class="role-header">
              <div>
                <h3 class="role-title">Sr. Software Engineer</h3>
                <div class="company-name">Cybage Software Pvt. Ltd. Pune, India</div>
              </div>
              <span class="role-dates">2004 – 2006</span>
            </div>
            <div class="project-banner">Key Project: “ChannelWave PRM”</div>
            <div class="role-details">
              <p>Manages the complete partner lifecycle and improves channel performance. Increases visibility of sales opportunities into the sales pipeline across channels. Enhances demand generation with more effective marketing. ChannelWave's Business Intelligence identifies, measures, and replicates the most profitable business activities. Allows customers and channels easy access to information needed to drive sales and improve service. Helps vendor organizations recruit new partners, enhance existing partnerships, and structure and manage partner programs to produce more sales and higher margins.</p>
              <ul>
                <li><strong>Lucene Full-Text Search Engine:</strong> Played a pivotal role in implementing and enhancing major functionalities within ChannelWave PRM. Contributed to performance improvements and UML diagram creation. Notably, spearheaded the development of text search functionality utilizing Lucene for the 6.3 release.</li>
                <li><strong>Production Support & Bug Fixes:</strong> Actively involved in bug fixing and providing production support to ensure system stability and reliability.</li>
              </ul>
              <div class="role-tech-stack">
                <span class="tech-title">Technology set:</span>
                <span class="skill-pill">Java</span>
                <span class="skill-pill">Apache Lucene</span>
                <span class="skill-pill">UML Diagrams</span>
                <span class="skill-pill">ChannelWave PRM</span>
                <span class="skill-pill">Business Intelligence</span>
              </div>
            </div>
          </article>

        </div>
      </section>

      <!-- Certifications Section -->
      <section class="content-card" id="certifications">
        <div class="card-header">
          <h2 class="card-title">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
            Certificates & Achievements
          </h2>
        </div>

        <div class="certs-grid">
          <div class="cert-card search-target">
            <div class="cert-icon-box">🤖</div>
            <div class="cert-info">
              <h4>Generative AI Leader</h4>
              <p>Google</p>
            </div>
          </div>

          <div class="cert-card search-target">
            <div class="cert-icon-box">☁️</div>
            <div class="cert-info">
              <h4>Kubernetes & Cloud Native Associate (KCNA)</h4>
              <p>The Linux Foundation</p>
            </div>
          </div>

          <div class="cert-card search-target">
            <div class="cert-icon-box">📜</div>
            <div class="cert-info">
              <h4>Professional Scrum Master I & II</h4>
              <p>Scrum.org</p>
            </div>
          </div>

          <div class="cert-card search-target">
            <div class="cert-icon-box">🌐</div>
            <div class="cert-info">
              <h4>Architecting with Google Compute Engine</h4>
              <p>Coursera</p>
            </div>
          </div>

          <div class="cert-card search-target">
            <div class="cert-icon-box">💡</div>
            <div class="cert-info">
              <h4>AI For Everyone</h4>
              <p>Coursera (DeepLearning.AI)</p>
            </div>
          </div>

          <div class="cert-card search-target">
            <div class="cert-icon-box">🏆</div>
            <div class="cert-info">
              <h4>HSBC Corporate Excellence Awards</h4>
              <p>Received "RISE", "TEAM", "STARS", and "SPOT" Awards</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Education Section -->
      <section class="content-card" id="education">
        <div class="card-header">
          <h2 class="card-title">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
            Education & Academic Qualifications
          </h2>
        </div>

        <div class="edu-grid">
          <div class="edu-card search-target">
            <div class="edu-degree">MCA (Master in Computer Application)</div>
            <div class="edu-inst">Sikkim Manipal University, India</div>
            <div class="edu-year">2006 – 2009</div>
          </div>

          <div class="edu-card search-target">
            <div class="edu-degree">Diploma in Advanced Computing</div>
            <div class="edu-inst">CDAC-ACTS Hyderabad, India</div>
          </div>

          <div class="edu-card search-target">
            <div class="edu-degree">Post Graduate Diploma in IT</div>
            <div class="edu-inst">Sikkim Manipal University, India</div>
          </div>

          <div class="edu-card search-target">
            <div class="edu-degree">Advanced Diploma in Software Application</div>
            <div class="edu-inst">Tata Infotech, Dehradun, India</div>
          </div>

          <div class="edu-card search-target">
            <div class="edu-degree">Bachelor of Science (B.Sc.)</div>
            <div class="edu-inst">Mahatma Jyotiba Phule Rohilkhand University, Bareilly, India</div>
          </div>
        </div>
      </section>

    </main>

  </div>

  <footer>
    <p>© 2026 Amit Kumar Shukla • Senior Technical Lead & Solution Architect • Mobile-Responsive HTML Resume</p>
  </footer>

  <!-- App Interactivity Scripts -->
  <script>
    // Theme Switcher Logic
    const themeBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('themeText');
    const htmlEl = document.documentElement;

    const savedTheme = localStorage.getItem('resume-theme') || 
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    
    setTheme(savedTheme);

    themeBtn.addEventListener('click', () => {{
      const currentTheme = htmlEl.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
    }});

    function setTheme(theme) {{
      htmlEl.setAttribute('data-theme', theme);
      localStorage.setItem('resume-theme', theme);
      if (theme === 'dark') {{
        themeIcon.textContent = '🌙';
        if (themeText) themeText.textContent = 'Dark';
      }} else {{
        themeIcon.textContent = '☀️';
        if (themeText) themeText.textContent = 'Light';
      }}
    }}

    // Skill Category Filter Logic
    function filterSkills(category) {{
      const btns = document.querySelectorAll('.skill-filter-btn');
      btns.forEach(b => b.classList.remove('active'));
      if (window.event && window.event.target) {{
        window.event.target.classList.add('active');
      }}

      const boxes = document.querySelectorAll('.skill-cat-box');
      boxes.forEach(box => {{
        if (category === 'all' || box.getAttribute('data-cat') === category) {{
          box.style.display = 'block';
        }} else {{
          box.style.display = 'none';
        }}
      }});
    }}

    // PDF Generation Function
    function downloadPDF() {{
      const btn = document.getElementById('downloadPdfBtn');
      const btnText = document.getElementById('downloadPdfText');
      const originalText = btnText ? btnText.textContent : '';
      
      if (btnText) btnText.textContent = 'Generating PDF...';
      btn.style.opacity = '0.7';
      btn.style.pointerEvents = 'none';

      const element = document.getElementById('pdf-container');
      const opt = {{
        margin: [8, 8, 8, 8],
        filename: 'Amit_Kumar_Shukla_Resume.pdf',
        image: {{ type: 'jpeg', quality: 0.98 }},
        html2canvas: {{ scale: 2, useCORS: true, logging: false }},
        jsPDF: {{ unit: 'mm', format: 'letter', orientation: 'portrait' }}
      }};

      if (typeof html2pdf !== 'undefined') {{
        html2pdf().set(opt).from(element).save().then(() => {{
          if (btnText) btnText.textContent = originalText;
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
        }}).catch(err => {{
          console.error('html2pdf error:', err);
          window.print();
          if (btnText) btnText.textContent = originalText;
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
        }});
      }} else {{
        window.print();
        if (btnText) btnText.textContent = originalText;
        btn.style.opacity = '1';
        btn.style.pointerEvents = 'auto';
      }}
    }}

    // Real-time Search Logic
    function performSearch() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const targets = document.querySelectorAll('.search-target');

      targets.forEach(target => {{
        const text = target.textContent.toLowerCase();
        if (!query || text.includes(query)) {{
          target.style.display = '';
        }} else {{
          target.style.display = 'none';
        }}
      }});
    }}

    // Scrollspy for Mobile Nav Chips & Sidebar TOC
    window.addEventListener('scroll', () => {{
      const sections = document.querySelectorAll('section[id]');
      const scrollPos = window.scrollY + 200;

      sections.forEach(sec => {{
        const top = sec.offsetTop;
        const height = sec.offsetHeight;
        const id = sec.getAttribute('id');
        
        if (scrollPos >= top && scrollPos < top + height) {{
          document.querySelectorAll('.toc-links a').forEach(l => l.classList.remove('active'));
          const desktopLink = document.querySelector(`.toc-links a[href="#${{id}}"]`);
          if (desktopLink) desktopLink.classList.add('active');

          document.querySelectorAll('.mobile-nav-strip a').forEach(c => c.classList.remove('active'));
          const mobileLink = document.querySelector(`.mobile-nav-strip a[href="#${{id}}"]`);
          if (mobileLink) mobileLink.classList.add('active');
        }}
      }});
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('Generated clean, fast, lightweight index.html! File size:', len(html_code))
