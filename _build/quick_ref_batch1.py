"""Quick Reference translations — batch 1.

8 priority languages: de, es, fr, it, pt, pl, ru, zh.

Each entry maps locale code → full markdown content of the
translated quick-reference. Structure mirrors the English
source: same headings, same image references, same tables.
"""

QUICK_REF_TRANSLATIONS = {

'de': """# NVH Source Locator — Kurzanleitung

Eine einseitige Zusammenfassung. Vollständige Details siehe `user-guide.md`.

---

## Grundablauf (2-Sensor, kostenlos)

1. **Material auswählen** — Materials-Registerkarte → tippen Sie auf Ihr Material
2. **Kalibrierung eingeben** in der 2-Sensor-Registerkarte:
   - Sensorabstand (`d`)
   - Kalibrierungszeit (`tCal`) — automatisch vom Material ausgefüllt
3. **Ereignis eingeben** — `tEvent` und Erster Sensor (A oder B)
4. **Ergebnis ablesen** — Abstand vom Sensor A

![2-Sensor Registerkarte](../screenshots/01-home-2sensor.png)

---

## Alle Registerkarten

| Registerkarte | Ergebnis | Pro-Felder? |
|---|---|---|
| 2-Sensor | Abstand entlang einer Linie | Nein (vollständig kostenlos) |
| 3-Sensor | X, Y auf einer Fläche | Ja |
| 3-Sen+ | X, Y mit LSQ über 3 Paare | Ja |
| 4-Sensor | X, Y aus zwei Paaren (A–B + C–D) | Ja |
| 4-Sen+ | X, Y aus 4 Sensoren, beliebige Position | Ja |
| 3D | X, Y, Z aus 4 Sensoren | Ja |
| 3D+ | X, Y, Z aus bis zu 6 Sensoren | Ja |
| Materials | Schallgeschwindigkeitsauswahl | Nein |
| Help | Tutorials | Nein |

Die Einstellungen befinden sich hinter dem ⚙-Symbol (oben rechts), nicht als Registerkarte.

---

## Temperaturkompensation

Einstellungen → Referenztemperatur, Bereich **-40 bis +200 °C**.

- **14 Metalle** verfügen über integrierte Kompensation (Aluminium, Stähle, Kupfer, Messing, Bronze, Titan, Magnesium, Blei, Zink, Nickel, Wolfram, Eisen, Gusseisen)
- Materialien ohne Kompensation zeigen **„ref only"** an
- **Wird bei jedem App-Start auf 20 °C zurückgesetzt** (sicherer Standardstart)
- Beim Abspielen eines Verlaufseintrags wird die ursprüngliche Temperatur wiederhergestellt

---

## Tastenkürzel

- **Material antippen** → füllt alle `tCal`-Felder in allen Registerkarten automatisch aus
- **+/− halten** auf Zahlenfeldern → schnelles Inkrementieren
- **Horizontales Ziehen** auf einem Zahlenfeld → Werte scrubben
- **Leere/negative/ungültige Eingabe** → springt beim Verlassen auf 0 (Temperaturfeld klemmt auf -40/200)
- **Material mit Stern markieren** → wird in der Auswahl nach oben verschoben

---

## Pro-Modell

**Feature-gesperrtes Freemium-Modell** ($19,99):
- Kostenlos: 2-Sensor-Registerkarte voll funktionsfähig, ohne Einschränkungen
- Pro: Andere Registerkarten zugänglich, aber mit **Feldern mit goldenem Schloss**, die beim Tippen die Paywall anzeigen

Pro schaltet frei: 3-Sensor bis 3D+, benutzerdefinierte Materialien, Backup/Wiederherstellung, PDF-Berichte, Fotoannotation.

![Paywall](../screenshots/07-paywall.png)

---

## Berichte & Backup

Die **Ergebnis drucken**-Schaltfläche auf einem beliebigen Ergebnisbildschirm → PDF mit Kopfzeile, Eingaben, Ergebnis, Visualisierung, Foto (falls aufgenommen) und Temperatur-Fußzeile (wenn Kompensation aktiv).

Kopfzeile anpassen unter Einstellungen → Berichtskopfzeile.

**Backup**: Einstellungen → Backup → in Cloud/E-Mail teilen.  
**Wiederherstellen**: Einstellungen → Wiederherstellen → Backup-Datei auswählen.

---

## Pro auf einem neuen Gerät wiederherstellen

Selbes Google-Konto (Android) oder Apple-ID (iOS), mit dem Sie gekauft haben → Einstellungen → **Kauf wiederherstellen** → wird innerhalb von Sekunden freigeschaltet.

Auto-Wiederherstellung erfolgt im Hintergrund, wenn Sie nach dem externen Einlösen eines Promo-Codes zur App zurückkehren.

---

## Schnelle Fehlerbehebung

- **Ergebnis außerhalb des Bereichs?** Vorzeichen von `tEvent` / Ersten Sensor / Sensorabstand überprüfen
- **Falsches nächstgelegenes Material?** Referenztemperatur wahrscheinlich versehentlich gesetzt — Einstellungen überprüfen
- **Kauf wiederherstellen schlägt fehl?** Selbes Store-Konto bestätigen; bei anhaltenden Problemen neu installieren
- **Feld auf 0 zurückgesetzt?** Leere/negative Eingaben werden beim Verlassen automatisch auf 0 gesetzt — Wert erneut eingeben
- **Stepper-Schaltflächen weg?** Sie erscheinen neben Feldern mit `data-step` — bei Fehlen App neu starten
- **Veraltete Temperaturwarnung?** Wird bei jedem Start auf 20 zurückgesetzt — für diese Sitzung erneut einstellen

---

Kontakt `support@evdiag.net` — geben Sie Gerätemodell, App-Version (Einstellungen → unten) und eine Beschreibung Ihres Vorgehens an.
""",

'es': """# NVH Source Locator — Referencia Rápida

Un resumen de una página. Para más detalles, consulte `user-guide.md`.

---

## Flujo principal (2-Sensor, gratis)

1. **Elija un material** — pestaña Materials → toque su material
2. **Introduzca calibración** en la pestaña 2-Sensor:
   - Espaciado del sensor (`d`)
   - Retardo de tiempo de calibración (`tCal`) — autocompletado desde el material
3. **Introduzca evento** — `tEvent` y Primer sensor (A o B)
4. **Lea el resultado** — distancia desde el sensor A

![Pestaña 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Todas las pestañas

| Pestaña | Salida | ¿Campos Pro? |
|---|---|---|
| 2-Sensor | Distancia a lo largo de la línea | No (completamente gratis) |
| 3-Sensor | X, Y en una superficie | Sí |
| 3-Sen+ | X, Y con LSQ sobre 3 pares | Sí |
| 4-Sensor | X, Y desde dos pares (A–B + C–D) | Sí |
| 4-Sen+ | X, Y desde 4 sensores, cualquier posición | Sí |
| 3D | X, Y, Z desde 4 sensores | Sí |
| 3D+ | X, Y, Z desde hasta 6 sensores | Sí |
| Materials | Selector de velocidad del sonido | No |
| Help | Tutoriales | No |

Los ajustes se encuentran en el icono ⚙ (arriba a la derecha), no en una pestaña.

---

## Compensación de temperatura

Ajustes → Temperatura de referencia, rango **-40 a +200 °C**.

- **14 metales** tienen compensación integrada (aluminio, aceros, cobre, latón, bronce, titanio, magnesio, plomo, zinc, níquel, tungsteno, hierro, hierro fundido)
- Los materiales sin compensación muestran **"ref only"**
- **Se restablece a 20 °C en cada inicio de la aplicación** (inicio seguro por defecto)
- Reproducir una entrada del historial restaura su temperatura original

---

## Atajos

- **Tocar un material** → autocompleta todos los campos `tCal` en todas las pestañas
- **Mantener pulsado +/-** en campos numéricos → incremento rápido
- **Arrastrar horizontalmente** en un campo numérico → ajustar valores
- **Entrada vacía/negativa/no válida** → se ajusta a 0 al perder el foco (el campo de temperatura se ajusta a -40/200)
- **Marcar un material con estrella** → se mueve a la parte superior del selector

---

## Modelo Pro

**Freemium con bloqueo por funciones** ($19,99):
- Gratis: pestaña 2-Sensor totalmente funcional, sin límites
- Pro: Otras pestañas accesibles pero con **campos con candado dorado** que muestran la paywall al tocar

Pro desbloquea: 3-Sensor hasta 3D+, materiales personalizados, backup/restauración, informes PDF, anotación de fotos.

![Paywall](../screenshots/07-paywall.png)

---

## Informes y backup

Botón **Imprimir resultado** en cualquier pantalla de resultados → PDF con encabezado, entradas, resultado, visualización, foto (si se tomó) y pie de página de temperatura (cuando la compensación está activa).

Personalice el encabezado en Ajustes → Encabezado del informe.

**Backup**: Ajustes → Backup → compartir a la nube/correo electrónico.  
**Restaurar**: Ajustes → Restaurar → seleccionar archivo de backup.

---

## Restaurar Pro en un nuevo dispositivo

Misma cuenta de Google (Android) o Apple ID (iOS) con la que compró → Ajustes → **Restaurar compra** → se desbloquea en segundos.

La restauración automática ocurre silenciosamente cuando regresa a la aplicación después de canjear un código promocional externamente.

---

## Resolución rápida de problemas

- **¿Resultado fuera de rango?** Verifique el signo de `tEvent` / Primer sensor / espaciado del sensor
- **¿Material más cercano incorrecto?** Probablemente la temperatura de referencia se ha establecido accidentalmente — verifique los ajustes
- **¿Falla la restauración de compra?** Verifique la misma cuenta de la tienda; reinstale si persiste
- **¿Campo ajustado a 0?** Las entradas vacías/negativas se ajustan automáticamente al perder el foco — vuelva a introducir el valor
- **¿No aparecen botones del stepper?** Aparecen junto a campos con `data-step` — reinicie la aplicación si faltan
- **¿Advertencia de temperatura obsoleta?** Se restablece a 20 en cada inicio — establezca de nuevo para esta sesión

---

Contacto `support@evdiag.net` — incluya modelo del dispositivo, versión de la aplicación (Ajustes → parte inferior) y descripción de lo que intentó.
""",

'fr': """# NVH Source Locator — Référence Rapide

Un rappel sur une page. Pour les détails complets, voir `user-guide.md`.

---

## Flux principal (2-Sensor, gratuit)

1. **Choisissez un matériau** — onglet Materials → touchez votre matériau
2. **Entrez la calibration** dans l'onglet 2-Sensor :
   - Espacement des capteurs (`d`)
   - Délai de temps de calibration (`tCal`) — automatiquement rempli depuis le matériau
3. **Entrez l'événement** — `tEvent` et Premier capteur (A ou B)
4. **Lisez le résultat** — distance depuis le capteur A

![Onglet 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tous les onglets

| Onglet | Sortie | Champs Pro ? |
|---|---|---|
| 2-Sensor | Distance le long d'une ligne | Non (entièrement gratuit) |
| 3-Sensor | X, Y sur une surface | Oui |
| 3-Sen+ | X, Y avec LSQ sur 3 paires | Oui |
| 4-Sensor | X, Y à partir de deux paires (A–B + C–D) | Oui |
| 4-Sen+ | X, Y à partir de 4 capteurs, position libre | Oui |
| 3D | X, Y, Z à partir de 4 capteurs | Oui |
| 3D+ | X, Y, Z à partir de jusqu'à 6 capteurs | Oui |
| Materials | Sélecteur de vitesse du son | Non |
| Help | Tutoriels | Non |

Les paramètres sont accessibles via l'icône ⚙ (en haut à droite), pas un onglet.

---

## Compensation de température

Paramètres → Température de référence, plage **-40 à +200 °C**.

- **14 métaux** ont une compensation intégrée (aluminium, aciers, cuivre, laiton, bronze, titane, magnésium, plomb, zinc, nickel, tungstène, fer, fonte)
- Les matériaux sans compensation affichent **« ref only »**
- **Réinitialisé à 20 °C à chaque lancement** (démarrage par défaut sécurisé)
- Rejouer une entrée d'historique restaure sa température d'origine

---

## Raccourcis

- **Toucher un matériau** → remplit automatiquement tous les champs `tCal` dans tous les onglets
- **Maintenir +/-** sur les champs numériques → incrémentation rapide
- **Glisser horizontalement** sur un champ numérique → faire défiler les valeurs
- **Entrée vide/négative/invalide** → se met à 0 à la perte de focus (le champ de température se limite à -40/200)
- **Marquer un matériau avec une étoile** → le déplace en haut du sélecteur

---

## Modèle Pro

**Freemium avec verrouillage par fonctionnalité** (19,99 $) :
- Gratuit : onglet 2-Sensor entièrement fonctionnel, sans limites
- Pro : Autres onglets accessibles mais avec des **champs verrouillés (cadenas doré)** qui affichent la paywall au toucher

Pro débloque : 3-Sensor jusqu'à 3D+, matériaux personnalisés, sauvegarde/restauration, rapports PDF, annotation de photos.

![Paywall](../screenshots/07-paywall.png)

---

## Rapports et sauvegarde

Bouton **Imprimer le résultat** sur n'importe quel écran de résultats → PDF avec en-tête, entrées, résultat, visualisation, photo (si prise) et pied de page de température (lorsque la compensation est active).

Personnalisez l'en-tête dans Paramètres → En-tête de rapport.

**Sauvegarde** : Paramètres → Sauvegarde → partager vers le cloud/courriel.  
**Restaurer** : Paramètres → Restaurer → sélectionnez le fichier de sauvegarde.

---

## Restaurer Pro sur un nouvel appareil

Même compte Google (Android) ou Apple ID (iOS) que celui utilisé pour l'achat → Paramètres → **Restaurer l'achat** → débloqué en quelques secondes.

La restauration automatique se produit silencieusement lorsque vous revenez à l'application après avoir échangé un code promo de manière externe.

---

## Dépannage rapide

- **Résultat hors plage ?** Vérifiez le signe de `tEvent` / Premier capteur / espacement des capteurs
- **Matériau le plus proche incorrect ?** La température de référence a probablement été définie accidentellement — vérifiez les paramètres
- **Échec de la restauration de l'achat ?** Vérifiez le même compte de magasin ; réinstallez si cela persiste
- **Champ mis à 0 ?** Les entrées vides/négatives se mettent automatiquement à 0 à la perte de focus — saisissez à nouveau la valeur
- **Boutons d'incrémentation manquants ?** Ils apparaissent à côté des champs avec `data-step` — redémarrez l'application s'ils manquent
- **Avertissement de température obsolète ?** Se réinitialise à 20 à chaque lancement — définissez à nouveau pour cette session

---

Contact `support@evdiag.net` — incluez le modèle de l'appareil, la version de l'application (Paramètres → bas) et une description de ce que vous avez essayé.
""",

'it': """# NVH Source Locator — Riferimento Rapido

Un riepilogo di una pagina. Per i dettagli completi, vedere `user-guide.md`.

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
""",

'pt': """# NVH Source Locator — Referência Rápida

Um resumo de uma página. Para detalhes completos, veja `user-guide.md`.

---

## Fluxo principal (2-Sensor, gratuito)

1. **Escolha um material** — aba Materials → toque no seu material
2. **Insira a calibração** na aba 2-Sensor:
   - Espaçamento entre sensores (`d`)
   - Atraso de tempo de calibração (`tCal`) — preenchido automaticamente pelo material
3. **Insira o evento** — `tEvent` e Primeiro sensor (A ou B)
4. **Leia o resultado** — distância do sensor A

![Aba 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Todas as abas

| Aba | Saída | Campos Pro? |
|---|---|---|
| 2-Sensor | Distância ao longo da linha | Não (totalmente gratuito) |
| 3-Sensor | X, Y em uma superfície | Sim |
| 3-Sen+ | X, Y com LSQ sobre 3 pares | Sim |
| 4-Sensor | X, Y a partir de dois pares (A–B + C–D) | Sim |
| 4-Sen+ | X, Y a partir de 4 sensores, posição livre | Sim |
| 3D | X, Y, Z a partir de 4 sensores | Sim |
| 3D+ | X, Y, Z a partir de até 6 sensores | Sim |
| Materials | Seletor de velocidade do som | Não |
| Help | Tutoriais | Não |

As configurações ficam no ícone ⚙ (canto superior direito), não em uma aba.

---

## Compensação de temperatura

Configurações → Temperatura de referência, intervalo **-40 a +200 °C**.

- **14 metais** têm compensação integrada (alumínio, aços, cobre, latão, bronze, titânio, magnésio, chumbo, zinco, níquel, tungstênio, ferro, ferro fundido)
- Materiais sem compensação mostram **"ref only"**
- **Redefine para 20 °C a cada inicialização do aplicativo** (início seguro padrão)
- Reproduzir uma entrada do histórico restaura sua temperatura original

---

## Atalhos

- **Tocar em um material** → preenche automaticamente todos os campos `tCal` em todas as abas
- **Manter pressionado +/-** em campos numéricos → incremento rápido
- **Arrastar horizontalmente** em um campo numérico → ajustar valores
- **Entrada vazia/negativa/inválida** → ajusta para 0 ao perder o foco (campo de temperatura limita a -40/200)
- **Marcar material com estrela** → move para o topo do seletor

---

## Modelo Pro

**Freemium com bloqueio por recurso** ($19,99):
- Gratuito: aba 2-Sensor totalmente funcional, sem limites
- Pro: Outras abas acessíveis, mas com **campos com cadeado dourado** que mostram a paywall ao toque

Pro desbloqueia: 3-Sensor até 3D+, materiais personalizados, backup/restauração, relatórios PDF, anotação de fotos.

![Paywall](../screenshots/07-paywall.png)

---

## Relatórios e backup

Botão **Imprimir resultado** em qualquer tela de resultado → PDF com cabeçalho, entradas, resultado, visualização, foto (se tirada) e rodapé de temperatura (quando a compensação está ativa).

Personalize o cabeçalho em Configurações → Cabeçalho do relatório.

**Backup**: Configurações → Backup → compartilhar em nuvem/e-mail.  
**Restaurar**: Configurações → Restaurar → selecionar arquivo de backup.

---

## Restaurar Pro em um novo dispositivo

Mesma conta Google (Android) ou Apple ID (iOS) com que comprou → Configurações → **Restaurar compra** → desbloqueia em segundos.

A restauração automática ocorre silenciosamente quando você retorna ao aplicativo depois de resgatar um código promocional externamente.

---

## Solução rápida de problemas

- **Resultado fora do intervalo?** Verifique o sinal de `tEvent` / Primeiro sensor / espaçamento entre sensores
- **Material mais próximo errado?** A temperatura de referência provavelmente foi definida acidentalmente — verifique as configurações
- **Falha ao restaurar compra?** Verifique a mesma conta da loja; reinstale se persistir
- **Campo redefinido para 0?** Entradas vazias/negativas se ajustam automaticamente ao perder o foco — reinsira o valor
- **Botões do stepper sumiram?** Aparecem ao lado de campos com `data-step` — reinicie o aplicativo se estiverem faltando
- **Aviso de temperatura desatualizada?** Redefine para 20 a cada inicialização — defina novamente para esta sessão

---

Contato `support@evdiag.net` — inclua modelo do dispositivo, versão do aplicativo (Configurações → parte inferior) e descrição do que você tentou.
""",

'pl': """# NVH Source Locator — Skrócona instrukcja

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
""",

'ru': """# NVH Source Locator — Краткий справочник

Одностраничное напоминание. Полные подробности см. в `user-guide.md`.

---

## Основной процесс (2-Sensor, бесплатно)

1. **Выберите материал** — вкладка Materials → коснитесь вашего материала
2. **Введите калибровку** во вкладке 2-Sensor:
   - Расстояние между датчиками (`d`)
   - Задержка времени калибровки (`tCal`) — автоматически заполняется из материала
3. **Введите событие** — `tEvent` и Первый датчик (A или B)
4. **Прочитайте результат** — расстояние от датчика A

![Вкладка 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Все вкладки

| Вкладка | Результат | Поля Pro? |
|---|---|---|
| 2-Sensor | Расстояние по линии | Нет (полностью бесплатно) |
| 3-Sensor | X, Y на поверхности | Да |
| 3-Sen+ | X, Y с МНК по 3 парам | Да |
| 4-Sensor | X, Y из двух пар (A–B + C–D) | Да |
| 4-Sen+ | X, Y из 4 датчиков, произвольная позиция | Да |
| 3D | X, Y, Z из 4 датчиков | Да |
| 3D+ | X, Y, Z из до 6 датчиков | Да |
| Materials | Выбор скорости звука | Нет |
| Help | Учебные материалы | Нет |

Настройки находятся в значке ⚙ (вверху справа), а не во вкладке.

---

## Температурная компенсация

Настройки → Опорная температура, диапазон **от -40 до +200 °C**.

- **14 металлов** имеют встроенную компенсацию (алюминий, стали, медь, латунь, бронза, титан, магний, свинец, цинк, никель, вольфрам, железо, чугун)
- Материалы без компенсации показывают **«ref only»**
- **Сбрасывается до 20 °C при каждом запуске приложения** (безопасный запуск по умолчанию)
- Воспроизведение записи истории восстанавливает её исходную температуру

---

## Сочетания клавиш

- **Коснитесь материала** → автоматически заполняет все поля `tCal` во всех вкладках
- **Удерживайте +/-** на числовых полях → быстрое инкрементирование
- **Перетащите горизонтально** на числовом поле → прокрутка значений
- **Пустой/отрицательный/недопустимый ввод** → переключается на 0 при потере фокуса (поле температуры ограничено -40/200)
- **Отметьте материал звёздочкой** → перемещает его в верх выбора

---

## Модель Pro

**Freemium с блокировкой по функциям** ($19,99):
- Бесплатно: вкладка 2-Sensor полностью функциональна, без ограничений
- Pro: Другие вкладки доступны, но с **полями с золотым замком**, которые показывают paywall при касании

Pro разблокирует: от 3-Sensor до 3D+, пользовательские материалы, резервное копирование/восстановление, PDF-отчёты, аннотирование фотографий.

![Paywall](../screenshots/07-paywall.png)

---

## Отчёты и резервное копирование

Кнопка **Распечатать результат** на любом экране результатов → PDF с заголовком, входными данными, результатом, визуализацией, фотографией (если сделана) и нижним колонтитулом температуры (когда компенсация активна).

Настройте заголовок в Настройки → Заголовок отчёта.

**Резервное копирование**: Настройки → Резервное копирование → поделиться в облако/электронную почту.  
**Восстановление**: Настройки → Восстановление → выберите файл резервной копии.

---

## Восстановление Pro на новом устройстве

Тот же аккаунт Google (Android) или Apple ID (iOS), с которого вы купили → Настройки → **Восстановить покупку** → разблокировка в течение секунд.

Автоматическое восстановление происходит незаметно, когда вы возвращаетесь в приложение после внешнего активирования промокода.

---

## Быстрое устранение неполадок

- **Результат вне диапазона?** Проверьте знак `tEvent` / Первый датчик / расстояние между датчиками
- **Неверный ближайший материал?** Опорная температура, вероятно, случайно установлена — проверьте настройки
- **Не удаётся восстановить покупку?** Проверьте тот же аккаунт магазина; переустановите, если проблема не устраняется
- **Поле сброшено на 0?** Пустые/отрицательные значения автоматически устанавливаются при потере фокуса — введите значение заново
- **Кнопки степпера пропали?** Они появляются рядом с полями с `data-step` — перезапустите приложение, если их нет
- **Предупреждение об устаревшей температуре?** Сбрасывается на 20 при каждом запуске — установите заново для этой сессии

---

Контакт `support@evdiag.net` — укажите модель устройства, версию приложения (Настройки → внизу) и описание того, что вы пытались сделать.
""",

'zh': """# NVH Source Locator — 快速参考

单页提要。完整详情请参阅 `user-guide.md`。

---

## 核心流程 (2-Sensor，免费)

1. **选择材料** — Materials 标签页 → 点击您的材料
2. **输入校准** 在 2-Sensor 标签页：
   - 传感器间距 (`d`)
   - 校准时间延迟 (`tCal`) — 从材料自动填充
3. **输入事件** — `tEvent` 和首先检测的传感器 (A 或 B)
4. **读取结果** — 距传感器 A 的距离

![2-Sensor 标签页](../screenshots/01-home-2sensor.png)

---

## 所有标签页

| 标签页 | 输出 | 是否含 Pro 字段？ |
|---|---|---|
| 2-Sensor | 沿直线的距离 | 否（完全免费） |
| 3-Sensor | 表面上的 X、Y | 是 |
| 3-Sen+ | 通过 3 对最小二乘法计算的 X、Y | 是 |
| 4-Sensor | 来自两对的 X、Y (A–B + C–D) | 是 |
| 4-Sen+ | 来自任意位置的 4 个传感器的 X、Y | 是 |
| 3D | 来自 4 个传感器的 X、Y、Z | 是 |
| 3D+ | 来自最多 6 个传感器的 X、Y、Z | 是 |
| Materials | 声速选择器 | 否 |
| Help | 教程 | 否 |

设置位于 ⚙ 图标（右上角），不是一个标签页。

---

## 温度补偿

设置 → 参考温度，范围 **-40 至 +200 °C**。

- **14 种金属** 具有内置补偿（铝、各种钢材、铜、黄铜、青铜、钛、镁、铅、锌、镍、钨、铁、铸铁）
- 没有补偿的材料显示 **"ref only"**
- **每次启动应用程序时重置为 20 °C**（默认安全启动）
- 回放历史记录条目时会恢复其原始温度

---

## 快捷方式

- **点击材料** → 自动填充所有标签页中的所有 `tCal` 字段
- **按住 +/-** 在数字字段上 → 快速递增
- **水平拖动** 在数字字段上 → 调整值
- **空/负数/无效输入** → 失去焦点时调整为 0（温度字段限制在 -40/200）
- **将材料标记为星标** → 移到选择器顶部

---

## Pro 模式

**按功能锁定的免费增值模式**（$19.99）：
- 免费：2-Sensor 标签页完全可用，无限制
- Pro：其他标签页可访问，但带有**金色锁定字段**，点击时显示付费墙

Pro 解锁：3-Sensor 至 3D+、自定义材料、备份/恢复、PDF 报告、照片注释。

![付费墙](../screenshots/07-paywall.png)

---

## 报告和备份

任何结果屏幕上的 **打印结果** 按钮 → 带有页眉、输入、结果、可视化、照片（如果拍摄）和温度页脚（当补偿激活时）的 PDF。

在设置 → 报告页眉中自定义页眉。

**备份**：设置 → 备份 → 分享到云/电子邮件。  
**恢复**：设置 → 恢复 → 选择备份文件。

---

## 在新设备上恢复 Pro

使用相同的 Google 帐户 (Android) 或 Apple ID (iOS) 购买 → 设置 → **恢复购买** → 几秒钟内解锁。

当您在外部兑换促销代码后返回应用程序时，自动恢复会在后台静默进行。

---

## 快速故障排除

- **结果超出范围？** 检查 `tEvent` 符号 / 首先检测的传感器 / 传感器间距
- **最接近的材料不对？** 参考温度可能被意外设置 — 检查设置
- **恢复购买失败？** 验证相同的商店帐户；如果问题持续存在，请重新安装
- **字段被设为 0？** 空/负值在失去焦点时自动调整 — 重新输入值
- **步进器按钮消失？** 它们出现在带有 `data-step` 的字段旁 — 如果缺失，请重启应用程序
- **温度过时警告？** 每次启动时重置为 20 — 为此会话重新设置

---

联系 `support@evdiag.net` — 请包括设备型号、应用版本（设置 → 底部）以及您尝试过的内容的描述。
""",

}
