# NVH Source Locator — Guia do Usuário

NVH Source Locator é uma ferramenta de medição para localizar fontes de ruído e vibração usando TDOA (Time Difference of Arrival) a partir de sinais de acelerômetros capturados em um osciloscópio ou sistema de medição.

Este guia cobre todos os recursos. Para uma revisão rápida, consulte `quick-reference.md`.

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
