# NVH Source Locator — Hızlı Başvuru

Tek sayfalık özet. Tam ayrıntılar için bkz **Kullanım Kılavuzu**.

---

## Temel akış (2-Sensor, ücretsiz)

1. **Bir malzeme seçin** — Materials sekmesi → malzemenize dokunun
2. **Kalibrasyonu girin** 2-Sensor sekmesinde:
   - Sensör aralığı (`d`)
   - Kalibrasyon zaman gecikmesi (`tCal`) — malzemeden otomatik doldurulur
3. **Olayı girin** — `tEvent` ve İlk sensör (A veya B)
4. **Sonucu okuyun** — sensör A'dan uzaklık

![2-Sensor sekmesi](../screenshots/01-home-2sensor.png)

---

## Tüm sekmeler

| Sekme | Çıktı | Pro alanlar? |
|---|---|---|
| 2-Sensor | Çizgi boyunca mesafe | Hayır (tamamen ücretsiz) |
| 3-Sensor | Yüzey üzerinde X, Y | Evet |
| 3-Sen+ | 3 çift üzerinden LSQ ile X, Y | Evet |
| 4-Sensor | İki çiftten X, Y (A–B + C–D) | Evet |
| 4-Sen+ | 4 sensörden X, Y, herhangi bir konum | Evet |
| 3D | 4 sensörden X, Y, Z | Evet |
| 3D+ | En fazla 6 sensörden X, Y, Z | Evet |
| Materials | Ses hızı seçici | Hayır |
| Help | Eğitimler | Hayır |

Ayarlar ⚙ simgesinin altındadır (sağ üst), sekme olarak değil.

---

## Sıcaklık dengelemesi

Ayarlar → Referans sıcaklığı, aralık **-40 ile +200 °C**.

- **14 metal** yerleşik dengeleme içerir (alüminyum, çelikler, bakır, pirinç, bronz, titanyum, magnezyum, kurşun, çinko, nikel, tungsten, demir, dökme demir)
- Dengeleme olmayan malzemeler **"ref only"** gösterir
- **Her uygulama başlangıcında 20 °C'ye sıfırlanır** (varsayılan güvenli başlangıç)
- Bir geçmiş kaydını yeniden oynatma orijinal sıcaklığını geri yükler

---

## Kısayollar

- **Bir malzemeye dokun** → tüm sekmelerdeki tüm `tCal` alanlarını otomatik doldurur
- **+/-'yi basılı tut** sayısal alanlarda → hızlı artırma
- **Yatay sürükle** bir sayısal alanda → değerler arasında geçiş
- **Boş/negatif/geçersiz giriş** → odak kaybında 0'a geçer (sıcaklık alanı -40/200'e sınırlanır)
- **Bir malzemeyi yıldızla** → seçicinin üstüne taşır

---

## Pro modeli

**Özellik kilitli freemium** ($19,99):
- Ücretsiz: 2-Sensor sekmesi tamamen işlevsel, sınırsız
- Pro: Diğer sekmeler erişilebilir ama dokunulduğunda paywall gösteren **altın kilitli alanlara** sahiptir

Pro şunların kilidini açar: 3-Sensor'dan 3D+'a kadar, özel malzemeler, yedekleme/geri yükleme, PDF raporları, fotoğraf açıklaması.

![Paywall](../screenshots/07-paywall.png)

---

## Raporlar ve yedekleme

Herhangi bir sonuç ekranındaki **Sonucu yazdır** düğmesi → başlık, girişler, sonuç, görselleştirme, fotoğraf (çekildiyse) ve sıcaklık altbilgisi (dengeleme aktif olduğunda) ile PDF.

Başlığı Ayarlar → Rapor başlığı altında özelleştirin.

**Yedekleme**: Ayarlar → Yedekleme → buluta/e-postaya paylaş.  
**Geri yükle**: Ayarlar → Geri yükle → yedek dosyasını seç.

---

## Yeni bir cihazda Pro'yu geri yükleme

Satın aldığınız aynı Google hesabı (Android) veya Apple ID (iOS) → Ayarlar → **Satın almayı geri yükle** → saniyeler içinde kilidi açılır.

Bir promosyon kodunu harici olarak kullandıktan sonra uygulamaya geri döndüğünüzde otomatik geri yükleme sessizce gerçekleşir.

---

## Hızlı sorun giderme

- **Sonuç aralık dışında mı?** `tEvent` işaretini / İlk sensörü / sensör aralığını kontrol edin
- **En yakın malzeme yanlış mı?** Referans sıcaklığı muhtemelen yanlışlıkla ayarlanmış — Ayarları kontrol edin
- **Satın alma geri yüklemesi başarısız mı?** Aynı mağaza hesabını doğrulayın; devam ederse yeniden yükleyin
- **Alan 0'a mı geçti?** Boş/negatif girişler odak kaybında otomatik olarak ayarlanır — değeri tekrar girin
- **Adım düğmeleri kayıp mı?** `data-step` olan alanların yanında görünürler — eksiklerse uygulamayı yeniden başlatın
- **Eski sıcaklık uyarısı mı?** Her başlangıçta 20'ye sıfırlanır — bu oturum için tekrar ayarlayın

---

İletişim `support@evdiag.net` — cihaz modelini, uygulama sürümünü (Ayarlar → alt) ve denediğinizin açıklamasını ekleyin.
