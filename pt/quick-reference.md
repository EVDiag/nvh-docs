# NVH Source Locator — Referência Rápida

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
