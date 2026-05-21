# NVH Source Locator — Quick Reference

A one-page refresher. For full details, see **User Guide**.

---

## Core flow (2-Sensor, free)

1. **Pick a material** — Materials tab → tap your material
2. **Enter calibration** on the 2-Sensor tab:
   - Sensor spacing (`d`)
   - Calibration time delay (`tCal`) — auto-filled from material
3. **Enter event** — `tEvent` and First sensor (A or B)
4. **Read result** — distance from sensor A

![2-Sensor tab](../screenshots/01-home-2sensor.png)

---

## All tabs

| Tab | Output | Pro fields? |
|---|---|---|
| 2-Sensor | Distance along line | No (fully free) |
| 3-Sensor | X, Y on a surface | Yes |
| 3-Sen+ | X, Y with LSQ over 3 pairs | Yes |
| 4-Sensor | X, Y from two pairs (A–B + C–D) | Yes |
| 4-Sen+ | X, Y from 4 sensors, any position | Yes |
| 3D | X, Y, Z from 4 sensors | Yes |
| 3D+ | X, Y, Z from up to 6 sensors | Yes |
| Materials | Speed-of-sound picker | No |
| Help | Tutorials | No |

Settings is the ⚙ icon (top-right), not a tab.

---

## Temperature compensation

Settings → Reference temperature, range **-40 to +200 °C**.

- **14 metals** have built-in compensation (aluminium, steels, copper, brass, bronze, titanium, magnesium, lead, zinc, nickel, tungsten, iron, iron cast)
- Materials without compensation show **"ref only"**
- **Resets to 20 °C on every app launch** (default-safe-start)
- Replaying a history entry restores its original temperature

---

## Shortcuts

- **Tap a material** → auto-fills all `tCal` fields across all tabs
- **Hold +/-** on number fields → fast increment
- **Drag horizontally** on a number field → scrub values
- **Empty/negative/garbage input** → snaps to 0 on blur (temp input clamps to -40/200)
- **Star a material** → moves to top of picker

---

## Pro model

**Feature-locked freemium** ($19.99):
- Free: 2-Sensor tab fully functional, no limits
- Pro: Other tabs accessible but have **gold-padlock fields** that show paywall on tap

Pro unlocks: 3-Sensor through 3D+, custom materials, backup/restore, PDF reports, photo annotation.

![Paywall](../screenshots/07-paywall.png)

---

## Reports & Backup

**Print result** button on any result screen → PDF with header, inputs, result, visualization, photo (if taken), and temperature footer (when compensation active).

Customize header in Settings → Report header.

**Backup**: Settings → Backup → share to cloud/email.  
**Restore**: Settings → Restore → pick backup file.

---

## Restore Pro on a new device

Same Google account (Android) or Apple ID (iOS) you bought with → Settings → **Restore purchase** → unlocks within seconds.

Auto-restore happens silently when you return to the app after redeeming a promo code externally.

---

## Quick troubleshooting

- **Result outside range?** Check `tEvent` sign / First sensor / sensor spacing
- **Closest material wrong?** Reference temperature probably accidentally set — check Settings
- **Restore purchase fails?** Verify same store account; reinstall if it persists
- **Field snapped to 0?** Empty/negative inputs auto-snap on blur — re-enter the value
- **Stepper buttons gone?** They appear next to fields with `data-step` — restart app if missing
- **Stale temperature warning?** It resets to 20 every launch — set again for this session

---

Contact `support@evdiag.net` — include device model, app version (Settings → bottom), and a description of what you tried.
