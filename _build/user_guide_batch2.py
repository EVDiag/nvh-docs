"""User Guide translations — batch 2.

4 languages: pt, pl, ru, zh.
"""

USER_GUIDE_TRANSLATIONS = {

'pt': """# NVH Source Locator — Guia do Usuário

NVH Source Locator é uma ferramenta de medição para localizar fontes de ruído e vibração usando TDOA (Time Difference of Arrival) a partir de sinais de acelerômetros capturados em um osciloscópio ou sistema de medição.

Este guia cobre todos os recursos. Para uma revisão rápida, consulte `quick-reference.md`.

> **Nota sobre as capturas de tela**: Este documento usa capturas de tela de espaço reservado do aplicativo. Substitua cada `../screenshots/*.png` por capturas de tela reais do dispositivo conforme você as captura.

---

## Sumário

1. [Como funciona](#how-it-works)
2. [Antes de começar](#before-you-start)
3. [As abas principais](#the-main-tabs)
4. [Modo 2-Sensor](#2-sensor-mode)
5. [Modo 3-Sensor](#3-sensor-mode)
6. [Modos Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [A aba Materials](#the-materials-tab)
8. [Compensação de temperatura](#temperature-compensation)
9. [Anotação de fotos](#photo-annotation)
10. [Relatórios](#reports)
11. [Backup e restauração](#backup-and-restore)
12. [Configurações](#settings)
13. [Recursos Pro](#pro-features)
14. [Aba Help e tutoriais](#help-tab-and-tutorials)
15. [Solução de problemas](#troubleshooting)

---

## Como funciona

Quando uma fonte de ruído emite um som ou vibração, a onda viaja através de um material em uma velocidade conhecida. Se você colocar dois ou mais acelerômetros no material e medir quando a onda chega a cada um, a diferença de tempo indica onde está a fonte.

NVH Source Locator usa:

- **Calibração**: a distância entre sensores e o tempo que uma onda leva para percorrer essa distância (usado para calcular a velocidade do som do material)
- **Evento**: a diferença de tempo entre os sensores detectando o evento de ruído/vibração

Então calcula onde está a fonte na estrutura.

Quanto mais sensores você usar, mais precisamente poderá localizar a fonte:

- **2 sensores** → distância ao longo de uma linha
- **3 sensores** → posição em uma superfície 2D (X, Y)
- **4 sensores** → posição no espaço 3D (X, Y, Z)

---

## Antes de começar

Você precisará de:

- **Um osciloscópio ou sistema de medição** que possa mostrar a diferença de tempo entre canais de acelerômetro em microssegundos (µs)
- **Pelo menos 2 acelerômetros** fisicamente conectados à estrutura (mais sensores = maior precisão)
- **Uma forma de medir distância** entre sensores (trena, paquímetro)
- **Uma forma de acionar uma onda** em um local conhecido para calibração (impacto de martelo calibrado, batida de chave de fenda ou outro sinal conhecido)

![Tela inicial com aba 2-Sensor](../screenshots/01-home-2sensor.png)

---

## As abas principais

O aplicativo tem abas no topo:

![Barra de abas](../screenshots/02-tab-bar.png)

| Aba | O que faz | Quando usar |
|---|---|---|
| **2-Sensor** | Localização de fonte 1D ao longo de uma linha entre 2 sensores | Verificações rápidas, estruturas tipo viga. **Totalmente gratuito.** |
| **3-Sensor** | Localização de fonte 2D usando 3 sensores em um triângulo | Uso mais geral, painéis e superfícies |
| **3-Sen+** | 3-Sensor com solucionador de mínimos quadrados sobredeterminado | Medições mais exigentes, robusto a ruído |
| **4-Sensor** | Localização 2D usando dois pares (A-B + C-D) | Layouts retangulares de sensores, verificação cruzada |
| **4-Sen+** | Modo 2D avançado, 4 sensores em qualquer posição | Geometrias não retangulares, LSQ completo |
| **3D** | Localização de fonte 3D usando 4 sensores com coordenadas XYZ | Estruturas complexas no espaço 3D |
| **3D+** | 3D com até 6 sensores, LSQ sobredeterminado | Geometrias muito complexas, máxima precisão |
| **Materials** | Biblioteca de velocidade do som + materiais personalizados | Selecionar uma vez por sessão de medição |
| **Help** | Tutoriais no aplicativo e referência | Quando você precisar de uma revisão rápida |

> **Gratuito vs Pro**: A aba 2-Sensor é totalmente gratuita. Outras abas são acessíveis mas têm campos de entrada específicos bloqueados para usuários Pro (marcados com um emblema de cadeado dourado). Tocar em um campo bloqueado mostra a paywall Pro.

As Configurações são acessadas através do ícone de engrenagem ⚙ no canto superior direito (não é uma aba).

---

## Modo 2-Sensor

A medição mais simples: localização de fonte ao longo de uma linha entre dois acelerômetros.

![Aba 2-Sensor](../screenshots/01-home-2sensor.png)

### Passo 1: Aplicar um material

Toque na aba Materials. Escolha o material do qual sua estrutura é feita (por exemplo, "Alumínio", "Aço, Mild (1020)"). O aplicativo usa a velocidade do som conhecida do material para preencher automaticamente o campo de tempo de calibração.

Se o material da sua estrutura não estiver na lista, você pode selecionar "Ar" temporariamente e substituir o tempo de calibração manualmente no passo 2.

### Passo 2: Inserir dados de calibração

Na aba 2-Sensor, você verá duas seções de pares: **Par A–B** e **Par A–C** (apenas A–B é necessário se você tiver apenas 2 sensores).

Para cada par, você preenche:

- **Espaçamento entre sensores** (`d`): distância física entre sensores, em cm ou polegadas (definido nas Configurações)
- **Atraso de tempo de calibração** (`tCal`): tempo para uma onda viajar entre os sensores na velocidade do som do material — preenchido automaticamente quando você seleciona um material, mas você pode substituir

### Passo 3: Inserir o tempo do evento

- **Atraso de tempo do evento** (`tEvent`): diferença de tempo entre sensores detectando o evento de ruído, em microssegundos
- **Primeiro sensor**: qual sensor ouviu o evento primeiro (A ou B)

### Passo 4: Ler o resultado

O aplicativo mostra a posição da fonte como uma distância do sensor A:
- Resultado = 0: a fonte está no sensor A
- Resultado = distância: a fonte está no sensor B
- Resultado intermediário: a fonte está entre eles
- Resultado externo: a fonte está além de um dos sensores (o toast avisará)

O cartão de resultado mostra ambas as distâncias (de A, de B) e indica qual sensor está mais próximo.

### Passo 5 (opcional): Anotar uma foto

Toque em **📷 Anotar foto** para tirar uma foto da sua configuração. O aplicativo sobrepõe marcadores para os sensores A, B e a fonte. Útil para relatórios.

---

## Modo 3-Sensor

Localiza uma fonte em um plano 2D usando três sensores dispostos em um triângulo.

![Aba 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configuração

Coloque três sensores na sua estrutura formando um triângulo. Equilátero, retângulo ou escaleno — o aplicativo lida com todas as geometrias.

### Inserir os dados

Na seção **Comprimentos dos lados do triângulo**, insira a distância física para todos os três lados (A–B, A–C, B–C).

Para cada par (A–B e A–C), insira:
- **tCal**: tempo de calibração (preenchido automaticamente do material)
- **tEvent**: diferença de tempo medida para o evento de ruído
- **Primeiro sensor**: qual ouviu primeiro

### Ler o resultado

O aplicativo mostra a posição da fonte como coordenadas X, Y relativas ao sensor A (sensor A na origem, sensor B no eixo X). A visualização mostra os três sensores e a localização da fonte.

![Resultado do triângulo](../screenshots/04-triangle-result.png)

---

## Modos Pro+

Várias abas avançadas oferecem solucionadores sobredeterminados e maior dimensionalidade:

### 3-Sen+ (Pro)

Mesma configuração triangular que 3-Sensor, mas calibre E meça todos os três pares (A–B, A–C, B–C). O solucionador usa todas as 3 TDOAs em um ajuste de mínimos quadrados — mais robusto ao ruído de medição e materiais anisotrópicos. Resíduos por par são relatados para que você possa detectar medições inconsistentes.

### 4-Sensor

Coloque quatro sensores ao redor da área:
- **A–B** = par horizontal (lados esquerdo/direito)
- **C–D** = par vertical (lados superior/inferior)

Execute o par A–B primeiro (horizontal), depois o par C–D (vertical). O mapa 2D mostra a intersecção. Cada par é calibrado separadamente — útil quando o material varia através da estrutura.

### 4-Sen+ (2D Avançado)

Quatro sensores em qualquer posição (não forçados a retangular). Empareje A com cada um de B, C, D e calibre separadamente. O solucionador de mínimos quadrados sobredeterminado faz a média do ruído de medição por par e relata os resíduos por par.

### 3D

Medição 3D completa com 4 sensores colocados no espaço 3D. Insira as coordenadas (X, Y, Z) de cada sensor, além dos tempos de calibração e evento para cada par (A–B, A–C, A–D).

### 3D+ (Pro)

Como 3D, mas suporta até **6 sensores** (A a F) com LSQ sobredeterminado. Máxima precisão para geometrias 3D complexas.

---

## A aba Materials

Biblioteca de materiais comuns de engenharia com velocidade do som conhecida a 20 °C.

![Aba Materials](../screenshots/05-materials-tab.png)

### Lista de materiais

A lista inclui ar, fluidos, borrachas, polímeros, madeiras, vidros e metais. As velocidades variam de ~340 m/s (ar) a ~13.000 m/s (alguns metais à temperatura ambiente).

### Materiais integrados com compensação de temperatura

14 metais comumente usados incluem dados de coeficiente de temperatura. Quando a Temperatura de referência nas Configurações difere de 20 °C, o aplicativo ajusta automaticamente as velocidades desses materiais:

- Alumínio
- Aço, Mild (1020)
- Aço Inoxidável (304)
- Ferro (fundido)
- Ferro
- Cobre
- Latão
- Bronze
- Titânio
- Magnésio
- Chumbo
- Zinco
- Níquel
- Tungstênio

Materiais com compensação mostram dois valores no seletor: a **velocidade compensada** (grande, em destaque) e a **velocidade de referência a 20 °C** (pequena, em cinza abaixo).

Materiais sem compensação mostram **"ref only"** em itálico — sua velocidade listada é usada como está, independentemente da temperatura.

### Materiais personalizados

Se você medir uma calibração na aba 2-Sensor, pode salvar o resultado como um material personalizado. Após uma medição 2-sensor bem-sucedida, procure a opção para salvar a velocidade derivada sob um nome de sua escolha.

Materiais personalizados armazenam a velocidade medida in-situ; eles nunca aplicam compensação de temperatura (a velocidade já foi medida na temperatura de teste).

### Favoritos

Toque na estrela ao lado de qualquer material para marcá-lo como favorito. Favoritos aparecem no topo da lista para acesso rápido.

### Pesquisa

Use a barra de pesquisa no topo para filtrar materiais por nome. A pesquisa corresponde tanto a nomes canônicos em inglês quanto a nomes de exibição traduzidos.

---

## Compensação de temperatura

A velocidade do som em materiais muda com a temperatura. Em testes NVH automotivos, isso importa: um compartimento do motor a 80 °C, uma cabine resfriada a -10 °C ou uma área do coletor de escape a 200 °C se comportam de maneira diferente das condições de laboratório à temperatura ambiente.

### Configuração da temperatura

Abra Configurações (ícone ⚙) → Temperatura de referência. Insira a temperatura do seu ambiente de teste em °C (faixa -40 a +200).

![Painel de Configurações](../screenshots/06-settings.png)

### O que acontece quando a temperatura ≠ 20 °C

- Os campos de tempo de calibração são preenchidos automaticamente com a velocidade ajustada por temperatura
- O seletor de Materials mostra a velocidade ajustada com destaque
- Um toast confirma: *"Alumínio aplicado (6.284 m/s @ 60 °C) — N par(es) atualizado(s)"*
- A dica "Material mais próximo" compara com velocidades ajustadas por temperatura
- Entradas do histórico salvas registram a temperatura ativa
- Relatórios incluem uma linha de rodapé: *"Temperatura de referência: 60 °C, compensação aplicada"*

### Redefinir ao iniciar o aplicativo

A Temperatura de referência **sempre redefine para 20 °C** quando você inicia o aplicativo. Isso evita que configurações desatualizadas de uma sessão de medição passada afetem silenciosamente o trabalho de hoje. Uma pequena nota em itálico nas Configurações lembra esse comportamento.

Se você quiser reproduzir uma medição histórica em sua temperatura original, basta tocar na entrada — a temperatura é restaurada automaticamente.

### Materiais sem compensação

A maioria dos materiais não metálicos não tem coeficientes de temperatura publicados confiáveis. O aplicativo mostra um emblema **"ref only"** para esses — sua velocidade listada é usada independentemente da configuração de temperatura. Se você precisar de medições precisas em temperaturas não ambientes para esses materiais, realize uma calibração in-situ e salve o resultado como um material personalizado.

---

## Anotação de fotos

Após um cálculo bem-sucedido, toque no botão **📷 Anotar foto** para sobrepor marcadores de sensor e fonte em uma foto da sua configuração.

![Anotação de foto](../screenshots/08-photo-annotation.png)

### Fluxo

1. Toque em **Anotar foto** — a câmera do sistema é aberta
2. Tire uma foto da colocação dos seus sensores
3. O aplicativo carrega a foto na sobreposição de anotação
4. Marcadores de sensor (A, B, C, D, E, F conforme aplicável — até 6 sensores) e o marcador de fonte são posicionados automaticamente com base em seu cálculo
5. Arraste qualquer marcador para ajustar a posição. Conforme você ajusta, a posição da fonte é recalculada a partir das posições corrigidas dos sensores
6. Toque em **Salvar** para manter, ou **Refazer** para tentar novamente

A foto anotada é incluída automaticamente nos relatórios PDF.

---

## Relatórios

Toque no botão **Imprimir resultado** em qualquer tela de resultados para gerar um relatório formatado.

![Relatório PDF](../screenshots/09-pdf-report.png)

### Conteúdo do relatório

- Cabeçalho (personalizável em Configurações → Cabeçalho do relatório)
- Título da medição e timestamp
- Todos os valores de entrada em uma tabela limpa
- Resultado do cálculo
- Texto de conclusão
- Visualização (gráfico de geometria)
- Foto anotada (se você tirou uma)
- Linha de rodapé de temperatura (se a compensação estava ativa)
- Número de página e linha de crédito

### Formato de saída

- **Android**: geração PDF nativa, salvar em seu telefone ou compartilhar
- **iOS**: caixa de diálogo de impressão do sistema → salvar como PDF, AirPrint ou compartilhar

### Personalizando o cabeçalho

Configurações → Cabeçalho do relatório. Insira o nome da sua empresa, nome do laboratório, informações do projeto, ou o que quiser no topo de cada relatório.

---

## Backup e restauração

Salve todos os seus materiais personalizados, favoritos, configurações e histórico em um único arquivo. Transferir entre dispositivos.

### Backup

Configurações → **Backup** → toque em "Salvar arquivo de backup". O aplicativo gera um arquivo JSON e abre a folha de compartilhamento do seu telefone. Salve-o em sua unidade na nuvem (Google Drive, iCloud, OneDrive), envie por e-mail para si mesmo ou transfira da maneira que preferir.

### Restaurar

Configurações → **Restaurar** → escolha o arquivo de backup do armazenamento do seu telefone. O aplicativo importa materiais personalizados, favoritos, histórico e configurações.

⚠️ **A restauração substitui seus dados atuais.** Se você tiver medições importantes no dispositivo atual, faça backup delas primeiro antes de restaurar de um backup diferente.

---

## Configurações

Acesso através do ícone de engrenagem ⚙ no canto superior direito. Configurações é um modal, não uma aba.

![Configurações](../screenshots/06-settings.png)

| Configuração | O que controla |
|---|---|
| **Atualizar para Pro** | Comprar ou aprender sobre os recursos Pro ($19,99) |
| **Idioma** | Idioma de exibição do aplicativo (30 suportados) |
| **Tema** | Claro, Escuro ou Auto (seguir o sistema) |
| **Unidade de distância** | cm ou polegadas |
| **Temperatura de referência** | Temperatura ativa para compensação, -40 a +200 °C |
| **Cabeçalho do relatório** | Texto personalizado no topo dos relatórios gerados |
| **Backup** | Exportar todos os dados para um arquivo |
| **Restaurar** | Importar dados de um arquivo de backup |
| **Restaurar compra** | Readquirir Pro em um novo dispositivo |

---

## Recursos Pro

NVH Source Locator usa um **modelo freemium com bloqueio por recurso**:

- **Gratuito**: A aba 2-Sensor é totalmente funcional sem limites
- **Pro**: Todas as outras abas têm campos de entrada específicos bloqueados. A paywall aparece quando um usuário gratuito toca em um campo bloqueado

### O que está bloqueado

Campos exigidos por Pro estão espalhados por:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modos 3D e 3D+
- Backup e Restaurar
- Relatórios PDF
- Materiais personalizados
- Anotação de fotos

Um usuário gratuito pode ABRIR qualquer aba e VER a interface. Ele simplesmente não pode inserir valores nos campos de entrada bloqueados por Pro.

![Campo bloqueado por Pro](../screenshots/11-pro-locked-field.png)

### A paywall

![Paywall](../screenshots/07-paywall.png)

Quando um usuário gratuito toca em um campo bloqueado, a paywall desliza mostrando:
- Ícone do aplicativo com emblema PRO
- Lista de recursos
- Botão de desbloqueio com preço ($19,99 padrão; pode variar por região)
- Resgate de código promocional (apenas Android — iOS usa o fluxo de Código de Oferta separado da Apple)
- Link promocional opcional para canais da comunidade

### Comprando Pro

Toque em qualquer campo bloqueado, ou toque em **Atualizar para Pro** nas Configurações. Usa o sistema de pagamento oficial da sua plataforma (Google Play no Android, Apple App Store no iOS).

### Restaurando Pro em um novo dispositivo

Se você comprou em um dispositivo e quer Pro em outro (mesma conta):

1. Faça login na **mesma** conta Google (Android) ou Apple ID (iOS) que você usou para comprar
2. Abra NVH Source Locator no novo dispositivo
3. Vá para Configurações → **Restaurar compra**
4. O aplicativo verifica com os registros de compra da plataforma e desbloqueia Pro

### Auto-restauração na inicialização

Se você resgatar um código promocional na Google Play Store ou App Store enquanto o NVH Source Locator está sendo executado em segundo plano, retornar ao aplicativo detecta automaticamente a nova compra e desbloqueia Pro — não é necessária Restauração manual.

### Resgate de código promocional

**Android**: um botão "Tem um código promocional do Google Play?" na paywall abre o fluxo de resgate do Google Play com seu código pré-preenchido.

**iOS**: A política da App Store 3.1.1 exige resgate através do fluxo "Resgatar código" oficial da Apple. O botão Google Play está oculto no iOS. Procure por "Resgatar código da App Store" nas Configurações.

---

## Aba Help e tutoriais

A aba **Help** inclui tutoriais no aplicativo, guias de melhores práticas e informações de referência.

![Aba Help](../screenshots/10-help-tab.png)

Tópicos cobertos:
- Quais equipamentos você precisa
- Como posicionar sensores para melhor precisão
- Dicas de calibração
- Cenários de medição comuns
- Dicas para triangulação e posicionamentos 3D
- Roteamento de cabos e qualidade do sinal

---

## Solução de problemas

### O resultado do cálculo está errado ou não faz sentido

1. Verifique sua calibração. O `tCal` preenchido automaticamente assume a velocidade publicada do material — materiais reais variam. A calibração mais precisa é in-situ: toque em um local conhecido e deixe o aplicativo derivar a velocidade real.
2. Verifique a configuração do **Primeiro sensor** — qual sensor ouviu o evento primeiro importa para a matemática.
3. Verifique suas medições de distância. Erros de alguns mm se propagam.

### Toast diz "Resultado fora do intervalo"

A matemática diz que a fonte não está entre seus sensores. Possíveis causas:
- A fonte está realmente fora da linha/plano do sensor
- Uma de suas entradas está errada
- A velocidade de calibração está muito longe da realidade

### A dica de velocidade de cálculo mostra uma cor de aviso

A velocidade do som implícita de suas entradas está longe de qualquer material comum (menos de 50 m/s ou mais de 20.000 m/s). Verifique suas entradas — provavelmente um erro de digitação em tCal ou distância.

### O seletor de Materials mostra velocidades diferentes do esperado

Verifique a Temperatura de referência nas Configurações. Se não for 20 °C, as velocidades exibidas refletem a compensação de temperatura. O aplicativo mostra "ref X @ 20°C" abaixo das velocidades compensadas para que você possa verificar.

### Entrada do histórico reproduz com resultado diferente

Entradas antigas do histórico criadas antes da versão 1.75 do aplicativo podem não ter armazenado a temperatura. Se você fez a medição em uma temperatura não-20 °C, a reprodução usará a configuração atual. Defina manualmente a temperatura nas Configurações antes de reproduzir, OU re-meça.

### Marcadores de anotação de foto não estão onde eu espero

Os marcadores se posicionam automaticamente com base na geometria de entrada. Arraste-os para ajustar. Ajustar marcadores atualiza a posição da fonte na sobreposição da foto — mas NÃO altera o resultado de cálculo subjacente.

### Backup/Restauração falha

Certifique-se de que está usando um arquivo de backup gerado pela mesma versão ou versão mais recente do aplicativo. Arquivos de backup mais antigos podem não ter campos de dados atuais.

### Restaurar compra diz "nenhuma compra encontrada"

1. Verifique se você está conectado à mesma conta da loja que usou para comprar
2. Verifique se a compra não foi reembolsada ou expirou
3. Tente desinstalar e reinstalar o aplicativo (a compra está vinculada à sua conta da loja, não à instalação do aplicativo)
4. Contate support@evdiag.net se persistir

### Entrada numérica salta para 0 inesperadamente

Por design: quando você desfoca um campo numérico (toca em outro lugar), se ele estiver vazio, negativo ou contiver texto não numérico, ele salta para 0. Evita cálculos silenciosamente quebrados de entradas acidentalmente limpas. A entrada de temperatura está isenta (em vez disso, ela limita a -40/+200).

### Precisa de mais ajuda

Contate `support@evdiag.net` com:
- O modelo e a versão do SO do seu dispositivo
- A versão do aplicativo (Configurações → parte inferior da página)
- Descrição do que você tentou
- Capturas de tela, se possível

---

*NVH Source Locator é desenvolvido pela EVDiag. Visite https://evdiag.net para atualizações e recursos.*
""",

'pl': """# NVH Source Locator — Podręcznik użytkownika

NVH Source Locator to narzędzie pomiarowe do lokalizowania źródeł hałasu i drgań przy użyciu TDOA (Time Difference of Arrival) z sygnałów akcelerometrów rejestrowanych na oscyloskopie lub systemie pomiarowym.

Ten przewodnik obejmuje wszystkie funkcje. Aby uzyskać szybkie przypomnienie, zobacz `quick-reference.md`.

> **Uwaga dotycząca zrzutów ekranu**: Ten dokument używa zastępczych zrzutów ekranu z aplikacji. Zastąp każdy plik `../screenshots/*.png` rzeczywistymi zrzutami ekranu urządzenia, gdy je wykonasz.

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
""",

'ru': """# NVH Source Locator — Руководство пользователя

NVH Source Locator — это измерительный инструмент для локализации источников шума и вибрации с использованием TDOA (Time Difference of Arrival) из сигналов акселерометров, захваченных на осциллографе или измерительной системе.

Это руководство охватывает все функции. Для краткого напоминания см. `quick-reference.md`.

> **Примечание о скриншотах**: Этот документ использует скриншоты-заполнители из приложения. Замените каждый `../screenshots/*.png` реальными скриншотами устройства по мере их получения.

---

## Содержание

1. [Как это работает](#how-it-works)
2. [Перед началом работы](#before-you-start)
3. [Основные вкладки](#the-main-tabs)
4. [Режим 2-Sensor](#2-sensor-mode)
5. [Режим 3-Sensor](#3-sensor-mode)
6. [Режимы Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Вкладка Materials](#the-materials-tab)
8. [Температурная компенсация](#temperature-compensation)
9. [Аннотирование фото](#photo-annotation)
10. [Отчёты](#reports)
11. [Резервное копирование и восстановление](#backup-and-restore)
12. [Настройки](#settings)
13. [Функции Pro](#pro-features)
14. [Вкладка Help и учебные материалы](#help-tab-and-tutorials)
15. [Устранение неполадок](#troubleshooting)

---

## Как это работает

Когда источник шума испускает звук или вибрацию, волна распространяется через материал с известной скоростью. Если вы разместите два или более акселерометра на материале и измерите, когда волна доходит до каждого из них, разница во времени укажет, где находится источник.

NVH Source Locator принимает:

- **Калибровку**: расстояние между датчиками и время, за которое волна проходит это расстояние (используется для вычисления скорости звука материала)
- **Событие**: разница во времени между датчиками, обнаруживающими событие шума/вибрации

Затем он вычисляет, где в структуре находится источник.

Чем больше датчиков вы используете, тем точнее можно определить источник:

- **2 датчика** → расстояние вдоль линии
- **3 датчика** → положение на 2D-поверхности (X, Y)
- **4 датчика** → положение в 3D-пространстве (X, Y, Z)

---

## Перед началом работы

Вам понадобится:

- **Осциллограф или измерительная система**, которые могут показать разницу во времени между каналами акселерометра в микросекундах (мкс)
- **Не менее 2 акселерометров**, физически прикреплённых к структуре (больше датчиков = выше точность)
- **Способ измерения расстояния** между датчиками (рулетка, штангенциркуль)
- **Способ запуска волны** в известном месте для калибровки (калиброванный удар молотка, удар отвёрткой или другой известный сигнал)

![Главный экран с вкладкой 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Основные вкладки

В приложении есть вкладки сверху:

![Панель вкладок](../screenshots/02-tab-bar.png)

| Вкладка | Что делает | Когда использовать |
|---|---|---|
| **2-Sensor** | 1D-локализация источника вдоль линии между 2 датчиками | Быстрые проверки, балочные структуры. **Полностью бесплатно.** |
| **3-Sensor** | 2D-локализация источника с использованием 3 датчиков в треугольнике | Наиболее общий случай использования, панели и поверхности |
| **3-Sen+** | 3-Sensor с переопределённым решателем наименьших квадратов | Более требовательные измерения, устойчивые к шуму |
| **4-Sensor** | 2D-локализация с использованием двух пар (A-B + C-D) | Прямоугольные расположения датчиков, перекрёстная проверка |
| **4-Sen+** | Расширенный 2D-режим, 4 датчика в любых положениях | Не-прямоугольные геометрии, полный LSQ |
| **3D** | 3D-локализация источника с использованием 4 датчиков с XYZ-координатами | Сложные структуры в 3D-пространстве |
| **3D+** | 3D с до 6 датчиков, переопределённый LSQ | Очень сложные геометрии, максимальная точность |
| **Materials** | Библиотека скорости звука + пользовательские материалы | Выбирать один раз за сессию измерений |
| **Help** | Учебные материалы в приложении и справка | Когда нужно быстрое напоминание |

> **Бесплатное vs Pro**: Вкладка 2-Sensor полностью бесплатна. Другие вкладки доступны, но имеют определённые поля ввода, заблокированные для пользователей Pro (отмечены значком золотого замка). Касание заблокированного поля показывает paywall Pro.

Настройки доступны через значок шестерёнки ⚙ в правом верхнем углу (не вкладка).

---

## Режим 2-Sensor

Простейшее измерение: локализация источника вдоль линии между двумя акселерометрами.

![Вкладка 2-Sensor](../screenshots/01-home-2sensor.png)

### Шаг 1: Применение материала

Коснитесь вкладки Materials. Выберите материал, из которого сделана ваша структура (например, «Алюминий», «Сталь, Mild (1020)»). Приложение использует известную скорость звука материала для автоматического заполнения поля времени калибровки.

Если материал вашей структуры отсутствует в списке, можно временно выбрать «Воздух» и вручную переопределить время калибровки в шаге 2.

### Шаг 2: Ввод данных калибровки

На вкладке 2-Sensor вы увидите два раздела пар: **Пара A–B** и **Пара A–C** (требуется только A–B, если у вас только 2 датчика).

Для каждой пары вы заполняете:

- **Расстояние между датчиками** (`d`): физическое расстояние между датчиками, в см или дюймах (устанавливается в Настройках)
- **Задержка времени калибровки** (`tCal`): время, за которое волна проходит между датчиками со скоростью звука материала — автоматически заполняется при выборе материала, но можно переопределить

### Шаг 3: Ввод времени события

- **Задержка времени события** (`tEvent`): разница во времени между датчиками, обнаруживающими событие шума, в микросекундах
- **Первый датчик**: какой датчик услышал событие первым (A или B)

### Шаг 4: Считывание результата

Приложение показывает положение источника как расстояние от датчика A:
- Результат = 0: источник у датчика A
- Результат = расстояние: источник у датчика B
- Результат между: источник между ними
- Результат снаружи: источник за пределами одного из датчиков (toast предупредит)

Карточка результата показывает оба расстояния (от A, от B) и указывает, какой датчик ближе.

### Шаг 5 (опционально): Аннотирование фото

Коснитесь **📷 Аннотировать фото**, чтобы сделать фото вашей установки. Приложение накладывает маркеры для датчиков A, B и источника. Полезно для отчётов.

---

## Режим 3-Sensor

Локализует источник на 2D-плоскости с использованием трёх датчиков, расположенных в треугольнике.

![Вкладка 3-Sensor](../screenshots/03-3sensor-tab.png)

### Настройка

Разместите три датчика на вашей структуре, образующих треугольник. Равносторонний, прямоугольный или разносторонний — приложение справляется со всеми геометриями.

### Ввод данных

В разделе **Длины сторон треугольника** введите физические расстояния для всех трёх сторон (A–B, A–C, B–C).

Для каждой пары (A–B и A–C) введите:
- **tCal**: время калибровки (автозаполнение из материала)
- **tEvent**: измеренная разница во времени для события шума
- **Первый датчик**: какой услышал первым

### Считывание результата

Приложение показывает положение источника как координаты X, Y относительно датчика A (датчик A в начале, датчик B на оси X). Визуализация показывает все три датчика и местоположение источника.

![Результат треугольника](../screenshots/04-triangle-result.png)

---

## Режимы Pro+

Несколько продвинутых вкладок предлагают переопределённые решатели и более высокую размерность:

### 3-Sen+ (Pro)

Та же треугольная установка, что и 3-Sensor, но калибруйте И измеряйте все три пары (A–B, A–C, B–C). Решатель использует все 3 TDOA в подгонке методом наименьших квадратов — более устойчиво к шуму измерения и анизотропным материалам. Остатки для каждой пары отображаются, чтобы можно было заметить несогласованные измерения.

### 4-Sensor

Разместите четыре датчика вокруг области:
- **A–B** = горизонтальная пара (левая/правая стороны)
- **C–D** = вертикальная пара (верхняя/нижняя стороны)

Запустите сначала пару A–B (горизонтальную), затем пару C–D (вертикальную). 2D-карта показывает пересечение. Каждая пара калибруется отдельно — полезно, когда материал варьируется по структуре.

### 4-Sen+ (Расширенный 2D)

Четыре датчика в любых положениях (не принудительно прямоугольных). Спарьте A с каждым из B, C, D и калибруйте отдельно. Переопределённый решатель методом наименьших квадратов усредняет шум измерения для каждой пары и сообщает остатки для каждой пары.

### 3D

Полное 3D-измерение с 4 датчиками, размещёнными в 3D-пространстве. Введите координаты (X, Y, Z) каждого датчика, плюс время калибровки и события для каждой пары (A–B, A–C, A–D).

### 3D+ (Pro)

Как 3D, но поддерживает до **6 датчиков** (от A до F) с переопределённым LSQ. Максимальная точность для сложных 3D-геометрий.

---

## Вкладка Materials

Библиотека распространённых инженерных материалов с известной скоростью звука при 20 °C.

![Вкладка Materials](../screenshots/05-materials-tab.png)

### Список материалов

Список включает воздух, жидкости, резины, полимеры, дерево, стекло и металлы. Скорости варьируются от ~340 м/с (воздух) до ~13 000 м/с (некоторые металлы при комнатной температуре).

### Встроенные материалы с температурной компенсацией

14 часто используемых металлов включают данные о температурном коэффициенте. Когда Опорная температура в Настройках отличается от 20 °C, приложение автоматически корректирует скорости этих материалов:

- Алюминий
- Сталь, Mild (1020)
- Нержавеющая сталь (304)
- Чугун (литой)
- Железо
- Медь
- Латунь
- Бронза
- Титан
- Магний
- Свинец
- Цинк
- Никель
- Вольфрам

Материалы с компенсацией показывают два значения в селекторе: **компенсированную скорость** (большую, выделенную) и **опорную скорость при 20 °C** (маленькую, серую под ней).

Материалы без компенсации показывают **«ref only»** курсивом — их указанная скорость используется как есть, независимо от температуры.

### Пользовательские материалы

Если вы измерите калибровку на вкладке 2-Sensor, можно сохранить результат как пользовательский материал. После успешного 2-sensor измерения найдите опцию сохранения полученной скорости под выбранным именем.

Пользовательские материалы хранят измеренную in-situ скорость; они никогда не применяют температурную компенсацию (скорость уже была измерена при тестовой температуре).

### Избранное

Коснитесь звёздочки рядом с любым материалом, чтобы пометить его как избранный. Избранные появляются вверху списка для быстрого доступа.

### Поиск

Используйте строку поиска вверху для фильтрации материалов по имени. Поиск соответствует как английским каноническим именам, так и переведённым отображаемым именам.

---

## Температурная компенсация

Скорость звука в материалах меняется с температурой. В автомобильных NVH-тестах это имеет значение: моторный отсек при 80 °C, охлаждённая кабина при -10 °C или область выпускного коллектора при 200 °C все ведут себя иначе, чем в лабораторных условиях при комнатной температуре.

### Установка температуры

Откройте Настройки (значок ⚙) → Опорная температура. Введите температуру вашей тестовой среды в °C (диапазон от -40 до +200).

![Панель Настройки](../screenshots/06-settings.png)

### Что происходит, когда температура ≠ 20 °C

- Поля времени калибровки автоматически заполняются скорректированной по температуре скоростью
- Селектор Materials прямо отображает скорректированную скорость
- Toast подтверждает: *«Алюминий применён (6 284 м/с @ 60 °C) — N пара(ы) обновлено»*
- Подсказка «Ближайший материал» сравнивает со скоростями, скорректированными по температуре
- Сохранённые записи истории фиксируют активную температуру
- Отчёты включают строку нижнего колонтитула: *«Опорная температура: 60 °C, применена компенсация»*

### Сброс при запуске приложения

Опорная температура **всегда сбрасывается до 20 °C** при запуске приложения. Это предотвращает тихое влияние устаревших настроек из предыдущей сессии измерений на сегодняшнюю работу. Маленькая курсивная заметка в Настройках напоминает об этом поведении.

Если вы хотите воспроизвести историческое измерение при его исходной температуре, просто коснитесь записи — температура восстановится автоматически.

### Материалы без компенсации

Большинство неметаллических материалов не имеют надёжных опубликованных температурных коэффициентов. Приложение показывает значок **«ref only»** для них — их указанная скорость используется независимо от настройки температуры. Если вам нужны точные измерения при не-комнатных температурах для этих материалов, выполните in-situ калибровку и сохраните результат как пользовательский материал.

---

## Аннотирование фото

После успешного вычисления коснитесь кнопки **📷 Аннотировать фото**, чтобы наложить маркеры датчиков и источника на фото вашей установки.

![Аннотация фото](../screenshots/08-photo-annotation.png)

### Процесс

1. Коснитесь **Аннотировать фото** — открывается системная камера
2. Сделайте фото размещения ваших датчиков
3. Приложение загружает фото в наложение аннотаций
4. Маркеры датчиков (A, B, C, D, E, F по необходимости — до 6 датчиков) и маркер источника автоматически размещаются на основе ваших вычислений
5. Перетащите любой маркер для тонкой настройки положения. При настройке положение источника пересчитывается из исправленных положений датчиков
6. Коснитесь **Сохранить** для сохранения или **Переснять** для повторной попытки

Аннотированное фото автоматически включается в PDF-отчёты.

---

## Отчёты

Коснитесь кнопки **Распечатать результат** на любом экране результатов для генерации форматированного отчёта.

![PDF-отчёт](../screenshots/09-pdf-report.png)

### Содержимое отчёта

- Заголовок (настраиваемый в Настройки → Заголовок отчёта)
- Название измерения и временная метка
- Все входные значения в аккуратной таблице
- Результат вычисления
- Текст заключения
- Визуализация (геометрический график)
- Аннотированное фото (если сделали)
- Строка нижнего колонтитула температуры (если компенсация была активна)
- Номер страницы и строка кредитов

### Формат вывода

- **Android**: нативная генерация PDF, сохранение на телефон или поделиться
- **iOS**: системное диалоговое окно печати → сохранить как PDF, AirPrint или поделиться

### Настройка заголовка

Настройки → Заголовок отчёта. Введите название вашей компании, лаборатории, информацию о проекте или что угодно, что хотите видеть вверху каждого отчёта.

---

## Резервное копирование и восстановление

Сохраните все ваши пользовательские материалы, избранное, настройки и историю в один файл. Перенос между устройствами.

### Резервное копирование

Настройки → **Резервное копирование** → коснитесь «Сохранить файл резервной копии». Приложение генерирует JSON-файл и открывает лист общего доступа вашего телефона. Сохраните его на ваш облачный диск (Google Drive, iCloud, OneDrive), отправьте себе по электронной почте или передайте любым удобным способом.

### Восстановление

Настройки → **Восстановление** → выберите файл резервной копии из хранилища вашего телефона. Приложение импортирует пользовательские материалы, избранное, историю и настройки.

⚠️ **Восстановление заменяет ваши текущие данные.** Если у вас есть важные измерения на текущем устройстве, сначала сделайте их резервную копию перед восстановлением из другой резервной копии.

---

## Настройки

Доступ через значок шестерёнки ⚙ в правом верхнем углу. Настройки — это модальное окно, не вкладка.

![Настройки](../screenshots/06-settings.png)

| Настройка | Что контролирует |
|---|---|
| **Обновить до Pro** | Купить или узнать о функциях Pro ($19,99) |
| **Язык** | Язык отображения приложения (30 поддерживается) |
| **Тема** | Светлая, Тёмная или Авто (следовать системе) |
| **Единица расстояния** | см или дюймы |
| **Опорная температура** | Активная температура для компенсации, от -40 до +200 °C |
| **Заголовок отчёта** | Пользовательский текст вверху сгенерированных отчётов |
| **Резервное копирование** | Экспортировать все данные в файл |
| **Восстановление** | Импортировать данные из файла резервной копии |
| **Восстановить покупку** | Повторно получить Pro на новом устройстве |

---

## Функции Pro

NVH Source Locator использует **freemium-модель с блокировкой функций**:

- **Бесплатно**: Вкладка 2-Sensor полностью функциональна без ограничений
- **Pro**: Все остальные вкладки имеют определённые поля ввода заблокированными. Paywall появляется, когда бесплатный пользователь касается заблокированного поля

### Что заблокировано

Поля, требующие Pro, разбросаны по:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Режимам 3D и 3D+
- Резервному копированию и Восстановлению
- PDF-отчётам
- Пользовательским материалам
- Аннотированию фото

Бесплатный пользователь может ОТКРЫТЬ любую вкладку и УВИДЕТЬ интерфейс. Он просто не может вводить значения в заблокированные Pro поля ввода.

![Заблокированное Pro-поле](../screenshots/11-pro-locked-field.png)

### Paywall

![Paywall](../screenshots/07-paywall.png)

Когда бесплатный пользователь касается заблокированного поля, paywall въезжает, показывая:
- Значок приложения с PRO-значком
- Список функций
- Кнопку разблокировки с ценой ($19,99 по умолчанию; может варьироваться по регионам)
- Активацию промо-кода (только Android — iOS использует отдельный процесс Offer Code от Apple)
- Опциональную промо-ссылку на каналы сообщества

### Покупка Pro

Коснитесь любого заблокированного поля или коснитесь **Обновить до Pro** в Настройках. Использует официальную платёжную систему вашей платформы (Google Play на Android, Apple App Store на iOS).

### Восстановление Pro на новом устройстве

Если вы купили на одном устройстве и хотите Pro на другом (тот же аккаунт):

1. Войдите в **тот же** аккаунт Google (Android) или Apple ID (iOS), который использовали для покупки
2. Откройте NVH Source Locator на новом устройстве
3. Перейдите в Настройки → **Восстановить покупку**
4. Приложение проверяет записи покупок платформы и разблокирует Pro

### Авто-восстановление при запуске

Если вы активируете промо-код в Google Play Store или App Store, пока NVH Source Locator работает в фоновом режиме, возврат в приложение автоматически обнаружит новую покупку и разблокирует Pro — ручное Восстановление не требуется.

### Активация промо-кода

**Android**: кнопка «Есть промо-код Google Play?» в paywall открывает процесс активации Google Play с предварительно заполненным кодом.

**iOS**: Политика App Store 3.1.1 требует активации через официальный процесс Apple «Активировать код». Кнопка Google Play скрыта в iOS. Вместо этого ищите «Активировать код App Store» в Настройках.

---

## Вкладка Help и учебные материалы

Вкладка **Help** включает учебные материалы в приложении, руководства по лучшим практикам и справочную информацию.

![Вкладка Help](../screenshots/10-help-tab.png)

Охватываемые темы:
- Какое оборудование вам нужно
- Как размещать датчики для наилучшей точности
- Советы по калибровке
- Распространённые измерительные сценарии
- Советы по триангуляции и 3D-размещению
- Маршрутизация кабелей и качество сигнала

---

## Устранение неполадок

### Результат вычисления неверный или не имеет смысла

1. Проверьте калибровку. Автозаполненное `tCal` предполагает опубликованную скорость материала — реальные материалы варьируются. Наиболее точная калибровка — in-situ: коснитесь известного места и позвольте приложению вывести фактическую скорость.
2. Проверьте настройку **Первый датчик** — какой датчик услышал событие первым, имеет значение для математики.
3. Проверьте свои измерения расстояния. Ошибки в несколько мм распространяются.

### Toast говорит «Результат вне диапазона»

Математика говорит, что источник не находится между вашими датчиками. Возможные причины:
- Источник действительно находится за линией/плоскостью датчиков
- Один из ваших входов неверен
- Скорость калибровки слишком далека от реальности

### Подсказка вычисляемой скорости показывает предупреждающий цвет

Подразумеваемая скорость звука из ваших входов далека от любого распространённого материала (менее 50 м/с или более 20 000 м/с). Проверьте свои входы — вероятно, опечатка в tCal или расстоянии.

### Селектор Materials показывает другие скорости, чем ожидалось

Проверьте Опорную температуру в Настройках. Если не 20 °C, отображаемые скорости отражают температурную компенсацию. Приложение показывает «ref X @ 20°C» под компенсированными скоростями, чтобы вы могли проверить.

### Запись истории воспроизводится с другим результатом

Старые записи истории, созданные до версии приложения 1.75, могут не сохранить температуру. Если вы делали измерение при температуре, отличной от 20 °C, воспроизведение будет использовать текущую настройку. Вручную установите температуру в Настройках перед воспроизведением, ИЛИ перемерьте.

### Маркеры аннотации фото не там, где я ожидаю

Маркеры автоматически размещаются на основе входной геометрии. Перетащите их для регулировки. Регулировка маркеров обновляет положение источника в наложении фото — но НЕ изменяет основной результат вычисления.

### Сбой Резервного копирования/Восстановления

Убедитесь, что используете файл резервной копии, сгенерированный той же или более новой версией приложения. Старые файлы резервных копий могут не иметь текущих полей данных.

### Восстановить покупку говорит «покупка не найдена»

1. Проверьте, что вы вошли в тот же магазин-аккаунт, который использовали для покупки
2. Проверьте, что покупка не была возвращена или не истекла
3. Попробуйте удалить и переустановить приложение (покупка привязана к вашему магазин-аккаунту, а не к установке приложения)
4. Свяжитесь с support@evdiag.net, если проблема не устраняется

### Числовой ввод неожиданно сбрасывается на 0

По дизайну: когда вы покидаете числовое поле (касаетесь в другом месте), если оно пустое, отрицательное или содержит нечисловой текст, оно сбрасывается на 0. Предотвращает тихо сломанные вычисления из случайно очищенных входов. Ввод температуры исключён (вместо этого он ограничивается -40/+200).

### Нужна дополнительная помощь

Свяжитесь с `support@evdiag.net`, указав:
- Модель устройства и версию ОС
- Версию приложения (Настройки → внизу страницы)
- Описание того, что вы пытались сделать
- Скриншоты, если возможно

---

*NVH Source Locator разработан EVDiag. Посетите https://evdiag.net для обновлений и ресурсов.*
""",

'zh': """# NVH Source Locator — 用户指南

NVH Source Locator 是一款测量工具，使用 TDOA（Time Difference of Arrival，到达时间差）从示波器或测量系统捕获的加速度计信号定位噪声和振动源。

本指南涵盖所有功能。如需快速复习，请参阅 `quick-reference.md`。

> **截图说明**：本文档使用应用程序的占位符截图。请在您捕获实际设备截图时，将每个 `../screenshots/*.png` 替换为真实截图。

---

## 目录

1. [工作原理](#how-it-works)
2. [开始之前](#before-you-start)
3. [主要选项卡](#the-main-tabs)
4. [2-Sensor 模式](#2-sensor-mode)
5. [3-Sensor 模式](#3-sensor-mode)
6. [Pro+ 模式 (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [Materials 选项卡](#the-materials-tab)
8. [温度补偿](#temperature-compensation)
9. [照片注释](#photo-annotation)
10. [报告](#reports)
11. [备份和恢复](#backup-and-restore)
12. [设置](#settings)
13. [Pro 功能](#pro-features)
14. [Help 选项卡和教程](#help-tab-and-tutorials)
15. [疑难解答](#troubleshooting)

---

## 工作原理

当噪声源发出声音或振动时，波以已知速度在材料中传播。如果您在材料上放置两个或更多加速度计并测量波到达每个加速度计的时间，时间差就会告诉您源在哪里。

NVH Source Locator 采集：

- **校准**：传感器之间的距离，以及波传播该距离所需的时间（用于计算材料的声速）
- **事件**：检测到噪声/振动事件的传感器之间的时间差

然后它计算源在结构中的位置。

您使用的传感器越多，就越能精确地定位源：

- **2 个传感器** → 沿一条线的距离
- **3 个传感器** → 在 2D 表面上的位置 (X, Y)
- **4 个传感器** → 在 3D 空间中的位置 (X, Y, Z)

---

## 开始之前

您需要：

- **一台示波器或测量系统**，能够以微秒 (µs) 为单位显示加速度计通道之间的时间差
- **至少 2 个加速度计**，物理连接到结构上（更多传感器 = 更高精度）
- **一种测量传感器间距离的方法**（卷尺、卡尺）
- **一种在已知位置触发波的方法** 用于校准（校准锤击、螺丝刀敲击或其他已知信号）

![带 2-Sensor 选项卡的主屏幕](../screenshots/01-home-2sensor.png)

---

## 主要选项卡

应用程序顶部有选项卡：

![选项卡栏](../screenshots/02-tab-bar.png)

| 选项卡 | 功能 | 何时使用 |
|---|---|---|
| **2-Sensor** | 沿 2 个传感器之间一条线的 1D 源定位 | 快速检查，梁状结构。**完全免费。** |
| **3-Sensor** | 使用三角形中的 3 个传感器进行 2D 源定位 | 最常见用途，面板和表面 |
| **3-Sen+** | 带超定最小二乘求解器的 3-Sensor | 更严格的测量，抗噪声 |
| **4-Sensor** | 使用两对 (A-B + C-D) 进行 2D 定位 | 矩形传感器布局，交叉检查 |
| **4-Sen+** | 高级 2D 模式，4 个传感器在任何位置 | 非矩形几何，完整 LSQ |
| **3D** | 使用具有 XYZ 坐标的 4 个传感器进行 3D 源定位 | 3D 空间中的复杂结构 |
| **3D+** | 最多 6 个传感器的 3D，超定 LSQ | 非常复杂的几何，最大精度 |
| **Materials** | 声速库 + 自定义材料 | 每次测量会话选择一次 |
| **Help** | 应用内教程和参考 | 当您需要快速复习时 |

> **免费 vs Pro**：2-Sensor 选项卡完全免费。其他选项卡可访问但有特定输入字段对 Pro 用户锁定（用金色挂锁徽章标记）。点击锁定字段会显示 Pro 付费墙。

设置可通过右上角的 ⚙ 齿轮图标访问（不是选项卡）。

---

## 2-Sensor 模式

最简单的测量：沿两个加速度计之间一条线的源定位。

![2-Sensor 选项卡](../screenshots/01-home-2sensor.png)

### 步骤 1：应用材料

点击 Materials 选项卡。选择您的结构所用材料（例如，"铝"，"钢，Mild (1020)"）。应用程序使用材料的已知声速自动填充校准时间字段。

如果您的结构材料不在列表中，可以暂时选择"空气"，然后在步骤 2 手动覆盖校准时间。

### 步骤 2：输入校准数据

在 2-Sensor 选项卡上，您将看到两个对部分：**对 A–B** 和 **对 A–C**（如果您只有 2 个传感器，仅需 A–B）。

对于每一对，您填写：

- **传感器间距** (`d`)：传感器之间的物理距离，以厘米或英寸为单位（在设置中设定）
- **校准时间延迟** (`tCal`)：波以材料声速在传感器之间传播的时间 — 当您选择材料时自动填充，但您可以覆盖

### 步骤 3：输入事件时间

- **事件时间延迟** (`tEvent`)：检测到噪声事件的传感器之间的时间差，以微秒为单位
- **首先检测的传感器**：哪个传感器首先听到事件（A 或 B）

### 步骤 4：读取结果

应用程序将源位置显示为与传感器 A 的距离：
- 结果 = 0：源位于传感器 A
- 结果 = 距离：源位于传感器 B
- 结果在中间：源位于两者之间
- 结果在外部：源超出传感器之一（toast 将警告）

结果卡显示两个距离（来自 A，来自 B）并指示哪个传感器更近。

### 步骤 5（可选）：注释照片

点击 **📷 注释照片** 拍摄您的设置照片。应用程序为传感器 A、B 和源叠加标记。对报告有用。

---

## 3-Sensor 模式

使用排列成三角形的三个传感器在 2D 平面上定位源。

![3-Sensor 选项卡](../screenshots/03-3sensor-tab.png)

### 设置

在您的结构上放置三个传感器形成三角形。等边、直角或不等边 — 应用程序处理所有几何。

### 输入数据

在 **三角形边长** 部分，输入所有三条边的物理距离 (A–B, A–C, B–C)。

对于每一对（A–B 和 A–C），输入：
- **tCal**：校准时间（从材料自动填充）
- **tEvent**：测量的噪声事件时间差
- **首先检测的传感器**：哪个先听到

### 读取结果

应用程序将源位置显示为相对于传感器 A 的 X, Y 坐标（传感器 A 在原点，传感器 B 在 X 轴上）。可视化显示所有三个传感器和源位置。

![三角形结果](../screenshots/04-triangle-result.png)

---

## Pro+ 模式

几个高级选项卡提供超定求解器和更高维度：

### 3-Sen+ (Pro)

与 3-Sensor 相同的三角形设置，但校准和测量所有三对 (A–B, A–C, B–C)。求解器在最小二乘拟合中使用所有 3 个 TDOA — 对测量噪声和各向异性材料更稳健。报告每对的残差，以便您可以发现不一致的测量。

### 4-Sensor

在区域周围放置四个传感器：
- **A–B** = 水平对（左/右边）
- **C–D** = 垂直对（上/下边）

首先运行 A–B 对（水平），然后运行 C–D 对（垂直）。2D 地图显示交点。每对单独校准 — 当材料在结构上变化时有用。

### 4-Sen+ (高级 2D)

四个传感器在任何位置（不强制矩形）。将 A 与 B、C、D 中的每一个配对并单独校准。超定最小二乘求解器平均每对的测量噪声并报告每对的残差。

### 3D

使用放置在 3D 空间中的 4 个传感器进行完整 3D 测量。输入每个传感器的 (X, Y, Z) 坐标，以及每对 (A–B, A–C, A–D) 的校准和事件时间。

### 3D+ (Pro)

类似 3D，但支持最多 **6 个传感器**（A 到 F）和超定 LSQ。复杂 3D 几何的最大精度。

---

## Materials 选项卡

20 °C 下已知声速的常见工程材料库。

![Materials 选项卡](../screenshots/05-materials-tab.png)

### 材料列表

列表包括空气、流体、橡胶、聚合物、木材、玻璃和金属。速度范围从约 340 m/s（空气）到约 13,000 m/s（一些金属在室温下）。

### 内置材料带温度补偿

14 种常用金属包含温度系数数据。当设置中的参考温度与 20 °C 不同时，应用程序会自动调整这些材料的速度：

- 铝
- 钢，Mild (1020)
- 不锈钢 (304)
- 铁 (铸造)
- 铁
- 铜
- 黄铜
- 青铜
- 钛
- 镁
- 铅
- 锌
- 镍
- 钨

带补偿的材料在选择器中显示两个值：**补偿后速度**（大，突出）和**20 °C 下的参考速度**（小，下方灰色）。

不带补偿的材料显示斜体的 **"ref only"** — 它们列出的速度按原样使用，不受温度影响。

### 自定义材料

如果您在 2-Sensor 选项卡上测量校准，您可以将结果保存为自定义材料。在 2-sensor 测量成功后，寻找以您选择的名称保存导出速度的选项。

自定义材料存储就地测量速度；它们从不应用温度补偿（速度已在测试温度下测量）。

### 收藏夹

点击任何材料旁边的星标将其标记为收藏。收藏夹出现在列表顶部以便快速访问。

### 搜索

使用顶部的搜索栏按名称过滤材料。搜索匹配英语规范名称和翻译显示名称。

---

## 温度补偿

材料中的声速随温度变化。在汽车 NVH 测试中这很重要：80 °C 的发动机舱、-10 °C 的冷浸舱或 200 °C 的排气歧管区域都与室温实验室条件不同。

### 设置温度

打开设置（⚙ 图标）→ 参考温度。以 °C 输入您的测试环境温度（范围 -40 至 +200）。

![设置面板](../screenshots/06-settings.png)

### 当温度 ≠ 20 °C 时会发生什么

- 校准时间字段自动填充温度调整后的速度
- Materials 选择器突出显示调整后的速度
- toast 确认：*"铝已应用 (6,284 m/s @ 60 °C) — 已更新 N 对"*
- "最接近材料"提示与温度调整后的速度进行比较
- 保存的历史条目记录活动温度
- 报告包括页脚行：*"参考温度：60 °C，已应用补偿"*

### 应用启动时重置

当您启动应用程序时，参考温度**始终重置为 20 °C**。这可以防止过去测量会话的过时设置无声地影响今天的工作。设置中的小斜体注释提醒您此行为。

如果您想以其原始温度重放历史测量，只需点击该条目 — 温度会自动恢复。

### 无补偿的材料

大多数非金属材料没有可靠的已发布温度系数。应用程序对这些显示 **"ref only"** 徽章 — 它们列出的速度无论温度设置如何都使用。如果您需要在非室温下对这些材料进行精确测量，请进行就地校准并将结果保存为自定义材料。

---

## 照片注释

成功计算后，点击 **📷 注释照片** 按钮以在您设置的照片上叠加传感器和源标记。

![照片注释](../screenshots/08-photo-annotation.png)

### 流程

1. 点击 **注释照片** — 系统相机打开
2. 拍摄传感器位置的照片
3. 应用程序将照片加载到注释叠加层中
4. 传感器标记（A、B、C、D、E、F 视情况而定 — 最多 6 个传感器）和源标记根据您的计算自动放置
5. 拖动任何标记以微调位置。当您调整时，源位置会从校正的传感器位置重新计算
6. 点击 **保存** 以保留，或 **重拍** 以重试

注释的照片会自动包含在 PDF 报告中。

---

## 报告

点击任何结果屏幕上的 **打印结果** 按钮以生成格式化报告。

![PDF 报告](../screenshots/09-pdf-report.png)

### 报告内容

- 标题（在设置 → 报告标题中可自定义）
- 测量标题和时间戳
- 所有输入值在整洁的表格中
- 计算结果
- 结论文本
- 可视化（几何图）
- 注释照片（如果您拍摄了一张）
- 温度页脚行（如果补偿处于活动状态）
- 页码和版权行

### 输出格式

- **Android**：原生 PDF 生成，保存到您的手机或分享
- **iOS**：系统打印对话框 → 保存为 PDF、AirPrint 或分享

### 自定义标题

设置 → 报告标题。输入您的公司名称、实验室名称、项目信息或您希望在每个报告顶部的任何内容。

---

## 备份和恢复

将您所有的自定义材料、收藏夹、设置和历史保存到单个文件中。在设备之间传输。

### 备份

设置 → **备份** → 点击"保存备份文件"。应用程序生成 JSON 文件并打开您手机的共享表。将其保存到您的云驱动器（Google Drive、iCloud、OneDrive）、通过电子邮件发送给自己或以任何您喜欢的方式传输。

### 恢复

设置 → **恢复** → 从您手机的存储中选择备份文件。应用程序导入自定义材料、收藏夹、历史和设置。

⚠️ **恢复替换您当前的数据。** 如果您在当前设备上有重要测量，请在从不同备份恢复之前先备份它们。

---

## 设置

通过右上角的 ⚙ 齿轮图标访问。设置是一个模态，不是选项卡。

![设置](../screenshots/06-settings.png)

| 设置 | 控制什么 |
|---|---|
| **升级到 Pro** | 购买或了解 Pro 功能 ($19.99) |
| **语言** | 应用显示语言（支持 30 种） |
| **主题** | 浅色、深色或自动（跟随系统） |
| **距离单位** | 厘米或英寸 |
| **参考温度** | 补偿的活动温度，-40 至 +200 °C |
| **报告标题** | 生成报告顶部的自定义文本 |
| **备份** | 将所有数据导出到文件 |
| **恢复** | 从备份文件导入数据 |
| **恢复购买** | 在新设备上重新获取 Pro |

---

## Pro 功能

NVH Source Locator 使用**按功能锁定的免费增值模式**：

- **免费**：2-Sensor 选项卡完全功能正常，没有限制
- **Pro**：所有其他选项卡都有特定输入字段被锁定。当免费用户点击锁定字段时，付费墙会出现

### 锁定的内容

需要 Pro 的字段分散在：
- 3-Sensor、3-Sen+、4-Sensor、4-Sen+
- 3D 和 3D+ 模式
- 备份和恢复
- PDF 报告
- 自定义材料
- 照片注释

免费用户可以打开任何选项卡并查看界面。他们只是不能在 Pro 锁定的输入字段中输入值。

![Pro 锁定字段](../screenshots/11-pro-locked-field.png)

### 付费墙

![付费墙](../screenshots/07-paywall.png)

当免费用户点击锁定字段时，付费墙滑入显示：
- 带 PRO 徽章的应用图标
- 功能列表
- 带价格的解锁按钮（默认 $19.99；可能因地区而异）
- 促销码兑换（仅限 Android — iOS 使用 Apple 的单独 Offer Code 流程）
- 可选的社区频道促销链接

### 购买 Pro

点击任何锁定字段，或在设置中点击 **升级到 Pro**。使用您平台的官方支付系统（Android 上为 Google Play，iOS 上为 Apple App Store）。

### 在新设备上恢复 Pro

如果您在一台设备上购买并想要在另一台设备上获得 Pro（相同帐户）：

1. 使用您用于购买的**相同** Google 帐户 (Android) 或 Apple ID (iOS) 登录
2. 在新设备上打开 NVH Source Locator
3. 转到设置 → **恢复购买**
4. 应用程序与平台的购买记录进行验证并解锁 Pro

### 启动时自动恢复

如果您在 NVH Source Locator 在后台运行时在 Google Play Store 或 App Store 中兑换促销码，返回应用程序会自动检测到新购买并解锁 Pro — 无需手动恢复。

### 促销码兑换

**Android**：付费墙中"有 Google Play 促销码？"按钮打开 Google Play 兑换流程，您的代码已预填充。

**iOS**：App Store 政策 3.1.1 要求通过 Apple 的官方"兑换代码"流程进行兑换。Google Play 按钮在 iOS 上隐藏。请改为在设置中查找"兑换 App Store 代码"。

---

## Help 选项卡和教程

**Help** 选项卡包括应用内教程、最佳实践指南和参考信息。

![Help 选项卡](../screenshots/10-help-tab.png)

涵盖的主题：
- 您需要什么设备
- 如何放置传感器以获得最佳精度
- 校准提示
- 常见测量场景
- 三角测量和 3D 放置提示
- 电缆布线和信号质量

---

## 疑难解答

### 计算结果不正确或没有意义

1. 检查您的校准。自动填充的 `tCal` 假定已发布的材料速度 — 实际材料各异。最准确的校准是就地的：点击已知位置，让应用程序导出实际速度。
2. 检查 **首先检测的传感器** 设置 — 哪个传感器首先听到事件对数学很重要。
3. 验证您的距离测量。几毫米的误差会传播。

### Toast 说"结果超出范围"

数学表明源不在您的传感器之间。可能的原因：
- 源实际上在传感器线/平面之外
- 您的一个输入是错误的
- 校准速度与现实相差太远

### 计算速度提示显示警告颜色

从您的输入隐含的声速与任何常见材料相差很远（小于 50 m/s 或大于 20,000 m/s）。检查您的输入 — 很可能是 tCal 或距离中的拼写错误。

### Materials 选择器显示与预期不同的速度

检查设置中的参考温度。如果不是 20 °C，显示的速度反映温度补偿。应用程序在补偿速度下方显示"ref X @ 20°C"，以便您可以验证。

### 历史条目重放时结果不同

应用版本 1.75 之前创建的旧历史条目可能未存储温度。如果您在非 20 °C 温度下进行测量，重放将使用当前设置。在重放前手动在设置中设定温度，或重新测量。

### 照片注释标记不在我预期的位置

标记根据输入几何自动放置。拖动它们以调整。调整标记会更新照片叠加中的源位置 — 但不会更改基础计算结果。

### 备份/恢复失败

确保您使用相同或更新版本的应用程序生成的备份文件。较旧的备份文件可能缺少当前数据字段。

### 恢复购买说"未找到购买"

1. 验证您已登录到用于购买的相同商店帐户
2. 验证购买未被退款或过期
3. 尝试卸载并重新安装应用程序（购买与您的商店帐户绑定，而不是与应用程序安装绑定）
4. 如果问题仍然存在，请联系 support@evdiag.net

### 数字输入意外跳到 0

按设计：当您退出数字字段（在其他地方点击）时，如果它为空、负数或包含非数字文本，它会跳到 0。防止从意外清除的输入产生静默损坏的计算。温度输入是例外（它改为限制在 -40/+200）。

### 需要更多帮助

通过以下方式联系 `support@evdiag.net`：
- 您的设备型号和操作系统版本
- 应用版本（设置 → 页面底部）
- 您尝试的描述
- 如果可能，截图

---

*NVH Source Locator 由 EVDiag 开发。访问 https://evdiag.net 获取更新和资源。*
""",

}
