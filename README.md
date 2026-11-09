Nama: Annisa Saskya Aulia 
NPM: 2506537915 
Kelas : PBP C 

# My Personal Portfolio

## Deskripsi Proyek

Proyek ini merupakan website portofolio pribadi yang dikembangkan menggunakan Django sebagai bagian dari mata kuliah Pemrograman Berbasis Platform (PBP).

Website ini berfungsi untuk menampilkan informasi pribadi dan hasil karya, serta menyediakan fitur pengelolaan data portofolio secara dinamis. Pengembangan dilakukan secara bertahap dengan menerapkan konsep pengembangan web, pengelolaan database, autentikasi dan otorisasi pengguna, hingga implementasi REST API menggunakan Django REST Framework.

Beberapa fitur yang dikembangkan meliputi:
- Menampilkan informasi dan konten portofolio.
- Mengelola data portofolio melalui fitur tambah, lihat, ubah, dan hapus.
- Menerapkan pembagian hak akses berdasarkan peran pengguna.
- Memberikan fitur star pada konten tertentu.
- Menggunakan AJAX dan Fetch API untuk berinteraksi dengan server tanpa perlu memuat ulang halaman.
- Menyediakan REST API untuk mengakses dan mengelola data portofolio.

## Teknologi yang Digunakan

- **Python** sebagai bahasa pemrograman.
- **Django** sebagai web framework.
- **Django REST Framework** untuk implementasi REST API.
- **SQLite** sebagai database pengembangan.
- **HTML, CSS, dan JavaScript** untuk membangun antarmuka website.
- **Fetch API dan AJAX** untuk komunikasi asynchronous antara frontend dan backend.
- **Git dan GitHub** untuk version control dan penyimpanan kode.

## Instruksi Setup

### 1. Clone repository

```bash
git clone https://github.com/annisasaskya3-art/myportofolio.git
cd myportofolio
```

### 2. Buat dan aktifkan virtual environment

Untuk Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan migrasi database

```bash
python manage.py migrate
```

### 5. Jalankan development server

```bash
python manage.py runserver
```

Website dapat diakses melalui:

```text
http://127.0.0.1:8000/
```

## Rangkuman Progress Mingguan

| Tugas | Progress |
|---|---|
| Individual Assignment 1 – Static Web with HTML5 and CSS3 | Membangun website statis menggunakan HTML5 dan CSS3 sebagai fondasi awal pengembangan portofolio. |
| Individual Assignment 2 – Implementasi MVT pada Django | Mengembangkan website menggunakan Django dengan menerapkan pola Model-View-Template (MVT). |
| Individual Assignment 3 – Form & Data Delivery | Mengimplementasikan form untuk menerima input pengguna serta mempelajari proses pengiriman dan pengolahan data pada Django. |
| Individual Assignment 4 – Authentication, Session and Cookies Implementation | Menerapkan autentikasi pengguna serta memahami pengelolaan session dan cookies dalam aplikasi web. |
| Individual Assignment 5 – Web Interactivity with JavaScript | Mengembangkan interaktivitas website menggunakan JavaScript agar interaksi pengguna dengan halaman web menjadi lebih dinamis. |
| Individual Assignment 6 – Django REST Framework Implementation | Mengimplementasikan REST API menggunakan Django REST Framework, termasuk serializer, validasi data, permission, autentikasi, serta pengujian endpoint API. |

---


## Pertanyaan Reflektif Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Jawab: Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<footer>` dalam merancang struktur website portofolio ini. Ketika saya menggunakan elemen-elemen semantik tersebut, saya merasakan beberapa kegunaan yang membantu pekerjaan saya lebih meaningful dan rapi.
 - **Aksesibilitas (Accessibility & Screen Readers)**: Elemen semantik membantu *screen reader* memahami struktur halaman, sehingga memudahkan penyandang disabilitas dalam menavigasi website. Selain itu, elemen semantik juga meningkatkan kualitas kode karena kualitas kode tidak hanya dilihat dari seberapa efisien dan sukses kodenya untuk mencapai tujuan, tapi juga bagaimana kode itu bisa dibaca dan dipahami dengan mudah dan cepat oleh orang lain.
 - **Organisasi Kode:** Struktur kode menjadi jauh lebih rapi dan mudah dibaca (maintainable) dibanding hanya menggunakan tag `<div>` yang generik dan multifungsi. Jika menggunakan elemen <div> dalam setiap baris kode yang dibutuhkan, possibility untuk berasumsi dalam pengerjaan kode akan semakin tinggi. Oleh karena itu elemen semantik memberikan keunggulan besar dalam mengorganisasikan kode.
 - **Informasi yang Hirarkis:** Tag semantik seperti `<section>` berfungsi untuk memperjelas pembagian area konten utama (seperti *Profile* dan *Skills & Interests*), sementara tag `<article>` membungkus setiap item kartu (*card*) sebagai satu kesatuan informasi yang berdiri sendiri.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Jawab: Tantangan utama yang dihadapi selama saya mengatur tata letak suatu komponen adalah menjaga tata letak komponen Neo-Brutalist (yang menggunakan garis tepi tebal dan bayangan tajam/"box-shadow") agar tidak saling menumpuk atau terpotong saat lebar layar mengecil. Selain itu, mengatur gambar profil agar tetap proporsional menggunakan `object-fit` dan `aspect-ratio` dan juga mengatur komponen agar tidak terlihat terlalu besar/terlalau kecil di berbagai ukuran layar juga memerlukan penyesuaian khusus.

**Evaluasi:**
 - **Sistem Grid & Flexbox:** Menggunakan CSS Grid dengan properti `repeat(auto-fit, minmax(280px, 1fr))` pada bagian kartu. Saat berada di desktop, kartu akan sejajar ke samping (3 kolom), namun saat berpindah ke mobile, kartu akan otomatis menyusun ke bawah (1 kolom).
 - **Prioritas Hirarki Visual:** Pada layar mobile yang terbatas, ukuran teks judul diperkecil secara proporsional dan jarak antar-elemen (*padding/margin*) dikurangi agar pengguna mobile dapat melakukan *skimming* informasi dengan cepat tanpa perlu melakukan *scroll* yang terlalu panjang.
 - **Banyak Berlatih dan Bereksperimen:** Selain memahami teori teknis dan *shortcut* agar mendapatkan posisi dan ukuran yang pas, diperlukan juga latihan dengan frekuensi yang cukup agar dapat mengefisiensikan waktu dan tidak menghabiskan waktu hanya untuk mencari tahu posisi dan ukuran apa yang tepat untuk satu komponen.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Jawab:
 - **Konten Statis (Hardcoded):** Semua data profil, keahlian, dan proyek harus diubah manual di file HTML jika ada pembaruan data.
 - **Interaktivitas Visual & State terbatas:** Halaman statis murni belum memiliki manajemen state otomatis untuk preferensi visual pengguna (seperti menyimpan pilihan *Dark/Light Mode*) serta kurangnya animasi transisi pemuatan halaman (*loading screen*) yang lebih hidup.

**Fungsionalitas Dinamis yang Ingin Ditambahkan pada Iterasi Selanjutnya:**
 - **Menetapkan Tema Besar Website:** Mencari kombinasi warna, elemen, dan meningkatkan UI Design agar saya mendapatkan arah yang jelas ke mana saya ingin membawa user dalam website portofolio saya dan perasaan apa yang ingin saya ciptakan untuk mereka selama mereka menelusuri website portofolio saya.
 - **Interactive Dark/Light Mode dengan Animasi Tali Lampu:** Menambahkan fitur saklar interaktif berbentuk tali yang dapat ditarik untuk mengubah tema warna global (*light/dark mode*) serta menyimpan preferensinya di *local storage*.
 - **Custom Brutalist Loading Animation:** Menambahkan animasi pemuatan halaman (*page loader screen*) saat website pertama kali dibuka untuk meningkatkan aspek *user experience* dan memberikan kesan aplikasi modern.
 - **Integrasi Django Backend & Database:** Menggunakan Django ORM untuk menyimpan data *Experience* (timeline) dan proyek secara dinamis sehingga mudah diubah melalui antarmuka Django Admin.

 ## AI Disclosure

Sesuai dengan ketentuan pengerjaan tugas, saya menggunakan Generative AI (Gemini) dalam proses pengembangan website portofolio ini untuk membantu beberapa aspek berikut:

1. **Eksplorasi & Refinement UI/UX:** Membantu menentukan hirarki informasi (*Information Architecture*) yang baik berdasarkan prinsip UX (seperti F-Shape Pattern dan Jacob Nielsen's Heuristics) serta merancang konsep tema *Neo-Brutalist*.
2. **Pengembangan CSS & Responsive Layout:** Diskusi dan pembuatan struktur kodingan CSS Grid, Flexbox, penanganan `object-fit` pada foto profil, serta efek interaktif *hover* pada kartu (*cards*).
3. **Troubleshooting & Debugging:** Menyelesaikan kendala *browser caching* pada file statis CSS dan memastikan tampilan tetap konsisten (*cross-browser compatibility*).
4. **Penyusunan Dokumentasi:** Penerjemahan konten ke dalam bahasa Inggris yang profesional.

Seluruh kodingan, struktur HTML/CSS, dan konten yang dihasilkan oleh AI telah ditinjau, dipahami, dites, dan dimodifikasi secara mandiri untuk memastikan kesesuaian dengan persyaratan tugas Mata Kuliah Pemrograman Berbasis Platform.


### Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
Jawab: **HTTP Request**: Pengguna mengakses URL halaman portofolio baru di browser (misal: '/experience/'). Di sini pengguna akan mengetahui alamat URL dari menu atau laman yang sedang ia buka. **Proyek 'urls.py'**: Berkas 'urls.py' tingkat proyek menerima permintaan HTTP pertama kali dan mengarahkannya ke berkas 'urls.py' tingkat aplikasi menggunakan fungsi 'include()'. **Aplikasi 'urls.py'**: Berkas 'urls.py' aplikasi mencocokkan pola path '/experience/' dan memanggil fungsi pemroses (*view*) yang bersesuaian, yaitu 'show_experience'. **'views.py'**: Fungsi 'show_experience' mengeksekusi logika bisnis. View meminta data dari **'models.py'** menggunakan perintah ORM 'Experience.objects.all()'. **'models.py'**: Model berkomunikasi dengan database untuk mengambil seluruh rekaman data *experience* dan mengembalikannya ke *view*. **Context & Rendering 'template'**: *View* memasukkan data objek dari model ke dalam kamus 'context', lalu memanggil fungsi 'render()' untuk menggabungkan 'context' dengan berkas 'experience.html'. **HTTP Response**: Django memproses sintaks DTL (Django Template Language) pada berkas 'template.html' menjadi dokumen HTML statis utuh, lalu mengirimkannya kembali ke browser pengguna sebagai HTTP Response.
2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
Jawab: **Pemisahan Tanggung Jawab (Separation of Concerns)**: Menjaga struktur tampilan (HTML/CSS) tetap terpisah dari data bisnis. **Kemudahan Pemeliharaan (Maintainability)**: Jika ada pembaruan data portofolio, pengembang cukup memperbarui isi database (melalui Admin Panel atau Shell) tanpa perlu menyentuh atau merubah struktur kode HTML secara manual. **Dinamis dan Terstruktur (Scalability)**: Penggunaan *loop* DTL memungkinkan tampilan bertambah secara otomatis menyesuaikan jumlah baris data di database. **Reusability Data**: Data yang tersimpan di model dapat dengan mudah digunakan kembali untuk fitur lain, seperti API endpoint (JSON) untuk aplikasi *mobile*, fitur pencarian, atau filter kategori. Menyimpan data portofolio di dalam *model* daripada menuliskannya secara langsung (*hard-coded*) di dalam *template* HTML merupakan penerapan prinsip pemisahan tanggung jawab (*separation of concerns*) yang sangat fundamental dalam arsitektur MVT. Ketika data dipisahkan dari lapisan tampilan, *template* hanya berfokus pada struktur visual dan antarmuka pengguna, sementara *model* bertindak sebagai sumber kebenaran data (*single source of truth*). Pendekatan ini berdampak besar pada kemudahan pemeliharaan aplikasi; jika di kemudian hari terdapat pembaruan informasi seperti perubahan deskripsi proyek, judul pengalaman, atau penambahan portofolio baru, pengembang tidak perlu lagi menyentuh kode HTML secara manual. Seluruh pembaruan data dapat dilakukan secara aman dan cepat melalui antarmuka *Admin Panel* atau perintah basis data tanpa risiko merusak struktur desain yang sudah ada.

Dampaknya terhadap pengembangan aplikasi di masa depan juga sangat signifikan, terutama dari segi skalabilitas dan fleksibilitas. Dengan memanfaatkan perulangan dinamis pada Django Template Language, halaman web dapat menyesuaikan jumlah konten secara otomatis sebanyak apa pun data yang ada di dalam basis data. Selain itu, penyimpanan data secara terstruktur pada *model* memungkinkan data tersebut untuk digunakan kembali (*reusable*) pada berbagai kebutuhan fitur lain secara efisien. Sebagai contoh, data portofolio yang sama kelak dapat dengan mudah diintegrasikan ke dalam fitur pencarian, penyaringan berbasis kategori, hingga penyediaan *endpoint* REST API jika aplikasi ingin dikembangkan ke tingkat yang lebih kompleks, seperti integrasi dengan aplikasi *mobile* atau layanan pihak ketiga.

3. Apa perbedaan fungsi 'makemigrations' dan 'migrate' pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut!
Jawab: **'python manage.py makemigrations'**: Berfungsi untuk **menyiapkan dan mencatat rancangan cetak biru (*blueprint*)** perubahan struktur model menjadi berkas migrasi baru di dalam folder 'migrations/'. Perintah ini **belum** mengubah struktur tabel fisik pada database. **'python manage.py migrate'**: Berfungsi untuk **mengeksekusi berkas migrasi** yang telah dibuat sebelumnya ke dalam skema database fisik. Perintah ini yang benar-benar membuat, mengubah, atau menghapus tabel/kolom pada database.

**Contoh Perubahan Model:**
Ketika pengembang menambahkan atribut/field baru 'category = models.CharField(max_length=50)' pada model 'Experience' di 'models.py':
1. Wajib menjalankan 'python manage.py makemigrations' untuk membuat berkas '0002_experience_category.py'.
2. Kemudian menjalankan 'python manage.py migrate' agar kolom 'category' benar-benar ditambahkan ke tabel database 'main_experience'.

### AI Tool Disclosure
Dalam pengerjaan Tugas 2 ini, saya menggunakan AI (*Gemini*) sebagai *learning assistant / copilot* untuk:
1. *Brainstorming* ide tata letak antarmuka gaya **Neo-Brutalism** (3D deck card perspective).
2. Membantu penyusunan *unit test* dan pemecahan masalah (*troubleshooting*) saat terjadi kegagalan *assertion test*.

### Tugas 3

1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!
    - **ModelForm**: Memungkinkan Django secara otomatis membuat elemen form HTML berdasarkan struktur field pada model yang sudah kita definisikan. Ini menerapkan prinsip *Don't Repeat Yourself* (DRY), menghemat waktu penulisan kode, serta menangani validasi tipe data dan penyimpanan langsung ke database secara aman dan terstandar.
    - **`{% csrf_token %}`**: Diwajibkan untuk mencegah serangan *Cross-Site Request Forgery* (CSRF). Token rahasia yang digenerate oleh server ini memastikan bahwa request bertipe `POST` benar-benar berasal dari pengguna sah melalui form di aplikasi web kita, bukan dari situs pihak ketiga yang berniat jahat.
   
2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
    - **Ukuran Berkas Lebih Ringan**: JSON menggunakan sintaks key-value sederhana tanpa tag penutup seperti XML, sehingga ukuran payload data lebih kecil dan menghemat bandwith.
    - **Parsing Lebih Cepat**: JSON terintegrasi secara native dengan JavaScript (JavaScript Object Notation), sehingga aplikasi frontend modern dapat memproses data JSON jauh lebih cepat dan mudah dibanding XML yang membutuhkan sintaks DOM Parser relatif kompleks.
    - **Keterbacaan**: Struktur JSON lebih bersih dan lebih gampang dibaca oleh pengembang (*human-readable*).
3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
    - **Alur Data**:
     1. Client (Browser/Frontend) mengirimkan request HTTP GET ke URL endpoint JSON (misalnya `/experience/json/`).
     2. Django mencocokkan URL di `urls.py` dan memanggil fungsi view yang sesuai (misalnya `show_json_experience`).
     3. View mengeksekusi query ORM `Experience.objects.all()` untuk mengambil objek QuerySet dari database.
     4. Objek QuerySet tersebut diserialisasi menjadi format string JSON menggunakan `serializers.serialize("json", data)`.
     5. View mengembalikan response berupa `HttpResponse` bertipe `content_type="application/json"`.
   - **Alasan Serialization**: Objek Python/Django QuerySet bersifat *complex Python objects* yang tidak bisa langsung dikirim via protokol HTTP atau dibaca oleh browser. Serialization berfungsi mengubah/menerjemahkan objek kompleks Django tersebut menjadi format standar teks murni (JSON) yang dapat ditransmisikan via jaringan dan dimengerti oleh sistem lain.

### AI Disclosure Statement

- **Tools yang Digunakan**: Gemini.
- **Strategi Prompting**: Memberikan konteks penuh mengenai error terminal (IntegrityError, ImportError), potongan kode `views.py` dan `urls.py`, serta checklist instruksi dari SCELE untuk mendapatkan bimbingan perbaikan bertahap.
- **Bagian yang Dibantu AI**:
  - Penanganan resolusi error migrasi SQLite (`datatype mismatch`) dan perbaikan struktur import pada `urls.py`.
  - Pembuatan fungsi CRUD & JSON delivery pada `views.py` untuk entity `Experience`.
  - Menyusun jawaban atas pertanyaan reflektif Tugas 3 secara komprehensif.
- **Analisis Kritis & Perbaikan Manual**: AI sangat membantu mempercepat penyusunan sintaks boilerplate Django dan isolasi error terminal. Namun, beberapa saran awal seperti pengerjaan prompt manual dalam terminal memerlukan penyesuaian penulisan string Python, sehingga dilakukan langkah reset migrasi secara bersih agar database lokal kembali normal dan konsisten dengan kebutuhan repositori. Selain itu, saya juga me-redo apa yang dikeluarkan oleh AI melalui prompt saya dan mempelajari mengapa kode tersebut bisa tersusun dan memberikan output dengan baik.

### AI Disclosure Statement (Individual Assignment 4)
Dalam pengerjaan Assignment 4 ini, saya menggunakan bantuan AI (Gemini dan Claude) untuk:
1. Membantu perancangan matriks otorisasi (4 Role Access Control) pada sisi Django view dan membantu menyelesaikan kode error pada projects.html.
2. Untuk brainstorming kode error di bagian add projects dan add experiences

*Penyesuaian Manual yang Dilakukan:*
* Menyelaraskan nama endpoint URL dengan struktur urls.py yang sudah ada pada Tugas 3.
* Mempelajari output kode yang dikeluarkan oleh Gemini dan mempelajari mengapa kode tersebut bisa tersusun seperti itu.

### Tugas 5

1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

   Debouncing adalah teknik menunda eksekusi sebuah fungsi sampai pemicunya berhenti terjadi selama jeda waktu tertentu atau syarat tertentu. Setiap ada pemicu baru, timer lama dibatalkan (`clearTimeout`) dan timer baru dimulai (direset kembali ke perhitungan timer awal). Pada pencarian di halaman Experience, fungsi `loadExperiences()` baru dipanggil 400 ms setelah pengguna berhenti mengetik. Tanpa debouncing, mengetik "research" akan mengirim 8 permintaan, satu per huruf. Ini penting karena:
   - **Mengurangi beban server dan database.** Setiap permintaan menjalankan query `LIKE` dan membuat respons JSON. Debouncing mengurangi permintaan yang tidak berguna.
   - **Menghindari respons yang datang tidak berurutan.** Respons untuk "res" bisa tiba setelah respons untuk "research" dan menimpanya dengan hasil yang salah. Selain debouncing, aku menambahkan penanda `latestRequestId` supaya respons lama diabaikan.
   - **UI lebih mulus.** Daftar dan state loading tidak berkedip setiap ketukan tombol, sehingga pengalaman pengguna lebih nyaman dan hemat bandwidth.

2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

   `fetch()` bersifat asinkron dan langsung mengembalikan sebuah `Promise` tanpa menunggu respons jaringan selesai. `await` menjeda eksekusi fungsi `async` sampai Promise itu selesai, lalu memberikan nilai hasilnya, yaitu objek `Response`. Eksekusi yang dijeda hanya fungsi tersebut, sedangkan halaman tetap responsif. Karena itu `await` juga dipakai untuk `response.json()`, yang juga mengembalikan Promise.

   Tanpa `await`, variabel yang kita terima hanyalah objek `Promise`, bukan datanya. Akibatnya:
   - `response.ok` atau `response.json()` dipanggil pada Promise, bukan pada `Response`, sehingga muncul `undefined` atau error (misalnya `data.results.map is not a function`).
   - Kode setelahnya berjalan lebih dulu, sehingga state loading langsung hilang atau daftar dirender dari data kosong sebelum respons tiba.
   - Error jaringan tidak tertangkap oleh `try/catch` karena penolakan Promise terjadi di luar blok tersebut. Hasilnya `unhandled promise rejection`, dan state error tidak pernah muncul.

3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

   XSS adalah serangan ketika penyerang berhasil menyisipkan kode JavaScript ke halaman yang kemudian dijalankan di browser korban. Contohnya, data berisi `<img src="x" onerror="alert('XSS!')">` yang disimpan ke database. Skrip itu berjalan dengan hak akses halaman kita, sehingga bisa mencuri cookie sesi, memalsukan aksi pengguna, atau mengalihkan halaman.

   Data lewat AJAX lebih rentan karena **perlindungan otomatis Django tidak berlaku di sana**:
   - Template Django melakukan *autoescape*. `{{ exp.title }}` mengubah `<` menjadi `&lt;`, sehingga tag tampil sebagai teks biasa.
   - Pada AJAX, server hanya mengirim JSON mentah. JSON bukan HTML, jadi tidak ada escaping HTML otomatis. Kita yang merakit HTML di JavaScript. Jika nilai dimasukkan ke `innerHTML` lewat template literal tanpa escape, browser menguraikannya sebagai markup dan `onerror` ikut berjalan.
   - Kerentanan ini mudah terlewat karena kodenya terlihat wajar (`` `<h2>${exp.title}</h2>` ``) dan semua nilai harus di-escape secara manual satu per satu.

   Karena itu aku memakai pertahanan berlapis. Di klien, semua teks melewati `escapeHtml()` dan URL difilter `safeUrl()` (hanya http/https). Di server, `strip_tags` membersihkan input di `clean_title` dan `clean_description`, sehingga input berisi tag ditolak atau dibersihkan sebelum disimpan.


### AI Disclosure (Individual Assignment 5)

- **Tools yang digunakan:** Claude (Claude Code) dan Gemini AI.
- **Bagian yang dibantu AI:**
  - Endpoint JSON, view POST dengan status 201/400/403, endpoint star, dan endpoint hapus untuk Experience.
  - `static/js/experience.js` (AJAX, debouncing, modal, toast) dan `static/js/utils.js` (`getCookie`, `escapeHtml`, `safeUrl`).
  - `clean_title` dan `clean_description` dengan `strip_tags`, migrasi `0005`, serta unit test.
  - Draf jawaban pertanyaan reflektif di atas.
- **Keterbatasan AI yang ditemukan:**
  - Komponen `toast.html` lama tidak cocok dengan `toast.js`: id elemennya berbeda dan `toast.js` tidak pernah dimuat di `base.html`. Claude menyelaraskannya.
  - Test lama `test_projects_content_display` dan `test_experience_content_display` mengecek HTML server-side, padahal halamannya sudah AJAX, jadi tes itu diubah.
  - Claude tidak bisa menjalankan `runserver` di lingkungannya (tidak ada akses ke PyPI). JavaScript-nya diuji di Chromium dengan endpoint tiruan, tetapi Python/Django dan migrasi harus dijalankan dan diuji sendiri.
- **Penyesuaian dan pengujian manual:** hasil kerja Claude dibaca, dijalankan, dan diuji di browser untuk peran superuser, Editor, user biasa, dan pengunjung, termasuk payload XSS `<img src="x" onerror="alert('XSS!')">` (daftar uji di bawah).

### Tugas 6

1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan `PUT` dan `PATCH` beserta contoh kapan masing-masing sebaiknya digunakan!

REST (*Representational State Transfer*) merupakan pendekatan dalam merancang API agar komunikasi antara client dan server dapat dilakukan secara terstruktur. Dalam REST, data atau objek yang dikelola disebut sebagai resource dan setiap resource memiliki alamat atau URL tersendiri. REST juga memanfaatkan HTTP method seperti `GET`, `POST`, `PUT`, `PATCH`, dan `DELETE` untuk menentukan tindakan apa yang ingin dilakukan terhadap resource tersebut.

Mengembalikan data dalam format JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful. JSON hanya merupakan format pertukaran data, sedangkan REST memiliki prinsip dan aturan dalam mengatur komunikasi antara client dan server sehingga API yang mengembalikan JSON belum tentu mengikuti prinsip REST. Sebuah API perlu memperhatikan penggunaan URL untuk mengidentifikasi resource, HTTP method yang sesuai dengan tindakan yang dilakukan, serta HTTP status code untuk menunjukkan hasil dari suatu request.

Perbedaan antara `PUT` dan `PATCH` terletak pada cara keduanya memperbarui data. `PUT` digunakan untuk memperbarui representasi resource secara keseluruhan, sedangkan `PATCH` digunakan apabila hanya sebagian data yang ingin diperbarui.

Sebagai contoh, jika sebuah data pengalaman memiliki field `title`, `description`, dan `category`, penggunaan `PUT` berarti client mengirimkan representasi data secara lengkap ketika melakukan pembaruan. Sementara itu, jika hanya ingin mengganti `title`, client dapat menggunakan `PATCH` tanpa harus mengirimkan seluruh field lainnya. Dengan demikian, `PUT` lebih sesuai untuk pembaruan keseluruhan resource, sedangkan `PATCH` lebih praktis untuk perubahan pada field tertentu saja.

2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan `JsonResponse` seperti pada Tutorial 05?

Serializer merupakan komponen dalam Django REST Framework yang berfungsi untuk mengubah data dari model Django menjadi format yang dapat dikirim melalui API, seperti JSON. Selain itu, serializer juga bertugas memeriksa dan memvalidasi data yang dikirimkan oleh client sebelum data tersebut diproses atau disimpan ke database.

Dalam proyek ini, saya menggunakan `ModelSerializer` untuk mengelola data Experience. Dengan `ModelSerializer`, struktur field dapat disesuaikan dengan model yang sudah dibuat sehingga proses pengelolaan data menjadi lebih terorganisasi. Saya juga dapat menentukan field yang hanya boleh dibaca (*read-only*), seperti `star_count` dan `is_starred`, karena kedua field tersebut merupakan informasi hasil perhitungan yang tidak seharusnya diubah secara langsung oleh client.

Dibandingkan dengan membuat dictionary secara manual menggunakan `JsonResponse` seperti pada Tutorial 05, penggunaan serializer memberikan beberapa keuntungan. Pada pendekatan manual, developer harus menentukan sendiri data yang akan dimasukkan ke dalam dictionary serta mengatur validasinya. Jika jumlah field bertambah, proses tersebut dapat menjadi lebih panjang dan sulit dikelola.

Dengan serializer, proses konversi data, pengaturan field, dan validasi dapat dilakukan dengan lebih terstruktur. Hal ini membuat kode lebih mudah dibaca, dikembangkan, dan dipelihara, terutama ketika API memiliki banyak jenis data dan operasi.

3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?

Autentikasi (*authentication*) merupakan proses untuk memastikan identitas pengguna yang mengakses aplikasi. Dalam Django REST Framework, proses ini digunakan untuk mengetahui apakah pengguna sudah terautentikasi dan akun mana yang sedang melakukan request.

Sementara itu, otorisasi (*authorization*) merupakan proses untuk menentukan tindakan apa saja yang boleh dilakukan oleh pengguna berdasarkan hak akses atau perannya. Sebagai contoh, pada proyek ini terdapat beberapa tingkat hak akses, yaitu pengunjung anonim yang hanya dapat melihat data, pengguna biasa (dengan catatan sang pengguna sudah login) yang dapat melihat data dan memberikan atau membatalkan star, Editor yang memiliki tambahan hak untuk mengubah data, serta pemilik portofolio yang memiliki seluruh hak akses termasuk membuat dan menghapus data.

Pemeriksaan hak akses perlu dilakukan di sisi server menggunakan permission class karena menyembunyikan tombol pada template hanya memengaruhi tampilan antarmuka. Hal tersebut tidak benar-benar mencegah pengguna melakukan request secara langsung ke endpoint API. Pengguna masih dapat mencoba mengirimkan request melalui browser console atau aplikasi lain meskipun tombol tertentu tidak ditampilkan pada halaman.

Oleh karena itu, server tetap harus memeriksa izin setiap kali menerima request. Dengan menggunakan permission class, aturan hak akses dapat diterapkan secara konsisten sehingga pengguna hanya dapat melakukan tindakan yang memang diperbolehkan untuk perannya. Hal ini juga membuat pengaturan keamanan lebih terstruktur karena logika hak akses tidak hanya bergantung pada tampilan frontend.

4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai `SessionAuthentication`! Mengapa test yang memakai `force_authenticate` tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

CSRF (*Cross-Site Request Forgery*) merupakan jenis serangan yang memanfaatkan kondisi ketika pengguna sedang login pada suatu website untuk membuat browser mengirimkan request yang tidak diinginkan ke website tersebut.

Pada Django REST Framework, `SessionAuthentication` menggunakan session pengguna untuk melakukan autentikasi. Karena browser dapat mengirimkan cookie session secara otomatis, terdapat kemungkinan website lain mencoba memanfaatkan session tersebut untuk mengirimkan request tanpa sepengetahuan pengguna.

Oleh karena itu, token CSRF diperlukan sebagai perlindungan tambahan, terutama untuk request yang mengubah data seperti `POST`, `PUT`, `PATCH`, dan `DELETE`. Token ini membantu server memastikan bahwa request yang mengubah data berasal dari konteks aplikasi yang sah, bukan sekadar request yang dikirim dengan memanfaatkan cookie session pengguna.

Pengujian menggunakan `force_authenticate` saja tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan karena metode tersebut secara langsung mengatur pengguna yang dianggap sudah terautentikasi dalam test. Dengan demikian, proses autentikasi normal melalui `SessionAuthentication` yang berkaitan dengan pemeriksaan CSRF tidak benar-benar diuji.

Untuk menguji perlindungan CSRF, diperlukan `APIClient` dengan `enforce_csrf_checks=True` dan autentikasi melalui session, misalnya menggunakan `.login()`. Setelah itu, request yang mengubah data dapat dicoba tanpa menyertakan token CSRF. Apabila perlindungan berjalan dengan benar, request tersebut seharusnya ditolak oleh server.

### AI Disclosure

Dalam pengerjaan Individual Assignment 6, saya menggunakan ChatGPT dan Claude AI sebagai alat bantu untuk memahami materi dan membantu proses pengembangan aplikasi menggunakan Django REST Framework serta memahami dengan baik goals yang harus dicapai pada Individual Assignment 6 ini.

ChatGPT digunakan untuk membantu menjelaskan konsep REST API, serializer, permission class, autentikasi, otorisasi, validasi data, serta perlindungan CSRF. Sedangkan Claude AI saya gunakan untuk membantu dalam membaca pesan error, memahami kemungkinan penyebab masalah, dan memberikan arahan ketika melakukan implementasi maupun pengujian fitur API.

Strategi yang saya gunakan adalah memberikan konteks proyek, mengirimkan potongan kode atau pesan error yang ditemukan, kemudian meminta penjelasan dan arahan secara bertahap. Saya juga meminta penjelasan mengenai fungsi setiap bagian kode agar dapat memahami alasan penggunaannya, bukan hanya menyalin implementasi yang diberikan.

Berikut merupakan ringkasan prompt yang digunakan selama pengerjaan Tugas 6:

| No. | AI Tool | Ringkasan Prompt | Tujuan Penggunaan |
|---|---|---|---|
| 1 | ChatGPT | Meminta penjelasan mengenai konsep REST API, serializer, dan perbedaan antara serialisasi dengan validasi data secara umum. | Memahami konsep dasar Django REST Framework sebelum mengimplementasikannya. |
| 2 | ChatGPT | Meminta panduan bertahap untuk memahami dan mengimplementasikan permission class serta pembagian hak akses berdasarkan role pengguna. | Membantu menerapkan aturan akses untuk anonymous user, authenticated user, Editor, dan portfolio owner. |
| 3 | ChatGPT | Meminta bantuan memahami validasi input menggunakan `validate_<field>` dan fungsi `strip_tags`. | Memastikan data yang diterima API divalidasi dan tidak mengandung HTML tags yang tidak diinginkan. |
| 4 | ChatGPT | Meminta bantuan memahami error yang muncul selama implementasi dan pengujian API, disertai potongan kode atau pesan error yang relevan. | Mengidentifikasi penyebab error dan menentukan langkah perbaikan. |
| 5 | ChatGPT | Meminta penjelasan mengenai perbedaan PUT dan PATCH, authentication dan authorization, serta mekanisme CSRF pada SessionAuthentication. | Memahami konsep yang diperlukan untuk menjawab pertanyaan reflektif Tugas 6. |
| 6 | Claude | Meminta bantuan menganalisis kode dan error yang muncul selama pengerjaan, serta mendapatkan arahan untuk implementasi dan pengujian. | Membantu proses debugging dan memahami solusi yang dapat diterapkan pada proyek. |

**Strategi penggunaan AI:**

Saya memberikan konteks proyek, potongan kode, serta pesan error yang ditemukan agar AI dapat memberikan bantuan yang relevan. Saya juga meminta penjelasan mengenai konsep yang belum dipahami, bukan hanya meminta kode jadi.

**Kontribusi mandiri:**

Saya menyadari bahwa jawaban dan saran dari AI tidak selalu langsung sesuai dengan kondisi proyek. Beberapa saran perlu diperiksa kembali dan disesuaikan dengan struktur model, URL, serta implementasi yang sudah ada. Oleh karena itu, ChatGPT dan Claude AI digunakan sebagai pendamping belajar dan debugging, sedangkan keputusan akhir mengenai kode dan hasil implementasi tetap melalui pemeriksaan serta pengujian pada proyek saya sendiri.
