# NVH Source Locator — Uživatelská příručka

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
