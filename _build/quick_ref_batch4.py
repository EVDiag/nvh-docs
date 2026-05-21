"""Quick Reference translations — batch 4 (final extension).

6 languages: be, fa, hi, id, ms, tl.
These were previously English fallback locales; now translated.
"""

QUICK_REF_TRANSLATIONS = {

'be': """# NVH Source Locator — Кароткі даведнік

Аднастаронкавае напамінанне. Поўныя падрабязнасці — у **Кіраўніцтва карыстальніка**.

---

## Асноўны працэс (2-Sensor, бясплатна)

1. **Выберыце матэрыял** — укладка Materials → націсніце ваш матэрыял
2. **Увядзіце каліброўку** на ўкладцы 2-Sensor:
   - Адлегласць паміж датчыкамі (`d`)
   - Затрымка часу каліброўкі (`tCal`) — аўтапапаўняецца з матэрыялу
3. **Увядзіце падзею** — `tEvent` і Першы датчык (A або B)
4. **Прачытайце вынік** — адлегласць ад датчыка A

![Укладка 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Усе ўкладкі

| Укладка | Вынік | Поля Pro? |
|---|---|---|
| 2-Sensor | Адлегласць уздоўж лініі | Не (цалкам бясплатна) |
| 3-Sensor | X, Y на паверхні | Так |
| 3-Sen+ | X, Y з LSQ па 3 парах | Так |
| 4-Sensor | X, Y з дзвюх пар (A–B + C–D) | Так |
| 4-Sen+ | X, Y з 4 датчыкаў, любая пазіцыя | Так |
| 3D | X, Y, Z з 4 датчыкаў | Так |
| 3D+ | X, Y, Z да 6 датчыкаў | Так |
| Materials | Выбар хуткасці гуку | Не |
| Help | Навучальныя матэрыялы | Не |

Налады — гэта значок ⚙ (правы верхні кут), а не ўкладка.

---

## Тэмпературная кампенсацыя

Налады → Эталонная тэмпература, дыяпазон **-40 да +200 °C**.

- **14 металаў** маюць убудаваную кампенсацыю (алюміній, сталі, медзь, латунь, бронза, тытан, магній, свінец, цынк, нікель, вальфрам, жалеза, чыгун)
- Матэрыялы без кампенсацыі паказваюць **"ref only"**
- **Скідае на 20 °C пры кожным запуску праграмы** (бяспечны стандарт)
- Прайграванне запісу гісторыі аднаўляе яго першапачатковую тэмпературу

---

## Спалучэнні

- **Націсніце на матэрыял** → аўтаматычна запаўняе ўсе палі `tCal` на ўсіх укладках
- **Утрымлівайце +/-** на лікавых палях → хуткае павелічэнне
- **Перацягвайце гарызантальна** на лікавым полі → змяненне значэння
- **Пустое/адмоўнае/смецце** → пераходзіць у 0 пры страце фокусу (тэмпература абмежавана -40/200)
- **Адзначце матэрыял зорачкай** → перамяшчае ў верх спісу

---

## Мадэль Pro

**Freemium з блакіроўкай функцый** ($19.99):
- Бясплатна: укладка 2-Sensor цалкам функцыянальная, без абмежаванняў
- Pro: іншыя ўкладкі даступныя, але маюць **палі з залатым замком**, якія паказваюць paywall пры націсканні

Pro адкрывае: 3-Sensor да 3D+, карыстальніцкія матэрыялы, рэзервовае капіраванне/аднаўленне, PDF справаздачы, анатацыю фота.

![Paywall](../screenshots/07-paywall.png)

---

## Справаздачы і рэзервовае капіраванне

Кнопка **Друкаваць вынік** на любым экране выніку → PDF з загалоўкам, уваходамі, вынікам, візуалізацыяй, фота (калі зроблена) і ніжнім калонтытулам тэмпературы (калі кампенсацыя актыўная).

Наладзьце загаловак у Налады → Загаловак справаздачы.

**Рэзервовае капіраванне**: Налады → Рэзервовае капіраванне → падзяліцеся ў воблаку/email.  
**Аднаўленне**: Налады → Аднаўленне → выберыце файл рэзервовай копіі.

---

## Аднаўленне Pro на новай прыладзе

Той жа ўліковы запіс Google (Android) або Apple ID (iOS), з якім вы куплялі → Налады → **Аднавіць пакупку** → разблакуе на працягу некалькіх секунд.

Аўтаматычнае аднаўленне адбываецца ціха пры вяртанні ў праграму пасля выкарыстання прома-кода звонку.

---

## Хуткае выпраўленне непаладак

- **Вынік па-за дыяпазонам?** Праверце знак `tEvent` / Першы датчык / адлегласць паміж датчыкамі
- **Найбліжэйшы матэрыял няправільны?** Эталонная тэмпература, верагодна, выпадкова ўстаноўлена — праверце Налады
- **Аднавіць пакупку не атрымоўваецца?** Праверце той жа ўліковы запіс магазіна; пераўсталюйце калі захоўваецца
- **Поле перайшло ў 0?** Пустыя/адмоўныя ўводы аўта-пераходзяць пры страце фокусу — увядзіце значэнне зноў
- **Кнопкі крокаў зніклі?** Яны з'яўляюцца побач з палямі з `data-step` — перазапусціце праграму, калі іх няма
- **Папярэджанне аб састарэлай тэмпературы?** Скідае да 20 пры кожным запуску — устанавіце зноў для гэтай сесіі

---

Звяртайцеся `support@evdiag.net` — пакажыце мадэль прылады, версію праграмы (Налады → нізе) і апісанне таго, што вы спрабавалі.
""",

'fa': """# NVH Source Locator — مرجع سریع

یک یادآوری یک‌صفحه‌ای. برای جزئیات کامل، به **راهنمای کاربر** مراجعه کنید.

---

## جریان اصلی (2-Sensor، رایگان)

1. **یک ماده انتخاب کنید** — برگه Materials → ماده خود را لمس کنید
2. **کالیبراسیون را وارد کنید** در برگه 2-Sensor:
   - فاصله سنسور (`d`)
   - تأخیر زمان کالیبراسیون (`tCal`) — به طور خودکار از ماده پر می‌شود
3. **رویداد را وارد کنید** — `tEvent` و سنسور اول (A یا B)
4. **نتیجه را بخوانید** — فاصله از سنسور A

![برگه 2-Sensor](../screenshots/01-home-2sensor.png)

---

## همه برگه‌ها

| برگه | خروجی | فیلدهای Pro؟ |
|---|---|---|
| 2-Sensor | فاصله در امتداد خط | خیر (کاملاً رایگان) |
| 3-Sensor | X, Y روی یک سطح | بله |
| 3-Sen+ | X, Y با LSQ روی 3 جفت | بله |
| 4-Sensor | X, Y از دو جفت (A–B + C–D) | بله |
| 4-Sen+ | X, Y از 4 سنسور، هر موقعیتی | بله |
| 3D | X, Y, Z از 4 سنسور | بله |
| 3D+ | X, Y, Z از حداکثر 6 سنسور | بله |
| Materials | انتخاب‌گر سرعت صوت | خیر |
| Help | آموزش‌ها | خیر |

تنظیمات نماد ⚙ (بالا-راست) است، نه برگه.

---

## جبران دما

تنظیمات → دمای مرجع، محدوده **-40 تا +200 °C**.

- **14 فلز** دارای جبران داخلی هستند (آلومینیوم، فولادها، مس، برنج، برنز، تیتانیوم، منیزیم، سرب، روی، نیکل، تنگستن، آهن، آهن ریخته)
- مواد بدون جبران **"ref only"** نشان می‌دهند
- **در هر راه‌اندازی برنامه به 20 °C بازنشانی می‌شود** (شروع ایمن پیش‌فرض)
- بازپخش یک ورودی تاریخچه دمای اصلی آن را بازیابی می‌کند

---

## میانبرها

- **روی یک ماده لمس کنید** → همه فیلدهای `tCal` را در همه برگه‌ها به طور خودکار پر می‌کند
- **+/- را نگه دارید** روی فیلدهای عددی → افزایش سریع
- **به طور افقی بکشید** روی یک فیلد عددی → تغییر مقادیر
- **ورودی خالی/منفی/نامعتبر** → هنگام از دست دادن تمرکز به 0 می‌رود (ورودی دما به -40/200 محدود می‌شود)
- **یک ماده را ستاره‌دار کنید** → به بالای انتخاب‌گر منتقل می‌شود

---

## مدل Pro

**Freemium قفل-شده بر اساس ویژگی** ($19.99):
- رایگان: برگه 2-Sensor کاملاً کاربردی، بدون محدودیت
- Pro: سایر برگه‌ها قابل دسترسی هستند اما دارای **فیلدهای قفل طلایی** هستند که هنگام لمس paywall را نشان می‌دهند

Pro باز می‌کند: 3-Sensor تا 3D+، مواد سفارشی، پشتیبان‌گیری/بازیابی، گزارش‌های PDF، حاشیه‌نویسی عکس.

![Paywall](../screenshots/07-paywall.png)

---

## گزارش‌ها و پشتیبان‌گیری

دکمه **چاپ نتیجه** در هر صفحه نتیجه → PDF با سرصفحه، ورودی‌ها، نتیجه، تجسم، عکس (در صورت وجود) و پاورقی دما (وقتی جبران فعال است).

سرصفحه را در تنظیمات → سرصفحه گزارش سفارشی کنید.

**پشتیبان‌گیری**: تنظیمات → پشتیبان‌گیری → اشتراک‌گذاری به ابر/ایمیل.  
**بازیابی**: تنظیمات → بازیابی → انتخاب فایل پشتیبان.

---

## بازیابی Pro در دستگاه جدید

همان حساب گوگل (اندروید) یا اپل آی‌دی (iOS) که با آن خریداری کرده‌اید → تنظیمات → **بازیابی خرید** → ظرف چند ثانیه باز می‌شود.

بازیابی خودکار بی‌صدا اتفاق می‌افتد هنگامی که پس از استفاده از کد تبلیغاتی خارجی به برنامه برمی‌گردید.

---

## عیب‌یابی سریع

- **نتیجه خارج از محدوده؟** علامت `tEvent` / سنسور اول / فاصله سنسور را بررسی کنید
- **نزدیک‌ترین ماده اشتباه است؟** احتمالاً دمای مرجع به طور تصادفی تنظیم شده — تنظیمات را بررسی کنید
- **بازیابی خرید ناموفق است؟** همان حساب فروشگاه را تأیید کنید؛ در صورت تداوم نصب مجدد کنید
- **فیلد به 0 می‌رود؟** ورودی‌های خالی/منفی به طور خودکار با از دست دادن تمرکز می‌روند — مقدار را دوباره وارد کنید
- **دکمه‌های مرحله ناپدید شده؟** آن‌ها در کنار فیلدهای دارای `data-step` ظاهر می‌شوند — اگر گم هستند برنامه را راه‌اندازی مجدد کنید
- **اخطار دمای قدیمی؟** در هر راه‌اندازی به 20 بازنشانی می‌شود — دوباره برای این جلسه تنظیم کنید

---

با `support@evdiag.net` تماس بگیرید — مدل دستگاه، نسخه برنامه (تنظیمات → پایین) و توضیح آنچه را امتحان کرده‌اید را شامل کنید.
""",

'hi': """# NVH Source Locator — त्वरित संदर्भ

एक-पृष्ठ का स्मरण। पूर्ण विवरण के लिए, **उपयोगकर्ता पुस्तिका** देखें।

---

## मुख्य प्रवाह (2-Sensor, मुफ्त)

1. **एक सामग्री चुनें** — Materials टैब → अपनी सामग्री को टैप करें
2. **कैलिब्रेशन दर्ज करें** 2-Sensor टैब पर:
   - सेंसर दूरी (`d`)
   - कैलिब्रेशन समय विलंब (`tCal`) — सामग्री से स्वतः भरा हुआ
3. **घटना दर्ज करें** — `tEvent` और पहला सेंसर (A या B)
4. **परिणाम पढ़ें** — सेंसर A से दूरी

![2-Sensor टैब](../screenshots/01-home-2sensor.png)

---

## सभी टैब

| टैब | आउटपुट | Pro फ़ील्ड? |
|---|---|---|
| 2-Sensor | रेखा के साथ दूरी | नहीं (पूरी तरह से मुफ्त) |
| 3-Sensor | सतह पर X, Y | हाँ |
| 3-Sen+ | 3 जोड़ों पर LSQ के साथ X, Y | हाँ |
| 4-Sensor | दो जोड़ों से X, Y (A–B + C–D) | हाँ |
| 4-Sen+ | 4 सेंसरों से X, Y, कोई भी स्थिति | हाँ |
| 3D | 4 सेंसरों से X, Y, Z | हाँ |
| 3D+ | 6 सेंसरों तक X, Y, Z | हाँ |
| Materials | ध्वनि-की-गति चयनकर्ता | नहीं |
| Help | ट्यूटोरियल | नहीं |

सेटिंग्स ⚙ आइकन (शीर्ष-दाएं) है, टैब नहीं।

---

## तापमान क्षतिपूर्ति

सेटिंग्स → संदर्भ तापमान, सीमा **-40 से +200 °C**।

- **14 धातुओं** में अंतर्निहित क्षतिपूर्ति है (एल्यूमीनियम, स्टील्स, तांबा, पीतल, कांस्य, टाइटेनियम, मैग्नीशियम, सीसा, जस्ता, निकल, टंगस्टन, लोहा, ढलवां लोहा)
- क्षतिपूर्ति के बिना सामग्री **"ref only"** दिखाती है
- **हर ऐप लॉन्च पर 20 °C पर रीसेट होता है** (डिफ़ॉल्ट-सुरक्षित-शुरुआत)
- इतिहास प्रविष्टि को फिर से चलाने से इसका मूल तापमान पुनर्स्थापित हो जाता है

---

## शॉर्टकट

- **एक सामग्री पर टैप करें** → सभी टैब पर सभी `tCal` फ़ील्ड स्वतः भरता है
- **संख्या फ़ील्ड पर +/- दबाए रखें** → तेज़ वृद्धि
- **संख्या फ़ील्ड पर क्षैतिज रूप से खींचें** → मानों को स्क्रब करें
- **खाली/नकारात्मक/अमान्य इनपुट** → फोकस खोने पर 0 हो जाता है (तापमान इनपुट -40/200 तक सीमित)
- **एक सामग्री को स्टार करें** → चयनकर्ता के शीर्ष पर ले जाता है

---

## Pro मॉडल

**फ़ीचर-लॉक्ड freemium** ($19.99):
- मुफ्त: 2-Sensor टैब पूरी तरह से कार्यात्मक, कोई सीमा नहीं
- Pro: अन्य टैब पहुंच योग्य हैं लेकिन **सुनहरे ताला वाले फ़ील्ड** हैं जो टैप करने पर paywall दिखाते हैं

Pro अनलॉक करता है: 3-Sensor से 3D+ तक, कस्टम सामग्री, बैकअप/पुनर्स्थापन, PDF रिपोर्ट, फ़ोटो एनोटेशन।

![Paywall](../screenshots/07-paywall.png)

---

## रिपोर्ट और बैकअप

किसी भी परिणाम स्क्रीन पर **परिणाम प्रिंट करें** बटन → हेडर, इनपुट, परिणाम, विज़ुअलाइज़ेशन, फ़ोटो (यदि ली गई) और तापमान फ़ुटर (जब क्षतिपूर्ति सक्रिय हो) के साथ PDF।

सेटिंग्स → रिपोर्ट हेडर में हेडर को अनुकूलित करें।

**बैकअप**: सेटिंग्स → बैकअप → क्लाउड/ईमेल पर साझा करें।  
**पुनर्स्थापन**: सेटिंग्स → पुनर्स्थापन → बैकअप फ़ाइल चुनें।

---

## नए डिवाइस पर Pro पुनर्स्थापित करें

वही Google खाता (Android) या Apple ID (iOS) जिससे आपने खरीदा था → सेटिंग्स → **खरीदारी पुनर्स्थापित करें** → सेकंडों में अनलॉक हो जाता है।

बाह्य रूप से प्रोमो कोड भुनाने के बाद ऐप पर लौटने पर ऑटो-पुनर्स्थापन चुपचाप होता है।

---

## त्वरित समस्या निवारण

- **परिणाम सीमा से बाहर?** `tEvent` चिह्न / पहला सेंसर / सेंसर दूरी की जाँच करें
- **निकटतम सामग्री गलत?** संदर्भ तापमान शायद गलती से सेट हो गया — सेटिंग्स की जाँच करें
- **खरीदारी पुनर्स्थापित विफल?** उसी स्टोर खाते की पुष्टि करें; यदि बना रहता है तो पुनः इंस्टॉल करें
- **फ़ील्ड 0 पर चला गया?** खाली/नकारात्मक इनपुट फोकस खोने पर ऑटो-स्नैप हो जाते हैं — मान पुनः दर्ज करें
- **स्टेपर बटन गायब?** वे `data-step` वाले फ़ील्ड के बगल में दिखाई देते हैं — गायब होने पर ऐप पुनः आरंभ करें
- **पुराना तापमान चेतावनी?** हर लॉन्च पर 20 पर रीसेट होता है — इस सत्र के लिए फिर से सेट करें

---

`support@evdiag.net` से संपर्क करें — डिवाइस मॉडल, ऐप संस्करण (सेटिंग्स → नीचे) और आपने जो प्रयास किया उसका विवरण शामिल करें।
""",

'id': """# NVH Source Locator — Referensi Cepat

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
""",

'ms': """# NVH Source Locator — Rujukan Pantas

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
""",

'tl': """# NVH Source Locator — Mabilis na Sanggunian

Isang-pahinang paalala. Para sa kumpletong detalye, tingnan ang **Gabay sa Gumagamit**.

---

## Pangunahing daloy (2-Sensor, libre)

1. **Pumili ng materyal** — tab na Materials → i-tap ang inyong materyal
2. **Ilagay ang calibration** sa tab na 2-Sensor:
   - Pagitan ng sensor (`d`)
   - Pagkaantala ng calibration time (`tCal`) — auto-fill mula sa materyal
3. **Ilagay ang event** — `tEvent` at Unang sensor (A o B)
4. **Basahin ang resulta** — distansya mula sa sensor A

![Tab na 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Lahat ng tab

| Tab | Output | Mga Pro field? |
|---|---|---|
| 2-Sensor | Distansya sa kahabaan ng linya | Hindi (ganap na libre) |
| 3-Sensor | X, Y sa isang ibabaw | Oo |
| 3-Sen+ | X, Y na may LSQ sa 3 pares | Oo |
| 4-Sensor | X, Y mula sa dalawang pares (A–B + C–D) | Oo |
| 4-Sen+ | X, Y mula sa 4 na sensor, anumang posisyon | Oo |
| 3D | X, Y, Z mula sa 4 na sensor | Oo |
| 3D+ | X, Y, Z mula sa hanggang 6 na sensor | Oo |
| Materials | Pumipili ng bilis ng tunog | Hindi |
| Help | Mga tutorial | Hindi |

Ang Settings ay icon na ⚙ (kanang itaas), hindi tab.

---

## Pagbabayad sa temperatura

Settings → Reference temperature, saklaw na **-40 hanggang +200 °C**.

- **14 na metal** ay may built-in na compensation (aluminyo, mga acero, tanso, brass, bronze, titanium, magnesium, tingga, sink, nikel, tungsten, bakal, bakal na hinulma)
- Ang mga materyal na walang compensation ay nagpapakita ng **"ref only"**
- **Nare-reset sa 20 °C sa bawat paglulunsad ng app** (default-ligtas-simula)
- Ang pag-replay sa entry sa history ay nagbabalik sa orihinal na temperatura nito

---

## Mga shortcut

- **I-tap ang isang materyal** → auto-fill ang lahat ng `tCal` field sa lahat ng tab
- **Pindutin nang matagal ang +/-** sa mga number field → mabilis na pagdaragdag
- **I-drag nang pahalang** sa isang number field → i-scrub ang mga value
- **Walang laman/negatibo/basurang input** → magiging 0 kapag nawala ang focus (ang temperature input ay limitado sa -40/200)
- **Star-han ang materyal** → mapupunta sa itaas ng picker

---

## Modelong Pro

**Naka-lock-ng-feature na freemium** ($19.99):
- Libre: ang tab na 2-Sensor ay ganap na gumagana, walang limitasyon
- Pro: ang iba pang mga tab ay naa-access ngunit may mga **gintong padlock na field** na nagpapakita ng paywall kapag na-tap

Binubuksan ng Pro: 3-Sensor hanggang 3D+, mga custom na materyal, backup/restore, mga ulat ng PDF, anotasyon ng larawan.

![Paywall](../screenshots/07-paywall.png)

---

## Mga ulat at Backup

Ang **Print result** button sa anumang screen ng resulta → PDF na may header, mga input, resulta, visualization, larawan (kung kinunan), at footer ng temperatura (kapag aktibo ang compensation).

I-customize ang header sa Settings → Report header.

**Backup**: Settings → Backup → ibahagi sa cloud/email.  
**Restore**: Settings → Restore → piliin ang backup file.

---

## Ibalik ang Pro sa bagong device

Parehong Google account (Android) o Apple ID (iOS) na binili mo → Settings → **Restore purchase** → magbubukas sa loob ng ilang segundo.

Ang auto-restore ay nangyayari nang tahimik kapag bumalik ka sa app pagkatapos mag-redeem ng promo code sa labas.

---

## Mabilis na pag-troubleshoot

- **Resulta sa labas ng saklaw?** Suriin ang sign ng `tEvent` / Unang sensor / pagitan ng sensor
- **Mali ang pinakamalapit na materyal?** Marahil ay aksidenteng naitakda ang reference temperature — suriin ang Settings
- **Nabigo ang Restore purchase?** I-verify ang parehong store account; i-reinstall kung nagpapatuloy
- **Naging 0 ang field?** Walang laman/negatibong input ay auto-snap kapag nawala ang focus — ilagay muli ang value
- **Nawawala ang mga stepper button?** Lalabas sila sa tabi ng mga field na may `data-step` — i-restart ang app kung nawawala
- **Babala sa lumang temperatura?** Nare-reset sa 20 sa bawat paglulunsad — itakda muli para sa session na ito

---

Makipag-ugnayan sa `support@evdiag.net` — isama ang modelo ng device, bersyon ng app (Settings → ibaba), at paglalarawan ng kung ano ang sinubukan mo.
""",

}
