Nama: Annisa Saskya Aulia 
NPM: 2506537915 
Kelas : PBP C 

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