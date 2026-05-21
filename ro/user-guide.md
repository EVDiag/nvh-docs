# NVH Source Locator — Ghidul utilizatorului

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

## Cum funcționează

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

## Înainte de a începe

Vei avea nevoie de:

- **Un osciloscop sau sistem de măsurare** care poate afișa diferența de timp dintre canalele accelerometrului în microsecunde (µs)
- **Cel puțin 2 accelerometre** fizic atașate la structură (mai mulți senzori = precizie mai mare)
- **O modalitate de a măsura distanța** între senzori (ruletă, șubler)
- **O modalitate de a declanșa o undă** într-o locație cunoscută pentru calibrare (impact de ciocan calibrat, lovitură de șurubelniță sau alt semnal cunoscut)

![Ecran principal cu fila 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Filele principale

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

## Modul 2-Sensor

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

## Modul 3-Sensor

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

## Moduri Pro+

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

## Fila Materials

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

## Compensarea temperaturii

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

## Adnotarea fotografiei

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

## Rapoarte

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

## Backup și restaurare

Salvează toate materialele tale personalizate, favoritele, setările și istoricul într-un singur fișier. Transfer între dispozitive.

### Backup

Setări → **Backup** → atinge „Salvează fișier backup". Aplicația generează un fișier JSON și deschide fișa de partajare a telefonului tău. Salvează-l pe unitatea ta cloud (Google Drive, iCloud, OneDrive), trimite-l prin e-mail ție însuți sau transferă-l în orice mod dorești.

### Restaurare

Setări → **Restaurare** → alege fișierul de backup din stocarea telefonului tău. Aplicația importă materiale personalizate, favorite, istoric și setări.

⚠️ **Restaurarea înlocuiește datele tale actuale.** Dacă ai măsurători importante pe dispozitivul actual, fă mai întâi backup pentru ele înainte de a restaura dintr-un backup diferit.

---

## Setări

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

## Funcții Pro

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

## Fila Help și tutoriale

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

## Depanare

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
