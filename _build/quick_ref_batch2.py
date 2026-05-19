"""Quick Reference translations — batch 2.

8 more languages: cs, sk, hu, hr, bg, sv, no, fi.
"""

QUICK_REF_TRANSLATIONS = {

'cs': """# NVH Source Locator — Stručná příručka

Jednostránkový přehled. Úplné podrobnosti naleznete v `user-guide.md`.

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
""",

'sk': """# NVH Source Locator — Stručná príručka

Jednostranový prehľad. Úplné podrobnosti nájdete v `user-guide.md`.

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
""",

'hu': """# NVH Source Locator — Gyors útmutató

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
""",

'hr': """# NVH Source Locator — Kratki priručnik

Jednostranični pregled. Za pune detalje pogledajte `user-guide.md`.

---

## Glavni tijek (2-Sensor, besplatno)

1. **Odaberite materijal** — kartica Materials → dodirnite materijal
2. **Unesite kalibraciju** na kartici 2-Sensor:
   - Razmak između senzora (`d`)
   - Kašnjenje vremena kalibracije (`tCal`) — automatski popunjeno iz materijala
3. **Unesite događaj** — `tEvent` i Prvi senzor (A ili B)
4. **Pročitajte rezultat** — udaljenost od senzora A

![Kartica 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Sve kartice

| Kartica | Izlaz | Pro polja? |
|---|---|---|
| 2-Sensor | Udaljenost duž linije | Ne (potpuno besplatno) |
| 3-Sensor | X, Y na površini | Da |
| 3-Sen+ | X, Y s LSQ-om iz 3 para | Da |
| 4-Sensor | X, Y iz dva para (A–B + C–D) | Da |
| 4-Sen+ | X, Y iz 4 senzora, bilo koja pozicija | Da |
| 3D | X, Y, Z iz 4 senzora | Da |
| 3D+ | X, Y, Z iz najviše 6 senzora | Da |
| Materials | Birač brzine zvuka | Ne |
| Help | Vodiči | Ne |

Postavke se nalaze pod ikonom ⚙ (gore desno), a ne kao kartica.

---

## Temperaturna kompenzacija

Postavke → Referentna temperatura, raspon **-40 do +200 °C**.

- **14 metala** ima ugrađenu kompenzaciju (aluminij, čelici, bakar, mjed, bronca, titan, magnezij, olovo, cink, nikal, volfram, željezo, lijevano željezo)
- Materijali bez kompenzacije prikazuju **„ref only"**
- **Resetira se na 20 °C pri svakom pokretanju aplikacije** (zadani siguran početak)
- Reprodukcija unosa povijesti vraća izvornu temperaturu

---

## Prečaci

- **Dodir na materijal** → automatski popunjava sva `tCal` polja na svim karticama
- **Držite +/-** na brojčanim poljima → brzo povećanje
- **Vodoravno povlačenje** po brojčanom polju → mijenjanje vrijednosti
- **Prazan/negativan/neispravan unos** → resetira se na 0 pri gubitku fokusa (polje temperature ograničeno na -40/200)
- **Označi materijal zvjezdicom** → premješta ga na vrh izbornika

---

## Pro model

**Freemium s zaključanim značajkama** ($19,99):
- Besplatno: kartica 2-Sensor potpuno funkcionalna, bez ograničenja
- Pro: Druge kartice dostupne, ali sa **zlatnim katancima na poljima** koji pri dodiru prikazuju paywall

Pro otključava: 3-Sensor do 3D+, prilagođene materijale, sigurnosno kopiranje/vraćanje, PDF izvješća, označavanje fotografija.

![Paywall](../screenshots/07-paywall.png)

---

## Izvješća i sigurnosno kopiranje

Gumb **Ispiši rezultat** na bilo kojem zaslonu rezultata → PDF sa zaglavljem, ulazima, rezultatom, vizualizacijom, fotografijom (ako je snimljena) i podnožjem s temperaturom (kada je kompenzacija aktivna).

Prilagodite zaglavlje u Postavke → Zaglavlje izvješća.

**Sigurnosno kopiranje**: Postavke → Sigurnosno kopiranje → dijeljenje u oblak/e-poštom.  
**Vraćanje**: Postavke → Vraćanje → odaberite datoteku kopije.

---

## Vraćanje Pro-a na novom uređaju

Isti Google račun (Android) ili Apple ID (iOS) s kojim ste kupili → Postavke → **Vrati kupnju** → otključava se za nekoliko sekundi.

Automatsko vraćanje događa se tiho kada se vratite u aplikaciju nakon vanjske primjene promotivnog koda.

---

## Brzo rješavanje problema

- **Rezultat izvan raspona?** Provjerite predznak `tEvent` / Prvi senzor / razmak senzora
- **Pogrešan najbliži materijal?** Referentna temperatura vjerojatno je slučajno postavljena — provjerite postavke
- **Vraćanje kupnje ne uspijeva?** Provjerite isti račun trgovine; ponovno instalirajte ako problem traje
- **Polje postavljeno na 0?** Prazni/negativni unosi automatski se postavljaju pri gubitku fokusa — ponovno unesite vrijednost
- **Nestale tipke step-pera?** Pojavljuju se uz polja s `data-step` — ponovno pokrenite aplikaciju ako nedostaju
- **Upozorenje o zastarjeloj temperaturi?** Resetira se na 20 pri svakom pokretanju — ponovno postavite za ovu sesiju

---

Kontakt `support@evdiag.net` — navedite model uređaja, verziju aplikacije (Postavke → dno) i opis onoga što ste pokušali.
""",

'bg': """# NVH Source Locator — Кратко справочно ръководство

Едностранично резюме. За пълни подробности вижте `user-guide.md`.

---

## Основен процес (2-Sensor, безплатно)

1. **Изберете материал** — раздел Materials → докоснете вашия материал
2. **Въведете калибриране** в раздела 2-Sensor:
   - Разстояние между сензорите (`d`)
   - Закъснение на времето за калибриране (`tCal`) — автоматично попълнено от материала
3. **Въведете събитие** — `tEvent` и Първи сензор (A или B)
4. **Прочетете резултата** — разстояние от сензор A

![Раздел 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Всички раздели

| Раздел | Изход | Полета Pro? |
|---|---|---|
| 2-Sensor | Разстояние по линия | Не (изцяло безплатно) |
| 3-Sensor | X, Y на повърхност | Да |
| 3-Sen+ | X, Y с LSQ от 3 двойки | Да |
| 4-Sensor | X, Y от две двойки (A–B + C–D) | Да |
| 4-Sen+ | X, Y от 4 сензора, произволна позиция | Да |
| 3D | X, Y, Z от 4 сензора | Да |
| 3D+ | X, Y, Z от до 6 сензора | Да |
| Materials | Селектор на скорост на звука | Не |
| Help | Уроци | Не |

Настройките се намират в иконата ⚙ (горе вдясно), а не като раздел.

---

## Температурна компенсация

Настройки → Референтна температура, диапазон **-40 до +200 °C**.

- **14 метала** имат вградена компенсация (алуминий, стомани, мед, месинг, бронз, титан, магнезий, олово, цинк, никел, волфрам, желязо, чугун)
- Материалите без компенсация показват **„ref only"**
- **Нулира се до 20 °C при всяко стартиране на приложението** (безопасен старт по подразбиране)
- Възпроизвеждането на запис от историята възстановява първоначалната му температура

---

## Бързи команди

- **Докосване на материал** → автоматично попълва всички `tCal` полета във всички раздели
- **Задържане на +/-** на числови полета → бързо увеличаване
- **Хоризонтално плъзгане** върху числово поле → превъртане на стойностите
- **Празно/отрицателно/невалидно въвеждане** → при загуба на фокус се настройва на 0 (полето за температура се ограничава до -40/200)
- **Маркиране на материал със звезда** → премества го в горната част на селектора

---

## Pro модел

**Freemium с заключени функции** ($19,99):
- Безплатно: разделът 2-Sensor е напълно функционален, без ограничения
- Pro: Други раздели са достъпни, но имат **полета със златен катинар**, които показват paywall при докосване

Pro отключва: 3-Sensor до 3D+, потребителски материали, архивиране/възстановяване, PDF отчети, анотация на снимки.

![Paywall](../screenshots/07-paywall.png)

---

## Отчети и архивиране

Бутонът **Печат на резултата** на всеки екран с резултати → PDF с заглавна част, входни данни, резултат, визуализация, снимка (ако е направена) и долен колонтитул с температура (когато компенсацията е активна).

Персонализирайте заглавната част в Настройки → Заглавна част на отчета.

**Архивиране**: Настройки → Архивиране → споделяне в облак/имейл.  
**Възстановяване**: Настройки → Възстановяване → изберете архивен файл.

---

## Възстановяване на Pro на ново устройство

Същият Google акаунт (Android) или Apple ID (iOS), с който сте купили → Настройки → **Възстановяване на покупка** → отключва се за секунди.

Автоматичното възстановяване се случва тихо, когато се върнете в приложението след външно изкупуване на промо код.

---

## Бързо отстраняване на проблеми

- **Резултат извън диапазона?** Проверете знака на `tEvent` / Първи сензор / разстоянието между сензорите
- **Грешен най-близък материал?** Референтната температура вероятно е зададена случайно — проверете Настройките
- **Възстановяването на покупката е неуспешно?** Проверете същия акаунт на магазина; преинсталирайте, ако проблемът продължава
- **Полето е зададено на 0?** Празните/отрицателни входни данни автоматично се настройват при загуба на фокус — въведете отново стойността
- **Изчезнали бутони на стъпковия инструмент?** Появяват се до полета с `data-step` — рестартирайте приложението, ако липсват
- **Предупреждение за остаряла температура?** Нулира се до 20 при всяко стартиране — задайте отново за тази сесия

---

Контакт `support@evdiag.net` — посочете модел на устройството, версия на приложението (Настройки → долу) и описание на това, което сте опитали.
""",

'sv': """# NVH Source Locator — Snabbreferens

En sammanfattning på en sida. För fullständiga detaljer, se `user-guide.md`.

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
""",

'no': """# NVH Source Locator — Hurtigreferanse

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
""",

'fi': """# NVH Source Locator — Pikaviite

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
""",

}
