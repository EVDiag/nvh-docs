# NVH Source Locator — Käyttöopas

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

![2-Sensor-välilehti](../screenshots/01b-home-2sensor.png)

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
