# NVH Source Locator — Používateľská príručka

NVH Source Locator je merací nástroj na lokalizáciu zdrojov hluku a vibrácií pomocou TDOA (Time Difference of Arrival) zo signálov akcelerometrov zachytených na osciloskope alebo meracom systéme.

Táto príručka pokrýva všetky funkcie. Pre stručné pripomenutie pozri **Stručná príručka**.

---

## Obsah

1. [Ako to funguje](#how-it-works)
2. [Pred začiatkom](#before-you-start)
3. [Hlavné karty](#the-main-tabs)
4. [Režim 2-Sensor](#2-sensor-mode)
5. [Režim 3-Sensor](#3-sensor-mode)
6. [Režimy Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Karta Materials](#the-materials-tab)
8. [Teplotná kompenzácia](#temperature-compensation)
9. [Anotácia fotografie](#photo-annotation)
10. [Reporty](#reports)
11. [Záloha a obnova](#backup-and-restore)
12. [Nastavenia](#settings)
13. [Funkcie Pro](#pro-features)
14. [Karta Help a návody](#help-tab-and-tutorials)
15. [Riešenie problémov](#troubleshooting)

---

## Ako to funguje {#how-it-works}

Keď zdroj hluku vydáva zvuk alebo vibrácie, vlna sa šíri materiálom známou rýchlosťou. Ak na materiál umiestnite dva alebo viac akcelerometrov a zmeriate, kedy vlna dorazí ku každému z nich, časový rozdiel vám povie, kde sa zdroj nachádza.

NVH Source Locator preberá:

- **Kalibráciu**: vzdialenosť medzi senzormi a čas, ktorý vlna potrebuje na prekonanie tejto vzdialenosti (používa sa na výpočet rýchlosti zvuku materiálu)
- **Udalosť**: časový rozdiel medzi senzormi detekujúcimi udalosť hluku/vibrácie

Potom vypočíta, kde sa zdroj nachádza v štruktúre.

Čím viac senzorov použijete, tým presnejšie môžete zdroj lokalizovať:

- **2 senzory** → vzdialenosť pozdĺž čiary
- **3 senzory** → poloha na 2D ploche (X, Y)
- **4 senzory** → poloha v 3D priestore (X, Y, Z)

---

## Pred začiatkom {#before-you-start}

Budete potrebovať:

- **Osciloskop alebo merací systém**, ktorý vám môže zobraziť časový rozdiel medzi kanálmi akcelerometra v mikrosekundách (µs)
- **Aspoň 2 akcelerometre** fyzicky pripevnené k štruktúre (viac senzorov = vyššia presnosť)
- **Spôsob merania vzdialenosti** medzi senzormi (meter, šuplera)
- **Spôsob vyvolania vlny** na známom mieste pre kalibráciu (kalibrovaný úder kladivom, klepnutie skrutkovačom alebo iný známy signál)

![Domovská obrazovka s kartou 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Hlavné karty {#the-main-tabs}

Aplikácia má karty hore:

![Lišta kariet](../screenshots/02-tab-bar.png)

| Karta | Čo robí | Kedy použiť |
|---|---|---|
| **2-Sensor** | 1D lokalizácia zdroja pozdĺž čiary medzi 2 senzormi | Rýchle kontroly, štruktúry podobné nosníkom. **Plne zadarmo.** |
| **3-Sensor** | 2D lokalizácia zdroja pomocou 3 senzorov v trojuholníku | Najvšeobecnejšie použitie, panely a plochy |
| **3-Sen+** | 3-Sensor s preurčeným riešením metódy najmenších štvorcov | Náročnejšie merania, odolné proti šumu |
| **4-Sensor** | 2D lokalizácia pomocou dvoch párov (A-B + C-D) | Pravouhlé usporiadanie senzorov, krížová kontrola |
| **4-Sen+** | Pokročilý 2D režim, 4 senzory v ľubovoľných polohách | Nepravouhlé geometrie, plný LSQ |
| **3D** | 3D lokalizácia zdroja pomocou 4 senzorov so súradnicami XYZ | Zložité štruktúry v 3D priestore |
| **3D+** | 3D s až 6 senzormi, preurčené LSQ | Veľmi zložité geometrie, maximálna presnosť |
| **Materials** | Knižnica rýchlosti zvuku + vlastné materiály | Vyberá sa raz za meraciu reláciu |
| **Help** | Návody v aplikácii a referencie | Keď potrebujete rýchle pripomenutie |

> **Zadarmo vs Pro**: Karta 2-Sensor je plne zadarmo. Ostatné karty sú prístupné, ale majú konkrétne vstupné polia zamknuté pre Pro používateľov (označené zlatým odznakom zámku). Klepnutím na zamknuté pole sa zobrazí paywall Pro.

Nastavenia sú prístupné cez ikonu ozubeného kolesa ⚙ v pravom hornom rohu (nie je to karta).

---

## Režim 2-Sensor {#2-sensor-mode}

Najjednoduchšie meranie: lokalizácia zdroja pozdĺž čiary medzi dvoma akcelerometrami.

![Karta 2-Sensor](../screenshots/01-home-2sensor.png)

### Krok 1: Aplikovať materiál

Klepnite na kartu Materials. Vyberte materiál, z ktorého je vaša štruktúra vyrobená (napr. „Hliník", „Oceľ, Mild (1020)"). Aplikácia používa známu rýchlosť zvuku materiálu na automatické vyplnenie poľa kalibračného času.

Ak materiál vašej štruktúry nie je v zozname, môžete dočasne vybrať „Vzduch" a v kroku 2 manuálne prepísať kalibračný čas.

### Krok 2: Zadať kalibračné údaje

Na karte 2-Sensor uvidíte dve sekcie párov: **Pár A–B** a **Pár A–C** (ak máte iba 2 senzory, vyžaduje sa iba A–B).

Pre každý pár vypĺňate:

- **Vzdialenosť senzorov** (`d`): fyzická vzdialenosť medzi senzormi v cm alebo palcoch (nastavená v Nastaveniach)
- **Oneskorenie kalibračného času** (`tCal`): čas, za ktorý sa vlna pohybuje medzi senzormi rýchlosťou zvuku materiálu — automaticky vyplnené, keď vyberiete materiál, ale môžete prepísať

### Krok 3: Zadať čas udalosti

- **Oneskorenie času udalosti** (`tEvent`): časový rozdiel medzi senzormi detekujúcimi udalosť hluku v mikrosekundách
- **Prvý senzor**: ktorý senzor udalosť počul ako prvý (A alebo B)

### Krok 4: Prečítať výsledok

Aplikácia zobrazí polohu zdroja ako vzdialenosť od senzora A:
- Výsledok = 0: zdroj je pri senzore A
- Výsledok = vzdialenosť: zdroj je pri senzore B
- Výsledok medzi: zdroj je medzi nimi
- Výsledok mimo: zdroj je za jedným zo senzorov (toast varuje)

Karta výsledku zobrazuje obe vzdialenosti (od A, od B) a označuje, ktorý senzor je bližšie.

### Krok 5 (voliteľný): Anotovať fotografiu

Klepnutím na **📷 Anotovať fotografiu** vytvoríte fotografiu vašej zostavy. Aplikácia prekryje značky pre senzory A, B a zdroj. Užitočné pre reporty.

---

## Režim 3-Sensor {#3-sensor-mode}

Lokalizuje zdroj na 2D rovine pomocou troch senzorov usporiadaných do trojuholníka.

![Karta 3-Sensor](../screenshots/03-3sensor-tab.png)

### Nastavenie

Umiestnite tri senzory na svoju štruktúru tvoriacu trojuholník. Rovnoramenný, pravouhlý alebo rôznostranný — aplikácia zvládne všetky geometrie.

### Zadať údaje

V sekcii **Dĺžky strán trojuholníka** zadajte fyzickú vzdialenosť pre všetky tri strany (A–B, A–C, B–C).

Pre každý pár (A–B a A–C) zadajte:
- **tCal**: kalibračný čas (automaticky vyplnený z materiálu)
- **tEvent**: nameraný časový rozdiel pre udalosť hluku
- **Prvý senzor**: ktorý ju počul ako prvý

### Prečítať výsledok

Aplikácia zobrazí polohu zdroja ako súradnice X, Y vzhľadom na senzor A (senzor A v počiatku, senzor B na osi X). Vizualizácia ukazuje všetky tri senzory a polohu zdroja.

![Výsledok trojuholníka](../screenshots/04-triangle-result.png)

---

## Režimy Pro+ {#pro-modes}

Niekoľko pokročilých kariet ponúka preurčené riešenia a vyššiu dimenzionalitu:

### 3-Sen+ (Pro)

Rovnaké nastavenie trojuholníka ako 3-Sensor, ale kalibrujte A merajte všetky tri páry (A–B, A–C, B–C). Riešenie používa všetky 3 TDOA v aproximácii metódou najmenších štvorcov — odolnejšie proti meraciemu šumu a anizotropným materiálom. Rezíduá pre každý pár sú hlásené, takže môžete odhaliť nekonzistentné merania.

### 4-Sensor

Umiestnite štyri senzory okolo oblasti:
- **A–B** = horizontálny pár (ľavé/pravé strany)
- **C–D** = vertikálny pár (horné/spodné strany)

Najprv spustite pár A–B (horizontálny), potom pár C–D (vertikálny). 2D mapa zobrazuje priesečník. Každý pár sa kalibruje samostatne — užitočné, keď sa materiál mení naprieč štruktúrou.

### 4-Sen+ (Pokročilý 2D)

Štyri senzory v ľubovoľných polohách (nie sú nútene pravouhlé). Spárujte A s každým z B, C, D a kalibrujte samostatne. Preurčené riešenie metódou najmenších štvorcov spriemerňuje merací šum medzi pármi a hlási rezíduá pre každý pár.

### 3D

Plné 3D meranie so 4 senzormi umiestnenými v 3D priestore. Zadajte súradnice (X, Y, Z) každého senzora a kalibračné časy a časy udalostí pre každý pár (A–B, A–C, A–D).

### 3D+ (Pro)

Ako 3D, ale podporuje až **6 senzorov** (A až F) s preurčeným LSQ. Maximálna presnosť pre zložité 3D geometrie.

---

## Karta Materials {#the-materials-tab}

Knižnica bežných technických materiálov so známou rýchlosťou zvuku pri 20 °C.

![Karta Materials](../screenshots/05-materials-tab.png)

### Zoznam materiálov

Zoznam obsahuje vzduch, tekutiny, gumy, polyméry, drevá, sklá a kovy. Rýchlosti sa pohybujú od ~340 m/s (vzduch) do ~13 000 m/s (niektoré kovy pri izbovej teplote).

### Vstavané materiály s teplotnou kompenzáciou

14 bežne používaných kovov obsahuje údaje o teplotnom koeficiente. Keď sa referenčná teplota v Nastaveniach líši od 20 °C, aplikácia automaticky upravuje rýchlosti týchto materiálov:

- Hliník
- Oceľ, Mild (1020)
- Nerezová oceľ (304)
- Železo (liatina)
- Železo
- Meď
- Mosadz
- Bronz
- Titán
- Horčík
- Olovo
- Zinok
- Nikel
- Volfrám

Materiály s kompenzáciou zobrazujú dve hodnoty vo výbere: **kompenzovanú rýchlosť** (veľkú, výraznú) a **referenčnú rýchlosť pri 20 °C** (malú, sivú pod ňou).

Materiály bez kompenzácie zobrazujú **„ref only"** kurzívou — ich uvedená rýchlosť sa používa tak, ako je, bez ohľadu na teplotu.

### Vlastné materiály

Ak zmeráte kalibráciu na karte 2-Sensor, môžete výsledok uložiť ako vlastný materiál. Po úspešnom 2-sensor meraní hľadajte možnosť uložiť odvodenú rýchlosť pod menom podľa vášho výberu.

Vlastné materiály ukladajú rýchlosť zmeranú in-situ; nikdy nepoužívajú teplotnú kompenzáciu (rýchlosť už bola zmeraná pri testovacej teplote).

### Obľúbené

Klepnite na hviezdičku vedľa ľubovoľného materiálu, aby ste ho označili ako obľúbený. Obľúbené sa zobrazujú v hornej časti zoznamu pre rýchly prístup.

### Vyhľadávanie

Použite vyhľadávaciu lištu hore na filtrovanie materiálov podľa názvu. Vyhľadávanie zodpovedá ako anglickým kanonickým názvom, tak preloženým zobrazovaným názvom.

---

## Teplotná kompenzácia {#temperature-compensation}

Rýchlosť zvuku v materiáloch sa mení s teplotou. V automobilových NVH testoch je to dôležité: motorový priestor pri 80 °C, schladnutá kabína pri -10 °C alebo oblasť výfukového potrubia pri 200 °C sa správajú odlišne od izbových laboratórnych podmienok.

### Nastavenie teploty

Otvorte Nastavenia (ikona ⚙) → Referenčná teplota. Zadajte teplotu vášho testovacieho prostredia v °C (rozsah -40 až +200).

![Panel Nastavenia](../screenshots/06-settings.png)

### Čo sa stane, keď teplota ≠ 20 °C

- Polia kalibračného času sa automaticky vyplnia teplotne upravenou rýchlosťou
- Výber Materials prominentne zobrazuje upravenú rýchlosť
- Toast potvrdzuje: *„Hliník aplikovaný (6 284 m/s @ 60 °C) — aktualizovaných N párov"*
- Náznak „Najbližší materiál" porovnáva s teplotne upravenými rýchlosťami
- Uložené záznamy histórie zaznamenávajú aktívnu teplotu
- Reporty obsahujú riadok zápätia: *„Referenčná teplota: 60 °C, aplikovaná kompenzácia"*

### Reset pri štarte aplikácie

Referenčná teplota **sa vždy resetuje na 20 °C** pri štarte aplikácie. To zabraňuje, aby zastarané nastavenia z minulej meracej relácie ticho ovplyvňovali dnešnú prácu. Malá kurzíva v Nastaveniach vám pripomína toto správanie.

Ak chcete prehrať historické meranie pri jeho pôvodnej teplote, stačí klepnúť na záznam — teplota sa obnoví automaticky.

### Materiály bez kompenzácie

Väčšina nekovových materiálov nemá spoľahlivé publikované teplotné koeficienty. Aplikácia pre ne zobrazuje odznak **„ref only"** — ich uvedená rýchlosť sa používa bez ohľadu na nastavenie teploty. Ak potrebujete presné merania pri ne-izbových teplotách pre tieto materiály, vykonajte in-situ kalibráciu a uložte výsledok ako vlastný materiál.

---

## Anotácia fotografie {#photo-annotation}

Po úspešnom výpočte klepnite na tlačidlo **📷 Anotovať fotografiu**, aby ste prekryli značky senzorov a zdroja na fotografii vašej zostavy.

![Anotácia fotografie](../screenshots/08-photo-annotation.png)

### Postup

1. Klepnite na **Anotovať fotografiu** — otvorí sa systémová kamera
2. Vytvorte fotografiu umiestnenia senzorov
3. Aplikácia načíta fotografiu do prekryvnej anotácie
4. Značky senzorov (A, B, C, D, E, F podľa potreby — až 6 senzorov) a značka zdroja sa automaticky umiestnia na základe vášho výpočtu
5. Pretiahnite ľubovoľnú značku pre jemné nastavenie polohy. Pri úprave sa poloha zdroja prepočítava z opravených pozícií senzorov
6. Klepnite na **Uložiť** pre zachovanie alebo **Vytvoriť znova** pre nový pokus

Anotovaná fotografia je automaticky zahrnutá do PDF reportov.

---

## Reporty {#reports}

Klepnite na tlačidlo **Tlač výsledku** na ľubovoľnej obrazovke výsledku pre generovanie formátovaného reportu.

![PDF report](../screenshots/09-pdf-report.png)

### Obsah reportu

- Záhlavie (prispôsobiteľné v Nastavenia → Záhlavie reportu)
- Názov merania a časová pečiatka
- Všetky vstupné hodnoty v prehľadnej tabuľke
- Výsledok výpočtu
- Text záveru
- Vizualizácia (geometrický graf)
- Anotovaná fotografia (ak ste ju vytvorili)
- Riadok zápätia s teplotou (ak bola kompenzácia aktívna)
- Číslo strany a riadok so zaslúženými údajmi

### Formát výstupu

- **Android**: natívne generovanie PDF, uloženie do telefónu alebo zdieľanie
- **iOS**: systémový dialóg tlače → uložiť ako PDF, AirPrint alebo zdieľať

### Prispôsobenie záhlavia

Nastavenia → Záhlavie reportu. Zadajte názov vašej spoločnosti, názov laboratória, info o projekte alebo čokoľvek chcete v hornej časti každého reportu.

---

## Záloha a obnova {#backup-and-restore}

Uložte všetky svoje vlastné materiály, obľúbené, nastavenia a históriu do jedného súboru. Prenos medzi zariadeniami.

### Záloha

Nastavenia → **Záloha** → klepnite na „Uložiť záložný súbor". Aplikácia vygeneruje JSON súbor a otvorí zdieľací hárok vášho telefónu. Uložte ho do svojho cloudového úložiska (Google Drive, iCloud, OneDrive), pošlite si ho e-mailom alebo preneste akokoľvek chcete.

### Obnova

Nastavenia → **Obnova** → vyberte záložný súbor z úložiska vášho telefónu. Aplikácia importuje vlastné materiály, obľúbené, históriu a nastavenia.

⚠️ **Obnova nahradí vaše aktuálne údaje.** Ak máte na aktuálnom zariadení dôležité merania, najprv ich zálohujte pred obnovením z inej zálohy.

---

## Nastavenia {#settings}

Prístup cez ikonu ozubeného kolesa ⚙ v pravom hornom rohu. Nastavenia sú modálne, nie karta.

![Nastavenia](../screenshots/06-settings.png)

| Nastavenie | Čo riadi |
|---|---|
| **Upgrade na Pro** | Kúpiť alebo sa dozvedieť o funkciách Pro ($19,99) |
| **Jazyk** | Zobrazovací jazyk aplikácie (podporované 30) |
| **Téma** | Svetlé, Tmavé alebo Auto (nasledovať systém) |
| **Jednotka vzdialenosti** | cm alebo palce |
| **Referenčná teplota** | Aktívna teplota pre kompenzáciu, -40 až +200 °C |
| **Záhlavie reportu** | Vlastný text v hornej časti generovaných reportov |
| **Záloha** | Exportovať všetky údaje do súboru |
| **Obnova** | Importovať údaje zo záložného súboru |
| **Obnoviť nákup** | Znovu získať Pro na novom zariadení |

---

## Funkcie Pro {#pro-features}

NVH Source Locator používa **freemium model so zámkom funkcií**:

- **Zadarmo**: Karta 2-Sensor je plne funkčná bez obmedzení
- **Pro**: Všetky ostatné karty majú konkrétne vstupné polia zamknuté. Paywall sa zobrazí, keď používateľ s bezplatnou verziou klepne na zamknuté pole

### Čo je zamknuté

Polia vyžadujúce Pro sú rozptýlené v:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Režimy 3D a 3D+
- Záloha a Obnova
- PDF reporty
- Vlastné materiály
- Anotácia fotografie

Používateľ s bezplatnou verziou môže OTVORIŤ ľubovoľnú kartu a VIDIEŤ rozhranie. Jednoducho nemôže zadávať hodnoty do Pro-zamknutých vstupných polí.

![Pro-zamknuté pole](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Keď používateľ s bezplatnou verziou klepne na zamknuté pole, paywall vyjde a zobrazí:
- Ikonu aplikácie s odznakom PRO
- Zoznam funkcií
- Tlačidlo odomknutia s cenou ($19,99 predvolené; môže sa líšiť podľa regiónu)
- Uplatnenie promo kódu (iba Android — iOS používa samostatný tok Offer Code od Apple)
- Voliteľný promo odkaz na komunitné kanály

### Nákup Pro

Klepnite na ľubovoľné zamknuté pole alebo klepnite na **Upgrade na Pro** v Nastaveniach. Používa oficiálny platobný systém vašej platformy (Google Play na Androide, Apple App Store na iOS).

### Obnovenie Pro na novom zariadení

Ak ste zakúpili na jednom zariadení a chcete Pro na inom (rovnaký účet):

1. Prihláste sa k **rovnakému** účtu Google (Android) alebo Apple ID (iOS), ktoré ste použili na nákup
2. Otvorte NVH Source Locator na novom zariadení
3. Prejdite do Nastavenia → **Obnoviť nákup**
4. Aplikácia overí v záznamoch nákupov platformy a odomkne Pro

### Automatická obnova pri štarte

Ak uplatníte promo kód v Google Play Store alebo App Store, zatiaľ čo NVH Source Locator beží na pozadí, návrat do aplikácie automaticky deteguje nový nákup a odomkne Pro — manuálna obnova nie je potrebná.

### Uplatnenie promo kódu

**Android**: tlačidlo „Máte promo kód Google Play?" v paywall otvorí tok uplatnenia Google Play s vaším predvyplneným kódom.

**iOS**: Politika App Store 3.1.1 vyžaduje uplatnenie prostredníctvom oficiálneho toku „Uplatniť kód" od Apple. Tlačidlo Google Play je v iOS skryté. Namiesto toho hľadajte „Uplatniť kód App Store" v Nastaveniach.

---

## Karta Help a návody {#help-tab-and-tutorials}

Karta **Help** obsahuje návody v aplikácii, príručky najlepších postupov a referenčné informácie.

![Karta Help](../screenshots/10-help-tab.png)

Pokryté témy:
- Aké vybavenie potrebujete
- Ako umiestniť senzory pre najlepšiu presnosť
- Tipy na kalibráciu
- Bežné meracie scenáre
- Tipy na trianguláciu a 3D umiestnenie
- Vedenie káblov a kvalita signálu

---

## Riešenie problémov {#troubleshooting}

### Výsledok výpočtu je zlý alebo nedáva zmysel

1. Skontrolujte kalibráciu. Automaticky vyplnené `tCal` predpokladá publikovanú rýchlosť materiálu — skutočné materiály sa líšia. Najpresnejšia kalibrácia je in-situ: klepnite na známe miesto a nechajte aplikáciu odvodiť skutočnú rýchlosť.
2. Skontrolujte nastavenie **Prvý senzor** — ktorý senzor počul udalosť ako prvý, je dôležité pre matematiku.
3. Overte merania vzdialenosti. Chyby niekoľkých mm sa šíria.

### Toast hovorí „Výsledok mimo rozsahu"

Matematika hovorí, že zdroj nie je medzi vašimi senzormi. Možné príčiny:
- Zdroj je skutočne mimo línie/roviny senzorov
- Jeden z vašich vstupov je nesprávne
- Kalibračná rýchlosť je príliš ďaleko od reality

### Nápoveda vypočítanej rýchlosti zobrazuje varovnú farbu

Implikovaná rýchlosť zvuku z vašich vstupov je ďaleko od akéhokoľvek bežného materiálu (menej ako 50 m/s alebo viac ako 20 000 m/s). Skontrolujte vstupy — pravdepodobne preklep v tCal alebo vzdialenosti.

### Výber Materials zobrazuje iné rýchlosti, než sa očakávalo

Skontrolujte referenčnú teplotu v Nastaveniach. Ak nie je 20 °C, zobrazené rýchlosti odrážajú teplotnú kompenzáciu. Aplikácia zobrazuje „ref X @ 20°C" pod kompenzovanými rýchlosťami, aby ste mohli overiť.

### Záznam histórie sa prehráva s iným výsledkom

Staré záznamy histórie vytvorené pred verziou aplikácie 1.75 možno neuložili teplotu. Ak ste vykonali meranie pri ne-20 °C teplote, prehrávanie použije aktuálne nastavenie. Pred prehrávaním manuálne nastavte teplotu v Nastaveniach ALEBO znova zmerajte.

### Značky anotácie fotografie nie sú tam, kde očakávam

Značky sa umiestňujú automaticky podľa vstupnej geometrie. Pretiahnite ich pre úpravu. Úprava značiek aktualizuje polohu zdroja v prekryve fotografie — ale NEMENÍ základný výsledok výpočtu.

### Záloha/Obnova zlyháva

Uistite sa, že používate záložný súbor generovaný rovnakou alebo novšou verziou aplikácie. Staršie záložné súbory nemusia mať aktuálne dátové polia.

### Obnoviť nákup hovorí „nenájdený žiadny nákup"

1. Overte, že ste prihlásený k rovnakému účtu obchodu, ktorý ste použili na nákup
2. Overte, že nákup nebol refundovaný alebo nevypršal
3. Skúste aplikáciu odinštalovať a preinštalovať (nákup je viazaný na váš účet obchodu, nie na inštaláciu aplikácie)
4. Ak problém pretrváva, kontaktujte support@evdiag.net

### Číselný vstup sa neočakávane mení na 0

Zámerne: keď opustíte číselné pole (klepnete inde) a je prázdne, záporné alebo obsahuje nečíselný text, prepne sa na 0. Zabraňuje tichým rozbitým výpočtom z náhodne vymazaných vstupov. Vstup teploty je výnimkou (namiesto toho sa obmedzí na -40/+200).

### Potrebujem ďalšiu pomoc

Kontaktujte `support@evdiag.net` s:
- Modelom zariadenia a verziou OS
- Verziou aplikácie (Nastavenia → spodok stránky)
- Popisom toho, čo ste skúsili
- Snímkami obrazovky, ak je to možné

---

*NVH Source Locator je vyvíjaný spoločnosťou EVDiag. Navštívte https://evdiag.net pre aktualizácie a zdroje.*
