# NVH Source Locator — Guida Utente

NVH Source Locator è uno strumento di misurazione per localizzare sorgenti di rumore e vibrazione utilizzando TDOA (Time Difference of Arrival) dai segnali degli accelerometri catturati su un oscilloscopio o sistema di misurazione.

Questa guida copre tutte le funzionalità. Per un ripasso rapido, vedere **Riferimento Rapido**.

---

## Indice

1. [Come funziona](#how-it-works)
2. [Prima di iniziare](#before-you-start)
3. [Le schede principali](#the-main-tabs)
4. [Modalità 2-Sensor](#2-sensor-mode)
5. [Modalità 3-Sensor](#3-sensor-mode)
6. [Modalità Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [La scheda Materials](#the-materials-tab)
8. [Compensazione della temperatura](#temperature-compensation)
9. [Annotazione foto](#photo-annotation)
10. [Report](#reports)
11. [Backup e ripristino](#backup-and-restore)
12. [Impostazioni](#settings)
13. [Funzionalità Pro](#pro-features)
14. [Scheda Help e tutorial](#help-tab-and-tutorials)
15. [Risoluzione dei problemi](#troubleshooting)

---

## Come funziona {#how-it-works}

Quando una sorgente di rumore emette un suono o una vibrazione, l'onda viaggia attraverso un materiale a velocità nota. Se posizioni due o più accelerometri sul materiale e misuri quando l'onda arriva a ciascuno, la differenza di tempo ti dice dove si trova la sorgente.

NVH Source Locator prende:

- **Calibrazione**: la distanza tra i sensori e il tempo che ci vuole per un'onda per percorrere quella distanza (utilizzato per calcolare la velocità del suono del materiale)
- **Evento**: la differenza di tempo tra i sensori che rilevano l'evento di rumore/vibrazione

Poi calcola dove si trova la sorgente nella struttura.

Più sensori usi, più accuratamente puoi localizzare la sorgente:

- **2 sensori** → distanza lungo una linea
- **3 sensori** → posizione su una superficie 2D (X, Y)
- **4 sensori** → posizione nello spazio 3D (X, Y, Z)

---

## Prima di iniziare {#before-you-start}

Avrai bisogno di:

- **Un oscilloscopio o sistema di misurazione** che possa mostrarti la differenza di tempo tra i canali dell'accelerometro in microsecondi (µs)
- **Almeno 2 accelerometri** fisicamente collegati alla struttura (più sensori = maggiore precisione)
- **Un modo per misurare la distanza** tra i sensori (metro a nastro, calibri)
- **Un modo per innescare un'onda** in una posizione nota per la calibrazione (impatto di martello calibrato, colpo di cacciavite o altro segnale noto)

![Schermata principale con scheda 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Le schede principali {#the-main-tabs}

L'app ha schede in alto:

![Barra delle schede](../screenshots/02-tab-bar.png)

| Scheda | Cosa fa | Quando usarla |
|---|---|---|
| **2-Sensor** | Localizzazione sorgente 1D lungo una linea tra 2 sensori | Controlli rapidi, strutture tipo trave. **Completamente gratuito.** |
| **3-Sensor** | Localizzazione sorgente 2D usando 3 sensori in un triangolo | Uso più generale, pannelli e superfici |
| **3-Sen+** | 3-Sensor con risolutore minimi quadrati sovradeterminato | Misurazioni più impegnative, robusto al rumore |
| **4-Sensor** | Localizzazione 2D usando due coppie (A-B + C-D) | Layout rettangolari di sensori, verifica incrociata |
| **4-Sen+** | Modalità 2D avanzata, 4 sensori in qualsiasi posizione | Geometrie non rettangolari, LSQ completo |
| **3D** | Localizzazione sorgente 3D usando 4 sensori con coordinate XYZ | Strutture complesse nello spazio 3D |
| **3D+** | 3D con fino a 6 sensori, LSQ sovradeterminato | Geometrie molto complesse, massima precisione |
| **Materials** | Libreria di velocità del suono + materiali personalizzati | Selezionare una volta per sessione di misurazione |
| **Help** | Tutorial in-app e riferimento | Quando hai bisogno di un ripasso rapido |

> **Gratuito vs Pro**: La scheda 2-Sensor è completamente gratuita. Altre schede sono accessibili ma hanno campi di input specifici bloccati per gli utenti Pro (contrassegnati con un badge lucchetto dorato). Toccare un campo bloccato mostra la paywall Pro.

Le Impostazioni sono accessibili tramite l'icona ⚙ dell'ingranaggio in alto a destra (non una scheda).

---

## Modalità 2-Sensor {#2-sensor-mode}

La misurazione più semplice: localizzazione sorgente lungo una linea tra due accelerometri.

![Scheda 2-Sensor](../screenshots/01b-home-2sensor.png)

### Passaggio 1: Applicare un materiale

Tocca la scheda Materials. Scegli il materiale di cui è fatta la tua struttura (ad es., "Alluminio", "Acciaio, Mild (1020)"). L'app utilizza la velocità del suono nota del materiale per riempire automaticamente il campo del tempo di calibrazione.

Se il materiale della tua struttura non è nell'elenco, puoi selezionare temporaneamente "Aria" e sovrascrivere il tempo di calibrazione manualmente nel passaggio 2.

### Passaggio 2: Inserire i dati di calibrazione

Sulla scheda 2-Sensor, vedrai due sezioni di coppia: **Coppia A–B** e **Coppia A–C** (è richiesta solo A–B se hai solo 2 sensori).

Per ogni coppia, compili:

- **Distanza tra sensori** (`d`): distanza fisica tra i sensori, in cm o pollici (impostato in Impostazioni)
- **Ritardo tempo di calibrazione** (`tCal`): tempo per un'onda di viaggiare tra i sensori alla velocità del suono del materiale — riempito automaticamente quando selezioni un materiale, ma puoi sovrascriverlo

### Passaggio 3: Inserire il tempo dell'evento

- **Ritardo tempo dell'evento** (`tEvent`): differenza di tempo tra i sensori che rilevano l'evento di rumore, in microsecondi
- **Primo sensore**: quale sensore ha sentito l'evento per primo (A o B)

### Passaggio 4: Leggere il risultato

L'app mostra la posizione della sorgente come una distanza dal sensore A:
- Risultato = 0: la sorgente è al sensore A
- Risultato = distanza: la sorgente è al sensore B
- Risultato intermedio: la sorgente è tra di essi
- Risultato esterno: la sorgente è oltre uno dei sensori (il toast avviserà)

La scheda del risultato mostra entrambe le distanze (da A, da B) e indica quale sensore è più vicino.

### Passaggio 5 (opzionale): Annotare una foto

Tocca **📷 Annota foto** per scattare una foto della tua configurazione. L'app sovrappone marker per i sensori A, B e la sorgente. Utile per i report.

---

## Modalità 3-Sensor {#3-sensor-mode}

Localizza una sorgente su un piano 2D utilizzando tre sensori disposti in un triangolo.

![Scheda 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configurazione

Posiziona tre sensori sulla tua struttura formando un triangolo. Equilatero, rettangolo o scaleno: l'app gestisce tutte le geometrie.

### Inserire i dati

Nella sezione **Lunghezze lati del triangolo**, inserisci la distanza fisica per tutti e tre i lati (A–B, A–C, B–C).

Per ogni coppia (A–B e A–C), inserisci:
- **tCal**: tempo di calibrazione (compilato automaticamente dal materiale)
- **tEvent**: differenza di tempo misurata per l'evento di rumore
- **Primo sensore**: quale lo ha sentito per primo

### Leggere il risultato

L'app mostra la posizione della sorgente come coordinate X, Y relative al sensore A (sensore A all'origine, sensore B sull'asse X). La visualizzazione mostra tutti e tre i sensori e la posizione della sorgente.

![Risultato triangolo](../screenshots/04-triangle-result.png)

---

## Modalità Pro+ {#pro-modes}

Diverse schede avanzate offrono risolutori sovradeterminati e dimensionalità superiore:

### 3-Sen+ (Pro)

Stessa configurazione triangolare di 3-Sensor, ma calibra E misura tutte e tre le coppie (A–B, A–C, B–C). Il risolutore utilizza tutti e 3 i TDOA in un adattamento ai minimi quadrati — più robusto al rumore di misurazione e ai materiali anisotropi. I residui per coppia sono riportati così puoi individuare misurazioni incoerenti.

### 4-Sensor

Posiziona quattro sensori intorno all'area:
- **A–B** = coppia orizzontale (lati sinistro/destro)
- **C–D** = coppia verticale (lati superiore/inferiore)

Esegui prima la coppia A–B (orizzontale), poi la coppia C–D (verticale). La mappa 2D mostra l'intersezione. Ogni coppia è calibrata separatamente — utile quando il materiale varia attraverso la struttura.

### 4-Sen+ (2D avanzato)

Quattro sensori in qualsiasi posizione (non forzati rettangolari). Accoppia A con ciascuno di B, C, D e calibra separatamente. Il risolutore minimi quadrati sovradeterminato fa la media del rumore di misurazione per coppia e riporta i residui per coppia.

### 3D

Misurazione 3D completa con 4 sensori posizionati nello spazio 3D. Inserisci le coordinate (X, Y, Z) di ciascun sensore, più i tempi di calibrazione ed evento per ogni coppia (A–B, A–C, A–D).

### 3D+ (Pro)

Come 3D ma supporta fino a **6 sensori** (da A a F) con LSQ sovradeterminato. Massima precisione per geometrie 3D complesse.

---

## La scheda Materials {#the-materials-tab}

Libreria di materiali ingegneristici comuni con velocità del suono nota a 20 °C.

![Scheda Materials](../screenshots/05-materials-tab.png)

### Elenco dei materiali

L'elenco include aria, fluidi, gomme, polimeri, legni, vetri e metalli. Le velocità vanno da ~340 m/s (aria) a ~13.000 m/s (alcuni metalli a temperatura ambiente).

### Materiali integrati con compensazione della temperatura

14 metalli comunemente usati includono dati sul coefficiente di temperatura. Quando la Temperatura di riferimento in Impostazioni differisce da 20 °C, l'app regola automaticamente le velocità di questi materiali:

- Alluminio
- Acciaio, Mild (1020)
- Acciaio Inossidabile (304)
- Ferro (ghisa)
- Ferro
- Rame
- Ottone
- Bronzo
- Titanio
- Magnesio
- Piombo
- Zinco
- Nichel
- Tungsteno

I materiali con compensazione mostrano due valori nel selettore: la **velocità compensata** (grande, in evidenza) e la **velocità di riferimento a 20 °C** (piccola, grigia sotto).

I materiali senza compensazione mostrano **"ref only"** in corsivo — la loro velocità elencata viene usata così com'è indipendentemente dalla temperatura.

### Materiali personalizzati

Se misuri una calibrazione sulla scheda 2-Sensor, puoi salvare il risultato come materiale personalizzato. Dopo una misurazione 2-sensor riuscita, cerca l'opzione per salvare la velocità derivata con un nome di tua scelta.

I materiali personalizzati memorizzano la velocità misurata in-situ; non applicano mai la compensazione della temperatura (la velocità è già stata misurata alla temperatura di test).

### Preferiti

Tocca la stella accanto a qualsiasi materiale per contrassegnarlo come preferito. I preferiti appaiono in cima all'elenco per un accesso rapido.

### Ricerca

Usa la barra di ricerca in alto per filtrare i materiali per nome. La ricerca corrisponde sia ai nomi canonici inglesi che ai nomi di visualizzazione tradotti.

---

## Compensazione della temperatura {#temperature-compensation}

La velocità del suono nei materiali cambia con la temperatura. Nei test NVH automobilistici questo è importante: un vano motore a 80 °C, un abitacolo raffreddato a -10 °C o un'area del collettore di scarico a 200 °C si comportano tutti diversamente dalle condizioni di laboratorio a temperatura ambiente.

### Impostare la temperatura

Apri Impostazioni (icona ⚙) → Temperatura di riferimento. Inserisci la temperatura del tuo ambiente di test in °C (intervallo da -40 a +200).

![Pannello Impostazioni](../screenshots/06-settings.png)

### Cosa succede quando la temperatura ≠ 20 °C

- I campi del tempo di calibrazione si compilano automaticamente con la velocità regolata per temperatura
- Il selettore Materials mostra la velocità regolata in modo evidente
- Un toast conferma: *"Alluminio applicato (6.284 m/s @ 60 °C) — N coppia/e aggiornata/e"*
- Il suggerimento "Materiale più vicino" confronta con velocità regolate per temperatura
- Le voci della cronologia salvate registrano la temperatura attiva
- I report includono una riga a piè di pagina: *"Temperatura di riferimento: 60 °C, compensazione applicata"*

### Reset all'avvio dell'app

La Temperatura di riferimento **viene sempre ripristinata a 20 °C** quando avvii l'app. Questo impedisce che impostazioni obsolete da una sessione di misurazione passata influenzino silenziosamente il lavoro di oggi. Una piccola nota in corsivo in Impostazioni ti ricorda questo comportamento.

Se vuoi riprodurre una misurazione storica alla sua temperatura originale, tocca semplicemente la voce — la temperatura viene ripristinata automaticamente.

### Materiali senza compensazione

La maggior parte dei materiali non metallici non ha coefficienti di temperatura pubblicati affidabili. L'app mostra un badge **"ref only"** per questi — la loro velocità elencata viene usata indipendentemente dall'impostazione della temperatura. Se hai bisogno di misurazioni accurate a temperature non ambientali per questi materiali, esegui una calibrazione in-situ e salva il risultato come materiale personalizzato.

---

## Annotazione foto {#photo-annotation}

Dopo un calcolo riuscito, tocca il pulsante **📷 Annota foto** per sovrapporre marker di sensore e sorgente su una foto della tua configurazione.

![Annotazione foto](../screenshots/08-photo-annotation.png)

### Flusso

1. Tocca **Annota foto** — si apre la fotocamera di sistema
2. Scatta una foto del posizionamento del tuo sensore
3. L'app carica la foto nell'overlay di annotazione
4. I marker dei sensori (A, B, C, D, E, F a seconda dei casi — fino a 6 sensori) e il marker della sorgente si posizionano automaticamente in base al tuo calcolo
5. Trascina qualsiasi marker per regolare finemente la posizione. Mentre regoli, la posizione della sorgente viene ricalcolata dalle posizioni corrette dei sensori
6. Tocca **Salva** per conservare, o **Riprova** per riprovare

La foto annotata è inclusa automaticamente nei report PDF.

---

## Report {#reports}

Tocca il pulsante **Stampa risultato** su qualsiasi schermata dei risultati per generare un report formattato.

![Report PDF](../screenshots/09-pdf-report.png)

### Contenuto del report

- Intestazione (personalizzabile in Impostazioni → Intestazione report)
- Titolo della misurazione e timestamp
- Tutti i valori di input in una tabella pulita
- Risultato del calcolo
- Testo della conclusione
- Visualizzazione (grafico della geometria)
- Foto annotata (se ne hai scattata una)
- Riga a piè di pagina della temperatura (se la compensazione era attiva)
- Numero di pagina e riga di credito

### Formato di output

- **Android**: generazione PDF nativa, salva sul tuo telefono o condividi
- **iOS**: finestra di dialogo di stampa del sistema → salva come PDF, AirPrint o condividi

### Personalizzare l'intestazione

Impostazioni → Intestazione report. Inserisci il nome della tua azienda, nome del laboratorio, info del progetto o qualsiasi cosa tu voglia in cima a ogni report.

---

## Backup e ripristino {#backup-and-restore}

Salva tutti i tuoi materiali personalizzati, preferiti, impostazioni e cronologia in un singolo file. Trasferisci tra dispositivi.

### Backup

Impostazioni → **Backup** → tocca "Salva file di backup". L'app genera un file JSON e apre il foglio di condivisione del tuo telefono. Salvalo nel tuo cloud drive (Google Drive, iCloud, OneDrive), inviatelo via email a te stesso o trasferiscilo come preferisci.

### Ripristino

Impostazioni → **Ripristino** → seleziona il file di backup dall'archiviazione del tuo telefono. L'app importa materiali personalizzati, preferiti, cronologia e impostazioni.

⚠️ **Il ripristino sostituisce i tuoi dati attuali.** Se hai misurazioni importanti sul dispositivo corrente, eseguine prima il backup prima di ripristinare da un backup diverso.

---

## Impostazioni {#settings}

Accesso tramite l'icona ⚙ dell'ingranaggio in alto a destra. Impostazioni è una finestra modale, non una scheda.

![Impostazioni](../screenshots/06-settings.png)

| Impostazione | Cosa controlla |
|---|---|
| **Aggiorna a Pro** | Acquista o scopri le funzionalità Pro ($19,99) |
| **Lingua** | Lingua di visualizzazione dell'app (30 supportate) |
| **Tema** | Chiaro, Scuro o Auto (seguire il sistema) |
| **Unità di distanza** | cm o pollici |
| **Temperatura di riferimento** | Temperatura attiva per la compensazione, da -40 a +200 °C |
| **Intestazione report** | Testo personalizzato in cima ai report generati |
| **Backup** | Esporta tutti i dati in un file |
| **Ripristino** | Importa i dati da un file di backup |
| **Ripristina acquisto** | Riacquisisci Pro su un nuovo dispositivo |

---

## Funzionalità Pro {#pro-features}

NVH Source Locator usa un **modello freemium con blocco per funzionalità**:

- **Gratuito**: La scheda 2-Sensor è completamente funzionante senza limiti
- **Pro**: Tutte le altre schede hanno campi di input specifici bloccati. La paywall appare quando un utente gratuito tocca un campo bloccato

### Cosa è bloccato

I campi richiesti per Pro sono distribuiti su:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modalità 3D e 3D+
- Backup e Ripristino
- Report PDF
- Materiali personalizzati
- Annotazione foto

Un utente gratuito può APRIRE qualsiasi scheda e VEDERE l'interfaccia. Semplicemente non può inserire valori nei campi di input bloccati da Pro.

![Campo bloccato da Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Quando un utente gratuito tocca un campo bloccato, la paywall scorre mostrando:
- Icona dell'app con badge PRO
- Elenco di funzionalità
- Pulsante di sblocco con prezzo ($19,99 predefinito; può variare in base alla regione)
- Riscatto codice promozionale (solo Android — iOS usa il flusso Offer Code separato di Apple)
- Link promozionale opzionale ai canali della community

### Acquistare Pro

Tocca qualsiasi campo bloccato, o tocca **Aggiorna a Pro** in Impostazioni. Usa il sistema di pagamento ufficiale della tua piattaforma (Google Play su Android, Apple App Store su iOS).

### Ripristinare Pro su un nuovo dispositivo

Se hai acquistato su un dispositivo e vuoi Pro su un altro (stesso account):

1. Accedi al **medesimo** account Google (Android) o Apple ID (iOS) che hai usato per acquistare
2. Apri NVH Source Locator sul nuovo dispositivo
3. Vai a Impostazioni → **Ripristina acquisto**
4. L'app verifica con i record di acquisto della piattaforma e sblocca Pro

### Auto-ripristino all'avvio

Se riscatti un codice promozionale nel Google Play Store o App Store mentre NVH Source Locator è in esecuzione in background, il ritorno all'app rileva automaticamente il nuovo acquisto e sblocca Pro — nessun Ripristino manuale necessario.

### Riscatto codice promozionale

**Android**: un pulsante "Hai un codice promozionale Google Play?" nella paywall apre il flusso di riscatto Google Play con il tuo codice pre-compilato.

**iOS**: La politica dell'App Store 3.1.1 richiede il riscatto attraverso il flusso ufficiale "Riscatta codice" di Apple. Il pulsante Google Play è nascosto su iOS. Cerca "Riscatta codice App Store" in Impostazioni invece.

---

## Scheda Help e tutorial {#help-tab-and-tutorials}

La scheda **Help** include tutorial in-app, guide alle migliori pratiche e informazioni di riferimento.

![Scheda Help](../screenshots/10-help-tab.png)

Argomenti trattati:
- Quale attrezzatura hai bisogno
- Come posizionare i sensori per la migliore precisione
- Consigli di calibrazione
- Scenari di misurazione comuni
- Suggerimenti per triangolazione e posizionamenti 3D
- Instradamento dei cavi e qualità del segnale

---

## Risoluzione dei problemi {#troubleshooting}

### Il risultato del calcolo è sbagliato o non ha senso

1. Controlla la tua calibrazione. Il `tCal` autocompilato presuppone la velocità pubblicata del materiale — i materiali reali variano. La calibrazione più accurata è in-situ: tocca una posizione nota e lascia che l'app derivi la velocità reale.
2. Controlla l'impostazione del **Primo sensore** — quale sensore ha sentito l'evento per primo è importante per la matematica.
3. Verifica le tue misurazioni di distanza. Errori di pochi mm si propagano.

### Il toast dice "Risultato fuori range"

La matematica dice che la sorgente non è tra i tuoi sensori. Possibili cause:
- La sorgente è effettivamente al di fuori della linea/piano del sensore
- Uno dei tuoi input è sbagliato
- La velocità di calibrazione è troppo lontana dalla realtà

### Il suggerimento di velocità di calc mostra un colore di avviso

La velocità del suono implicita dai tuoi input è lontana da qualsiasi materiale comune (meno di 50 m/s o più di 20.000 m/s). Controlla i tuoi input — probabilmente un errore di battitura in tCal o distanza.

### Il selettore Materials mostra velocità diverse da quelle attese

Controlla la Temperatura di riferimento in Impostazioni. Se non è 20 °C, le velocità visualizzate riflettono la compensazione della temperatura. L'app mostra "ref X @ 20°C" sotto le velocità compensate così puoi verificare.

### La voce della cronologia si riproduce con un risultato diverso

Le vecchie voci della cronologia create prima della versione 1.75 dell'app potrebbero non aver memorizzato la temperatura. Se hai effettuato la misurazione a una temperatura non di 20 °C, la riproduzione userà l'impostazione corrente. Imposta manualmente la temperatura in Impostazioni prima di riprodurre, OPPURE misura di nuovo.

### I marker di annotazione foto non sono dove mi aspetto

I marker si posizionano automaticamente in base alla geometria di input. Trascinali per regolare. Regolare i marker aggiorna la posizione della sorgente nell'overlay della foto — ma NON cambia il risultato di calcolo sottostante.

### Il backup/ripristino fallisce

Assicurati di utilizzare un file di backup generato dalla stessa versione o da una versione più recente dell'app. I file di backup più vecchi potrebbero mancare di campi di dati attuali.

### Ripristina acquisto dice "nessun acquisto trovato"

1. Verifica di essere connesso allo stesso account dello store che hai usato per acquistare
2. Verifica che l'acquisto non sia stato rimborsato o scaduto
3. Prova a disinstallare e reinstallare l'app (l'acquisto è legato al tuo account dello store, non all'installazione dell'app)
4. Contatta support@evdiag.net se persiste

### L'input numerico si imposta a 0 inaspettatamente

Per progettazione: quando perdi il focus su un campo numerico (tocchi altrove), se è vuoto, negativo o contiene testo non numerico, si imposta a 0. Previene calcoli silenziosamente rotti da input accidentalmente cancellati. L'input della temperatura è esente (si limita invece a -40/+200).

### Hai bisogno di più aiuto

Contatta `support@evdiag.net` con:
- Il modello del tuo dispositivo e la versione del SO
- La versione dell'app (Impostazioni → in fondo alla pagina)
- Descrizione di cosa hai provato
- Screenshot se possibile

---

*NVH Source Locator è sviluppato da EVDiag. Visita https://evdiag.net per aggiornamenti e risorse.*
