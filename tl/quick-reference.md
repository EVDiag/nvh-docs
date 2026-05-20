# NVH Source Locator — Mabilis na Sanggunian

Isang-pahinang paalala. Para sa kumpletong detalye, tingnan ang `user-guide.md`.

---

## Pangunahing daloy (2-Sensor, libre)

1. **Pumili ng materyal** — tab na Materials → i-tap ang inyong materyal
2. **Ilagay ang calibration** sa tab na 2-Sensor:
   - Pagitan ng sensor (`d`)
   - Pagkaantala ng calibration time (`tCal`) — auto-fill mula sa materyal
3. **Ilagay ang event** — `tEvent` at Unang sensor (A o B)
4. **Basahin ang resulta** — distansya mula sa sensor A

![Tab na 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Lahat ng tab

| Tab | Output | Mga Pro field? |
|---|---|---|
| 2-Sensor | Distansya sa kahabaan ng linya | Hindi (ganap na libre) |
| 3-Sensor | X, Y sa isang ibabaw | Oo |
| 3-Sen+ | X, Y na may LSQ sa 3 pares | Oo |
| 4-Sensor | X, Y mula sa dalawang pares (A–B + C–D) | Oo |
| 4-Sen+ | X, Y mula sa 4 na sensor, anumang posisyon | Oo |
| 3D | X, Y, Z mula sa 4 na sensor | Oo |
| 3D+ | X, Y, Z mula sa hanggang 6 na sensor | Oo |
| Materials | Pumipili ng bilis ng tunog | Hindi |
| Help | Mga tutorial | Hindi |

Ang Settings ay icon na ⚙ (kanang itaas), hindi tab.

---

## Pagbabayad sa temperatura

Settings → Reference temperature, saklaw na **-40 hanggang +200 °C**.

- **14 na metal** ay may built-in na compensation (aluminyo, mga acero, tanso, brass, bronze, titanium, magnesium, tingga, sink, nikel, tungsten, bakal, bakal na hinulma)
- Ang mga materyal na walang compensation ay nagpapakita ng **"ref only"**
- **Nare-reset sa 20 °C sa bawat paglulunsad ng app** (default-ligtas-simula)
- Ang pag-replay sa entry sa history ay nagbabalik sa orihinal na temperatura nito

---

## Mga shortcut

- **I-tap ang isang materyal** → auto-fill ang lahat ng `tCal` field sa lahat ng tab
- **Pindutin nang matagal ang +/-** sa mga number field → mabilis na pagdaragdag
- **I-drag nang pahalang** sa isang number field → i-scrub ang mga value
- **Walang laman/negatibo/basurang input** → magiging 0 kapag nawala ang focus (ang temperature input ay limitado sa -40/200)
- **Star-han ang materyal** → mapupunta sa itaas ng picker

---

## Modelong Pro

**Naka-lock-ng-feature na freemium** ($19.99):
- Libre: ang tab na 2-Sensor ay ganap na gumagana, walang limitasyon
- Pro: ang iba pang mga tab ay naa-access ngunit may mga **gintong padlock na field** na nagpapakita ng paywall kapag na-tap

Binubuksan ng Pro: 3-Sensor hanggang 3D+, mga custom na materyal, backup/restore, mga ulat ng PDF, anotasyon ng larawan.

![Paywall](../screenshots/07-paywall.png)

---

## Mga ulat at Backup

Ang **Print result** button sa anumang screen ng resulta → PDF na may header, mga input, resulta, visualization, larawan (kung kinunan), at footer ng temperatura (kapag aktibo ang compensation).

I-customize ang header sa Settings → Report header.

**Backup**: Settings → Backup → ibahagi sa cloud/email.  
**Restore**: Settings → Restore → piliin ang backup file.

---

## Ibalik ang Pro sa bagong device

Parehong Google account (Android) o Apple ID (iOS) na binili mo → Settings → **Restore purchase** → magbubukas sa loob ng ilang segundo.

Ang auto-restore ay nangyayari nang tahimik kapag bumalik ka sa app pagkatapos mag-redeem ng promo code sa labas.

---

## Mabilis na pag-troubleshoot

- **Resulta sa labas ng saklaw?** Suriin ang sign ng `tEvent` / Unang sensor / pagitan ng sensor
- **Mali ang pinakamalapit na materyal?** Marahil ay aksidenteng naitakda ang reference temperature — suriin ang Settings
- **Nabigo ang Restore purchase?** I-verify ang parehong store account; i-reinstall kung nagpapatuloy
- **Naging 0 ang field?** Walang laman/negatibong input ay auto-snap kapag nawala ang focus — ilagay muli ang value
- **Nawawala ang mga stepper button?** Lalabas sila sa tabi ng mga field na may `data-step` — i-restart ang app kung nawawala
- **Babala sa lumang temperatura?** Nare-reset sa 20 sa bawat paglulunsad — itakda muli para sa session na ito

---

Makipag-ugnayan sa `support@evdiag.net` — isama ang modelo ng device, bersyon ng app (Settings → ibaba), at paglalarawan ng kung ano ang sinubukan mo.
