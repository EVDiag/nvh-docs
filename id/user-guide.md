# NVH Source Locator — Panduan Pengguna

NVH Source Locator adalah alat pengukuran untuk menemukan sumber kebisingan dan getaran menggunakan TDOA (Time Difference of Arrival) dari sinyal akselerometer yang ditangkap pada osiloskop atau sistem pengukuran.

Panduan ini mencakup semua fitur. Untuk penyegar cepat, lihat `quick-reference.md`.

---

## Daftar Isi

1. [Cara kerjanya](#how-it-works)
2. [Sebelum Anda mulai](#before-you-start)
3. [Tab utama](#the-main-tabs)
4. [Mode 2-Sensor](#2-sensor-mode)
5. [Mode 3-Sensor](#3-sensor-mode)
6. [Mode Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Tab Materials](#the-materials-tab)
8. [Kompensasi suhu](#temperature-compensation)
9. [Anotasi foto](#photo-annotation)
10. [Laporan](#reports)
11. [Cadangan dan pemulihan](#backup-and-restore)
12. [Pengaturan](#settings)
13. [Fitur Pro](#pro-features)
14. [Tab Help dan tutorial](#help-tab-and-tutorials)
15. [Pemecahan masalah](#troubleshooting)

---

## Cara kerjanya

Ketika sumber kebisingan memancarkan suara atau getaran, gelombang merambat melalui material dengan kecepatan yang diketahui. Jika Anda menempatkan dua atau lebih akselerometer pada material dan mengukur kapan gelombang tiba di masing-masing, perbedaan waktu memberi tahu Anda di mana sumbernya berada.

NVH Source Locator mengambil:

- **Kalibrasi**: jarak antara sensor dan waktu yang dibutuhkan gelombang untuk menempuh jarak itu (digunakan untuk menghitung kecepatan suara material)
- **Peristiwa**: perbedaan waktu antara sensor yang mendeteksi peristiwa kebisingan/getaran

Kemudian menghitung di mana sumber berada di struktur.

Semakin banyak sensor yang Anda gunakan, semakin akurat Anda dapat menentukan sumbernya:

- **2 sensor** → jarak sepanjang garis
- **3 sensor** → posisi pada permukaan 2D (X, Y)
- **4 sensor** → posisi dalam ruang 3D (X, Y, Z)

---

## Sebelum Anda mulai

Anda akan membutuhkan:

- **Osiloskop atau sistem pengukuran** yang dapat menampilkan perbedaan waktu antara saluran akselerometer dalam mikrodetik (µs)
- **Setidaknya 2 akselerometer** terpasang secara fisik ke struktur (lebih banyak sensor = akurasi lebih tinggi)
- **Cara mengukur jarak** antara sensor (pita ukur, jangka sorong)
- **Cara memicu gelombang** di lokasi yang diketahui untuk kalibrasi (benturan palu yang dikalibrasi, ketukan obeng, atau sinyal lain yang diketahui)

![Layar utama dengan tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tab utama

Aplikasi memiliki tab di bagian atas:

![Bilah tab](../screenshots/02-tab-bar.png)

| Tab | Apa yang dilakukannya | Kapan menggunakan |
|---|---|---|
| **2-Sensor** | Lokalisasi sumber 1D sepanjang garis antara 2 sensor | Pemeriksaan cepat, struktur mirip balok. **Sepenuhnya gratis.** |
| **3-Sensor** | Lokalisasi sumber 2D menggunakan 3 sensor dalam segitiga | Penggunaan paling umum, panel dan permukaan |
| **3-Sen+** | 3-Sensor dengan solver kuadrat terkecil yang ditentukan berlebih | Pengukuran lebih menuntut, tahan kebisingan |
| **4-Sensor** | Lokalisasi 2D menggunakan dua pasangan (A-B + C-D) | Tata letak sensor persegi panjang, pemeriksaan silang |
| **4-Sen+** | Mode 2D lanjutan, 4 sensor di posisi mana pun | Geometri non-persegi panjang, LSQ penuh |
| **3D** | Lokalisasi sumber 3D menggunakan 4 sensor dengan koordinat XYZ | Struktur kompleks dalam ruang 3D |
| **3D+** | 3D dengan hingga 6 sensor, LSQ yang ditentukan berlebih | Geometri sangat kompleks, presisi maksimum |
| **Materials** | Pustaka kecepatan suara + material kustom | Pilih sekali per sesi pengukuran |
| **Help** | Tutorial dalam aplikasi dan referensi | Saat Anda membutuhkan penyegar cepat |

> **Gratis vs Pro**: Tab 2-Sensor sepenuhnya gratis. Tab lain dapat diakses tetapi memiliki bidang input tertentu yang dikunci untuk pengguna Pro (ditandai dengan lencana gembok emas). Mengetuk bidang yang terkunci menampilkan paywall Pro.

Pengaturan diakses melalui ikon roda gigi ⚙ di sudut kanan atas (bukan tab).

---

## Mode 2-Sensor

Pengukuran paling sederhana: lokalisasi sumber sepanjang garis antara dua akselerometer.

![Tab 2-Sensor](../screenshots/01-home-2sensor.png)

### Langkah 1: Terapkan material

Ketuk tab Materials. Pilih material yang membuat struktur Anda (misalnya "Aluminium", "Baja, Mild (1020)"). Aplikasi menggunakan kecepatan suara material yang diketahui untuk mengisi bidang waktu kalibrasi secara otomatis.

Jika material struktur Anda tidak ada dalam daftar, Anda dapat sementara memilih "Udara" dan menimpa waktu kalibrasi secara manual di langkah 2.

### Langkah 2: Masukkan data kalibrasi

Pada tab 2-Sensor, Anda akan melihat dua bagian pasangan: **Pasangan A–B** dan **Pasangan A–C** (hanya A–B yang diperlukan jika Anda hanya memiliki 2 sensor).

Untuk setiap pasangan, Anda mengisi:

- **Jarak sensor** (`d`): jarak fisik antara sensor, dalam cm atau inci (diatur di Pengaturan)
- **Penundaan waktu kalibrasi** (`tCal`): waktu untuk gelombang menempuh jarak antara sensor pada kecepatan suara material — terisi otomatis saat Anda memilih material, tetapi Anda dapat menimpa

### Langkah 3: Masukkan waktu peristiwa

- **Penundaan waktu peristiwa** (`tEvent`): perbedaan waktu antara sensor yang mendeteksi peristiwa kebisingan, dalam mikrodetik
- **Sensor pertama**: sensor mana yang mendengar peristiwa terlebih dahulu (A atau B)

### Langkah 4: Baca hasilnya

Aplikasi menampilkan posisi sumber sebagai jarak dari sensor A:
- Hasil = 0: sumber berada di sensor A
- Hasil = jarak: sumber berada di sensor B
- Hasil di antara: sumber berada di antara keduanya
- Hasil di luar: sumber berada di luar salah satu sensor (toast akan memperingatkan)

Kartu hasil menampilkan kedua jarak (dari A, dari B) dan menunjukkan sensor mana yang lebih dekat.

### Langkah 5 (opsional): Anotasi foto

Ketuk **📷 Anotasi foto** untuk mengambil foto pengaturan Anda. Aplikasi menumpangkan penanda untuk sensor A, B dan sumber. Berguna untuk laporan.

---

## Mode 3-Sensor

Menemukan sumber pada bidang 2D menggunakan tiga sensor yang diatur dalam segitiga.

![Tab 3-Sensor](../screenshots/03-3sensor-tab.png)

### Pengaturan

Tempatkan tiga sensor pada struktur Anda membentuk segitiga. Sama sisi, siku-siku, atau sembarang — aplikasi menangani semua geometri.

### Masukkan data

Di bagian **Panjang sisi segitiga**, masukkan jarak fisik untuk ketiga sisi (A–B, A–C, B–C).

Untuk setiap pasangan (A–B dan A–C), masukkan:
- **tCal**: waktu kalibrasi (terisi otomatis dari material)
- **tEvent**: perbedaan waktu terukur untuk peristiwa kebisingan
- **Sensor pertama**: yang mendengarnya terlebih dahulu

### Baca hasilnya

Aplikasi menampilkan posisi sumber sebagai koordinat X, Y relatif terhadap sensor A (sensor A di asal, sensor B di sumbu X). Visualisasi menunjukkan ketiga sensor dan lokasi sumber.

![Hasil segitiga](../screenshots/04-triangle-result.png)

---

## Mode Pro+

Beberapa tab lanjutan menawarkan solver yang ditentukan berlebih dan dimensi yang lebih tinggi:

### 3-Sen+ (Pro)

Pengaturan segitiga yang sama dengan 3-Sensor, tetapi kalibrasi dan ukur ketiga pasangan (A–B, A–C, B–C). Solver menggunakan ketiga TDOA dalam fit kuadrat terkecil — lebih kuat terhadap kebisingan pengukuran dan material anisotropik. Residu per pasangan dilaporkan sehingga Anda dapat menemukan pengukuran yang tidak konsisten.

### 4-Sensor

Tempatkan empat sensor di sekitar area:
- **A–B** = pasangan horizontal (sisi kiri/kanan)
- **C–D** = pasangan vertikal (sisi atas/bawah)

Jalankan pasangan A–B terlebih dahulu (horizontal), lalu pasangan C–D (vertikal). Peta 2D menampilkan persimpangan. Setiap pasangan dikalibrasi secara terpisah — berguna saat material bervariasi di seluruh struktur.

### 4-Sen+ (2D Lanjutan)

Empat sensor di posisi mana pun (tidak dipaksa persegi panjang). Pasangkan A dengan masing-masing B, C, D dan kalibrasi secara terpisah. Solver kuadrat terkecil yang ditentukan berlebih merata-ratakan kebisingan pengukuran per pasangan dan melaporkan residu per pasangan.

### 3D

Pengukuran 3D penuh dengan 4 sensor yang ditempatkan dalam ruang 3D. Masukkan koordinat (X, Y, Z) setiap sensor, ditambah waktu kalibrasi dan peristiwa untuk setiap pasangan (A–B, A–C, A–D).

### 3D+ (Pro)

Seperti 3D tetapi mendukung hingga **6 sensor** (A hingga F) dengan LSQ yang ditentukan berlebih. Presisi maksimum untuk geometri 3D yang kompleks.

---

## Tab Materials

Pustaka material rekayasa umum dengan kecepatan suara yang diketahui pada 20 °C.

![Tab Materials](../screenshots/05-materials-tab.png)

### Daftar material

Daftar mencakup udara, fluida, karet, polimer, kayu, kaca, dan logam. Kecepatan berkisar dari ~340 m/s (udara) hingga ~13.000 m/s (beberapa logam pada suhu kamar).

### Material bawaan dengan kompensasi suhu

14 logam yang umum digunakan menyertakan data koefisien suhu. Ketika Suhu referensi di Pengaturan berbeda dari 20 °C, aplikasi secara otomatis menyesuaikan kecepatan material ini:

- Aluminium
- Baja, Mild (1020)
- Baja Tahan Karat (304)
- Besi (cor)
- Besi
- Tembaga
- Kuningan
- Perunggu
- Titanium
- Magnesium
- Timbal
- Seng
- Nikel
- Tungsten

Material dengan kompensasi menampilkan dua nilai di pemilih: **kecepatan terkompensasi** (besar, menonjol) dan **kecepatan referensi pada 20 °C** (kecil, abu-abu di bawah).

Material tanpa kompensasi menampilkan **"ref only"** dalam huruf miring — kecepatan tercantum mereka digunakan apa adanya terlepas dari suhu.

### Material kustom

Jika Anda mengukur kalibrasi di tab 2-Sensor, Anda dapat menyimpan hasilnya sebagai material kustom. Setelah pengukuran 2-sensor yang berhasil, cari opsi untuk menyimpan kecepatan turunan di bawah nama pilihan Anda.

Material kustom menyimpan kecepatan yang diukur in-situ; mereka tidak pernah menerapkan kompensasi suhu (kecepatan sudah diukur pada suhu pengujian).

### Favorit

Ketuk bintang di samping material apa pun untuk menandainya sebagai favorit. Favorit muncul di bagian atas daftar untuk akses cepat.

### Pencarian

Gunakan bilah pencarian di bagian atas untuk memfilter material berdasarkan nama. Pencarian cocok dengan nama kanonik Inggris dan nama tampilan yang diterjemahkan.

---

## Kompensasi suhu

Kecepatan suara dalam material berubah dengan suhu. Dalam pengujian NVH otomotif, ini penting: ruang mesin pada 80 °C, kabin yang direndam dingin pada -10 °C, atau area manifold buang pada 200 °C semuanya berperilaku berbeda dari kondisi laboratorium suhu kamar.

### Mengatur suhu

Buka Pengaturan (ikon ⚙) → Suhu referensi. Masukkan suhu lingkungan pengujian Anda dalam °C (rentang -40 hingga +200).

![Panel Pengaturan](../screenshots/06-settings.png)

### Apa yang terjadi ketika suhu ≠ 20 °C

- Bidang waktu kalibrasi terisi otomatis dengan kecepatan yang disesuaikan dengan suhu
- Pemilih Materials secara mencolok menampilkan kecepatan yang disesuaikan
- Toast mengonfirmasi: *"Aluminium diterapkan (6.284 m/s @ 60 °C) — N pasangan diperbarui"*
- Petunjuk "Material terdekat" membandingkan dengan kecepatan yang disesuaikan dengan suhu
- Entri riwayat tersimpan mencatat suhu aktif
- Laporan menyertakan baris footer: *"Suhu referensi: 60 °C, kompensasi diterapkan"*

### Reset saat aplikasi diluncurkan

Suhu referensi **selalu direset ke 20 °C** saat Anda meluncurkan aplikasi. Ini mencegah pengaturan basi dari sesi pengukuran masa lalu memengaruhi pekerjaan hari ini secara diam-diam. Catatan miring kecil di Pengaturan mengingatkan Anda tentang perilaku ini.

Jika Anda ingin memutar ulang pengukuran historis pada suhu aslinya, cukup ketuk entri — suhu dipulihkan secara otomatis.

### Material tanpa kompensasi

Sebagian besar material non-logam tidak memiliki koefisien suhu yang dipublikasikan dengan andal. Aplikasi menampilkan lencana **"ref only"** untuk ini — kecepatan tercantum mereka digunakan terlepas dari pengaturan suhu. Jika Anda memerlukan pengukuran akurat pada suhu non-kamar untuk material ini, lakukan kalibrasi in-situ dan simpan hasilnya sebagai material kustom.

---

## Anotasi foto

Setelah perhitungan yang berhasil, ketuk tombol **📷 Anotasi foto** untuk menumpangkan penanda sensor dan sumber pada foto pengaturan Anda.

![Anotasi foto](../screenshots/08-photo-annotation.png)

### Alur

1. Ketuk **Anotasi foto** — kamera sistem terbuka
2. Ambil foto penempatan sensor Anda
3. Aplikasi memuat foto ke dalam overlay anotasi
4. Penanda sensor (A, B, C, D, E, F sesuai berlaku — hingga 6 sensor) dan penanda sumber ditempatkan secara otomatis berdasarkan perhitungan Anda
5. Seret penanda apa pun untuk menyesuaikan posisi. Saat Anda menyesuaikan, posisi sumber dihitung ulang dari posisi sensor yang dikoreksi
6. Ketuk **Simpan** untuk menyimpan, atau **Ambil ulang** untuk mencoba lagi

Foto beranotasi secara otomatis disertakan dalam laporan PDF.

---

## Laporan

Ketuk tombol **Cetak hasil** pada layar hasil apa pun untuk menghasilkan laporan yang diformat.

![Laporan PDF](../screenshots/09-pdf-report.png)

### Konten laporan

- Header (dapat disesuaikan di Pengaturan → Header laporan)
- Judul pengukuran dan stempel waktu
- Semua nilai input dalam tabel yang rapi
- Hasil perhitungan
- Teks kesimpulan
- Visualisasi (plot geometri)
- Foto beranotasi (jika Anda mengambilnya)
- Baris footer suhu (jika kompensasi aktif)
- Nomor halaman dan baris kredit

### Format output

- **Android**: pembuatan PDF asli, simpan ke ponsel atau bagikan
- **iOS**: dialog cetak sistem → simpan sebagai PDF, AirPrint, atau bagikan

### Menyesuaikan header

Pengaturan → Header laporan. Masukkan nama perusahaan Anda, nama lab, info proyek, atau apa pun yang Anda inginkan di bagian atas setiap laporan.

---

## Cadangan dan pemulihan

Simpan semua material kustom, favorit, pengaturan, dan riwayat Anda ke satu file. Transfer antar perangkat.

### Cadangan

Pengaturan → **Cadangan** → ketuk "Simpan file cadangan". Aplikasi menghasilkan file JSON dan membuka sheet berbagi ponsel Anda. Simpan ke cloud drive Anda (Google Drive, iCloud, OneDrive), email ke diri sendiri, atau transfer dengan cara apa pun yang Anda suka.

### Pemulihan

Pengaturan → **Pemulihan** → pilih file cadangan dari penyimpanan ponsel Anda. Aplikasi mengimpor material kustom, favorit, riwayat, dan pengaturan.

⚠️ **Pemulihan menggantikan data Anda saat ini.** Jika Anda memiliki pengukuran penting di perangkat saat ini, cadangkan terlebih dahulu sebelum memulihkan dari cadangan yang berbeda.

---

## Pengaturan

Diakses melalui ikon roda gigi ⚙ di sudut kanan atas. Pengaturan adalah modal, bukan tab.

![Pengaturan](../screenshots/06-settings.png)

| Pengaturan | Apa yang dikontrolnya |
|---|---|
| **Tingkatkan ke Pro** | Beli atau pelajari tentang fitur Pro ($19,99) |
| **Bahasa** | Bahasa tampilan aplikasi (30 didukung) |
| **Tema** | Terang, Gelap, atau Otomatis (ikuti sistem) |
| **Satuan jarak** | cm atau inci |
| **Suhu referensi** | Suhu aktif untuk kompensasi, -40 hingga +200 °C |
| **Header laporan** | Teks khusus di bagian atas laporan yang dihasilkan |
| **Cadangan** | Ekspor semua data ke file |
| **Pemulihan** | Impor data dari file cadangan |
| **Pulihkan pembelian** | Dapatkan kembali Pro di perangkat baru |

---

## Fitur Pro

NVH Source Locator menggunakan **model freemium dengan kunci fitur**:

- **Gratis**: Tab 2-Sensor sepenuhnya berfungsi tanpa batas
- **Pro**: Semua tab lain memiliki bidang input tertentu yang dikunci. Paywall muncul ketika pengguna gratis mengetuk bidang yang terkunci

### Apa yang dikunci

Bidang yang memerlukan Pro tersebar di:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Mode 3D dan 3D+
- Cadangan dan Pemulihan
- Laporan PDF
- Material kustom
- Anotasi foto

Pengguna gratis dapat MEMBUKA tab apa pun dan MELIHAT antarmuka. Mereka hanya tidak dapat memasukkan nilai ke dalam bidang input yang dikunci Pro.

![Bidang yang dikunci Pro](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Ketika pengguna gratis mengetuk bidang yang terkunci, paywall meluncur menampilkan:
- Ikon aplikasi dengan lencana PRO
- Daftar fitur
- Tombol buka kunci dengan harga ($19,99 default; dapat bervariasi menurut wilayah)
- Penukaran kode promo (hanya Android — iOS menggunakan alur Kode Penawaran terpisah Apple)
- Tautan promo opsional ke saluran komunitas

### Membeli Pro

Ketuk bidang yang terkunci, atau ketuk **Tingkatkan ke Pro** di Pengaturan. Menggunakan sistem pembayaran resmi platform Anda (Google Play di Android, Apple App Store di iOS).

### Memulihkan Pro di perangkat baru

Jika Anda membeli di satu perangkat dan menginginkan Pro di perangkat lain (akun yang sama):

1. Masuk ke akun Google **yang sama** (Android) atau Apple ID (iOS) yang Anda gunakan untuk membeli
2. Buka NVH Source Locator di perangkat baru
3. Buka Pengaturan → **Pulihkan pembelian**
4. Aplikasi memverifikasi dengan catatan pembelian platform dan membuka kunci Pro

### Pemulihan otomatis saat diluncurkan

Jika Anda menebus kode promo di Google Play Store atau App Store saat NVH Source Locator berjalan di latar belakang, kembali ke aplikasi secara otomatis mendeteksi pembelian baru dan membuka kunci Pro — tidak diperlukan Pemulihan manual.

### Penukaran kode promo

**Android**: tombol "Punya kode promo Google Play?" di paywall membuka alur penebusan Google Play dengan kode Anda yang sudah terisi sebelumnya.

**iOS**: Kebijakan App Store 3.1.1 memerlukan penebusan melalui alur "Tebus Kode" resmi Apple. Tombol Google Play disembunyikan di iOS. Cari "Tebus kode App Store" di Pengaturan sebagai gantinya.

---

## Tab Help dan tutorial

Tab **Help** mencakup tutorial dalam aplikasi, panduan praktik terbaik, dan informasi referensi.

![Tab Help](../screenshots/10-help-tab.png)

Topik yang dibahas:
- Peralatan apa yang Anda perlukan
- Cara menempatkan sensor untuk akurasi terbaik
- Tip kalibrasi
- Skenario pengukuran umum
- Tip untuk triangulasi dan penempatan 3D
- Perutean kabel dan kualitas sinyal

---

## Pemecahan masalah

### Hasil perhitungan salah atau tidak masuk akal

1. Periksa kalibrasi Anda. `tCal` yang terisi otomatis mengasumsikan kecepatan material yang dipublikasikan — material asli bervariasi. Kalibrasi paling akurat adalah in-situ: ketuk lokasi yang diketahui dan biarkan aplikasi menurunkan kecepatan sebenarnya.
2. Periksa pengaturan **Sensor pertama** — sensor mana yang mendengar peristiwa terlebih dahulu penting untuk matematika.
3. Verifikasi pengukuran jarak Anda. Kesalahan beberapa mm menyebar.

### Toast mengatakan "Hasil di luar rentang"

Matematika mengatakan sumbernya tidak berada di antara sensor Anda. Kemungkinan penyebab:
- Sumber sebenarnya di luar garis/bidang sensor
- Salah satu input Anda salah
- Kecepatan kalibrasi terlalu jauh dari kenyataan

### Petunjuk kecepatan perhitungan menampilkan warna peringatan

Kecepatan suara yang tersirat dari input Anda jauh dari material umum mana pun (kurang dari 50 m/s atau lebih dari 20.000 m/s). Periksa input Anda — kemungkinan kesalahan ketik di tCal atau jarak.

### Pemilih Materials menampilkan kecepatan yang berbeda dari yang diharapkan

Periksa Suhu referensi di Pengaturan. Jika tidak 20 °C, kecepatan yang ditampilkan mencerminkan kompensasi suhu. Aplikasi menampilkan "ref X @ 20°C" di bawah kecepatan terkompensasi sehingga Anda dapat memverifikasi.

### Entri riwayat diputar ulang dengan hasil berbeda

Entri riwayat lama yang dibuat sebelum versi aplikasi 1.75 mungkin tidak menyimpan suhu. Jika Anda mengambil pengukuran pada suhu non-20 °C, pemutaran ulang akan menggunakan pengaturan saat ini. Atur suhu secara manual di Pengaturan sebelum memutar ulang, ATAU ukur ulang.

### Penanda anotasi foto tidak di tempat yang saya harapkan

Penanda ditempatkan secara otomatis berdasarkan geometri input. Seret untuk menyesuaikan. Menyesuaikan penanda memperbarui posisi sumber di overlay foto — tetapi TIDAK mengubah hasil perhitungan yang mendasarinya.

### Cadangan/Pemulihan gagal

Pastikan Anda menggunakan file cadangan yang dihasilkan oleh versi aplikasi yang sama atau lebih baru. File cadangan yang lebih lama mungkin tidak memiliki bidang data saat ini.

### Pulihkan pembelian mengatakan "tidak ada pembelian ditemukan"

1. Verifikasi Anda masuk ke akun toko yang sama dengan yang Anda gunakan untuk membeli
2. Verifikasi pembelian tidak dikembalikan atau kedaluwarsa
3. Coba copot pemasangan dan pasang ulang aplikasi (pembelian terikat ke akun toko Anda, bukan pemasangan aplikasi)
4. Hubungi support@evdiag.net jika berlanjut

### Input numerik secara tak terduga melompat ke 0

Berdasarkan desain: ketika Anda keluar fokus dari bidang numerik (ketuk di tempat lain), jika kosong, negatif, atau berisi teks non-numerik, ia melompat ke 0. Mencegah perhitungan yang rusak secara diam-diam dari input yang dihapus secara tidak sengaja. Input suhu dikecualikan (sebaliknya dikunci ke -40/+200).

### Perlu bantuan lebih lanjut

Hubungi `support@evdiag.net` dengan:
- Model perangkat dan versi OS Anda
- Versi aplikasi (Pengaturan → bagian bawah halaman)
- Deskripsi tentang apa yang Anda coba
- Tangkapan layar jika memungkinkan

---

*NVH Source Locator dikembangkan oleh EVDiag. Kunjungi https://evdiag.net untuk pembaruan dan sumber daya.*
