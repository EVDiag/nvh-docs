# NVH Source Locator — Gyors útmutató

Egyoldalas összefoglaló. A teljes részletekért lásd `user-guide.md`.

---

## Alapfolyamat (2-Sensor, ingyenes)

1. **Válasszon anyagot** — Materials fül → koppintson az anyagra
2. **Adja meg a kalibrációt** a 2-Sensor fülön:
   - Érzékelők távolsága (`d`)
   - Kalibrációs idő késleltetése (`tCal`) — automatikusan kitöltve az anyagból
3. **Adja meg az eseményt** — `tEvent` és Első érzékelő (A vagy B)
4. **Olvassa le az eredményt** — távolság az A érzékelőtől

![2-Sensor fül](../screenshots/01-home-2sensor.png)

---

## Összes fül

| Fül | Kimenet | Pro mezők? |
|---|---|---|
| 2-Sensor | Távolság a vonal mentén | Nem (teljesen ingyenes) |
| 3-Sensor | X, Y egy felületen | Igen |
| 3-Sen+ | X, Y LSQ-val 3 páron | Igen |
| 4-Sensor | X, Y két párból (A–B + C–D) | Igen |
| 4-Sen+ | X, Y 4 érzékelőből, tetszőleges pozíció | Igen |
| 3D | X, Y, Z 4 érzékelőből | Igen |
| 3D+ | X, Y, Z legfeljebb 6 érzékelőből | Igen |
| Materials | Hangsebesség választó | Nem |
| Help | Oktatóanyagok | Nem |

A beállítások a ⚙ ikon alatt találhatók (jobbra fent), nem fülként.

---

## Hőmérséklet-kompenzáció

Beállítások → Referencia hőmérséklet, tartomány **-40 - +200 °C**.

- **14 fém** rendelkezik beépített kompenzációval (alumínium, acélok, réz, sárgaréz, bronz, titán, magnézium, ólom, cink, nikkel, volfrám, vas, öntöttvas)
- A kompenzáció nélküli anyagok a **„ref only"** feliratot mutatják
- **Minden app-indításkor 20 °C-ra áll vissza** (alapértelmezett biztonságos indítás)
- Az előzményeb bejegyzés visszajátszása helyreállítja eredeti hőmérsékletét

---

## Gyorsbillentyűk

- **Koppintson egy anyagra** → automatikusan kitölti az összes `tCal` mezőt az összes fülön
- **Tartsa lenyomva +/-** a számmezőkön → gyors növelés
- **Húzza vízszintesen** egy számmezőn → értékek görgetése
- **Üres/negatív/érvénytelen bemenet** → fókusz elvesztésekor 0-ra áll (a hőmérsékleti mező -40/200-ra korlátozódik)
- **Csillagozzon egy anyagot** → a választó tetejére helyezi

---

## Pro modell

**Funkció-zárolt freemium** ($19,99):
- Ingyenes: 2-Sensor fül teljesen funkcionális, korlátozások nélkül
- Pro: Más fülek elérhetők, de **arany lakat mezőket** tartalmaznak, amelyek koppintáskor megjelenítik a paywallt

A Pro feloldja: 3-Sensor-tól 3D+-ig, egyéni anyagok, biztonsági mentés/visszaállítás, PDF jelentések, fénykép-annotáció.

![Paywall](../screenshots/07-paywall.png)

---

## Jelentések és biztonsági mentés

Az **Eredmény nyomtatása** gomb bármely eredményképernyőn → PDF fejléccel, bemenetekkel, eredménnyel, vizualizációval, fényképpel (ha készült) és hőmérsékleti lábléccel (amikor a kompenzáció aktív).

A fejlécet a Beállítások → Jelentés fejléce alatt szabhatja testre.

**Biztonsági mentés**: Beállítások → Biztonsági mentés → megosztás felhőre/e-mailre.  
**Visszaállítás**: Beállítások → Visszaállítás → mentési fájl kiválasztása.

---

## Pro visszaállítása új eszközön

Ugyanaz a Google fiók (Android) vagy Apple ID (iOS), amellyel megvásárolta → Beállítások → **Vásárlás visszaállítása** → másodperceken belül feloldja.

Az automatikus visszaállítás csendben történik, amikor visszatér az alkalmazásba egy promóciós kód külső beváltása után.

---

## Gyors hibaelhárítás

- **Eredmény tartományon kívül?** Ellenőrizze a `tEvent` előjelét / Első érzékelőt / érzékelők távolságát
- **Rossz legközelebbi anyag?** A referencia hőmérséklet valószínűleg véletlenül van beállítva — ellenőrizze a Beállításokat
- **Vásárlás visszaállítása sikertelen?** Ellenőrizze az azonos áruházi fiókot; ha továbbra is fennáll, telepítse újra
- **Mező 0-ra állítva?** Az üres/negatív bemenetek automatikusan beállnak a fókusz elvesztésekor — adja meg újra az értéket
- **Eltűntek a léptetőgombok?** A `data-step` mezők mellett jelennek meg — indítsa újra az alkalmazást, ha hiányoznak
- **Elavult hőmérséklet figyelmeztetés?** Minden induláskor 20-ra áll vissza — állítsa be újra ehhez a munkamenethez

---

Kapcsolat `support@evdiag.net` — adja meg az eszköz modelljét, az alkalmazás verzióját (Beállítások → alul) és a leírást arról, mit próbált.
