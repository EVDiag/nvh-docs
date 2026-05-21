# NVH Source Locator — Podręcznik użytkownika

NVH Source Locator to narzędzie pomiarowe do lokalizowania źródeł hałasu i drgań przy użyciu TDOA (Time Difference of Arrival) z sygnałów akcelerometrów rejestrowanych na oscyloskopie lub systemie pomiarowym.

Ten przewodnik obejmuje wszystkie funkcje. Aby uzyskać szybkie przypomnienie, zobacz **Skrócona instrukcja**.

---

## Spis treści

1. [Jak to działa](#how-it-works)
2. [Przed rozpoczęciem](#before-you-start)
3. [Główne karty](#the-main-tabs)
4. [Tryb 2-Sensor](#2-sensor-mode)
5. [Tryb 3-Sensor](#3-sensor-mode)
6. [Tryby Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Karta Materials](#the-materials-tab)
8. [Kompensacja temperatury](#temperature-compensation)
9. [Adnotacja zdjęć](#photo-annotation)
10. [Raporty](#reports)
11. [Kopia zapasowa i przywracanie](#backup-and-restore)
12. [Ustawienia](#settings)
13. [Funkcje Pro](#pro-features)
14. [Karta Help i samouczki](#help-tab-and-tutorials)
15. [Rozwiązywanie problemów](#troubleshooting)

---

## Jak to działa

Gdy źródło hałasu emituje dźwięk lub drgania, fala przemieszcza się przez materiał z określoną prędkością. Jeśli umieścisz dwa lub więcej akcelerometrów na materiale i zmierzysz, kiedy fala dociera do każdego z nich, różnica czasu wskaże, gdzie znajduje się źródło.

NVH Source Locator pobiera:

- **Kalibrację**: odległość między czujnikami i czas, jaki fala potrzebuje, aby przebyć tę odległość (używane do obliczenia prędkości dźwięku materiału)
- **Zdarzenie**: różnicę czasu między czujnikami wykrywającymi zdarzenie hałasu/drgań

Następnie oblicza, gdzie znajduje się źródło w strukturze.

Im więcej czujników użyjesz, tym dokładniej zlokalizujesz źródło:

- **2 czujniki** → odległość wzdłuż linii
- **3 czujniki** → położenie na powierzchni 2D (X, Y)
- **4 czujniki** → położenie w przestrzeni 3D (X, Y, Z)

---

## Przed rozpoczęciem

Będziesz potrzebować:

- **Oscyloskopu lub systemu pomiarowego**, który może pokazać różnicę czasu między kanałami akcelerometru w mikrosekundach (µs)
- **Co najmniej 2 akcelerometrów** fizycznie zamocowanych do struktury (więcej czujników = większa dokładność)
- **Sposób na pomiar odległości** między czujnikami (miarka, suwmiarki)
- **Sposób na wywołanie fali** w znanym miejscu do kalibracji (kalibrowane uderzenie młotka, stuknięcie śrubokrętem lub inny znany sygnał)

![Ekran główny z kartą 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Główne karty

Aplikacja ma karty u góry:

![Pasek kart](../screenshots/02-tab-bar.png)

| Karta | Co robi | Kiedy używać |
|---|---|---|
| **2-Sensor** | Lokalizacja źródła 1D wzdłuż linii między 2 czujnikami | Szybkie sprawdzenia, struktury typu belka. **W pełni darmowe.** |
| **3-Sensor** | Lokalizacja źródła 2D z użyciem 3 czujników w trójkącie | Najczęstsze zastosowanie, panele i powierzchnie |
| **3-Sen+** | 3-Sensor z nadokreślonym solverem najmniejszych kwadratów | Bardziej wymagające pomiary, odporne na szum |
| **4-Sensor** | Lokalizacja 2D z użyciem dwóch par (A-B + C-D) | Prostokątne układy czujników, weryfikacja krzyżowa |
| **4-Sen+** | Zaawansowany tryb 2D, 4 czujniki w dowolnych pozycjach | Geometrie nieprostokątne, pełne LSQ |
| **3D** | Lokalizacja źródła 3D z użyciem 4 czujników ze współrzędnymi XYZ | Złożone struktury w przestrzeni 3D |
| **3D+** | 3D z maksymalnie 6 czujnikami, nadokreślone LSQ | Bardzo złożone geometrie, maksymalna precyzja |
| **Materials** | Biblioteka prędkości dźwięku + materiały niestandardowe | Wybierz raz na sesję pomiarową |
| **Help** | Samouczki w aplikacji i odniesienia | Gdy potrzebujesz szybkiego przypomnienia |

> **Darmowe vs Pro**: Karta 2-Sensor jest w pełni darmowa. Inne karty są dostępne, ale mają określone pola wejściowe zablokowane dla użytkowników Pro (oznaczone złotą plakietką kłódki). Dotknięcie zablokowanego pola pokazuje paywall Pro.

Ustawienia są dostępne przez ikonę koła zębatego ⚙ w prawym górnym rogu (nie jest to karta).

---

## Tryb 2-Sensor

Najprostszy pomiar: lokalizacja źródła wzdłuż linii między dwoma akcelerometrami.

![Karta 2-Sensor](../screenshots/01-home-2sensor.png)

### Krok 1: Zastosuj materiał

Dotknij karty Materials. Wybierz materiał, z którego wykonana jest twoja struktura (np. „Aluminium", „Stal, Mild (1020)"). Aplikacja używa znanej prędkości dźwięku materiału, aby automatycznie wypełnić pole czasu kalibracji.

Jeśli materiał twojej struktury nie znajduje się na liście, możesz tymczasowo wybrać „Powietrze" i ręcznie zastąpić czas kalibracji w kroku 2.

### Krok 2: Wprowadź dane kalibracyjne

Na karcie 2-Sensor zobaczysz dwie sekcje par: **Para A–B** i **Para A–C** (tylko A–B jest wymagana, jeśli masz tylko 2 czujniki).

Dla każdej pary wypełniasz:

- **Odstęp czujników** (`d`): fizyczna odległość między czujnikami, w cm lub calach (ustawione w Ustawieniach)
- **Opóźnienie czasu kalibracji** (`tCal`): czas potrzebny fali do przebycia odległości między czujnikami z prędkością dźwięku materiału — wypełniane automatycznie po wybraniu materiału, ale możesz nadpisać

### Krok 3: Wprowadź czas zdarzenia

- **Opóźnienie czasu zdarzenia** (`tEvent`): różnica czasu między czujnikami wykrywającymi zdarzenie hałasu, w mikrosekundach
- **Pierwszy czujnik**: który czujnik usłyszał zdarzenie jako pierwszy (A lub B)

### Krok 4: Odczytaj wynik

Aplikacja pokazuje położenie źródła jako odległość od czujnika A:
- Wynik = 0: źródło jest przy czujniku A
- Wynik = odległość: źródło jest przy czujniku B
- Wynik pomiędzy: źródło jest między nimi
- Wynik na zewnątrz: źródło jest poza jednym z czujników (toast ostrzeże)

Karta wyniku pokazuje obie odległości (od A, od B) i wskazuje, który czujnik jest bliżej.

### Krok 5 (opcjonalny): Adnotacja zdjęcia

Dotknij **📷 Adnotuj zdjęcie**, aby zrobić zdjęcie swojej konfiguracji. Aplikacja nakłada znaczniki dla czujników A, B i źródła. Przydatne dla raportów.

---

## Tryb 3-Sensor

Lokalizuje źródło na płaszczyźnie 2D przy użyciu trzech czujników ułożonych w trójkąt.

![Karta 3-Sensor](../screenshots/03-3sensor-tab.png)

### Konfiguracja

Umieść trzy czujniki na strukturze, tworząc trójkąt. Równoboczny, prostokątny lub różnoboczny — aplikacja obsługuje wszystkie geometrie.

### Wprowadź dane

W sekcji **Długości boków trójkąta** wprowadź fizyczne odległości dla wszystkich trzech boków (A–B, A–C, B–C).

Dla każdej pary (A–B i A–C) wprowadź:
- **tCal**: czas kalibracji (automatycznie wypełniany z materiału)
- **tEvent**: zmierzona różnica czasu dla zdarzenia hałasu
- **Pierwszy czujnik**: który usłyszał jako pierwszy

### Odczytaj wynik

Aplikacja pokazuje położenie źródła jako współrzędne X, Y względem czujnika A (czujnik A w początku, czujnik B na osi X). Wizualizacja pokazuje wszystkie trzy czujniki i położenie źródła.

![Wynik trójkąta](../screenshots/04-triangle-result.png)

---

## Tryby Pro+

Kilka zaawansowanych kart oferuje nadokreślone solvery i wyższą wymiarowość:

### 3-Sen+ (Pro)

Ta sama konfiguracja trójkąta co 3-Sensor, ale skalibruj ORAZ zmierz wszystkie trzy pary (A–B, A–C, B–C). Solver używa wszystkich 3 TDOA w dopasowaniu najmniejszych kwadratów — bardziej odporny na szum pomiarowy i materiały anizotropowe. Reszty dla każdej pary są raportowane, dzięki czemu możesz zauważyć niespójne pomiary.

### 4-Sensor

Umieść cztery czujniki wokół obszaru:
- **A–B** = para pozioma (strony lewa/prawa)
- **C–D** = para pionowa (strony górna/dolna)

Uruchom najpierw parę A–B (poziomą), a następnie parę C–D (pionową). Mapa 2D pokazuje przecięcie. Każda para jest kalibrowana osobno — przydatne, gdy materiał różni się w obrębie struktury.

### 4-Sen+ (Zaawansowany 2D)

Cztery czujniki w dowolnych pozycjach (nie wymuszone prostokątne). Sparuj A z każdym z B, C, D i skalibruj osobno. Nadokreślony solver najmniejszych kwadratów uśrednia szum pomiarowy dla każdej pary i raportuje reszty dla każdej pary.

### 3D

Pełny pomiar 3D z 4 czujnikami umieszczonymi w przestrzeni 3D. Wprowadź współrzędne (X, Y, Z) każdego czujnika oraz czasy kalibracji i zdarzenia dla każdej pary (A–B, A–C, A–D).

### 3D+ (Pro)

Jak 3D, ale obsługuje do **6 czujników** (A do F) z nadokreślonym LSQ. Maksymalna precyzja dla złożonych geometrii 3D.

---

## Karta Materials

Biblioteka popularnych materiałów inżynieryjnych ze znaną prędkością dźwięku w 20 °C.

![Karta Materials](../screenshots/05-materials-tab.png)

### Lista materiałów

Lista obejmuje powietrze, płyny, gumy, polimery, drewno, szkła i metale. Prędkości wahają się od ~340 m/s (powietrze) do ~13 000 m/s (niektóre metale w temperaturze pokojowej).

### Wbudowane materiały z kompensacją temperatury

14 powszechnie używanych metali zawiera dane współczynnika temperatury. Gdy Temperatura odniesienia w Ustawieniach różni się od 20 °C, aplikacja automatycznie dostosowuje prędkości tych materiałów:

- Aluminium
- Stal, Mild (1020)
- Stal nierdzewna (304)
- Żelazo (lite)
- Żelazo
- Miedź
- Mosiądz
- Brąz
- Tytan
- Magnez
- Ołów
- Cynk
- Nikiel
- Wolfram

Materiały z kompensacją pokazują dwie wartości w selektorze: **prędkość skompensowaną** (duża, wyróżniona) i **prędkość odniesienia w 20 °C** (mała, szara poniżej).

Materiały bez kompensacji pokazują **„ref only"** kursywą — ich listowana prędkość jest używana bez zmian niezależnie od temperatury.

### Materiały niestandardowe

Jeśli zmierzysz kalibrację na karcie 2-Sensor, możesz zapisać wynik jako materiał niestandardowy. Po udanym pomiarze 2-sensor poszukaj opcji zapisania wyprowadzonej prędkości pod wybraną nazwą.

Materiały niestandardowe przechowują prędkość zmierzoną in-situ; nigdy nie stosują kompensacji temperatury (prędkość była już zmierzona w temperaturze testowej).

### Ulubione

Dotknij gwiazdki obok dowolnego materiału, aby oznaczyć go jako ulubiony. Ulubione pojawiają się na górze listy dla szybkiego dostępu.

### Wyszukiwanie

Użyj paska wyszukiwania u góry, aby filtrować materiały według nazwy. Wyszukiwanie pasuje zarówno do angielskich nazw kanonicznych, jak i przetłumaczonych nazw wyświetlanych.

---

## Kompensacja temperatury

Prędkość dźwięku w materiałach zmienia się wraz z temperaturą. W testach NVH motoryzacyjnych to ma znaczenie: komora silnika w 80 °C, zimna kabina w -10 °C lub obszar kolektora wydechowego w 200 °C zachowują się inaczej niż w laboratoryjnych warunkach pokojowych.

### Ustawianie temperatury

Otwórz Ustawienia (ikona ⚙) → Temperatura odniesienia. Wprowadź temperaturę środowiska testowego w °C (zakres -40 do +200).

![Panel Ustawienia](../screenshots/06-settings.png)

### Co się dzieje, gdy temperatura ≠ 20 °C

- Pola czasu kalibracji są automatycznie wypełniane prędkością dostosowaną do temperatury
- Selektor Materials pokazuje dostosowaną prędkość w widoczny sposób
- Toast potwierdza: *„Aluminium zastosowane (6 284 m/s @ 60 °C) — zaktualizowano N par"*
- Wskazówka „Najbliższy materiał" porównuje z prędkościami dostosowanymi do temperatury
- Zapisane wpisy historii rejestrują aktywną temperaturę
- Raporty zawierają linię stopki: *„Temperatura odniesienia: 60 °C, zastosowano kompensację"*

### Reset przy uruchomieniu aplikacji

Temperatura odniesienia **zawsze resetuje się do 20 °C** przy uruchomieniu aplikacji. Zapobiega to cichemu wpływaniu na dzisiejszą pracę nieaktualnych ustawień z poprzedniej sesji pomiarowej. Mała kursywna notatka w Ustawieniach przypomina o tym zachowaniu.

Jeśli chcesz odtworzyć historyczny pomiar w jego pierwotnej temperaturze, po prostu dotknij wpisu — temperatura zostanie automatycznie przywrócona.

### Materiały bez kompensacji

Większość materiałów niemetalicznych nie ma wiarygodnych opublikowanych współczynników temperatury. Aplikacja pokazuje plakietkę **„ref only"** dla nich — ich listowana prędkość jest używana niezależnie od ustawienia temperatury. Jeśli potrzebujesz dokładnych pomiarów w temperaturach innych niż pokojowe dla tych materiałów, przeprowadź kalibrację in-situ i zapisz wynik jako materiał niestandardowy.

---

## Adnotacja zdjęć

Po udanym obliczeniu dotknij przycisku **📷 Adnotuj zdjęcie**, aby nałożyć znaczniki czujników i źródła na zdjęcie swojej konfiguracji.

![Adnotacja zdjęcia](../screenshots/08-photo-annotation.png)

### Przebieg

1. Dotknij **Adnotuj zdjęcie** — otwiera się systemowa kamera
2. Zrób zdjęcie umiejscowienia czujników
3. Aplikacja ładuje zdjęcie do nakładki adnotacji
4. Znaczniki czujników (A, B, C, D, E, F w zależności od potrzeb — do 6 czujników) i znacznik źródła są automatycznie umieszczane na podstawie twojego obliczenia
5. Przeciągnij dowolny znacznik, aby dostroić położenie. Podczas dostrajania pozycja źródła jest ponownie obliczana z poprawionych pozycji czujników
6. Dotknij **Zapisz**, aby zachować, lub **Powtórz**, aby spróbować ponownie

Adnotowane zdjęcie jest automatycznie dołączane do raportów PDF.

---

## Raporty

Dotknij przycisku **Drukuj wynik** na dowolnym ekranie wyników, aby wygenerować sformatowany raport.

![Raport PDF](../screenshots/09-pdf-report.png)

### Zawartość raportu

- Nagłówek (konfigurowalny w Ustawienia → Nagłówek raportu)
- Tytuł pomiaru i znacznik czasu
- Wszystkie wartości wejściowe w przejrzystej tabeli
- Wynik obliczeń
- Tekst wniosku
- Wizualizacja (wykres geometrii)
- Adnotowane zdjęcie (jeśli zrobiłeś jedno)
- Linia stopki temperatury (jeśli kompensacja była aktywna)
- Numer strony i linia kredytowa

### Format wyjściowy

- **Android**: natywne generowanie PDF, zapisz na telefonie lub udostępnij
- **iOS**: systemowe okno drukowania → zapisz jako PDF, AirPrint lub udostępnij

### Dostosowywanie nagłówka

Ustawienia → Nagłówek raportu. Wprowadź nazwę firmy, nazwę laboratorium, informacje o projekcie lub cokolwiek, co chcesz mieć na górze każdego raportu.

---

## Kopia zapasowa i przywracanie

Zapisz wszystkie swoje materiały niestandardowe, ulubione, ustawienia i historię do jednego pliku. Przenoszenie między urządzeniami.

### Kopia zapasowa

Ustawienia → **Kopia zapasowa** → dotknij „Zapisz plik kopii zapasowej". Aplikacja generuje plik JSON i otwiera arkusz udostępniania telefonu. Zapisz go na dysku w chmurze (Google Drive, iCloud, OneDrive), wyślij sobie e-mailem lub przenieś w dowolny sposób.

### Przywracanie

Ustawienia → **Przywróć** → wybierz plik kopii zapasowej z pamięci telefonu. Aplikacja importuje materiały niestandardowe, ulubione, historię i ustawienia.

⚠️ **Przywracanie zastępuje twoje obecne dane.** Jeśli masz ważne pomiary na obecnym urządzeniu, najpierw zrób ich kopię zapasową przed przywracaniem z innej kopii zapasowej.

---

## Ustawienia

Dostęp przez ikonę koła zębatego ⚙ w prawym górnym rogu. Ustawienia są modalne, nie są kartą.

![Ustawienia](../screenshots/06-settings.png)

| Ustawienie | Co kontroluje |
|---|---|
| **Aktualizuj do Pro** | Kup lub dowiedz się o funkcjach Pro ($19,99) |
| **Język** | Język wyświetlania aplikacji (30 obsługiwanych) |
| **Motyw** | Jasny, Ciemny lub Auto (zgodnie z systemem) |
| **Jednostka odległości** | cm lub cale |
| **Temperatura odniesienia** | Aktywna temperatura dla kompensacji, -40 do +200 °C |
| **Nagłówek raportu** | Niestandardowy tekst na górze generowanych raportów |
| **Kopia zapasowa** | Eksportuj wszystkie dane do pliku |
| **Przywróć** | Importuj dane z pliku kopii zapasowej |
| **Przywróć zakup** | Ponownie zdobądź Pro na nowym urządzeniu |

---

## Funkcje Pro

NVH Source Locator używa **modelu freemium z blokadą funkcji**:

- **Darmowe**: Karta 2-Sensor jest w pełni funkcjonalna bez ograniczeń
- **Pro**: Wszystkie inne karty mają określone pola wejściowe zablokowane. Paywall pojawia się, gdy darmowy użytkownik dotyka zablokowanego pola

### Co jest zablokowane

Pola wymagające Pro są rozproszone w:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Trybach 3D i 3D+
- Kopii zapasowej i Przywracaniu
- Raportach PDF
- Materiałach niestandardowych
- Adnotacji zdjęć

Darmowy użytkownik może OTWORZYĆ dowolną kartę i ZOBACZYĆ interfejs. Po prostu nie może wprowadzać wartości w pola wejściowe zablokowane dla Pro.

![Pole zablokowane dla Pro](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Gdy darmowy użytkownik dotyka zablokowanego pola, paywall pojawia się pokazując:
- Ikonę aplikacji z plakietką PRO
- Listę funkcji
- Przycisk odblokowania z ceną ($19,99 domyślnie; może się różnić w zależności od regionu)
- Realizację kodu promocyjnego (tylko Android — iOS używa osobnego procesu Offer Code firmy Apple)
- Opcjonalny link promocyjny do kanałów społeczności

### Zakup Pro

Dotknij dowolnego zablokowanego pola lub dotknij **Aktualizuj do Pro** w Ustawieniach. Używa oficjalnego systemu płatności platformy (Google Play na Androidzie, Apple App Store na iOS).

### Przywracanie Pro na nowym urządzeniu

Jeśli zakupiłeś na jednym urządzeniu i chcesz Pro na innym (to samo konto):

1. Zaloguj się na **to samo** konto Google (Android) lub Apple ID (iOS), z którego dokonano zakupu
2. Otwórz NVH Source Locator na nowym urządzeniu
3. Przejdź do Ustawienia → **Przywróć zakup**
4. Aplikacja weryfikuje z rekordami zakupów platformy i odblokowuje Pro

### Auto-przywracanie przy uruchomieniu

Jeśli zrealizujesz kod promocyjny w Google Play Store lub App Store, gdy NVH Source Locator działa w tle, powrót do aplikacji automatycznie wykryje nowy zakup i odblokuje Pro — nie jest potrzebne ręczne Przywracanie.

### Realizacja kodu promocyjnego

**Android**: przycisk „Czy masz kod promocyjny Google Play?" w paywall otwiera proces realizacji Google Play z twoim wstępnie wypełnionym kodem.

**iOS**: Polityka App Store 3.1.1 wymaga realizacji przez oficjalny proces „Zrealizuj kod" Apple. Przycisk Google Play jest ukryty na iOS. Zamiast tego poszukaj „Zrealizuj kod App Store" w Ustawieniach.

---

## Karta Help i samouczki

Karta **Help** zawiera samouczki w aplikacji, przewodniki najlepszych praktyk i informacje referencyjne.

![Karta Help](../screenshots/10-help-tab.png)

Omawiane tematy:
- Jaki sprzęt jest potrzebny
- Jak umieszczać czujniki dla najlepszej dokładności
- Wskazówki dotyczące kalibracji
- Powszechne scenariusze pomiarowe
- Wskazówki dotyczące triangulacji i umiejscowienia 3D
- Prowadzenie kabli i jakość sygnału

---

## Rozwiązywanie problemów

### Wynik obliczeń jest nieprawidłowy lub nie ma sensu

1. Sprawdź kalibrację. Automatycznie wypełnione `tCal` zakłada opublikowaną prędkość materiału — rzeczywiste materiały się różnią. Najbardziej dokładna kalibracja to in-situ: dotknij znanego miejsca i pozwól aplikacji wyprowadzić rzeczywistą prędkość.
2. Sprawdź ustawienie **Pierwszego czujnika** — który czujnik usłyszał zdarzenie jako pierwszy, ma znaczenie dla matematyki.
3. Zweryfikuj swoje pomiary odległości. Błędy kilku mm się propagują.

### Toast mówi „Wynik poza zakresem"

Matematyka mówi, że źródło nie znajduje się między czujnikami. Możliwe przyczyny:
- Źródło rzeczywiście jest poza linią/płaszczyzną czujnika
- Jedno z twoich wejść jest błędne
- Prędkość kalibracji jest zbyt daleka od rzeczywistości

### Wskazówka prędkości obliczeniowej pokazuje kolor ostrzegawczy

Implikowana prędkość dźwięku z twoich wejść jest daleka od jakiegokolwiek powszechnego materiału (mniej niż 50 m/s lub więcej niż 20 000 m/s). Sprawdź swoje wejścia — prawdopodobnie literówka w tCal lub odległości.

### Selektor Materials pokazuje inne prędkości niż oczekiwano

Sprawdź Temperaturę odniesienia w Ustawieniach. Jeśli nie wynosi 20 °C, wyświetlane prędkości odzwierciedlają kompensację temperatury. Aplikacja pokazuje „ref X @ 20°C" pod skompensowanymi prędkościami, abyś mógł zweryfikować.

### Wpis historii odtwarza się z innym wynikiem

Stare wpisy historii utworzone przed wersją 1.75 aplikacji mogły nie zapisać temperatury. Jeśli wykonałeś pomiar w temperaturze innej niż 20 °C, odtwarzanie użyje obecnego ustawienia. Ręcznie ustaw temperaturę w Ustawieniach przed odtworzeniem LUB zmierz ponownie.

### Znaczniki adnotacji zdjęć nie są tam, gdzie się spodziewam

Znaczniki są automatycznie umieszczane na podstawie geometrii wejścia. Przeciągnij je, aby dostosować. Dostosowanie znaczników aktualizuje pozycję źródła w nakładce zdjęcia — ale NIE zmienia podstawowego wyniku obliczeń.

### Niepowodzenie kopii zapasowej/przywracania

Upewnij się, że używasz pliku kopii zapasowej wygenerowanego przez tę samą lub nowszą wersję aplikacji. Starsze pliki kopii zapasowych mogą nie mieć obecnych pól danych.

### Przywróć zakup mówi „nie znaleziono zakupu"

1. Zweryfikuj, że jesteś zalogowany na to samo konto sklepu, z którego dokonano zakupu
2. Zweryfikuj, że zakup nie został zwrócony lub nie wygasł
3. Spróbuj odinstalować i ponownie zainstalować aplikację (zakup jest powiązany z kontem sklepu, a nie z instalacją aplikacji)
4. Skontaktuj się z support@evdiag.net, jeśli problem nie ustąpi

### Wejście numeryczne nieoczekiwanie przeskakuje do 0

Z założenia: gdy opuszczasz pole numeryczne (dotykasz gdzie indziej), jeśli jest puste, ujemne lub zawiera tekst nienumeryczny, przeskakuje do 0. Zapobiega cichym, uszkodzonym obliczeniom z przypadkowo wyczyszczonych wejść. Wejście temperatury jest zwolnione (zamiast tego ogranicza się do -40/+200).

### Potrzebuję więcej pomocy

Skontaktuj się z `support@evdiag.net` z:
- Modelem urządzenia i wersją systemu
- Wersją aplikacji (Ustawienia → dół strony)
- Opisem tego, co próbowałeś
- Zrzutami ekranu, jeśli to możliwe

---

*NVH Source Locator jest opracowany przez EVDiag. Odwiedź https://evdiag.net, aby uzyskać aktualizacje i zasoby.*
