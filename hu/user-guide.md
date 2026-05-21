# NVH Source Locator — Felhasználói kézikönyv

NVH Source Locator egy mérőeszköz zaj- és rezgésforrások lokalizálására TDOA (Time Difference of Arrival) használatával, az oszcilloszkópon vagy mérőrendszeren rögzített gyorsulásmérő jelekből.

Ez az útmutató lefedi az összes funkciót. Gyors emlékeztetőhöz lásd **Gyors útmutató**.

---

## Tartalomjegyzék

1. [Hogyan működik](#how-it-works)
2. [Mielőtt elkezdené](#before-you-start)
3. [A főbb lapok](#the-main-tabs)
4. [2-Sensor mód](#2-sensor-mode)
5. [3-Sensor mód](#3-sensor-mode)
6. [Pro+ módok (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [A Materials lap](#the-materials-tab)
8. [Hőmérséklet-kompenzáció](#temperature-compensation)
9. [Fotóannotáció](#photo-annotation)
10. [Jelentések](#reports)
11. [Biztonsági mentés és visszaállítás](#backup-and-restore)
12. [Beállítások](#settings)
13. [Pro funkciók](#pro-features)
14. [Help lap és oktatóanyagok](#help-tab-and-tutorials)
15. [Hibaelhárítás](#troubleshooting)

---

## Hogyan működik

Amikor egy zajforrás hangot vagy rezgést bocsát ki, a hullám ismert sebességgel terjed az anyagban. Ha két vagy több gyorsulásmérőt helyez az anyagra, és megméri, mikor érkezik a hullám mindegyikhez, az időkülönbség megmondja, hol van a forrás.

NVH Source Locator átveszi:

- **Kalibrációt**: az érzékelők közötti távolságot, és azt az időt, amennyi alatt egy hullám megteszi ezt a távolságot (az anyag hangsebességének kiszámításához használatos)
- **Eseményt**: az időkülönbséget azon érzékelők között, amelyek észlelik a zaj-/rezgéseseményt

Ezután kiszámítja, hol található a forrás a szerkezetben.

Minél több érzékelőt használ, annál pontosabban tudja meghatározni a forrást:

- **2 érzékelő** → távolság egy vonal mentén
- **3 érzékelő** → pozíció egy 2D felületen (X, Y)
- **4 érzékelő** → pozíció 3D térben (X, Y, Z)

---

## Mielőtt elkezdené

Szükséges lesz:

- **Egy oszcilloszkóp vagy mérőrendszer**, amely meg tudja mutatni az időkülönbséget gyorsulásmérő csatornák között mikroszekundumban (µs)
- **Legalább 2 gyorsulásmérő** fizikailag a szerkezethez rögzítve (több érzékelő = nagyobb pontosság)
- **Egy mód a távolság mérésére** az érzékelők között (mérőszalag, tolómérő)
- **Egy mód egy hullám kiváltására** egy ismert helyen kalibráláshoz (kalibrált kalapácsütés, csavarhúzó-ütés vagy más ismert jel)

![Kezdőképernyő 2-Sensor lappal](../screenshots/01-home-2sensor.png)

---

## A főbb lapok

Az alkalmazás lapjai a tetején vannak:

![Lapsáv](../screenshots/02-tab-bar.png)

| Lap | Mit csinál | Mikor használja |
|---|---|---|
| **2-Sensor** | 1D forráslokalizálás egy vonal mentén 2 érzékelő között | Gyors ellenőrzések, gerendaszerű szerkezetek. **Teljesen ingyenes.** |
| **3-Sensor** | 2D forráslokalizálás 3 érzékelővel egy háromszögben | Legáltalánosabb használat, panelek és felületek |
| **3-Sen+** | 3-Sensor túldetermináltt legkisebb négyzetes megoldóval | Igényesebb mérések, zajálló |
| **4-Sensor** | 2D lokalizálás két párral (A-B + C-D) | Téglalap alakú érzékelőelrendezések, keresztellenőrzés |
| **4-Sen+** | Speciális 2D mód, 4 érzékelő bármilyen helyzetben | Nem-téglalap geometriák, teljes LSQ |
| **3D** | 3D forráslokalizálás 4 érzékelővel XYZ koordinátákkal | Komplex szerkezetek 3D térben |
| **3D+** | 3D akár 6 érzékelőig, túldeterminált LSQ | Nagyon komplex geometriák, maximális pontosság |
| **Materials** | Hangsebesség-könyvtár + egyéni anyagok | Egyszer választja ki mérési munkamenetenként |
| **Help** | Alkalmazáson belüli oktatóanyagok és referencia | Amikor gyors emlékeztetőre van szüksége |

> **Ingyenes vs Pro**: A 2-Sensor lap teljesen ingyenes. Más lapok elérhetők, de bizonyos beviteli mezők zárolva vannak Pro felhasználók számára (arany lakat jelvénnyel jelölve). Egy zárolt mező megérintése megjeleníti a Pro paywallt.

A beállítások a ⚙ fogaskerék ikonon keresztül érhetők el a jobb felső sarokban (nem egy lap).

---

## 2-Sensor mód

A legegyszerűbb mérés: forráslokalizálás egy vonal mentén két gyorsulásmérő között.

![2-Sensor lap](../screenshots/01-home-2sensor.png)

### 1. lépés: Anyag alkalmazása

Koppintson a Materials lapra. Válassza ki az anyagot, amelyből a szerkezete készült (pl. „Alumínium", „Acél, Mild (1020)"). Az alkalmazás az anyag ismert hangsebességét használja a kalibrációs idő mező automatikus kitöltéséhez.

Ha a szerkezete anyaga nincs a listán, ideiglenesen választhatja a „Levegő"-t és a 2. lépésben kézzel felülírhatja a kalibrációs időt.

### 2. lépés: Kalibrációs adatok bevitele

A 2-Sensor lapon két párszekciót lát: **Pár A–B** és **Pár A–C** (csak A–B szükséges, ha csak 2 érzékelője van).

Minden párhoz kitölti:

- **Érzékelőtávolság** (`d`): fizikai távolság az érzékelők között, cm-ben vagy hüvelykben (a Beállításokban beállítva)
- **Kalibrációs idő késleltetés** (`tCal`): az az idő, amennyi alatt egy hullám átszáguld az érzékelők között az anyag hangsebességén — automatikusan kitöltődik anyag kiválasztásakor, de felülírhatja

### 3. lépés: Esemény idejének bevitele

- **Esemény idő késleltetés** (`tEvent`): időkülönbség azon érzékelők között, amelyek észlelik a zajeseményt, mikroszekundumban
- **Első érzékelő**: melyik érzékelő hallotta először az eseményt (A vagy B)

### 4. lépés: Eredmény leolvasása

Az alkalmazás a forrás pozícióját az A érzékelőtől mért távolságként mutatja:
- Eredmény = 0: forrás az A érzékelőnél van
- Eredmény = távolság: forrás a B érzékelőnél van
- Eredmény közöttük: forrás közöttük van
- Eredmény kívül: a forrás az egyik érzékelőn túl van (a toast figyelmeztet)

Az eredménykártya mindkét távolságot mutatja (A-tól, B-től) és jelzi, melyik érzékelő van közelebb.

### 5. lépés (opcionális): Fotó annotálása

Koppintson a **📷 Fotó annotálása** gombra, hogy fényképet készítsen az elrendezéséről. Az alkalmazás A, B érzékelő és a forrás jelölőket helyez rá. Hasznos jelentésekhez.

---

## 3-Sensor mód

Egy forrást lokalizál egy 2D síkon három, háromszögbe elrendezett érzékelővel.

![3-Sensor lap](../screenshots/03-3sensor-tab.png)

### Beállítás

Helyezzen három érzékelőt a szerkezetére háromszöget alkotva. Egyenlő oldalú, derékszögű vagy szabálytalan — az alkalmazás minden geometriát kezel.

### Adatok bevitele

A **Háromszögoldalak hosszai** szakaszban adja meg a fizikai távolságot mind a három oldalra (A–B, A–C, B–C).

Minden párhoz (A–B és A–C) adja meg:
- **tCal**: kalibrációs idő (automatikusan kitöltve az anyagból)
- **tEvent**: mért időkülönbség a zajeseményhez
- **Első érzékelő**: melyik hallotta először

### Eredmény leolvasása

Az alkalmazás a forrás pozícióját X, Y koordinátákként mutatja az A érzékelőhöz viszonyítva (A érzékelő az origóban, B érzékelő az X tengelyen). A vizualizáció mutatja mindhárom érzékelőt és a forrás helyét.

![Háromszög eredmény](../screenshots/04-triangle-result.png)

---

## Pro+ módok

Több haladó lap kínál túldeterminált megoldókat és magasabb dimenzionalitást:

### 3-Sen+ (Pro)

Ugyanaz a háromszög-beállítás, mint a 3-Sensor, de kalibrálja ÉS mérje meg mind a három párat (A–B, A–C, B–C). A megoldó mindhárom TDOA-t használja egy legkisebb négyzetes illeszkedésben — robusztusabb mérési zajra és anizotrop anyagokra. Páronkénti maradékok jelennek meg, így észreveheti a következetlen méréseket.

### 4-Sensor

Helyezzen négy érzékelőt a terület köré:
- **A–B** = vízszintes pár (bal/jobb oldalak)
- **C–D** = függőleges pár (felső/alsó oldalak)

Először az A–B párt (vízszintes), majd a C–D párt (függőleges) futtassa. A 2D térkép mutatja a metszéspontot. Minden pár külön kalibrálva van — hasznos, amikor az anyag változik a szerkezeten keresztül.

### 4-Sen+ (Speciális 2D)

Négy érzékelő bármilyen helyzetben (nem kényszerítve téglalapra). Párosítsa A-t B, C, D mindegyikével és kalibráljon külön. A túldeterminált legkisebb négyzetes megoldó átlagolja a páronkénti mérési zajt és jelenti a páronkénti maradékokat.

### 3D

Teljes 3D mérés 4 érzékelővel 3D térben elhelyezve. Adja meg minden érzékelő (X, Y, Z) koordinátáit, valamint a kalibrációs és eseményidőket minden párhoz (A–B, A–C, A–D).

### 3D+ (Pro)

Mint a 3D, de akár **6 érzékelőig** támogat (A-tól F-ig) túldeterminált LSQ-val. Maximális pontosság komplex 3D geometriákhoz.

---

## A Materials lap

Gyakori mérnöki anyagok könyvtára 20 °C-on ismert hangsebességgel.

![Materials lap](../screenshots/05-materials-tab.png)

### Anyaglista

A lista tartalmaz levegőt, folyadékokat, gumikat, polimereket, fát, üveget és fémeket. A sebességek ~340 m/s (levegő) és ~13 000 m/s (egyes fémek szobahőmérsékleten) között mozognak.

### Beépített anyagok hőmérséklet-kompenzációval

14 gyakran használt fém tartalmaz hőmérsékleti együttható adatokat. Amikor a Referencia hőmérséklet a Beállításokban eltér 20 °C-tól, az alkalmazás automatikusan beállítja ezen anyagok sebességét:

- Alumínium
- Acél, Mild (1020)
- Rozsdamentes Acél (304)
- Vas (öntött)
- Vas
- Réz
- Sárgaréz
- Bronz
- Titán
- Magnézium
- Ólom
- Cink
- Nikkel
- Volfrám

A kompenzálással rendelkező anyagok két értéket mutatnak a választóban: a **kompenzált sebességet** (nagy, prominens) és a **20 °C-on lévő referencia sebességet** (kis, szürke alatta).

A kompenzáció nélküli anyagok **„ref only"** kurzívval jelennek meg — a felsorolt sebességüket úgy használjuk, ahogy van, függetlenül a hőmérséklettől.

### Egyéni anyagok

Ha kalibrációt mér a 2-Sensor lapon, mentheti az eredményt egyéni anyagként. Sikeres 2-sensor mérés után keresse a lehetőséget, hogy a levezetett sebességet egy Ön által választott név alatt mentse.

Az egyéni anyagok tárolják az in-situ mért sebességet; soha nem alkalmaznak hőmérséklet-kompenzációt (a sebességet már a teszt hőmérsékletén mérték).

### Kedvencek

Koppintson a csillagra bármely anyag mellett, hogy kedvencként megjelölje. A kedvencek a lista tetején jelennek meg gyors hozzáférés érdekében.

### Keresés

Használja a tetején lévő keresősávot az anyagok név szerinti szűréséhez. A keresés megfelel mind az angol kanonikus neveknek, mind a fordított megjelenítési neveknek.

---

## Hőmérséklet-kompenzáció

Az anyagokban a hangsebesség változik a hőmérséklettel. Az autóipari NVH tesztelésben ez számít: egy 80 °C-os motorháztető, egy -10 °C-os hidegen áztatott kabin vagy egy 200 °C-os kipufogóelosztó terület mind másképp viselkedik, mint a szobahőmérsékleti laboratóriumi körülmények.

### Hőmérséklet beállítása

Nyissa meg a Beállítások (⚙ ikon) → Referencia hőmérséklet menüpontot. Adja meg a teszt környezete hőmérsékletét °C-ban (tartomány -40-től +200-ig).

![Beállítások panel](../screenshots/06-settings.png)

### Mi történik, ha a hőmérséklet ≠ 20 °C

- A kalibrációs idő mezők automatikusan kitöltődnek a hőmérséklet-korrigált sebességgel
- A Materials választó kiemelten mutatja a beállított sebességet
- Egy toast megerősíti: *„Alumínium alkalmazva (6 284 m/s @ 60 °C) — N pár(ok) frissítve"*
- A „Legközelebbi anyag" javaslat a hőmérséklet-korrigált sebességekkel hasonlítja össze
- A mentett előzményekbe bejegyzések rögzítik az aktív hőmérsékletet
- A jelentések tartalmaznak egy lábsort: *„Referencia hőmérséklet: 60 °C, kompenzáció alkalmazva"*

### Visszaállítás alkalmazás indításkor

A Referencia hőmérséklet **mindig 20 °C-ra áll vissza**, amikor elindítja az alkalmazást. Ez megakadályozza, hogy egy múltbeli mérési munkamenet elavult beállításai csendben befolyásolják a mai munkát. A Beállításokban egy kis kurzív jegyzet emlékezteti erre a viselkedésre.

Ha egy múltbeli mérést szeretne lejátszani az eredeti hőmérsékletén, csak koppintson a bejegyzésre — a hőmérséklet automatikusan visszaáll.

### Anyagok kompenzáció nélkül

A legtöbb nem-fém anyag nem rendelkezik megbízható publikált hőmérsékleti együtthatókkal. Az alkalmazás ezekhez **„ref only"** jelvényt mutat — a felsorolt sebességet a hőmérsékleti beállítástól függetlenül használja. Ha pontos méréseket kell elvégeznie nem szobahőmérsékleten ezekhez az anyagokhoz, végezzen in-situ kalibrációt és mentse az eredményt egyéni anyagként.

---

## Fotóannotáció

Sikeres számítás után koppintson a **📷 Fotó annotálása** gombra, hogy érzékelő- és forrásjelölőket helyezzen az elrendezésének fényképére.

![Fotóannotáció](../screenshots/08-photo-annotation.png)

### Folyamat

1. Koppintson a **Fotó annotálása** gombra — megnyílik a rendszerkamera
2. Készítsen fényképet az érzékelők elhelyezéséről
3. Az alkalmazás betölti a fényképet az annotációs rétegbe
4. Az érzékelőjelölők (A, B, C, D, E, F szükség szerint — akár 6 érzékelőig) és a forrásjelölő automatikusan elhelyeződik a számításának alapján
5. Húzza bármelyik jelölőt a pozíció finomításához. Ahogy igazít, a forrás pozíciója újraszámolódik a korrigált érzékelőpozíciókból
6. Koppintson a **Mentés** gombra a megtartáshoz, vagy az **Újrafelvétel** gombra az újrapróbáláshoz

Az annotált fénykép automatikusan beépül a PDF jelentésekbe.

---

## Jelentések

Koppintson a **Eredmény nyomtatása** gombra bármelyik eredményképernyőn formázott jelentés generálásához.

![PDF jelentés](../screenshots/09-pdf-report.png)

### Jelentés tartalma

- Fejléc (testreszabható a Beállítások → Jelentés fejléce menüben)
- Mérés címe és időbélyege
- Az összes bemeneti érték egy tiszta táblázatban
- Számítási eredmény
- Következtetés szöveg
- Vizualizáció (geometriai grafikon)
- Annotált fénykép (ha készített egyet)
- Hőmérséklet lábsor (ha a kompenzáció aktív volt)
- Oldalszám és köszönetnyilvánítási sor

### Kimeneti formátum

- **Android**: natív PDF-generálás, mentse a telefonjára vagy ossza meg
- **iOS**: rendszer nyomtatási párbeszéd → mentse PDF-ként, AirPrint vagy ossza meg

### Fejléc testreszabása

Beállítások → Jelentés fejléce. Adja meg cégének nevét, laborja nevét, projekt-információkat vagy bármi mást, amit minden jelentés tetejére szeretne.

---

## Biztonsági mentés és visszaállítás

Mentse el az összes egyéni anyagát, kedvenceit, beállításait és előzményeit egyetlen fájlba. Eszközök közötti átvitel.

### Biztonsági mentés

Beállítások → **Biztonsági mentés** → koppintson a „Mentési fájl mentése" gombra. Az alkalmazás generál egy JSON fájlt és megnyitja a telefonja megosztási panelét. Mentse a felhőmeghajtójára (Google Drive, iCloud, OneDrive), küldje el magának e-mailben vagy adja át bármilyen módon.

### Visszaállítás

Beállítások → **Visszaállítás** → válassza ki a mentési fájlt a telefonja tárolójából. Az alkalmazás importálja az egyéni anyagokat, kedvenceket, előzményeket és beállításokat.

⚠️ **A visszaállítás felülírja a jelenlegi adatait.** Ha fontos mérései vannak a jelenlegi eszközön, először mentse el azokat, mielőtt visszaállítaná egy másik biztonsági mentésből.

---

## Beállítások

Hozzáférés a ⚙ fogaskerék ikonon keresztül a jobb felső sarokban. A Beállítások egy modális, nem egy lap.

![Beállítások](../screenshots/06-settings.png)

| Beállítás | Mit szabályoz |
|---|---|
| **Frissítés Pro-ra** | Vásároljon vagy tudjon meg többet a Pro funkciókról ($19,99) |
| **Nyelv** | Az alkalmazás megjelenítési nyelve (30 támogatott) |
| **Téma** | Világos, Sötét vagy Auto (rendszer követése) |
| **Távolság egysége** | cm vagy hüvelyk |
| **Referencia hőmérséklet** | Aktív hőmérséklet a kompenzációhoz, -40 - +200 °C |
| **Jelentés fejléce** | Egyéni szöveg a generált jelentések tetején |
| **Biztonsági mentés** | Az összes adat exportálása fájlba |
| **Visszaállítás** | Adatok importálása mentési fájlból |
| **Vásárlás visszaállítása** | Pro újraszerzése új eszközön |

---

## Pro funkciók

NVH Source Locator egy **funkció-zárolt freemium modellt** használ:

- **Ingyenes**: A 2-Sensor lap teljesen funkcionális korlátozások nélkül
- **Pro**: Minden más lapnak bizonyos beviteli mezői zárolva vannak. A paywall akkor jelenik meg, amikor egy ingyenes felhasználó megérint egy zárolt mezőt

### Mi van zárolva

A Pro-kötelező mezők szétszórva vannak:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D és 3D+ módok
- Biztonsági mentés és Visszaállítás
- PDF jelentések
- Egyéni anyagok
- Fotóannotáció

Egy ingyenes felhasználó MEGNYITHATJA bármelyik lapot és LÁTHATJA a felületet. Csak nem tud értékeket beírni a Pro-zárolt beviteli mezőkbe.

![Pro-zárolt mező](../screenshots/11-pro-locked-field.png)

### A paywall

![Paywall](../screenshots/07-paywall.png)

Amikor egy ingyenes felhasználó megérint egy zárolt mezőt, a paywall becsúszik, mutatva:
- Alkalmazás ikon PRO jelvénnyel
- Funkciólista
- Feloldás gomb árral ($19,99 alapértelmezett; régiónként változhat)
- Promóciós kód beváltás (csak Android — iOS az Apple külön Offer Code folyamatát használja)
- Opcionális promóciós link közösségi csatornákra

### Pro vásárlása

Koppintson bármely zárolt mezőre, vagy koppintson a **Frissítés Pro-ra** gombra a Beállításokban. A platform hivatalos fizetési rendszerét használja (Google Play Androidon, Apple App Store iOS-en).

### Pro visszaállítása új eszközön

Ha egy eszközön vásárolt és Pro-t szeretne egy másikon (ugyanaz a fiók):

1. Jelentkezzen be **ugyanazzal** a Google fiókkal (Android) vagy Apple ID-val (iOS), amit a vásárláskor használt
2. Nyissa meg az NVH Source Locator-t az új eszközön
3. Menjen a Beállítások → **Vásárlás visszaállítása** menüpontba
4. Az alkalmazás ellenőrzi a platform vásárlási rekordjait és feloldja a Pro-t

### Automatikus visszaállítás indításkor

Ha promóciós kódot vált be a Google Play Store-ban vagy App Store-ban, amíg az NVH Source Locator a háttérben fut, az alkalmazáshoz való visszatérés automatikusan észleli az új vásárlást és feloldja a Pro-t — nincs szükség kézi visszaállításra.

### Promóciós kód beváltás

**Android**: a paywallban lévő „Van Google Play promóciós kódja?" gomb megnyitja a Google Play beváltási folyamatot az előre kitöltött kódjával.

**iOS**: Az App Store irányelv 3.1.1 megköveteli az Apple hivatalos „Kód beváltása" folyamatán keresztüli beváltást. A Google Play gomb el van rejtve iOS-en. Ehelyett keresse az „App Store kód beváltása" lehetőséget a Beállításokban.

---

## Help lap és oktatóanyagok

A **Help** lap tartalmaz alkalmazáson belüli oktatóanyagokat, legjobb gyakorlati útmutatókat és referenciainformációkat.

![Help lap](../screenshots/10-help-tab.png)

Lefedett témák:
- Milyen felszerelésre van szüksége
- Hogyan helyezze el az érzékelőket a legjobb pontosságért
- Kalibrálási tippek
- Gyakori mérési forgatókönyvek
- Tippek trianguláláshoz és 3D elhelyezésekhez
- Kábelvezetés és jelminőség

---

## Hibaelhárítás

### A számítás eredménye rossz vagy nincs értelme

1. Ellenőrizze a kalibrációt. Az automatikusan kitöltött `tCal` a publikált anyag sebességét feltételezi — a valós anyagok különbözőek. A legpontosabb kalibrálás az in-situ: érintsen meg egy ismert helyet, és hagyja, hogy az alkalmazás levezesse a tényleges sebességet.
2. Ellenőrizze az **Első érzékelő** beállítást — melyik érzékelő hallotta először az eseményt, számít a matematikának.
3. Ellenőrizze a távolságméréseit. Néhány mm-es hibák terjednek.

### A toast azt mondja „Eredmény tartományon kívül"

A matematika azt mondja, hogy a forrás nincs az érzékelői között. Lehetséges okok:
- A forrás valóban az érzékelővonalon/síkon kívül van
- Az egyik bemenete rossz
- A kalibrálási sebesség túl messze van a valóságtól

### A számítási sebesség javaslat figyelmeztető színt mutat

A bemeneteiből származó implicit hangsebesség messze van bármely gyakori anyagétól (kevesebb mint 50 m/s vagy több mint 20 000 m/s). Ellenőrizze a bemeneteit — valószínűleg elírás van a tCal-ban vagy távolságban.

### A Materials választó eltérő sebességeket mutat, mint amire számít

Ellenőrizze a Referencia hőmérsékletet a Beállításokban. Ha nem 20 °C, a megjelenített sebességek hőmérséklet-kompenzációt tükröznek. Az alkalmazás „ref X @ 20°C"-ot mutat a kompenzált sebességek alatt, hogy ellenőrizhesse.

### Az előzménybejegyzés más eredménnyel játszódik le

Az 1.75 alkalmazás verzió előtt létrehozott régi előzménybejegyzések lehet, hogy nem tárolták a hőmérsékletet. Ha a mérést nem 20 °C-on végezte, a lejátszás az aktuális beállítást használja. Kézzel állítsa be a hőmérsékletet a Beállításokban a lejátszás előtt, VAGY mérje újra.

### A fotóannotáció jelölői nem ott vannak, ahol várom

A jelölők a bemeneti geometria alapján automatikusan helyezkednek el. Húzza őket a beállításhoz. A jelölők igazítása frissíti a forrás pozícióját a fényképrétegben — de NEM változtatja meg az alapul szolgáló számítási eredményt.

### Sikertelen biztonsági mentés/visszaállítás

Győződjön meg arról, hogy ugyanaz vagy újabb verziójú alkalmazás által generált mentési fájlt használ. A régebbi mentési fájlokból hiányozhatnak az aktuális adatmezők.

### A vásárlás visszaállítása azt mondja „nem található vásárlás"

1. Ellenőrizze, hogy ugyanahhoz az áruházi fiókhoz csatlakozott, amelyet a vásárláskor használt
2. Ellenőrizze, hogy a vásárlást nem térítették vissza vagy nem járt le
3. Próbálja meg eltávolítani és újratelepíteni az alkalmazást (a vásárlás az áruházi fiókjához van kötve, nem az alkalmazás telepítéséhez)
4. Ha a probléma továbbra is fennáll, vegye fel a kapcsolatot a support@evdiag.net címmel

### A numerikus bemenet váratlanul 0-ra ugrik

Tervezés szerint: amikor elhagy egy számmezőt (máshová koppint), ha üres, negatív vagy nem-numerikus szöveget tartalmaz, 0-ra ugrik. Megakadályozza a csendben megsérült számításokat a véletlenül törölt bemenetekből. A hőmérséklet bemenet kivétel (helyette -40/+200-ra korlátozódik).

### Több segítségre van szüksége

Vegye fel a kapcsolatot a `support@evdiag.net` címmel:
- Eszközmodell és OS verzió
- Alkalmazásverzió (Beállítások → oldal alja)
- Annak leírása, hogy mit próbált
- Képernyőképek, ha lehetséges

---

*NVH Source Locator-t az EVDiag fejleszti. Látogasson el a https://evdiag.net oldalra frissítésekért és erőforrásokért.*
