# NVH Source Locator — Pikaviite

Yhden sivun yhteenveto. Täydet tiedot löytyvät `user-guide.md` -tiedostosta.

---

## Pääprosessi (2-Sensor, ilmainen)

1. **Valitse materiaali** — Materials-välilehti → napauta materiaalia
2. **Anna kalibrointi** 2-Sensor-välilehdellä:
   - Antureiden välimatka (`d`)
   - Kalibrointiajan viive (`tCal`) — täyttyy automaattisesti materiaalista
3. **Anna tapahtuma** — `tEvent` ja Ensimmäinen anturi (A tai B)
4. **Lue tulos** — etäisyys anturista A

![2-Sensor välilehti](../screenshots/01-home-2sensor.png)

---

## Kaikki välilehdet

| Välilehti | Tuloste | Pro-kentät? |
|---|---|---|
| 2-Sensor | Etäisyys viivaa pitkin | Ei (täysin ilmainen) |
| 3-Sensor | X, Y pinnalla | Kyllä |
| 3-Sen+ | X, Y LSQ:lla 3 parista | Kyllä |
| 4-Sensor | X, Y kahdesta parista (A–B + C–D) | Kyllä |
| 4-Sen+ | X, Y 4 anturista, mikä tahansa sijainti | Kyllä |
| 3D | X, Y, Z 4 anturista | Kyllä |
| 3D+ | X, Y, Z enintään 6 anturista | Kyllä |
| Materials | Äänennopeuden valitsin | Ei |
| Help | Oppaat | Ei |

Asetukset löytyvät ⚙-kuvakkeen alta (oikealla ylhäällä), ei välilehdeltä.

---

## Lämpötilakompensointi

Asetukset → Vertailulämpötila, alue **-40 - +200 °C**.

- **14 metallia** sisältää sisäänrakennetun kompensoinnin (alumiini, teräkset, kupari, messinki, pronssi, titaani, magnesium, lyijy, sinkki, nikkeli, volframi, rauta, valurauta)
- Materiaalit ilman kompensointia näyttävät **"ref only"**
- **Palautuu 20 °C:een jokaisella sovelluksen käynnistyksellä** (oletusturvallinen aloitus)
- Historiamerkinnän toistaminen palauttaa sen alkuperäisen lämpötilan

---

## Pikanäppäimet

- **Napauta materiaalia** → täyttää kaikki `tCal`-kentät automaattisesti kaikilla välilehdillä
- **Pidä +/-** numerokentissä → nopea lisäys
- **Vedä vaakasuoraan** numerokentällä → arvojen vierittäminen
- **Tyhjä/negatiivinen/virheellinen syöte** → asettuu nollaan kohdistuksen menetyksessä (lämpötilakenttä lukittuu -40/200)
- **Merkitse materiaali tähdellä** → siirtää sen valitsimen yläosaan

---

## Pro-malli

**Ominaisuuslukittu freemium** ($19,99):
- Ilmainen: 2-Sensor välilehti täysin toimiva, ei rajoituksia
- Pro: Muut välilehdet käytettävissä, mutta sisältävät **kultaisia lukko-kenttiä**, jotka näyttävät paywallin napautettaessa

Pro avaa: 3-Sensor - 3D+, mukautetut materiaalit, varmuuskopiointi/palautus, PDF-raportit, valokuvan annotointi.

![Paywall](../screenshots/07-paywall.png)

---

## Raportit ja varmuuskopiointi

**Tulosta tulos** -painike millä tahansa tulosnäytöllä → PDF, jossa on otsikko, syötteet, tulos, visualisointi, valokuva (jos otettu) ja lämpötila-alatunniste (kun kompensointi on aktiivinen).

Mukauta otsikkoa kohdassa Asetukset → Raportin otsikko.

**Varmuuskopiointi**: Asetukset → Varmuuskopiointi → jaa pilveen/sähköpostiin.  
**Palautus**: Asetukset → Palautus → valitse varmuuskopiotiedosto.

---

## Pron palauttaminen uuteen laitteeseen

Sama Google-tili (Android) tai Apple ID (iOS), jolla ostit → Asetukset → **Palauta ostos** → avautuu sekunneissa.

Automaattinen palautus tapahtuu hiljaa, kun palaat sovellukseen lunastettuasi promokoodin ulkopuolella.

---

## Nopea vianetsintä

- **Tulos alueen ulkopuolella?** Tarkista `tEvent`-merkki / Ensimmäinen anturi / antureiden välimatka
- **Väärä lähin materiaali?** Vertailulämpötila on todennäköisesti vahingossa asetettu — tarkista Asetukset
- **Ostoksen palauttaminen epäonnistuu?** Vahvista sama kaupan tili; asenna uudelleen, jos ongelma jatkuu
- **Kenttä asetettu nollaan?** Tyhjät/negatiiviset syötteet asettuvat automaattisesti kohdistuksen menetyksessä — syötä arvo uudelleen
- **Lisäyspainikkeet poissa?** Ne näkyvät `data-step`-kenttien vieressä — käynnistä sovellus uudelleen, jos puuttuvat
- **Vanhentunut lämpötilavaroitus?** Palautuu 20:een jokaisella käynnistyksellä — aseta uudelleen tälle istunnolle

---

Yhteystiedot `support@evdiag.net` — sisällytä laitemalli, sovelluksen versio (Asetukset → alaosa) ja kuvaus siitä, mitä yritit.
