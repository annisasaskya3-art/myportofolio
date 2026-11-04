/**
 * Halaman Experience (Tugas 5): AJAX + debounced search + modal tambah + toast + anti-XSS.
 *
 * Dibagi menjadi bagian kecil:
 *   1. Konfigurasi & referensi elemen
 *   2. State UI (loading / error / empty / grid)
 *   3. Pengambilan data (fetch) dan render kartu
 *   4. Aksi kartu: star & hapus
 *   5. Modal tambah data
 *   6. Pencarian dengan debouncing
 *
 * Bergantung pada utils.js (getCookie, escapeHtml, safeUrl) dan toast.js (showToast).
 */
(function () {
  'use strict';

  const root = document.getElementById('experience-app');
  if (!root) return;

  // ---------- 1. Konfigurasi & elemen ----------
  const DEBOUNCE_MS = 400;
  const urls = {
    list: root.dataset.listUrl,
    add: root.dataset.addUrl,
  };

  const searchForm = document.getElementById('experience-search-form');
  const searchInput = document.getElementById('experience-search-input');
  const states = {
    loading: document.getElementById('experience-loading'),
    error: document.getElementById('experience-error'),
    empty: document.getElementById('experience-empty'),
    grid: document.getElementById('experience-grid'),
  };
  const emptyMessage = document.getElementById('experience-empty-message');
  const retryButton = document.getElementById('experience-retry');

  // Elemen di bawah ini HANYA dirender untuk peran yang berhak -> bisa null.
  const modal = document.getElementById('experience-modal');
  const openModalButton = document.getElementById('experience-open-modal');
  const addForm = document.getElementById('experience-form');

  let debounceTimer = null;
  let latestRequestId = 0; // mencegah respons lama menimpa respons baru

  // ---------- 2. State UI ----------
  function showState(name) {
    Object.entries(states).forEach(([key, el]) => {
      if (el) el.classList.toggle('hide', key !== name);
    });
  }

  // ---------- 3. Ambil data & render ----------
  async function fetchExperiences(query) {
    const response = await fetch(`${urls.list}?q=${encodeURIComponent(query)}`, {
      headers: { 'X-Requested-With': 'XMLHttpRequest' },
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }

  function renderCard(exp) {
    const thumb = safeUrl(exp.thumbnail);
    const thumbHtml = thumb
      ? `<img src="${escapeHtml(thumb)}" alt="" class="exp-card__thumb" loading="lazy">`
      : '';
    const editBtn = exp.can_edit
      ? `<a href="${escapeHtml(exp.edit_url)}" class="pa-btn pa-btn--edit">Edit</a>`
      : '';
    const deleteBtn = exp.can_delete
      ? `<button type="button" class="pa-btn pa-btn--danger" data-action="delete"
                 data-url="${escapeHtml(exp.delete_url)}">Hapus</button>`
      : '';

    // Setiap nilai teks dari server di-escape sebelum masuk ke innerHTML.
    return `
      <article class="project-card-3d experience-card exp-card" data-id="${escapeHtml(exp.id)}">
        ${thumbHtml}
        <div class="exp-card__meta">
          <span class="tech-tag experience-category">${escapeHtml(exp.category_label)}</span>
          <span class="exp-card__date">${escapeHtml(exp.started_at)}${exp.is_ongoing ? ' – sekarang' : ''}</span>
        </div>
        <h2>${escapeHtml(exp.title)}</h2>
        <p class="experience-description exp-card__desc">${escapeHtml(exp.description)}</p>
        <div class="project-actions">
          <button type="button" class="pa-btn pa-btn--star ${exp.is_starred ? 'is-starred' : ''}"
                  data-action="star" data-url="${escapeHtml(exp.star_url)}"
                  aria-pressed="${exp.is_starred ? 'true' : 'false'}">
            ${exp.is_starred ? '⭐' : '☆'} <span class="star-count">${escapeHtml(exp.stars_count)}</span>
          </button>
          ${editBtn}
          ${deleteBtn}
        </div>
      </article>`;
  }

  async function loadExperiences(query = '') {
    const requestId = ++latestRequestId;
    showState('loading');
    try {
      const data = await fetchExperiences(query);
      if (requestId !== latestRequestId) return; // sudah ada permintaan yang lebih baru

      if (!data.results.length) {
        emptyMessage.textContent = query
          ? `Tidak ada pengalaman yang cocok dengan "${query}".`
          : 'Belum ada pengalaman yang ditambahkan.';
        showState('empty');
        return;
      }
      states.grid.innerHTML = data.results.map(renderCard).join('');
      showState('grid');
    } catch (err) {
      if (requestId !== latestRequestId) return;
      console.error('Gagal memuat experience:', err);
      showState('error');
    }
  }

  const currentQuery = () => searchInput.value.trim();

  // ---------- helper POST dengan token CSRF ----------
  async function postRequest(url, body) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
      body: body, // FormData / undefined
    });
    let data = {};
    try { data = await response.json(); } catch (e) { /* respons bukan JSON */ }
    return { response, data };
  }

  // ---------- 4. Aksi kartu (event delegation) ----------
  async function handleStar(button) {
    button.disabled = true;
    try {
      const { response, data } = await postRequest(button.dataset.url);
      if (response.status === 401) {
        showToast('Perlu login', data.message || 'Silakan login terlebih dahulu.', 'error');
        if (data.login_url) setTimeout(() => { window.location.href = data.login_url; }, 1200);
        return;
      }
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      loadExperiences(currentQuery());
    } catch (err) {
      showToast('Gagal', 'Star tidak dapat diubah. Coba lagi.', 'error');
    } finally {
      button.disabled = false;
    }
  }

  async function handleDelete(button) {
    if (!confirm('Yakin ingin menghapus pengalaman ini?')) return;
    button.disabled = true;
    try {
      const { response, data } = await postRequest(button.dataset.url);
      if (response.ok) {
        showToast('Berhasil', data.message || 'Pengalaman dihapus.', 'success');
        loadExperiences(currentQuery());
      } else {
        showToast('Gagal', data.message || 'Anda tidak memiliki akses.', 'error');
      }
    } catch (err) {
      showToast('Gagal', 'Terjadi kesalahan jaringan.', 'error');
    } finally {
      button.disabled = false;
    }
  }

  states.grid.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-action]');
    if (!button) return;
    if (button.dataset.action === 'star') handleStar(button);
    if (button.dataset.action === 'delete') handleDelete(button);
  });

  // ---------- 5. Modal tambah data ----------
  function clearFieldErrors() {
    addForm.querySelectorAll('[data-error-for]').forEach((el) => { el.textContent = ''; });
  }

  function showFieldErrors(errors) {
    const lines = [];
    Object.entries(errors || {}).forEach(([field, items]) => {
      const messages = items.map((item) => item.message);
      const slot = addForm.querySelector(`[data-error-for="${field}"]`);
      if (slot) slot.textContent = messages.join(' '); // textContent -> aman dari XSS
      lines.push(`${field}: ${messages.join(' ')}`);
    });
    return lines.join('\n');
  }

  function closeModal() {
    if (modal && modal.open) modal.close();
  }

  // Listener hanya dipasang jika elemennya ada (pengunjung/peran lain tidak punya modal).
  if (openModalButton && modal) {
    openModalButton.addEventListener('click', () => modal.showModal());
    modal.querySelectorAll('[data-close-modal]').forEach((el) => el.addEventListener('click', closeModal));
    // klik pada backdrop (di luar kotak dialog) menutup modal
    modal.addEventListener('click', (event) => { if (event.target === modal) closeModal(); });
  }

  if (addForm) {
    addForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      clearFieldErrors();
      const submitButton = addForm.querySelector('button[type="submit"]');
      submitButton.disabled = true;
      try {
        // FormData sudah memuat csrfmiddlewaretoken dari {% csrf_token %}; header X-CSRFToken ikut dikirim juga.
        const { response, data } = await postRequest(urls.add, new FormData(addForm));
        if (response.status === 201) {
          closeModal();
          addForm.reset();
          showToast('Berhasil', data.message || 'Pengalaman berhasil ditambahkan.', 'success');
          searchInput.value = '';          // tampilkan semua data agar item baru terlihat
          loadExperiences('');             // perbarui daftar tanpa reload halaman
        } else if (response.status === 400) {
          showToast('Data tidak valid', showFieldErrors(data.errors) || data.message, 'error');
        } else {
          showToast('Gagal', data.message || `Terjadi kesalahan (HTTP ${response.status}).`, 'error');
        }
      } catch (err) {
        showToast('Gagal', 'Terjadi kesalahan jaringan.', 'error');
      } finally {
        submitButton.disabled = false;
      }
    });
  }

  // ---------- 6. Pencarian dengan debouncing ----------
  // Permintaan baru hanya dikirim setelah pengguna berhenti mengetik selama DEBOUNCE_MS.
  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => loadExperiences(currentQuery()), DEBOUNCE_MS);
  });

  searchForm.addEventListener('submit', (event) => {
    event.preventDefault();
    clearTimeout(debounceTimer);
    loadExperiences(currentQuery());
  });

  if (retryButton) retryButton.addEventListener('click', () => loadExperiences(currentQuery()));

  loadExperiences(currentQuery());
})();
