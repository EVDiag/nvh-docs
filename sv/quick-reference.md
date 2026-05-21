# NVH Source Locator — Snabbreferens

En sammanfattning på en sida. För fullständiga detaljer, se **Användarhandbok**.

---

## Huvudflöde (2-Sensor, gratis)

1. **Välj ett material** — fliken Materials → tryck på ditt material
2. **Ange kalibrering** i fliken 2-Sensor:
   - Sensoravstånd (`d`)
   - Kalibreringstidsfördröjning (`tCal`) — automatiskt ifylld från materialet
3. **Ange händelse** — `tEvent` och Första sensor (A eller B)
4. **Läs resultat** — avstånd från sensor A

![2-Sensor flik](../screenshots/01-home-2sensor.png)

---

## Alla flikar

| Flik | Utdata | Pro-fält? |
|---|---|---|
| 2-Sensor | Avstånd längs linje | Nej (helt gratis) |
| 3-Sensor | X, Y på en yta | Ja |
| 3-Sen+ | X, Y med LSQ över 3 par | Ja |
| 4-Sensor | X, Y från två par (A–B + C–D) | Ja |
| 4-Sen+ | X, Y från 4 sensorer, valfri position | Ja |
| 3D | X, Y, Z från 4 sensorer | Ja |
| 3D+ | X, Y, Z från upp till 6 sensorer | Ja |
| Materials | Ljudhastighetsväljare | Nej |
| Help | Handledningar | Nej |

Inställningar finns under ⚙-ikonen (uppe till höger), inte som en flik.

---

## Temperaturkompensation

Inställningar → Referenstemperatur, intervall **-40 till +200 °C**.

- **14 metaller** har inbyggd kompensation (aluminium, stål, koppar, mässing, brons, titan, magnesium, bly, zink, nickel, volfram, järn, gjutjärn)
- Material utan kompensation visar **"ref only"**
- **Återställs till 20 °C vid varje appstart** (standard säker start)
- Att spela upp en historikpost återställer dess ursprungliga temperatur

---

## Genvägar

- **Tryck på ett material** → fyller automatiskt i alla `tCal`-fält i alla flikar
- **Håll +/-** på sifferfält → snabb inkrementering
- **Dra horisontellt** på ett sifferfält → bläddra igenom värden
- **Tomt/negativt/ogiltigt inmatning** → snappar till 0 vid fokusförlust (temperaturfältet låses till -40/200)
- **Stjärnmärk ett material** → flyttar det till toppen av väljaren

---

## Pro-modell

**Funktionslåst freemium** ($19,99):
- Gratis: 2-Sensor flik fullt funktionell, utan begränsningar
- Pro: Andra flikar är tillgängliga men har **fält med guldlås** som visar paywall vid tryck

Pro låser upp: 3-Sensor till 3D+, anpassade material, säkerhetskopiering/återställning, PDF-rapporter, fotoannotering.

![Paywall](../screenshots/07-paywall.png)

---

## Rapporter och säkerhetskopiering

**Skriv ut resultat**-knappen på vilken resultatskärm som helst → PDF med rubrik, indata, resultat, visualisering, foto (om taget) och temperaturfot (när kompensation är aktiv).

Anpassa rubriken i Inställningar → Rapportrubrik.

**Säkerhetskopiering**: Inställningar → Säkerhetskopiering → dela till molnet/e-post.  
**Återställ**: Inställningar → Återställ → välj säkerhetskopia.

---

## Återställ Pro på en ny enhet

Samma Google-konto (Android) eller Apple-ID (iOS) som du köpte med → Inställningar → **Återställ köp** → låser upp inom sekunder.

Automatisk återställning sker tyst när du återvänder till appen efter att ha löst in en kampanjkod externt.

---

## Snabb felsökning

- **Resultat utanför intervallet?** Kontrollera tecknet på `tEvent` / Första sensor / sensoravstånd
- **Närmaste material fel?** Referenstemperaturen är förmodligen oavsiktligt inställd — kontrollera Inställningar
- **Återställ köp misslyckas?** Verifiera samma butikskonto; installera om om det kvarstår
- **Fältet snappat till 0?** Tomma/negativa indata snappar automatiskt vid fokusförlust — ange värdet igen
- **Stegknappar borta?** De visas bredvid fält med `data-step` — starta om appen om de saknas
- **Föråldrad temperaturvarning?** Återställs till 20 vid varje start — ställ in igen för denna session

---

Kontakt `support@evdiag.net` — inkludera enhetsmodell, appversion (Inställningar → nederst) och en beskrivning av vad du försökte.
