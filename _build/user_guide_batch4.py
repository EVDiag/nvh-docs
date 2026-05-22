"""User Guide translations — batch 4.

5 languages: sv, no, fi, ro, tr.
"""

USER_GUIDE_TRANSLATIONS = {

'sv': """# NVH Source Locator — Användarhandbok

NVH Source Locator är ett mätverktyg för att lokalisera buller- och vibrationskällor med hjälp av TDOA (Time Difference of Arrival) från accelerometersignaler som registreras på ett oscilloskop eller mätsystem.

Den här handboken täcker alla funktioner. För en snabb påminnelse, se **Snabbreferens**.

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

## Hur det fungerar {#how-it-works}

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

## Innan du börjar {#before-you-start}

Du behöver:

- **Ett oscilloskop eller mätsystem** som kan visa tidsskillnaden mellan accelerometerkanaler i mikrosekunder (µs)
- **Minst 2 accelerometrar** fysiskt fästa till strukturen (fler sensorer = högre noggrannhet)
- **Ett sätt att mäta avstånd** mellan sensorer (måttband, skjutmått)
- **Ett sätt att utlösa en våg** på en känd plats för kalibrering (kalibrerat hammarslag, skruvmejselslag eller annan känd signal)

![Hemskärm med fliken 2-Sensor](../screenshots/01-home-2sensor.png)

---

## De viktigaste flikarna {#the-main-tabs}

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

## 2-Sensor-läge {#2-sensor-mode}

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

## 3-Sensor-läge {#3-sensor-mode}

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

## Pro+-lägen {#pro-modes}

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

## Fliken Materials {#the-materials-tab}

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

## Temperaturkompensation {#temperature-compensation}

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

## Fotoannotering {#photo-annotation}

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

## Rapporter {#reports}

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

## Säkerhetskopiering och återställning {#backup-and-restore}

Spara alla dina anpassade material, favoriter, inställningar och historik i en enda fil. Överför mellan enheter.

### Säkerhetskopiering

Inställningar → **Säkerhetskopiering** → tryck på "Spara säkerhetskopia". Appen genererar en JSON-fil och öppnar telefonens delningsark. Spara den på din molnenhet (Google Drive, iCloud, OneDrive), e-posta den till dig själv eller överför på vilket sätt du vill.

### Återställ

Inställningar → **Återställ** → välj säkerhetskopian från telefonens lagring. Appen importerar anpassade material, favoriter, historik och inställningar.

⚠️ **Återställning ersätter dina nuvarande data.** Om du har viktiga mätningar på den nuvarande enheten, säkerhetskopiera dem först innan du återställer från en annan säkerhetskopia.

---

## Inställningar {#settings}

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

## Pro-funktioner {#pro-features}

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

## Fliken Help och handledningar {#help-tab-and-tutorials}

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

## Felsökning {#troubleshooting}

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
""",

'no': """# NVH Source Locator — Brukerhåndbok

NVH Source Locator er et måleverktøy for å lokalisere støy- og vibrasjonskilder ved hjelp av TDOA (Time Difference of Arrival) fra akselerometersignaler fanget på et oscilloskop eller målesystem.

Denne håndboken dekker alle funksjoner. For en rask oppfriskning, se **Hurtigreferanse**.

---

## Innholdsfortegnelse

1. [Hvordan det fungerer](#how-it-works)
2. [Før du starter](#before-you-start)
3. [Hovedfanene](#the-main-tabs)
4. [2-Sensor-modus](#2-sensor-mode)
5. [3-Sensor-modus](#3-sensor-mode)
6. [Pro+-moduser (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Materials-fanen](#the-materials-tab)
8. [Temperaturkompensasjon](#temperature-compensation)
9. [Fotomerknad](#photo-annotation)
10. [Rapporter](#reports)
11. [Sikkerhetskopiering og gjenoppretting](#backup-and-restore)
12. [Innstillinger](#settings)
13. [Pro-funksjoner](#pro-features)
14. [Help-fanen og veiledninger](#help-tab-and-tutorials)
15. [Feilsøking](#troubleshooting)

---

## Hvordan det fungerer {#how-it-works}

Når en støykilde sender ut lyd eller vibrasjon, beveger bølgen seg gjennom et materiale med kjent hastighet. Hvis du plasserer to eller flere akselerometre på materialet og måler når bølgen kommer til hver av dem, forteller tidsforskjellen deg hvor kilden er.

NVH Source Locator tar:

- **Kalibrering**: avstanden mellom sensorene og tiden det tar for en bølge å reise den avstanden (brukes til å beregne materialets lydhastighet)
- **Hendelse**: tidsforskjellen mellom sensorer som oppdager støy-/vibrasjonshendelsen

Deretter beregner den hvor på strukturen kilden er.

Jo flere sensorer du bruker, desto mer nøyaktig kan du finne kilden:

- **2 sensorer** → avstand langs en linje
- **3 sensorer** → posisjon på en 2D-overflate (X, Y)
- **4 sensorer** → posisjon i 3D-rom (X, Y, Z)

---

## Før du starter {#before-you-start}

Du trenger:

- **Et oscilloskop eller målesystem** som kan vise tidsforskjellen mellom akselerometerkanaler i mikrosekunder (µs)
- **Minst 2 akselerometre** fysisk festet til strukturen (flere sensorer = høyere nøyaktighet)
- **En måte å måle avstand** mellom sensorene (målebånd, skyvelære)
- **En måte å utløse en bølge** på et kjent sted for kalibrering (kalibrert hammerslag, skrutrekker-banking eller annet kjent signal)

![Hjemmeskjerm med 2-Sensor-fane](../screenshots/01-home-2sensor.png)

---

## Hovedfanene {#the-main-tabs}

Appen har faner øverst:

![Fanelinje](../screenshots/02-tab-bar.png)

| Fane | Hva den gjør | Når den brukes |
|---|---|---|
| **2-Sensor** | 1D-kildelokalisering langs en linje mellom 2 sensorer | Raske kontroller, bjelkelignende strukturer. **Helt gratis.** |
| **3-Sensor** | 2D-kildelokalisering med 3 sensorer i en trekant | Mest generell bruk, paneler og overflater |
| **3-Sen+** | 3-Sensor med overbestemt minste kvadraters løser | Mer krevende målinger, støyrobust |
| **4-Sensor** | 2D-lokalisering med to par (A-B + C-D) | Rektangulære sensorplassering, krysskontroll |
| **4-Sen+** | Avansert 2D-modus, 4 sensorer i hvilken som helst posisjon | Ikke-rektangulære geometrier, full LSQ |
| **3D** | 3D-kildelokalisering med 4 sensorer med XYZ-koordinater | Komplekse strukturer i 3D-rom |
| **3D+** | 3D med opptil 6 sensorer, overbestemt LSQ | Svært komplekse geometrier, maksimal presisjon |
| **Materials** | Lydhastighetsbibliotek + tilpassede materialer | Velg én gang per måleøkt |
| **Help** | Veiledninger i appen og referanse | Når du trenger en rask oppfriskning |

> **Gratis vs Pro**: 2-Sensor-fanen er helt gratis. Andre faner er tilgjengelige, men har spesifikke inntastingsfelt låst for Pro-brukere (markert med et gullhengelås-merke). Å trykke på et låst felt viser Pro-paywallen.

Innstillinger nås via ⚙ tannhjul-ikonet i øvre høyre hjørne (ikke en fane).

---

## 2-Sensor-modus {#2-sensor-mode}

Den enkleste målingen: kildelokalisering langs en linje mellom to akselerometre.

![2-Sensor-fane](../screenshots/01-home-2sensor.png)

### Trinn 1: Bruk et materiale

Trykk på Materials-fanen. Velg materialet din struktur er laget av (f.eks. "Aluminium", "Stål, Mild (1020)"). Appen bruker materialets kjente lydhastighet for å automatisk fylle kalibreringstidsfeltet.

Hvis strukturens materiale ikke er på listen, kan du midlertidig velge "Luft" og overstyre kalibreringstiden manuelt i trinn 2.

### Trinn 2: Skriv inn kalibreringsdata

På 2-Sensor-fanen ser du to par-seksjoner: **Par A–B** og **Par A–C** (bare A–B er nødvendig hvis du bare har 2 sensorer).

For hvert par fyller du inn:

- **Sensoravstand** (`d`): fysisk avstand mellom sensorer, i cm eller tommer (innstilt i Innstillinger)
- **Kalibreringstidforsinkelse** (`tCal`): tid for en bølge å reise mellom sensorene ved materialets lydhastighet — fylles automatisk når du velger et materiale, men du kan overstyre

### Trinn 3: Skriv inn hendelsestiden

- **Hendelsestidsforsinkelse** (`tEvent`): tidsforskjell mellom sensorer som oppdager støyhendelsen, i mikrosekunder
- **Første sensor**: hvilken sensor som hørte hendelsen først (A eller B)

### Trinn 4: Les resultatet

Appen viser kildeposisjonen som en avstand fra sensor A:
- Resultat = 0: kilden er ved sensor A
- Resultat = avstand: kilden er ved sensor B
- Resultat mellom: kilden er mellom dem
- Resultat utenfor: kilden er utenfor en av sensorene (toast vil advare)

Resultatkortet viser begge avstandene (fra A, fra B) og angir hvilken sensor som er nærmere.

### Trinn 5 (valgfritt): Annoter et bilde

Trykk på **📷 Annoter bilde** for å ta et bilde av oppsettet ditt. Appen legger til markører for sensorer A, B og kilden. Nyttig for rapporter.

---

## 3-Sensor-modus {#3-sensor-mode}

Lokaliserer en kilde på et 2D-plan ved å bruke tre sensorer arrangert i en trekant.

![3-Sensor-fane](../screenshots/03-3sensor-tab.png)

### Oppsett

Plasser tre sensorer på strukturen din som danner en trekant. Likebenet, rettvinklet eller skjevvinklet — appen håndterer alle geometrier.

### Skriv inn dataene

I delen **Trekantsidelengder**, skriv inn fysisk avstand for alle tre sidene (A–B, A–C, B–C).

For hvert par (A–B og A–C), skriv inn:
- **tCal**: kalibreringstid (autofylles fra materialet)
- **tEvent**: målt tidsforskjell for støyhendelsen
- **Første sensor**: hvilken hørte den først

### Les resultatet

Appen viser kildeposisjonen som X-, Y-koordinater relativt til sensor A (sensor A ved origo, sensor B på X-aksen). Visualiseringen viser alle tre sensorene og kildens plassering.

![Trekantresultat](../screenshots/04-triangle-result.png)

---

## Pro+-moduser {#pro-modes}

Flere avanserte faner tilbyr overbestemte løsere og høyere dimensjonalitet:

### 3-Sen+ (Pro)

Samme trekantoppsett som 3-Sensor, men kalibrer OG mål alle tre par (A–B, A–C, B–C). Løseren bruker alle 3 TDOA i en minste kvadraters tilpasning — mer robust mot målingsstøy og anisotropiske materialer. Restverdier per par rapporteres slik at du kan oppdage inkonsistente målinger.

### 4-Sensor

Plasser fire sensorer rundt området:
- **A–B** = horisontalt par (venstre/høyre sider)
- **C–D** = vertikalt par (øvre/nedre sider)

Kjør A–B-paret først (horisontalt), deretter C–D-paret (vertikalt). 2D-kartet viser skjæringspunktet. Hvert par kalibreres separat — nyttig når materialet varierer over strukturen.

### 4-Sen+ (Avansert 2D)

Fire sensorer i hvilken som helst posisjon (ikke tvunget rektangulær). Par A med hver av B, C, D og kalibrer separat. Den overbestemte minste kvadraters løseren gjennomsnittlig målingsstøyen per par og rapporterer restverdier per par.

### 3D

Full 3D-måling med 4 sensorer plassert i 3D-rom. Skriv inn hver sensors (X, Y, Z) koordinater, pluss kalibrerings- og hendelsestider for hvert par (A–B, A–C, A–D).

### 3D+ (Pro)

Som 3D men støtter opptil **6 sensorer** (A til F) med overbestemt LSQ. Maksimal presisjon for komplekse 3D-geometrier.

---

## Materials-fanen {#the-materials-tab}

Bibliotek med vanlige ingeniørmaterialer med kjent lydhastighet ved 20 °C.

![Materials-fane](../screenshots/05-materials-tab.png)

### Materialliste

Listen inkluderer luft, væsker, gummi, polymerer, tre, glass og metaller. Hastighetene varierer fra ~340 m/s (luft) til ~13 000 m/s (noen metaller ved romtemperatur).

### Innebygde materialer med temperaturkompensasjon

14 vanlig brukte metaller inkluderer temperaturkoeffisientdata. Når referansetemperaturen i Innstillinger skiller seg fra 20 °C, justerer appen automatisk hastighetene for disse materialene:

- Aluminium
- Stål, Mild (1020)
- Rustfritt Stål (304)
- Jern (støpt)
- Jern
- Kobber
- Messing
- Bronse
- Titan
- Magnesium
- Bly
- Sink
- Nikkel
- Wolfram

Materialer med kompensasjon viser to verdier i velgeren: den **kompenserte hastigheten** (stor, fremtredende) og **referansehastigheten ved 20 °C** (liten, grå under).

Materialer uten kompensasjon viser **"ref only"** i kursiv — deres oppførte hastighet brukes som den er uavhengig av temperatur.

### Tilpassede materialer

Hvis du måler en kalibrering på 2-Sensor-fanen, kan du lagre resultatet som et tilpasset materiale. Etter en vellykket 2-sensor-måling, se etter alternativet for å lagre den utledede hastigheten under et navn du velger.

Tilpassede materialer lagrer den in-situ målte hastigheten; de bruker aldri temperaturkompensasjon (hastigheten ble allerede målt ved testtemperaturen).

### Favoritter

Trykk på stjernen ved siden av et materiale for å merke det som favoritt. Favoritter vises øverst i listen for rask tilgang.

### Søk

Bruk søkefeltet øverst for å filtrere materialer etter navn. Søk samsvarer både med engelske kanoniske navn og oversatte visningsnavn.

---

## Temperaturkompensasjon {#temperature-compensation}

Lydhastigheten i materialer endrer seg med temperaturen. I bil-NVH-testing er dette viktig: et motorrom ved 80 °C, en kaldsenket kabin ved -10 °C eller et område for eksosmanifold ved 200 °C oppfører seg alle annerledes enn laboratorieforhold ved romtemperatur.

### Stille inn temperaturen

Åpne Innstillinger (⚙ ikon) → Referansetemperatur. Skriv inn temperaturen til testmiljøet ditt i °C (område -40 til +200).

![Innstillingspanel](../screenshots/06-settings.png)

### Hva skjer når temperaturen ≠ 20 °C

- Kalibreringstidsfeltene fylles automatisk med temperaturjustert hastighet
- Materials-velgeren viser fremtredende den justerte hastigheten
- En toast bekrefter: *"Aluminium brukt (6 284 m/s @ 60 °C) — N par oppdatert"*
- Tipset "Nærmeste materiale" sammenlignes med temperaturjusterte hastigheter
- Lagrede historikkoppføringer registrerer den aktive temperaturen
- Rapporter inkluderer en bunntekstlinje: *"Referansetemperatur: 60 °C, kompensasjon brukt"*

### Tilbakestilling ved appstart

Referansetemperaturen **tilbakestilles alltid til 20 °C** når du starter appen. Dette forhindrer at gamle innstillinger fra en tidligere måleøkt stille påvirker dagens arbeid. En liten kursiv merknad i Innstillinger minner deg på denne oppførselen.

Hvis du vil spille av en historisk måling ved den opprinnelige temperaturen, trykker du bare på oppføringen — temperaturen gjenopprettes automatisk.

### Materialer uten kompensasjon

De fleste ikke-metalliske materialer har ikke pålitelige publiserte temperaturkoeffisienter. Appen viser et **"ref only"**-merke for disse — deres oppførte hastighet brukes uavhengig av temperaturinnstillingen. Hvis du trenger nøyaktige målinger ved ikke-romtemperaturer for disse materialene, utfør en in-situ-kalibrering og lagre resultatet som et tilpasset materiale.

---

## Fotomerknad {#photo-annotation}

Etter en vellykket beregning, trykk på knappen **📷 Annoter bilde** for å legge sensor- og kildemarkører på et bilde av oppsettet ditt.

![Fotomerknad](../screenshots/08-photo-annotation.png)

### Flyt

1. Trykk på **Annoter bilde** — systemkameraet åpnes
2. Ta et bilde av sensorplasseringen din
3. Appen laster bildet inn i merknadsoverlegget
4. Sensormarkører (A, B, C, D, E, F etter behov — opptil 6 sensorer) og kildemarkøren plasseres automatisk basert på beregningen din
5. Dra en hvilken som helst markør for å finjustere posisjonen. Mens du justerer, beregnes kildeposisjonen på nytt fra de korrigerte sensorposisjonene
6. Trykk på **Lagre** for å beholde, eller **Ta på nytt** for å prøve igjen

Det annoterte bildet inkluderes automatisk i PDF-rapporter.

---

## Rapporter {#reports}

Trykk på knappen **Skriv ut resultat** på en hvilken som helst resultatskjerm for å generere en formatert rapport.

![PDF-rapport](../screenshots/09-pdf-report.png)

### Rapportinnhold

- Topptekst (kan tilpasses i Innstillinger → Rapporttopptekst)
- Måletittel og tidsstempel
- Alle inndataverdier i en oversiktlig tabell
- Beregningsresultat
- Konklusjonstekst
- Visualisering (geometrigraf)
- Annotert bilde (hvis du tok et)
- Bunntekstlinje for temperatur (hvis kompensasjon var aktiv)
- Sidetall og kreditlinje

### Utdataformat

- **Android**: nativ PDF-generering, lagre på telefonen eller del
- **iOS**: systemets utskriftsdialog → lagre som PDF, AirPrint eller del

### Tilpasse toppteksten

Innstillinger → Rapporttopptekst. Skriv inn firmanavnet, labnavnet, prosjektinfo eller hva du vil ha øverst i hver rapport.

---

## Sikkerhetskopiering og gjenoppretting {#backup-and-restore}

Lagre alle de tilpassede materialene, favorittene, innstillingene og historikken til en enkelt fil. Overfør mellom enheter.

### Sikkerhetskopiering

Innstillinger → **Sikkerhetskopiering** → trykk på "Lagre sikkerhetskopifil". Appen genererer en JSON-fil og åpner telefonens delingsark. Lagre den til skystasjonen din (Google Drive, iCloud, OneDrive), e-post den til deg selv eller overfør på hvilken som helst måte.

### Gjenopprett

Innstillinger → **Gjenopprett** → velg sikkerhetskopifilen fra telefonens lagring. Appen importerer tilpassede materialer, favoritter, historikk og innstillinger.

⚠️ **Gjenoppretting erstatter dine nåværende data.** Hvis du har viktige målinger på den nåværende enheten, sikkerhetskopier dem først før du gjenoppretter fra en annen sikkerhetskopi.

---

## Innstillinger {#settings}

Tilgang via ⚙ tannhjul-ikonet i øvre høyre hjørne. Innstillinger er en modal, ikke en fane.

![Innstillinger](../screenshots/06-settings.png)

| Innstilling | Hva den kontrollerer |
|---|---|
| **Oppgrader til Pro** | Kjøp eller lær om Pro-funksjoner ($19,99) |
| **Språk** | Appens visningsspråk (30 støttes) |
| **Tema** | Lys, Mørk eller Auto (følg systemet) |
| **Avstandsenhet** | cm eller tommer |
| **Referansetemperatur** | Aktiv temperatur for kompensasjon, -40 til +200 °C |
| **Rapporttopptekst** | Egendefinert tekst øverst i genererte rapporter |
| **Sikkerhetskopiering** | Eksporter alle data til en fil |
| **Gjenopprett** | Importer data fra en sikkerhetskopi |
| **Gjenopprett kjøp** | Anskaff Pro på nytt på en ny enhet |

---

## Pro-funksjoner {#pro-features}

NVH Source Locator bruker en **funksjonslåst freemium-modell**:

- **Gratis**: 2-Sensor-fanen er fullt funksjonell uten begrensninger
- **Pro**: Alle andre faner har spesifikke inntastingsfelt låst. Paywallen vises når en gratisbruker trykker på et låst felt

### Hva som er låst

Pro-krevende felt er spredt over:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D- og 3D+-moduser
- Sikkerhetskopiering og Gjenoppretting
- PDF-rapporter
- Tilpassede materialer
- Fotomerknad

En gratisbruker kan ÅPNE en hvilken som helst fane og SE grensesnittet. De kan bare ikke skrive inn verdier i Pro-låste inntastingsfelt.

![Pro-låst felt](../screenshots/11-pro-locked-field.png)

### Paywallen

![Paywall](../screenshots/07-paywall.png)

Når en gratisbruker trykker på et låst felt, glir paywallen inn og viser:
- App-ikon med PRO-merke
- Funksjonsliste
- Opplåsingsknapp med pris ($19,99 standard; kan variere etter region)
- Innløsing av kampanjekode (kun Android — iOS bruker Apples separate Offer Code-flyt)
- Valgfri kampanjelenke til samfunnskanaler

### Kjøpe Pro

Trykk på et hvilket som helst låst felt, eller trykk på **Oppgrader til Pro** i Innstillinger. Bruker plattformens offisielle betalingssystem (Google Play på Android, Apple App Store på iOS).

### Gjenopprette Pro på en ny enhet

Hvis du kjøpte på én enhet og vil ha Pro på en annen (samme konto):

1. Logg på den **samme** Google-kontoen (Android) eller Apple ID (iOS) som du brukte for å kjøpe
2. Åpne NVH Source Locator på den nye enheten
3. Gå til Innstillinger → **Gjenopprett kjøp**
4. Appen verifiserer med plattformens kjøpsregistre og låser opp Pro

### Auto-gjenoppretting ved oppstart

Hvis du løser inn en kampanjekode i Google Play Store eller App Store mens NVH Source Locator kjører i bakgrunnen, oppdager retur til appen automatisk det nye kjøpet og låser opp Pro — ingen manuell Gjenoppretting nødvendig.

### Innløsing av kampanjekode

**Android**: en knapp "Har du en Google Play-kampanjekode?" i paywallen åpner Google Play-innløsingsflyten med koden din forhåndsutfylt.

**iOS**: App Store-policy 3.1.1 krever innløsing gjennom Apples offisielle "Løs inn kode"-flyt. Google Play-knappen er skjult på iOS. Se etter "Løs inn App Store-kode" i Innstillinger i stedet.

---

## Help-fanen og veiledninger {#help-tab-and-tutorials}

**Help**-fanen inkluderer veiledninger i appen, beste praksis-guider og referanseinformasjon.

![Help-fane](../screenshots/10-help-tab.png)

Emner dekket:
- Hvilket utstyr du trenger
- Hvordan plassere sensorer for best nøyaktighet
- Kalibreringstips
- Vanlige målescenarier
- Tips for triangulering og 3D-plasseringer
- Kabelføring og signalkvalitet

---

## Feilsøking {#troubleshooting}

### Beregningsresultatet er feil eller gir ingen mening

1. Sjekk kalibreringen. Auto-fylt `tCal` antar publisert materialhastighet — virkelige materialer varierer. Den mest nøyaktige kalibreringen er in-situ: trykk på en kjent plassering og la appen utlede den faktiske hastigheten.
2. Sjekk **Første sensor**-innstillingen — hvilken sensor som hørte hendelsen først betyr noe for matematikken.
3. Verifiser avstandsmålingene dine. Feil på noen mm forplanter seg.

### Toast sier "Resultat utenfor området"

Matematikken sier at kilden ikke er mellom sensorene dine. Mulige årsaker:
- Kilden er faktisk utenfor sensorlinjen/planet
- En av inndataene dine er feil
- Kalibreringshastigheten er for langt fra virkeligheten

### Beregningshastighetstips viser en advarselsfarge

Den implisitte lydhastigheten fra inndataene dine er langt fra noe vanlig materiale (mindre enn 50 m/s eller mer enn 20 000 m/s). Sjekk inndataene dine — sannsynligvis en skrivefeil i tCal eller avstand.

### Materialvelgeren viser forskjellige hastigheter enn forventet

Sjekk referansetemperaturen i Innstillinger. Hvis ikke 20 °C, reflekterer viste hastigheter temperaturkompensasjon. Appen viser "ref X @ 20°C" under kompenserte hastigheter slik at du kan verifisere.

### Historikkoppføring spiller av med annet resultat

Gamle historikkoppføringer opprettet før appversjon 1.75 har kanskje ikke lagret temperaturen. Hvis du tok målingen ved en ikke-20 °C-temperatur, vil avspilling bruke den nåværende innstillingen. Sett temperaturen manuelt i Innstillinger før avspilling, ELLER mål på nytt.

### Fotomerknadsmarkører er ikke der jeg forventer

Markører plasseres automatisk basert på inndatageometri. Dra dem for å justere. Justering av markører oppdaterer kildeposisjonen i fotooverlegget — men ENDRER IKKE det underliggende beregningsresultatet.

### Sikkerhetskopiering/Gjenoppretting mislykkes

Sørg for at du bruker en sikkerhetskopi generert av samme eller nyere versjon av appen. Eldre sikkerhetskopier kan mangle gjeldende datafelt.

### Gjenopprett kjøp sier "ingen kjøp funnet"

1. Verifiser at du er logget på samme butikkonto som du brukte for å kjøpe
2. Verifiser at kjøpet ikke ble refundert eller har utløpt
3. Prøv å avinstallere og installere appen på nytt (kjøpet er knyttet til butikkontoen din, ikke app-installasjonen)
4. Kontakt support@evdiag.net hvis det vedvarer

### Numerisk inndata snapper uventet til 0

Med hensikt: når du mister fokus på et numerisk felt (trykker andre steder), hvis det er tomt, negativt eller inneholder ikke-numerisk tekst, snapper det til 0. Forhindrer stille ødelagte beregninger fra utilsiktet slettede inndata. Temperaturinndataen er unntatt (den klemmes i stedet til -40/+200).

### Trenger mer hjelp

Kontakt `support@evdiag.net` med:
- Enhetsmodell og OS-versjon
- App-versjonen (Innstillinger → bunnen av siden)
- Beskrivelse av hva du prøvde
- Skjermbilder hvis mulig

---

*NVH Source Locator utvikles av EVDiag. Besøk https://evdiag.net for oppdateringer og ressurser.*
""",

'fi': """# NVH Source Locator — Käyttöopas

NVH Source Locator on mittaustyökalu melu- ja tärinälähteiden paikantamiseen TDOA:n (Time Difference of Arrival) avulla oskilloskoopilla tai mittausjärjestelmällä taltioiduista kiihtyvyysanturin signaaleista.

Tämä opas kattaa kaikki ominaisuudet. Pikaviittaukseen, katso **Pikaviite**.

---

## Sisällysluettelo

1. [Kuinka se toimii](#how-it-works)
2. [Ennen aloittamista](#before-you-start)
3. [Päävälilehdet](#the-main-tabs)
4. [2-Sensor-tila](#2-sensor-mode)
5. [3-Sensor-tila](#3-sensor-mode)
6. [Pro+-tilat (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Materials-välilehti](#the-materials-tab)
8. [Lämpötilakompensointi](#temperature-compensation)
9. [Valokuvan merkintä](#photo-annotation)
10. [Raportit](#reports)
11. [Varmuuskopiointi ja palautus](#backup-and-restore)
12. [Asetukset](#settings)
13. [Pro-ominaisuudet](#pro-features)
14. [Help-välilehti ja opetusohjelmat](#help-tab-and-tutorials)
15. [Vianmääritys](#troubleshooting)

---

## Kuinka se toimii {#how-it-works}

Kun melulähde lähettää ääntä tai tärinää, aalto kulkee materiaalin läpi tunnetulla nopeudella. Jos asetat kaksi tai useampia kiihtyvyysanturia materiaalille ja mittaat, milloin aalto saapuu kuhunkin, aikaero kertoo missä lähde sijaitsee.

NVH Source Locator ottaa:

- **Kalibroinnin**: antureiden välisen etäisyyden ja ajan, joka aallolla kestää tämän etäisyyden kulkemiseen (käytetään materiaalin äänennopeuden laskemiseen)
- **Tapahtuman**: aikaeron antureiden välillä, jotka havaitsevat melu-/tärinätapahtuman

Sitten se laskee, missä lähde sijaitsee rakenteessa.

Mitä enemmän antureita käytät, sitä tarkemmin voit paikallistaa lähteen:

- **2 anturia** → etäisyys viivan suuntaisesti
- **3 anturia** → asema 2D-pinnalla (X, Y)
- **4 anturia** → asema 3D-tilassa (X, Y, Z)

---

## Ennen aloittamista {#before-you-start}

Tarvitset:

- **Oskilloskoopin tai mittausjärjestelmän**, joka pystyy näyttämään aikaeron kiihtyvyysantureiden kanavien välillä mikrosekuntina (µs)
- **Vähintään 2 kiihtyvyysanturia** fyysisesti kiinnitettynä rakenteeseen (enemmän antureita = suurempi tarkkuus)
- **Tapa mitata etäisyyttä** antureiden välillä (mittanauha, kaliiperi)
- **Tapa laukaista aalto** tunnetussa paikassa kalibrointia varten (kalibroitu vasaranisku, ruuvimeisselin napautus tai muu tunnettu signaali)

![Aloitusnäyttö 2-Sensor-välilehdellä](../screenshots/01-home-2sensor.png)

---

## Päävälilehdet {#the-main-tabs}

Sovelluksessa on välilehdet yläosassa:

![Välilehtipalkki](../screenshots/02-tab-bar.png)

| Välilehti | Mitä se tekee | Milloin käyttää |
|---|---|---|
| **2-Sensor** | 1D lähteen paikannus viivaa pitkin 2 anturin välillä | Pikatarkistukset, palkkimaiset rakenteet. **Täysin ilmainen.** |
| **3-Sensor** | 2D lähteen paikannus 3 anturilla kolmiossa | Yleisin käyttö, paneelit ja pinnat |
| **3-Sen+** | 3-Sensor ylidefinoidulla pienimmän neliösumman ratkaisijalla | Vaativammat mittaukset, kohinankestävä |
| **4-Sensor** | 2D paikannus kahdella parilla (A-B + C-D) | Suorakaiteen muotoiset anturiasettelut, ristikkäistarkistus |
| **4-Sen+** | Edistynyt 2D-tila, 4 anturia missä tahansa sijainnissa | Ei-suorakaiteen geometriat, täysi LSQ |
| **3D** | 3D lähteen paikannus 4 anturilla XYZ-koordinaateilla | Monimutkaiset rakenteet 3D-tilassa |
| **3D+** | 3D enintään 6 anturilla, ylidefinoituun LSQ:hen | Erittäin monimutkaiset geometriat, maksimaalinen tarkkuus |
| **Materials** | Äänennopeuskirjasto + mukautetut materiaalit | Valitse kerran mittausistuntoa kohti |
| **Help** | Sovelluksen sisäiset opetusohjelmat ja viite | Kun tarvitset pikaviittauksen |

> **Ilmainen vs Pro**: 2-Sensor-välilehti on täysin ilmainen. Muut välilehdet ovat saatavilla, mutta niissä on tiettyjä syöttökenttiä lukittuna Pro-käyttäjille (merkitty kultaisella riippulukon merkillä). Lukitun kentän napauttaminen näyttää Pro-paywallin.

Asetuksiin pääsee ⚙ rataspyörän kuvakkeen kautta oikeassa yläkulmassa (ei välilehti).

---

## 2-Sensor-tila {#2-sensor-mode}

Yksinkertaisin mittaus: lähteen paikannus viivaa pitkin kahden kiihtyvyysanturin välillä.

![2-Sensor-välilehti](../screenshots/01-home-2sensor.png)

### Vaihe 1: Käytä materiaalia

Napauta Materials-välilehteä. Valitse materiaali, josta rakenteesi on tehty (esim. "Alumiini", "Teräs, Mild (1020)"). Sovellus käyttää materiaalin tunnettua äänennopeutta täyttääkseen kalibrointiaikakentän automaattisesti.

Jos rakenteesi materiaalia ei ole luettelossa, voit valita väliaikaisesti "Ilma" ja ohittaa kalibrointiajan manuaalisesti vaiheessa 2.

### Vaihe 2: Syötä kalibrointitiedot

2-Sensor-välilehdellä näet kaksi parisektioita: **Pari A–B** ja **Pari A–C** (vain A–B vaaditaan, jos sinulla on vain 2 anturia).

Kullekin parille täytät:

- **Anturien etäisyys** (`d`): antureiden välinen fyysinen etäisyys, cm tai tuumina (asetetaan Asetuksissa)
- **Kalibrointiajan viive** (`tCal`): aika, jonka aalto kulkee anturien välillä materiaalin äänennopeudella — automaattisesti täytetty, kun valitset materiaalin, mutta voit ohittaa

### Vaihe 3: Syötä tapahtuma-aika

- **Tapahtuma-ajan viive** (`tEvent`): aikaero antureiden välillä, jotka havaitsevat melutapahtuman, mikrosekunteina
- **Ensimmäinen anturi**: mikä anturi kuuli tapahtuman ensimmäisenä (A vai B)

### Vaihe 4: Lue tulos

Sovellus näyttää lähteen sijainnin etäisyytenä anturista A:
- Tulos = 0: lähde on anturin A kohdalla
- Tulos = etäisyys: lähde on anturin B kohdalla
- Tulos välissä: lähde on niiden välissä
- Tulos ulkopuolella: lähde on yhden anturin takana (toast varoittaa)

Tuloskortti näyttää molemmat etäisyydet (A:sta, B:stä) ja osoittaa, mikä anturi on lähempänä.

### Vaihe 5 (valinnainen): Merkitse valokuva

Napauta **📷 Merkitse valokuva** ottaaksesi valokuvan asennuksesta. Sovellus asettaa merkit antureille A, B ja lähteelle. Hyödyllinen raportteihin.

---

## 3-Sensor-tila {#3-sensor-mode}

Paikallistaa lähteen 2D-tasolla kolmen kolmioon asetetun anturin avulla.

![3-Sensor-välilehti](../screenshots/03-3sensor-tab.png)

### Asennus

Aseta kolme anturia rakenteellesi muodostaen kolmion. Tasakylkinen, suorakulmainen tai eripuolinen — sovellus käsittelee kaikki geometriat.

### Syötä tiedot

**Kolmion sivun pituudet** -osiossa, syötä fyysinen etäisyys kaikille kolmelle sivulle (A–B, A–C, B–C).

Kullekin parille (A–B ja A–C) syötä:
- **tCal**: kalibrointiaika (täyttyy automaattisesti materiaalista)
- **tEvent**: mitattu aikaero melutapahtumalle
- **Ensimmäinen anturi**: mikä kuuli sen ensimmäisenä

### Lue tulos

Sovellus näyttää lähteen sijainnin X-, Y-koordinaatteina suhteessa anturiin A (anturi A origossa, anturi B X-akselilla). Visualisointi näyttää kaikki kolme anturia ja lähteen sijainnin.

![Kolmion tulos](../screenshots/04-triangle-result.png)

---

## Pro+-tilat {#pro-modes}

Useat edistyneet välilehdet tarjoavat ylidefinoituja ratkaisijoita ja korkeampaa ulottuvuutta:

### 3-Sen+ (Pro)

Sama kolmioasennus kuin 3-Sensor, mutta kalibroi JA mittaa kaikki kolme paria (A–B, A–C, B–C). Ratkaisija käyttää kaikkia 3 TDOA:ta pienimmän neliösumman sovituksessa — vahvempi mittausäänekohinaa ja anisotrooppisia materiaaleja vastaan. Parikohtaiset jäännökset raportoidaan, joten voit havaita epäjohdonmukaiset mittaukset.

### 4-Sensor

Aseta neljä anturia alueen ympärille:
- **A–B** = vaakatasoinen pari (vasen/oikea sivu)
- **C–D** = pystysuora pari (ylä/ala sivut)

Suorita ensin pari A–B (vaakatasoinen), sitten pari C–D (pystysuora). 2D-kartta näyttää leikkauspisteen. Jokainen pari kalibroidaan erikseen — hyödyllistä, kun materiaali vaihtelee rakenteen yli.

### 4-Sen+ (Edistynyt 2D)

Neljä anturia missä tahansa sijainnissa (ei pakotettu suorakaiteeksi). Parita A jokaisen B:n, C:n, D:n kanssa ja kalibroi erikseen. Ylidefinoituun pienimmän neliösumman ratkaisija laskee parikohtaisen mittausäänen keskimäärän ja raportoi parikohtaiset jäännökset.

### 3D

Täysi 3D-mittaus 4 anturilla sijoitettuna 3D-tilaan. Syötä kunkin anturin (X, Y, Z) koordinaatit, sekä kalibrointi- ja tapahtuma-ajat kullekin parille (A–B, A–C, A–D).

### 3D+ (Pro)

Kuten 3D, mutta tukee enintään **6 anturia** (A:sta F:ään) ylidefinoituun LSQ:hen. Maksimaalinen tarkkuus monimutkaisille 3D-geometrioille.

---

## Materials-välilehti {#the-materials-tab}

Tavallisten teknisten materiaalien kirjasto tunnetulla äänennopeudella 20 °C:ssa.

![Materials-välilehti](../screenshots/05-materials-tab.png)

### Materiaaliluettelo

Luettelo sisältää ilmaa, nesteitä, kumeja, polymeerejä, puuta, lasia ja metalleja. Nopeudet vaihtelevat ~340 m/s:sta (ilma) ~13 000 m/s:hen (jotkut metallit huoneenlämpötilassa).

### Sisäänrakennetut materiaalit lämpötilakompensoinnilla

14 yleisesti käytettyä metallia sisältää lämpötilakerroindatat. Kun Asetusten viitelämpötila eroaa 20 °C:sta, sovellus säätää näiden materiaalien nopeudet automaattisesti:

- Alumiini
- Teräs, Mild (1020)
- Ruostumaton Teräs (304)
- Rauta (valettu)
- Rauta
- Kupari
- Messinki
- Pronssi
- Titaani
- Magnesium
- Lyijy
- Sinkki
- Nikkeli
- Volframi

Kompensoidut materiaalit näyttävät kaksi arvoa valitsimessa: **kompensoidun nopeuden** (suuri, näkyvä) ja **viitenopeuden 20 °C:ssa** (pieni, harmaa alla).

Kompensoimattomat materiaalit näyttävät **"ref only"** kursiivilla — niiden listattu nopeus käytetään sellaisenaan riippumatta lämpötilasta.

### Mukautetut materiaalit

Jos mittaat kalibroinnin 2-Sensor-välilehdellä, voit tallentaa tuloksen mukautettuna materiaalina. Onnistuneen 2-sensor-mittauksen jälkeen etsi vaihtoehto johdetun nopeuden tallentamiseen valitsemasi nimen alla.

Mukautetut materiaalit tallentavat in-situ-mitatun nopeuden; ne eivät koskaan käytä lämpötilakompensointia (nopeus on jo mitattu testin lämpötilassa).

### Suosikit

Napauta tähteä minkä tahansa materiaalin vieressä merkitäksesi sen suosikiksi. Suosikit näkyvät luettelon yläosassa nopeaa pääsyä varten.

### Haku

Käytä yläosan hakukenttää suodattaaksesi materiaalit nimen mukaan. Haku vastaa sekä englannin kielen kanonisia nimiä että käännettyjä näyttönimiä.

---

## Lämpötilakompensointi {#temperature-compensation}

Äänennopeus materiaaleissa muuttuu lämpötilan myötä. Automotiivisessa NVH-testauksessa tämä on tärkeää: 80 °C:n moottoritila, -10 °C:n kylmäimeytetty hytti tai 200 °C:n pakosarjaalue käyttäytyvät eri tavalla kuin huoneenlämpötilan laboratorio-olosuhteet.

### Lämpötilan asettaminen

Avaa Asetukset (⚙-kuvake) → Viitelämpötila. Syötä testiympäristösi lämpötila °C:ssa (alue -40 - +200).

![Asetuspaneeli](../screenshots/06-settings.png)

### Mitä tapahtuu, kun lämpötila ≠ 20 °C

- Kalibrointiaikakentät täyttyvät automaattisesti lämpötilan mukaan säädetyllä nopeudella
- Materials-valitsin näyttää näkyvästi säädetyn nopeuden
- Toast vahvistaa: *"Alumiini sovellettu (6 284 m/s @ 60 °C) — N paria päivitetty"*
- "Lähin materiaali" -vihje vertailee lämpötilan mukaan säädettyihin nopeuksiin
- Tallennetut historiamerkinnät kirjaavat aktiivisen lämpötilan
- Raportit sisältävät alatunnisteen: *"Viitelämpötila: 60 °C, kompensointi sovellettu"*

### Nollaus sovelluksen käynnistyksessä

Viitelämpötila **nollautuu aina 20 °C:hen**, kun käynnistät sovelluksen. Tämä estää vanhentuneita asetuksia aiemmasta mittausistunnosta hiljaa vaikuttamasta tämän päivän työhön. Pieni kursiivinen merkintä Asetuksissa muistuttaa sinua tästä käyttäytymisestä.

Jos haluat toistaa historiallisen mittauksen sen alkuperäisessä lämpötilassa, napauta vain merkintää — lämpötila palautetaan automaattisesti.

### Materiaalit ilman kompensointia

Useimmilla ei-metallisilla materiaaleilla ei ole luotettavia julkaistuja lämpötilakertoimia. Sovellus näyttää niille **"ref only"**-merkin — niiden listattu nopeus käytetään riippumatta lämpötila-asetuksesta. Jos tarvitset tarkkoja mittauksia ei-huoneenlämpötiloissa näille materiaaleille, suorita in-situ-kalibrointi ja tallenna tulos mukautettuna materiaalina.

---

## Valokuvan merkintä {#photo-annotation}

Onnistuneen laskennan jälkeen, napauta **📷 Merkitse valokuva** -painiketta asettaaksesi anturi- ja lähdemerkit asennuksesi valokuvan päälle.

![Valokuvan merkintä](../screenshots/08-photo-annotation.png)

### Kulku

1. Napauta **Merkitse valokuva** — järjestelmäkamera avautuu
2. Ota valokuva anturien sijoittelusta
3. Sovellus lataa valokuvan merkintätason
4. Anturimerkit (A, B, C, D, E, F tarpeen mukaan — enintään 6 anturia) ja lähdemerkki sijoitetaan automaattisesti laskelmasi perusteella
5. Vedä mitä tahansa merkkiä asennon hienosäätämiseksi. Säätäessäsi lähteen sijainti lasketaan uudelleen korjattujen anturien sijaintien perusteella
6. Napauta **Tallenna** säilyttääksesi tai **Ota uudelleen** yrittääksesi uudelleen

Merkitty valokuva sisällytetään automaattisesti PDF-raportteihin.

---

## Raportit {#reports}

Napauta **Tulosta tulos** -painiketta millä tahansa tulosnäytöllä luodaksesi muotoillun raportin.

![PDF-raportti](../screenshots/09-pdf-report.png)

### Raportin sisältö

- Otsikko (mukautettavissa Asetuksissa → Raportin otsikko)
- Mittauksen nimi ja aikaleima
- Kaikki syöttöarvot siistissä taulukossa
- Laskentatulos
- Päätelmäteksti
- Visualisointi (geometriakuvaaja)
- Merkitty valokuva (jos otit sellaisen)
- Lämpötilan alatunniste (jos kompensointi oli aktiivinen)
- Sivunumero ja nimirivi

### Tulostusmuoto

- **Android**: natiivi PDF-luonti, tallenna puhelimeen tai jaa
- **iOS**: järjestelmän tulostusvalintaikkuna → tallenna PDF:nä, AirPrint tai jaa

### Otsikon mukauttaminen

Asetukset → Raportin otsikko. Syötä yrityksesi nimi, laboratorion nimi, projektin tiedot tai mitä haluat jokaisen raportin yläosaan.

---

## Varmuuskopiointi ja palautus {#backup-and-restore}

Tallenna kaikki mukautetut materiaalit, suosikit, asetukset ja historia yhteen tiedostoon. Siirto laitteiden välillä.

### Varmuuskopiointi

Asetukset → **Varmuuskopiointi** → napauta "Tallenna varmuuskopiotiedosto". Sovellus luo JSON-tiedoston ja avaa puhelimesi jakovalikon. Tallenna se pilvitallennuksessasi (Google Drive, iCloud, OneDrive), lähetä se sähköpostitse itsellesi tai siirrä haluamallasi tavalla.

### Palautus

Asetukset → **Palautus** → valitse varmuuskopiotiedosto puhelimesi tallennustilasta. Sovellus tuo mukautetut materiaalit, suosikit, historian ja asetukset.

⚠️ **Palautus korvaa nykyiset tietosi.** Jos sinulla on tärkeitä mittauksia nykyisellä laitteella, varmuuskopioi ne ensin ennen palauttamista eri varmuuskopiosta.

---

## Asetukset {#settings}

Pääsy ⚙ rataspyörän kuvakkeen kautta oikeassa yläkulmassa. Asetukset on modaalinen, ei välilehti.

![Asetukset](../screenshots/06-settings.png)

| Asetus | Mitä se ohjaa |
|---|---|
| **Päivitä Pro:hon** | Osta tai opi Pro-ominaisuuksista ($19,99) |
| **Kieli** | Sovelluksen näyttökieli (30 tuettu) |
| **Teema** | Vaalea, Tumma tai Automaattinen (seuraa järjestelmää) |
| **Etäisyysyksikkö** | cm tai tuumat |
| **Viitelämpötila** | Aktiivinen lämpötila kompensointia varten, -40 - +200 °C |
| **Raportin otsikko** | Mukautettu teksti luotujen raporttien yläosassa |
| **Varmuuskopiointi** | Vie kaikki tiedot tiedostoon |
| **Palautus** | Tuo tiedot varmuuskopiotiedostosta |
| **Palauta osto** | Hanki Pro uudelleen uudella laitteella |

---

## Pro-ominaisuudet {#pro-features}

NVH Source Locator käyttää **ominaisuuslukittua freemium-mallia**:

- **Ilmainen**: 2-Sensor-välilehti on täysin toimiva ilman rajoituksia
- **Pro**: Kaikilla muilla välilehdillä on tiettyjä syöttökenttiä lukittuna. Paywall ilmestyy, kun ilmainen käyttäjä napauttaa lukittua kenttää

### Mitä on lukittu

Pro-vaativat kentät ovat hajallaan:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D- ja 3D+-tilat
- Varmuuskopiointi ja Palautus
- PDF-raportit
- Mukautetut materiaalit
- Valokuvan merkintä

Ilmainen käyttäjä voi AVATA minkä tahansa välilehden ja NÄHDÄ käyttöliittymän. He eivät vain voi syöttää arvoja Pro-lukittuihin syöttökenttiin.

![Pro-lukittu kenttä](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Kun ilmainen käyttäjä napauttaa lukittua kenttää, paywall liukuu esiin näyttäen:
- Sovelluksen kuvake PRO-merkillä
- Ominaisuusluettelo
- Avauspainike hinnan kanssa ($19,99 oletus; voi vaihdella alueittain)
- Promokoodin lunastus (vain Android — iOS käyttää Applen erillistä Offer Code -kulkua)
- Valinnainen promo-linkki yhteisökanaviin

### Pron osto

Napauta mitä tahansa lukittua kenttää tai napauta **Päivitä Pro:hon** Asetuksissa. Käyttää alustasi virallista maksujärjestelmää (Google Play Androidilla, Apple App Store iOS:ssä).

### Pron palauttaminen uudella laitteella

Jos ostit yhdellä laitteella ja haluat Pro:n toisella (sama tili):

1. Kirjaudu **samaan** Google-tiliin (Android) tai Apple ID:hen (iOS), jota käytit ostoon
2. Avaa NVH Source Locator uudella laitteella
3. Mene Asetukset → **Palauta osto**
4. Sovellus tarkistaa alustan ostotietueet ja avaa Pro:n

### Automaattinen palautus käynnistyksessä

Jos lunastat promokoodin Google Play Storessa tai App Storessa NVH Source Locatorin ollessa taustalla, sovellukseen palaaminen havaitsee automaattisesti uuden oston ja avaa Pro:n — manuaalista palautusta ei tarvita.

### Promokoodin lunastus

**Android**: paywallin "Onko sinulla Google Play -promokoodi?" -painike avaa Google Play -lunastuskulun esitäytetyllä koodillasi.

**iOS**: App Storen käytäntö 3.1.1 vaatii lunastuksen Applen virallisen "Lunasta koodi" -kulun kautta. Google Play -painike on piilotettu iOS:ssä. Etsi sen sijaan "Lunasta App Store -koodi" Asetuksista.

---

## Help-välilehti ja opetusohjelmat {#help-tab-and-tutorials}

**Help**-välilehti sisältää sovelluksen sisäisiä opetusohjelmia, parhaiden käytäntöjen oppaita ja viitetietoja.

![Help-välilehti](../screenshots/10-help-tab.png)

Käsitellyt aiheet:
- Mitä laitteita tarvitset
- Kuinka sijoittaa anturit parhaan tarkkuuden saavuttamiseksi
- Kalibrointivinkit
- Yleiset mittausskenaariot
- Vinkit triangulaatioon ja 3D-sijoitteluihin
- Kaapelireititys ja signaalin laatu

---

## Vianmääritys {#troubleshooting}

### Laskennan tulos on väärä tai ei ole järkeenkäypä

1. Tarkista kalibrointi. Automaattisesti täytetty `tCal` olettaa julkaistun materiaalin nopeuden — todelliset materiaalit vaihtelevat. Tarkin kalibrointi on in-situ: napauta tunnettua paikkaa ja anna sovelluksen johtaa todellinen nopeus.
2. Tarkista **Ensimmäinen anturi** -asetus — mikä anturi kuuli tapahtuman ensin, on tärkeää matematiikan kannalta.
3. Vahvista etäisyysmittauksesi. Muutaman millimetrin virheet leviävät.

### Toast sanoo "Tulos alueen ulkopuolella"

Matematiikka sanoo, että lähde ei ole anturiensisi välillä. Mahdolliset syyt:
- Lähde on todella anturin linjan/tason ulkopuolella
- Yksi syötteistäsi on väärin
- Kalibrointinopeus on liian kaukana todellisuudesta

### Laskennan nopeuden vihje näyttää varoitusvärin

Implisiittinen äänennopeus syötteistäsi on kaukana mistä tahansa yleisestä materiaalista (alle 50 m/s tai yli 20 000 m/s). Tarkista syötteet — todennäköisesti kirjoitusvirhe tCal:ssa tai etäisyydessä.

### Materials-valitsin näyttää eri nopeuksia kuin odotettu

Tarkista Viitelämpötila Asetuksissa. Jos ei 20 °C, näytetyt nopeudet heijastavat lämpötilakompensointia. Sovellus näyttää "ref X @ 20°C" kompensoitujen nopeuksien alla, jotta voit tarkistaa.

### Historiamerkintä toistuu eri tuloksella

Vanhat historiamerkinnät, jotka on luotu ennen sovellusversio 1.75:tä, eivät välttämättä ole tallentaneet lämpötilaa. Jos mittasit ei-20 °C-lämpötilassa, toisto käyttää nykyistä asetusta. Aseta lämpötila manuaalisesti Asetuksissa ennen toistamista TAI mittaa uudelleen.

### Valokuvan merkit eivät ole missä odotan

Merkit sijoitetaan automaattisesti syötegeometrian perusteella. Vedä niitä säätääksesi. Merkkien säätäminen päivittää lähteen sijainnin valokuvan päällä — mutta EI muuta taustalla olevaa laskentatulosta.

### Varmuuskopiointi/Palautus epäonnistuu

Varmista, että käytät varmuuskopiotiedostoa, joka on luotu samalla tai uudemmalla sovellusversiolla. Vanhemmat varmuuskopiot voivat puuttua nykyisistä datakentistä.

### Palauta osto sanoo "ostoa ei löytynyt"

1. Vahvista, että olet kirjautunut samalle kauppatilille, jota käytit ostoon
2. Vahvista, että ostoa ei ole hyvitetty tai vanhentunut
3. Yritä asentaa ja asentaa sovellus uudelleen (osto on sidottu kauppatililiin, ei sovelluksen asennukseen)
4. Ota yhteyttä support@evdiag.net, jos ongelma jatkuu

### Numeerinen syöte hyppää odottamatta 0:aan

Suunnittelulla: kun lopetat fokuksen numeerisesta kentästä (napautat muualta), jos se on tyhjä, negatiivinen tai sisältää ei-numeerista tekstiä, se hyppää 0:aan. Estää hiljaa rikkoutuneet laskelmat vahingossa tyhjennetyistä syötteistä. Lämpötilasyöte on poikkeus (sen sijaan se rajoittuu -40/+200:aan).

### Tarvitsen lisää apua

Ota yhteyttä `support@evdiag.net`:iin:
- Laitteesi malli ja OS-versio
- Sovelluksen versio (Asetukset → sivun alaosa)
- Kuvaus siitä, mitä yritit
- Kuvakaappauksia, jos mahdollista

---

*NVH Source Locator on EVDiagin kehittämä. Vieraile osoitteessa https://evdiag.net päivityksiä ja resursseja varten.*
""",

'ro': """# NVH Source Locator — Ghidul utilizatorului

NVH Source Locator este un instrument de măsurare pentru localizarea surselor de zgomot și vibrații folosind TDOA (Time Difference of Arrival) din semnalele accelerometrelor capturate pe un osciloscop sau sistem de măsurare.

Acest ghid acoperă toate funcțiile. Pentru o reamintire rapidă, vezi **Referință rapidă**.

---

## Cuprins

1. [Cum funcționează](#how-it-works)
2. [Înainte de a începe](#before-you-start)
3. [Filele principale](#the-main-tabs)
4. [Modul 2-Sensor](#2-sensor-mode)
5. [Modul 3-Sensor](#3-sensor-mode)
6. [Moduri Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Fila Materials](#the-materials-tab)
8. [Compensarea temperaturii](#temperature-compensation)
9. [Adnotarea fotografiei](#photo-annotation)
10. [Rapoarte](#reports)
11. [Backup și restaurare](#backup-and-restore)
12. [Setări](#settings)
13. [Funcții Pro](#pro-features)
14. [Fila Help și tutoriale](#help-tab-and-tutorials)
15. [Depanare](#troubleshooting)

---

## Cum funcționează {#how-it-works}

Când o sursă de zgomot emite sunet sau vibrație, unda se deplasează prin material la o viteză cunoscută. Dacă plasezi două sau mai multe accelerometre pe material și măsori când unda ajunge la fiecare, diferența de timp îți spune unde este sursa.

NVH Source Locator preia:

- **Calibrare**: distanța dintre senzori și timpul necesar ca o undă să parcurgă acea distanță (folosit pentru a calcula viteza sunetului materialului)
- **Eveniment**: diferența de timp dintre senzorii care detectează evenimentul de zgomot/vibrație

Apoi calculează unde se află sursa în structură.

Cu cât folosești mai mulți senzori, cu atât poți localiza mai precis sursa:

- **2 senzori** → distanță de-a lungul unei linii
- **3 senzori** → poziție pe o suprafață 2D (X, Y)
- **4 senzori** → poziție în spațiul 3D (X, Y, Z)

---

## Înainte de a începe {#before-you-start}

Vei avea nevoie de:

- **Un osciloscop sau sistem de măsurare** care poate afișa diferența de timp dintre canalele accelerometrului în microsecunde (µs)
- **Cel puțin 2 accelerometre** fizic atașate la structură (mai mulți senzori = precizie mai mare)
- **O modalitate de a măsura distanța** între senzori (ruletă, șubler)
- **O modalitate de a declanșa o undă** într-o locație cunoscută pentru calibrare (impact de ciocan calibrat, lovitură de șurubelniță sau alt semnal cunoscut)

![Ecran principal cu fila 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Filele principale {#the-main-tabs}

Aplicația are file în partea de sus:

![Bara de file](../screenshots/02-tab-bar.png)

| Filă | Ce face | Când să folosești |
|---|---|---|
| **2-Sensor** | Localizare 1D a sursei de-a lungul unei linii între 2 senzori | Verificări rapide, structuri tip grindă. **Complet gratuit.** |
| **3-Sensor** | Localizare 2D a sursei folosind 3 senzori într-un triunghi | Cea mai generală utilizare, panouri și suprafețe |
| **3-Sen+** | 3-Sensor cu rezolvator supradeterminat de cele mai mici pătrate | Măsurători mai pretențioase, robust la zgomot |
| **4-Sensor** | Localizare 2D folosind două perechi (A-B + C-D) | Aranjamente rectangulare de senzori, verificare încrucișată |
| **4-Sen+** | Mod 2D avansat, 4 senzori în orice poziție | Geometrii nerectangulare, LSQ complet |
| **3D** | Localizare 3D a sursei folosind 4 senzori cu coordonate XYZ | Structuri complexe în spațiul 3D |
| **3D+** | 3D cu până la 6 senzori, LSQ supradeterminat | Geometrii foarte complexe, precizie maximă |
| **Materials** | Bibliotecă de viteză a sunetului + materiale personalizate | Selectează o dată pe sesiune de măsurare |
| **Help** | Tutoriale în aplicație și referință | Când ai nevoie de o reamintire rapidă |

> **Gratuit vs Pro**: Fila 2-Sensor este complet gratuită. Alte file sunt accesibile, dar au câmpuri specifice de intrare blocate pentru utilizatorii Pro (marcate cu o insignă de lacăt auriu). Atingerea unui câmp blocat afișează paywall-ul Pro.

Setările sunt accesate prin pictograma roată dințată ⚙ din colțul din dreapta sus (nu este o filă).

---

## Modul 2-Sensor {#2-sensor-mode}

Cea mai simplă măsurătoare: localizare a sursei de-a lungul unei linii între două accelerometre.

![Fila 2-Sensor](../screenshots/01-home-2sensor.png)

### Pasul 1: Aplică un material

Atinge fila Materials. Alege materialul din care este făcută structura ta (de exemplu, „Aluminiu", „Oțel, Mild (1020)"). Aplicația folosește viteza sunetului cunoscută a materialului pentru a completa automat câmpul de timp de calibrare.

Dacă materialul structurii tale nu este în listă, poți selecta temporar „Aer" și să suprascrii manual timpul de calibrare în pasul 2.

### Pasul 2: Introdu datele de calibrare

În fila 2-Sensor, vei vedea două secțiuni de perechi: **Perechea A–B** și **Perechea A–C** (doar A–B este necesar dacă ai doar 2 senzori).

Pentru fiecare pereche, completezi:

- **Distanța dintre senzori** (`d`): distanță fizică între senzori, în cm sau inci (setat în Setări)
- **Întârziere timp de calibrare** (`tCal`): timpul necesar unei unde să parcurgă distanța între senzori la viteza sunetului materialului — completat automat când selectezi un material, dar poți suprascrie

### Pasul 3: Introdu timpul evenimentului

- **Întârziere timp eveniment** (`tEvent`): diferența de timp între senzorii care detectează evenimentul de zgomot, în microsecunde
- **Primul senzor**: care senzor a auzit primul evenimentul (A sau B)

### Pasul 4: Citește rezultatul

Aplicația afișează poziția sursei ca o distanță de la senzorul A:
- Rezultat = 0: sursa este la senzorul A
- Rezultat = distanță: sursa este la senzorul B
- Rezultat între: sursa este între ei
- Rezultat în afară: sursa este dincolo de unul dintre senzori (toastul va avertiza)

Cardul de rezultat arată ambele distanțe (de la A, de la B) și indică care senzor este mai aproape.

### Pasul 5 (opțional): Adnotează o fotografie

Atinge **📷 Adnotează fotografie** pentru a face o fotografie a configurației tale. Aplicația suprapune markeri pentru senzorii A, B și sursă. Util pentru rapoarte.

---

## Modul 3-Sensor {#3-sensor-mode}

Localizează o sursă pe un plan 2D folosind trei senzori aranjați într-un triunghi.

![Fila 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configurare

Plasează trei senzori pe structura ta formând un triunghi. Echilateral, dreptunghic sau scalen — aplicația gestionează toate geometriile.

### Introdu datele

În secțiunea **Lungimile laturilor triunghiului**, introdu distanța fizică pentru toate cele trei laturi (A–B, A–C, B–C).

Pentru fiecare pereche (A–B și A–C), introdu:
- **tCal**: timp de calibrare (auto-completat din material)
- **tEvent**: diferența de timp măsurată pentru evenimentul de zgomot
- **Primul senzor**: care a auzit primul

### Citește rezultatul

Aplicația afișează poziția sursei ca coordonate X, Y relative la senzorul A (senzorul A în origine, senzorul B pe axa X). Vizualizarea arată toți cei trei senzori și locația sursei.

![Rezultat triunghi](../screenshots/04-triangle-result.png)

---

## Moduri Pro+ {#pro-modes}

Mai multe file avansate oferă rezolvatori supradeterminați și dimensionalitate mai mare:

### 3-Sen+ (Pro)

Aceeași configurare triunghiulară ca 3-Sensor, dar calibrează ȘI măsoară toate cele trei perechi (A–B, A–C, B–C). Rezolvatorul folosește toate cele 3 TDOA-uri într-o ajustare a celor mai mici pătrate — mai robust la zgomotul de măsurare și materialele anizotrope. Reziduurile pe pereche sunt raportate astfel încât să poți detecta măsurători inconsistente.

### 4-Sensor

Plasează patru senzori în jurul zonei:
- **A–B** = pereche orizontală (părți stânga/dreapta)
- **C–D** = pereche verticală (părți sus/jos)

Rulează perechea A–B mai întâi (orizontal), apoi perechea C–D (vertical). Harta 2D arată intersecția. Fiecare pereche este calibrată separat — util când materialul variază prin structură.

### 4-Sen+ (2D Avansat)

Patru senzori în orice poziție (nu forțat rectangulară). Asociază A cu fiecare dintre B, C, D și calibrează separat. Rezolvatorul supradeterminat al celor mai mici pătrate face media zgomotului de măsurare pe pereche și raportează reziduurile pe pereche.

### 3D

Măsurătoare 3D completă cu 4 senzori plasați în spațiul 3D. Introdu coordonatele (X, Y, Z) ale fiecărui senzor, plus timpurile de calibrare și eveniment pentru fiecare pereche (A–B, A–C, A–D).

### 3D+ (Pro)

Ca 3D, dar suportă până la **6 senzori** (A până la F) cu LSQ supradeterminat. Precizie maximă pentru geometrii 3D complexe.

---

## Fila Materials {#the-materials-tab}

Bibliotecă de materiale inginerești comune cu viteza sunetului cunoscută la 20 °C.

![Fila Materials](../screenshots/05-materials-tab.png)

### Lista materialelor

Lista include aer, fluide, cauciucuri, polimeri, lemne, sticle și metale. Vitezele variază de la ~340 m/s (aer) până la ~13.000 m/s (unele metale la temperatura camerei).

### Materiale încorporate cu compensare de temperatură

14 metale frecvent utilizate includ date despre coeficientul de temperatură. Când Temperatura de referință din Setări diferă de 20 °C, aplicația ajustează automat vitezele acestor materiale:

- Aluminiu
- Oțel, Mild (1020)
- Oțel inoxidabil (304)
- Fier (turnat)
- Fier
- Cupru
- Alamă
- Bronz
- Titan
- Magneziu
- Plumb
- Zinc
- Nichel
- Wolfram

Materialele cu compensare arată două valori în selector: **viteza compensată** (mare, proeminentă) și **viteza de referință la 20 °C** (mică, gri dedesubt).

Materialele fără compensare arată **„ref only"** cu italic — viteza lor listată este folosită așa cum este, indiferent de temperatură.

### Materiale personalizate

Dacă măsori o calibrare în fila 2-Sensor, poți salva rezultatul ca material personalizat. După o măsurătoare 2-sensor reușită, caută opțiunea de a salva viteza derivată sub un nume la alegerea ta.

Materialele personalizate stochează viteza măsurată in-situ; ele nu aplică niciodată compensarea temperaturii (viteza a fost deja măsurată la temperatura testului).

### Favorite

Atinge steaua de lângă orice material pentru a-l marca ca favorit. Favoritele apar în partea de sus a listei pentru acces rapid.

### Căutare

Folosește bara de căutare din partea de sus pentru a filtra materialele după nume. Căutarea potrivește atât numele canonice englezești, cât și numele de afișare traduse.

---

## Compensarea temperaturii {#temperature-compensation}

Viteza sunetului în materiale se schimbă cu temperatura. În testarea NVH auto, asta contează: un compartiment motor la 80 °C, o cabină rece la -10 °C sau o zonă a galeriei de eșapament la 200 °C se comportă diferit de condițiile de laborator la temperatura camerei.

### Setarea temperaturii

Deschide Setări (pictogramă ⚙) → Temperatură de referință. Introdu temperatura mediului tău de testare în °C (interval -40 la +200).

![Panou Setări](../screenshots/06-settings.png)

### Ce se întâmplă când temperatura ≠ 20 °C

- Câmpurile de timp de calibrare se autocompletează cu viteza ajustată la temperatură
- Selectorul Materials afișează proeminent viteza ajustată
- Un toast confirmă: *„Aluminiu aplicat (6.284 m/s @ 60 °C) — N pereche(i) actualizată(e)"*
- Indiciul „Cel mai apropiat material" compară cu vitezele ajustate la temperatură
- Intrările salvate ale istoricului înregistrează temperatura activă
- Rapoartele includ o linie de subsol: *„Temperatura de referință: 60 °C, compensare aplicată"*

### Resetare la lansarea aplicației

Temperatura de referință **se resetează întotdeauna la 20 °C** când lansezi aplicația. Aceasta împiedică setările învechite de la o sesiune anterioară de măsurare să afecteze tăcut munca de astăzi. O mică notă cu italic în Setări îți reamintește acest comportament.

Dacă vrei să redai o măsurătoare istorică la temperatura sa originală, doar atinge intrarea — temperatura este restaurată automat.

### Materiale fără compensare

Majoritatea materialelor non-metalice nu au coeficienți de temperatură publicați fiabili. Aplicația afișează o insignă **„ref only"** pentru acestea — viteza lor listată este folosită indiferent de setarea temperaturii. Dacă ai nevoie de măsurători precise la temperaturi non-camerale pentru aceste materiale, efectuează o calibrare in-situ și salvează rezultatul ca material personalizat.

---

## Adnotarea fotografiei {#photo-annotation}

După un calcul reușit, atinge butonul **📷 Adnotează fotografie** pentru a suprapune markeri de senzor și sursă pe o fotografie a configurației tale.

![Adnotarea fotografiei](../screenshots/08-photo-annotation.png)

### Flux

1. Atinge **Adnotează fotografie** — camera sistemului se deschide
2. Fă o fotografie a plasării senzorilor
3. Aplicația încarcă fotografia în suprapunerea de adnotări
4. Markerii senzorilor (A, B, C, D, E, F după caz — până la 6 senzori) și markerul sursei se plasează automat pe baza calculului tău
5. Trage orice marker pentru a ajusta fin poziția. Pe măsură ce ajustezi, poziția sursei este recalculată din pozițiile corectate ale senzorilor
6. Atinge **Salvează** pentru a păstra sau **Reia** pentru a încerca din nou

Fotografia adnotată este inclusă automat în rapoartele PDF.

---

## Rapoarte {#reports}

Atinge butonul **Tipărește rezultat** pe orice ecran de rezultat pentru a genera un raport formatat.

![Raport PDF](../screenshots/09-pdf-report.png)

### Conținutul raportului

- Antet (personalizabil în Setări → Antet raport)
- Titlul măsurătorii și marca temporală
- Toate valorile de intrare într-un tabel ordonat
- Rezultatul calculului
- Text de concluzie
- Vizualizare (grafic de geometrie)
- Fotografie adnotată (dacă ai făcut una)
- Linia subsolului pentru temperatură (dacă compensarea era activă)
- Numărul paginii și linia de credit

### Format de ieșire

- **Android**: generare nativă PDF, salvează pe telefon sau partajează
- **iOS**: dialog de tipărire al sistemului → salvează ca PDF, AirPrint sau partajează

### Personalizarea antetului

Setări → Antet raport. Introdu numele companiei tale, numele laboratorului, informații despre proiect sau orice vrei în partea de sus a fiecărui raport.

---

## Backup și restaurare {#backup-and-restore}

Salvează toate materialele tale personalizate, favoritele, setările și istoricul într-un singur fișier. Transfer între dispozitive.

### Backup

Setări → **Backup** → atinge „Salvează fișier backup". Aplicația generează un fișier JSON și deschide fișa de partajare a telefonului tău. Salvează-l pe unitatea ta cloud (Google Drive, iCloud, OneDrive), trimite-l prin e-mail ție însuți sau transferă-l în orice mod dorești.

### Restaurare

Setări → **Restaurare** → alege fișierul de backup din stocarea telefonului tău. Aplicația importă materiale personalizate, favorite, istoric și setări.

⚠️ **Restaurarea înlocuiește datele tale actuale.** Dacă ai măsurători importante pe dispozitivul actual, fă mai întâi backup pentru ele înainte de a restaura dintr-un backup diferit.

---

## Setări {#settings}

Acces prin pictograma roată dințată ⚙ din colțul din dreapta sus. Setări este un modal, nu o filă.

![Setări](../screenshots/06-settings.png)

| Setare | Ce controlează |
|---|---|
| **Upgrade la Pro** | Cumpără sau află despre funcțiile Pro ($19,99) |
| **Limbă** | Limba de afișare a aplicației (30 suportate) |
| **Temă** | Luminoasă, Întunecată sau Auto (urmează sistemul) |
| **Unitate de distanță** | cm sau inci |
| **Temperatură de referință** | Temperatură activă pentru compensare, -40 până la +200 °C |
| **Antet raport** | Text personalizat în partea de sus a rapoartelor generate |
| **Backup** | Exportă toate datele într-un fișier |
| **Restaurare** | Importă datele dintr-un fișier backup |
| **Restaurează cumpărarea** | Reachiziționează Pro pe un dispozitiv nou |

---

## Funcții Pro {#pro-features}

NVH Source Locator folosește un **model freemium cu blocare per funcție**:

- **Gratuit**: Fila 2-Sensor este complet funcțională fără limite
- **Pro**: Toate celelalte file au câmpuri specifice de intrare blocate. Paywall-ul apare când un utilizator gratuit atinge un câmp blocat

### Ce este blocat

Câmpurile necesare Pro sunt împrăștiate prin:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Moduri 3D și 3D+
- Backup și Restaurare
- Rapoarte PDF
- Materiale personalizate
- Adnotarea fotografiei

Un utilizator gratuit poate DESCHIDE orice filă și VEDEA interfața. Pur și simplu nu poate introduce valori în câmpurile de intrare blocate de Pro.

![Câmp blocat de Pro](../screenshots/11-pro-locked-field.png)

### Paywall-ul

![Paywall](../screenshots/07-paywall.png)

Când un utilizator gratuit atinge un câmp blocat, paywall-ul glisează arătând:
- Pictograma aplicației cu insignă PRO
- Listă de funcții
- Buton de deblocare cu preț ($19,99 implicit; poate varia în funcție de regiune)
- Răscumpărare cod promoțional (doar Android — iOS folosește fluxul separat Offer Code al Apple)
- Link promoțional opțional către canalele comunității

### Cumpărarea Pro

Atinge orice câmp blocat, sau atinge **Upgrade la Pro** în Setări. Folosește sistemul oficial de plată al platformei tale (Google Play pe Android, Apple App Store pe iOS).

### Restaurarea Pro pe un dispozitiv nou

Dacă ai cumpărat pe un dispozitiv și vrei Pro pe altul (același cont):

1. Conectează-te la **același** cont Google (Android) sau Apple ID (iOS) pe care l-ai folosit pentru cumpărare
2. Deschide NVH Source Locator pe noul dispozitiv
3. Mergi la Setări → **Restaurează cumpărarea**
4. Aplicația verifică cu înregistrările de cumpărare ale platformei și deblochează Pro

### Auto-restaurare la lansare

Dacă răscumperi un cod promoțional în Google Play Store sau App Store în timp ce NVH Source Locator rulează în fundal, revenirea la aplicație detectează automat noua cumpărare și deblochează Pro — nu este necesară Restaurare manuală.

### Răscumpărare cod promoțional

**Android**: un buton „Ai un cod promoțional Google Play?" în paywall deschide fluxul de răscumpărare Google Play cu codul tău precompletat.

**iOS**: Politica App Store 3.1.1 cere răscumpărare prin fluxul oficial „Răscumpără cod" al Apple. Butonul Google Play este ascuns pe iOS. Caută „Răscumpără cod App Store" în Setări în schimb.

---

## Fila Help și tutoriale {#help-tab-and-tutorials}

Fila **Help** include tutoriale în aplicație, ghiduri de cele mai bune practici și informații de referință.

![Fila Help](../screenshots/10-help-tab.png)

Subiecte acoperite:
- Ce echipament ai nevoie
- Cum să plasezi senzorii pentru cea mai bună precizie
- Sfaturi de calibrare
- Scenarii comune de măsurare
- Sfaturi pentru triangulare și plasări 3D
- Direcționarea cablurilor și calitatea semnalului

---

## Depanare {#troubleshooting}

### Rezultatul calculului este greșit sau nu are sens

1. Verifică-ți calibrarea. `tCal` autocompletat presupune viteza publicată a materialului — materialele reale variază. Cea mai precisă calibrare este in-situ: atinge o locație cunoscută și lasă aplicația să deducă viteza reală.
2. Verifică setarea **Primul senzor** — care senzor a auzit primul evenimentul contează pentru matematică.
3. Verifică-ți măsurătorile de distanță. Erorile de câțiva mm se propagă.

### Toast spune „Rezultat în afara intervalului"

Matematica spune că sursa nu este între senzorii tăi. Cauze posibile:
- Sursa este de fapt în afara liniei/planului senzorilor
- Una dintre intrările tale este greșită
- Viteza de calibrare este prea departe de realitate

### Indiciul vitezei de calcul afișează o culoare de avertisment

Viteza sunetului implicită din intrările tale este departe de orice material comun (sub 50 m/s sau peste 20.000 m/s). Verifică-ți intrările — probabil o eroare de tipar în tCal sau distanță.

### Selectorul Materials arată viteze diferite decât așteptat

Verifică Temperatura de referință în Setări. Dacă nu este 20 °C, vitezele afișate reflectă compensarea temperaturii. Aplicația afișează „ref X @ 20°C" sub vitezele compensate astfel încât să poți verifica.

### Intrarea din istoric se redă cu un rezultat diferit

Intrările vechi din istoric create înainte de versiunea 1.75 a aplicației ar putea să nu fi stocat temperatura. Dacă ai făcut măsurătoarea la o temperatură non-20 °C, redarea va folosi setarea actuală. Setează manual temperatura în Setări înainte de redare, SAU remăsoară.

### Markerii de adnotare a fotografiei nu sunt acolo unde mă aștept

Markerii se plasează automat pe baza geometriei de intrare. Trage-i pentru a ajusta. Ajustarea markerilor actualizează poziția sursei în suprapunerea fotografiei — dar NU modifică rezultatul de calcul subiacent.

### Backup/Restaurare eșuează

Asigură-te că folosești un fișier de backup generat de aceeași sau o versiune mai nouă a aplicației. Fișierele backup mai vechi ar putea lipsi de câmpuri actuale de date.

### Restaurează cumpărarea spune „nicio cumpărare găsită"

1. Verifică că ești conectat la același cont de magazin pe care l-ai folosit pentru cumpărare
2. Verifică că cumpărarea nu a fost rambursată sau expirată
3. Încearcă să dezinstalezi și să reinstalezi aplicația (cumpărarea este legată de contul de magazin, nu de instalarea aplicației)
4. Contactează support@evdiag.net dacă persistă

### Intrarea numerică se schimbă neașteptat la 0

Prin design: când părăsești un câmp numeric (atingi în altă parte), dacă este gol, negativ sau conține text non-numeric, se schimbă la 0. Previne calcule tăcut stricate din intrări șterse accidental. Intrarea de temperatură este exceptată (în schimb se limitează la -40/+200).

### Am nevoie de mai mult ajutor

Contactează `support@evdiag.net` cu:
- Modelul dispozitivului tău și versiunea OS
- Versiunea aplicației (Setări → partea de jos a paginii)
- Descrierea a ceea ce ai încercat
- Capturi de ecran dacă este posibil

---

*NVH Source Locator este dezvoltat de EVDiag. Vizitează https://evdiag.net pentru actualizări și resurse.*
""",

'tr': """# NVH Source Locator — Kullanım Kılavuzu

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
""",

}
