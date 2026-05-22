"""User Guide translations — batch 3.

5 languages: cs, sk, hu, hr, bg.
"""

USER_GUIDE_TRANSLATIONS = {

'cs': """# NVH Source Locator — Uživatelská příručka

NVH Source Locator je měřicí nástroj pro lokalizaci zdrojů hluku a vibrací pomocí TDOA (Time Difference of Arrival) ze signálů akcelerometrů zachycených na osciloskopu nebo měřicím systému.

Tato příručka pokrývá všechny funkce. Pro stručné připomenutí viz **Stručná příručka**.

---

## Obsah

1. [Jak to funguje](#how-it-works)
2. [Před začátkem](#before-you-start)
3. [Hlavní záložky](#the-main-tabs)
4. [Režim 2-Sensor](#2-sensor-mode)
5. [Režim 3-Sensor](#3-sensor-mode)
6. [Režimy Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Záložka Materials](#the-materials-tab)
8. [Teplotní kompenzace](#temperature-compensation)
9. [Anotace fotografie](#photo-annotation)
10. [Reporty](#reports)
11. [Záloha a obnova](#backup-and-restore)
12. [Nastavení](#settings)
13. [Funkce Pro](#pro-features)
14. [Záložka Help a návody](#help-tab-and-tutorials)
15. [Řešení problémů](#troubleshooting)

---

## Jak to funguje {#how-it-works}

Když zdroj hluku vydává zvuk nebo vibrace, vlna se šíří materiálem známou rychlostí. Pokud na materiál umístíte dva nebo více akcelerometrů a změříte, kdy vlna dorazí ke každému z nich, časový rozdíl vám řekne, kde se zdroj nachází.

NVH Source Locator přijímá:

- **Kalibraci**: vzdálenost mezi senzory a čas, který vlna potřebuje k překonání této vzdálenosti (používá se k výpočtu rychlosti zvuku materiálu)
- **Událost**: časový rozdíl mezi senzory detekujícími událost hluku/vibrace

Pak vypočítá, kde se zdroj nachází ve struktuře.

Čím více senzorů použijete, tím přesněji můžete zdroj lokalizovat:

- **2 senzory** → vzdálenost podél čáry
- **3 senzory** → poloha na 2D ploše (X, Y)
- **4 senzory** → poloha v 3D prostoru (X, Y, Z)

---

## Před začátkem {#before-you-start}

Budete potřebovat:

- **Osciloskop nebo měřicí systém**, který může zobrazit časový rozdíl mezi kanály akcelerometru v mikrosekundách (µs)
- **Nejméně 2 akcelerometry** fyzicky připevněné ke struktuře (více senzorů = vyšší přesnost)
- **Způsob měření vzdálenosti** mezi senzory (metr, šuplera)
- **Způsob vyvolání vlny** na známém místě pro kalibraci (kalibrovaný úder kladivem, klepnutí šroubovákem nebo jiný známý signál)

![Domovská obrazovka se záložkou 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Hlavní záložky {#the-main-tabs}

Aplikace má záložky nahoře:

![Lišta záložek](../screenshots/02-tab-bar.png)

| Záložka | Co dělá | Kdy použít |
|---|---|---|
| **2-Sensor** | 1D lokalizace zdroje podél čáry mezi 2 senzory | Rychlé kontroly, struktury podobné nosníkům. **Plně zdarma.** |
| **3-Sensor** | 2D lokalizace zdroje pomocí 3 senzorů v trojúhelníku | Nejobecnější použití, panely a plochy |
| **3-Sen+** | 3-Sensor s přeurčeným řešením metody nejmenších čtverců | Náročnější měření, odolné proti šumu |
| **4-Sensor** | 2D lokalizace pomocí dvou párů (A-B + C-D) | Pravoúhlé uspořádání senzorů, křížová kontrola |
| **4-Sen+** | Pokročilý 2D režim, 4 senzory v libovolných pozicích | Nepravoúhlé geometrie, plný LSQ |
| **3D** | 3D lokalizace zdroje pomocí 4 senzorů se souřadnicemi XYZ | Složité struktury v 3D prostoru |
| **3D+** | 3D s až 6 senzory, přeurčené LSQ | Velmi složité geometrie, maximální přesnost |
| **Materials** | Knihovna rychlosti zvuku + vlastní materiály | Vybírá se jednou za měřicí relaci |
| **Help** | Návody v aplikaci a reference | Když potřebujete rychlé připomenutí |

> **Zdarma vs Pro**: Záložka 2-Sensor je plně zdarma. Ostatní záložky jsou přístupné, ale mají konkrétní vstupní pole zamčená pro Pro uživatele (označená zlatým odznakem zámku). Klepnutím na zamčené pole se zobrazí paywall Pro.

Nastavení je přístupné přes ikonu ozubeného kola ⚙ v pravém horním rohu (není to záložka).

---

## Režim 2-Sensor {#2-sensor-mode}

Nejjednodušší měření: lokalizace zdroje podél čáry mezi dvěma akcelerometry.

![Záložka 2-Sensor](../screenshots/01-home-2sensor.png)

### Krok 1: Aplikovat materiál

Klepněte na záložku Materials. Vyberte materiál, ze kterého je vaše struktura vyrobena (např. „Hliník", „Ocel, Mild (1020)"). Aplikace používá známou rychlost zvuku materiálu k automatickému vyplnění pole kalibračního času.

Pokud materiál vaší struktury není v seznamu, můžete dočasně vybrat „Vzduch" a v kroku 2 ručně přepsat kalibrační čas.

### Krok 2: Zadat kalibrační data

Na záložce 2-Sensor uvidíte dvě sekce párů: **Pár A–B** a **Pár A–C** (pokud máte pouze 2 senzory, vyžaduje se pouze A–B).

Pro každý pár vyplníte:

- **Vzdálenost senzorů** (`d`): fyzická vzdálenost mezi senzory v cm nebo palcích (nastavena v Nastavení)
- **Zpoždění kalibračního času** (`tCal`): čas, za který se vlna pohybuje mezi senzory rychlostí zvuku materiálu — automaticky vyplněno, když vyberete materiál, ale můžete přepsat

### Krok 3: Zadat čas události

- **Zpoždění času události** (`tEvent`): časový rozdíl mezi senzory detekujícími událost hluku v mikrosekundách
- **První senzor**: který senzor událost slyšel jako první (A nebo B)

### Krok 4: Přečíst výsledek

Aplikace zobrazí polohu zdroje jako vzdálenost od senzoru A:
- Výsledek = 0: zdroj je u senzoru A
- Výsledek = vzdálenost: zdroj je u senzoru B
- Výsledek mezi: zdroj je mezi nimi
- Výsledek mimo: zdroj je za jedním ze senzorů (toast varuje)

Karta výsledku zobrazuje obě vzdálenosti (od A, od B) a označuje, který senzor je blíže.

### Krok 5 (volitelný): Anotovat fotografii

Klepnutím na **📷 Anotovat fotografii** pořídíte fotografii své sestavy. Aplikace překryje značky pro senzory A, B a zdroj. Užitečné pro reporty.

---

## Režim 3-Sensor {#3-sensor-mode}

Lokalizuje zdroj na 2D rovině pomocí tří senzorů uspořádaných do trojúhelníku.

![Záložka 3-Sensor](../screenshots/03-3sensor-tab.png)

### Nastavení

Umístěte tři senzory na svou strukturu tvořící trojúhelník. Rovnoramenný, pravoúhlý nebo různostranný — aplikace zvládne všechny geometrie.

### Zadat data

V sekci **Délky stran trojúhelníku** zadejte fyzickou vzdálenost pro všechny tři strany (A–B, A–C, B–C).

Pro každý pár (A–B a A–C) zadejte:
- **tCal**: kalibrační čas (automaticky vyplněn z materiálu)
- **tEvent**: naměřený časový rozdíl pro událost hluku
- **První senzor**: který ji slyšel jako první

### Přečíst výsledek

Aplikace zobrazí polohu zdroje jako souřadnice X, Y vzhledem k senzoru A (senzor A v počátku, senzor B na ose X). Vizualizace ukazuje všechny tři senzory a polohu zdroje.

![Výsledek trojúhelníku](../screenshots/04-triangle-result.png)

---

## Režimy Pro+ {#pro-modes}

Několik pokročilých záložek nabízí přeurčená řešení a vyšší dimenzionalitu:

### 3-Sen+ (Pro)

Stejné nastavení trojúhelníku jako 3-Sensor, ale kalibrujte A měřte všechny tři páry (A–B, A–C, B–C). Řešení používá všechny 3 TDOA v aproximaci metodou nejmenších čtverců — odolnější proti měřicímu šumu a anizotropním materiálům. Rezidua pro každý pár jsou hlášena, takže můžete odhalit nekonzistentní měření.

### 4-Sensor

Umístěte čtyři senzory kolem oblasti:
- **A–B** = horizontální pár (levé/pravé strany)
- **C–D** = vertikální pár (horní/spodní strany)

Nejprve spusťte pár A–B (horizontální), pak pár C–D (vertikální). 2D mapa zobrazuje průsečík. Každý pár se kalibruje samostatně — užitečné, když se materiál mění napříč strukturou.

### 4-Sen+ (Pokročilý 2D)

Čtyři senzory v libovolných pozicích (nejsou nuceně pravoúhlé). Spárujte A s každým z B, C, D a kalibrujte samostatně. Přeurčené řešení metodou nejmenších čtverců průměruje měřicí šum mezi páry a hlásí rezidua pro každý pár.

### 3D

Plné 3D měření se 4 senzory umístěnými v 3D prostoru. Zadejte souřadnice (X, Y, Z) každého senzoru a kalibrační časy a časy událostí pro každý pár (A–B, A–C, A–D).

### 3D+ (Pro)

Jako 3D, ale podporuje až **6 senzorů** (A až F) s přeurčeným LSQ. Maximální přesnost pro složité 3D geometrie.

---

## Záložka Materials {#the-materials-tab}

Knihovna běžných technických materiálů se známou rychlostí zvuku při 20 °C.

![Záložka Materials](../screenshots/05-materials-tab.png)

### Seznam materiálů

Seznam obsahuje vzduch, tekutiny, gumy, polymery, dřeva, skla a kovy. Rychlosti se pohybují od ~340 m/s (vzduch) do ~13 000 m/s (některé kovy při pokojové teplotě).

### Vestavěné materiály s teplotní kompenzací

14 běžně používaných kovů obsahuje data o teplotním koeficientu. Když se referenční teplota v Nastavení liší od 20 °C, aplikace automaticky upravuje rychlosti těchto materiálů:

- Hliník
- Ocel, Mild (1020)
- Nerezová ocel (304)
- Železo (litina)
- Železo
- Měď
- Mosaz
- Bronz
- Titan
- Hořčík
- Olovo
- Zinek
- Nikl
- Wolfram

Materiály s kompenzací zobrazují dvě hodnoty ve výběru: **kompenzovanou rychlost** (velkou, výraznou) a **referenční rychlost při 20 °C** (malou, šedou pod ní).

Materiály bez kompenzace zobrazují **„ref only"** kurzivou — jejich uvedená rychlost se používá tak, jak je, bez ohledu na teplotu.

### Vlastní materiály

Pokud změříte kalibraci na záložce 2-Sensor, můžete výsledek uložit jako vlastní materiál. Po úspěšném 2-sensor měření hledejte možnost uložit odvozenou rychlost pod jménem dle vašeho výběru.

Vlastní materiály ukládají rychlost změřenou in-situ; nikdy nepoužívají teplotní kompenzaci (rychlost už byla změřena při testovací teplotě).

### Oblíbené

Klepněte na hvězdičku vedle libovolného materiálu, abyste jej označili jako oblíbený. Oblíbené se zobrazují v horní části seznamu pro rychlý přístup.

### Vyhledávání

Použijte vyhledávací lištu nahoře pro filtrování materiálů podle názvu. Vyhledávání odpovídá jak anglickým kanonickým názvům, tak přeloženým zobrazovaným názvům.

---

## Teplotní kompenzace {#temperature-compensation}

Rychlost zvuku v materiálech se mění s teplotou. V automobilových NVH testech je to důležité: motorový prostor při 80 °C, zachlazená kabina při -10 °C nebo oblast výfukového potrubí při 200 °C se chovají odlišně od pokojových laboratorních podmínek.

### Nastavení teploty

Otevřete Nastavení (ikona ⚙) → Referenční teplota. Zadejte teplotu vašeho testovacího prostředí ve °C (rozsah -40 až +200).

![Panel Nastavení](../screenshots/06-settings.png)

### Co se stane, když teplota ≠ 20 °C

- Pole kalibračního času se automaticky vyplní teplotně upravenou rychlostí
- Výběr Materials prominentně zobrazuje upravenou rychlost
- Toast potvrzuje: *„Hliník aplikován (6 284 m/s @ 60 °C) — aktualizováno N párů"*
- Náznak „Nejbližší materiál" porovnává s teplotně upravenými rychlostmi
- Uložené záznamy historie zaznamenávají aktivní teplotu
- Reporty obsahují řádek zápatí: *„Referenční teplota: 60 °C, aplikována kompenzace"*

### Reset při startu aplikace

Referenční teplota **se vždy resetuje na 20 °C** při startu aplikace. To zabraňuje, aby zastaralá nastavení z minulé měřicí relace tiše ovlivňovala dnešní práci. Malá kurziva v Nastavení vám připomíná toto chování.

Pokud chcete přehrát historické měření při jeho původní teplotě, stačí klepnout na záznam — teplota se obnoví automaticky.

### Materiály bez kompenzace

Většina nekovových materiálů nemá spolehlivé publikované teplotní koeficienty. Aplikace pro ně zobrazuje odznak **„ref only"** — jejich uvedená rychlost se používá bez ohledu na nastavení teploty. Pokud potřebujete přesná měření při ne-pokojových teplotách pro tyto materiály, proveďte in-situ kalibraci a uložte výsledek jako vlastní materiál.

---

## Anotace fotografie {#photo-annotation}

Po úspěšném výpočtu klepněte na tlačítko **📷 Anotovat fotografii**, abyste překryli značky senzorů a zdroje na fotografii vaší sestavy.

![Anotace fotografie](../screenshots/08-photo-annotation.png)

### Postup

1. Klepněte na **Anotovat fotografii** — otevře se systémová kamera
2. Pořiďte fotografii umístění senzorů
3. Aplikace načte fotografii do překryvné anotace
4. Značky senzorů (A, B, C, D, E, F podle potřeby — až 6 senzorů) a značka zdroje se automaticky umístí na základě vašeho výpočtu
5. Přetáhněte libovolnou značku pro jemné nastavení polohy. Při úpravě se poloha zdroje přepočítává z opravených pozic senzorů
6. Klepněte na **Uložit** pro zachování nebo **Pořídit znovu** pro nový pokus

Anotovaná fotografie je automaticky zahrnuta do PDF reportů.

---

## Reporty {#reports}

Klepněte na tlačítko **Tisk výsledku** na libovolné obrazovce výsledku pro generování formátovaného reportu.

![PDF report](../screenshots/09-pdf-report.png)

### Obsah reportu

- Záhlaví (přizpůsobitelné v Nastavení → Záhlaví reportu)
- Název měření a časová značka
- Všechny vstupní hodnoty v přehledné tabulce
- Výsledek výpočtu
- Text závěru
- Vizualizace (geometrický graf)
- Anotovaná fotografie (pokud jste ji pořídili)
- Řádek zápatí s teplotou (pokud byla kompenzace aktivní)
- Číslo stránky a řádek se zaslouženými údaji

### Formát výstupu

- **Android**: nativní generování PDF, uložení do telefonu nebo sdílení
- **iOS**: systémový dialog tisku → uložit jako PDF, AirPrint nebo sdílet

### Přizpůsobení záhlaví

Nastavení → Záhlaví reportu. Zadejte název vaší společnosti, název laboratoře, info o projektu nebo cokoliv chcete v horní části každého reportu.

---

## Záloha a obnova {#backup-and-restore}

Uložte všechny své vlastní materiály, oblíbené, nastavení a historii do jednoho souboru. Přenos mezi zařízeními.

### Záloha

Nastavení → **Záloha** → klepněte na „Uložit záložní soubor". Aplikace vygeneruje JSON soubor a otevře sdílecí list vašeho telefonu. Uložte jej do svého cloudového úložiště (Google Drive, iCloud, OneDrive), pošlete si jej e-mailem nebo přeneste jakkoliv chcete.

### Obnova

Nastavení → **Obnova** → vyberte záložní soubor z úložiště vašeho telefonu. Aplikace importuje vlastní materiály, oblíbené, historii a nastavení.

⚠️ **Obnova nahradí vaše aktuální data.** Pokud máte na aktuálním zařízení důležitá měření, nejprve je zálohujte před obnovením z jiné zálohy.

---

## Nastavení {#settings}

Přístup přes ikonu ozubeného kola ⚙ v pravém horním rohu. Nastavení je modální, ne záložka.

![Nastavení](../screenshots/06-settings.png)

| Nastavení | Co řídí |
|---|---|
| **Upgrade na Pro** | Koupit nebo se dozvědět o funkcích Pro ($19,99) |
| **Jazyk** | Zobrazovací jazyk aplikace (podporováno 30) |
| **Téma** | Světlé, Tmavé nebo Auto (následovat systém) |
| **Jednotka vzdálenosti** | cm nebo palce |
| **Referenční teplota** | Aktivní teplota pro kompenzaci, -40 až +200 °C |
| **Záhlaví reportu** | Vlastní text v horní části generovaných reportů |
| **Záloha** | Exportovat všechna data do souboru |
| **Obnova** | Importovat data ze záložního souboru |
| **Obnovit nákup** | Znovu získat Pro na novém zařízení |

---

## Funkce Pro {#pro-features}

NVH Source Locator používá **freemium model se zámkem funkcí**:

- **Zdarma**: Záložka 2-Sensor je plně funkční bez omezení
- **Pro**: Všechny ostatní záložky mají konkrétní vstupní pole zamčená. Paywall se zobrazí, když uživatel s bezplatnou verzí klepne na zamčené pole

### Co je zamčené

Pole vyžadující Pro jsou rozptýlena v:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Režimy 3D a 3D+
- Záloha a Obnova
- PDF reporty
- Vlastní materiály
- Anotace fotografie

Uživatel s bezplatnou verzí může OTEVŘÍT libovolnou záložku a VIDĚT rozhraní. Prostě nemůže zadávat hodnoty do Pro-zamčených vstupních polí.

![Pro-zamčené pole](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Když uživatel s bezplatnou verzí klepne na zamčené pole, paywall vyjede a zobrazí:
- Ikonu aplikace s odznakem PRO
- Seznam funkcí
- Tlačítko odemčení s cenou ($19,99 výchozí; může se lišit podle regionu)
- Uplatnění promo kódu (pouze Android — iOS používá samostatný tok Offer Code od Apple)
- Volitelný promo odkaz na komunitní kanály

### Nákup Pro

Klepněte na libovolné zamčené pole nebo klepněte na **Upgrade na Pro** v Nastavení. Používá oficiální platební systém vaší platformy (Google Play na Androidu, Apple App Store na iOS).

### Obnovení Pro na novém zařízení

Pokud jste zakoupili na jednom zařízení a chcete Pro na jiném (stejný účet):

1. Přihlaste se ke **stejnému** účtu Google (Android) nebo Apple ID (iOS), které jste použili k nákupu
2. Otevřete NVH Source Locator na novém zařízení
3. Přejděte do Nastavení → **Obnovit nákup**
4. Aplikace ověří v záznamech nákupů platformy a odemkne Pro

### Automatická obnova při startu

Pokud uplatníte promo kód v Google Play Store nebo App Store, zatímco NVH Source Locator běží na pozadí, návrat do aplikace automaticky detekuje nový nákup a odemkne Pro — manuální obnova není potřeba.

### Uplatnění promo kódu

**Android**: tlačítko „Máte promo kód Google Play?" v paywall otevře tok uplatnění Google Play s vaším předvyplněným kódem.

**iOS**: Politika App Store 3.1.1 vyžaduje uplatnění prostřednictvím oficiálního toku „Uplatnit kód" od Apple. Tlačítko Google Play je v iOS skryté. Místo toho hledejte „Uplatnit kód App Store" v Nastavení.

---

## Záložka Help a návody {#help-tab-and-tutorials}

Záložka **Help** obsahuje návody v aplikaci, příručky nejlepších postupů a referenční informace.

![Záložka Help](../screenshots/10-help-tab.png)

Pokryté témata:
- Jaké vybavení potřebujete
- Jak umístit senzory pro nejlepší přesnost
- Tipy pro kalibraci
- Běžné měřicí scénáře
- Tipy pro triangulaci a 3D umístění
- Vedení kabelů a kvalita signálu

---

## Řešení problémů {#troubleshooting}

### Výsledek výpočtu je špatný nebo nedává smysl

1. Zkontrolujte kalibraci. Automaticky vyplněné `tCal` předpokládá publikovanou rychlost materiálu — skutečné materiály se liší. Nejpřesnější kalibrace je in-situ: klepněte na známé místo a nechte aplikaci odvodit skutečnou rychlost.
2. Zkontrolujte nastavení **První senzor** — který senzor událost slyšel jako první, je důležité pro matematiku.
3. Ověřte měření vzdálenosti. Chyby několika mm se šíří.

### Toast říká „Výsledek mimo rozsah"

Matematika říká, že zdroj není mezi vašimi senzory. Možné příčiny:
- Zdroj je skutečně mimo linii/rovinu senzorů
- Jeden z vašich vstupů je špatně
- Kalibrační rychlost je příliš daleko od reality

### Nápověda vypočtené rychlosti zobrazuje varovnou barvu

Implikovaná rychlost zvuku z vašich vstupů je daleko od jakéhokoliv běžného materiálu (méně než 50 m/s nebo více než 20 000 m/s). Zkontrolujte vstupy — pravděpodobně překlep v tCal nebo vzdálenosti.

### Výběr Materials zobrazuje jiné rychlosti než očekávané

Zkontrolujte referenční teplotu v Nastavení. Pokud není 20 °C, zobrazené rychlosti odrážejí teplotní kompenzaci. Aplikace zobrazuje „ref X @ 20°C" pod kompenzovanými rychlostmi, abyste mohli ověřit.

### Záznam historie se přehrává s jiným výsledkem

Staré záznamy historie vytvořené před verzí aplikace 1.75 nemusely uložit teplotu. Pokud jste provedli měření při ne-20 °C teplotě, přehrávání použije aktuální nastavení. Před přehráváním ručně nastavte teplotu v Nastavení NEBO znovu změřte.

### Značky anotace fotografie nejsou tam, kde očekávám

Značky se umisťují automaticky podle vstupní geometrie. Přetáhněte je pro úpravu. Úprava značek aktualizuje polohu zdroje v překryvu fotografie — ale NEMĚNÍ základní výsledek výpočtu.

### Záloha/Obnova selhává

Ujistěte se, že používáte záložní soubor generovaný stejnou nebo novější verzí aplikace. Starší záložní soubory nemusí mít aktuální datová pole.

### Obnovit nákup říká „nenalezen žádný nákup"

1. Ověřte, že jste přihlášeni ke stejnému účtu obchodu, který jste použili k nákupu
2. Ověřte, že nákup nebyl refundován nebo nevypršel
3. Zkuste aplikaci odinstalovat a přeinstalovat (nákup je vázán na váš účet obchodu, ne na instalaci aplikace)
4. Pokud problém přetrvává, kontaktujte support@evdiag.net

### Číselný vstup se neočekávaně mění na 0

Záměrně: když opustíte číselné pole (klepnete jinam) a je prázdné, záporné nebo obsahuje nečíselný text, přepne se na 0. Zabraňuje tichým rozbitým výpočtům z náhodně vymazaných vstupů. Vstup teploty je výjimkou (místo toho se omezí na -40/+200).

### Potřebuji další pomoc

Kontaktujte `support@evdiag.net` s:
- Modelem zařízení a verzí OS
- Verzí aplikace (Nastavení → spodek stránky)
- Popisem toho, co jste zkusili
- Snímky obrazovky, pokud možno

---

*NVH Source Locator je vyvíjen společností EVDiag. Navštivte https://evdiag.net pro aktualizace a zdroje.*
""",

'sk': """# NVH Source Locator — Používateľská príručka

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
""",

'hu': """# NVH Source Locator — Felhasználói kézikönyv

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

## Hogyan működik {#how-it-works}

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

## Mielőtt elkezdené {#before-you-start}

Szükséges lesz:

- **Egy oszcilloszkóp vagy mérőrendszer**, amely meg tudja mutatni az időkülönbséget gyorsulásmérő csatornák között mikroszekundumban (µs)
- **Legalább 2 gyorsulásmérő** fizikailag a szerkezethez rögzítve (több érzékelő = nagyobb pontosság)
- **Egy mód a távolság mérésére** az érzékelők között (mérőszalag, tolómérő)
- **Egy mód egy hullám kiváltására** egy ismert helyen kalibráláshoz (kalibrált kalapácsütés, csavarhúzó-ütés vagy más ismert jel)

![Kezdőképernyő 2-Sensor lappal](../screenshots/01-home-2sensor.png)

---

## A főbb lapok {#the-main-tabs}

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

## 2-Sensor mód {#2-sensor-mode}

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

## 3-Sensor mód {#3-sensor-mode}

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

## Pro+ módok {#pro-modes}

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

## A Materials lap {#the-materials-tab}

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

## Hőmérséklet-kompenzáció {#temperature-compensation}

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

## Fotóannotáció {#photo-annotation}

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

## Jelentések {#reports}

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

## Biztonsági mentés és visszaállítás {#backup-and-restore}

Mentse el az összes egyéni anyagát, kedvenceit, beállításait és előzményeit egyetlen fájlba. Eszközök közötti átvitel.

### Biztonsági mentés

Beállítások → **Biztonsági mentés** → koppintson a „Mentési fájl mentése" gombra. Az alkalmazás generál egy JSON fájlt és megnyitja a telefonja megosztási panelét. Mentse a felhőmeghajtójára (Google Drive, iCloud, OneDrive), küldje el magának e-mailben vagy adja át bármilyen módon.

### Visszaállítás

Beállítások → **Visszaállítás** → válassza ki a mentési fájlt a telefonja tárolójából. Az alkalmazás importálja az egyéni anyagokat, kedvenceket, előzményeket és beállításokat.

⚠️ **A visszaállítás felülírja a jelenlegi adatait.** Ha fontos mérései vannak a jelenlegi eszközön, először mentse el azokat, mielőtt visszaállítaná egy másik biztonsági mentésből.

---

## Beállítások {#settings}

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

## Pro funkciók {#pro-features}

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

## Help lap és oktatóanyagok {#help-tab-and-tutorials}

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

## Hibaelhárítás {#troubleshooting}

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
""",

'hr': """# NVH Source Locator — Korisnički priručnik

NVH Source Locator je mjerni alat za lociranje izvora buke i vibracija pomoću TDOA (Time Difference of Arrival) iz signala akcelerometra zabilježenih na osciloskopu ili mjernom sustavu.

Ovaj priručnik pokriva sve značajke. Za kratki podsjetnik pogledajte **Kratki priručnik**.

---

## Sadržaj

1. [Kako radi](#how-it-works)
2. [Prije nego što počnete](#before-you-start)
3. [Glavne kartice](#the-main-tabs)
4. [Način 2-Sensor](#2-sensor-mode)
5. [Način 3-Sensor](#3-sensor-mode)
6. [Načini Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Kartica Materials](#the-materials-tab)
8. [Temperaturna kompenzacija](#temperature-compensation)
9. [Označavanje fotografije](#photo-annotation)
10. [Izvješća](#reports)
11. [Sigurnosna kopija i vraćanje](#backup-and-restore)
12. [Postavke](#settings)
13. [Pro značajke](#pro-features)
14. [Kartica Help i tutorijali](#help-tab-and-tutorials)
15. [Rješavanje problema](#troubleshooting)

---

## Kako radi {#how-it-works}

Kad izvor buke emitira zvuk ili vibraciju, val putuje kroz materijal poznatom brzinom. Ako postavite dva ili više akcelerometara na materijal i izmjerite kada val stigne do svakog od njih, vremenska razlika vam govori gdje je izvor.

NVH Source Locator uzima:

- **Kalibraciju**: udaljenost između senzora i vrijeme potrebno da val prijeđe tu udaljenost (koristi se za izračun brzine zvuka materijala)
- **Događaj**: vremensku razliku između senzora koji detektiraju događaj buke/vibracije

Zatim izračunava gdje se izvor nalazi u strukturi.

Što više senzora koristite, to preciznije možete locirati izvor:

- **2 senzora** → udaljenost duž linije
- **3 senzora** → položaj na 2D površini (X, Y)
- **4 senzora** → položaj u 3D prostoru (X, Y, Z)

---

## Prije nego što počnete {#before-you-start}

Trebat će vam:

- **Osciloskop ili mjerni sustav** koji vam može pokazati vremensku razliku između kanala akcelerometra u mikrosekundama (µs)
- **Najmanje 2 akcelerometra** fizički pričvršćena na strukturu (više senzora = veća točnost)
- **Način mjerenja udaljenosti** između senzora (mjerna traka, šestar)
- **Način pokretanja vala** na poznatoj lokaciji za kalibraciju (kalibrirani udarac čekićem, udarac odvijačem ili drugi poznati signal)

![Početni zaslon s karticom 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Glavne kartice {#the-main-tabs}

Aplikacija ima kartice na vrhu:

![Traka kartica](../screenshots/02-tab-bar.png)

| Kartica | Što radi | Kada koristiti |
|---|---|---|
| **2-Sensor** | 1D lociranje izvora duž linije između 2 senzora | Brze provjere, strukture nalik gredama. **Potpuno besplatno.** |
| **3-Sensor** | 2D lociranje izvora pomoću 3 senzora u trokutu | Najopćenitija upotreba, ploče i površine |
| **3-Sen+** | 3-Sensor s preodređenim rješavačem najmanjih kvadrata | Zahtjevnija mjerenja, otporno na buku |
| **4-Sensor** | 2D lociranje pomoću dva para (A-B + C-D) | Pravokutni rasporedi senzora, unakrsna provjera |
| **4-Sen+** | Napredni 2D način, 4 senzora u bilo kojem položaju | Nepravokutne geometrije, puni LSQ |
| **3D** | 3D lociranje izvora pomoću 4 senzora s XYZ koordinatama | Složene strukture u 3D prostoru |
| **3D+** | 3D s do 6 senzora, preodređeni LSQ | Vrlo složene geometrije, maksimalna preciznost |
| **Materials** | Knjižnica brzine zvuka + prilagođeni materijali | Odaberite jednom po sesiji mjerenja |
| **Help** | Tutorijali u aplikaciji i referenca | Kada vam treba brzi podsjetnik |

> **Besplatno vs Pro**: Kartica 2-Sensor je potpuno besplatna. Druge kartice su dostupne, ali imaju određena polja za unos zaključana za Pro korisnike (označena zlatnom značkom lokota). Dodir zaključanog polja prikazuje Pro paywall.

Postavke su dostupne putem ikone zupčanika ⚙ u gornjem desnom kutu (nije kartica).

---

## Način 2-Sensor {#2-sensor-mode}

Najjednostavnije mjerenje: lociranje izvora duž linije između dva akcelerometra.

![Kartica 2-Sensor](../screenshots/01-home-2sensor.png)

### Korak 1: Primijenite materijal

Dodirnite karticu Materials. Odaberite materijal od kojeg je vaša struktura napravljena (npr. „Aluminij", „Čelik, Mild (1020)"). Aplikacija koristi poznatu brzinu zvuka materijala za automatsko popunjavanje polja vremena kalibracije.

Ako materijal vaše strukture nije na popisu, možete privremeno odabrati „Zrak" i ručno prepisati vrijeme kalibracije u koraku 2.

### Korak 2: Unesite podatke kalibracije

Na kartici 2-Sensor vidjet ćete dvije sekcije parova: **Par A–B** i **Par A–C** (potreban je samo A–B ako imate samo 2 senzora).

Za svaki par popunjavate:

- **Razmak senzora** (`d`): fizička udaljenost između senzora, u cm ili inčima (postavljeno u Postavkama)
- **Kašnjenje vremena kalibracije** (`tCal`): vrijeme potrebno valu da putuje između senzora pri brzini zvuka materijala — automatski popunjeno kada odaberete materijal, ali možete prepisati

### Korak 3: Unesite vrijeme događaja

- **Kašnjenje vremena događaja** (`tEvent`): vremenska razlika između senzora koji detektiraju događaj buke, u mikrosekundama
- **Prvi senzor**: koji senzor je prvi čuo događaj (A ili B)

### Korak 4: Pročitajte rezultat

Aplikacija prikazuje položaj izvora kao udaljenost od senzora A:
- Rezultat = 0: izvor je kod senzora A
- Rezultat = udaljenost: izvor je kod senzora B
- Rezultat između: izvor je između njih
- Rezultat izvana: izvor je iza jednog od senzora (toast će upozoriti)

Kartica rezultata prikazuje obje udaljenosti (od A, od B) i pokazuje koji senzor je bliži.

### Korak 5 (neobavezno): Označite fotografiju

Dodirnite **📷 Označi fotografiju** kako biste fotografirali svoju postavku. Aplikacija postavlja oznake za senzore A, B i izvor. Korisno za izvješća.

---

## Način 3-Sensor {#3-sensor-mode}

Locira izvor na 2D ravnini koristeći tri senzora raspoređena u trokut.

![Kartica 3-Sensor](../screenshots/03-3sensor-tab.png)

### Postavljanje

Postavite tri senzora na svoju strukturu tvoreći trokut. Jednakostranični, pravokutni ili raznostranični — aplikacija obrađuje sve geometrije.

### Unesite podatke

U sekciji **Duljine stranica trokuta** unesite fizičku udaljenost za sve tri stranice (A–B, A–C, B–C).

Za svaki par (A–B i A–C) unesite:
- **tCal**: vrijeme kalibracije (automatski se popunjava iz materijala)
- **tEvent**: izmjerena vremenska razlika za događaj buke
- **Prvi senzor**: koji je prvi čuo

### Pročitajte rezultat

Aplikacija prikazuje položaj izvora kao koordinate X, Y u odnosu na senzor A (senzor A u ishodištu, senzor B na X osi). Vizualizacija prikazuje sva tri senzora i lokaciju izvora.

![Rezultat trokuta](../screenshots/04-triangle-result.png)

---

## Pro+ načini {#pro-modes}

Nekoliko naprednih kartica nudi preodređene rješavače i veću dimenzionalnost:

### 3-Sen+ (Pro)

Ista postavka trokuta kao 3-Sensor, ali kalibrirajte I mjerite sva tri para (A–B, A–C, B–C). Rješavač koristi sva 3 TDOA u prilagodbi najmanjih kvadrata — robustnije na mjernu buku i anizotropne materijale. Reziduali po paru se prijavljuju kako biste mogli uočiti nedosljedna mjerenja.

### 4-Sensor

Postavite četiri senzora oko područja:
- **A–B** = horizontalni par (lijeve/desne strane)
- **C–D** = vertikalni par (gornja/donja strane)

Najprije pokrenite par A–B (horizontalni), zatim par C–D (vertikalni). 2D karta prikazuje sjecište. Svaki par se kalibrira odvojeno — korisno kada materijal varira preko strukture.

### 4-Sen+ (Napredni 2D)

Četiri senzora u bilo kojem položaju (nije forsirana pravokutnost). Uparite A sa svakim od B, C, D i kalibrirajte odvojeno. Preodređeni rješavač najmanjih kvadrata uprosječuje mjernu buku po paru i prijavljuje rezidualne vrijednosti po paru.

### 3D

Potpuno 3D mjerenje s 4 senzora smještena u 3D prostoru. Unesite koordinate (X, Y, Z) svakog senzora, plus vremena kalibracije i događaja za svaki par (A–B, A–C, A–D).

### 3D+ (Pro)

Kao 3D, ali podržava do **6 senzora** (A do F) s preodređenim LSQ. Maksimalna preciznost za složene 3D geometrije.

---

## Kartica Materials {#the-materials-tab}

Knjižnica uobičajenih inženjerskih materijala s poznatom brzinom zvuka na 20 °C.

![Kartica Materials](../screenshots/05-materials-tab.png)

### Popis materijala

Popis uključuje zrak, tekućine, gume, polimere, drvo, stakla i metale. Brzine se kreću od ~340 m/s (zrak) do ~13 000 m/s (neki metali na sobnoj temperaturi).

### Ugrađeni materijali s temperaturnom kompenzacijom

14 često korištenih metala uključuje podatke o temperaturnom koeficijentu. Kada se Referentna temperatura u Postavkama razlikuje od 20 °C, aplikacija automatski prilagođava brzine ovih materijala:

- Aluminij
- Čelik, Mild (1020)
- Nehrđajući čelik (304)
- Željezo (lijevano)
- Željezo
- Bakar
- Mjed
- Bronca
- Titan
- Magnezij
- Olovo
- Cink
- Nikal
- Volfram

Materijali s kompenzacijom prikazuju dvije vrijednosti u izborniku: **kompenziranu brzinu** (velika, istaknuta) i **referentnu brzinu na 20 °C** (mala, siva ispod).

Materijali bez kompenzacije prikazuju **„ref only"** kurzivom — njihova navedena brzina koristi se onakva kakva je, bez obzira na temperaturu.

### Prilagođeni materijali

Ako izmjerite kalibraciju na kartici 2-Sensor, možete spremiti rezultat kao prilagođeni materijal. Nakon uspješnog 2-sensor mjerenja, potražite opciju spremanja izvedene brzine pod imenom po vašem izboru.

Prilagođeni materijali pohranjuju in-situ izmjerenu brzinu; nikada ne primjenjuju temperaturnu kompenzaciju (brzina je već izmjerena pri temperaturi testa).

### Favoriti

Dodirnite zvjezdicu uz bilo koji materijal kako biste ga označili kao favorit. Favoriti se pojavljuju na vrhu popisa za brzi pristup.

### Pretraga

Koristite traku za pretraživanje na vrhu za filtriranje materijala prema imenu. Pretraga odgovara i engleskim kanonskim imenima i prevedenim prikaznim imenima.

---

## Temperaturna kompenzacija {#temperature-compensation}

Brzina zvuka u materijalima mijenja se s temperaturom. U automobilskom NVH testiranju to je važno: prostor motora na 80 °C, hlađena kabina na -10 °C ili područje ispušne grane na 200 °C svi se ponašaju drugačije od laboratorijskih uvjeta na sobnoj temperaturi.

### Postavljanje temperature

Otvorite Postavke (ikona ⚙) → Referentna temperatura. Unesite temperaturu svog testnog okruženja u °C (raspon -40 do +200).

![Panel Postavke](../screenshots/06-settings.png)

### Što se događa kada je temperatura ≠ 20 °C

- Polja vremena kalibracije automatski se popunjavaju brzinom prilagođenom temperaturi
- Izbornik Materials istaknuto prikazuje prilagođenu brzinu
- Toast potvrđuje: *„Aluminij primijenjen (6.284 m/s @ 60 °C) — ažurirano N par(ova)"*
- Savjet „Najbliži materijal" uspoređuje s brzinama prilagođenim temperaturi
- Spremljeni unosi povijesti bilježe aktivnu temperaturu
- Izvješća uključuju liniju podnožja: *„Referentna temperatura: 60 °C, primijenjena kompenzacija"*

### Resetiranje pri pokretanju aplikacije

Referentna temperatura **uvijek se resetira na 20 °C** kada pokrenete aplikaciju. To sprječava da zastarjele postavke iz prošle sesije mjerenja tiho utječu na današnji rad. Mala kurzivna napomena u Postavkama vas podsjeća na ovo ponašanje.

Ako želite reproducirati povijesno mjerenje na njegovoj originalnoj temperaturi, samo dodirnite unos — temperatura se automatski vraća.

### Materijali bez kompenzacije

Većina nemetalnih materijala nema pouzdane objavljene temperaturne koeficijente. Aplikacija za njih prikazuje značku **„ref only"** — njihova navedena brzina koristi se bez obzira na postavku temperature. Ako trebate točna mjerenja na ne-sobnim temperaturama za ove materijale, izvršite in-situ kalibraciju i spremite rezultat kao prilagođeni materijal.

---

## Označavanje fotografije {#photo-annotation}

Nakon uspješnog izračuna, dodirnite gumb **📷 Označi fotografiju** kako biste postavili oznake senzora i izvora na fotografiju svoje postavke.

![Označavanje fotografije](../screenshots/08-photo-annotation.png)

### Tijek

1. Dodirnite **Označi fotografiju** — otvara se sistemska kamera
2. Snimite fotografiju postavljanja senzora
3. Aplikacija učitava fotografiju u sloj označavanja
4. Oznake senzora (A, B, C, D, E, F prema potrebi — do 6 senzora) i oznaka izvora automatski se postavljaju na temelju vašeg izračuna
5. Povucite bilo koju oznaku za fino podešavanje položaja. Kako podešavate, položaj izvora se ponovno izračunava iz ispravljenih položaja senzora
6. Dodirnite **Spremi** za zadržavanje ili **Snimi ponovno** za novi pokušaj

Označena fotografija automatski se uključuje u PDF izvješća.

---

## Izvješća {#reports}

Dodirnite gumb **Ispiši rezultat** na bilo kojem zaslonu rezultata za generiranje formatiranog izvješća.

![PDF izvješće](../screenshots/09-pdf-report.png)

### Sadržaj izvješća

- Zaglavlje (prilagodljivo u Postavke → Zaglavlje izvješća)
- Naslov mjerenja i vremenska oznaka
- Sve ulazne vrijednosti u uredan tablici
- Rezultat izračuna
- Tekst zaključka
- Vizualizacija (geometrijski grafikon)
- Označena fotografija (ako ste je snimili)
- Linija podnožja s temperaturom (ako je kompenzacija bila aktivna)
- Broj stranice i linija zahvale

### Format izlaza

- **Android**: nativna generacija PDF-a, spremite na svoj telefon ili podijelite
- **iOS**: sistemski dijalog ispisa → spremite kao PDF, AirPrint ili podijelite

### Prilagodba zaglavlja

Postavke → Zaglavlje izvješća. Unesite ime svoje tvrtke, ime laboratorija, podatke projekta ili bilo što što želite na vrhu svakog izvješća.

---

## Sigurnosna kopija i vraćanje {#backup-and-restore}

Spremite sve svoje prilagođene materijale, favorite, postavke i povijest u jednu datoteku. Prijenos između uređaja.

### Sigurnosna kopija

Postavke → **Sigurnosna kopija** → dodirnite „Spremi datoteku sigurnosne kopije". Aplikacija generira JSON datoteku i otvara list za dijeljenje na vašem telefonu. Spremite je u svoj oblačni pogon (Google Drive, iCloud, OneDrive), pošaljite e-poštom sebi ili prenesite na bilo koji način.

### Vraćanje

Postavke → **Vraćanje** → odaberite datoteku sigurnosne kopije iz pohrane vašeg telefona. Aplikacija uvozi prilagođene materijale, favorite, povijest i postavke.

⚠️ **Vraćanje zamjenjuje vaše trenutne podatke.** Ako imate važna mjerenja na trenutnom uređaju, prvo ih sigurnosno kopirajte prije vraćanja iz druge sigurnosne kopije.

---

## Postavke {#settings}

Pristup putem ikone zupčanika ⚙ u gornjem desnom kutu. Postavke su modalni prozor, nisu kartica.

![Postavke](../screenshots/06-settings.png)

| Postavka | Što kontrolira |
|---|---|
| **Nadogradnja na Pro** | Kupite ili saznajte više o Pro značajkama ($19,99) |
| **Jezik** | Jezik prikaza aplikacije (podržano 30) |
| **Tema** | Svjetla, Tamna ili Auto (slijedi sustav) |
| **Mjerna jedinica udaljenosti** | cm ili inči |
| **Referentna temperatura** | Aktivna temperatura za kompenzaciju, -40 do +200 °C |
| **Zaglavlje izvješća** | Prilagođeni tekst na vrhu generiranih izvješća |
| **Sigurnosna kopija** | Izvoz svih podataka u datoteku |
| **Vraćanje** | Uvoz podataka iz datoteke sigurnosne kopije |
| **Vrati kupnju** | Ponovno preuzmite Pro na novom uređaju |

---

## Pro značajke {#pro-features}

NVH Source Locator koristi **freemium model s zaključanim značajkama**:

- **Besplatno**: Kartica 2-Sensor potpuno je funkcionalna bez ograničenja
- **Pro**: Sve druge kartice imaju određena polja za unos zaključana. Paywall se pojavljuje kada besplatni korisnik dodirne zaključano polje

### Što je zaključano

Polja koja zahtijevaju Pro raspoređena su u:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D i 3D+ načine
- Sigurnosnu kopiju i Vraćanje
- PDF izvješća
- Prilagođene materijale
- Označavanje fotografije

Besplatni korisnik može OTVORITI bilo koju karticu i VIDJETI sučelje. Jednostavno ne može unijeti vrijednosti u Pro-zaključana polja za unos.

![Pro-zaključano polje](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Kada besplatni korisnik dodirne zaključano polje, paywall klizi prikazujući:
- Ikonu aplikacije s PRO značkom
- Popis značajki
- Gumb za otključavanje s cijenom ($19,99 zadano; može varirati po regiji)
- Iskorištavanje promo koda (samo Android — iOS koristi Appleov zasebni proces Offer Code)
- Neobavezni promotivni link za kanale zajednice

### Kupnja Pro

Dodirnite bilo koje zaključano polje ili dodirnite **Nadogradnja na Pro** u Postavkama. Koristi službeni sustav plaćanja vaše platforme (Google Play na Androidu, Apple App Store na iOS).

### Vraćanje Pro na novom uređaju

Ako ste kupili na jednom uređaju i želite Pro na drugom (isti račun):

1. Prijavite se na **isti** Google račun (Android) ili Apple ID (iOS) koji ste koristili za kupnju
2. Otvorite NVH Source Locator na novom uređaju
3. Idite na Postavke → **Vrati kupnju**
4. Aplikacija provjerava zapise kupnji platforme i otključava Pro

### Automatsko vraćanje pri pokretanju

Ako iskoristite promo kod u Google Play Storeu ili App Storeu dok NVH Source Locator radi u pozadini, povratak u aplikaciju automatski detektira novu kupnju i otključava Pro — nije potrebno ručno Vraćanje.

### Iskorištavanje promo koda

**Android**: gumb „Imate Google Play promo kod?" u paywallu otvara Google Play proces iskorištavanja s vašim unaprijed popunjenim kodom.

**iOS**: Politika App Storea 3.1.1 zahtijeva iskorištavanje putem Appleovog službenog procesa „Iskoristi kod". Gumb Google Play sakriven je na iOS-u. Umjesto toga potražite „Iskoristi kod App Storea" u Postavkama.

---

## Kartica Help i tutorijali {#help-tab-and-tutorials}

Kartica **Help** uključuje tutorijale u aplikaciji, vodiče najboljih praksi i referentne informacije.

![Kartica Help](../screenshots/10-help-tab.png)

Pokrivene teme:
- Koju opremu trebate
- Kako postaviti senzore za najbolju točnost
- Savjeti za kalibraciju
- Uobičajeni scenariji mjerenja
- Savjeti za triangulaciju i 3D postavljanja
- Vođenje kabela i kvaliteta signala

---

## Rješavanje problema {#troubleshooting}

### Rezultat izračuna je pogrešan ili nema smisla

1. Provjerite kalibraciju. Automatski popunjen `tCal` pretpostavlja objavljenu brzinu materijala — stvarni materijali variraju. Najtočnija kalibracija je in-situ: dodirnite poznatu lokaciju i pustite aplikaciju da izvuče stvarnu brzinu.
2. Provjerite postavku **Prvi senzor** — koji senzor je prvi čuo događaj važno je za matematiku.
3. Provjerite svoja mjerenja udaljenosti. Pogreške od nekoliko mm se šire.

### Toast kaže „Rezultat izvan raspona"

Matematika kaže da izvor nije između vaših senzora. Mogući uzroci:
- Izvor je zapravo izvan linije/ravnine senzora
- Jedan od vaših ulaza je pogrešan
- Brzina kalibracije previše je daleko od stvarnosti

### Savjet za izračunatu brzinu prikazuje boju upozorenja

Implicirana brzina zvuka iz vaših ulaza daleko je od bilo kojeg uobičajenog materijala (manje od 50 m/s ili više od 20 000 m/s). Provjerite svoje ulaze — vjerojatno tipfeler u tCal ili udaljenosti.

### Izbornik Materials prikazuje različite brzine od očekivanih

Provjerite Referentnu temperaturu u Postavkama. Ako nije 20 °C, prikazane brzine odražavaju temperaturnu kompenzaciju. Aplikacija prikazuje „ref X @ 20°C" ispod kompenziranih brzina kako biste mogli provjeriti.

### Unos povijesti reproducira se s drugim rezultatom

Stari unosi povijesti stvoreni prije verzije aplikacije 1.75 možda nisu pohranili temperaturu. Ako ste izvršili mjerenje na ne-20 °C temperaturi, reprodukcija će koristiti trenutnu postavku. Ručno postavite temperaturu u Postavkama prije reprodukcije, ILI ponovno mjerite.

### Oznake označavanja fotografije nisu tamo gdje očekujem

Oznake se automatski postavljaju na temelju ulazne geometrije. Povucite ih za prilagodbu. Prilagodba oznaka ažurira položaj izvora u sloju fotografije — ali NE mijenja temeljni rezultat izračuna.

### Sigurnosna kopija/Vraćanje ne uspijeva

Provjerite koristite li datoteku sigurnosne kopije generiranu istom ili novijom verzijom aplikacije. Stariji backup datoteke možda nemaju trenutna polja podataka.

### Vraćanje kupnje kaže „nije pronađena kupnja"

1. Provjerite jeste li prijavljeni na isti račun trgovine koji ste koristili za kupnju
2. Provjerite da kupnja nije vraćena ili istekla
3. Pokušajte deinstalirati i ponovno instalirati aplikaciju (kupnja je vezana uz vaš račun trgovine, a ne uz instalaciju aplikacije)
4. Kontaktirajte support@evdiag.net ako problem traje

### Numerički unos neočekivano se postavlja na 0

Po dizajnu: kada izađete iz numeričkog polja (dodirnete drugdje), ako je prazno, negativno ili sadrži ne-numerički tekst, postavlja se na 0. Sprječava tiho slomljene izračune iz slučajno obrisanih unosa. Unos temperature je izuzet (umjesto toga ograničava se na -40/+200).

### Trebam više pomoći

Kontaktirajte `support@evdiag.net` s:
- Modelom uređaja i verzijom OS-a
- Verzijom aplikacije (Postavke → dno stranice)
- Opisom onoga što ste pokušali
- Snimkama zaslona ako je moguće

---

*NVH Source Locator razvija EVDiag. Posjetite https://evdiag.net za ažuriranja i resurse.*
""",

'bg': """# NVH Source Locator — Ръководство за потребителя

NVH Source Locator е измервателен инструмент за локализиране на източници на шум и вибрации с помощта на TDOA (Time Difference of Arrival) от сигнали на акселерометри, заснети на осцилоскоп или измервателна система.

Това ръководство обхваща всички функции. За кратко припомняне вижте **Кратко справочно ръководство**.

---

## Съдържание

1. [Как работи](#how-it-works)
2. [Преди да започнете](#before-you-start)
3. [Основни раздели](#the-main-tabs)
4. [Режим 2-Sensor](#2-sensor-mode)
5. [Режим 3-Sensor](#3-sensor-mode)
6. [Режими Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Раздел Materials](#the-materials-tab)
8. [Температурна компенсация](#temperature-compensation)
9. [Анотация на снимка](#photo-annotation)
10. [Отчети](#reports)
11. [Архивиране и възстановяване](#backup-and-restore)
12. [Настройки](#settings)
13. [Pro функции](#pro-features)
14. [Раздел Help и уроци](#help-tab-and-tutorials)
15. [Отстраняване на проблеми](#troubleshooting)

---

## Как работи {#how-it-works}

Когато източник на шум излъчва звук или вибрация, вълната се разпространява през материала с известна скорост. Ако поставите два или повече акселерометъра на материала и измерите кога вълната достига до всеки от тях, времевата разлика ви казва къде е източникът.

NVH Source Locator приема:

- **Калибриране**: разстоянието между сензорите и времето, необходимо на вълната да измине това разстояние (използва се за изчисляване на скоростта на звука на материала)
- **Събитие**: времевата разлика между сензорите, които откриват събитието на шум/вибрация

След това изчислява къде се намира източникът в структурата.

Колкото повече сензори използвате, толкова по-точно можете да локализирате източника:

- **2 сензора** → разстояние по линия
- **3 сензора** → позиция върху 2D повърхност (X, Y)
- **4 сензора** → позиция в 3D пространство (X, Y, Z)

---

## Преди да започнете {#before-you-start}

Ще ви трябва:

- **Осцилоскоп или измервателна система**, която може да ви покаже времевата разлика между каналите на акселерометъра в микросекунди (µs)
- **Поне 2 акселерометъра**, физически прикрепени към структурата (повече сензори = по-висока точност)
- **Начин за измерване на разстоянието** между сензорите (рулетка, шублери)
- **Начин за задействане на вълна** на известно място за калибриране (калибриран удар с чук, удар с отвертка или друг известен сигнал)

![Начален екран с раздел 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Основни раздели {#the-main-tabs}

Приложението има раздели в горната част:

![Лента с раздели](../screenshots/02-tab-bar.png)

| Раздел | Какво прави | Кога да използвате |
|---|---|---|
| **2-Sensor** | 1D локализиране на източник по линия между 2 сензора | Бързи проверки, структури тип греда. **Напълно безплатно.** |
| **3-Sensor** | 2D локализиране на източник с 3 сензора в триъгълник | Най-общо използване, панели и повърхности |
| **3-Sen+** | 3-Sensor с предопределен решател на най-малките квадрати | По-взискателни измервания, устойчив на шум |
| **4-Sensor** | 2D локализиране с две двойки (A-B + C-D) | Правоъгълни оформления на сензори, кръстосана проверка |
| **4-Sen+** | Разширен 2D режим, 4 сензора в произволни позиции | Неправоъгълни геометрии, пълен LSQ |
| **3D** | 3D локализиране на източник с 4 сензора с XYZ координати | Сложни структури в 3D пространство |
| **3D+** | 3D с до 6 сензора, предопределен LSQ | Много сложни геометрии, максимална точност |
| **Materials** | Библиотека на скоростта на звука + персонализирани материали | Изберете веднъж на сесия за измерване |
| **Help** | Уроци в приложението и справка | Когато имате нужда от бързо припомняне |

> **Безплатно vs Pro**: Разделът 2-Sensor е напълно безплатен. Други раздели са достъпни, но имат специфични полета за въвеждане, заключени за Pro потребители (отбелязани със златна значка катинар). Докосването на заключено поле показва Pro paywall.

Настройките се достъпват през иконата зъбно колело ⚙ в горния десен ъгъл (не е раздел).

---

## Режим 2-Sensor {#2-sensor-mode}

Най-простото измерване: локализиране на източник по линия между два акселерометъра.

![Раздел 2-Sensor](../screenshots/01-home-2sensor.png)

### Стъпка 1: Приложете материал

Докоснете раздела Materials. Изберете материала, от който е направена вашата структура (напр. „Алуминий", „Стомана, Mild (1020)"). Приложението използва известната скорост на звука на материала, за да попълни автоматично полето за време за калибриране.

Ако материалът на вашата структура не е в списъка, можете временно да изберете „Въздух" и ръчно да замените времето за калибриране в стъпка 2.

### Стъпка 2: Въведете данни за калибриране

В раздела 2-Sensor ще видите две секции с двойки: **Двойка A–B** и **Двойка A–C** (изисква се само A–B, ако имате само 2 сензора).

За всяка двойка попълвате:

- **Разстояние между сензорите** (`d`): физическо разстояние между сензорите, в см или инчове (зададено в Настройките)
- **Закъснение на времето за калибриране** (`tCal`): времето, за което вълната пътува между сензорите при скоростта на звука на материала — автоматично се попълва, когато изберете материал, но можете да замените

### Стъпка 3: Въведете времето на събитието

- **Закъснение на времето на събитието** (`tEvent`): времева разлика между сензорите, които откриват събитието на шум, в микросекунди
- **Първи сензор**: кой сензор е чул събитието първи (A или B)

### Стъпка 4: Прочетете резултата

Приложението показва позицията на източника като разстояние от сензор A:
- Резултат = 0: източникът е при сензор A
- Резултат = разстояние: източникът е при сензор B
- Резултат между: източникът е между тях
- Резултат отвън: източникът е извън един от сензорите (toast ще предупреди)

Картата с резултата показва и двете разстояния (от A, от B) и показва кой сензор е по-близо.

### Стъпка 5 (по избор): Анотиране на снимка

Докоснете **📷 Анотирай снимка**, за да направите снимка на вашата настройка. Приложението наслагва маркери за сензорите A, B и източника. Полезно за отчети.

---

## Режим 3-Sensor {#3-sensor-mode}

Локализира източник на 2D равнина с помощта на три сензора, подредени в триъгълник.

![Раздел 3-Sensor](../screenshots/03-3sensor-tab.png)

### Настройка

Поставете три сензора на вашата структура, образуващи триъгълник. Равностранен, правоъгълен или разностранен — приложението обработва всички геометрии.

### Въведете данните

В секцията **Дължини на страните на триъгълника** въведете физическото разстояние за всичките три страни (A–B, A–C, B–C).

За всяка двойка (A–B и A–C) въведете:
- **tCal**: време за калибриране (автоматично попълвано от материала)
- **tEvent**: измерена времева разлика за събитието на шум
- **Първи сензор**: кой го е чул първи

### Прочетете резултата

Приложението показва позицията на източника като координати X, Y относно сензор A (сензор A в началото, сензор B на оста X). Визуализацията показва всичките три сензора и местоположението на източника.

![Резултат от триъгълник](../screenshots/04-triangle-result.png)

---

## Режими Pro+ {#pro-modes}

Няколко напреднали раздела предлагат предопределени решатели и по-висока размерност:

### 3-Sen+ (Pro)

Същата настройка на триъгълник като 3-Sensor, но калибрирайте И измервайте всичките три двойки (A–B, A–C, B–C). Решателят използва всичките 3 TDOA в напасване на най-малките квадрати — по-устойчиво на шум при измерване и анизотропни материали. Остатъците за всяка двойка се отчитат, така че можете да забележите несъвместими измервания.

### 4-Sensor

Поставете четири сензора около областта:
- **A–B** = хоризонтална двойка (леви/десни страни)
- **C–D** = вертикална двойка (горни/долни страни)

Първо стартирайте двойката A–B (хоризонтална), след това двойката C–D (вертикална). 2D картата показва пресечната точка. Всяка двойка се калибрира поотделно — полезно, когато материалът варира в структурата.

### 4-Sen+ (Разширен 2D)

Четири сензора в произволни позиции (не принудени правоъгълни). Сдвоете A с всеки от B, C, D и калибрирайте поотделно. Предопределеният решател на най-малките квадрати осреднява шума на измерванията за всяка двойка и отчита остатъци за всяка двойка.

### 3D

Пълно 3D измерване с 4 сензора, поставени в 3D пространство. Въведете координатите (X, Y, Z) на всеки сензор, плюс времена за калибриране и събитие за всяка двойка (A–B, A–C, A–D).

### 3D+ (Pro)

Като 3D, но поддържа до **6 сензора** (от A до F) с предопределен LSQ. Максимална точност за сложни 3D геометрии.

---

## Раздел Materials {#the-materials-tab}

Библиотека с общи инженерни материали с известна скорост на звука при 20 °C.

![Раздел Materials](../screenshots/05-materials-tab.png)

### Списък с материали

Списъкът включва въздух, флуиди, гуми, полимери, дървесини, стъкла и метали. Скоростите варират от ~340 m/s (въздух) до ~13 000 m/s (някои метали при стайна температура).

### Вградени материали с температурна компенсация

14 често използвани метала включват данни за температурен коефициент. Когато Референтната температура в Настройките се различава от 20 °C, приложението автоматично коригира скоростите на тези материали:

- Алуминий
- Стомана, Mild (1020)
- Неръждаема стомана (304)
- Желязо (чугун)
- Желязо
- Мед
- Месинг
- Бронз
- Титан
- Магнезий
- Олово
- Цинк
- Никел
- Волфрам

Материалите с компенсация показват две стойности в селектора: **компенсираната скорост** (голяма, изпъкваща) и **референтната скорост при 20 °C** (малка, сива под нея).

Материалите без компенсация показват **„ref only"** в курсив — посочената им скорост се използва така, както е, независимо от температурата.

### Персонализирани материали

Ако измерите калибриране в раздела 2-Sensor, можете да запазите резултата като персонализиран материал. След успешно 2-sensor измерване, потърсете опцията да запазите производната скорост под име по ваш избор.

Персонализираните материали съхраняват скоростта, измерена in-situ; те никога не прилагат температурна компенсация (скоростта вече е била измерена при температурата на теста).

### Любими

Докоснете звездата до всеки материал, за да го маркирате като любим. Любимите се появяват в горната част на списъка за бърз достъп.

### Търсене

Използвайте лентата за търсене в горната част, за да филтрирате материали по име. Търсенето съответства както на английските канонични имена, така и на преведените показателни имена.

---

## Температурна компенсация {#temperature-compensation}

Скоростта на звука в материалите се променя с температурата. В автомобилните NVH тестове това е важно: моторно отделение при 80 °C, охладен салон при -10 °C или зона на изпускателен колектор при 200 °C се държат различно от лабораторни условия при стайна температура.

### Настройване на температурата

Отворете Настройки (икона ⚙) → Референтна температура. Въведете температурата на тестовата ви среда в °C (диапазон -40 до +200).

![Панел Настройки](../screenshots/06-settings.png)

### Какво се случва, когато температурата ≠ 20 °C

- Полетата за време за калибриране се попълват автоматично с коригираната по температура скорост
- Селекторът Materials показва изпъкващо коригираната скорост
- Toast потвърждава: *„Алуминий приложен (6 284 m/s @ 60 °C) — актуализирани N двойка(и)"*
- Подсказката „Най-близкият материал" сравнява с коригираните по температура скорости
- Записите в запазената история записват активната температура
- Отчетите включват ред в долен колонтитул: *„Референтна температура: 60 °C, приложена компенсация"*

### Нулиране при стартиране на приложението

Референтната температура **винаги се нулира до 20 °C**, когато стартирате приложението. Това предотвратява стари настройки от предишна сесия за измерване тихо да повлияят на днешната работа. Малка курсивна бележка в Настройките ви напомня за това поведение.

Ако искате да възпроизведете историческо измерване при оригиналната му температура, просто докоснете записа — температурата се възстановява автоматично.

### Материали без компенсация

Повечето неметални материали нямат надеждни публикувани температурни коефициенти. Приложението показва значка **„ref only"** за тях — посочената им скорост се използва независимо от настройката на температурата. Ако имате нужда от точни измервания при не-стайни температури за тези материали, извършете in-situ калибриране и запазете резултата като персонализиран материал.

---

## Анотация на снимка {#photo-annotation}

След успешно изчисление докоснете бутона **📷 Анотирай снимка**, за да наслагате маркери на сензори и източник върху снимка на вашата настройка.

![Анотация на снимка](../screenshots/08-photo-annotation.png)

### Процес

1. Докоснете **Анотирай снимка** — отваря се системната камера
2. Направете снимка на разположението на сензорите ви
3. Приложението зарежда снимката в наслагването на анотации
4. Маркерите на сензорите (A, B, C, D, E, F според приложимото — до 6 сензора) и маркерът на източника се поставят автоматично въз основа на вашето изчисление
5. Плъзнете който и да е маркер за фино настройване на позицията. Докато настройвате, позицията на източника се преизчислява от коригираните позиции на сензорите
6. Докоснете **Запази** за запазване или **Снимай отново** за нов опит

Анотираната снимка автоматично се включва в PDF отчетите.

---

## Отчети {#reports}

Докоснете бутона **Печат на резултата** на всеки екран с резултати, за да генерирате форматиран отчет.

![PDF отчет](../screenshots/09-pdf-report.png)

### Съдържание на отчета

- Горен колонтитул (персонализируем в Настройки → Горен колонтитул на отчета)
- Заглавие на измерването и времеви печат
- Всички входни стойности в спретната таблица
- Резултат от изчислението
- Текст на заключение
- Визуализация (геометрична графика)
- Анотирана снимка (ако сте направили такава)
- Ред в долен колонтитул с температура (ако компенсацията е била активна)
- Номер на страница и ред за благодарности

### Изходен формат

- **Android**: генериране на нативен PDF, запазване на телефона ви или споделяне
- **iOS**: системен диалог за печат → запазване като PDF, AirPrint или споделяне

### Персонализиране на горния колонтитул

Настройки → Горен колонтитул на отчета. Въведете името на вашата фирма, името на лабораторията, информация за проекта или каквото искате в горната част на всеки отчет.

---

## Архивиране и възстановяване {#backup-and-restore}

Запазете всички ваши персонализирани материали, любими, настройки и история в един файл. Прехвърляне между устройства.

### Архивиране

Настройки → **Архивиране** → докоснете „Запази архивен файл". Приложението генерира JSON файл и отваря менюто за споделяне на телефона ви. Запазете го в облачното си хранилище (Google Drive, iCloud, OneDrive), изпратете си го по имейл или прехвърлете по какъвто и да е начин.

### Възстановяване

Настройки → **Възстановяване** → изберете архивния файл от хранилището на телефона ви. Приложението импортира персонализирани материали, любими, история и настройки.

⚠️ **Възстановяването замества текущите ви данни.** Ако имате важни измервания на текущото устройство, първо ги архивирайте, преди да възстановявате от различен архив.

---

## Настройки {#settings}

Достъп през иконата зъбно колело ⚙ в горния десен ъгъл. Настройките са модални, не са раздел.

![Настройки](../screenshots/06-settings.png)

| Настройка | Какво контролира |
|---|---|
| **Надстройка до Pro** | Купете или научете за Pro функциите ($19,99) |
| **Език** | Език на показване на приложението (поддържат се 30) |
| **Тема** | Светла, Тъмна или Автоматична (следване на системата) |
| **Единица за разстояние** | см или инчове |
| **Референтна температура** | Активна температура за компенсация, -40 до +200 °C |
| **Горен колонтитул на отчета** | Персонализиран текст в горната част на генерирани отчети |
| **Архивиране** | Експорт на всички данни във файл |
| **Възстановяване** | Импорт на данни от архивен файл |
| **Възстанови покупка** | Повторно придобиване на Pro на ново устройство |

---

## Pro функции {#pro-features}

NVH Source Locator използва **freemium модел с заключени функции**:

- **Безплатно**: Разделът 2-Sensor е напълно функционален без ограничения
- **Pro**: Всички други раздели имат специфични полета за въвеждане заключени. Paywall се появява, когато безплатен потребител докосне заключено поле

### Какво е заключено

Полетата, изискващи Pro, са разпръснати в:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D и 3D+ режими
- Архивиране и Възстановяване
- PDF отчети
- Персонализирани материали
- Анотация на снимка

Безплатен потребител може да ОТВОРИ всеки раздел и да ВИДИ интерфейса. Просто не може да въвежда стойности в Pro-заключените полета за въвеждане.

![Pro-заключено поле](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Когато безплатен потребител докосне заключено поле, paywall се плъзга, показвайки:
- Икона на приложението с PRO значка
- Списък с функции
- Бутон за отключване с цена ($19,99 по подразбиране; може да варира по регион)
- Активиране на промо код (само Android — iOS използва отделния процес Offer Code на Apple)
- Незадължителен промо линк към канали на общността

### Покупка на Pro

Докоснете всяко заключено поле или докоснете **Надстройка до Pro** в Настройките. Използва официалната платежна система на вашата платформа (Google Play на Android, Apple App Store на iOS).

### Възстановяване на Pro на ново устройство

Ако сте закупили на едно устройство и искате Pro на друго (същият акаунт):

1. Влезте в **същия** Google акаунт (Android) или Apple ID (iOS), който сте използвали за покупката
2. Отворете NVH Source Locator на новото устройство
3. Отидете в Настройки → **Възстанови покупка**
4. Приложението проверява с записите за покупки на платформата и отключва Pro

### Автоматично възстановяване при стартиране

Ако активирате промо код в Google Play Store или App Store, докато NVH Source Locator работи във фонов режим, връщането към приложението автоматично открива новата покупка и отключва Pro — не е необходимо ръчно Възстановяване.

### Активиране на промо код

**Android**: бутон „Имате ли промо код за Google Play?" в paywall отваря процеса за активиране на Google Play с предварително попълнен код.

**iOS**: Политиката на App Store 3.1.1 изисква активиране през официалния процес „Активирай код" на Apple. Бутонът Google Play е скрит на iOS. Вместо това потърсете „Активирай код за App Store" в Настройките.

---

## Раздел Help и уроци {#help-tab-and-tutorials}

Разделът **Help** включва уроци в приложението, ръководства за най-добри практики и справочна информация.

![Раздел Help](../screenshots/10-help-tab.png)

Покрити теми:
- Какво оборудване ви е необходимо
- Как да позиционирате сензорите за най-добра точност
- Съвети за калибриране
- Често срещани сценарии за измерване
- Съвети за триангулация и 3D позициониране
- Поставяне на кабели и качество на сигнала

---

## Отстраняване на проблеми {#troubleshooting}

### Резултатът от изчислението е грешен или няма смисъл

1. Проверете калибрирането. Автоматично попълненото `tCal` приема публикуваната скорост на материала — реалните материали варират. Най-точното калибриране е in-situ: докоснете известно място и оставете приложението да изведе действителната скорост.
2. Проверете настройката на **Първи сензор** — кой сензор е чул събитието първи, има значение за математиката.
3. Проверете измерванията си на разстояние. Грешки от няколко мм се разпространяват.

### Toast казва „Резултат извън диапазона"

Математиката казва, че източникът не е между вашите сензори. Възможни причини:
- Източникът всъщност е извън линията/равнината на сензорите
- Един от вашите входове е грешен
- Скоростта на калибриране е твърде далеч от реалността

### Подсказката за изчислителна скорост показва предупредителен цвят

Имплицираната скорост на звука от вашите входове е далеч от всеки общ материал (по-малко от 50 m/s или повече от 20 000 m/s). Проверете входовете си — вероятно правописна грешка в tCal или разстояние.

### Селекторът Materials показва различни скорости от очакваните

Проверете Референтната температура в Настройките. Ако не е 20 °C, показаните скорости отразяват температурната компенсация. Приложението показва „ref X @ 20°C" под компенсираните скорости, така че можете да проверите.

### Запис от историята се възпроизвежда с различен резултат

Стари записи от историята, създадени преди версия 1.75 на приложението, може да не са съхранили температурата. Ако сте направили измерване при не-20 °C температура, възпроизвеждането ще използва текущата настройка. Ръчно задайте температурата в Настройките преди възпроизвеждане ИЛИ измерете отново.

### Маркерите за анотация на снимка не са там, където очаквам

Маркерите се поставят автоматично въз основа на входната геометрия. Плъзнете ги, за да коригирате. Коригирането на маркери актуализира позицията на източника в наслагването на снимката — но НЕ променя основния резултат от изчислението.

### Архивирането/Възстановяването се проваля

Уверете се, че използвате архивен файл, генериран от същата или по-нова версия на приложението. По-старите архивни файлове може да нямат текущите полета с данни.

### Възстанови покупка казва „не е намерена покупка"

1. Проверете, че сте влезли в същия акаунт на магазина, който сте използвали за покупката
2. Проверете, че покупката не е била възстановена или не е изтекла
3. Опитайте да деинсталирате и преинсталирате приложението (покупката е свързана с вашия акаунт в магазина, не с инсталирането на приложението)
4. Свържете се с support@evdiag.net, ако проблемът продължи

### Числовият вход неочаквано се променя на 0

По дизайн: когато напуснете числово поле (докоснете другаде), ако е празно, отрицателно или съдържа нечислов текст, то се променя на 0. Предотвратява тихо счупени изчисления от случайно изчистени входове. Входът за температура е освободен (вместо това се ограничава до -40/+200).

### Нуждая се от повече помощ

Свържете се със `support@evdiag.net` с:
- Модел на устройството и версия на ОС
- Версия на приложението (Настройки → дъното на страницата)
- Описание на това, което сте опитали
- Екранни снимки, ако е възможно

---

*NVH Source Locator се разработва от EVDiag. Посетете https://evdiag.net за актуализации и ресурси.*
""",

}
