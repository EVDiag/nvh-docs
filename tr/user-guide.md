# NVH Source Locator — Kullanım Kılavuzu

NVH Source Locator, osiloskop veya ölçüm sisteminde yakalanan ivmeölçer sinyallerinden TDOA (Time Difference of Arrival) kullanarak gürültü ve titreşim kaynaklarını lokalize etmek için bir ölçüm aracıdır.

Bu kılavuz tüm özellikleri kapsar. Hızlı bir hatırlatma için **Hızlı Başvuru** dosyasına bakın.

---

## İçindekiler

1. [Nasıl çalışır](#how-it-works)
2. [Başlamadan önce](#before-you-start)
3. [Ana sekmeler](#the-main-tabs)
4. [2-Sensor modu](#2-sensor-mode)
5. [3-Sensor modu](#3-sensor-mode)
6. [Pro+ modları (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Materials sekmesi](#the-materials-tab)
8. [Sıcaklık kompanzasyonu](#temperature-compensation)
9. [Fotoğraf açıklaması](#photo-annotation)
10. [Raporlar](#reports)
11. [Yedekleme ve geri yükleme](#backup-and-restore)
12. [Ayarlar](#settings)
13. [Pro özellikler](#pro-features)
14. [Help sekmesi ve öğreticiler](#help-tab-and-tutorials)
15. [Sorun giderme](#troubleshooting)

---

## Nasıl çalışır {#how-it-works}

Bir gürültü kaynağı ses veya titreşim yaydığında, dalga bilinen bir hızda bir malzemeden geçer. Malzeme üzerine iki veya daha fazla ivmeölçer yerleştirir ve dalganın her birine ne zaman ulaştığını ölçerseniz, zaman farkı size kaynağın nerede olduğunu söyler.

NVH Source Locator alır:

- **Kalibrasyon**: sensörler arasındaki mesafe ve bir dalganın bu mesafeyi katetmesi için geçen süre (malzemenin ses hızını hesaplamak için kullanılır)
- **Olay**: gürültü/titreşim olayını algılayan sensörler arasındaki zaman farkı

Daha sonra yapıdaki kaynağın nerede olduğunu hesaplar.

Ne kadar çok sensör kullanırsanız, kaynağı o kadar doğru lokalize edebilirsiniz:

- **2 sensör** → bir çizgi boyunca mesafe
- **3 sensör** → 2D yüzeyde konum (X, Y)
- **4 sensör** → 3D uzayda konum (X, Y, Z)

---

## Başlamadan önce {#before-you-start}

Şunlara ihtiyacınız olacak:

- **İvmeölçer kanalları arasındaki zaman farkını mikrosaniye (µs) cinsinden gösterebilen bir osiloskop veya ölçüm sistemi**
- **En az 2 ivmeölçer** yapıya fiziksel olarak bağlı (daha fazla sensör = daha yüksek hassasiyet)
- **Sensörler arasındaki mesafeyi ölçmek için bir yol** (şerit metre, kumpas)
- **Kalibrasyon için bilinen bir yerde bir dalga tetiklemek için bir yol** (kalibre edilmiş çekiç darbesi, tornavida vuruşu veya diğer bilinen sinyal)

![2-Sensor sekmesi olan ana ekran](../screenshots/01-home-2sensor.png)

---

## Ana sekmeler {#the-main-tabs}

Uygulamanın üst kısmında sekmeler var:

![Sekme çubuğu](../screenshots/02-tab-bar.png)

| Sekme | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| **2-Sensor** | 2 sensör arasında bir çizgi boyunca 1D kaynak lokalizasyonu | Hızlı kontroller, kiriş benzeri yapılar. **Tamamen ücretsiz.** |
| **3-Sensor** | Üçgen şeklinde 3 sensör kullanarak 2D kaynak lokalizasyonu | En genel kullanım, paneller ve yüzeyler |
| **3-Sen+** | Aşırı belirlenmiş en küçük kareler çözücü ile 3-Sensor | Daha zorlu ölçümler, gürültüye dayanıklı |
| **4-Sensor** | İki çift kullanarak 2D lokalizasyon (A-B + C-D) | Dikdörtgen sensör düzenleri, çapraz kontrol |
| **4-Sen+** | Gelişmiş 2D modu, herhangi bir konumda 4 sensör | Dikdörtgen olmayan geometriler, tam LSQ |
| **3D** | XYZ koordinatlı 4 sensör kullanarak 3D kaynak lokalizasyonu | 3D uzayda karmaşık yapılar |
| **3D+** | 6 sensöre kadar 3D, aşırı belirlenmiş LSQ | Çok karmaşık geometriler, maksimum hassasiyet |
| **Materials** | Ses hızı kütüphanesi + özel malzemeler | Her ölçüm oturumunda bir kez seçin |
| **Help** | Uygulama içi öğreticiler ve referans | Hızlı bir hatırlatmaya ihtiyacınız olduğunda |

> **Ücretsiz vs Pro**: 2-Sensor sekmesi tamamen ücretsizdir. Diğer sekmeler erişilebilirdir ancak Pro kullanıcılar için kilitli belirli giriş alanları vardır (altın kilit rozetiyle işaretlenmiştir). Kilitli bir alana dokunmak Pro paywall'ını gösterir.

Ayarlara sağ üst köşedeki ⚙ dişli simgesi aracılığıyla erişilir (sekme değil).

---

## 2-Sensor modu {#2-sensor-mode}

En basit ölçüm: iki ivmeölçer arasında bir çizgi boyunca kaynak lokalizasyonu.

![2-Sensor sekmesi](../screenshots/01-home-2sensor.png)

### Adım 1: Bir malzeme uygulayın

Materials sekmesine dokunun. Yapınızın yapıldığı malzemeyi seçin (örneğin, "Alüminyum", "Çelik, Mild (1020)"). Uygulama, kalibrasyon süresi alanını otomatik olarak doldurmak için malzemenin bilinen ses hızını kullanır.

Yapınızın malzemesi listede değilse, geçici olarak "Hava" seçebilir ve adım 2'de kalibrasyon süresini manuel olarak geçersiz kılabilirsiniz.

### Adım 2: Kalibrasyon verilerini girin

2-Sensor sekmesinde iki çift bölümü göreceksiniz: **Çift A–B** ve **Çift A–C** (yalnızca 2 sensörünüz varsa yalnızca A–B gereklidir).

Her çift için doldurursunuz:

- **Sensör aralığı** (`d`): sensörler arasındaki fiziksel mesafe, cm veya inç olarak (Ayarlar'da ayarlanır)
- **Kalibrasyon zaman gecikmesi** (`tCal`): bir dalganın sensörler arasında malzemenin ses hızında ilerlemek için gereken süre — bir malzeme seçtiğinizde otomatik olarak doldurulur, ancak geçersiz kılabilirsiniz

### Adım 3: Olay zamanını girin

- **Olay zaman gecikmesi** (`tEvent`): gürültü olayını algılayan sensörler arasındaki zaman farkı, mikrosaniye olarak
- **İlk sensör**: olayı ilk hangi sensör duydu (A veya B)

### Adım 4: Sonucu okuyun

Uygulama kaynak konumunu A sensöründen mesafe olarak gösterir:
- Sonuç = 0: kaynak A sensöründe
- Sonuç = mesafe: kaynak B sensöründe
- Sonuç arada: kaynak ikisi arasında
- Sonuç dışarıda: kaynak sensörlerden birinin ötesinde (toast uyaracaktır)

Sonuç kartı her iki mesafeyi de (A'dan, B'den) gösterir ve hangi sensörün daha yakın olduğunu belirtir.

### Adım 5 (isteğe bağlı): Bir fotoğrafı açıklayın

Kurulumunuzun bir fotoğrafını çekmek için **📷 Fotoğrafı açıkla** seçeneğine dokunun. Uygulama A, B sensörleri ve kaynak için işaretler bindirir. Raporlar için yararlı.

---

## 3-Sensor modu {#3-sensor-mode}

Bir üçgen şeklinde düzenlenmiş üç sensör kullanarak 2D düzlemde bir kaynak lokalize eder.

![3-Sensor sekmesi](../screenshots/03-3sensor-tab.png)

### Kurulum

Bir üçgen oluşturarak yapınıza üç sensör yerleştirin. Eşkenar, dik açılı veya farklı kenarlı — uygulama tüm geometrileri işler.

### Verileri girin

**Üçgen kenar uzunlukları** bölümünde, üç kenarın tümü için fiziksel mesafeyi girin (A–B, A–C, B–C).

Her çift (A–B ve A–C) için girin:
- **tCal**: kalibrasyon süresi (malzemeden otomatik doldurulur)
- **tEvent**: gürültü olayı için ölçülen zaman farkı
- **İlk sensör**: hangisi önce duydu

### Sonucu okuyun

Uygulama kaynak konumunu A sensörüne göre X, Y koordinatları olarak gösterir (A sensörü orijinde, B sensörü X ekseninde). Görselleştirme üç sensörü ve kaynak konumunu gösterir.

![Üçgen sonucu](../screenshots/04-triangle-result.png)

---

## Pro+ modları {#pro-modes}

Birkaç gelişmiş sekme aşırı belirlenmiş çözücüler ve daha yüksek boyutluluk sunar:

### 3-Sen+ (Pro)

3-Sensor ile aynı üçgen kurulumu, ancak üç çiftin tümünü (A–B, A–C, B–C) kalibre EDİN ve ölçün. Çözücü, üç TDOA'nın tümünü bir en küçük kareler uyumunda kullanır — ölçüm gürültüsüne ve anizotropik malzemelere karşı daha sağlam. Tutarsız ölçümleri tespit edebilmeniz için çift başına artıklar raporlanır.

### 4-Sensor

Alan etrafına dört sensör yerleştirin:
- **A–B** = yatay çift (sol/sağ taraflar)
- **C–D** = dikey çift (üst/alt taraflar)

Önce A–B çiftini (yatay), sonra C–D çiftini (dikey) çalıştırın. 2D harita kesişimi gösterir. Her çift ayrı ayrı kalibre edilir — yapı boyunca malzeme değiştiğinde kullanışlıdır.

### 4-Sen+ (Gelişmiş 2D)

Herhangi bir konumda dört sensör (dikdörtgen olarak zorlanmamış). A'yı B, C, D'nin her biriyle eşleştirin ve ayrı ayrı kalibre edin. Aşırı belirlenmiş en küçük kareler çözücü, çift başına ölçüm gürültüsünün ortalamasını alır ve çift başına artıkları raporlar.

### 3D

3D uzayda yerleştirilmiş 4 sensörle tam 3D ölçüm. Her sensörün (X, Y, Z) koordinatlarını ve her çift için (A–B, A–C, A–D) kalibrasyon ve olay sürelerini girin.

### 3D+ (Pro)

3D gibidir ancak aşırı belirlenmiş LSQ ile **6 sensöre kadar** (A'dan F'ye) destekler. Karmaşık 3D geometriler için maksimum hassasiyet.

---

## Materials sekmesi {#the-materials-tab}

20 °C'de bilinen ses hızına sahip yaygın mühendislik malzemeleri kütüphanesi.

![Materials sekmesi](../screenshots/05-materials-tab.png)

### Malzeme listesi

Liste hava, sıvılar, lastikler, polimerler, ahşaplar, camlar ve metaller içerir. Hızlar ~340 m/s'den (hava) ~13.000 m/s'ye (oda sıcaklığında bazı metaller) kadar değişir.

### Sıcaklık kompanzasyonlu yerleşik malzemeler

Yaygın olarak kullanılan 14 metal sıcaklık katsayısı verileri içerir. Ayarlardaki Referans sıcaklığı 20 °C'den farklı olduğunda, uygulama bu malzemelerin hızlarını otomatik olarak ayarlar:

- Alüminyum
- Çelik, Mild (1020)
- Paslanmaz Çelik (304)
- Demir (döküm)
- Demir
- Bakır
- Pirinç
- Bronz
- Titanyum
- Magnezyum
- Kurşun
- Çinko
- Nikel
- Tungsten

Kompanzasyonlu malzemeler seçicide iki değer gösterir: **kompanze edilmiş hız** (büyük, belirgin) ve **20 °C'deki referans hız** (küçük, altında gri).

Kompanzasyonsuz malzemeler italik **"ref only"** gösterir — listelenen hızları sıcaklığa bakılmaksızın olduğu gibi kullanılır.

### Özel malzemeler

2-Sensor sekmesinde bir kalibrasyon ölçerseniz, sonucu özel bir malzeme olarak kaydedebilirsiniz. Başarılı bir 2-sensör ölçümünden sonra, türetilmiş hızı seçtiğiniz bir adla kaydetme seçeneğini arayın.

Özel malzemeler in-situ ölçülen hızı saklar; asla sıcaklık kompanzasyonu uygulamazlar (hız zaten test sıcaklığında ölçüldü).

### Favoriler

Bir favori olarak işaretlemek için herhangi bir malzemenin yanındaki yıldıza dokunun. Favoriler hızlı erişim için listenin üstünde görünür.

### Arama

Malzemeleri ada göre filtrelemek için üstteki arama çubuğunu kullanın. Arama hem İngilizce kanonik adlarla hem de çevrilmiş görünen adlarla eşleşir.

---

## Sıcaklık kompanzasyonu {#temperature-compensation}

Malzemelerdeki ses hızı sıcaklıkla değişir. Otomotiv NVH testinde bu önemlidir: 80 °C'deki bir motor bölmesi, -10 °C'de soğukta beklemiş bir kabin veya 200 °C'deki bir egzoz manifold alanı, oda sıcaklığındaki laboratuvar koşullarından farklı davranır.

### Sıcaklığı ayarlama

Ayarlar (⚙ simge) → Referans sıcaklığı açın. Test ortamınızın sıcaklığını °C cinsinden girin (aralık -40 ila +200).

![Ayarlar paneli](../screenshots/06-settings.png)

### Sıcaklık ≠ 20 °C olduğunda ne olur

- Kalibrasyon süresi alanları sıcaklığa göre ayarlanmış hızla otomatik olarak doldurulur
- Materials seçicisi ayarlanmış hızı belirgin şekilde gösterir
- Bir toast onaylar: *"Alüminyum uygulandı (6.284 m/s @ 60 °C) — N çift güncellendi"*
- "En yakın malzeme" ipucu sıcaklığa göre ayarlanmış hızlarla karşılaştırır
- Kaydedilen geçmiş girişleri etkin sıcaklığı kaydeder
- Raporlar bir altbilgi satırı içerir: *"Referans sıcaklığı: 60 °C, kompanzasyon uygulandı"*

### Uygulama başlatılırken sıfırlama

Uygulamayı başlattığınızda Referans sıcaklığı **her zaman 20 °C'ye sıfırlanır**. Bu, geçmiş bir ölçüm oturumundan kalan eski ayarların bugünkü çalışmayı sessizce etkilemesini önler. Ayarlardaki küçük bir italik not bu davranışı size hatırlatır.

Geçmişteki bir ölçümü orijinal sıcaklığında yeniden oynatmak istiyorsanız, sadece girdiye dokunun — sıcaklık otomatik olarak geri yüklenir.

### Kompanzasyonsuz malzemeler

Çoğu metalik olmayan malzemenin güvenilir yayınlanmış sıcaklık katsayıları yoktur. Uygulama bunlar için **"ref only"** rozeti gösterir — listelenen hızları sıcaklık ayarına bakılmaksızın kullanılır. Bu malzemeler için oda dışı sıcaklıklarda doğru ölçümlere ihtiyacınız varsa, bir in-situ kalibrasyonu gerçekleştirin ve sonucu özel bir malzeme olarak kaydedin.

---

## Fotoğraf açıklaması {#photo-annotation}

Başarılı bir hesaplamadan sonra, kurulumunuzun bir fotoğrafına sensör ve kaynak işaretlerini bindirmek için **📷 Fotoğrafı açıkla** düğmesine dokunun.

![Fotoğraf açıklaması](../screenshots/08-photo-annotation.png)

### Akış

1. **Fotoğrafı açıkla**'ya dokunun — sistem kamerası açılır
2. Sensör yerleşiminin bir fotoğrafını çekin
3. Uygulama fotoğrafı açıklama bindirisine yükler
4. Sensör işaretleri (uygun olarak A, B, C, D, E, F — 6 sensöre kadar) ve kaynak işareti hesaplamanıza göre otomatik olarak yerleştirilir
5. Konumu ince ayarlamak için herhangi bir işareti sürükleyin. Ayarladıkça, kaynak konumu düzeltilmiş sensör konumlarından yeniden hesaplanır
6. Saklamak için **Kaydet**'e veya tekrar denemek için **Yeniden çek**'e dokunun

Açıklanan fotoğraf otomatik olarak PDF raporlarına dahil edilir.

---

## Raporlar {#reports}

Biçimlendirilmiş bir rapor oluşturmak için herhangi bir sonuç ekranındaki **Sonucu yazdır** düğmesine dokunun.

![PDF raporu](../screenshots/09-pdf-report.png)

### Rapor içeriği

- Başlık (Ayarlar → Rapor başlığında özelleştirilebilir)
- Ölçüm başlığı ve zaman damgası
- Tüm giriş değerleri temiz bir tabloda
- Hesaplama sonucu
- Sonuç metni
- Görselleştirme (geometri grafiği)
- Açıklanan fotoğraf (bir tane çektiyseniz)
- Sıcaklık altbilgi satırı (kompanzasyon aktifse)
- Sayfa numarası ve teşekkür satırı

### Çıktı biçimi

- **Android**: yerel PDF oluşturma, telefonunuza kaydedin veya paylaşın
- **iOS**: sistem yazdırma iletişim kutusu → PDF olarak kaydet, AirPrint veya paylaş

### Başlığı özelleştirme

Ayarlar → Rapor başlığı. Şirket adınızı, laboratuvar adınızı, proje bilgilerinizi veya her raporun üstünde istediğiniz herhangi bir şeyi girin.

---

## Yedekleme ve geri yükleme {#backup-and-restore}

Tüm özel malzemelerinizi, favorilerinizi, ayarlarınızı ve geçmişinizi tek bir dosyaya kaydedin. Cihazlar arasında aktarım.

### Yedekleme

Ayarlar → **Yedekleme** → "Yedek dosyasını kaydet"e dokunun. Uygulama bir JSON dosyası oluşturur ve telefonunuzun paylaş sayfasını açar. Bulut sürücünüze (Google Drive, iCloud, OneDrive) kaydedin, kendinize e-postayla gönderin veya istediğiniz şekilde aktarın.

### Geri yükleme

Ayarlar → **Geri yükleme** → telefonunuzun depolamasından yedek dosyasını seçin. Uygulama özel malzemeleri, favorileri, geçmişi ve ayarları içe aktarır.

⚠️ **Geri yükleme mevcut verilerinizi değiştirir.** Mevcut cihazda önemli ölçümleriniz varsa, farklı bir yedekten geri yüklemeden önce bunları yedekleyin.

---

## Ayarlar {#settings}

Sağ üst köşedeki ⚙ dişli simgesi aracılığıyla erişin. Ayarlar bir kalıcıdır, sekme değildir.

![Ayarlar](../screenshots/06-settings.png)

| Ayar | Neyi kontrol ettiği |
|---|---|
| **Pro'ya Yükselt** | Pro özelliklerini satın alın veya hakkında bilgi edinin ($19,99) |
| **Dil** | Uygulamanın görüntüleme dili (30 desteklenir) |
| **Tema** | Açık, Koyu veya Otomatik (sistemi takip et) |
| **Mesafe birimi** | cm veya inç |
| **Referans sıcaklığı** | Kompanzasyon için etkin sıcaklık, -40 ila +200 °C |
| **Rapor başlığı** | Oluşturulan raporların üstünde özel metin |
| **Yedekleme** | Tüm verileri bir dosyaya dışa aktarma |
| **Geri yükleme** | Bir yedek dosyasından verileri içe aktar |
| **Satın almayı geri yükle** | Yeni bir cihazda Pro'yu yeniden edin |

---

## Pro özellikler {#pro-features}

NVH Source Locator bir **özellik kilitli freemium modeli** kullanır:

- **Ücretsiz**: 2-Sensor sekmesi sınırsız olarak tam işlevseldir
- **Pro**: Diğer tüm sekmelerin belirli giriş alanları kilitli. Bir ücretsiz kullanıcı kilitli bir alana dokunduğunda paywall görünür

### Neler kilitli

Pro gerekli alanlar şunlara dağılmıştır:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D ve 3D+ modları
- Yedekleme ve Geri yükleme
- PDF raporları
- Özel malzemeler
- Fotoğraf açıklaması

Bir ücretsiz kullanıcı herhangi bir sekmeyi AÇABİLİR ve arayüzü GÖREBİLİR. Sadece Pro kilitli giriş alanlarına değerler giremez.

![Pro kilitli alan](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Bir ücretsiz kullanıcı kilitli bir alana dokunduğunda, paywall şunları gösterir:
- PRO rozeti olan uygulama simgesi
- Özellik listesi
- Fiyatlı kilit açma düğmesi ($19,99 varsayılan; bölgeye göre değişebilir)
- Promosyon kodu kullanma (yalnızca Android — iOS Apple'ın ayrı Offer Code akışını kullanır)
- Topluluk kanallarına isteğe bağlı promosyon bağlantısı

### Pro satın alma

Herhangi bir kilitli alana dokunun veya Ayarlar'da **Pro'ya Yükselt**'e dokunun. Platformunuzun resmi ödeme sistemini kullanır (Android'de Google Play, iOS'ta Apple App Store).

### Yeni bir cihazda Pro'yu geri yükleme

Bir cihazda satın aldıysanız ve diğerinde Pro istiyorsanız (aynı hesap):

1. Satın almak için kullandığınız **aynı** Google hesabına (Android) veya Apple ID'sine (iOS) giriş yapın
2. NVH Source Locator'ı yeni cihazda açın
3. Ayarlar → **Satın almayı geri yükle**'ye gidin
4. Uygulama platformun satın alma kayıtlarıyla doğrular ve Pro'yu açar

### Başlatmada otomatik geri yükleme

NVH Source Locator arka planda çalışırken Google Play Store veya App Store'da bir promosyon kodunu kullanırsanız, uygulamaya geri dönmek yeni satın almayı otomatik olarak algılar ve Pro'yu açar — manuel Geri yükleme gerekmez.

### Promosyon kodu kullanma

**Android**: paywall'daki "Google Play promosyon kodunuz var mı?" düğmesi, kodunuz önceden doldurulmuş olarak Google Play kullanma akışını açar.

**iOS**: App Store politikası 3.1.1, Apple'ın resmi "Kodu kullan" akışı üzerinden kullanmayı gerektirir. Google Play düğmesi iOS'ta gizlidir. Bunun yerine Ayarlar'da "App Store kodunu kullan"ı arayın.

---

## Help sekmesi ve öğreticiler {#help-tab-and-tutorials}

**Help** sekmesi, uygulama içi öğreticiler, en iyi uygulama kılavuzları ve referans bilgileri içerir.

![Help sekmesi](../screenshots/10-help-tab.png)

Kapsanan konular:
- İhtiyacınız olan ekipman
- En iyi doğruluk için sensörler nasıl yerleştirilir
- Kalibrasyon ipuçları
- Yaygın ölçüm senaryoları
- Triangülasyon ve 3D yerleştirmeler için ipuçları
- Kablo yönlendirme ve sinyal kalitesi

---

## Sorun giderme {#troubleshooting}

### Hesaplama sonucu yanlış veya anlamsız

1. Kalibrasyonunuzu kontrol edin. Otomatik doldurulan `tCal`, yayınlanan malzeme hızını varsayar — gerçek malzemeler değişir. En doğru kalibrasyon in-situ'dur: bilinen bir yere dokunun ve uygulamanın gerçek hızı türetmesine izin verin.
2. **İlk sensör** ayarını kontrol edin — olayı ilk hangi sensörün duyduğu matematik için önemlidir.
3. Mesafe ölçümlerinizi doğrulayın. Birkaç mm'lik hatalar yayılır.

### Toast "Sonuç aralık dışında" diyor

Matematik kaynağın sensörleriniz arasında olmadığını söylüyor. Olası nedenler:
- Kaynak gerçekten sensör hattının/düzleminin dışında
- Girdilerinizden biri yanlış
- Kalibrasyon hızı gerçeklikten çok uzakta

### Hesaplama hızı ipucu bir uyarı rengi gösteriyor

Girdilerinizden ima edilen ses hızı, herhangi bir yaygın malzemeden uzak (50 m/s'den az veya 20.000 m/s'den fazla). Girdilerinizi kontrol edin — muhtemelen tCal veya mesafede bir yazım hatası.

### Materials seçicisi beklenenden farklı hızlar gösteriyor

Ayarlardaki Referans sıcaklığını kontrol edin. 20 °C değilse, gösterilen hızlar sıcaklık kompanzasyonunu yansıtır. Uygulama, kompanze edilmiş hızların altında "ref X @ 20°C" gösterir, böylece doğrulayabilirsiniz.

### Geçmiş girişi farklı sonuçla yeniden oynatılıyor

Uygulama sürüm 1.75'ten önce oluşturulan eski geçmiş girişleri sıcaklığı saklamamış olabilir. Ölçümü 20 °C olmayan bir sıcaklıkta yaptıysanız, yeniden oynatma mevcut ayarı kullanacaktır. Yeniden oynatmadan önce Ayarlarda sıcaklığı manuel olarak ayarlayın VEYA yeniden ölçün.

### Fotoğraf açıklama işaretleri beklediğim yerde değil

İşaretler giriş geometrisine göre otomatik olarak yerleştirilir. Ayarlamak için onları sürükleyin. İşaretleri ayarlamak fotoğraf bindirmesindeki kaynak konumunu günceller — ancak altta yatan hesaplama sonucunu DEĞİŞTİRMEZ.

### Yedekleme/Geri yükleme başarısız

Uygulamanın aynı veya daha yeni bir sürümü tarafından oluşturulan bir yedek dosyası kullandığınızdan emin olun. Eski yedek dosyalarında mevcut veri alanları eksik olabilir.

### Satın almayı geri yükle "satın alma bulunamadı" diyor

1. Satın almak için kullandığınız mağaza hesabıyla aynı hesaba giriş yaptığınızı doğrulayın
2. Satın almanın iade edilmediğini veya süresinin dolmadığını doğrulayın
3. Uygulamayı kaldırıp yeniden yüklemeyi deneyin (satın alma, uygulama kurulumuna değil mağaza hesabınıza bağlıdır)
4. Sorun devam ederse support@evdiag.net ile iletişime geçin

### Sayısal giriş beklenmedik şekilde 0'a geçiyor

Tasarım gereği: bir sayı alanından bulanıklık yaptığınızda (başka bir yere dokunduğunuzda), eğer boş, negatif veya sayısal olmayan metin içeriyorsa, 0'a geçer. Yanlışlıkla temizlenen girdilerden sessizce bozuk hesaplamaları önler. Sıcaklık girişi muaftır (bunun yerine -40/+200'e kıstırılır).

### Daha fazla yardıma ihtiyacım var

`support@evdiag.net` ile şunlarla iletişime geçin:
- Cihaz modeliniz ve OS sürümü
- Uygulama sürümü (Ayarlar → sayfanın alt kısmı)
- Ne denediğinizin açıklaması
- Mümkünse ekran görüntüleri

---

*NVH Source Locator, EVDiag tarafından geliştirilmiştir. Güncellemeler ve kaynaklar için https://evdiag.net adresini ziyaret edin.*
