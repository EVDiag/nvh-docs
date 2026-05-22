"""User Guide translations — batch 1.

4 languages: de, es, fr, it.
Each is a full translation of the English user-guide.md, preserving
markdown structure, image references, code blocks, tables, etc.
"""

USER_GUIDE_TRANSLATIONS = {

'de': """# NVH Source Locator — Benutzerhandbuch

NVH Source Locator ist ein Messwerkzeug zur Lokalisierung von Geräusch- und Vibrationsquellen mithilfe von TDOA (Time Difference of Arrival) aus Beschleunigungssensorsignalen, die auf einem Oszilloskop oder Messsystem erfasst werden.

Dieses Handbuch deckt alle Funktionen ab. Eine kurze Auffrischung finden Sie in **Kurzanleitung**.

---

## Inhaltsverzeichnis

1. [Funktionsweise](#how-it-works)
2. [Bevor Sie beginnen](#before-you-start)
3. [Die Haupt-Registerkarten](#the-main-tabs)
4. [2-Sensor-Modus](#2-sensor-mode)
5. [3-Sensor-Modus](#3-sensor-mode)
6. [Pro+-Modi (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Die Materials-Registerkarte](#the-materials-tab)
8. [Temperaturkompensation](#temperature-compensation)
9. [Fotoannotation](#photo-annotation)
10. [Berichte](#reports)
11. [Backup und Wiederherstellung](#backup-and-restore)
12. [Einstellungen](#settings)
13. [Pro-Funktionen](#pro-features)
14. [Help-Registerkarte und Tutorials](#help-tab-and-tutorials)
15. [Fehlerbehebung](#troubleshooting)

---

## Funktionsweise {#how-it-works}

Wenn eine Geräuschquelle einen Schall oder eine Vibration erzeugt, breitet sich die Welle mit einer bekannten Geschwindigkeit durch das Material aus. Wenn Sie zwei oder mehr Beschleunigungssensoren auf dem Material platzieren und messen, wann die Welle an jedem ankommt, sagt Ihnen die Zeitdifferenz, wo sich die Quelle befindet.

NVH Source Locator nimmt:

- **Kalibrierung**: den Abstand zwischen den Sensoren und die Zeit, die eine Welle benötigt, um diese Distanz zurückzulegen (zur Berechnung der Schallgeschwindigkeit im Material verwendet)
- **Ereignis**: die Zeitdifferenz zwischen Sensoren, die das Geräusch-/Vibrationsereignis erfassen

Dann berechnet sie, wo sich die Quelle in der Struktur befindet.

Je mehr Sensoren Sie verwenden, desto genauer können Sie die Quelle lokalisieren:

- **2 Sensoren** → Abstand entlang einer Linie
- **3 Sensoren** → Position auf einer 2D-Oberfläche (X, Y)
- **4 Sensoren** → Position im 3D-Raum (X, Y, Z)

---

## Bevor Sie beginnen {#before-you-start}

Sie benötigen:

- **Ein Oszilloskop oder Messsystem**, das die Zeitdifferenz zwischen Beschleunigungssensor-Kanälen in Mikrosekunden (µs) anzeigen kann
- **Mindestens 2 Beschleunigungssensoren**, die physisch an der Struktur angebracht sind (mehr Sensoren = höhere Genauigkeit)
- **Eine Möglichkeit, den Abstand** zwischen den Sensoren zu messen (Maßband, Messschieber)
- **Eine Möglichkeit, eine Welle auszulösen** an einer bekannten Stelle zur Kalibrierung (kalibrierter Hammerschlag, Schraubenzieher-Klopfen oder anderes bekanntes Signal)

![Startbildschirm mit 2-Sensor-Registerkarte](../screenshots/01-home-2sensor.png)

---

## Die Haupt-Registerkarten {#the-main-tabs}

Die App hat Registerkarten oben:

![Registerkarten-Leiste](../screenshots/02-tab-bar.png)

| Registerkarte | Funktion | Wann zu verwenden |
|---|---|---|
| **2-Sensor** | 1D-Quellortung entlang einer Linie zwischen 2 Sensoren | Schnellprüfungen, balkenartige Strukturen. **Vollständig kostenlos.** |
| **3-Sensor** | 2D-Quellortung mit 3 Sensoren in einem Dreieck | Allgemeinster Anwendungsfall, Platten und Oberflächen |
| **3-Sen+** | 3-Sensor mit überbestimmtem Kleinste-Quadrate-Solver | Anspruchsvollere Messungen, störungsrobust |
| **4-Sensor** | 2D-Lokalisierung mit zwei Paaren (A-B + C-D) | Rechteckige Sensorlayouts, Gegenprüfung |
| **4-Sen+** | Erweiterter 2D-Modus, 4 Sensoren in beliebigen Positionen | Nicht-rechteckige Geometrien, voller LSQ |
| **3D** | 3D-Quellortung mit 4 Sensoren mit XYZ-Koordinaten | Komplexe Strukturen im 3D-Raum |
| **3D+** | 3D mit bis zu 6 Sensoren, überbestimmtes LSQ | Sehr komplexe Geometrien, maximale Präzision |
| **Materials** | Schallgeschwindigkeits-Bibliothek + benutzerdefinierte Materialien | Einmal pro Messsitzung auswählen |
| **Help** | In-App-Tutorials und Referenz | Wenn Sie eine schnelle Auffrischung benötigen |

> **Kostenlos vs. Pro**: Die 2-Sensor-Registerkarte ist vollständig kostenlos. Andere Registerkarten sind zugänglich, haben aber bestimmte Eingabefelder, die für Pro-Benutzer gesperrt sind (mit einem goldenen Schloss-Abzeichen markiert). Das Antippen eines gesperrten Felds zeigt die Pro-Paywall.

Die Einstellungen werden über das ⚙-Zahnradsymbol in der oberen rechten Ecke aufgerufen (keine Registerkarte).

---

## 2-Sensor-Modus {#2-sensor-mode}

Die einfachste Messung: Quellortung entlang einer Linie zwischen zwei Beschleunigungssensoren.

![2-Sensor-Registerkarte](../screenshots/01-home-2sensor.png)

### Schritt 1: Material anwenden

Tippen Sie auf die Materials-Registerkarte. Wählen Sie das Material, aus dem Ihre Struktur besteht (z. B. „Aluminium", „Stahl, Mild (1020)"). Die App verwendet die bekannte Schallgeschwindigkeit des Materials, um das Kalibrierungszeitfeld automatisch zu füllen.

Wenn das Material Ihrer Struktur nicht in der Liste enthalten ist, können Sie vorübergehend „Luft" auswählen und die Kalibrierungszeit in Schritt 2 manuell überschreiben.

### Schritt 2: Kalibrierungsdaten eingeben

Auf der 2-Sensor-Registerkarte sehen Sie zwei Paar-Abschnitte: **Paar A–B** und **Paar A–C** (nur A–B ist erforderlich, wenn Sie nur 2 Sensoren haben).

Für jedes Paar geben Sie ein:

- **Sensorabstand** (`d`): physischer Abstand zwischen Sensoren, in cm oder Zoll (in den Einstellungen festgelegt)
- **Kalibrierungszeitverzögerung** (`tCal`): Zeit für eine Welle, sich zwischen den Sensoren mit der Schallgeschwindigkeit des Materials zu bewegen — wird automatisch ausgefüllt, wenn Sie ein Material auswählen, kann aber überschrieben werden

### Schritt 3: Ereigniszeit eingeben

- **Ereigniszeitverzögerung** (`tEvent`): Zeitdifferenz zwischen Sensoren, die das Geräuschereignis erfassen, in Mikrosekunden
- **Erster Sensor**: welcher Sensor das Ereignis zuerst gehört hat (A oder B)

### Schritt 4: Ergebnis ablesen

Die App zeigt die Quellposition als Abstand vom Sensor A:
- Ergebnis = 0: Quelle befindet sich bei Sensor A
- Ergebnis = Abstand: Quelle befindet sich bei Sensor B
- Ergebnis dazwischen: Quelle befindet sich zwischen ihnen
- Ergebnis außerhalb: Quelle befindet sich jenseits eines der Sensoren (Toast warnt)

Die Ergebniskarte zeigt beide Entfernungen (von A, von B) und zeigt an, welcher Sensor näher ist.

### Schritt 5 (optional): Foto annotieren

Tippen Sie auf **📷 Foto annotieren**, um ein Foto Ihres Aufbaus aufzunehmen. Die App überlagert Markierungen für Sensoren A, B und die Quelle. Nützlich für Berichte.

---

## 3-Sensor-Modus {#3-sensor-mode}

Lokalisiert eine Quelle auf einer 2D-Ebene mit drei in einem Dreieck angeordneten Sensoren.

![3-Sensor-Registerkarte](../screenshots/03-3sensor-tab.png)

### Aufbau

Platzieren Sie drei Sensoren auf Ihrer Struktur, die ein Dreieck bilden. Gleichseitig, rechtwinklig oder ungleichseitig — die App bewältigt alle Geometrien.

### Daten eingeben

Geben Sie im Abschnitt **Dreiecksseitenlängen** den physischen Abstand für alle drei Seiten ein (A–B, A–C, B–C).

Für jedes Paar (A–B und A–C) geben Sie ein:
- **tCal**: Kalibrierungszeit (automatisch aus Material ausgefüllt)
- **tEvent**: gemessene Zeitdifferenz für das Geräuschereignis
- **Erster Sensor**: welcher es zuerst gehört hat

### Ergebnis ablesen

Die App zeigt die Quellposition als X-, Y-Koordinaten relativ zum Sensor A (Sensor A im Ursprung, Sensor B auf der X-Achse). Die Visualisierung zeigt alle drei Sensoren und die Quellposition.

![Dreiecksergebnis](../screenshots/04-triangle-result.png)

---

## Pro+-Modi {#pro-modes}

Mehrere fortgeschrittene Registerkarten bieten überbestimmte Solver und höhere Dimensionalität:

### 3-Sen+ (Pro)

Gleicher Dreiecksaufbau wie 3-Sensor, aber kalibrieren UND messen Sie alle drei Paare (A–B, A–C, B–C). Der Solver verwendet alle 3 TDOAs in einer Kleinste-Quadrate-Anpassung — robuster gegenüber Messrauschen und anisotropen Materialien. Paarweise Residuen werden gemeldet, damit Sie inkonsistente Messungen erkennen können.

### 4-Sensor

Platzieren Sie vier Sensoren um den Bereich:
- **A–B** = horizontales Paar (linke/rechte Seiten)
- **C–D** = vertikales Paar (obere/untere Seiten)

Führen Sie zuerst das A–B-Paar (horizontal) und dann das C–D-Paar (vertikal) aus. Die 2D-Karte zeigt den Schnittpunkt. Jedes Paar wird separat kalibriert — nützlich, wenn das Material über die Struktur variiert.

### 4-Sen+ (Erweitertes 2D)

Vier Sensoren in beliebigen Positionen (nicht zwangsläufig rechteckig). Paaren Sie A mit jedem von B, C, D und kalibrieren Sie separat. Der überbestimmte Kleinste-Quadrate-Solver mittelt das paarweise Messrauschen aus und meldet paarweise Residuen.

### 3D

Vollständige 3D-Messung mit 4 Sensoren im 3D-Raum platziert. Geben Sie für jeden Sensor die (X, Y, Z)-Koordinaten sowie Kalibrierungs- und Ereigniszeiten für jedes Paar (A–B, A–C, A–D) ein.

### 3D+ (Pro)

Wie 3D, aber unterstützt bis zu **6 Sensoren** (A bis F) mit überbestimmtem LSQ. Maximale Präzision für komplexe 3D-Geometrien.

---

## Die Materials-Registerkarte {#the-materials-tab}

Bibliothek gängiger technischer Materialien mit bekannter Schallgeschwindigkeit bei 20 °C.

![Materials-Registerkarte](../screenshots/05-materials-tab.png)

### Materialliste

Die Liste umfasst Luft, Flüssigkeiten, Gummi, Polymere, Holz, Glas und Metalle. Die Geschwindigkeiten reichen von ~340 m/s (Luft) bis ~13.000 m/s (einige Metalle bei Raumtemperatur).

### Eingebaute Materialien mit Temperaturkompensation

14 häufig verwendete Metalle enthalten Temperaturkoeffizientendaten. Wenn die Referenztemperatur in den Einstellungen von 20 °C abweicht, passt die App die Geschwindigkeiten dieser Materialien automatisch an:

- Aluminium
- Stahl, Mild (1020)
- Edelstahl (304)
- Eisen (Guss)
- Eisen
- Kupfer
- Messing
- Bronze
- Titan
- Magnesium
- Blei
- Zink
- Nickel
- Wolfram

Materialien mit Kompensation zeigen zwei Werte im Picker: die **kompensierte Geschwindigkeit** (groß, prominent) und die **Referenzgeschwindigkeit bei 20 °C** (klein, grau darunter).

Materialien ohne Kompensation zeigen **„ref only"** in Kursivschrift an — ihre gelistete Geschwindigkeit wird unabhängig von der Temperatur unverändert verwendet.

### Benutzerdefinierte Materialien

Wenn Sie eine Kalibrierung auf der 2-Sensor-Registerkarte messen, können Sie das Ergebnis als benutzerdefiniertes Material speichern. Nach einer erfolgreichen 2-Sensor-Messung suchen Sie nach der Option, die abgeleitete Geschwindigkeit unter einem Namen Ihrer Wahl zu speichern.

Benutzerdefinierte Materialien speichern die in-situ gemessene Geschwindigkeit; sie wenden niemals eine Temperaturkompensation an (die Geschwindigkeit wurde bereits bei der Testtemperatur gemessen).

### Favoriten

Tippen Sie auf den Stern neben einem Material, um es als Favorit zu markieren. Favoriten erscheinen oben in der Liste für schnellen Zugriff.

### Suche

Verwenden Sie die Suchleiste oben, um Materialien nach Namen zu filtern. Die Suche stimmt sowohl mit englischen kanonischen Namen als auch mit übersetzten Anzeigenamen überein.

---

## Temperaturkompensation {#temperature-compensation}

Die Schallgeschwindigkeit in Materialien ändert sich mit der Temperatur. Im automobilen NVH-Test ist dies wichtig: ein Motorraum bei 80 °C, eine kalt eingelagerte Kabine bei -10 °C oder ein Auspuffkrümmerbereich bei 200 °C verhalten sich alle anders als bei Raumtemperatur-Laborbedingungen.

### Temperatur einstellen

Öffnen Sie Einstellungen (⚙-Symbol) → Referenztemperatur. Geben Sie die Temperatur Ihrer Testumgebung in °C ein (Bereich -40 bis +200).

![Einstellungsfenster](../screenshots/06-settings.png)

### Was passiert, wenn Temperatur ≠ 20 °C

- Kalibrierungszeitfelder werden automatisch mit der temperaturangepassten Geschwindigkeit ausgefüllt
- Der Materials-Picker zeigt die angepasste Geschwindigkeit prominent an
- Ein Toast bestätigt: *„Aluminium angewendet (6.284 m/s @ 60 °C) — N Paar(e) aktualisiert"*
- Der Hinweis „Nächstes Material" vergleicht mit temperaturangepassten Geschwindigkeiten
- Gespeicherte Verlaufseinträge zeichnen die aktive Temperatur auf
- Berichte enthalten eine Fußzeile: *„Referenztemperatur: 60 °C, Kompensation angewendet"*

### Zurücksetzen beim App-Start

Die Referenztemperatur **wird immer auf 20 °C zurückgesetzt**, wenn Sie die App starten. Dies verhindert, dass veraltete Einstellungen aus einer vergangenen Messsitzung die heutige Arbeit stillschweigend beeinflussen. Ein kleiner kursiver Hinweis in den Einstellungen erinnert Sie an dieses Verhalten.

Wenn Sie eine historische Messung bei ihrer ursprünglichen Temperatur abspielen möchten, tippen Sie einfach auf den Eintrag — die Temperatur wird automatisch wiederhergestellt.

### Materialien ohne Kompensation

Die meisten nicht-metallischen Materialien haben keine zuverlässigen veröffentlichten Temperaturkoeffizienten. Die App zeigt für diese ein **„ref only"**-Abzeichen an — ihre gelistete Geschwindigkeit wird unabhängig von der Temperatureinstellung verwendet. Wenn Sie genaue Messungen bei nicht-Raumtemperaturen für diese Materialien benötigen, führen Sie eine In-situ-Kalibrierung durch und speichern Sie das Ergebnis als benutzerdefiniertes Material.

---

## Fotoannotation {#photo-annotation}

Nach einer erfolgreichen Berechnung tippen Sie auf die Schaltfläche **📷 Foto annotieren**, um Sensor- und Quellenmarkierungen über ein Foto Ihres Aufbaus zu legen.

![Fotoannotation](../screenshots/08-photo-annotation.png)

### Ablauf

1. Tippen Sie auf **Foto annotieren** — die Systemkamera öffnet sich
2. Machen Sie ein Foto Ihrer Sensorplatzierung
3. Die App lädt das Foto in die Annotationsüberlagerung
4. Sensormarkierungen (A, B, C, D, E, F je nach Bedarf — bis zu 6 Sensoren) und die Quellenmarkierung werden basierend auf Ihrer Berechnung automatisch platziert
5. Ziehen Sie eine beliebige Markierung, um die Position fein abzustimmen. Während Sie anpassen, wird die Quellposition aus den korrigierten Sensorpositionen neu berechnet
6. Tippen Sie auf **Speichern**, um zu behalten, oder **Erneut aufnehmen**, um es erneut zu versuchen

Das annotierte Foto wird automatisch in PDF-Berichte aufgenommen.

---

## Berichte {#reports}

Tippen Sie auf die Schaltfläche **Ergebnis drucken** auf einem beliebigen Ergebnisbildschirm, um einen formatierten Bericht zu erstellen.

![PDF-Bericht](../screenshots/09-pdf-report.png)

### Berichtsinhalt

- Kopfzeile (anpassbar in Einstellungen → Berichtskopfzeile)
- Messtitel und Zeitstempel
- Alle Eingabewerte in einer übersichtlichen Tabelle
- Berechnungsergebnis
- Schlussfolgerungstext
- Visualisierung (Geometriediagramm)
- Annotiertes Foto (falls aufgenommen)
- Temperatur-Fußzeile (wenn Kompensation aktiv war)
- Seitenzahl und Credit-Zeile

### Ausgabeformat

- **Android**: native PDF-Generierung, auf Ihrem Telefon speichern oder teilen
- **iOS**: System-Druckdialog → als PDF speichern, AirPrint oder teilen

### Anpassen der Kopfzeile

Einstellungen → Berichtskopfzeile. Geben Sie Ihren Firmennamen, Labornamen, Projektinfo oder was auch immer Sie oben in jedem Bericht haben möchten ein.

---

## Backup und Wiederherstellung {#backup-and-restore}

Speichern Sie alle Ihre benutzerdefinierten Materialien, Favoriten, Einstellungen und den Verlauf in einer einzigen Datei. Übertragung zwischen Geräten.

### Backup

Einstellungen → **Backup** → tippen Sie auf „Backup-Datei speichern". Die App erzeugt eine JSON-Datei und öffnet das Teilen-Menü Ihres Telefons. Speichern Sie sie in Ihrem Cloud-Laufwerk (Google Drive, iCloud, OneDrive), senden Sie sie sich per E-Mail oder übertragen Sie sie auf beliebige Weise.

### Wiederherstellen

Einstellungen → **Wiederherstellen** → wählen Sie die Backup-Datei aus dem Speicher Ihres Telefons. Die App importiert benutzerdefinierte Materialien, Favoriten, den Verlauf und die Einstellungen.

⚠️ **Wiederherstellung ersetzt Ihre aktuellen Daten.** Wenn Sie wichtige Messungen auf dem aktuellen Gerät haben, sichern Sie diese zuerst, bevor Sie aus einem anderen Backup wiederherstellen.

---

## Einstellungen {#settings}

Zugriff über das ⚙-Zahnradsymbol in der oberen rechten Ecke. Die Einstellungen sind ein Modal, keine Registerkarte.

![Einstellungen](../screenshots/06-settings.png)

| Einstellung | Was es steuert |
|---|---|
| **Auf Pro upgraden** | Pro-Funktionen kaufen oder mehr darüber erfahren ($19,99) |
| **Sprache** | App-Anzeigesprache (30 unterstützt) |
| **Theme** | Hell, Dunkel oder Auto (System folgen) |
| **Distanzeinheit** | cm oder Zoll |
| **Referenztemperatur** | Aktive Temperatur für die Kompensation, -40 bis +200 °C |
| **Berichtskopfzeile** | Benutzerdefinierter Text oben in generierten Berichten |
| **Backup** | Alle Daten in eine Datei exportieren |
| **Wiederherstellen** | Daten aus einer Backup-Datei importieren |
| **Kauf wiederherstellen** | Pro auf einem neuen Gerät neu erwerben |

---

## Pro-Funktionen {#pro-features}

NVH Source Locator verwendet ein **Feature-gesperrtes Freemium-Modell**:

- **Kostenlos**: Die 2-Sensor-Registerkarte ist voll funktionsfähig ohne Einschränkungen
- **Pro**: Alle anderen Registerkarten haben bestimmte Eingabefelder gesperrt. Die Paywall erscheint, wenn ein kostenloser Benutzer ein gesperrtes Feld antippt

### Was gesperrt ist

Pro-erforderliche Felder sind verteilt auf:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D- und 3D+-Modi
- Backup und Wiederherstellung
- PDF-Berichte
- Benutzerdefinierte Materialien
- Fotoannotation

Ein kostenloser Benutzer kann jede Registerkarte ÖFFNEN und die Oberfläche SEHEN. Er kann nur keine Werte in die Pro-gesperrten Eingabefelder eingeben.

![Pro-gesperrtes Feld](../screenshots/11-pro-locked-field.png)

### Die Paywall

![Paywall](../screenshots/07-paywall.png)

Wenn ein kostenloser Benutzer ein gesperrtes Feld antippt, gleitet die Paywall ein und zeigt:
- App-Symbol mit PRO-Abzeichen
- Funktionsliste
- Freischalt-Schaltfläche mit Preis ($19,99 Standard; kann je nach Region variieren)
- Promo-Code-Einlösung (nur Android — iOS verwendet Apples separaten Offer-Code-Flow)
- Optionaler Promo-Link zu Community-Kanälen

### Pro kaufen

Tippen Sie auf ein beliebiges gesperrtes Feld oder tippen Sie auf **Auf Pro upgraden** in den Einstellungen. Verwendet das offizielle Zahlungssystem Ihrer Plattform (Google Play auf Android, Apple App Store auf iOS).

### Pro auf einem neuen Gerät wiederherstellen

Wenn Sie auf einem Gerät gekauft haben und Pro auf einem anderen möchten (gleiches Konto):

1. Melden Sie sich mit dem **gleichen** Google-Konto (Android) oder Apple-ID (iOS) an, mit dem Sie gekauft haben
2. Öffnen Sie NVH Source Locator auf dem neuen Gerät
3. Gehen Sie zu Einstellungen → **Kauf wiederherstellen**
4. Die App überprüft die Kaufdatensätze der Plattform und schaltet Pro frei

### Auto-Wiederherstellung beim Start

Wenn Sie einen Promo-Code im Google Play Store oder App Store einlösen, während NVH Source Locator im Hintergrund läuft, erkennt die Rückkehr zur App automatisch den neuen Kauf und schaltet Pro frei — keine manuelle Wiederherstellung erforderlich.

### Promo-Code-Einlösung

**Android**: Eine Schaltfläche „Haben Sie einen Google Play-Promo-Code?" in der Paywall öffnet den Google Play-Einlösungs-Flow mit Ihrem vorausgefüllten Code.

**iOS**: Die App Store-Richtlinie 3.1.1 erfordert die Einlösung über Apples offiziellen „Code einlösen"-Flow. Die Google Play-Schaltfläche ist auf iOS ausgeblendet. Suchen Sie stattdessen nach „App Store-Code einlösen" in den Einstellungen.

---

## Help-Registerkarte und Tutorials {#help-tab-and-tutorials}

Die **Help**-Registerkarte enthält In-App-Tutorials, Best-Practice-Anleitungen und Referenzinformationen.

![Help-Registerkarte](../screenshots/10-help-tab.png)

Behandelte Themen:
- Welche Ausrüstung Sie benötigen
- Wie man Sensoren für die beste Genauigkeit platziert
- Kalibrierungstipps
- Häufige Messszenarien
- Tipps für Triangulation und 3D-Platzierungen
- Kabelführung und Signalqualität

---

## Fehlerbehebung {#troubleshooting}

### Berechnungsergebnis ist falsch oder ergibt keinen Sinn

1. Überprüfen Sie Ihre Kalibrierung. Das automatisch ausgefüllte `tCal` setzt die veröffentlichte Materialgeschwindigkeit voraus — reale Materialien variieren. Die genaueste Kalibrierung ist in-situ: tippen Sie auf eine bekannte Position und lassen Sie die App die tatsächliche Geschwindigkeit ableiten.
2. Überprüfen Sie die Einstellung **Erster Sensor** — welcher Sensor das Ereignis zuerst gehört hat, ist für die Berechnung wichtig.
3. Überprüfen Sie Ihre Abstandsmessungen. Fehler von wenigen mm pflanzen sich fort.

### Toast sagt „Ergebnis außerhalb des Bereichs"

Die Mathematik besagt, dass sich die Quelle nicht zwischen Ihren Sensoren befindet. Mögliche Ursachen:
- Die Quelle ist tatsächlich außerhalb der Sensorlinie/-ebene
- Eine Ihrer Eingaben ist falsch
- Die Kalibrierungsgeschwindigkeit weicht zu weit von der Realität ab

### Berechnungsgeschwindigkeits-Hinweis zeigt eine Warnfarbe

Die implizite Schallgeschwindigkeit aus Ihren Eingaben ist weit von jedem üblichen Material entfernt (weniger als 50 m/s oder mehr als 20.000 m/s). Überprüfen Sie Ihre Eingaben — wahrscheinlich ein Tippfehler in tCal oder Abstand.

### Materials-Picker zeigt andere Geschwindigkeiten als erwartet

Überprüfen Sie die Referenztemperatur in den Einstellungen. Wenn ungleich 20 °C, spiegeln die angezeigten Geschwindigkeiten die Temperaturkompensation wider. Die App zeigt „ref X @ 20°C" unter kompensierten Geschwindigkeiten an, damit Sie überprüfen können.

### Verlaufseintrag spielt mit anderem Ergebnis ab

Alte Verlaufseinträge, die vor App-Version 1.75 erstellt wurden, haben die Temperatur möglicherweise nicht gespeichert. Wenn Sie die Messung bei einer Nicht-20 °C-Temperatur durchgeführt haben, verwendet die Wiedergabe die aktuelle Einstellung. Stellen Sie die Temperatur in den Einstellungen manuell ein, bevor Sie sie wiedergeben, ODER messen Sie erneut.

### Fotoannotationsmarkierungen nicht dort, wo ich sie erwarte

Markierungen werden basierend auf der Eingabegeometrie automatisch platziert. Ziehen Sie sie zum Anpassen. Das Anpassen von Markierungen aktualisiert die Quellposition in der Fotoüberlagerung — ändert jedoch NICHT das zugrunde liegende Berechnungsergebnis.

### Backup/Wiederherstellung schlägt fehl

Stellen Sie sicher, dass Sie eine Backup-Datei verwenden, die von der gleichen oder einer neueren Version der App generiert wurde. Ältere Backup-Dateien können aktuelle Datenfelder vermissen.

### Kauf wiederherstellen sagt „Kein Kauf gefunden"

1. Überprüfen Sie, dass Sie mit dem gleichen Store-Konto angemeldet sind, mit dem Sie den Kauf getätigt haben
2. Überprüfen Sie, dass der Kauf nicht erstattet wurde oder abgelaufen ist
3. Versuchen Sie, die App zu deinstallieren und neu zu installieren (der Kauf ist an Ihr Store-Konto gebunden, nicht an die App-Installation)
4. Kontaktieren Sie support@evdiag.net, falls es weiterhin besteht

### Numerische Eingabe springt unerwartet auf 0

Beabsichtigt: Wenn Sie ein numerisches Feld verlassen (woanders tippen) und es leer, negativ oder nicht-numerischer Text ist, springt es auf 0. Verhindert stillschweigend defekte Berechnungen durch versehentlich gelöschte Eingaben. Die Temperatureingabe ist ausgenommen (sie klemmt stattdessen auf -40/+200).

### Brauche mehr Hilfe

Kontaktieren Sie `support@evdiag.net` mit:
- Ihrem Gerätemodell und Ihrer Betriebssystemversion
- Der App-Version (Einstellungen → unten auf der Seite)
- Beschreibung dessen, was Sie versucht haben
- Screenshots, falls möglich

---

*NVH Source Locator wird von EVDiag entwickelt. Besuchen Sie https://evdiag.net für Updates und Ressourcen.*
""",

'es': """# NVH Source Locator — Guía del Usuario

NVH Source Locator es una herramienta de medición para localizar fuentes de ruido y vibración mediante TDOA (Tiempo Diferencial de Llegada) a partir de señales de acelerómetros capturadas en un osciloscopio o sistema de medición.

Esta guía cubre todas las funciones. Para un repaso rápido, consulte **Referencia Rápida**.

---

## Tabla de Contenidos

1. [Cómo funciona](#how-it-works)
2. [Antes de empezar](#before-you-start)
3. [Las pestañas principales](#the-main-tabs)
4. [Modo 2-Sensor](#2-sensor-mode)
5. [Modo 3-Sensor](#3-sensor-mode)
6. [Modos Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [La pestaña Materials](#the-materials-tab)
8. [Compensación de temperatura](#temperature-compensation)
9. [Anotación de fotos](#photo-annotation)
10. [Informes](#reports)
11. [Backup y restauración](#backup-and-restore)
12. [Ajustes](#settings)
13. [Funciones Pro](#pro-features)
14. [Pestaña Help y tutoriales](#help-tab-and-tutorials)
15. [Resolución de problemas](#troubleshooting)

---

## Cómo funciona {#how-it-works}

Cuando una fuente de ruido emite un sonido o vibración, la onda viaja a través de un material a una velocidad conocida. Si coloca dos o más acelerómetros en el material y mide cuándo llega la onda a cada uno, la diferencia de tiempo le indica dónde está la fuente.

NVH Source Locator toma:

- **Calibración**: la distancia entre sensores y el tiempo que tarda una onda en recorrer esa distancia (utilizado para calcular la velocidad del sonido del material)
- **Evento**: la diferencia de tiempo entre sensores que detectan el evento de ruido/vibración

Luego calcula dónde se encuentra la fuente en la estructura.

Cuantos más sensores utilice, con mayor precisión podrá localizar la fuente:

- **2 sensores** → distancia a lo largo de una línea
- **3 sensores** → posición en una superficie 2D (X, Y)
- **4 sensores** → posición en el espacio 3D (X, Y, Z)

---

## Antes de empezar {#before-you-start}

Necesitará:

- **Un osciloscopio o sistema de medición** que pueda mostrar la diferencia de tiempo entre los canales del acelerómetro en microsegundos (µs)
- **Al menos 2 acelerómetros** físicamente conectados a la estructura (más sensores = mayor precisión)
- **Una forma de medir la distancia** entre sensores (cinta métrica, calibres)
- **Una forma de generar una onda** en una ubicación conocida para la calibración (impacto de martillo calibrado, golpe de destornillador u otra señal conocida)

![Pantalla principal con pestaña 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Las pestañas principales {#the-main-tabs}

La aplicación tiene pestañas en la parte superior:

![Barra de pestañas](../screenshots/02-tab-bar.png)

| Pestaña | Qué hace | Cuándo usar |
|---|---|---|
| **2-Sensor** | Localización de fuente 1D a lo largo de una línea entre 2 sensores | Comprobaciones rápidas, estructuras tipo viga. **Completamente gratis.** |
| **3-Sensor** | Localización de fuente 2D usando 3 sensores en un triángulo | Uso más general, paneles y superficies |
| **3-Sen+** | 3-Sensor con solucionador de mínimos cuadrados sobredeterminado | Mediciones más exigentes, robusto al ruido |
| **4-Sensor** | Localización 2D usando dos pares (A-B + C-D) | Distribuciones rectangulares de sensores, verificación cruzada |
| **4-Sen+** | Modo 2D avanzado, 4 sensores en cualquier posición | Geometrías no rectangulares, LSQ completo |
| **3D** | Localización de fuente 3D usando 4 sensores con coordenadas XYZ | Estructuras complejas en el espacio 3D |
| **3D+** | 3D con hasta 6 sensores, LSQ sobredeterminado | Geometrías muy complejas, máxima precisión |
| **Materials** | Biblioteca de velocidad del sonido + materiales personalizados | Seleccionar una vez por sesión de medición |
| **Help** | Tutoriales en la aplicación y referencia | Cuando necesite un repaso rápido |

> **Gratis vs Pro**: La pestaña 2-Sensor es completamente gratis. Las otras pestañas son accesibles pero tienen campos de entrada específicos bloqueados para usuarios Pro (marcados con una insignia de candado dorado). Tocar un campo bloqueado muestra la paywall Pro.

Los ajustes se acceden mediante el icono de engranaje ⚙ en la esquina superior derecha (no es una pestaña).

---

## Modo 2-Sensor {#2-sensor-mode}

La medición más simple: localización de fuente a lo largo de una línea entre dos acelerómetros.

![Pestaña 2-Sensor](../screenshots/01-home-2sensor.png)

### Paso 1: Aplicar un material

Toque la pestaña Materials. Elija el material del que está hecha su estructura (por ejemplo, "Aluminio", "Acero, Mild (1020)"). La aplicación usa la velocidad del sonido conocida del material para rellenar automáticamente el campo de tiempo de calibración.

Si el material de su estructura no está en la lista, puede seleccionar "Aire" temporalmente y anular el tiempo de calibración manualmente en el paso 2.

### Paso 2: Introducir datos de calibración

En la pestaña 2-Sensor, verá dos secciones de pares: **Par A–B** y **Par A–C** (solo se requiere A–B si solo tiene 2 sensores).

Para cada par, complete:

- **Espaciado del sensor** (`d`): distancia física entre sensores, en cm o pulgadas (configurado en Ajustes)
- **Retardo de tiempo de calibración** (`tCal`): tiempo para que una onda viaje entre los sensores a la velocidad del sonido del material — se rellena automáticamente cuando elige un material, pero puede anularlo

### Paso 3: Introducir el tiempo del evento

- **Retardo de tiempo del evento** (`tEvent`): diferencia de tiempo entre sensores que detectan el evento de ruido, en microsegundos
- **Primer sensor**: qué sensor escuchó el evento primero (A o B)

### Paso 4: Leer el resultado

La aplicación muestra la posición de la fuente como una distancia desde el sensor A:
- Resultado = 0: la fuente está en el sensor A
- Resultado = distancia: la fuente está en el sensor B
- Resultado intermedio: la fuente está entre ellos
- Resultado fuera: la fuente está más allá de uno de los sensores (el toast advertirá)

La tarjeta de resultados muestra ambas distancias (desde A, desde B) e indica qué sensor está más cerca.

### Paso 5 (opcional): Anotar una foto

Toque **📷 Anotar foto** para tomar una foto de su configuración. La aplicación superpone marcadores para los sensores A, B y la fuente. Útil para informes.

---

## Modo 3-Sensor {#3-sensor-mode}

Localiza una fuente en un plano 2D usando tres sensores dispuestos en un triángulo.

![Pestaña 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configuración

Coloque tres sensores en su estructura formando un triángulo. Equilátero, rectángulo o escaleno: la aplicación maneja todas las geometrías.

### Introducir los datos

En la sección **Longitudes de los lados del triángulo**, introduzca la distancia física para los tres lados (A–B, A–C, B–C).

Para cada par (A–B y A–C), introduzca:
- **tCal**: tiempo de calibración (autocompletado desde el material)
- **tEvent**: diferencia de tiempo medida para el evento de ruido
- **Primer sensor**: cuál lo escuchó primero

### Leer el resultado

La aplicación muestra la posición de la fuente como coordenadas X, Y relativas al sensor A (sensor A en el origen, sensor B en el eje X). La visualización muestra los tres sensores y la ubicación de la fuente.

![Resultado del triángulo](../screenshots/04-triangle-result.png)

---

## Modos Pro+ {#pro-modes}

Varias pestañas avanzadas ofrecen solucionadores sobredeterminados y mayor dimensionalidad:

### 3-Sen+ (Pro)

Misma configuración triangular que 3-Sensor, pero calibre Y mida los tres pares (A–B, A–C, B–C). El solucionador usa las 3 TDOAs en un ajuste de mínimos cuadrados, más robusto al ruido de medición y a los materiales anisotrópicos. Se reportan los residuos por par para que pueda detectar mediciones inconsistentes.

### 4-Sensor

Coloque cuatro sensores alrededor del área:
- **A–B** = par horizontal (lados izquierdo/derecho)
- **C–D** = par vertical (lados superior/inferior)

Ejecute el par A–B primero (horizontal), luego el par C–D (vertical). El mapa 2D muestra la intersección. Cada par se calibra por separado, útil cuando el material varía a través de la estructura.

### 4-Sen+ (2D Avanzado)

Cuatro sensores en cualquier posición (no forzados a rectangular). Empareje A con cada uno de B, C, D y calibre por separado. El solucionador de mínimos cuadrados sobredeterminado promedia el ruido de medición por par e informa los residuos por par.

### 3D

Medición 3D completa con 4 sensores colocados en el espacio 3D. Introduzca las coordenadas (X, Y, Z) de cada sensor, además de los tiempos de calibración y de evento para cada par (A–B, A–C, A–D).

### 3D+ (Pro)

Como 3D pero admite hasta **6 sensores** (A a F) con LSQ sobredeterminado. Máxima precisión para geometrías 3D complejas.

---

## La pestaña Materials {#the-materials-tab}

Biblioteca de materiales de ingeniería comunes con velocidad del sonido conocida a 20 °C.

![Pestaña Materials](../screenshots/05-materials-tab.png)

### Lista de materiales

La lista incluye aire, fluidos, gomas, polímeros, maderas, vidrios y metales. Las velocidades van desde ~340 m/s (aire) hasta ~13.000 m/s (algunos metales a temperatura ambiente).

### Materiales integrados con compensación de temperatura

14 metales comúnmente utilizados incluyen datos de coeficiente de temperatura. Cuando la Temperatura de referencia en Ajustes difiere de 20 °C, la aplicación ajusta automáticamente las velocidades de estos materiales:

- Aluminio
- Acero, Mild (1020)
- Acero Inoxidable (304)
- Hierro (fundido)
- Hierro
- Cobre
- Latón
- Bronce
- Titanio
- Magnesio
- Plomo
- Zinc
- Níquel
- Tungsteno

Los materiales con compensación muestran dos valores en el selector: la **velocidad compensada** (grande, destacada) y la **velocidad de referencia a 20 °C** (pequeña, gris debajo).

Los materiales sin compensación muestran **"ref only"** en cursiva: su velocidad listada se usa tal cual independientemente de la temperatura.

### Materiales personalizados

Si mide una calibración en la pestaña 2-Sensor, puede guardar el resultado como un material personalizado. Después de una medición 2-Sensor exitosa, busque la opción para guardar la velocidad derivada con un nombre de su elección.

Los materiales personalizados almacenan la velocidad medida in-situ; nunca aplican compensación de temperatura (la velocidad ya se midió a la temperatura de prueba).

### Favoritos

Toque la estrella junto a cualquier material para marcarlo como favorito. Los favoritos aparecen en la parte superior de la lista para acceso rápido.

### Búsqueda

Use la barra de búsqueda en la parte superior para filtrar materiales por nombre. La búsqueda coincide con los nombres canónicos en inglés y los nombres de visualización traducidos.

---

## Compensación de temperatura {#temperature-compensation}

La velocidad del sonido en los materiales cambia con la temperatura. En las pruebas NVH automotrices, esto es importante: un compartimento del motor a 80 °C, una cabina enfriada a -10 °C o un área del colector de escape a 200 °C se comportan de manera diferente a las condiciones de laboratorio a temperatura ambiente.

### Configuración de la temperatura

Abra Ajustes (icono ⚙) → Temperatura de referencia. Introduzca la temperatura de su entorno de prueba en °C (rango -40 a +200).

![Panel de ajustes](../screenshots/06-settings.png)

### Qué sucede cuando la temperatura ≠ 20 °C

- Los campos de tiempo de calibración se autocompletan con la velocidad ajustada por temperatura
- El selector de Materials muestra la velocidad ajustada de forma prominente
- Un toast confirma: *"Aluminio aplicado (6.284 m/s @ 60 °C) — N par(es) actualizado(s)"*
- La pista "Material más cercano" compara con velocidades ajustadas por temperatura
- Las entradas de historial guardadas registran la temperatura activa
- Los informes incluyen una línea de pie de página: *"Temperatura de referencia: 60 °C, compensación aplicada"*

### Restablecer al iniciar la aplicación

La Temperatura de referencia **siempre se restablece a 20 °C** cuando inicia la aplicación. Esto evita que configuraciones obsoletas de una sesión de medición pasada afecten silenciosamente el trabajo de hoy. Una pequeña nota en cursiva en Ajustes le recuerda este comportamiento.

Si desea reproducir una medición histórica a su temperatura original, simplemente toque la entrada: la temperatura se restaura automáticamente.

### Materiales sin compensación

La mayoría de los materiales no metálicos no tienen coeficientes de temperatura publicados confiables. La aplicación muestra una insignia **"ref only"** para estos: su velocidad listada se usa independientemente de la configuración de temperatura. Si necesita mediciones precisas a temperaturas no ambientales para estos materiales, realice una calibración in-situ y guarde el resultado como un material personalizado.

---

## Anotación de fotos {#photo-annotation}

Después de un cálculo exitoso, toque el botón **📷 Anotar foto** para superponer marcadores de sensor y fuente en una foto de su configuración.

![Anotación de fotos](../screenshots/08-photo-annotation.png)

### Flujo

1. Toque **Anotar foto**: se abre la cámara del sistema
2. Tome una foto de la colocación de su sensor
3. La aplicación carga la foto en la superposición de anotaciones
4. Los marcadores de sensor (A, B, C, D, E, F según corresponda, hasta 6 sensores) y el marcador de fuente se colocan automáticamente según su cálculo
5. Arrastre cualquier marcador para ajustar finamente la posición. A medida que ajusta, la posición de la fuente se recalcula a partir de las posiciones de sensor corregidas
6. Toque **Guardar** para conservar, o **Volver a tomar** para intentarlo de nuevo

La foto anotada se incluye automáticamente en los informes PDF.

---

## Informes {#reports}

Toque el botón **Imprimir resultado** en cualquier pantalla de resultados para generar un informe formateado.

![Informe PDF](../screenshots/09-pdf-report.png)

### Contenido del informe

- Encabezado (personalizable en Ajustes → Encabezado del informe)
- Título de la medición y marca de tiempo
- Todos los valores de entrada en una tabla limpia
- Resultado del cálculo
- Texto de conclusión
- Visualización (gráfico de geometría)
- Foto anotada (si tomó una)
- Línea de pie de página de temperatura (si la compensación estaba activa)
- Número de página y línea de crédito

### Formato de salida

- **Android**: generación nativa de PDF, guardar en su teléfono o compartir
- **iOS**: diálogo de impresión del sistema → guardar como PDF, AirPrint o compartir

### Personalizar el encabezado

Ajustes → Encabezado del informe. Introduzca el nombre de su empresa, nombre del laboratorio, información del proyecto o lo que desee en la parte superior de cada informe.

---

## Backup y restauración {#backup-and-restore}

Guarde todos sus materiales personalizados, favoritos, configuraciones e historial en un solo archivo. Transferir entre dispositivos.

### Backup

Ajustes → **Backup** → toque "Guardar archivo de backup". La aplicación genera un archivo JSON y abre la hoja para compartir de su teléfono. Guárdelo en su unidad en la nube (Google Drive, iCloud, OneDrive), envíelo por correo electrónico a sí mismo o transfiéralo de cualquier manera.

### Restaurar

Ajustes → **Restaurar** → seleccione el archivo de backup del almacenamiento de su teléfono. La aplicación importa materiales personalizados, favoritos, historial y configuraciones.

⚠️ **Restaurar reemplaza sus datos actuales.** Si tiene mediciones importantes en el dispositivo actual, haga una copia de seguridad primero antes de restaurar desde un backup diferente.

---

## Ajustes {#settings}

Acceso a través del icono de engranaje ⚙ en la esquina superior derecha. Ajustes es un modal, no una pestaña.

![Ajustes](../screenshots/06-settings.png)

| Ajuste | Qué controla |
|---|---|
| **Actualizar a Pro** | Comprar o aprender sobre las funciones Pro ($19,99) |
| **Idioma** | Idioma de visualización de la aplicación (30 admitidos) |
| **Tema** | Claro, Oscuro o Auto (seguir sistema) |
| **Unidad de distancia** | cm o pulgadas |
| **Temperatura de referencia** | Temperatura activa para la compensación, -40 a +200 °C |
| **Encabezado del informe** | Texto personalizado en la parte superior de los informes generados |
| **Backup** | Exportar todos los datos a un archivo |
| **Restaurar** | Importar datos desde un archivo de backup |
| **Restaurar compra** | Volver a adquirir Pro en un nuevo dispositivo |

---

## Funciones Pro {#pro-features}

NVH Source Locator utiliza un **modelo freemium con bloqueo por funciones**:

- **Gratis**: La pestaña 2-Sensor es completamente funcional sin límites
- **Pro**: Todas las demás pestañas tienen campos de entrada específicos bloqueados. La paywall aparece cuando un usuario gratuito toca un campo bloqueado

### Qué está bloqueado

Los campos requeridos por Pro están distribuidos en:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modos 3D y 3D+
- Backup y Restaurar
- Informes PDF
- Materiales personalizados
- Anotación de fotos

Un usuario gratuito puede ABRIR cualquier pestaña y VER la interfaz. Simplemente no puede introducir valores en los campos de entrada bloqueados por Pro.

![Campo bloqueado por Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Cuando un usuario gratuito toca un campo bloqueado, la paywall se desliza mostrando:
- Icono de la aplicación con insignia PRO
- Lista de funciones
- Botón de desbloqueo con precio ($19,99 por defecto; puede variar según la región)
- Canje de código promocional (solo Android — iOS usa el flujo separado de Código de Oferta de Apple)
- Enlace promocional opcional a canales de la comunidad

### Comprar Pro

Toque cualquier campo bloqueado o toque **Actualizar a Pro** en Ajustes. Utiliza el sistema de pago oficial de su plataforma (Google Play en Android, Apple App Store en iOS).

### Restaurar Pro en un nuevo dispositivo

Si compró en un dispositivo y desea Pro en otro (misma cuenta):

1. Inicie sesión con la **misma** cuenta de Google (Android) o Apple ID (iOS) que usó para comprar
2. Abra NVH Source Locator en el nuevo dispositivo
3. Vaya a Ajustes → **Restaurar compra**
4. La aplicación verifica con los registros de compra de la plataforma y desbloquea Pro

### Auto-restauración al iniciar

Si canjea un código promocional en Google Play Store o App Store mientras NVH Source Locator se ejecuta en segundo plano, al volver a la aplicación detecta automáticamente la nueva compra y desbloquea Pro: no se necesita Restaurar manual.

### Canje de código promocional

**Android**: un botón "¿Tiene un código promocional de Google Play?" en la paywall abre el flujo de canje de Google Play con su código precargado.

**iOS**: La política de App Store 3.1.1 requiere el canje a través del flujo oficial "Canjear código" de Apple. El botón de Google Play está oculto en iOS. Busque "Canjear código de App Store" en Ajustes en su lugar.

---

## Pestaña Help y tutoriales {#help-tab-and-tutorials}

La pestaña **Help** incluye tutoriales dentro de la aplicación, guías de mejores prácticas e información de referencia.

![Pestaña Help](../screenshots/10-help-tab.png)

Temas cubiertos:
- Qué equipo necesita
- Cómo colocar sensores para la mejor precisión
- Consejos de calibración
- Escenarios de medición comunes
- Consejos para triangulación y colocaciones 3D
- Enrutamiento de cables y calidad de la señal

---

## Resolución de problemas {#troubleshooting}

### El resultado del cálculo es incorrecto o no tiene sentido

1. Verifique su calibración. El `tCal` autocompletado asume la velocidad publicada del material; los materiales reales varían. La calibración más precisa es in-situ: toque una ubicación conocida y deje que la aplicación derive la velocidad real.
2. Verifique la configuración del **Primer sensor**: qué sensor escuchó el evento primero importa para las matemáticas.
3. Verifique sus mediciones de distancia. Los errores de unos pocos mm se propagan.

### Toast dice "Resultado fuera de rango"

Las matemáticas dicen que la fuente no está entre sus sensores. Posibles causas:
- La fuente realmente está fuera de la línea/plano del sensor
- Una de sus entradas es incorrecta
- La velocidad de calibración está demasiado lejos de la realidad

### La pista de velocidad de cálculo muestra un color de advertencia

La velocidad del sonido implícita de sus entradas está lejos de cualquier material común (menos de 50 m/s o más de 20.000 m/s). Verifique sus entradas: probablemente un error tipográfico en tCal o distancia.

### El selector de Materials muestra velocidades diferentes a las esperadas

Verifique la Temperatura de referencia en Ajustes. Si no es 20 °C, las velocidades mostradas reflejan la compensación de temperatura. La aplicación muestra "ref X @ 20°C" debajo de las velocidades compensadas para que pueda verificar.

### La entrada del historial se reproduce con un resultado diferente

Las entradas de historial antiguas creadas antes de la versión 1.75 de la aplicación pueden no haber almacenado la temperatura. Si tomó la medición a una temperatura no de 20 °C, la reproducción usará la configuración actual. Establezca manualmente la temperatura en Ajustes antes de reproducir, O vuelva a medir.

### Marcadores de anotación de fotos no donde esperaba

Los marcadores se colocan automáticamente según la geometría de entrada. Arrástrelos para ajustar. Ajustar los marcadores actualiza la posición de la fuente en la superposición de fotos, pero NO cambia el resultado del cálculo subyacente.

### Falla Backup/Restaurar

Asegúrese de utilizar un archivo de backup generado por la misma versión o una versión más reciente de la aplicación. Los archivos de backup más antiguos pueden carecer de campos de datos actuales.

### Restaurar compra dice "no se encontró ninguna compra"

1. Verifique que está conectado con la misma cuenta de tienda que utilizó para comprar
2. Verifique que la compra no fue reembolsada o ha expirado
3. Intente desinstalar y reinstalar la aplicación (la compra está vinculada a su cuenta de tienda, no a la instalación de la aplicación)
4. Contacte support@evdiag.net si persiste

### La entrada numérica se ajusta a 0 inesperadamente

Por diseño: cuando desenfoca un campo numérico (toca en otro lugar), si está vacío, es negativo o contiene texto no numérico, se ajusta a 0. Evita cálculos silenciosamente rotos por entradas accidentalmente borradas. La entrada de temperatura está exenta (en su lugar, se limita a -40/+200).

### Necesita más ayuda

Contacte `support@evdiag.net` con:
- El modelo de su dispositivo y la versión del SO
- La versión de la aplicación (Ajustes → parte inferior de la página)
- Descripción de lo que intentó
- Capturas de pantalla si es posible

---

*NVH Source Locator es desarrollado por EVDiag. Visite https://evdiag.net para actualizaciones y recursos.*
""",

'fr': """# NVH Source Locator — Guide de l'utilisateur

NVH Source Locator est un outil de mesure pour localiser les sources de bruit et de vibration en utilisant le TDOA (Time Difference of Arrival) à partir des signaux d'accéléromètres capturés sur un oscilloscope ou un système de mesure.

Ce guide couvre toutes les fonctionnalités. Pour un rappel rapide, consultez **Référence Rapide**.

---

## Table des matières

1. [Comment ça fonctionne](#how-it-works)
2. [Avant de commencer](#before-you-start)
3. [Les onglets principaux](#the-main-tabs)
4. [Mode 2-Sensor](#2-sensor-mode)
5. [Mode 3-Sensor](#3-sensor-mode)
6. [Modes Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [L'onglet Materials](#the-materials-tab)
8. [Compensation de température](#temperature-compensation)
9. [Annotation de photo](#photo-annotation)
10. [Rapports](#reports)
11. [Sauvegarde et restauration](#backup-and-restore)
12. [Paramètres](#settings)
13. [Fonctionnalités Pro](#pro-features)
14. [Onglet Help et tutoriels](#help-tab-and-tutorials)
15. [Dépannage](#troubleshooting)

---

## Comment ça fonctionne {#how-it-works}

Lorsqu'une source de bruit émet un son ou une vibration, l'onde se propage à travers le matériau à une vitesse connue. Si vous placez deux ou plusieurs accéléromètres sur le matériau et mesurez le moment où l'onde arrive à chacun, la différence de temps vous indique où se trouve la source.

NVH Source Locator prend :

- **Calibration** : la distance entre les capteurs et le temps qu'il faut à une onde pour parcourir cette distance (utilisé pour calculer la vitesse du son du matériau)
- **Événement** : la différence de temps entre les capteurs détectant l'événement de bruit/vibration

Puis il calcule où se trouve la source dans la structure.

Plus vous utilisez de capteurs, plus précisément vous pouvez localiser la source :

- **2 capteurs** → distance le long d'une ligne
- **3 capteurs** → position sur une surface 2D (X, Y)
- **4 capteurs** → position dans l'espace 3D (X, Y, Z)

---

## Avant de commencer {#before-you-start}

Vous aurez besoin de :

- **Un oscilloscope ou système de mesure** qui peut vous montrer la différence de temps entre les canaux d'accéléromètre en microsecondes (µs)
- **Au moins 2 accéléromètres** physiquement attachés à la structure (plus de capteurs = plus de précision)
- **Un moyen de mesurer la distance** entre les capteurs (mètre, pieds à coulisse)
- **Un moyen de déclencher une onde** à un endroit connu pour la calibration (impact de marteau calibré, frappe de tournevis ou autre signal connu)

![Écran d'accueil avec onglet 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Les onglets principaux {#the-main-tabs}

L'application a des onglets en haut :

![Barre d'onglets](../screenshots/02-tab-bar.png)

| Onglet | Ce qu'il fait | Quand l'utiliser |
|---|---|---|
| **2-Sensor** | Localisation de source 1D le long d'une ligne entre 2 capteurs | Vérifications rapides, structures de type poutre. **Entièrement gratuit.** |
| **3-Sensor** | Localisation de source 2D à l'aide de 3 capteurs dans un triangle | Utilisation la plus générale, panneaux et surfaces |
| **3-Sen+** | 3-Sensor avec solveur des moindres carrés surdéterminé | Mesures plus exigeantes, robuste au bruit |
| **4-Sensor** | Localisation 2D à l'aide de deux paires (A-B + C-D) | Disposition rectangulaire des capteurs, vérification croisée |
| **4-Sen+** | Mode 2D avancé, 4 capteurs à n'importe quelle position | Géométries non rectangulaires, LSQ complet |
| **3D** | Localisation de source 3D à l'aide de 4 capteurs avec coordonnées XYZ | Structures complexes dans l'espace 3D |
| **3D+** | 3D avec jusqu'à 6 capteurs, LSQ surdéterminé | Géométries très complexes, précision maximale |
| **Materials** | Bibliothèque de vitesse du son + matériaux personnalisés | Choisir une fois par session de mesure |
| **Help** | Tutoriels intégrés et référence | Quand vous avez besoin d'un rappel rapide |

> **Gratuit vs Pro** : L'onglet 2-Sensor est entièrement gratuit. Les autres onglets sont accessibles mais ont des champs de saisie spécifiques verrouillés pour les utilisateurs Pro (marqués d'un badge cadenas doré). Toucher un champ verrouillé affiche la paywall Pro.

Les paramètres sont accessibles via l'icône d'engrenage ⚙ dans le coin supérieur droit (pas un onglet).

---

## Mode 2-Sensor {#2-sensor-mode}

La mesure la plus simple : localisation de source le long d'une ligne entre deux accéléromètres.

![Onglet 2-Sensor](../screenshots/01-home-2sensor.png)

### Étape 1 : Appliquer un matériau

Touchez l'onglet Materials. Choisissez le matériau dont est composée votre structure (par exemple, « Aluminium », « Acier, Mild (1020) »). L'application utilise la vitesse du son connue du matériau pour remplir automatiquement le champ de temps de calibration.

Si le matériau de votre structure n'est pas dans la liste, vous pouvez choisir « Air » temporairement et remplacer le temps de calibration manuellement à l'étape 2.

### Étape 2 : Saisir les données de calibration

Sur l'onglet 2-Sensor, vous verrez deux sections de paires : **Paire A–B** et **Paire A–C** (seul A–B est requis si vous n'avez que 2 capteurs).

Pour chaque paire, vous remplissez :

- **Espacement des capteurs** (`d`) : distance physique entre les capteurs, en cm ou pouces (défini dans les Paramètres)
- **Délai de temps de calibration** (`tCal`) : temps pour qu'une onde voyage entre les capteurs à la vitesse du son du matériau — rempli automatiquement quand vous choisissez un matériau, mais vous pouvez le remplacer

### Étape 3 : Saisir le temps de l'événement

- **Délai de temps de l'événement** (`tEvent`) : différence de temps entre les capteurs détectant l'événement de bruit, en microsecondes
- **Premier capteur** : quel capteur a entendu l'événement en premier (A ou B)

### Étape 4 : Lire le résultat

L'application affiche la position de la source comme une distance depuis le capteur A :
- Résultat = 0 : la source est au capteur A
- Résultat = distance : la source est au capteur B
- Résultat intermédiaire : la source est entre eux
- Résultat à l'extérieur : la source est au-delà d'un des capteurs (le toast avertira)

La carte de résultats affiche les deux distances (depuis A, depuis B) et indique quel capteur est plus proche.

### Étape 5 (optionnelle) : Annoter une photo

Touchez **📷 Annoter une photo** pour prendre une photo de votre configuration. L'application superpose des marqueurs pour les capteurs A, B et la source. Utile pour les rapports.

---

## Mode 3-Sensor {#3-sensor-mode}

Localise une source sur un plan 2D à l'aide de trois capteurs disposés en triangle.

![Onglet 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configuration

Placez trois capteurs sur votre structure formant un triangle. Équilatéral, rectangle ou scalène — l'application gère toutes les géométries.

### Saisir les données

Dans la section **Longueurs des côtés du triangle**, saisissez la distance physique pour les trois côtés (A–B, A–C, B–C).

Pour chaque paire (A–B et A–C), saisissez :
- **tCal** : temps de calibration (rempli automatiquement depuis le matériau)
- **tEvent** : différence de temps mesurée pour l'événement de bruit
- **Premier capteur** : lequel l'a entendu en premier

### Lire le résultat

L'application affiche la position de la source comme coordonnées X, Y relatives au capteur A (capteur A à l'origine, capteur B sur l'axe X). La visualisation montre les trois capteurs et l'emplacement de la source.

![Résultat triangle](../screenshots/04-triangle-result.png)

---

## Modes Pro+ {#pro-modes}

Plusieurs onglets avancés offrent des solveurs surdéterminés et une dimensionnalité supérieure :

### 3-Sen+ (Pro)

Même configuration triangulaire que 3-Sensor, mais calibrez ET mesurez les trois paires (A–B, A–C, B–C). Le solveur utilise les 3 TDOAs dans un ajustement par moindres carrés — plus robuste au bruit de mesure et aux matériaux anisotropes. Les résidus par paire sont rapportés pour que vous puissiez repérer les mesures incohérentes.

### 4-Sensor

Placez quatre capteurs autour de la zone :
- **A–B** = paire horizontale (côtés gauche/droite)
- **C–D** = paire verticale (côtés haut/bas)

Exécutez d'abord la paire A–B (horizontale), puis la paire C–D (verticale). La carte 2D montre l'intersection. Chaque paire est calibrée séparément — utile lorsque le matériau varie à travers la structure.

### 4-Sen+ (2D avancé)

Quatre capteurs à n'importe quelle position (pas forcés rectangulaires). Appariez A avec chacun de B, C, D et calibrez séparément. Le solveur des moindres carrés surdéterminé moyenne le bruit de mesure par paire et rapporte les résidus par paire.

### 3D

Mesure 3D complète avec 4 capteurs placés dans l'espace 3D. Saisissez les coordonnées (X, Y, Z) de chaque capteur, plus les temps de calibration et d'événement pour chaque paire (A–B, A–C, A–D).

### 3D+ (Pro)

Comme 3D mais prend en charge jusqu'à **6 capteurs** (A à F) avec LSQ surdéterminé. Précision maximale pour les géométries 3D complexes.

---

## L'onglet Materials {#the-materials-tab}

Bibliothèque de matériaux d'ingénierie courants avec vitesse du son connue à 20 °C.

![Onglet Materials](../screenshots/05-materials-tab.png)

### Liste des matériaux

La liste comprend l'air, les fluides, les caoutchoucs, les polymères, les bois, les verres et les métaux. Les vitesses vont de ~340 m/s (air) à ~13 000 m/s (certains métaux à température ambiante).

### Matériaux intégrés avec compensation de température

14 métaux couramment utilisés incluent des données de coefficient de température. Lorsque la Température de référence dans les Paramètres diffère de 20 °C, l'application ajuste automatiquement les vitesses de ces matériaux :

- Aluminium
- Acier, Mild (1020)
- Acier Inoxydable (304)
- Fer (fonte)
- Fer
- Cuivre
- Laiton
- Bronze
- Titane
- Magnésium
- Plomb
- Zinc
- Nickel
- Tungstène

Les matériaux avec compensation affichent deux valeurs dans le sélecteur : la **vitesse compensée** (grande, importante) et la **vitesse de référence à 20 °C** (petite, grise en dessous).

Les matériaux sans compensation affichent **« ref only »** en italique — leur vitesse listée est utilisée telle quelle indépendamment de la température.

### Matériaux personnalisés

Si vous mesurez une calibration sur l'onglet 2-Sensor, vous pouvez enregistrer le résultat en tant que matériau personnalisé. Après une mesure 2-sensor réussie, recherchez l'option d'enregistrer la vitesse dérivée sous un nom de votre choix.

Les matériaux personnalisés stockent la vitesse mesurée in-situ ; ils n'appliquent jamais de compensation de température (la vitesse a déjà été mesurée à la température de test).

### Favoris

Touchez l'étoile à côté de tout matériau pour le marquer comme favori. Les favoris apparaissent en haut de la liste pour un accès rapide.

### Recherche

Utilisez la barre de recherche en haut pour filtrer les matériaux par nom. La recherche correspond à la fois aux noms canoniques anglais et aux noms d'affichage traduits.

---

## Compensation de température {#temperature-compensation}

La vitesse du son dans les matériaux change avec la température. Dans les tests NVH automobiles, cela compte : un compartiment moteur à 80 °C, une cabine refroidie à -10 °C ou une zone du collecteur d'échappement à 200 °C se comportent tous différemment des conditions de laboratoire à température ambiante.

### Réglage de la température

Ouvrez Paramètres (icône ⚙) → Température de référence. Saisissez la température de votre environnement de test en °C (plage -40 à +200).

![Panneau Paramètres](../screenshots/06-settings.png)

### Que se passe-t-il lorsque la température ≠ 20 °C

- Les champs de temps de calibration se remplissent automatiquement avec la vitesse ajustée à la température
- Le sélecteur de Materials affiche la vitesse ajustée de manière importante
- Un toast confirme : *« Aluminium appliqué (6 284 m/s @ 60 °C) — N paire(s) mise(s) à jour »*
- L'indice « Matériau le plus proche » compare avec les vitesses ajustées à la température
- Les entrées d'historique enregistrées enregistrent la température active
- Les rapports incluent une ligne de pied de page : *« Température de référence : 60 °C, compensation appliquée »*

### Réinitialisation au lancement de l'application

La Température de référence **se réinitialise toujours à 20 °C** quand vous lancez l'application. Cela empêche les paramètres obsolètes d'une session de mesure passée d'affecter silencieusement le travail d'aujourd'hui. Une petite note en italique dans les Paramètres vous rappelle ce comportement.

Si vous voulez rejouer une mesure historique à sa température d'origine, touchez simplement l'entrée — la température est restaurée automatiquement.

### Matériaux sans compensation

La plupart des matériaux non métalliques n'ont pas de coefficients de température publiés fiables. L'application affiche un badge **« ref only »** pour ceux-ci — leur vitesse listée est utilisée indépendamment du réglage de la température. Si vous avez besoin de mesures précises à des températures non ambiantes pour ces matériaux, effectuez une calibration in-situ et enregistrez le résultat en tant que matériau personnalisé.

---

## Annotation de photo {#photo-annotation}

Après un calcul réussi, touchez le bouton **📷 Annoter une photo** pour superposer des marqueurs de capteur et de source sur une photo de votre configuration.

![Annotation de photo](../screenshots/08-photo-annotation.png)

### Flux

1. Touchez **Annoter une photo** — la caméra système s'ouvre
2. Prenez une photo de votre placement de capteur
3. L'application charge la photo dans la superposition d'annotation
4. Les marqueurs de capteur (A, B, C, D, E, F selon le cas — jusqu'à 6 capteurs) et le marqueur de source se placent automatiquement en fonction de votre calcul
5. Faites glisser tout marqueur pour affiner la position. Au fur et à mesure que vous ajustez, la position de la source est recalculée à partir des positions de capteur corrigées
6. Touchez **Enregistrer** pour conserver, ou **Reprendre** pour réessayer

La photo annotée est incluse automatiquement dans les rapports PDF.

---

## Rapports {#reports}

Touchez le bouton **Imprimer le résultat** sur n'importe quel écran de résultats pour générer un rapport formaté.

![Rapport PDF](../screenshots/09-pdf-report.png)

### Contenu du rapport

- En-tête (personnalisable dans Paramètres → En-tête de rapport)
- Titre de la mesure et horodatage
- Toutes les valeurs d'entrée dans un tableau propre
- Résultat du calcul
- Texte de conclusion
- Visualisation (graphique de géométrie)
- Photo annotée (si vous en avez pris une)
- Ligne de pied de page de température (si la compensation était active)
- Numéro de page et ligne de crédit

### Format de sortie

- **Android** : génération PDF native, enregistrer sur votre téléphone ou partager
- **iOS** : boîte de dialogue d'impression système → enregistrer en PDF, AirPrint ou partager

### Personnalisation de l'en-tête

Paramètres → En-tête de rapport. Saisissez votre nom d'entreprise, nom de laboratoire, informations sur le projet ou ce que vous voulez en haut de chaque rapport.

---

## Sauvegarde et restauration {#backup-and-restore}

Enregistrez tous vos matériaux personnalisés, favoris, paramètres et historique dans un seul fichier. Transférer entre appareils.

### Sauvegarde

Paramètres → **Sauvegarde** → touchez « Enregistrer le fichier de sauvegarde ». L'application génère un fichier JSON et ouvre la feuille de partage de votre téléphone. Enregistrez-le dans votre lecteur cloud (Google Drive, iCloud, OneDrive), envoyez-le par e-mail à vous-même ou transférez-le de la manière que vous souhaitez.

### Restauration

Paramètres → **Restauration** → choisissez le fichier de sauvegarde dans le stockage de votre téléphone. L'application importe les matériaux personnalisés, les favoris, l'historique et les paramètres.

⚠️ **La restauration remplace vos données actuelles.** Si vous avez des mesures importantes sur l'appareil actuel, sauvegardez-les d'abord avant de restaurer depuis une autre sauvegarde.

---

## Paramètres {#settings}

Accès via l'icône d'engrenage ⚙ dans le coin supérieur droit. Les paramètres sont une fenêtre modale, pas un onglet.

![Paramètres](../screenshots/06-settings.png)

| Paramètre | Ce qu'il contrôle |
|---|---|
| **Passer à Pro** | Acheter ou en savoir plus sur les fonctionnalités Pro (19,99 $) |
| **Langue** | Langue d'affichage de l'application (30 prises en charge) |
| **Thème** | Clair, Sombre ou Auto (suivre le système) |
| **Unité de distance** | cm ou pouces |
| **Température de référence** | Température active pour la compensation, -40 à +200 °C |
| **En-tête de rapport** | Texte personnalisé en haut des rapports générés |
| **Sauvegarde** | Exporter toutes les données vers un fichier |
| **Restauration** | Importer des données depuis un fichier de sauvegarde |
| **Restaurer l'achat** | Ré-acquérir Pro sur un nouvel appareil |

---

## Fonctionnalités Pro {#pro-features}

NVH Source Locator utilise un **modèle freemium avec verrouillage par fonctionnalité** :

- **Gratuit** : L'onglet 2-Sensor est entièrement fonctionnel sans limites
- **Pro** : Tous les autres onglets ont des champs de saisie spécifiques verrouillés. La paywall apparaît quand un utilisateur gratuit touche un champ verrouillé

### Ce qui est verrouillé

Les champs requérant Pro sont répartis sur :
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modes 3D et 3D+
- Sauvegarde et Restauration
- Rapports PDF
- Matériaux personnalisés
- Annotation de photo

Un utilisateur gratuit peut OUVRIR n'importe quel onglet et VOIR l'interface. Il ne peut simplement pas saisir de valeurs dans les champs de saisie verrouillés par Pro.

![Champ verrouillé par Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Quand un utilisateur gratuit touche un champ verrouillé, la paywall glisse en montrant :
- Icône de l'application avec badge PRO
- Liste de fonctionnalités
- Bouton de déverrouillage avec prix (19,99 $ par défaut ; peut varier selon la région)
- Échange de code promotionnel (Android uniquement — iOS utilise le flux d'Offer Code séparé d'Apple)
- Lien promotionnel optionnel vers les canaux communautaires

### Acheter Pro

Touchez n'importe quel champ verrouillé, ou touchez **Passer à Pro** dans les Paramètres. Utilise le système de paiement officiel de votre plateforme (Google Play sur Android, Apple App Store sur iOS).

### Restaurer Pro sur un nouvel appareil

Si vous avez acheté sur un appareil et voulez Pro sur un autre (même compte) :

1. Connectez-vous au **même** compte Google (Android) ou Apple ID (iOS) que vous avez utilisé pour acheter
2. Ouvrez NVH Source Locator sur le nouvel appareil
3. Allez à Paramètres → **Restaurer l'achat**
4. L'application vérifie avec les enregistrements d'achat de la plateforme et déverrouille Pro

### Auto-restauration au lancement

Si vous échangez un code promotionnel dans le Google Play Store ou l'App Store pendant que NVH Source Locator s'exécute en arrière-plan, le retour à l'application détecte automatiquement le nouvel achat et déverrouille Pro — pas besoin de Restauration manuelle.

### Échange de code promotionnel

**Android** : un bouton « Avez-vous un code promotionnel Google Play ? » dans la paywall ouvre le flux d'échange de Google Play avec votre code pré-rempli.

**iOS** : La politique de l'App Store 3.1.1 exige l'échange via le flux officiel « Échanger un code » d'Apple. Le bouton Google Play est masqué sur iOS. Cherchez « Échanger un code App Store » dans les Paramètres à la place.

---

## Onglet Help et tutoriels {#help-tab-and-tutorials}

L'onglet **Help** inclut des tutoriels intégrés, des guides de meilleures pratiques et des informations de référence.

![Onglet Help](../screenshots/10-help-tab.png)

Sujets couverts :
- Quel équipement vous avez besoin
- Comment placer les capteurs pour la meilleure précision
- Conseils de calibration
- Scénarios de mesure courants
- Conseils pour la triangulation et les placements 3D
- Cheminement des câbles et qualité du signal

---

## Dépannage {#troubleshooting}

### Le résultat du calcul est faux ou n'a aucun sens

1. Vérifiez votre calibration. Le `tCal` rempli automatiquement suppose la vitesse publiée du matériau — les matériaux réels varient. La calibration la plus précise est in-situ : touchez un emplacement connu et laissez l'application dériver la vitesse réelle.
2. Vérifiez le paramètre **Premier capteur** — quel capteur a entendu l'événement en premier compte pour les mathématiques.
3. Vérifiez vos mesures de distance. Les erreurs de quelques mm se propagent.

### Le toast dit « Résultat hors plage »

Les mathématiques disent que la source n'est pas entre vos capteurs. Causes possibles :
- La source est en fait à l'extérieur de la ligne/du plan du capteur
- L'une de vos entrées est fausse
- La vitesse de calibration est trop éloignée de la réalité

### L'indice de vitesse de calcul affiche une couleur d'avertissement

La vitesse du son implicite de vos entrées est loin de tout matériau commun (moins de 50 m/s ou plus de 20 000 m/s). Vérifiez vos entrées — probablement une faute de frappe dans tCal ou distance.

### Le sélecteur Materials affiche des vitesses différentes de celles attendues

Vérifiez la Température de référence dans les Paramètres. Si non-20 °C, les vitesses affichées reflètent la compensation de température. L'application affiche « ref X @ 20°C » sous les vitesses compensées pour que vous puissiez vérifier.

### L'entrée d'historique se rejoue avec un résultat différent

Les anciennes entrées d'historique créées avant la version 1.75 de l'application peuvent ne pas avoir stocké la température. Si vous avez pris la mesure à une température non-20 °C, la relecture utilisera le paramètre actuel. Définissez manuellement la température dans les Paramètres avant de rejouer, OU re-mesurez.

### Les marqueurs d'annotation de photo ne sont pas où je m'y attends

Les marqueurs se placent automatiquement en fonction de la géométrie d'entrée. Faites-les glisser pour ajuster. Ajuster les marqueurs met à jour la position de la source dans la superposition photo — mais NE change PAS le résultat de calcul sous-jacent.

### La sauvegarde/restauration échoue

Assurez-vous d'utiliser un fichier de sauvegarde généré par la même version ou une version plus récente de l'application. Les fichiers de sauvegarde plus anciens peuvent manquer des champs de données actuels.

### Restaurer l'achat dit « aucun achat trouvé »

1. Vérifiez que vous êtes connecté au même compte de boutique que vous avez utilisé pour acheter
2. Vérifiez que l'achat n'a pas été remboursé ou n'a pas expiré
3. Essayez de désinstaller et réinstaller l'application (l'achat est lié à votre compte de boutique, pas à l'installation de l'application)
4. Contactez support@evdiag.net si cela persiste

### L'entrée numérique se réinitialise à 0 de manière inattendue

Par conception : quand vous quittez un champ numérique (touchez ailleurs), s'il est vide, négatif ou contient du texte non numérique, il se réinitialise à 0. Empêche les calculs silencieusement cassés à partir d'entrées accidentellement effacées. L'entrée de température est exemptée (elle se limite à -40/+200 à la place).

### Besoin de plus d'aide

Contactez `support@evdiag.net` avec :
- Le modèle et la version OS de votre appareil
- La version de l'application (Paramètres → bas de page)
- Description de ce que vous avez essayé
- Captures d'écran si possible

---

*NVH Source Locator est développé par EVDiag. Visitez https://evdiag.net pour les mises à jour et les ressources.*
""",

'it': """# NVH Source Locator — Guida Utente

NVH Source Locator è uno strumento di misurazione per localizzare sorgenti di rumore e vibrazione utilizzando TDOA (Time Difference of Arrival) dai segnali degli accelerometri catturati su un oscilloscopio o sistema di misurazione.

Questa guida copre tutte le funzionalità. Per un ripasso rapido, vedere **Riferimento Rapido**.

---

## Indice

1. [Come funziona](#how-it-works)
2. [Prima di iniziare](#before-you-start)
3. [Le schede principali](#the-main-tabs)
4. [Modalità 2-Sensor](#2-sensor-mode)
5. [Modalità 3-Sensor](#3-sensor-mode)
6. [Modalità Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [La scheda Materials](#the-materials-tab)
8. [Compensazione della temperatura](#temperature-compensation)
9. [Annotazione foto](#photo-annotation)
10. [Report](#reports)
11. [Backup e ripristino](#backup-and-restore)
12. [Impostazioni](#settings)
13. [Funzionalità Pro](#pro-features)
14. [Scheda Help e tutorial](#help-tab-and-tutorials)
15. [Risoluzione dei problemi](#troubleshooting)

---

## Come funziona {#how-it-works}

Quando una sorgente di rumore emette un suono o una vibrazione, l'onda viaggia attraverso un materiale a velocità nota. Se posizioni due o più accelerometri sul materiale e misuri quando l'onda arriva a ciascuno, la differenza di tempo ti dice dove si trova la sorgente.

NVH Source Locator prende:

- **Calibrazione**: la distanza tra i sensori e il tempo che ci vuole per un'onda per percorrere quella distanza (utilizzato per calcolare la velocità del suono del materiale)
- **Evento**: la differenza di tempo tra i sensori che rilevano l'evento di rumore/vibrazione

Poi calcola dove si trova la sorgente nella struttura.

Più sensori usi, più accuratamente puoi localizzare la sorgente:

- **2 sensori** → distanza lungo una linea
- **3 sensori** → posizione su una superficie 2D (X, Y)
- **4 sensori** → posizione nello spazio 3D (X, Y, Z)

---

## Prima di iniziare {#before-you-start}

Avrai bisogno di:

- **Un oscilloscopio o sistema di misurazione** che possa mostrarti la differenza di tempo tra i canali dell'accelerometro in microsecondi (µs)
- **Almeno 2 accelerometri** fisicamente collegati alla struttura (più sensori = maggiore precisione)
- **Un modo per misurare la distanza** tra i sensori (metro a nastro, calibri)
- **Un modo per innescare un'onda** in una posizione nota per la calibrazione (impatto di martello calibrato, colpo di cacciavite o altro segnale noto)

![Schermata principale con scheda 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Le schede principali {#the-main-tabs}

L'app ha schede in alto:

![Barra delle schede](../screenshots/02-tab-bar.png)

| Scheda | Cosa fa | Quando usarla |
|---|---|---|
| **2-Sensor** | Localizzazione sorgente 1D lungo una linea tra 2 sensori | Controlli rapidi, strutture tipo trave. **Completamente gratuito.** |
| **3-Sensor** | Localizzazione sorgente 2D usando 3 sensori in un triangolo | Uso più generale, pannelli e superfici |
| **3-Sen+** | 3-Sensor con risolutore minimi quadrati sovradeterminato | Misurazioni più impegnative, robusto al rumore |
| **4-Sensor** | Localizzazione 2D usando due coppie (A-B + C-D) | Layout rettangolari di sensori, verifica incrociata |
| **4-Sen+** | Modalità 2D avanzata, 4 sensori in qualsiasi posizione | Geometrie non rettangolari, LSQ completo |
| **3D** | Localizzazione sorgente 3D usando 4 sensori con coordinate XYZ | Strutture complesse nello spazio 3D |
| **3D+** | 3D con fino a 6 sensori, LSQ sovradeterminato | Geometrie molto complesse, massima precisione |
| **Materials** | Libreria di velocità del suono + materiali personalizzati | Selezionare una volta per sessione di misurazione |
| **Help** | Tutorial in-app e riferimento | Quando hai bisogno di un ripasso rapido |

> **Gratuito vs Pro**: La scheda 2-Sensor è completamente gratuita. Altre schede sono accessibili ma hanno campi di input specifici bloccati per gli utenti Pro (contrassegnati con un badge lucchetto dorato). Toccare un campo bloccato mostra la paywall Pro.

Le Impostazioni sono accessibili tramite l'icona ⚙ dell'ingranaggio in alto a destra (non una scheda).

---

## Modalità 2-Sensor {#2-sensor-mode}

La misurazione più semplice: localizzazione sorgente lungo una linea tra due accelerometri.

![Scheda 2-Sensor](../screenshots/01-home-2sensor.png)

### Passaggio 1: Applicare un materiale

Tocca la scheda Materials. Scegli il materiale di cui è fatta la tua struttura (ad es., "Alluminio", "Acciaio, Mild (1020)"). L'app utilizza la velocità del suono nota del materiale per riempire automaticamente il campo del tempo di calibrazione.

Se il materiale della tua struttura non è nell'elenco, puoi selezionare temporaneamente "Aria" e sovrascrivere il tempo di calibrazione manualmente nel passaggio 2.

### Passaggio 2: Inserire i dati di calibrazione

Sulla scheda 2-Sensor, vedrai due sezioni di coppia: **Coppia A–B** e **Coppia A–C** (è richiesta solo A–B se hai solo 2 sensori).

Per ogni coppia, compili:

- **Distanza tra sensori** (`d`): distanza fisica tra i sensori, in cm o pollici (impostato in Impostazioni)
- **Ritardo tempo di calibrazione** (`tCal`): tempo per un'onda di viaggiare tra i sensori alla velocità del suono del materiale — riempito automaticamente quando selezioni un materiale, ma puoi sovrascriverlo

### Passaggio 3: Inserire il tempo dell'evento

- **Ritardo tempo dell'evento** (`tEvent`): differenza di tempo tra i sensori che rilevano l'evento di rumore, in microsecondi
- **Primo sensore**: quale sensore ha sentito l'evento per primo (A o B)

### Passaggio 4: Leggere il risultato

L'app mostra la posizione della sorgente come una distanza dal sensore A:
- Risultato = 0: la sorgente è al sensore A
- Risultato = distanza: la sorgente è al sensore B
- Risultato intermedio: la sorgente è tra di essi
- Risultato esterno: la sorgente è oltre uno dei sensori (il toast avviserà)

La scheda del risultato mostra entrambe le distanze (da A, da B) e indica quale sensore è più vicino.

### Passaggio 5 (opzionale): Annotare una foto

Tocca **📷 Annota foto** per scattare una foto della tua configurazione. L'app sovrappone marker per i sensori A, B e la sorgente. Utile per i report.

---

## Modalità 3-Sensor {#3-sensor-mode}

Localizza una sorgente su un piano 2D utilizzando tre sensori disposti in un triangolo.

![Scheda 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configurazione

Posiziona tre sensori sulla tua struttura formando un triangolo. Equilatero, rettangolo o scaleno: l'app gestisce tutte le geometrie.

### Inserire i dati

Nella sezione **Lunghezze lati del triangolo**, inserisci la distanza fisica per tutti e tre i lati (A–B, A–C, B–C).

Per ogni coppia (A–B e A–C), inserisci:
- **tCal**: tempo di calibrazione (compilato automaticamente dal materiale)
- **tEvent**: differenza di tempo misurata per l'evento di rumore
- **Primo sensore**: quale lo ha sentito per primo

### Leggere il risultato

L'app mostra la posizione della sorgente come coordinate X, Y relative al sensore A (sensore A all'origine, sensore B sull'asse X). La visualizzazione mostra tutti e tre i sensori e la posizione della sorgente.

![Risultato triangolo](../screenshots/04-triangle-result.png)

---

## Modalità Pro+ {#pro-modes}

Diverse schede avanzate offrono risolutori sovradeterminati e dimensionalità superiore:

### 3-Sen+ (Pro)

Stessa configurazione triangolare di 3-Sensor, ma calibra E misura tutte e tre le coppie (A–B, A–C, B–C). Il risolutore utilizza tutti e 3 i TDOA in un adattamento ai minimi quadrati — più robusto al rumore di misurazione e ai materiali anisotropi. I residui per coppia sono riportati così puoi individuare misurazioni incoerenti.

### 4-Sensor

Posiziona quattro sensori intorno all'area:
- **A–B** = coppia orizzontale (lati sinistro/destro)
- **C–D** = coppia verticale (lati superiore/inferiore)

Esegui prima la coppia A–B (orizzontale), poi la coppia C–D (verticale). La mappa 2D mostra l'intersezione. Ogni coppia è calibrata separatamente — utile quando il materiale varia attraverso la struttura.

### 4-Sen+ (2D avanzato)

Quattro sensori in qualsiasi posizione (non forzati rettangolari). Accoppia A con ciascuno di B, C, D e calibra separatamente. Il risolutore minimi quadrati sovradeterminato fa la media del rumore di misurazione per coppia e riporta i residui per coppia.

### 3D

Misurazione 3D completa con 4 sensori posizionati nello spazio 3D. Inserisci le coordinate (X, Y, Z) di ciascun sensore, più i tempi di calibrazione ed evento per ogni coppia (A–B, A–C, A–D).

### 3D+ (Pro)

Come 3D ma supporta fino a **6 sensori** (da A a F) con LSQ sovradeterminato. Massima precisione per geometrie 3D complesse.

---

## La scheda Materials {#the-materials-tab}

Libreria di materiali ingegneristici comuni con velocità del suono nota a 20 °C.

![Scheda Materials](../screenshots/05-materials-tab.png)

### Elenco dei materiali

L'elenco include aria, fluidi, gomme, polimeri, legni, vetri e metalli. Le velocità vanno da ~340 m/s (aria) a ~13.000 m/s (alcuni metalli a temperatura ambiente).

### Materiali integrati con compensazione della temperatura

14 metalli comunemente usati includono dati sul coefficiente di temperatura. Quando la Temperatura di riferimento in Impostazioni differisce da 20 °C, l'app regola automaticamente le velocità di questi materiali:

- Alluminio
- Acciaio, Mild (1020)
- Acciaio Inossidabile (304)
- Ferro (ghisa)
- Ferro
- Rame
- Ottone
- Bronzo
- Titanio
- Magnesio
- Piombo
- Zinco
- Nichel
- Tungsteno

I materiali con compensazione mostrano due valori nel selettore: la **velocità compensata** (grande, in evidenza) e la **velocità di riferimento a 20 °C** (piccola, grigia sotto).

I materiali senza compensazione mostrano **"ref only"** in corsivo — la loro velocità elencata viene usata così com'è indipendentemente dalla temperatura.

### Materiali personalizzati

Se misuri una calibrazione sulla scheda 2-Sensor, puoi salvare il risultato come materiale personalizzato. Dopo una misurazione 2-sensor riuscita, cerca l'opzione per salvare la velocità derivata con un nome di tua scelta.

I materiali personalizzati memorizzano la velocità misurata in-situ; non applicano mai la compensazione della temperatura (la velocità è già stata misurata alla temperatura di test).

### Preferiti

Tocca la stella accanto a qualsiasi materiale per contrassegnarlo come preferito. I preferiti appaiono in cima all'elenco per un accesso rapido.

### Ricerca

Usa la barra di ricerca in alto per filtrare i materiali per nome. La ricerca corrisponde sia ai nomi canonici inglesi che ai nomi di visualizzazione tradotti.

---

## Compensazione della temperatura {#temperature-compensation}

La velocità del suono nei materiali cambia con la temperatura. Nei test NVH automobilistici questo è importante: un vano motore a 80 °C, un abitacolo raffreddato a -10 °C o un'area del collettore di scarico a 200 °C si comportano tutti diversamente dalle condizioni di laboratorio a temperatura ambiente.

### Impostare la temperatura

Apri Impostazioni (icona ⚙) → Temperatura di riferimento. Inserisci la temperatura del tuo ambiente di test in °C (intervallo da -40 a +200).

![Pannello Impostazioni](../screenshots/06-settings.png)

### Cosa succede quando la temperatura ≠ 20 °C

- I campi del tempo di calibrazione si compilano automaticamente con la velocità regolata per temperatura
- Il selettore Materials mostra la velocità regolata in modo evidente
- Un toast conferma: *"Alluminio applicato (6.284 m/s @ 60 °C) — N coppia/e aggiornata/e"*
- Il suggerimento "Materiale più vicino" confronta con velocità regolate per temperatura
- Le voci della cronologia salvate registrano la temperatura attiva
- I report includono una riga a piè di pagina: *"Temperatura di riferimento: 60 °C, compensazione applicata"*

### Reset all'avvio dell'app

La Temperatura di riferimento **viene sempre ripristinata a 20 °C** quando avvii l'app. Questo impedisce che impostazioni obsolete da una sessione di misurazione passata influenzino silenziosamente il lavoro di oggi. Una piccola nota in corsivo in Impostazioni ti ricorda questo comportamento.

Se vuoi riprodurre una misurazione storica alla sua temperatura originale, tocca semplicemente la voce — la temperatura viene ripristinata automaticamente.

### Materiali senza compensazione

La maggior parte dei materiali non metallici non ha coefficienti di temperatura pubblicati affidabili. L'app mostra un badge **"ref only"** per questi — la loro velocità elencata viene usata indipendentemente dall'impostazione della temperatura. Se hai bisogno di misurazioni accurate a temperature non ambientali per questi materiali, esegui una calibrazione in-situ e salva il risultato come materiale personalizzato.

---

## Annotazione foto {#photo-annotation}

Dopo un calcolo riuscito, tocca il pulsante **📷 Annota foto** per sovrapporre marker di sensore e sorgente su una foto della tua configurazione.

![Annotazione foto](../screenshots/08-photo-annotation.png)

### Flusso

1. Tocca **Annota foto** — si apre la fotocamera di sistema
2. Scatta una foto del posizionamento del tuo sensore
3. L'app carica la foto nell'overlay di annotazione
4. I marker dei sensori (A, B, C, D, E, F a seconda dei casi — fino a 6 sensori) e il marker della sorgente si posizionano automaticamente in base al tuo calcolo
5. Trascina qualsiasi marker per regolare finemente la posizione. Mentre regoli, la posizione della sorgente viene ricalcolata dalle posizioni corrette dei sensori
6. Tocca **Salva** per conservare, o **Riprova** per riprovare

La foto annotata è inclusa automaticamente nei report PDF.

---

## Report {#reports}

Tocca il pulsante **Stampa risultato** su qualsiasi schermata dei risultati per generare un report formattato.

![Report PDF](../screenshots/09-pdf-report.png)

### Contenuto del report

- Intestazione (personalizzabile in Impostazioni → Intestazione report)
- Titolo della misurazione e timestamp
- Tutti i valori di input in una tabella pulita
- Risultato del calcolo
- Testo della conclusione
- Visualizzazione (grafico della geometria)
- Foto annotata (se ne hai scattata una)
- Riga a piè di pagina della temperatura (se la compensazione era attiva)
- Numero di pagina e riga di credito

### Formato di output

- **Android**: generazione PDF nativa, salva sul tuo telefono o condividi
- **iOS**: finestra di dialogo di stampa del sistema → salva come PDF, AirPrint o condividi

### Personalizzare l'intestazione

Impostazioni → Intestazione report. Inserisci il nome della tua azienda, nome del laboratorio, info del progetto o qualsiasi cosa tu voglia in cima a ogni report.

---

## Backup e ripristino {#backup-and-restore}

Salva tutti i tuoi materiali personalizzati, preferiti, impostazioni e cronologia in un singolo file. Trasferisci tra dispositivi.

### Backup

Impostazioni → **Backup** → tocca "Salva file di backup". L'app genera un file JSON e apre il foglio di condivisione del tuo telefono. Salvalo nel tuo cloud drive (Google Drive, iCloud, OneDrive), inviatelo via email a te stesso o trasferiscilo come preferisci.

### Ripristino

Impostazioni → **Ripristino** → seleziona il file di backup dall'archiviazione del tuo telefono. L'app importa materiali personalizzati, preferiti, cronologia e impostazioni.

⚠️ **Il ripristino sostituisce i tuoi dati attuali.** Se hai misurazioni importanti sul dispositivo corrente, eseguine prima il backup prima di ripristinare da un backup diverso.

---

## Impostazioni {#settings}

Accesso tramite l'icona ⚙ dell'ingranaggio in alto a destra. Impostazioni è una finestra modale, non una scheda.

![Impostazioni](../screenshots/06-settings.png)

| Impostazione | Cosa controlla |
|---|---|
| **Aggiorna a Pro** | Acquista o scopri le funzionalità Pro ($19,99) |
| **Lingua** | Lingua di visualizzazione dell'app (30 supportate) |
| **Tema** | Chiaro, Scuro o Auto (seguire il sistema) |
| **Unità di distanza** | cm o pollici |
| **Temperatura di riferimento** | Temperatura attiva per la compensazione, da -40 a +200 °C |
| **Intestazione report** | Testo personalizzato in cima ai report generati |
| **Backup** | Esporta tutti i dati in un file |
| **Ripristino** | Importa i dati da un file di backup |
| **Ripristina acquisto** | Riacquisisci Pro su un nuovo dispositivo |

---

## Funzionalità Pro {#pro-features}

NVH Source Locator usa un **modello freemium con blocco per funzionalità**:

- **Gratuito**: La scheda 2-Sensor è completamente funzionante senza limiti
- **Pro**: Tutte le altre schede hanno campi di input specifici bloccati. La paywall appare quando un utente gratuito tocca un campo bloccato

### Cosa è bloccato

I campi richiesti per Pro sono distribuiti su:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modalità 3D e 3D+
- Backup e Ripristino
- Report PDF
- Materiali personalizzati
- Annotazione foto

Un utente gratuito può APRIRE qualsiasi scheda e VEDERE l'interfaccia. Semplicemente non può inserire valori nei campi di input bloccati da Pro.

![Campo bloccato da Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Quando un utente gratuito tocca un campo bloccato, la paywall scorre mostrando:
- Icona dell'app con badge PRO
- Elenco di funzionalità
- Pulsante di sblocco con prezzo ($19,99 predefinito; può variare in base alla regione)
- Riscatto codice promozionale (solo Android — iOS usa il flusso Offer Code separato di Apple)
- Link promozionale opzionale ai canali della community

### Acquistare Pro

Tocca qualsiasi campo bloccato, o tocca **Aggiorna a Pro** in Impostazioni. Usa il sistema di pagamento ufficiale della tua piattaforma (Google Play su Android, Apple App Store su iOS).

### Ripristinare Pro su un nuovo dispositivo

Se hai acquistato su un dispositivo e vuoi Pro su un altro (stesso account):

1. Accedi al **medesimo** account Google (Android) o Apple ID (iOS) che hai usato per acquistare
2. Apri NVH Source Locator sul nuovo dispositivo
3. Vai a Impostazioni → **Ripristina acquisto**
4. L'app verifica con i record di acquisto della piattaforma e sblocca Pro

### Auto-ripristino all'avvio

Se riscatti un codice promozionale nel Google Play Store o App Store mentre NVH Source Locator è in esecuzione in background, il ritorno all'app rileva automaticamente il nuovo acquisto e sblocca Pro — nessun Ripristino manuale necessario.

### Riscatto codice promozionale

**Android**: un pulsante "Hai un codice promozionale Google Play?" nella paywall apre il flusso di riscatto Google Play con il tuo codice pre-compilato.

**iOS**: La politica dell'App Store 3.1.1 richiede il riscatto attraverso il flusso ufficiale "Riscatta codice" di Apple. Il pulsante Google Play è nascosto su iOS. Cerca "Riscatta codice App Store" in Impostazioni invece.

---

## Scheda Help e tutorial {#help-tab-and-tutorials}

La scheda **Help** include tutorial in-app, guide alle migliori pratiche e informazioni di riferimento.

![Scheda Help](../screenshots/10-help-tab.png)

Argomenti trattati:
- Quale attrezzatura hai bisogno
- Come posizionare i sensori per la migliore precisione
- Consigli di calibrazione
- Scenari di misurazione comuni
- Suggerimenti per triangolazione e posizionamenti 3D
- Instradamento dei cavi e qualità del segnale

---

## Risoluzione dei problemi {#troubleshooting}

### Il risultato del calcolo è sbagliato o non ha senso

1. Controlla la tua calibrazione. Il `tCal` autocompilato presuppone la velocità pubblicata del materiale — i materiali reali variano. La calibrazione più accurata è in-situ: tocca una posizione nota e lascia che l'app derivi la velocità reale.
2. Controlla l'impostazione del **Primo sensore** — quale sensore ha sentito l'evento per primo è importante per la matematica.
3. Verifica le tue misurazioni di distanza. Errori di pochi mm si propagano.

### Il toast dice "Risultato fuori range"

La matematica dice che la sorgente non è tra i tuoi sensori. Possibili cause:
- La sorgente è effettivamente al di fuori della linea/piano del sensore
- Uno dei tuoi input è sbagliato
- La velocità di calibrazione è troppo lontana dalla realtà

### Il suggerimento di velocità di calc mostra un colore di avviso

La velocità del suono implicita dai tuoi input è lontana da qualsiasi materiale comune (meno di 50 m/s o più di 20.000 m/s). Controlla i tuoi input — probabilmente un errore di battitura in tCal o distanza.

### Il selettore Materials mostra velocità diverse da quelle attese

Controlla la Temperatura di riferimento in Impostazioni. Se non è 20 °C, le velocità visualizzate riflettono la compensazione della temperatura. L'app mostra "ref X @ 20°C" sotto le velocità compensate così puoi verificare.

### La voce della cronologia si riproduce con un risultato diverso

Le vecchie voci della cronologia create prima della versione 1.75 dell'app potrebbero non aver memorizzato la temperatura. Se hai effettuato la misurazione a una temperatura non di 20 °C, la riproduzione userà l'impostazione corrente. Imposta manualmente la temperatura in Impostazioni prima di riprodurre, OPPURE misura di nuovo.

### I marker di annotazione foto non sono dove mi aspetto

I marker si posizionano automaticamente in base alla geometria di input. Trascinali per regolare. Regolare i marker aggiorna la posizione della sorgente nell'overlay della foto — ma NON cambia il risultato di calcolo sottostante.

### Il backup/ripristino fallisce

Assicurati di utilizzare un file di backup generato dalla stessa versione o da una versione più recente dell'app. I file di backup più vecchi potrebbero mancare di campi di dati attuali.

### Ripristina acquisto dice "nessun acquisto trovato"

1. Verifica di essere connesso allo stesso account dello store che hai usato per acquistare
2. Verifica che l'acquisto non sia stato rimborsato o scaduto
3. Prova a disinstallare e reinstallare l'app (l'acquisto è legato al tuo account dello store, non all'installazione dell'app)
4. Contatta support@evdiag.net se persiste

### L'input numerico si imposta a 0 inaspettatamente

Per progettazione: quando perdi il focus su un campo numerico (tocchi altrove), se è vuoto, negativo o contiene testo non numerico, si imposta a 0. Previene calcoli silenziosamente rotti da input accidentalmente cancellati. L'input della temperatura è esente (si limita invece a -40/+200).

### Hai bisogno di più aiuto

Contatta `support@evdiag.net` con:
- Il modello del tuo dispositivo e la versione del SO
- La versione dell'app (Impostazioni → in fondo alla pagina)
- Descrizione di cosa hai provato
- Screenshot se possibile

---

*NVH Source Locator è sviluppato da EVDiag. Visita https://evdiag.net per aggiornamenti e risorse.*
""",

}
