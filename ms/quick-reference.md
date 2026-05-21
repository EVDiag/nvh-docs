# NVH Source Locator — Rujukan Pantas

Peringatan satu halaman. Untuk butiran penuh, lihat **Panduan Pengguna**.

---

## Aliran utama (2-Sensor, percuma)

1. **Pilih bahan** — tab Materials → ketik bahan anda
2. **Masukkan tentukuran** pada tab 2-Sensor:
   - Jarak sensor (`d`)
   - Kelewatan masa tentukuran (`tCal`) — diisi automatik daripada bahan
3. **Masukkan peristiwa** — `tEvent` dan Sensor pertama (A atau B)
4. **Baca keputusan** — jarak dari sensor A

![Tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Semua tab

| Tab | Output | Medan Pro? |
|---|---|---|
| 2-Sensor | Jarak sepanjang garis | Tidak (sepenuhnya percuma) |
| 3-Sensor | X, Y pada permukaan | Ya |
| 3-Sen+ | X, Y dengan LSQ pada 3 pasang | Ya |
| 4-Sensor | X, Y dari dua pasang (A–B + C–D) | Ya |
| 4-Sen+ | X, Y dari 4 sensor, kedudukan bebas | Ya |
| 3D | X, Y, Z dari 4 sensor | Ya |
| 3D+ | X, Y, Z dari sehingga 6 sensor | Ya |
| Materials | Pemilih kelajuan bunyi | Tidak |
| Help | Tutorial | Tidak |

Tetapan adalah ikon ⚙ (kanan atas), bukan tab.

---

## Pampasan suhu

Tetapan → Suhu rujukan, julat **-40 hingga +200 °C**.

- **14 logam** mempunyai pampasan terbina dalam (aluminium, keluli, kuprum, tembaga, gangsa, titanium, magnesium, plumbum, zink, nikel, tungsten, besi, besi tuang)
- Bahan tanpa pampasan menunjukkan **"ref only"**
- **Set semula kepada 20 °C setiap kali aplikasi dilancarkan** (mula-selamat-lalai)
- Memainkan semula entri sejarah memulihkan suhu asalnya

---

## Pintasan

- **Ketik bahan** → mengisi automatik semua medan `tCal` di semua tab
- **Tahan +/-** pada medan nombor → kenaikan cepat
- **Seret mendatar** pada medan nombor → ubah nilai
- **Input kosong/negatif/sampah** → menjadi 0 apabila kabur (input suhu dihadkan -40/200)
- **Bintangkan bahan** → memindahkan ke atas pemilih

---

## Model Pro

**Freemium dikunci-ciri** ($19.99):
- Percuma: tab 2-Sensor berfungsi sepenuhnya, tiada had
- Pro: tab lain boleh diakses tetapi mempunyai **medan kunci-emas** yang memaparkan paywall apabila diketik

Pro membuka: 3-Sensor hingga 3D+, bahan tersuai, sandaran/pemulihan, laporan PDF, anotasi foto.

![Paywall](../screenshots/07-paywall.png)

---

## Laporan & Sandaran

Butang **Cetak keputusan** pada mana-mana skrin keputusan → PDF dengan pengepala, input, keputusan, visualisasi, foto (jika diambil), dan pengaki suhu (apabila pampasan aktif).

Sesuaikan pengepala dalam Tetapan → Pengepala laporan.

**Sandaran**: Tetapan → Sandaran → kongsi ke awan/e-mel.  
**Pemulihan**: Tetapan → Pemulihan → pilih fail sandaran.

---

## Memulihkan Pro pada peranti baru

Akaun Google yang sama (Android) atau Apple ID (iOS) yang anda gunakan untuk membeli → Tetapan → **Pulihkan pembelian** → membuka kunci dalam saat.

Pemulihan automatik berlaku secara senyap apabila anda kembali ke aplikasi selepas menebus kod promosi secara luaran.

---

## Penyelesaian masalah pantas

- **Keputusan di luar julat?** Semak tanda `tEvent` / Sensor pertama / jarak sensor
- **Bahan terdekat salah?** Suhu rujukan mungkin tidak sengaja ditetapkan — semak Tetapan
- **Pulihkan pembelian gagal?** Sahkan akaun kedai yang sama; pasang semula jika berterusan
- **Medan menjadi 0?** Input kosong/negatif auto-snap apabila kabur — masukkan semula nilai
- **Butang stepper hilang?** Muncul di sebelah medan dengan `data-step` — mulakan semula aplikasi jika hilang
- **Amaran suhu lapuk?** Set semula kepada 20 setiap pelancaran — tetapkan semula untuk sesi ini

---

Hubungi `support@evdiag.net` — sertakan model peranti, versi aplikasi (Tetapan → bawah), dan penerangan tentang apa yang anda cuba.
