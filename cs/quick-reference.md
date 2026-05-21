# NVH Source Locator — Stručná příručka

Jednostránkový přehled. Úplné podrobnosti naleznete v **Uživatelská příručka**.

---

## Hlavní postup (2-Sensor, zdarma)

1. **Vyberte materiál** — záložka Materials → klepněte na materiál
2. **Zadejte kalibraci** v záložce 2-Sensor:
   - Vzdálenost senzorů (`d`)
   - Zpoždění kalibračního času (`tCal`) — automaticky vyplněno z materiálu
3. **Zadejte událost** — `tEvent` a První senzor (A nebo B)
4. **Přečtěte si výsledek** — vzdálenost od senzoru A

![Záložka 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Všechny záložky

| Záložka | Výstup | Pole Pro? |
|---|---|---|
| 2-Sensor | Vzdálenost podél čáry | Ne (zcela zdarma) |
| 3-Sensor | X, Y na ploše | Ano |
| 3-Sen+ | X, Y s LSQ ze 3 párů | Ano |
| 4-Sensor | X, Y ze dvou párů (A–B + C–D) | Ano |
| 4-Sen+ | X, Y ze 4 senzorů, libovolná poloha | Ano |
| 3D | X, Y, Z ze 4 senzorů | Ano |
| 3D+ | X, Y, Z až ze 6 senzorů | Ano |
| Materials | Výběr rychlosti zvuku | Ne |
| Help | Návody | Ne |

Nastavení se nachází pod ikonou ⚙ (vpravo nahoře), nikoli jako záložka.

---

## Teplotní kompenzace

Nastavení → Referenční teplota, rozsah **-40 až +200 °C**.

- **14 kovů** má vestavěnou kompenzaci (hliník, oceli, měď, mosaz, bronz, titan, hořčík, olovo, zinek, nikl, wolfram, železo, litina)
- Materiály bez kompenzace zobrazují **„ref only"**
- **Při každém spuštění aplikace se vrátí na 20 °C** (výchozí bezpečný start)
- Přehrání záznamu historie obnoví jeho původní teplotu

---

## Zkratky

- **Klepnutí na materiál** → automaticky vyplní všechna pole `tCal` ve všech záložkách
- **Podržení +/-** na číselných polích → rychlé zvyšování
- **Vodorovné přetažení** na číselném poli → posouvání hodnot
- **Prázdný/záporný/neplatný vstup** → při ztrátě fokusu se nastaví na 0 (teplotní pole se omezí na -40/200)
- **Označení materiálu hvězdou** → přesune ho na začátek výběru

---

## Model Pro

**Freemium s blokací funkcí** ($19,99):
- Zdarma: záložka 2-Sensor plně funkční, bez omezení
- Pro: Ostatní záložky jsou přístupné, ale obsahují **pole se zlatým zámkem**, která po klepnutí zobrazí paywall

Pro odemyká: 3-Sensor až 3D+, vlastní materiály, zálohu/obnovu, PDF zprávy, popisky fotografií.

![Paywall](../screenshots/07-paywall.png)

---

## Zprávy a záloha

Tlačítko **Tisk výsledku** na libovolné obrazovce s výsledky → PDF s hlavičkou, vstupy, výsledkem, vizualizací, fotografií (pokud byla pořízena) a zápatím s teplotou (když je kompenzace aktivní).

Hlavičku přizpůsobte v Nastavení → Hlavička zprávy.

**Záloha**: Nastavení → Záloha → sdílet do cloudu/e-mailu.  
**Obnova**: Nastavení → Obnova → vybrat záložní soubor.

---

## Obnovení Pro na novém zařízení

Stejný účet Google (Android) nebo Apple ID (iOS), se kterým jste si Pro koupili → Nastavení → **Obnovit nákup** → odemkne se během několika sekund.

Automatické obnovení proběhne tiše, když se po externím uplatnění promo kódu vrátíte do aplikace.

---

## Rychlé řešení problémů

- **Výsledek mimo rozsah?** Zkontrolujte znaménko `tEvent` / První senzor / vzdálenost senzorů
- **Špatný nejbližší materiál?** Referenční teplota je pravděpodobně nastavená omylem — zkontrolujte Nastavení
- **Obnovení nákupu selhává?** Ověřte stejný účet obchodu; pokud problém přetrvává, přeinstalujte
- **Pole nastaveno na 0?** Prázdné/záporné vstupy se automaticky nastaví při ztrátě fokusu — zadejte hodnotu znovu
- **Tlačítka stepperu zmizela?** Zobrazují se vedle polí s `data-step` — restartujte aplikaci, pokud chybí
- **Varování o zastaralé teplotě?** Při každém spuštění se resetuje na 20 — pro tuto relaci znovu nastavte

---

Kontakt `support@evdiag.net` — uveďte model zařízení, verzi aplikace (Nastavení → dole) a popis toho, co jste zkusili.
