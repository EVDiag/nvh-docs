# NVH Source Locator — Användarhandbok

NVH Source Locator är ett mätverktyg för att lokalisera buller- och vibrationskällor med hjälp av TDOA (Time Difference of Arrival) från accelerometersignaler som registreras på ett oscilloskop eller mätsystem.

Den här handboken täcker alla funktioner. För en snabb påminnelse, se `quick-reference.md`.

> **Anmärkning om skärmdumpar**: Detta dokument använder platshållarskärmdumpar från appen. Ersätt varje `../screenshots/*.png` med riktiga enhetsskärmdumpar när du tar dem.

---

## Innehållsförteckning

1. [Hur det fungerar](#how-it-works)
2. [Innan du börjar](#before-you-start)
3. [De viktigaste flikarna](#the-main-tabs)
4. [2-Sensor-läge](#2-sensor-mode)
5. [3-Sensor-läge](#3-sensor-mode)
6. [Pro+-lägen (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Fliken Materials](#the-materials-tab)
8. [Temperaturkompensation](#temperature-compensation)
9. [Fotoannotering](#photo-annotation)
10. [Rapporter](#reports)
11. [Säkerhetskopiering och återställning](#backup-and-restore)
12. [Inställningar](#settings)
13. [Pro-funktioner](#pro-features)
14. [Fliken Help och handledningar](#help-tab-and-tutorials)
15. [Felsökning](#troubleshooting)

---

## Hur det fungerar

När en bullerkälla avger ljud eller vibration färdas vågen genom ett material med en känd hastighet. Om du placerar två eller fler accelerometrar på materialet och mäter när vågen anländer till var och en, säger tidsskillnaden var källan finns.

NVH Source Locator tar:

- **Kalibrering**: avståndet mellan sensorerna och tiden det tar för en våg att färdas det avståndet (används för att beräkna materialets ljudhastighet)
- **Händelse**: tidsskillnaden mellan sensorer som upptäcker buller-/vibrationshändelsen

Sedan beräknar det var på strukturen källan är belägen.

Ju fler sensorer du använder, desto mer exakt kan du fastställa källan:

- **2 sensorer** → avstånd längs en linje
- **3 sensorer** → position på en 2D-yta (X, Y)
- **4 sensorer** → position i 3D-rymd (X, Y, Z)

---

## Innan du börjar

Du behöver:

- **Ett oscilloskop eller mätsystem** som kan visa tidsskillnaden mellan accelerometerkanaler i mikrosekunder (µs)
- **Minst 2 accelerometrar** fysiskt fästa till strukturen (fler sensorer = högre noggrannhet)
- **Ett sätt att mäta avstånd** mellan sensorer (måttband, skjutmått)
- **Ett sätt att utlösa en våg** på en känd plats för kalibrering (kalibrerat hammarslag, skruvmejselslag eller annan känd signal)

![Hemskärm med fliken 2-Sensor](../screenshots/01-home-2sensor.png)

---

## De viktigaste flikarna

Appen har flikar längst upp:

![Flikrad](../screenshots/02-tab-bar.png)

| Flik | Vad den gör | När ska användas |
|---|---|---|
| **2-Sensor** | 1D-källokalisering längs en linje mellan 2 sensorer | Snabbkontroller, balkliknande strukturer. **Helt gratis.** |
| **3-Sensor** | 2D-källokalisering med 3 sensorer i en triangel | Mest allmänt bruk, paneler och ytor |
| **3-Sen+** | 3-Sensor med överbestämd minstakvadratlösare | Mer krävande mätningar, brusrobust |
| **4-Sensor** | 2D-lokalisering med två par (A-B + C-D) | Rektangulära sensorlayouter, korskontroll |
| **4-Sen+** | Avancerat 2D-läge, 4 sensorer i valfria positioner | Icke-rektangulära geometrier, fullständig LSQ |
| **3D** | 3D-källokalisering med 4 sensorer med XYZ-koordinater | Komplexa strukturer i 3D-rymd |
| **3D+** | 3D med upp till 6 sensorer, överbestämd LSQ | Mycket komplexa geometrier, maximal precision |
| **Materials** | Ljudhastighetsbibliotek + anpassade material | Välj en gång per mätsession |
| **Help** | Handledningar i appen och referens | När du behöver en snabb påminnelse |

> **Gratis vs Pro**: Fliken 2-Sensor är helt gratis. Andra flikar är tillgängliga men har specifika inmatningsfält låsta för Pro-användare (markerade med en guldhänglåsmärkning). Att trycka på ett låst fält visar Pro-paywallen.

Inställningar nås via ⚙ kugghjulsikonen i det övre högra hörnet (inte en flik).

---

## 2-Sensor-läge

Den enklaste mätningen: källokalisering längs en linje mellan två accelerometrar.

![2-Sensor-fliken](../screenshots/01-home-2sensor.png)

### Steg 1: Tillämpa ett material

Tryck på Materials-fliken. Välj materialet som din struktur är gjord av (t.ex. "Aluminium", "Stål, Mild (1020)"). Appen använder materialets kända ljudhastighet för att automatiskt fylla i kalibreringstidsfältet.

Om din strukturs material inte finns med på listan kan du tillfälligt välja "Luft" och åsidosätta kalibreringstiden manuellt i steg 2.

### Steg 2: Ange kalibreringsdata

På 2-Sensor-fliken ser du två parsektioner: **Par A–B** och **Par A–C** (endast A–B krävs om du bara har 2 sensorer).

För varje par fyller du i:

- **Sensoravstånd** (`d`): fysiskt avstånd mellan sensorer, i cm eller tum (ställs in i Inställningar)
- **Kalibreringstidfördröjning** (`tCal`): tid för en våg att färdas mellan sensorerna vid materialets ljudhastighet — fylls i automatiskt när du väljer ett material, men du kan åsidosätta

### Steg 3: Ange händelsetiden

- **Händelsetidsfördröjning** (`tEvent`): tidsskillnad mellan sensorer som upptäcker bullerhändelsen, i mikrosekunder
- **Första sensor**: vilken sensor som hörde händelsen först (A eller B)

### Steg 4: Läs resultatet

Appen visar källpositionen som ett avstånd från sensor A:
- Resultat = 0: källan är vid sensor A
- Resultat = avstånd: källan är vid sensor B
- Resultat däremellan: källan är mellan dem
- Resultat utanför: källan är bortom en av sensorerna (toast varnar)

Resultatkortet visar båda avstånden (från A, från B) och anger vilken sensor som är närmare.

### Steg 5 (valfritt): Annotera ett foto

Tryck på **📷 Annotera foto** för att ta ett foto av din inställning. Appen lägger till markörer för sensorer A, B och källan. Användbart för rapporter.

---

## 3-Sensor-läge

Lokaliserar en källa på ett 2D-plan med tre sensorer arrangerade i en triangel.

![3-Sensor-fliken](../screenshots/03-3sensor-tab.png)

### Inställning

Placera tre sensorer på din struktur som bildar en triangel. Liksidig, rätvinklig eller oliksidig — appen hanterar alla geometrier.

### Ange data

I sektionen **Triangelsidlängder**, ange det fysiska avståndet för alla tre sidor (A–B, A–C, B–C).

För varje par (A–B och A–C), ange:
- **tCal**: kalibreringstid (autofylls från materialet)
- **tEvent**: uppmätt tidsskillnad för bullerhändelsen
- **Första sensor**: vilken som hörde den först

### Läs resultatet

Appen visar källpositionen som X-, Y-koordinater i förhållande till sensor A (sensor A vid origo, sensor B på X-axeln). Visualiseringen visar alla tre sensorerna och källans plats.

![Triangelresultat](../screenshots/04-triangle-result.png)

---

## Pro+-lägen

Flera avancerade flikar erbjuder överbestämda lösare och högre dimensionalitet:

### 3-Sen+ (Pro)

Samma triangelinställning som 3-Sensor, men kalibrera OCH mät alla tre par (A–B, A–C, B–C). Lösaren använder alla 3 TDOA i en minstakvadratanpassning — mer robust mot mätbrus och anisotropa material. Restvärden per par rapporteras så att du kan upptäcka inkonsekventa mätningar.

### 4-Sensor

Placera fyra sensorer runt området:
- **A–B** = horisontalt par (vänster/höger sida)
- **C–D** = vertikalt par (övre/nedre sida)

Kör A–B-paret först (horisontalt), sedan C–D-paret (vertikalt). 2D-kartan visar skärningen. Varje par kalibreras separat — användbart när material varierar över strukturen.

### 4-Sen+ (Avancerat 2D)

Fyra sensorer i valfria positioner (inte tvingade rektangulära). Para A med var och en av B, C, D och kalibrera separat. Den överbestämda minstakvadratlösaren medelvärdesbildar mätbrus per par och rapporterar restvärden per par.

### 3D

Fullständig 3D-mätning med 4 sensorer placerade i 3D-rymd. Ange varje sensors (X, Y, Z) koordinater, plus kalibrerings- och händelsetider för varje par (A–B, A–C, A–D).

### 3D+ (Pro)

Som 3D men stödjer upp till **6 sensorer** (A till F) med överbestämd LSQ. Maximal precision för komplexa 3D-geometrier.

---

## Fliken Materials

Bibliotek med vanliga ingenjörsmaterial med känd ljudhastighet vid 20 °C.

![Materials-fliken](../screenshots/05-materials-tab.png)

### Materiallista

Listan innehåller luft, vätskor, gummi, polymerer, trä, glas och metaller. Hastigheter varierar från ~340 m/s (luft) till ~13 000 m/s (vissa metaller vid rumstemperatur).

### Inbyggda material med temperaturkompensation

14 vanligt använda metaller inkluderar temperaturkoefficientdata. När referenstemperaturen i Inställningar skiljer sig från 20 °C justerar appen automatiskt dessa materials hastigheter:

- Aluminium
- Stål, Mild (1020)
- Rostfritt Stål (304)
- Järn (gjutet)
- Järn
- Koppar
- Mässing
- Brons
- Titan
- Magnesium
- Bly
- Zink
- Nickel
- Volfram

Material med kompensation visar två värden i väljaren: **kompenserad hastighet** (stor, framträdande) och **referenshastighet vid 20 °C** (liten, grå under).

Material utan kompensation visar **"ref only"** i kursiv — deras listade hastighet används som den är oavsett temperatur.

### Anpassade material

Om du mäter en kalibrering på 2-Sensor-fliken kan du spara resultatet som ett anpassat material. Efter en lyckad 2-sensor-mätning, leta efter alternativet att spara den härledda hastigheten under ett namn du väljer.

Anpassade material lagrar den in-situ uppmätta hastigheten; de tillämpar aldrig temperaturkompensation (hastigheten mättes redan vid testtemperaturen).

### Favoriter

Tryck på stjärnan bredvid något material för att markera det som favorit. Favoriter visas högst upp i listan för snabb åtkomst.

### Sökning

Använd sökfältet längst upp för att filtrera material efter namn. Sökning matchar både engelska kanoniska namn och översatta visningsnamn.

---

## Temperaturkompensation

Ljudhastigheten i material förändras med temperaturen. I bil-NVH-testning betyder detta: ett motorrum vid 80 °C, en kallindränkt kabin vid -10 °C eller ett område för avgasgrenrör vid 200 °C beter sig alla annorlunda än laboratorieförhållanden vid rumstemperatur.

### Ställa in temperaturen

Öppna Inställningar (⚙ ikon) → Referenstemperatur. Ange din testmiljös temperatur i °C (intervall -40 till +200).

![Inställningspanel](../screenshots/06-settings.png)

### Vad händer när temperatur ≠ 20 °C

- Kalibreringstidsfält fylls automatiskt med temperaturjusterad hastighet
- Materialväljaren visar den justerade hastigheten framträdande
- En toast bekräftar: *"Aluminium tillämpat (6 284 m/s @ 60 °C) — N par uppdaterade"*
- Tipset "Närmaste material" jämför med temperaturjusterade hastigheter
- Sparade historikposter registrerar den aktiva temperaturen
- Rapporter inkluderar en sidfotsrad: *"Referenstemperatur: 60 °C, kompensation tillämpad"*

### Återställ vid appstart

Referenstemperaturen **återställs alltid till 20 °C** när du startar appen. Detta förhindrar att gamla inställningar från en tidigare mätsession tyst påverkar dagens arbete. En liten kursiv anmärkning i Inställningar påminner dig om detta beteende.

Om du vill spela upp en historisk mätning vid dess ursprungliga temperatur, tryck bara på posten — temperaturen återställs automatiskt.

### Material utan kompensation

De flesta icke-metalliska material har inte tillförlitliga publicerade temperaturkoefficienter. Appen visar en **"ref only"**-märkning för dessa — deras listade hastighet används oavsett temperaturinställning. Om du behöver noggranna mätningar vid icke-rumstemperaturer för dessa material, utför en in-situ kalibrering och spara resultatet som ett anpassat material.

---

## Fotoannotering

Efter en lyckad beräkning, tryck på knappen **📷 Annotera foto** för att lägga till sensor- och källmarkörer på ett foto av din inställning.

![Fotoannotering](../screenshots/08-photo-annotation.png)

### Flöde

1. Tryck på **Annotera foto** — systemkameran öppnas
2. Ta ett foto av din sensorplacering
3. Appen laddar fotot i annoteringsöverlägg
4. Sensormarkörer (A, B, C, D, E, F efter behov — upp till 6 sensorer) och källmarkören placeras automatiskt baserat på din beräkning
5. Dra valfri markör för att finjustera positionen. När du justerar beräknas källpositionen om från de korrigerade sensorpositionerna
6. Tryck på **Spara** för att behålla, eller **Ta om** för att försöka igen

Det annoterade fotot inkluderas automatiskt i PDF-rapporter.

---

## Rapporter

Tryck på knappen **Skriv ut resultat** på vilken resultatskärm som helst för att generera en formaterad rapport.

![PDF-rapport](../screenshots/09-pdf-report.png)

### Rapportinnehåll

- Rubrik (anpassningsbar i Inställningar → Rapportrubrik)
- Mätningstitel och tidsstämpel
- Alla inmatningsvärden i en tydlig tabell
- Beräkningsresultat
- Slutsatstext
- Visualisering (geometridiagram)
- Annoterat foto (om du tog ett)
- Sidfotsrad för temperatur (om kompensation var aktiv)
- Sidnummer och kreditrad

### Utdataformat

- **Android**: nativ PDF-generering, spara till din telefon eller dela
- **iOS**: systemets utskriftsdialog → spara som PDF, AirPrint eller dela

### Anpassa rubriken

Inställningar → Rapportrubrik. Ange ditt företagsnamn, labnamn, projektinfo eller vad du vill ha överst i varje rapport.

---

## Säkerhetskopiering och återställning

Spara alla dina anpassade material, favoriter, inställningar och historik i en enda fil. Överför mellan enheter.

### Säkerhetskopiering

Inställningar → **Säkerhetskopiering** → tryck på "Spara säkerhetskopia". Appen genererar en JSON-fil och öppnar telefonens delningsark. Spara den på din molnenhet (Google Drive, iCloud, OneDrive), e-posta den till dig själv eller överför på vilket sätt du vill.

### Återställ

Inställningar → **Återställ** → välj säkerhetskopian från telefonens lagring. Appen importerar anpassade material, favoriter, historik och inställningar.

⚠️ **Återställning ersätter dina nuvarande data.** Om du har viktiga mätningar på den nuvarande enheten, säkerhetskopiera dem först innan du återställer från en annan säkerhetskopia.

---

## Inställningar

Åtkomst via ⚙ kugghjulsikonen i det övre högra hörnet. Inställningar är ett modalfönster, inte en flik.

![Inställningar](../screenshots/06-settings.png)

| Inställning | Vad det kontrollerar |
|---|---|
| **Uppgradera till Pro** | Köp eller lär om Pro-funktioner ($19,99) |
| **Språk** | Appens visningsspråk (30 stöds) |
| **Tema** | Ljust, Mörkt eller Auto (följ systemet) |
| **Avståndsenhet** | cm eller tum |
| **Referenstemperatur** | Aktiv temperatur för kompensation, -40 till +200 °C |
| **Rapportrubrik** | Anpassad text överst i genererade rapporter |
| **Säkerhetskopiering** | Exportera all data till en fil |
| **Återställ** | Importera data från en säkerhetskopia |
| **Återställ köp** | Återhämta Pro på en ny enhet |

---

## Pro-funktioner

NVH Source Locator använder en **funktionslåst freemium-modell**:

- **Gratis**: Fliken 2-Sensor är helt funktionell utan begränsningar
- **Pro**: Alla andra flikar har specifika inmatningsfält låsta. Paywallen visas när en gratisanvändare trycker på ett låst fält

### Vad som är låst

Pro-krävande fält är spridda över:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D och 3D+ lägen
- Säkerhetskopiering och Återställ
- PDF-rapporter
- Anpassade material
- Fotoannotering

En gratisanvändare kan ÖPPNA vilken flik som helst och SE gränssnittet. De kan bara inte mata in värden i Pro-låsta inmatningsfält.

![Pro-låst fält](../screenshots/11-pro-locked-field.png)

### Paywallen

![Paywall](../screenshots/07-paywall.png)

När en gratisanvändare trycker på ett låst fält, glider paywallen in och visar:
- Appikon med PRO-märke
- Funktionslista
- Upplåsningsknapp med pris ($19,99 standard; kan variera per region)
- Inlösning av kampanjkod (endast Android — iOS använder Apples separata Offer Code-flöde)
- Valfri kampanjlänk till gemenskapskanaler

### Köpa Pro

Tryck på vilket låst fält som helst, eller tryck på **Uppgradera till Pro** i Inställningar. Använder din plattforms officiella betalningssystem (Google Play på Android, Apple App Store på iOS).

### Återställa Pro på en ny enhet

Om du köpte på en enhet och vill ha Pro på en annan (samma konto):

1. Logga in på **samma** Google-konto (Android) eller Apple ID (iOS) som du använde för att köpa
2. Öppna NVH Source Locator på den nya enheten
3. Gå till Inställningar → **Återställ köp**
4. Appen verifierar med plattformens köpregister och låser upp Pro

### Auto-återställning vid start

Om du löser in en kampanjkod i Google Play Store eller App Store medan NVH Source Locator körs i bakgrunden, upptäcker återgång till appen automatiskt det nya köpet och låser upp Pro — ingen manuell Återställning behövs.

### Inlösning av kampanjkod

**Android**: en knapp "Har du en Google Play-kampanjkod?" i paywallen öppnar Google Play-inlösningsflödet med din kod förifylld.

**iOS**: App Store-policy 3.1.1 kräver inlösning via Apples officiella "Lös in kod"-flöde. Google Play-knappen är dold på iOS. Leta efter "Lös in App Store-kod" i Inställningar istället.

---

## Fliken Help och handledningar

Fliken **Help** inkluderar handledningar i appen, guider för bästa praxis och referensinformation.

![Help-fliken](../screenshots/10-help-tab.png)

Ämnen som täcks:
- Vilken utrustning du behöver
- Hur man placerar sensorer för bästa noggrannhet
- Kalibreringstips
- Vanliga mätscenarier
- Tips för triangulering och 3D-placeringar
- Kabeldragning och signalkvalitet

---

## Felsökning

### Beräkningsresultatet är fel eller meningslöst

1. Kontrollera din kalibrering. Auto-fylld `tCal` antar publicerad materialhastighet — verkliga material varierar. Den mest exakta kalibreringen är in-situ: tryck på en känd plats och låt appen härleda den faktiska hastigheten.
2. Kontrollera inställningen **Första sensor** — vilken sensor som hörde händelsen först har betydelse för matematiken.
3. Verifiera dina avståndsmätningar. Fel på några mm sprider sig.

### Toast säger "Resultat utanför intervallet"

Matematiken säger att källan inte är mellan dina sensorer. Möjliga orsaker:
- Källan är faktiskt utanför sensorlinjen/planet
- En av dina ingångar är fel
- Kalibreringshastigheten är för långt från verkligheten

### Beräkningshastighetstips visar en varningsfärg

Den implicerade ljudhastigheten från dina ingångar är långt från något vanligt material (mindre än 50 m/s eller mer än 20 000 m/s). Kontrollera dina ingångar — troligen ett stavfel i tCal eller avstånd.

### Materialväljaren visar olika hastigheter än förväntat

Kontrollera referenstemperaturen i Inställningar. Om inte 20 °C, återspeglar visade hastigheter temperaturkompensation. Appen visar "ref X @ 20°C" under kompenserade hastigheter så att du kan verifiera.

### Historikpost spelas upp med annat resultat

Gamla historikposter skapade före appversion 1.75 kanske inte lagrade temperaturen. Om du tog mätningen vid en icke-20 °C-temperatur kommer uppspelning att använda den aktuella inställningen. Ställ in temperaturen manuellt i Inställningar innan du spelar upp, ELLER mät om.

### Fotoannoteringsmarkörer är inte där jag förväntar mig

Markörer placeras automatiskt baserat på inmatningsgeometri. Dra dem för att justera. Att justera markörer uppdaterar källpositionen i fotoöverlägget — men ÄNDRAR INTE det underliggande beräkningsresultatet.

### Säkerhetskopiering/Återställning misslyckas

Se till att du använder en säkerhetskopia som genererats av samma eller nyare version av appen. Äldre säkerhetskopior kan sakna aktuella datafält.

### Återställ köp säger "inget köp hittades"

1. Verifiera att du är inloggad på samma butikskonto som du använde för att köpa
2. Verifiera att köpet inte återbetalades eller har gått ut
3. Försök avinstallera och installera om appen (köpet är knutet till ditt butikskonto, inte appinstallationen)
4. Kontakta support@evdiag.net om det kvarstår

### Numerisk inmatning hoppar oväntat till 0

Med avsikt: när du lämnar fokus från ett numeriskt fält (trycker någon annanstans), om det är tomt, negativt eller innehåller icke-numerisk text, snappar det till 0. Förhindrar tyst trasiga beräkningar från oavsiktligt rensade ingångar. Temperaturingången är undantagen (den klämmer istället till -40/+200).

### Behöver mer hjälp

Kontakta `support@evdiag.net` med:
- Din enhetsmodell och OS-version
- Appversionen (Inställningar → längst ned på sidan)
- Beskrivning av vad du försökte
- Skärmdumpar om möjligt

---

*NVH Source Locator utvecklas av EVDiag. Besök https://evdiag.net för uppdateringar och resurser.*
