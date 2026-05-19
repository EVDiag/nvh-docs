# NVH Source Locator — Brukerhåndbok

NVH Source Locator er et måleverktøy for å lokalisere støy- og vibrasjonskilder ved hjelp av TDOA (Time Difference of Arrival) fra akselerometersignaler fanget på et oscilloskop eller målesystem.

Denne håndboken dekker alle funksjoner. For en rask oppfriskning, se `quick-reference.md`.

> **Merknad om skjermbilder**: Dette dokumentet bruker plassholder-skjermbilder fra appen. Erstatt hvert `../screenshots/*.png` med ekte enhets-skjermbilder etter hvert som du tar dem.

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

## Hvordan det fungerer

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

## Før du starter

Du trenger:

- **Et oscilloskop eller målesystem** som kan vise tidsforskjellen mellom akselerometerkanaler i mikrosekunder (µs)
- **Minst 2 akselerometre** fysisk festet til strukturen (flere sensorer = høyere nøyaktighet)
- **En måte å måle avstand** mellom sensorene (målebånd, skyvelære)
- **En måte å utløse en bølge** på et kjent sted for kalibrering (kalibrert hammerslag, skrutrekker-banking eller annet kjent signal)

![Hjemmeskjerm med 2-Sensor-fane](../screenshots/01-home-2sensor.png)

---

## Hovedfanene

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

## 2-Sensor-modus

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

## 3-Sensor-modus

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

## Pro+-moduser

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

## Materials-fanen

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

## Temperaturkompensasjon

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

## Fotomerknad

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

## Rapporter

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

## Sikkerhetskopiering og gjenoppretting

Lagre alle de tilpassede materialene, favorittene, innstillingene og historikken til en enkelt fil. Overfør mellom enheter.

### Sikkerhetskopiering

Innstillinger → **Sikkerhetskopiering** → trykk på "Lagre sikkerhetskopifil". Appen genererer en JSON-fil og åpner telefonens delingsark. Lagre den til skystasjonen din (Google Drive, iCloud, OneDrive), e-post den til deg selv eller overfør på hvilken som helst måte.

### Gjenopprett

Innstillinger → **Gjenopprett** → velg sikkerhetskopifilen fra telefonens lagring. Appen importerer tilpassede materialer, favoritter, historikk og innstillinger.

⚠️ **Gjenoppretting erstatter dine nåværende data.** Hvis du har viktige målinger på den nåværende enheten, sikkerhetskopier dem først før du gjenoppretter fra en annen sikkerhetskopi.

---

## Innstillinger

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

## Pro-funksjoner

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

## Help-fanen og veiledninger

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

## Feilsøking

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
