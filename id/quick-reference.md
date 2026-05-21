# NVH Source Locator — Referensi Cepat

Pengingat satu halaman. Untuk detail lengkap, lihat **Panduan Pengguna**.

---

## Alur utama (2-Sensor, gratis)

1. **Pilih bahan** — tab Materials → ketuk bahan Anda
2. **Masukkan kalibrasi** di tab 2-Sensor:
   - Jarak sensor (`d`)
   - Penundaan waktu kalibrasi (`tCal`) — diisi otomatis dari bahan
3. **Masukkan peristiwa** — `tEvent` dan Sensor pertama (A atau B)
4. **Baca hasil** — jarak dari sensor A

![Tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Semua tab

| Tab | Output | Bidang Pro? |
|---|---|---|
| 2-Sensor | Jarak sepanjang garis | Tidak (sepenuhnya gratis) |
| 3-Sensor | X, Y pada permukaan | Ya |
| 3-Sen+ | X, Y dengan LSQ pada 3 pasang | Ya |
| 4-Sensor | X, Y dari dua pasang (A–B + C–D) | Ya |
| 4-Sen+ | X, Y dari 4 sensor, posisi bebas | Ya |
| 3D | X, Y, Z dari 4 sensor | Ya |
| 3D+ | X, Y, Z dari hingga 6 sensor | Ya |
| Materials | Pemilih kecepatan suara | Tidak |
| Help | Tutorial | Tidak |

Pengaturan adalah ikon ⚙ (kanan atas), bukan tab.

---

## Kompensasi suhu

Pengaturan → Suhu referensi, rentang **-40 hingga +200 °C**.

- **14 logam** memiliki kompensasi bawaan (aluminium, baja, tembaga, kuningan, perunggu, titanium, magnesium, timbal, seng, nikel, tungsten, besi, besi cor)
- Bahan tanpa kompensasi menunjukkan **"ref only"**
- **Reset ke 20 °C setiap kali aplikasi diluncurkan** (mulai-aman-default)
- Memutar ulang entri riwayat memulihkan suhu aslinya

---

## Pintasan

- **Ketuk bahan** → mengisi otomatis semua bidang `tCal` di semua tab
- **Tahan +/-** pada bidang angka → peningkatan cepat
- **Seret horizontal** pada bidang angka → ubah nilai
- **Input kosong/negatif/sampah** → menjadi 0 saat blur (input suhu dibatasi -40/200)
- **Bintangkan bahan** → memindahkan ke atas pemilih

---

## Model Pro

**Freemium terkunci-fitur** ($19,99):
- Gratis: tab 2-Sensor sepenuhnya berfungsi, tanpa batas
- Pro: tab lainnya dapat diakses tetapi memiliki **bidang kunci-emas** yang menampilkan paywall saat diketuk

Pro membuka kunci: 3-Sensor hingga 3D+, bahan kustom, pencadangan/pemulihan, laporan PDF, anotasi foto.

![Paywall](../screenshots/07-paywall.png)

---

## Laporan & Pencadangan

Tombol **Cetak hasil** di layar hasil mana pun → PDF dengan header, input, hasil, visualisasi, foto (jika diambil), dan footer suhu (saat kompensasi aktif).

Sesuaikan header di Pengaturan → Header laporan.

**Pencadangan**: Pengaturan → Pencadangan → bagikan ke cloud/email.  
**Pemulihan**: Pengaturan → Pemulihan → pilih file cadangan.

---

## Memulihkan Pro di perangkat baru

Akun Google yang sama (Android) atau Apple ID (iOS) yang Anda gunakan untuk membeli → Pengaturan → **Pulihkan pembelian** → membuka kunci dalam hitungan detik.

Pemulihan otomatis terjadi secara diam-diam saat Anda kembali ke aplikasi setelah menukarkan kode promo secara eksternal.

---

## Pemecahan masalah cepat

- **Hasil di luar rentang?** Periksa tanda `tEvent` / Sensor pertama / jarak sensor
- **Bahan terdekat salah?** Suhu referensi mungkin tidak sengaja disetel — periksa Pengaturan
- **Pulihkan pembelian gagal?** Verifikasi akun toko yang sama; instal ulang jika tetap ada
- **Bidang menjadi 0?** Input kosong/negatif auto-snap saat blur — masukkan kembali nilainya
- **Tombol stepper hilang?** Muncul di samping bidang dengan `data-step` — mulai ulang aplikasi jika hilang
- **Peringatan suhu kedaluwarsa?** Reset ke 20 setiap peluncuran — atur lagi untuk sesi ini

---

Hubungi `support@evdiag.net` — sertakan model perangkat, versi aplikasi (Pengaturan → bawah), dan deskripsi apa yang telah Anda coba.
