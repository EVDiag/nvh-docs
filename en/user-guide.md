# NVH Source Locator — User Guide

NVH Source Locator is a measurement tool for locating noise and vibration sources using TDOA (Time Difference of Arrival) from accelerometer signals captured on an oscilloscope or measurement system.

This guide covers all features. For a quick refresher, see `quick-reference.md`.

> **Note on screenshots**: This document uses placeholder screenshots from the app. Replace each `../screenshots/*.png` with real device screenshots as you capture them.

---

## Table of Contents

1. [How it works](#how-it-works)
2. [Before you start](#before-you-start)
3. [The main tabs](#the-main-tabs)
4. [2-Sensor mode](#2-sensor-mode)
5. [3-Sensor mode](#3-sensor-mode)
6. [Pro+ modes (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [The Materials tab](#the-materials-tab)
8. [Temperature compensation](#temperature-compensation)
9. [Photo annotation](#photo-annotation)
10. [Reports](#reports)
11. [Backup and restore](#backup-and-restore)
12. [Settings](#settings)
13. [Pro features](#pro-features)
14. [Help tab and tutorials](#help-tab-and-tutorials)
15. [Troubleshooting](#troubleshooting)

---

## How it works

When a noise source emits a sound or vibration, the wave travels through a material at a known speed. If you place two or more accelerometers on the material and measure when the wave arrives at each one, the time difference tells you where the source is.

NVH Source Locator takes:

- **Calibration**: the distance between sensors, and the time it takes a wave to travel that distance (used to compute the material's sound speed)
- **Event**: the time difference between sensors detecting the noise/vibration event

Then it calculates where on the structure the source is located.

The more sensors you use, the more accurately you can pin down the source:

- **2 sensors** → distance along a line
- **3 sensors** → position on a 2D surface (X, Y)
- **4 sensors** → position in 3D space (X, Y, Z)

---

## Before you start

You'll need:

- **An oscilloscope or measurement system** that can show you the time difference between accelerometer channels in microseconds (µs)
- **At least 2 accelerometers** physically attached to the structure (more sensors = higher accuracy)
- **A way to measure distance** between sensors (tape measure, calipers)
- **A way to trigger a wave** at a known location for calibration (calibrated hammer impact, screwdriver tap, or other known signal)

![Home screen with 2-Sensor tab](../screenshots/01-home-2sensor.png)

---

## The main tabs

The app has tabs along the top:

![Tab bar](../screenshots/02-tab-bar.png)

| Tab | What it does | When to use |
|---|---|---|
| **2-Sensor** | 1D source location along a line between 2 sensors | Quick checks, beam-like structures. **Fully free.** |
| **3-Sensor** | 2D source location using 3 sensors in a triangle | Most general use, panels and surfaces |
| **3-Sen+** | 3-Sensor with over-determined least-squares solver | More demanding measurements, noise-robust |
| **4-Sensor** | 2D location using two pairs (A-B + C-D) | Rectangular sensor layouts, cross-checking |
| **4-Sen+** | Advanced 2D mode, 4 sensors at any positions | Non-rectangular geometries, full LSQ |
| **3D** | 3D source location using 4 sensors with XYZ coords | Complex structures in 3D space |
| **3D+** | 3D with up to 6 sensors, over-determined LSQ | Very complex geometries, maximum precision |
| **Materials** | Speed-of-sound library + custom materials | Pick once per measurement session |
| **Help** | In-app tutorials and reference | When you need a quick refresher |

> **Free vs Pro**: The 2-Sensor tab is fully free. Other tabs are accessible but have specific input fields locked to Pro users (marked with a gold padlock badge). Tapping a locked field shows the Pro paywall.

Settings is accessed via the ⚙ gear icon in the top-right corner (not a tab).

---

## 2-Sensor mode

The simplest measurement: source location along a line between two accelerometers.

![2-Sensor tab](../screenshots/01-home-2sensor.png)

### Step 1: Apply a material

Tap the Materials tab. Pick the material your structure is made from (e.g., "Aluminium", "Steel, Mild (1020)"). The app uses the material's known speed of sound to populate the calibration time field automatically.

If your structure's material isn't in the list, you can pick "Air" temporarily and override the calibration time manually in step 2.

### Step 2: Enter calibration data

On the 2-Sensor tab, you'll see two pair sections: **Pair A–B** and **Pair A–C** (only A–B is required if you only have 2 sensors).

For each pair you fill in:

- **Sensor spacing** (`d`): physical distance between sensors, in cm or inches (set in Settings)
- **Calibration time delay** (`tCal`): time for a wave to travel between the sensors at the material's speed of sound — auto-filled when you pick a material, but you can override

### Step 3: Enter the event time

- **Event time delay** (`tEvent`): time difference between sensors detecting the noise event, in microseconds
- **First sensor**: which sensor heard the event first (A or B)

### Step 4: Read the result

The app shows the source position as a distance from sensor A:
- Result = 0: source is at sensor A
- Result = distance: source is at sensor B  
- Result between: source is between them
- Result outside: source is beyond one of the sensors (toast will warn)

The result card shows both distances (from A, from B) and indicates which sensor is closer.

### Step 5 (optional): Annotate a photo

Tap **📷 Annotate photo** to take a photo of your setup. The app overlays markers for sensors A, B and the source. Useful for reports.

---

## 3-Sensor mode

Locates a source on a 2D plane using three sensors arranged in a triangle.

![3-Sensor tab](../screenshots/03-3sensor-tab.png)

### Setup

Place three sensors on your structure forming a triangle. Equilateral, right-angle, or scalene — the app handles all geometries.

### Enter the data

In the **Triangle side lengths** section, enter the physical distance for all three sides (A–B, A–C, B–C).

For each pair (A–B and A–C), enter:
- **tCal**: calibration time (auto-fills from material)
- **tEvent**: measured time difference for the noise event
- **First sensor**: which heard it first

### Read the result

The app shows the source position as X, Y coordinates relative to sensor A (sensor A at origin, sensor B on the X-axis). The visualization shows all three sensors and the source location.

![Triangle result](../screenshots/04-triangle-result.png)

---

## Pro+ modes

Several advanced tabs offer over-determined solvers and higher dimensionality:

### 3-Sen+ (Pro)

Same triangle setup as 3-Sensor, but calibrate AND measure all three pairs (A–B, A–C, B–C). The solver uses all 3 TDOAs in a least-squares fit — more robust to measurement noise and anisotropic materials. Per-pair residuals are reported so you can spot inconsistent measurements.

### 4-Sensor

Place four sensors around the area:
- **A–B** = horizontal pair (left/right sides)
- **C–D** = vertical pair (top/bottom sides)

Run the A–B pair first (horizontal), then C–D pair (vertical). The 2D map shows the intersection. Each pair is calibrated separately — useful when material varies across the structure.

### 4-Sen+ (Advanced 2D)

Four sensors at any positions (not forced rectangular). Pair A with each of B, C, D and calibrate separately. Over-determined least-squares solver averages out per-pair measurement noise and reports per-pair residuals.

### 3D

Full 3D measurement with 4 sensors placed in 3D space. Enter each sensor's (X, Y, Z) coordinates, plus calibration and event times for each pair (A–B, A–C, A–D).

### 3D+ (Pro)

Like 3D but supports up to **6 sensors** (A through F) with over-determined LSQ. Maximum precision for complex 3D geometries.

---

## The Materials tab

Library of common engineering materials with known speed of sound at 20 °C.

![Materials tab](../screenshots/05-materials-tab.png)

### Material list

The list includes air, fluids, rubbers, polymers, woods, glasses, and metals. Speeds range from ~340 m/s (air) to ~13,000 m/s (some metals at room temperature).

### Built-in materials with temperature compensation

14 commonly-used metals include temperature coefficient data. When the Reference temperature in Settings differs from 20 °C, the app automatically adjusts these materials' speeds:

- Aluminium
- Steel, Mild (1020)
- Stainless Steel (304)
- Iron (cast)
- Iron
- Copper
- Brass
- Bronze
- Titanium
- Magnesium
- Lead
- Zinc
- Nickel
- Tungsten

Materials with compensation show two values in the picker: the **compensated speed** (large, prominent) and the **reference speed at 20 °C** (small, gray underneath).

Materials without compensation show **"ref only"** in italic — their listed speed is used as-is regardless of temperature.

### Custom materials

If you measure a calibration on the 2-Sensor tab, you can save the result as a custom material. After a successful 2-sensor measurement, look for the option to save the derived speed under a name of your choice.

Custom materials store the in-situ measured speed; they never apply temperature compensation (the speed was already measured at the test temperature).

### Favorites

Tap the star next to any material to mark it as a favorite. Favorites appear at the top of the list for quick access.

### Search

Use the search bar at the top to filter materials by name. Search matches both English canonical names and translated display names.

---

## Temperature compensation

The speed of sound in materials changes with temperature. In automotive NVH testing this matters: an engine bay at 80 °C, a cold-soaked cabin at -10 °C, or an exhaust manifold area at 200 °C all behave differently from room-temperature laboratory conditions.

### Setting the temperature

Open Settings (⚙ icon) → Reference temperature. Enter your test environment's temperature in °C (range -40 to +200).

![Settings panel](../screenshots/06-settings.png)

### What happens when temperature ≠ 20 °C

- Calibration time fields auto-fill with the temperature-adjusted speed
- The Materials picker shows the adjusted speed prominently
- A toast confirms: *"Aluminium applied (6,284 m/s @ 60 °C) — N pair(s) updated"*
- The "Closest material" hint compares against temperature-adjusted speeds
- Saved history entries record the active temperature
- Reports include a footer line: *"Reference temperature: 60 °C, compensation applied"*

### Reset on app launch

The Reference temperature **always resets to 20 °C** when you launch the app. This prevents stale settings from a past measurement session silently affecting today's work. A small italic note in Settings reminds you of this behavior.

If you want to replay a historical measurement at its original temperature, just tap the entry — the temperature is restored automatically.

### Materials without compensation

Most non-metal materials don't have reliable published temperature coefficients. The app shows a **"ref only"** badge for these — their listed speed is used regardless of the temperature setting. If you need accurate measurements at non-room temperatures for these materials, perform an in-situ calibration and save the result as a custom material.

---

## Photo annotation

After a successful calculation, tap the **📷 Annotate photo** button to overlay sensor and source markers on a photo of your setup.

![Photo annotation](../screenshots/08-photo-annotation.png)

### Flow

1. Tap **Annotate photo** — the system camera opens
2. Take a photo of your sensor placement
3. The app loads the photo into the annotation overlay
4. Sensor markers (A, B, C, D, E, F as applicable — up to 6 sensors) and the source marker auto-place based on your calculation
5. Drag any marker to fine-tune positioning. As you adjust, the source position recomputes from the corrected sensor positions
6. Tap **Save** to keep, or **Retake** to try again

The annotated photo is included automatically in PDF reports.

---

## Reports

Tap the **Print result** button on any result screen to generate a formatted report.

![PDF report](../screenshots/09-pdf-report.png)

### Report contents

- Header (customizable in Settings → Report header)
- Measurement title and timestamp
- All input values in a clean table
- Calculation result
- Conclusion text
- Visualization (geometry plot)
- Annotated photo (if you took one)
- Temperature footer line (if compensation was active)
- Page number and credit line

### Output format

- **Android**: native PDF generation, save to your phone or share
- **iOS**: system print dialog → save as PDF, AirPrint, or share

### Customizing the header

Settings → Report header. Enter your company name, lab name, project info, or whatever you want at the top of every report.

---

## Backup and restore

Save all your custom materials, favorites, settings, and history to a single file. Transfer between devices.

### Backup

Settings → **Backup** → tap "Save backup file." The app generates a JSON file and opens your phone's share sheet. Save it to your cloud drive (Google Drive, iCloud, OneDrive), email it to yourself, or transfer it any way you like.

### Restore

Settings → **Restore** → pick the backup file from your phone's storage. The app imports custom materials, favorites, history, and settings.

⚠️ **Restore replaces your current data.** If you have important measurements on the current device, back them up first before restoring from a different backup.

---

## Settings

Access via the ⚙ gear icon in the top-right corner. Settings is a modal, not a tab.

![Settings](../screenshots/06-settings.png)

| Setting | What it controls |
|---|---|
| **Upgrade to Pro** | Buy or learn about Pro features ($19.99) |
| **Language** | App display language (30 supported) |
| **Theme** | Light, Dark, or Auto (follow system) |
| **Distance unit** | cm or inches |
| **Reference temperature** | Active temperature for compensation, -40 to +200 °C |
| **Report header** | Custom text at the top of generated reports |
| **Backup** | Export all data to a file |
| **Restore** | Import data from a backup file |
| **Restore purchase** | Re-acquire Pro on a new device |

---

## Pro features

NVH Source Locator uses a **feature-locked freemium model**:

- **Free**: 2-Sensor tab is fully functional with no limits
- **Pro**: All other tabs have specific input fields locked. The paywall appears when a free user taps a locked field

### What's locked

Pro-required fields are scattered across:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- 3D and 3D+ modes
- Backup and Restore
- PDF reports
- Custom materials
- Photo annotation

A free user can OPEN any tab and SEE the interface. They just can't enter values into the Pro-locked input fields.

![Pro-locked field](../screenshots/11-pro-locked-field.png)

### The paywall

![Paywall](../screenshots/07-paywall.png)

When a free user taps a locked field, the paywall slides in showing:
- App icon with PRO badge
- Feature list
- Unlock button with price ($19.99 default; may vary by region)
- Promo code redemption (Android only — iOS uses Apple's separate Offer Code flow)
- Optional promo link to community channels

### Purchasing Pro

Tap any locked field, or tap **Upgrade to Pro** in Settings. Uses your platform's official payment system (Google Play on Android, Apple App Store on iOS).

### Restoring Pro on a new device

If you purchased on one device and want Pro on another (same account):

1. Sign into the **same** Google account (Android) or Apple ID (iOS) you used to buy
2. Open NVH Source Locator on the new device
3. Go to Settings → **Restore purchase**
4. The app verifies with the platform's purchase records and unlocks Pro

### Auto-restore on launch

If you redeem a promo code in the Google Play Store or App Store while NVH Source Locator is running in the background, returning to the app automatically detects the new purchase and unlocks Pro — no manual Restore needed.

### Promo code redemption

**Android**: a "Have a Google Play promo code?" button in the paywall opens the Google Play redemption flow with your code pre-filled.

**iOS**: App Store policy 3.1.1 requires redemption through Apple's official "Redeem code" flow. The Google Play button is hidden on iOS. Look for "Redeem App Store code" in Settings instead.

---

## Help tab and tutorials

The **Help** tab includes in-app tutorials, best-practice guides, and reference information.

![Help tab](../screenshots/10-help-tab.png)

Topics covered:
- What equipment you need
- How to place sensors for best accuracy
- Calibration tips
- Common measurement scenarios
- Tips for triangulation and 3D placements
- Cable routing and signal quality

---

## Troubleshooting

### Calculation result is wrong or makes no sense

1. Check your calibration. Auto-filled `tCal` assumes published material speed — real-world materials vary. The most accurate calibration is in-situ: tap a known location and let the app derive the actual speed.
2. Check the **First sensor** setting — which sensor heard the event first matters for the math.
3. Verify your distance measurements. Errors of a few mm propagate.

### Toast says "Result outside range"

The math says the source is not between your sensors. Possible causes:
- The source actually is outside the sensor line/plane
- One of your inputs is wrong
- The calibration speed is too far off from reality

### Calc-speed hint shows a warning color

The implied speed of sound from your inputs is far from any common material (less than 50 m/s or more than 20,000 m/s). Check your inputs — likely a typo in tCal or distance.

### Material picker shows different speeds than expected

Check the Reference temperature in Settings. If non-20 °C, displayed speeds reflect temperature compensation. The app shows "ref X @ 20°C" underneath compensated speeds so you can verify.

### History entry replays with different result

Old history entries created before app version 1.75 might not have stored the temperature. If you took the measurement at a non-20 °C temperature, replay will use the current setting. Manually set the temperature in Settings before replaying, OR re-measure.

### Photo annotation markers not where I expect

Markers auto-place based on input geometry. Drag them to adjust. Adjusting markers updates the source position in the photo overlay — but does NOT change the underlying calculation result.

### Backup/Restore fails

Make sure you're using a backup file generated by the same or newer version of the app. Older backup files might lack current data fields.

### Restore Purchase says "no purchase found"

1. Verify you're signed into the same store account that you used to purchase
2. Verify the purchase wasn't refunded or expired
3. Try uninstalling and reinstalling the app (purchase is tied to your store account, not the app installation)
4. Contact support@evdiag.net if it persists

### Numeric input snaps to 0 unexpectedly

By design: when you blur a numeric field (tap elsewhere), if it's empty, negative, or contains non-numeric text, it snaps to 0. Prevents silently broken calculations from accidentally cleared inputs. The temperature input is exempt (it clamps to -40/+200 instead).

### Need more help

Contact `support@evdiag.net` with:
- Your device model and OS version
- The app version (Settings → bottom of page)
- Description of what you tried
- Screenshots if possible

---

*NVH Source Locator is developed by EVDiag. Visit https://evdiag.net for updates and resources.*
