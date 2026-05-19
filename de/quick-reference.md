# NVH Source Locator — Kurzanleitung

Eine einseitige Zusammenfassung. Vollständige Details siehe `user-guide.md`.

---

## Grundablauf (2-Sensor, kostenlos)

1. **Material auswählen** — Materials-Registerkarte → tippen Sie auf Ihr Material
2. **Kalibrierung eingeben** in der 2-Sensor-Registerkarte:
   - Sensorabstand (`d`)
   - Kalibrierungszeit (`tCal`) — automatisch vom Material ausgefüllt
3. **Ereignis eingeben** — `tEvent` und Erster Sensor (A oder B)
4. **Ergebnis ablesen** — Abstand vom Sensor A

![2-Sensor Registerkarte](../screenshots/01-home-2sensor.png)

---

## Alle Registerkarten

| Registerkarte | Ergebnis | Pro-Felder? |
|---|---|---|
| 2-Sensor | Abstand entlang einer Linie | Nein (vollständig kostenlos) |
| 3-Sensor | X, Y auf einer Fläche | Ja |
| 3-Sen+ | X, Y mit LSQ über 3 Paare | Ja |
| 4-Sensor | X, Y aus zwei Paaren (A–B + C–D) | Ja |
| 4-Sen+ | X, Y aus 4 Sensoren, beliebige Position | Ja |
| 3D | X, Y, Z aus 4 Sensoren | Ja |
| 3D+ | X, Y, Z aus bis zu 6 Sensoren | Ja |
| Materials | Schallgeschwindigkeitsauswahl | Nein |
| Help | Tutorials | Nein |

Die Einstellungen befinden sich hinter dem ⚙-Symbol (oben rechts), nicht als Registerkarte.

---

## Temperaturkompensation

Einstellungen → Referenztemperatur, Bereich **-40 bis +200 °C**.

- **14 Metalle** verfügen über integrierte Kompensation (Aluminium, Stähle, Kupfer, Messing, Bronze, Titan, Magnesium, Blei, Zink, Nickel, Wolfram, Eisen, Gusseisen)
- Materialien ohne Kompensation zeigen **„ref only"** an
- **Wird bei jedem App-Start auf 20 °C zurückgesetzt** (sicherer Standardstart)
- Beim Abspielen eines Verlaufseintrags wird die ursprüngliche Temperatur wiederhergestellt

---

## Tastenkürzel

- **Material antippen** → füllt alle `tCal`-Felder in allen Registerkarten automatisch aus
- **+/− halten** auf Zahlenfeldern → schnelles Inkrementieren
- **Horizontales Ziehen** auf einem Zahlenfeld → Werte scrubben
- **Leere/negative/ungültige Eingabe** → springt beim Verlassen auf 0 (Temperaturfeld klemmt auf -40/200)
- **Material mit Stern markieren** → wird in der Auswahl nach oben verschoben

---

## Pro-Modell

**Feature-gesperrtes Freemium-Modell** ($19,99):
- Kostenlos: 2-Sensor-Registerkarte voll funktionsfähig, ohne Einschränkungen
- Pro: Andere Registerkarten zugänglich, aber mit **Feldern mit goldenem Schloss**, die beim Tippen die Paywall anzeigen

Pro schaltet frei: 3-Sensor bis 3D+, benutzerdefinierte Materialien, Backup/Wiederherstellung, PDF-Berichte, Fotoannotation.

![Paywall](../screenshots/07-paywall.png)

---

## Berichte & Backup

Die **Ergebnis drucken**-Schaltfläche auf einem beliebigen Ergebnisbildschirm → PDF mit Kopfzeile, Eingaben, Ergebnis, Visualisierung, Foto (falls aufgenommen) und Temperatur-Fußzeile (wenn Kompensation aktiv).

Kopfzeile anpassen unter Einstellungen → Berichtskopfzeile.

**Backup**: Einstellungen → Backup → in Cloud/E-Mail teilen.  
**Wiederherstellen**: Einstellungen → Wiederherstellen → Backup-Datei auswählen.

---

## Pro auf einem neuen Gerät wiederherstellen

Selbes Google-Konto (Android) oder Apple-ID (iOS), mit dem Sie gekauft haben → Einstellungen → **Kauf wiederherstellen** → wird innerhalb von Sekunden freigeschaltet.

Auto-Wiederherstellung erfolgt im Hintergrund, wenn Sie nach dem externen Einlösen eines Promo-Codes zur App zurückkehren.

---

## Schnelle Fehlerbehebung

- **Ergebnis außerhalb des Bereichs?** Vorzeichen von `tEvent` / Ersten Sensor / Sensorabstand überprüfen
- **Falsches nächstgelegenes Material?** Referenztemperatur wahrscheinlich versehentlich gesetzt — Einstellungen überprüfen
- **Kauf wiederherstellen schlägt fehl?** Selbes Store-Konto bestätigen; bei anhaltenden Problemen neu installieren
- **Feld auf 0 zurückgesetzt?** Leere/negative Eingaben werden beim Verlassen automatisch auf 0 gesetzt — Wert erneut eingeben
- **Stepper-Schaltflächen weg?** Sie erscheinen neben Feldern mit `data-step` — bei Fehlen App neu starten
- **Veraltete Temperaturwarnung?** Wird bei jedem Start auf 20 zurückgesetzt — für diese Sitzung erneut einstellen

---

Kontakt `support@evdiag.net` — geben Sie Gerätemodell, App-Version (Einstellungen → unten) und eine Beschreibung Ihres Vorgehens an.
