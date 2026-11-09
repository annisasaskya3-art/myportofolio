/**
 * Halaman Experience (Tugas 5): AJAX + debounced search + modal tambah + toast + anti-XSS.
 *
 */
(function () {
  'use strict';

  const root = document.getElementById('experience-app');
  if (!root) return;

  // ---------- 1. Konfigurasi & elemen ----------
  const DEBOUNCE_MS = 400;
  const urls = {
    list: root.dataset.listUrl,
    login: root.dataset.loginUrl,
  };
  const isAuthenticated = root.dataset.authenticated === 'true';
  const detailUrl = (id) => `${urls.list}${encodeURIComponent(id)}/`;
  const starUrl = (id) => `${detailUrl(id)}star/`;

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
  const modalTitle = document.getElementById('experience-modal-title');

  let debounceTimer = null;
  let latestRequestId = 0; // mencegah respons lama menimpa respons baru
  
  const FIELDS = ['title', 'description', 'category', 'thumbnail'];
  const experiencesById = new Map(); // untuk mengisi modal edit tanpa fetch ulang
  let editingId = null;              // null = mode tambah, selain itu = mode edit

  // ---------- 2. State UI ----------
  function showState(name) {
    Object.entries(states).forEach(([key, el]) => {
      if (el) el.classList.toggle('hide', key !== name);
    });
  }

  // ---------- 3. Ambil data & render ----------
  // Satu helper untuk semua panggilan ke API (GET/POST/PUT/DELETE).
  async function apiRequest(url, { method = 'GET', body } = {}) {
    const options = { method, credentials: 'same-origin', headers: { Accept: 'application/json' } };
    if (method !== 'GET') options.headers['X-CSRFToken'] = getCookie('csrftoken');
    if (body !== undefined) {
      options.headers['Content-Type'] = 'application/json';
      options.body = JSON.stringify(body);
    }
    const response = await fetch(url, options);
    let data = null;
    if (response.status !== 204) {
      try { data = await response.json(); } catch (e) { /* bukan JSON */ }
    }
    return { response, data };
  }

  // Error DRF: 400 -> {field: ["pesan"]}, 403 -> {"detail": "pesan"}
  function describeApiError(data, fallback) {
    if (!data) return fallback;
    if (typeof data.detail === 'string') return data.detail;
    const lines = Object.entries(data).map(([f, msgs]) => `${f}: ${[].concat(msgs).join(' ')}`);
    return lines.join('\n') || fallback;
  }

  function formatDate(iso) {
    return new Date(iso).toLocaleDateString('id-ID', { day: '2-digit', month: 'short', year: 'numeric' });
  }

  async function fetchExperiences(query) {
    const params = new URLSearchParams();
    if (query) params.set('q', query);
    const { response, data } = await apiRequest(`${urls.list}?${params}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return data; // API mengembalikan array langsung
  }

  function renderCard(exp) {
    const thumb = safeUrl(exp.thumbnail);
    const thumbHtml = thumb
      ? `<img src="${escapeHtml(thumb)}" alt="" class="exp-card__thumb" loading="lazy">`
      : '';
    const editBtn = exp.can_edit
      ? `<button type="button" class="pa-btn pa-btn--edit" data-action="edit"
                 data-id="${escapeHtml(exp.id)}">Edit</button>`
      : '';
    const deleteBtn = exp.can_delete
      ? `<button type="button" class="pa-btn pa-btn--danger" data-action="delete"
                 data-id="${escapeHtml(exp.id)}">Hapus</button>`
      : '';

    // Setiap nilai teks dari server di-escape sebelum masuk ke innerHTML.
    return `
      <article class="project-card-3d experience-card exp-card" data-id="${escapeHtml(exp.id)}">
        ${thumbHtml}
        <div class="exp-card__meta">
          <span class="tech-tag experience-category">${escapeHtml(exp.category_label)}</span>
          <span class="exp-card__date">${escapeHtml(formatDate(exp.started_at))}${exp.is_ongoing ? ' – sekarang' : ''}</span>
        </div>
        <h2>${escapeHtml(exp.title)}</h2>
        <p class="experience-description exp-card__desc">${escapeHtml(exp.description)}</p>
        <div class="project-actions">
          <button type="button" class="pa-btn pa-btn--star ${exp.is_starred ? 'is-starred' : ''}"
                  data-action="star" data-id="${escapeHtml(exp.id)}"
                  aria-pressed="${exp.is_starred ? 'true' : 'false'}">
            ${exp.is_starred ? '⭐' : '☆'} <span class="star-count">${escapeHtml(exp.star_count)}</span>
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
      if (requestId !== latestRequestId) return;

      experiencesById.clear();
      data.forEach((exp) => experiencesById.set(exp.id, exp));

      if (!data.length) {
        emptyMessage.textContent = query
          ? `Tidak ada pengalaman yang cocok dengan "${query}".`
          : 'Belum ada pengalaman yang ditambahkan.';
        showState('empty');
        return;
      }
       states.grid.innerHTML = data.map(renderCard).join('');
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
    if (!isAuthenticated) {
      showToast('Perlu login', 'Silakan login untuk memberi star.', 'error');
      setTimeout(() => { window.location.href = urls.login; }, 1200);
      return;
    }
    button.disabled = true;
    try {
      const { response, data } = await apiRequest(starUrl(button.dataset.id), { method: 'POST' });
      if (!response.ok) {
        showToast('Gagal', describeApiError(data, `HTTP ${response.status}`), 'error');
        return;
      }
      loadExperiences(currentQuery());
    } catch (err) {
      showToast('Gagal', 'Terjadi kesalahan jaringan.', 'error');
    } finally {
      button.disabled = false;
    }
  }

  async function handleDelete(button) {
    if (!confirm('Yakin ingin menghapus pengalaman ini?')) return;
    button.disabled = true;
    try {
      const { response, data } = await apiRequest(detailUrl(button.dataset.id), { method: 'DELETE' });
      if (response.status === 204) {
        showToast('Berhasil', 'Pengalaman dihapus.', 'success');
        loadExperiences(currentQuery());
      } else {
        showToast(response.status === 403 ? 'Tidak diizinkan' : 'Gagal',
                  describeApiError(data, `HTTP ${response.status}`), 'error');
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
    if (button.dataset.action === 'edit' && modal) openModal(experiencesById.get(button.dataset.id));
  });

   // ---------- 5. Modal tambah & edit data ----------
  function clearFieldErrors() {
    addForm.querySelectorAll('[data-error-for]').forEach((el) => { el.textContent = ''; });
  }

  // Error 400 DRF berbentuk {field: ["pesan", ...]}
  function showFieldErrors(errors) {
    addForm.querySelectorAll('[data-error-for]').forEach((el) => {
      el.textContent = [].concat((errors || {})[el.dataset.errorFor] || []).join(' '); // textContent -> aman XSS
    });
  }

  function openModal(exp = null) {
    editingId = exp ? exp.id : null;
    addForm.reset();
    clearFieldErrors();
    modalTitle.textContent = exp ? 'Edit Experience' : 'Tambah Experience';
    if (exp) {
      FIELDS.forEach((name) => { addForm.elements[name].value = exp[name] || ''; });
    }
    modal.showModal();
  }

  function closeModal() {
    if (modal && modal.open) modal.close();
  }

  // Modal ada untuk pemilik & Editor; tombol "Tambah" hanya untuk pemilik -> keduanya bisa null.
  if (modal) {
    modal.querySelectorAll('[data-close-modal]').forEach((el) => el.addEventListener('click', closeModal));
    modal.addEventListener('click', (event) => { if (event.target === modal) closeModal(); });
  }
  if (openModalButton) openModalButton.addEventListener('click', () => openModal());

  if (addForm) {
    addForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      clearFieldErrors();

      const body = Object.fromEntries(FIELDS.map((name) => [name, addForm.elements[name].value.trim()]));
      const isEdit = editingId !== null;
      const submitButton = addForm.querySelector('button[type="submit"]');
      submitButton.disabled = true;
      try {
        // Edit = PUT (form mengirim semua field), tambah = POST ke daftar.
        const { response, data } = await apiRequest(
          isEdit ? detailUrl(editingId) : urls.list,
          { method: isEdit ? 'PUT' : 'POST', body },
        );
        if (response.ok) { // 201 (dibuat) atau 200 (diperbarui)
          closeModal();
          showToast('Berhasil', isEdit ? 'Pengalaman diperbarui.' : 'Pengalaman berhasil ditambahkan.', 'success');
          if (!isEdit) searchInput.value = ''; // tampilkan semua agar item baru terlihat
          loadExperiences(currentQuery());
        } else if (response.status === 400) {
          showFieldErrors(data);
          showToast('Data tidak valid', describeApiError(data, 'Periksa kembali isian Anda.'), 'error');
        } else {
          showToast(response.status === 403 ? 'Tidak diizinkan' : 'Gagal',
                    describeApiError(data, `HTTP ${response.status}`), 'error');
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
