# NVH Source Locator — Benutzerhandbuch

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

## Funktionsweise

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

## Bevor Sie beginnen

Sie benötigen:

- **Ein Oszilloskop oder Messsystem**, das die Zeitdifferenz zwischen Beschleunigungssensor-Kanälen in Mikrosekunden (µs) anzeigen kann
- **Mindestens 2 Beschleunigungssensoren**, die physisch an der Struktur angebracht sind (mehr Sensoren = höhere Genauigkeit)
- **Eine Möglichkeit, den Abstand** zwischen den Sensoren zu messen (Maßband, Messschieber)
- **Eine Möglichkeit, eine Welle auszulösen** an einer bekannten Stelle zur Kalibrierung (kalibrierter Hammerschlag, Schraubenzieher-Klopfen oder anderes bekanntes Signal)

![Startbildschirm mit 2-Sensor-Registerkarte](../screenshots/01-home-2sensor.png)

---

## Die Haupt-Registerkarten

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

## 2-Sensor-Modus

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

## 3-Sensor-Modus

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

## Pro+-Modi

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

## Die Materials-Registerkarte

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

## Temperaturkompensation

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

## Fotoannotation

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

## Berichte

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

## Backup und Wiederherstellung

Speichern Sie alle Ihre benutzerdefinierten Materialien, Favoriten, Einstellungen und den Verlauf in einer einzigen Datei. Übertragung zwischen Geräten.

### Backup

Einstellungen → **Backup** → tippen Sie auf „Backup-Datei speichern". Die App erzeugt eine JSON-Datei und öffnet das Teilen-Menü Ihres Telefons. Speichern Sie sie in Ihrem Cloud-Laufwerk (Google Drive, iCloud, OneDrive), senden Sie sie sich per E-Mail oder übertragen Sie sie auf beliebige Weise.

### Wiederherstellen

Einstellungen → **Wiederherstellen** → wählen Sie die Backup-Datei aus dem Speicher Ihres Telefons. Die App importiert benutzerdefinierte Materialien, Favoriten, den Verlauf und die Einstellungen.

⚠️ **Wiederherstellung ersetzt Ihre aktuellen Daten.** Wenn Sie wichtige Messungen auf dem aktuellen Gerät haben, sichern Sie diese zuerst, bevor Sie aus einem anderen Backup wiederherstellen.

---

## Einstellungen

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

## Pro-Funktionen

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

## Help-Registerkarte und Tutorials

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

## Fehlerbehebung

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
