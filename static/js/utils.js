/**
 * Helper JavaScript bersama (dimuat dari base.html).
 * - getCookie  : membaca cookie, dipakai untuk token CSRF (header X-CSRFToken)
 * - escapeHtml : meng-escape teks sebelum disisipkan ke HTML lewat JavaScript (anti-XSS)
 * - safeUrl    : hanya meloloskan URL http/https (menolak javascript:, data:, dll.)
 */
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function escapeHtml(value) {
  if (value === null || value === undefined) return '';
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function safeUrl(url) {
  return /^https?:\/\//i.test(url || '') ? url : '';
}
