# NVH Source Locator — Hurtigreferanse

En sammendrag på én side. For fullstendige detaljer, se `user-guide.md`.

---

## Hovedflyt (2-Sensor, gratis)

1. **Velg et materiale** — Materials-fanen → trykk på materialet ditt
2. **Skriv inn kalibrering** i 2-Sensor-fanen:
   - Sensoravstand (`d`)
   - Kalibreringstidsforsinkelse (`tCal`) — fylles automatisk ut fra materialet
3. **Skriv inn hendelse** — `tEvent` og Første sensor (A eller B)
4. **Les resultatet** — avstand fra sensor A

![2-Sensor fane](../screenshots/01-home-2sensor.png)

---

## Alle faner

| Fane | Utgang | Pro-felter? |
|---|---|---|
| 2-Sensor | Avstand langs linje | Nei (helt gratis) |
| 3-Sensor | X, Y på en flate | Ja |
| 3-Sen+ | X, Y med LSQ over 3 par | Ja |
| 4-Sensor | X, Y fra to par (A–B + C–D) | Ja |
| 4-Sen+ | X, Y fra 4 sensorer, vilkårlig posisjon | Ja |
| 3D | X, Y, Z fra 4 sensorer | Ja |
| 3D+ | X, Y, Z fra opptil 6 sensorer | Ja |
| Materials | Lydhastighetsvelger | Nei |
| Help | Veiledninger | Nei |

Innstillinger finnes under ⚙-ikonet (øverst til høyre), ikke som en fane.

---

## Temperaturkompensasjon

Innstillinger → Referansetemperatur, område **-40 til +200 °C**.

- **14 metaller** har innebygd kompensasjon (aluminium, stål, kobber, messing, bronse, titan, magnesium, bly, sink, nikkel, wolfram, jern, støpejern)
- Materialer uten kompensasjon viser **"ref only"**
- **Tilbakestilles til 20 °C ved hver appstart** (standard sikker start)
- Avspilling av en historikkpost gjenoppretter dens opprinnelige temperatur

---

## Snarveier

- **Trykk på et materiale** → fyller automatisk ut alle `tCal`-felter i alle faner
- **Hold +/-** på tallfelt → rask inkrementering
- **Dra horisontalt** på et tallfelt → bla gjennom verdier
- **Tom/negativ/ugyldig inndata** → settes til 0 ved fokustap (temperaturfeltet klemmes til -40/200)
- **Stjernemerk et materiale** → flytter det til toppen av velgeren

---

## Pro-modell

**Funksjonslåst freemium** ($19,99):
- Gratis: 2-Sensor-fanen er fullt funksjonell, uten begrensninger
- Pro: Andre faner er tilgjengelige, men har **felter med gylden hengelås** som viser paywall ved trykk

Pro låser opp: 3-Sensor til 3D+, egendefinerte materialer, sikkerhetskopiering/gjenoppretting, PDF-rapporter, fotoanmerkning.

![Paywall](../screenshots/07-paywall.png)

---

## Rapporter og sikkerhetskopiering

**Skriv ut resultat**-knappen på enhver resultatskjerm → PDF med overskrift, inndata, resultat, visualisering, bilde (hvis tatt) og temperaturbunntekst (når kompensasjon er aktiv).

Tilpass overskriften i Innstillinger → Rapportoverskrift.

**Sikkerhetskopiering**: Innstillinger → Sikkerhetskopiering → del til skyen/e-post.  
**Gjenopprett**: Innstillinger → Gjenopprett → velg sikkerhetskopifil.

---

## Gjenopprett Pro på en ny enhet

Samme Google-konto (Android) eller Apple-ID (iOS) du kjøpte med → Innstillinger → **Gjenopprett kjøp** → låses opp innen sekunder.

Automatisk gjenoppretting skjer stille når du returnerer til appen etter å ha innløst en kampanjekode eksternt.

---

## Rask feilsøking

- **Resultat utenfor område?** Sjekk tegnet på `tEvent` / Første sensor / sensoravstand
- **Nærmeste materiale feil?** Referansetemperaturen er sannsynligvis utilsiktet satt — sjekk Innstillinger
- **Gjenopprett kjøp mislykkes?** Verifiser samme butikkonto; installer på nytt hvis det vedvarer
- **Felt satt til 0?** Tomme/negative inndata settes automatisk ved fokustap — skriv inn verdien på nytt
- **Stegknapper borte?** De vises ved siden av felter med `data-step` — start appen på nytt hvis de mangler
- **Foreldet temperaturadvarsel?** Tilbakestilles til 20 ved hver start — sett på nytt for denne økten

---

Kontakt `support@evdiag.net` — inkluder enhetsmodell, appversjon (Innstillinger → nederst) og en beskrivelse av hva du prøvde.
