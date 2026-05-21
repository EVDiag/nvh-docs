# NVH Source Locator — Stručná príručka

Jednostranový prehľad. Úplné podrobnosti nájdete v **Používateľská príručka**.

---

## Hlavný postup (2-Sensor, zadarmo)

1. **Vyberte materiál** — záložka Materials → klepnite na materiál
2. **Zadajte kalibráciu** v záložke 2-Sensor:
   - Vzdialenosť senzorov (`d`)
   - Oneskorenie kalibračného času (`tCal`) — automaticky vyplnené z materiálu
3. **Zadajte udalosť** — `tEvent` a Prvý senzor (A alebo B)
4. **Prečítajte si výsledok** — vzdialenosť od senzora A

![Záložka 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Všetky záložky

| Záložka | Výstup | Polia Pro? |
|---|---|---|
| 2-Sensor | Vzdialenosť pozdĺž čiary | Nie (úplne zadarmo) |
| 3-Sensor | X, Y na ploche | Áno |
| 3-Sen+ | X, Y s LSQ z 3 párov | Áno |
| 4-Sensor | X, Y z dvoch párov (A–B + C–D) | Áno |
| 4-Sen+ | X, Y zo 4 senzorov, ľubovoľná poloha | Áno |
| 3D | X, Y, Z zo 4 senzorov | Áno |
| 3D+ | X, Y, Z až zo 6 senzorov | Áno |
| Materials | Výber rýchlosti zvuku | Nie |
| Help | Návody | Nie |

Nastavenia sa nachádzajú pod ikonou ⚙ (vpravo hore), nie ako záložka.

---

## Teplotná kompenzácia

Nastavenia → Referenčná teplota, rozsah **-40 až +200 °C**.

- **14 kovov** má zabudovanú kompenzáciu (hliník, ocele, meď, mosadz, bronz, titán, horčík, olovo, zinok, nikel, volfrám, železo, liatina)
- Materiály bez kompenzácie zobrazujú **„ref only"**
- **Pri každom spustení aplikácie sa vráti na 20 °C** (predvolený bezpečný štart)
- Prehratie záznamu histórie obnoví jeho pôvodnú teplotu

---

## Skratky

- **Klepnutie na materiál** → automaticky vyplní všetky polia `tCal` vo všetkých záložkách
- **Podržanie +/-** na číselných poliach → rýchle zvyšovanie
- **Vodorovné potiahnutie** na číselnom poli → posúvanie hodnôt
- **Prázdny/záporný/neplatný vstup** → pri strate fokusu sa nastaví na 0 (teplotné pole sa obmedzí na -40/200)
- **Označenie materiálu hviezdou** → presunie ho na začiatok výberu

---

## Model Pro

**Freemium s blokádou funkcií** ($19,99):
- Zadarmo: záložka 2-Sensor plne funkčná, bez obmedzení
- Pro: Ostatné záložky sú prístupné, ale obsahujú **polia so zlatým zámkom**, ktoré po klepnutí zobrazia paywall

Pro odomkne: 3-Sensor až 3D+, vlastné materiály, zálohu/obnovu, PDF správy, popisky fotografií.

![Paywall](../screenshots/07-paywall.png)

---

## Správy a záloha

Tlačidlo **Tlačiť výsledok** na ľubovoľnej obrazovke s výsledkami → PDF s hlavičkou, vstupmi, výsledkom, vizualizáciou, fotografiou (ak bola urobená) a pätou s teplotou (keď je kompenzácia aktívna).

Hlavičku prispôsobte v Nastavenia → Hlavička správy.

**Záloha**: Nastavenia → Záloha → zdieľať do cloudu/e-mailu.  
**Obnova**: Nastavenia → Obnova → vybrať záložný súbor.

---

## Obnovenie Pro na novom zariadení

Rovnaký účet Google (Android) alebo Apple ID (iOS), s ktorým ste si Pro kúpili → Nastavenia → **Obnoviť nákup** → odomkne sa v priebehu niekoľkých sekúnd.

Automatické obnovenie prebehne potichu, keď sa po externom uplatnení promo kódu vrátite do aplikácie.

---

## Rýchle riešenie problémov

- **Výsledok mimo rozsah?** Skontrolujte znamienko `tEvent` / Prvý senzor / vzdialenosť senzorov
- **Nesprávny najbližší materiál?** Referenčná teplota je pravdepodobne nastavená omylom — skontrolujte Nastavenia
- **Obnovenie nákupu zlyháva?** Overte rovnaký účet obchodu; ak problém pretrváva, preinštalujte
- **Pole nastavené na 0?** Prázdne/záporné vstupy sa automaticky nastavia pri strate fokusu — zadajte hodnotu znova
- **Tlačidlá stepperu zmizli?** Zobrazujú sa vedľa polí s `data-step` — reštartujte aplikáciu, ak chýbajú
- **Varovanie o zastaranej teplote?** Pri každom spustení sa resetuje na 20 — pre túto reláciu znova nastavte

---

Kontakt `support@evdiag.net` — uveďte model zariadenia, verziu aplikácie (Nastavenia → dole) a popis toho, čo ste skúsili.
