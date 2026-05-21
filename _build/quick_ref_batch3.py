"""Quick Reference translations — batch 3 (final).

7 languages: ro, tr, ar, ja, ko, th, vi.
"""

QUICK_REF_TRANSLATIONS = {

'ro': """# NVH Source Locator — Referință rapidă

Un rezumat pe o pagină. Pentru detalii complete, consultați **Ghidul utilizatorului**.

---

## Flux principal (2-Sensor, gratuit)

1. **Alegeți un material** — fila Materials → atingeți materialul dvs.
2. **Introduceți calibrarea** în fila 2-Sensor:
   - Distanța dintre senzori (`d`)
   - Întârzierea timpului de calibrare (`tCal`) — completat automat din material
3. **Introduceți evenimentul** — `tEvent` și Primul senzor (A sau B)
4. **Citiți rezultatul** — distanța de la senzorul A

![Fila 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Toate filele

| Filă | Ieșire | Câmpuri Pro? |
|---|---|---|
| 2-Sensor | Distanța de-a lungul liniei | Nu (complet gratuit) |
| 3-Sensor | X, Y pe o suprafață | Da |
| 3-Sen+ | X, Y cu LSQ peste 3 perechi | Da |
| 4-Sensor | X, Y din două perechi (A–B + C–D) | Da |
| 4-Sen+ | X, Y din 4 senzori, orice poziție | Da |
| 3D | X, Y, Z din 4 senzori | Da |
| 3D+ | X, Y, Z din până la 6 senzori | Da |
| Materials | Selector de viteză a sunetului | Nu |
| Help | Tutoriale | Nu |

Setările se află sub pictograma ⚙ (sus-dreapta), nu ca filă.

---

## Compensarea temperaturii

Setări → Temperatura de referință, interval **-40 până la +200 °C**.

- **14 metale** au compensare integrată (aluminiu, oțeluri, cupru, alamă, bronz, titan, magneziu, plumb, zinc, nichel, wolfram, fier, fontă)
- Materialele fără compensare afișează **„ref only"**
- **Se resetează la 20 °C la fiecare pornire a aplicației** (pornire sigură implicită)
- Redarea unei intrări din istoric îi restaurează temperatura inițială

---

## Comenzi rapide

- **Atingeți un material** → completează automat toate câmpurile `tCal` în toate filele
- **Țineți apăsat +/-** pe câmpurile numerice → incrementare rapidă
- **Trageți orizontal** pe un câmp numeric → defilare prin valori
- **Intrare goală/negativă/nevalidă** → trece la 0 la pierderea focusului (câmpul de temperatură se limitează la -40/200)
- **Marcați un material cu stea** → îl mută în partea de sus a selectorului

---

## Modelul Pro

**Freemium cu blocare pe funcție** ($19,99):
- Gratuit: fila 2-Sensor complet funcțională, fără limite
- Pro: Alte file sunt accesibile, dar au **câmpuri cu lacăt auriu** care afișează paywall la atingere

Pro deblochează: de la 3-Sensor la 3D+, materiale personalizate, backup/restaurare, rapoarte PDF, adnotare foto.

![Paywall](../screenshots/07-paywall.png)

---

## Rapoarte și backup

Butonul **Imprimare rezultat** pe orice ecran de rezultate → PDF cu antet, intrări, rezultat, vizualizare, fotografie (dacă a fost făcută) și subsol cu temperatura (când compensarea este activă).

Personalizați antetul în Setări → Antet raport.

**Backup**: Setări → Backup → partajare în cloud/e-mail.  
**Restaurare**: Setări → Restaurare → selectați fișierul de backup.

---

## Restaurați Pro pe un dispozitiv nou

Același cont Google (Android) sau Apple ID (iOS) cu care ați cumpărat → Setări → **Restaurare achiziție** → se deblochează în câteva secunde.

Restaurarea automată se face în mod silențios când vă întoarceți la aplicație după ce ați răscumpărat un cod promoțional în mod extern.

---

## Depanare rapidă

- **Rezultat în afara intervalului?** Verificați semnul `tEvent` / Primul senzor / distanța senzorilor
- **Cel mai apropiat material greșit?** Temperatura de referință este probabil setată accidental — verificați Setările
- **Restaurarea achiziției eșuează?** Verificați același cont al magazinului; reinstalați dacă persistă
- **Câmp resetat la 0?** Intrările goale/negative se setează automat la pierderea focusului — reintroduceți valoarea
- **Butoanele stepper au dispărut?** Apar lângă câmpurile cu `data-step` — reporniți aplicația dacă lipsesc
- **Avertisment temperatură depășită?** Se resetează la 20 la fiecare pornire — setați din nou pentru această sesiune

---

Contact `support@evdiag.net` — includeți modelul dispozitivului, versiunea aplicației (Setări → jos) și o descriere a ceea ce ați încercat.
""",

'tr': """# NVH Source Locator — Hızlı Başvuru

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
""",

'ar': """# NVH Source Locator — مرجع سريع

ملخص من صفحة واحدة. للحصول على التفاصيل الكاملة، انظر **دليل المستخدم**.

---

## التدفق الأساسي (2-Sensor، مجاني)

1. **اختر مادة** — علامة تبويب Materials → اضغط على المادة
2. **أدخل المعايرة** في علامة تبويب 2-Sensor:
   - تباعد المستشعرات (`d`)
   - تأخير وقت المعايرة (`tCal`) — يتم تعبئته تلقائيًا من المادة
3. **أدخل الحدث** — `tEvent` والمستشعر الأول (A أو B)
4. **اقرأ النتيجة** — المسافة من المستشعر A

![علامة تبويب 2-Sensor](../screenshots/01-home-2sensor.png)

---

## جميع علامات التبويب

| علامة التبويب | الإخراج | حقول Pro؟ |
|---|---|---|
| 2-Sensor | المسافة على طول الخط | لا (مجاني بالكامل) |
| 3-Sensor | X، Y على سطح | نعم |
| 3-Sen+ | X، Y باستخدام LSQ على 3 أزواج | نعم |
| 4-Sensor | X، Y من زوجين (A–B + C–D) | نعم |
| 4-Sen+ | X، Y من 4 مستشعرات، أي موضع | نعم |
| 3D | X، Y، Z من 4 مستشعرات | نعم |
| 3D+ | X، Y، Z من ما يصل إلى 6 مستشعرات | نعم |
| Materials | محدد سرعة الصوت | لا |
| Help | دروس تعليمية | لا |

الإعدادات موجودة تحت أيقونة ⚙ (أعلى اليمين)، وليست علامة تبويب.

---

## تعويض درجة الحرارة

الإعدادات → درجة الحرارة المرجعية، النطاق **-40 إلى +200 °C**.

- **14 معدنًا** تحتوي على تعويض مدمج (الألومنيوم، الفولاذ، النحاس، النحاس الأصفر، البرونز، التيتانيوم، المغنيسيوم، الرصاص، الزنك، النيكل، التنغستن، الحديد، حديد الزهر)
- المواد بدون تعويض تعرض **"ref only"**
- **تُعاد إلى 20 °C عند كل تشغيل للتطبيق** (بداية آمنة افتراضية)
- إعادة تشغيل إدخال في السجل يستعيد درجة حرارته الأصلية

---

## الاختصارات

- **اضغط على مادة** → يملأ تلقائيًا جميع حقول `tCal` في جميع علامات التبويب
- **اضغط مع الاستمرار على +/-** على الحقول الرقمية → زيادة سريعة
- **اسحب أفقيًا** على حقل رقمي → تحريك القيم
- **إدخال فارغ/سالب/غير صالح** → ينتقل إلى 0 عند فقدان التركيز (يقتصر حقل درجة الحرارة على -40/200)
- **ضع علامة نجمة على مادة** → ينقلها إلى أعلى المحدد

---

## نموذج Pro

**Freemium بقفل الميزات** ($19.99):
- مجاني: علامة تبويب 2-Sensor تعمل بالكامل، بدون حدود
- Pro: علامات التبويب الأخرى متاحة ولكن تحتوي على **حقول بقفل ذهبي** تعرض paywall عند الضغط

Pro يفتح: من 3-Sensor إلى 3D+، مواد مخصصة، نسخ احتياطي/استعادة، تقارير PDF، شرح الصور.

![Paywall](../screenshots/07-paywall.png)

---

## التقارير والنسخ الاحتياطي

زر **طباعة النتيجة** في أي شاشة نتائج → PDF مع رأس، مدخلات، نتيجة، تصور، صورة (إذا تم التقاطها) وتذييل درجة الحرارة (عندما يكون التعويض نشطًا).

قم بتخصيص الرأس في الإعدادات → رأس التقرير.

**النسخ الاحتياطي**: الإعدادات → النسخ الاحتياطي → مشاركة إلى السحابة/البريد الإلكتروني.  
**استعادة**: الإعدادات → استعادة → اختر ملف النسخ الاحتياطي.

---

## استعادة Pro على جهاز جديد

نفس حساب Google (Android) أو Apple ID (iOS) الذي اشتريت به → الإعدادات → **استعادة الشراء** → يتم فتحه في ثوانٍ.

تحدث الاستعادة التلقائية بصمت عند العودة إلى التطبيق بعد استرداد رمز ترويجي خارجيًا.

---

## استكشاف الأخطاء وإصلاحها بسرعة

- **النتيجة خارج النطاق؟** تحقق من إشارة `tEvent` / المستشعر الأول / تباعد المستشعرات
- **أقرب مادة خاطئة؟** ربما تم تعيين درجة الحرارة المرجعية عن طريق الخطأ — تحقق من الإعدادات
- **فشل استعادة الشراء؟** تحقق من نفس حساب المتجر؛ أعد التثبيت إذا استمر
- **تم تعيين الحقل على 0؟** المدخلات الفارغة/السالبة تُعيَّن تلقائيًا عند فقدان التركيز — أدخل القيمة مرة أخرى
- **اختفت أزرار الخطوة؟** تظهر بجانب الحقول التي تحتوي على `data-step` — أعد تشغيل التطبيق إذا كانت مفقودة
- **تحذير درجة حرارة قديمة؟** يُعاد إلى 20 عند كل بدء تشغيل — قم بتعيينه مرة أخرى لهذه الجلسة

---

اتصل بـ `support@evdiag.net` — قم بتضمين طراز الجهاز، إصدار التطبيق (الإعدادات → الأسفل) ووصف ما حاولته.
""",

'ja': """# NVH Source Locator — クイックリファレンス

1ページの概要。完全な詳細は **ユーザーガイド** を参照してください。

---

## 基本フロー (2-Sensor、無料)

1. **材料を選択** — Materials タブ → 材料をタップ
2. **キャリブレーションを入力** 2-Sensor タブで:
   - センサー間隔 (`d`)
   - キャリブレーション時間遅延 (`tCal`) — 材料から自動入力
3. **イベントを入力** — `tEvent` と最初のセンサー (A または B)
4. **結果を読む** — センサー A からの距離

![2-Sensor タブ](../screenshots/01-home-2sensor.png)

---

## すべてのタブ

| タブ | 出力 | Pro フィールド? |
|---|---|---|
| 2-Sensor | 直線に沿った距離 | いいえ (完全無料) |
| 3-Sensor | 表面上の X、Y | はい |
| 3-Sen+ | 3 ペアでの LSQ を使用した X、Y | はい |
| 4-Sensor | 2 ペアからの X、Y (A–B + C–D) | はい |
| 4-Sen+ | 4 センサーからの X、Y、任意の位置 | はい |
| 3D | 4 センサーからの X、Y、Z | はい |
| 3D+ | 最大 6 センサーからの X、Y、Z | はい |
| Materials | 音速セレクター | いいえ |
| Help | チュートリアル | いいえ |

設定は ⚙ アイコン (右上) にあり、タブではありません。

---

## 温度補正

設定 → 基準温度、範囲 **-40 から +200 °C**。

- **14 種類の金属** に組み込み補正があります (アルミニウム、各種鋼、銅、真鍮、青銅、チタン、マグネシウム、鉛、亜鉛、ニッケル、タングステン、鉄、鋳鉄)
- 補正のない材料は **"ref only"** と表示されます
- **アプリ起動ごとに 20 °C にリセット** (デフォルトの安全な開始)
- 履歴エントリの再生は元の温度を復元します

---

## ショートカット

- **材料をタップ** → すべてのタブのすべての `tCal` フィールドを自動入力
- **数値フィールドで +/- を長押し** → 高速インクリメント
- **数値フィールドで水平にドラッグ** → 値をスクラブ
- **空/負/無効な入力** → フォーカスを失うと 0 にスナップ (温度フィールドは -40/200 にクランプ)
- **材料に星を付ける** → セレクターの先頭に移動

---

## Pro モデル

**機能ロック型フリーミアム** ($19.99):
- 無料: 2-Sensor タブが完全に機能、制限なし
- Pro: 他のタブはアクセス可能ですが、タップすると paywall を表示する **金色のロック付きフィールド** があります

Pro でロック解除: 3-Sensor から 3D+ まで、カスタム材料、バックアップ/復元、PDF レポート、写真の注釈。

![Paywall](../screenshots/07-paywall.png)

---

## レポートとバックアップ

任意の結果画面の **結果を印刷** ボタン → ヘッダー、入力、結果、視覚化、写真 (撮影した場合)、温度フッター (補正がアクティブな場合) を含む PDF。

ヘッダーを 設定 → レポートヘッダー でカスタマイズします。

**バックアップ**: 設定 → バックアップ → クラウド/メールに共有。  
**復元**: 設定 → 復元 → バックアップファイルを選択。

---

## 新しいデバイスで Pro を復元

購入時に使用したのと同じ Google アカウント (Android) または Apple ID (iOS) → 設定 → **購入を復元** → 数秒以内にロック解除。

外部でプロモーションコードを引き換えた後、アプリに戻ったときに自動復元が静かに実行されます。

---

## クイックトラブルシューティング

- **結果が範囲外?** `tEvent` の符号 / 最初のセンサー / センサー間隔を確認
- **最も近い材料が間違っている?** 基準温度が誤って設定されている可能性があります — 設定を確認
- **購入の復元に失敗?** 同じストアアカウントを確認し、問題が続く場合は再インストール
- **フィールドが 0 にスナップ?** 空/負の入力はフォーカスを失うと自動的にスナップします — 値を再入力
- **ステッパーボタンがない?** `data-step` を持つフィールドの横に表示されます — 不足している場合はアプリを再起動
- **古い温度の警告?** 起動ごとに 20 にリセットされます — このセッション用に再設定

---

`support@evdiag.net` までお問い合わせ — デバイスモデル、アプリのバージョン (設定 → 下部)、試した内容の説明を含めてください。
""",

'ko': """# NVH Source Locator — 빠른 참조

한 페이지 요약. 전체 내용은 **사용자 가이드**를 참조하세요.

---

## 핵심 흐름 (2-Sensor, 무료)

1. **재료 선택** — Materials 탭 → 재료를 탭
2. **보정 입력** 2-Sensor 탭에서:
   - 센서 간격 (`d`)
   - 보정 시간 지연 (`tCal`) — 재료에서 자동 입력됨
3. **이벤트 입력** — `tEvent` 및 첫 번째 센서 (A 또는 B)
4. **결과 읽기** — 센서 A로부터의 거리

![2-Sensor 탭](../screenshots/01-home-2sensor.png)

---

## 모든 탭

| 탭 | 출력 | Pro 필드? |
|---|---|---|
| 2-Sensor | 선을 따른 거리 | 아니요 (완전 무료) |
| 3-Sensor | 표면 위의 X, Y | 예 |
| 3-Sen+ | 3쌍에 대한 LSQ가 있는 X, Y | 예 |
| 4-Sensor | 두 쌍에서의 X, Y (A–B + C–D) | 예 |
| 4-Sen+ | 4개 센서에서의 X, Y, 임의 위치 | 예 |
| 3D | 4개 센서에서의 X, Y, Z | 예 |
| 3D+ | 최대 6개 센서에서의 X, Y, Z | 예 |
| Materials | 음속 선택기 | 아니요 |
| Help | 튜토리얼 | 아니요 |

설정은 ⚙ 아이콘 (오른쪽 위)에 있으며 탭이 아닙니다.

---

## 온도 보정

설정 → 기준 온도, 범위 **-40 ~ +200 °C**.

- **14가지 금속**에 내장 보정이 있습니다 (알루미늄, 강철, 구리, 황동, 청동, 티타늄, 마그네슘, 납, 아연, 니켈, 텅스텐, 철, 주철)
- 보정 없는 재료는 **"ref only"**를 표시합니다
- **앱 시작 시마다 20 °C로 재설정** (기본 안전 시작)
- 기록 항목을 재생하면 원래 온도가 복원됩니다

---

## 단축키

- **재료 탭** → 모든 탭의 모든 `tCal` 필드 자동 입력
- **숫자 필드에서 +/- 길게 누르기** → 빠른 증가
- **숫자 필드에서 가로 드래그** → 값 스크럽
- **빈/음수/유효하지 않은 입력** → 포커스를 잃으면 0으로 스냅 (온도 필드는 -40/200으로 클램프됨)
- **재료에 별표 표시** → 선택기 상단으로 이동

---

## Pro 모델

**기능 잠금 프리미엄** ($19.99):
- 무료: 2-Sensor 탭은 제한 없이 완전히 작동
- Pro: 다른 탭은 액세스 가능하지만 탭하면 paywall을 표시하는 **금색 자물쇠 필드**가 있습니다

Pro 잠금 해제: 3-Sensor부터 3D+까지, 사용자 정의 재료, 백업/복원, PDF 보고서, 사진 주석.

![Paywall](../screenshots/07-paywall.png)

---

## 보고서 및 백업

모든 결과 화면의 **결과 인쇄** 버튼 → 헤더, 입력, 결과, 시각화, 사진 (촬영한 경우), 온도 바닥글 (보정이 활성화된 경우)이 포함된 PDF.

설정 → 보고서 헤더에서 헤더를 사용자 정의합니다.

**백업**: 설정 → 백업 → 클라우드/이메일로 공유.  
**복원**: 설정 → 복원 → 백업 파일 선택.

---

## 새 장치에서 Pro 복원

구매한 동일한 Google 계정 (Android) 또는 Apple ID (iOS) → 설정 → **구매 복원** → 몇 초 안에 잠금 해제.

프로모션 코드를 외부에서 사용한 후 앱으로 돌아갈 때 자동 복원이 자동으로 발생합니다.

---

## 빠른 문제 해결

- **결과가 범위를 벗어남?** `tEvent` 부호 / 첫 번째 센서 / 센서 간격을 확인하세요
- **가장 가까운 재료가 잘못됨?** 기준 온도가 실수로 설정되었을 수 있습니다 — 설정을 확인하세요
- **구매 복원 실패?** 동일한 스토어 계정 확인; 계속되면 재설치
- **필드가 0으로 스냅됨?** 빈/음수 입력은 포커스를 잃을 때 자동으로 스냅됩니다 — 값을 다시 입력
- **스테퍼 버튼이 사라짐?** `data-step`이 있는 필드 옆에 나타납니다 — 누락된 경우 앱 재시작
- **오래된 온도 경고?** 시작할 때마다 20으로 재설정됩니다 — 이 세션을 위해 다시 설정

---

`support@evdiag.net` 문의 — 기기 모델, 앱 버전 (설정 → 하단), 시도한 내용 설명을 포함하세요.
""",

'th': """# NVH Source Locator — คู่มืออ้างอิงด่วน

สรุปหนึ่งหน้า สำหรับรายละเอียดทั้งหมด ดู **คู่มือผู้ใช้**

---

## ขั้นตอนหลัก (2-Sensor, ฟรี)

1. **เลือกวัสดุ** — แท็บ Materials → แตะวัสดุของคุณ
2. **ป้อนการสอบเทียบ** ในแท็บ 2-Sensor:
   - ระยะห่างระหว่างเซ็นเซอร์ (`d`)
   - การหน่วงเวลาสอบเทียบ (`tCal`) — กรอกอัตโนมัติจากวัสดุ
3. **ป้อนเหตุการณ์** — `tEvent` และเซ็นเซอร์แรก (A หรือ B)
4. **อ่านผลลัพธ์** — ระยะห่างจากเซ็นเซอร์ A

![แท็บ 2-Sensor](../screenshots/01-home-2sensor.png)

---

## แท็บทั้งหมด

| แท็บ | ผลลัพธ์ | ฟิลด์ Pro? |
|---|---|---|
| 2-Sensor | ระยะทางตามเส้น | ไม่ (ฟรีทั้งหมด) |
| 3-Sensor | X, Y บนพื้นผิว | ใช่ |
| 3-Sen+ | X, Y พร้อม LSQ จาก 3 คู่ | ใช่ |
| 4-Sensor | X, Y จากสองคู่ (A–B + C–D) | ใช่ |
| 4-Sen+ | X, Y จาก 4 เซ็นเซอร์ ตำแหน่งใดก็ได้ | ใช่ |
| 3D | X, Y, Z จาก 4 เซ็นเซอร์ | ใช่ |
| 3D+ | X, Y, Z จากสูงสุด 6 เซ็นเซอร์ | ใช่ |
| Materials | ตัวเลือกความเร็วเสียง | ไม่ |
| Help | บทช่วยสอน | ไม่ |

การตั้งค่าอยู่ใต้ไอคอน ⚙ (ขวาบน) ไม่ใช่แท็บ

---

## การชดเชยอุณหภูมิ

การตั้งค่า → อุณหภูมิอ้างอิง ช่วง **-40 ถึง +200 °C**

- **โลหะ 14 ชนิด** มีการชดเชยในตัว (อะลูมิเนียม, เหล็ก, ทองแดง, ทองเหลือง, บรอนซ์, ไทเทเนียม, แมกนีเซียม, ตะกั่ว, สังกะสี, นิกเกิล, ทังสเตน, เหล็ก, เหล็กหล่อ)
- วัสดุที่ไม่มีการชดเชยจะแสดง **"ref only"**
- **รีเซ็ตเป็น 20 °C ทุกครั้งที่เปิดแอป** (เริ่มต้นที่ปลอดภัยตามค่าเริ่มต้น)
- การเล่นรายการประวัติจะคืนค่าอุณหภูมิเดิม

---

## ทางลัด

- **แตะวัสดุ** → กรอกฟิลด์ `tCal` ทั้งหมดในทุกแท็บโดยอัตโนมัติ
- **กด +/- ค้างไว้** บนฟิลด์ตัวเลข → การเพิ่มที่รวดเร็ว
- **ลากในแนวนอน** บนฟิลด์ตัวเลข → ปรับค่า
- **อินพุตว่าง/ติดลบ/ไม่ถูกต้อง** → กลับเป็น 0 เมื่อสูญเสียโฟกัส (ฟิลด์อุณหภูมิจำกัดที่ -40/200)
- **ทำเครื่องหมายดาวบนวัสดุ** → ย้ายไปด้านบนของตัวเลือก

---

## โมเดล Pro

**Freemium แบบล็อกฟีเจอร์** ($19.99):
- ฟรี: แท็บ 2-Sensor ทำงานเต็มรูปแบบ ไม่มีข้อจำกัด
- Pro: แท็บอื่นๆ เข้าถึงได้แต่มี **ฟิลด์ที่ล็อกด้วยกุญแจสีทอง** ซึ่งจะแสดง paywall เมื่อแตะ

Pro ปลดล็อก: ตั้งแต่ 3-Sensor ถึง 3D+, วัสดุที่กำหนดเอง, สำรองข้อมูล/กู้คืน, รายงาน PDF, การใส่คำอธิบายภาพ

![Paywall](../screenshots/07-paywall.png)

---

## รายงานและสำรองข้อมูล

ปุ่ม **พิมพ์ผลลัพธ์** บนหน้าจอผลลัพธ์ใดๆ → PDF พร้อมส่วนหัว ข้อมูลที่ป้อน ผลลัพธ์ การแสดงภาพ รูปภาพ (หากถ่าย) และส่วนท้ายอุณหภูมิ (เมื่อการชดเชยทำงานอยู่)

ปรับแต่งส่วนหัวใน การตั้งค่า → ส่วนหัวรายงาน

**สำรองข้อมูล**: การตั้งค่า → สำรองข้อมูล → แชร์ไปยังคลาวด์/อีเมล  
**กู้คืน**: การตั้งค่า → กู้คืน → เลือกไฟล์สำรองข้อมูล

---

## กู้คืน Pro บนอุปกรณ์ใหม่

บัญชี Google (Android) หรือ Apple ID (iOS) เดียวกับที่คุณซื้อ → การตั้งค่า → **กู้คืนการซื้อ** → ปลดล็อกในไม่กี่วินาที

การกู้คืนอัตโนมัติจะเกิดขึ้นเงียบๆ เมื่อคุณกลับไปที่แอปหลังจากแลกรหัสโปรโมชั่นภายนอก

---

## การแก้ไขปัญหาด่วน

- **ผลลัพธ์อยู่นอกช่วง?** ตรวจสอบเครื่องหมาย `tEvent` / เซ็นเซอร์แรก / ระยะห่างระหว่างเซ็นเซอร์
- **วัสดุที่ใกล้ที่สุดผิด?** อาจตั้งค่าอุณหภูมิอ้างอิงโดยไม่ตั้งใจ — ตรวจสอบการตั้งค่า
- **การกู้คืนการซื้อล้มเหลว?** ตรวจสอบบัญชีร้านค้าเดียวกัน; ติดตั้งใหม่หากยังคงมีปัญหา
- **ฟิลด์ถูกตั้งเป็น 0?** อินพุตว่าง/ติดลบจะถูกตั้งโดยอัตโนมัติเมื่อสูญเสียโฟกัส — ป้อนค่าใหม่
- **ปุ่มสเต็ปเปอร์หายไป?** จะปรากฏข้างฟิลด์ที่มี `data-step` — รีสตาร์ทแอปหากขาดหายไป
- **คำเตือนอุณหภูมิล้าสมัย?** รีเซ็ตเป็น 20 ทุกครั้งที่เริ่ม — ตั้งค่าอีกครั้งสำหรับเซสชันนี้

---

ติดต่อ `support@evdiag.net` — รวมรุ่นอุปกรณ์ เวอร์ชันแอป (การตั้งค่า → ด้านล่าง) และคำอธิบายสิ่งที่คุณลอง
""",

'vi': """# NVH Source Locator — Tham khảo nhanh

Bản tóm tắt một trang. Để biết chi tiết đầy đủ, xem **Hướng dẫn sử dụng**.

---

## Quy trình chính (2-Sensor, miễn phí)

1. **Chọn vật liệu** — tab Materials → chạm vào vật liệu của bạn
2. **Nhập hiệu chuẩn** ở tab 2-Sensor:
   - Khoảng cách giữa các cảm biến (`d`)
   - Độ trễ thời gian hiệu chuẩn (`tCal`) — tự động điền từ vật liệu
3. **Nhập sự kiện** — `tEvent` và Cảm biến đầu tiên (A hoặc B)
4. **Đọc kết quả** — khoảng cách từ cảm biến A

![Tab 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tất cả các tab

| Tab | Đầu ra | Trường Pro? |
|---|---|---|
| 2-Sensor | Khoảng cách dọc theo đường | Không (hoàn toàn miễn phí) |
| 3-Sensor | X, Y trên bề mặt | Có |
| 3-Sen+ | X, Y với LSQ qua 3 cặp | Có |
| 4-Sensor | X, Y từ hai cặp (A–B + C–D) | Có |
| 4-Sen+ | X, Y từ 4 cảm biến, vị trí bất kỳ | Có |
| 3D | X, Y, Z từ 4 cảm biến | Có |
| 3D+ | X, Y, Z từ tối đa 6 cảm biến | Có |
| Materials | Bộ chọn tốc độ âm thanh | Không |
| Help | Hướng dẫn | Không |

Cài đặt nằm dưới biểu tượng ⚙ (trên cùng bên phải), không phải là tab.

---

## Bù nhiệt độ

Cài đặt → Nhiệt độ tham chiếu, phạm vi **-40 đến +200 °C**.

- **14 kim loại** có bù tích hợp sẵn (nhôm, các loại thép, đồng, đồng thau, đồng đỏ, titan, magie, chì, kẽm, niken, vonfram, sắt, gang)
- Vật liệu không có bù hiển thị **"ref only"**
- **Đặt lại về 20 °C mỗi khi khởi động ứng dụng** (khởi động an toàn mặc định)
- Phát lại mục lịch sử sẽ khôi phục nhiệt độ ban đầu của nó

---

## Phím tắt

- **Chạm vào vật liệu** → tự động điền vào tất cả các trường `tCal` ở tất cả các tab
- **Giữ +/-** trên các trường số → tăng nhanh
- **Kéo ngang** trên trường số → cuộn qua các giá trị
- **Đầu vào trống/âm/không hợp lệ** → quay về 0 khi mất tiêu điểm (trường nhiệt độ giới hạn ở -40/200)
- **Đánh dấu sao vật liệu** → di chuyển lên đầu bộ chọn

---

## Mô hình Pro

**Freemium khóa tính năng** ($19,99):
- Miễn phí: tab 2-Sensor hoạt động đầy đủ, không giới hạn
- Pro: Các tab khác có thể truy cập nhưng có **các trường có ổ khóa vàng** hiển thị paywall khi chạm

Pro mở khóa: từ 3-Sensor đến 3D+, vật liệu tùy chỉnh, sao lưu/khôi phục, báo cáo PDF, chú thích ảnh.

![Paywall](../screenshots/07-paywall.png)

---

## Báo cáo và sao lưu

Nút **In kết quả** trên bất kỳ màn hình kết quả nào → PDF với tiêu đề, đầu vào, kết quả, hình ảnh, ảnh (nếu đã chụp) và chân trang nhiệt độ (khi bù được kích hoạt).

Tùy chỉnh tiêu đề trong Cài đặt → Tiêu đề báo cáo.

**Sao lưu**: Cài đặt → Sao lưu → chia sẻ vào đám mây/email.  
**Khôi phục**: Cài đặt → Khôi phục → chọn tệp sao lưu.

---

## Khôi phục Pro trên thiết bị mới

Cùng tài khoản Google (Android) hoặc Apple ID (iOS) mà bạn đã mua → Cài đặt → **Khôi phục mua hàng** → mở khóa trong vài giây.

Khôi phục tự động diễn ra âm thầm khi bạn quay lại ứng dụng sau khi đổi mã khuyến mãi bên ngoài.

---

## Khắc phục sự cố nhanh

- **Kết quả ngoài phạm vi?** Kiểm tra dấu `tEvent` / Cảm biến đầu tiên / khoảng cách cảm biến
- **Vật liệu gần nhất sai?** Có thể nhiệt độ tham chiếu đã được đặt vô tình — kiểm tra Cài đặt
- **Khôi phục mua hàng thất bại?** Xác minh cùng tài khoản cửa hàng; cài đặt lại nếu vẫn tiếp tục
- **Trường được đặt thành 0?** Đầu vào trống/âm tự động được đặt khi mất tiêu điểm — nhập lại giá trị
- **Nút stepper biến mất?** Chúng xuất hiện bên cạnh các trường có `data-step` — khởi động lại ứng dụng nếu thiếu
- **Cảnh báo nhiệt độ lỗi thời?** Đặt lại về 20 mỗi khi khởi động — đặt lại cho phiên này

---

Liên hệ `support@evdiag.net` — kèm theo kiểu máy thiết bị, phiên bản ứng dụng (Cài đặt → dưới cùng) và mô tả về những gì bạn đã thử.
""",

}
