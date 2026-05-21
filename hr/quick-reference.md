# NVH Source Locator — Kratki priručnik

Jednostranični pregled. Za pune detalje pogledajte **Korisnički priručnik**.

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
