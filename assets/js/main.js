/**
 * Amit Kumar Shukla - Main Website Script
 * Handles Theme Toggle, Navigation, Code Copy, TOC, and Utilities
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initMobileMenu();
  initCodeCopyButtons();
  initTableOfContents();
  initBackToTop();
  initShareButtons();
});

/* ---------------------------------------------------------
   Theme Switcher (Dark / Light Mode)
   --------------------------------------------------------- */
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  if (!toggleBtn) return;

  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });
}

/* ---------------------------------------------------------
   Mobile Navigation Menu
   --------------------------------------------------------- */
function initMobileMenu() {
  const menuToggle = document.getElementById('mobile-menu-toggle');
  const siteNav = document.getElementById('site-nav');
  if (!menuToggle || !siteNav) return;

  menuToggle.addEventListener('click', () => {
    const isOpen = siteNav.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!siteNav.contains(e.target) && !menuToggle.contains(e.target) && siteNav.classList.contains('open')) {
      siteNav.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    }
  });
}

/* ---------------------------------------------------------
   Code Snippet Copy Buttons
   --------------------------------------------------------- */
function initCodeCopyButtons() {
  const codeBlocks = document.querySelectorAll('.post-entry-content pre, .post-entry-content .highlight');
  
  codeBlocks.forEach(block => {
    // Avoid double buttons
    if (block.querySelector('.code-copy-btn')) return;

    const copyBtn = document.createElement('button');
    copyBtn.className = 'code-copy-btn';
    copyBtn.setAttribute('aria-label', 'Copy code to clipboard');
    copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy';

    copyBtn.addEventListener('click', async () => {
      const code = block.querySelector('code') ? block.querySelector('code').innerText : block.innerText;
      try {
        await navigator.clipboard.writeText(code);
        copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
        copyBtn.style.color = '#10b981';
        setTimeout(() => {
          copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i> Copy';
          copyBtn.style.color = '';
        }, 2000);
      } catch (err) {
        console.error('Failed to copy code: ', err);
      }
    });

    block.style.position = 'relative';
    block.appendChild(copyBtn);
  });
}

/* ---------------------------------------------------------
   Dynamic Table of Contents (TOC) & ScrollSpy
   --------------------------------------------------------- */
function initTableOfContents() {
  const articleContent = document.getElementById('article-content');
  const tocNav = document.getElementById('toc-nav');
  const tocContainer = document.getElementById('toc-container');
  if (!articleContent || !tocNav) return;

  const headings = articleContent.querySelectorAll('h2, h3');
  if (headings.length === 0) {
    if (tocContainer) tocContainer.style.display = 'none';
    return;
  }

  const ul = document.createElement('ul');

  headings.forEach((heading, index) => {
    if (!heading.id) {
      heading.id = 'heading-' + index + '-' + heading.innerText.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    }

    const li = document.createElement('li');
    li.className = heading.tagName.toLowerCase() === 'h3' ? 'toc-subitem' : 'toc-item';
    if (heading.tagName.toLowerCase() === 'h3') {
      li.style.paddingLeft = '1rem';
    }

    const a = document.createElement('a');
    a.href = '#' + heading.id;
    a.innerText = heading.innerText;

    li.appendChild(a);
    ul.appendChild(li);
  });

  tocNav.innerHTML = '';
  tocNav.appendChild(ul);

  // ScrollSpy highlight
  const tocLinks = tocNav.querySelectorAll('a');
  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 100;

    headings.forEach(heading => {
      if (heading.offsetTop <= scrollPos) {
        currentId = heading.id;
      }
    });

    tocLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + currentId) {
        link.classList.add('active');
      }
    });
  }, { passive: true });
}

/* ---------------------------------------------------------
   Back to Top Button
   --------------------------------------------------------- */
function initBackToTop() {
  const backBtn = document.getElementById('back-to-top');
  if (!backBtn) return;

  backBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ---------------------------------------------------------
   Article Link Copy Button
   --------------------------------------------------------- */
function initShareButtons() {
  const copyLinkBtn = document.getElementById('copy-article-link');
  if (!copyLinkBtn) return;

  copyLinkBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      const textSpan = copyLinkBtn.querySelector('.share-btn-text');
      if (textSpan) {
        const orig = textSpan.innerText;
        textSpan.innerText = 'Copied!';
        setTimeout(() => { textSpan.innerText = orig; }, 2000);
      }
    } catch (e) {
      console.error(e);
    }
  });
}
