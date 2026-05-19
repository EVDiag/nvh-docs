# NVH Source Locator — Referencia Rápida

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
