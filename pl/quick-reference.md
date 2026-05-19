# NVH Source Locator — Skrócona instrukcja

Jednostronicowe podsumowanie. Pełne szczegóły znajdziesz w `user-guide.md`.

---

## Główny przepływ (2-Sensor, bezpłatny)

1. **Wybierz materiał** — karta Materials → dotknij swojego materiału
2. **Wprowadź kalibrację** w karcie 2-Sensor:
   - Odstęp między czujnikami (`d`)
   - Opóźnienie czasu kalibracji (`tCal`) — wypełnione automatycznie z materiału
3. **Wprowadź zdarzenie** — `tEvent` i Pierwszy czujnik (A lub B)
4. **Odczytaj wynik** — odległość od czujnika A

![Karta 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Wszystkie karty

| Karta | Wynik | Pola Pro? |
|---|---|---|
| 2-Sensor | Odległość wzdłuż linii | Nie (w pełni darmowe) |
| 3-Sensor | X, Y na powierzchni | Tak |
| 3-Sen+ | X, Y z LSQ na 3 parach | Tak |
| 4-Sensor | X, Y z dwóch par (A–B + C–D) | Tak |
| 4-Sen+ | X, Y z 4 czujników, dowolna pozycja | Tak |
| 3D | X, Y, Z z 4 czujników | Tak |
| 3D+ | X, Y, Z z maksymalnie 6 czujników | Tak |
| Materials | Wybór prędkości dźwięku | Nie |
| Help | Samouczki | Nie |

Ustawienia znajdują się w ikonie ⚙ (prawy górny róg), a nie jako karta.

---

## Kompensacja temperatury

Ustawienia → Temperatura odniesienia, zakres **od -40 do +200 °C**.

- **14 metali** ma wbudowaną kompensację (aluminium, stale, miedź, mosiądz, brąz, tytan, magnez, ołów, cynk, nikiel, wolfram, żelazo, żeliwo)
- Materiały bez kompensacji wyświetlają **„ref only"**
- **Resetuje się do 20 °C przy każdym uruchomieniu aplikacji** (bezpieczny domyślny start)
- Odtworzenie wpisu z historii przywraca jego oryginalną temperaturę

---

## Skróty

- **Dotknij materiału** → automatycznie wypełnia wszystkie pola `tCal` we wszystkich kartach
- **Przytrzymaj +/-** na polach liczbowych → szybkie inkrementowanie
- **Przeciągnij poziomo** na polu liczbowym → przewijanie wartości
- **Puste/ujemne/nieprawidłowe dane** → przeskakuje do 0 po utracie focusu (pole temperatury jest ograniczone do -40/200)
- **Oznacz materiał gwiazdką** → przenosi go na górę wyboru

---

## Model Pro

**Freemium z blokadą funkcji** ($19,99):
- Darmowy: karta 2-Sensor w pełni funkcjonalna, bez limitów
- Pro: Pozostałe karty dostępne, ale z **polami ze złotą kłódką**, które wyświetlają paywall po dotknięciu

Pro odblokowuje: od 3-Sensor do 3D+, własne materiały, kopię zapasową/przywracanie, raporty PDF, adnotacje zdjęć.

![Paywall](../screenshots/07-paywall.png)

---

## Raporty i kopia zapasowa

Przycisk **Drukuj wynik** na dowolnym ekranie wyników → PDF z nagłówkiem, danymi wejściowymi, wynikiem, wizualizacją, zdjęciem (jeśli wykonano) i stopką temperatury (gdy kompensacja jest aktywna).

Dostosuj nagłówek w Ustawienia → Nagłówek raportu.

**Kopia zapasowa**: Ustawienia → Kopia zapasowa → udostępnij do chmury/e-maila.  
**Przywróć**: Ustawienia → Przywróć → wybierz plik kopii zapasowej.

---

## Przywróć Pro na nowym urządzeniu

To samo konto Google (Android) lub Apple ID (iOS), z którego dokonano zakupu → Ustawienia → **Przywróć zakup** → odblokowuje w ciągu sekund.

Automatyczne przywracanie odbywa się dyskretnie po powrocie do aplikacji po zewnętrznym wykorzystaniu kodu promocyjnego.

---

## Szybkie rozwiązywanie problemów

- **Wynik poza zakresem?** Sprawdź znak `tEvent` / Pierwszy czujnik / odstęp między czujnikami
- **Nieprawidłowy najbliższy materiał?** Temperatura odniesienia prawdopodobnie została przypadkowo ustawiona — sprawdź ustawienia
- **Niepowodzenie przywracania zakupu?** Sprawdź to samo konto sklepu; zainstaluj ponownie, jeśli problem nie ustąpi
- **Pole zresetowane do 0?** Puste/ujemne dane są automatycznie ustawiane przy utracie focusu — wprowadź wartość ponownie
- **Brak przycisków steppera?** Pojawiają się obok pól z `data-step` — uruchom ponownie aplikację, jeśli ich brakuje
- **Ostrzeżenie o nieaktualnej temperaturze?** Resetuje się do 20 przy każdym uruchomieniu — ustaw ponownie dla tej sesji

---

Kontakt `support@evdiag.net` — podaj model urządzenia, wersję aplikacji (Ustawienia → dół) i opis tego, co próbowałeś.
