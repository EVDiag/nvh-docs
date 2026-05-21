# NVH Source Locator — Riferimento Rapido

Un riepilogo di una pagina. Per i dettagli completi, vedere **Guida Utente**.

---

## Flusso principale (2-Sensor, gratuito)

1. **Scegli un materiale** — scheda Materials → tocca il tuo materiale
2. **Inserisci la calibrazione** nella scheda 2-Sensor:
   - Distanza tra i sensori (`d`)
   - Ritardo di tempo di calibrazione (`tCal`) — compilato automaticamente dal materiale
3. **Inserisci l'evento** — `tEvent` e Primo sensore (A o B)
4. **Leggi il risultato** — distanza dal sensore A

![Scheda 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tutte le schede

| Scheda | Output | Campi Pro? |
|---|---|---|
| 2-Sensor | Distanza lungo una linea | No (completamente gratuito) |
| 3-Sensor | X, Y su una superficie | Sì |
| 3-Sen+ | X, Y con LSQ su 3 coppie | Sì |
| 4-Sensor | X, Y da due coppie (A–B + C–D) | Sì |
| 4-Sen+ | X, Y da 4 sensori, posizione libera | Sì |
| 3D | X, Y, Z da 4 sensori | Sì |
| 3D+ | X, Y, Z da fino a 6 sensori | Sì |
| Materials | Selettore della velocità del suono | No |
| Help | Tutorial | No |

Le impostazioni si trovano nell'icona ⚙ (in alto a destra), non in una scheda.

---

## Compensazione della temperatura

Impostazioni → Temperatura di riferimento, intervallo **da -40 a +200 °C**.

- **14 metalli** hanno compensazione integrata (alluminio, acciai, rame, ottone, bronzo, titanio, magnesio, piombo, zinco, nichel, tungsteno, ferro, ghisa)
- I materiali senza compensazione mostrano **"ref only"**
- **Si reimposta a 20 °C ad ogni avvio dell'app** (avvio sicuro predefinito)
- Riprodurre una voce della cronologia ripristina la sua temperatura originale

---

## Scorciatoie

- **Toccare un materiale** → compila automaticamente tutti i campi `tCal` in tutte le schede
- **Tenere premuto +/-** sui campi numerici → incremento rapido
- **Trascinare orizzontalmente** su un campo numerico → scorrere i valori
- **Input vuoto/negativo/non valido** → si imposta a 0 alla perdita di focus (il campo temperatura si blocca a -40/200)
- **Contrassegnare un materiale con una stella** → lo sposta in cima al selettore

---

## Modello Pro

**Freemium con blocco per funzionalità** ($19,99):
- Gratuito: scheda 2-Sensor completamente funzionante, senza limiti
- Pro: Altre schede accessibili ma con **campi con lucchetto dorato** che mostrano il paywall al tocco

Pro sblocca: da 3-Sensor a 3D+, materiali personalizzati, backup/ripristino, report PDF, annotazione foto.

![Paywall](../screenshots/07-paywall.png)

---

## Report e backup

Pulsante **Stampa risultato** su qualsiasi schermata dei risultati → PDF con intestazione, input, risultato, visualizzazione, foto (se scattata) e piè di pagina con temperatura (quando la compensazione è attiva).

Personalizza l'intestazione in Impostazioni → Intestazione report.

**Backup**: Impostazioni → Backup → condividi su cloud/email.  
**Ripristino**: Impostazioni → Ripristino → seleziona il file di backup.

---

## Ripristina Pro su un nuovo dispositivo

Stesso account Google (Android) o Apple ID (iOS) con cui hai effettuato l'acquisto → Impostazioni → **Ripristina acquisto** → si sblocca in pochi secondi.

Il ripristino automatico avviene silenziosamente quando torni all'app dopo aver riscattato un codice promozionale esternamente.

---

## Risoluzione rapida dei problemi

- **Risultato fuori dall'intervallo?** Controlla il segno di `tEvent` / Primo sensore / distanza tra i sensori
- **Materiale più vicino errato?** La temperatura di riferimento è probabilmente impostata accidentalmente — controlla le impostazioni
- **Il ripristino dell'acquisto non riesce?** Verifica lo stesso account dello store; reinstalla se persiste
- **Campo impostato a 0?** Gli input vuoti/negativi si impostano automaticamente alla perdita di focus — reinserisci il valore
- **Pulsanti dello stepper scomparsi?** Appaiono accanto ai campi con `data-step` — riavvia l'app se mancano
- **Avviso di temperatura obsoleta?** Si reimposta a 20 ad ogni avvio — impostala di nuovo per questa sessione

---

Contatto `support@evdiag.net` — includi modello del dispositivo, versione dell'app (Impostazioni → in basso) e una descrizione di cosa hai provato.
