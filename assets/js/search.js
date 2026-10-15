/**
 * Fast client-side search using search.json
 */

(function () {
  let searchIndex = null;
  let selectedIndex = -1;

  const modal = document.getElementById('search-modal');
  const triggerBtn = document.getElementById('search-trigger');
  const closeBtn = document.getElementById('search-modal-close');
  const backdrop = document.getElementById('search-backdrop');
  const searchInput = document.getElementById('search-input');
  const resultsContainer = document.getElementById('search-results');
  const statusContainer = document.getElementById('search-status');

  if (!modal || !searchInput) return;

  // Open modal
  function openSearch() {
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    searchInput.value = '';
    selectedIndex = -1;
    resultsContainer.innerHTML = '';
    statusContainer.innerHTML = '<span class="search-hint">Type to start searching... Press <kbd>ESC</kbd> to exit</span>';
    setTimeout(() => searchInput.focus(), 50);

    if (!searchIndex) {
      loadIndex();
    }
  }

  // Close modal
  function closeSearch() {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Fetch search.json
  async function loadIndex() {
    try {
      const response = await fetch('/search.json');
      if (response.ok) {
        searchIndex = await response.json();
      }
    } catch (err) {
      console.warn('Could not load search.json: ', err);
    }
  }

  // Search logic
  function performSearch(query) {
    if (!searchIndex || !query.trim()) {
      resultsContainer.innerHTML = '';
      statusContainer.innerHTML = '<span class="search-hint">Type to start searching... Press <kbd>ESC</kbd> to exit</span>';
      selectedIndex = -1;
      return;
    }

    const q = query.toLowerCase().trim();
    const words = q.split(/\s+/);

    const matches = searchIndex.filter(post => {
      const searchableText = `${post.title} ${post.description} ${post.category} ${(post.tags || []).join(' ')}`.toLowerCase();
      return words.every(word => searchableText.includes(word));
    });

    renderResults(matches, q);
  }

  function renderResults(posts, query) {
    selectedIndex = -1;
    if (posts.length === 0) {
      statusContainer.innerHTML = `<span>No articles found matching "<strong>${escapeHtml(query)}</strong>"</span>`;
      resultsContainer.innerHTML = '';
      return;
    }

    statusContainer.innerHTML = `<span>Found <strong>${posts.length}</strong> matching ${posts.length === 1 ? 'article' : 'articles'}</span>`;
    
    let html = '';
    posts.forEach((post, idx) => {
      html += `
        <div class="search-result-item" data-index="${idx}" data-url="${post.url}">
          <div class="search-result-meta">
            <span class="post-category-tag">${escapeHtml(post.category)}</span>
            <span>${escapeHtml(post.date)}</span>
          </div>
          <h4 class="search-result-title">
            <a href="${post.url}">${highlightMatches(escapeHtml(post.title), query)}</a>
          </h4>
          <p class="search-result-snippet">${highlightMatches(escapeHtml(post.description), query)}</p>
        </div>
      `;
    });

    resultsContainer.innerHTML = html;

    // Attach click handlers
    const items = resultsContainer.querySelectorAll('.search-result-item');
    items.forEach(item => {
      item.addEventListener('click', () => {
        window.location.href = item.getAttribute('data-url');
      });
    });
  }

  function highlightMatches(text, query) {
    if (!query) return text;
    const words = query.trim().split(/\s+/).filter(w => w.length > 0);
    let result = text;
    words.forEach(word => {
      const regex = new RegExp(`(${escapeRegExp(word)})`, 'gi');
      result = result.replace(regex, '<mark>$1</mark>');
    });
    return result;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/[&<>"']/g, m => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[m]);
  }

  function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Key navigation in modal
  function updateSelection(items) {
    items.forEach((item, idx) => {
      if (idx === selectedIndex) {
        item.classList.add('selected');
        item.scrollIntoView({ block: 'nearest' });
      } else {
        item.classList.remove('selected');
      }
    });
  }

  // Event Listeners
  if (triggerBtn) triggerBtn.addEventListener('click', openSearch);
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);
  if (backdrop) backdrop.addEventListener('click', closeSearch);

  searchInput.addEventListener('input', (e) => {
    performSearch(e.target.value);
  });

  // Keyboard navigation & global shortcuts
  document.addEventListener('keydown', (e) => {
    // Open on Ctrl+K or Cmd+K or / (when not in an input)
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (modal.classList.contains('active')) {
        closeSearch();
      } else {
        openSearch();
      }
    } else if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      e.preventDefault();
      openSearch();
    } else if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeSearch();
    } else if (modal.classList.contains('active')) {
      const items = resultsContainer.querySelectorAll('.search-result-item');
      if (items.length === 0) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = (selectedIndex + 1) % items.length;
        updateSelection(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = (selectedIndex - 1 + items.length) % items.length;
        updateSelection(items);
      } else if (e.key === 'Enter' && selectedIndex >= 0 && items[selectedIndex]) {
        e.preventDefault();
        window.location.href = items[selectedIndex].getAttribute('data-url');
      }
    }
  });
})();
