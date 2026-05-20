# NVH Source Locator — Referință rapidă

Un rezumat pe o pagină. Pentru detalii complete, consultați `user-guide.md`.

---

## Flux principal (2-Sensor, gratuit)

1. **Alegeți un material** — fila Materials → atingeți materialul dvs.
2. **Introduceți calibrarea** în fila 2-Sensor:
   - Distanța dintre senzori (`d`)
   - Întârzierea timpului de calibrare (`tCal`) — completat automat din material
3. **Introduceți evenimentul** — `tEvent` și Primul senzor (A sau B)
4. **Citiți rezultatul** — distanța de la senzorul A

![Fila 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Toate filele

| Filă | Ieșire | Câmpuri Pro? |
|---|---|---|
| 2-Sensor | Distanța de-a lungul liniei | Nu (complet gratuit) |
| 3-Sensor | X, Y pe o suprafață | Da |
| 3-Sen+ | X, Y cu LSQ peste 3 perechi | Da |
| 4-Sensor | X, Y din două perechi (A–B + C–D) | Da |
| 4-Sen+ | X, Y din 4 senzori, orice poziție | Da |
| 3D | X, Y, Z din 4 senzori | Da |
| 3D+ | X, Y, Z din până la 6 senzori | Da |
| Materials | Selector de viteză a sunetului | Nu |
| Help | Tutoriale | Nu |

Setările se află sub pictograma ⚙ (sus-dreapta), nu ca filă.

---

## Compensarea temperaturii

Setări → Temperatura de referință, interval **-40 până la +200 °C**.

- **14 metale** au compensare integrată (aluminiu, oțeluri, cupru, alamă, bronz, titan, magneziu, plumb, zinc, nichel, wolfram, fier, fontă)
- Materialele fără compensare afișează **„ref only"**
- **Se resetează la 20 °C la fiecare pornire a aplicației** (pornire sigură implicită)
- Redarea unei intrări din istoric îi restaurează temperatura inițială

---

## Comenzi rapide

- **Atingeți un material** → completează automat toate câmpurile `tCal` în toate filele
- **Țineți apăsat +/-** pe câmpurile numerice → incrementare rapidă
- **Trageți orizontal** pe un câmp numeric → defilare prin valori
- **Intrare goală/negativă/nevalidă** → trece la 0 la pierderea focusului (câmpul de temperatură se limitează la -40/200)
- **Marcați un material cu stea** → îl mută în partea de sus a selectorului

---

## Modelul Pro

**Freemium cu blocare pe funcție** ($19,99):
- Gratuit: fila 2-Sensor complet funcțională, fără limite
- Pro: Alte file sunt accesibile, dar au **câmpuri cu lacăt auriu** care afișează paywall la atingere

Pro deblochează: de la 3-Sensor la 3D+, materiale personalizate, backup/restaurare, rapoarte PDF, adnotare foto.

![Paywall](../screenshots/07-paywall.png)

---

## Rapoarte și backup

Butonul **Imprimare rezultat** pe orice ecran de rezultate → PDF cu antet, intrări, rezultat, vizualizare, fotografie (dacă a fost făcută) și subsol cu temperatura (când compensarea este activă).

Personalizați antetul în Setări → Antet raport.

**Backup**: Setări → Backup → partajare în cloud/e-mail.  
**Restaurare**: Setări → Restaurare → selectați fișierul de backup.

---

## Restaurați Pro pe un dispozitiv nou

Același cont Google (Android) sau Apple ID (iOS) cu care ați cumpărat → Setări → **Restaurare achiziție** → se deblochează în câteva secunde.

Restaurarea automată se face în mod silențios când vă întoarceți la aplicație după ce ați răscumpărat un cod promoțional în mod extern.

---

## Depanare rapidă

- **Rezultat în afara intervalului?** Verificați semnul `tEvent` / Primul senzor / distanța senzorilor
- **Cel mai apropiat material greșit?** Temperatura de referință este probabil setată accidental — verificați Setările
- **Restaurarea achiziției eșuează?** Verificați același cont al magazinului; reinstalați dacă persistă
- **Câmp resetat la 0?** Intrările goale/negative se setează automat la pierderea focusului — reintroduceți valoarea
- **Butoanele stepper au dispărut?** Apar lângă câmpurile cu `data-step` — reporniți aplicația dacă lipsesc
- **Avertisment temperatură depășită?** Se resetează la 20 la fiecare pornire — setați din nou pentru această sesiune

---

Contact `support@evdiag.net` — includeți modelul dispozitivului, versiunea aplicației (Setări → jos) și o descriere a ceea ce ați încercat.
