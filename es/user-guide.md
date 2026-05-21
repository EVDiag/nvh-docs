# NVH Source Locator — Guía del Usuario

NVH Source Locator es una herramienta de medición para localizar fuentes de ruido y vibración mediante TDOA (Tiempo Diferencial de Llegada) a partir de señales de acelerómetros capturadas en un osciloscopio o sistema de medición.

Esta guía cubre todas las funciones. Para un repaso rápido, consulte **Referencia Rápida**.

---

## Tabla de Contenidos

1. [Cómo funciona](#how-it-works)
2. [Antes de empezar](#before-you-start)
3. [Las pestañas principales](#the-main-tabs)
4. [Modo 2-Sensor](#2-sensor-mode)
5. [Modo 3-Sensor](#3-sensor-mode)
6. [Modos Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [La pestaña Materials](#the-materials-tab)
8. [Compensación de temperatura](#temperature-compensation)
9. [Anotación de fotos](#photo-annotation)
10. [Informes](#reports)
11. [Backup y restauración](#backup-and-restore)
12. [Ajustes](#settings)
13. [Funciones Pro](#pro-features)
14. [Pestaña Help y tutoriales](#help-tab-and-tutorials)
15. [Resolución de problemas](#troubleshooting)

---

## Cómo funciona

Cuando una fuente de ruido emite un sonido o vibración, la onda viaja a través de un material a una velocidad conocida. Si coloca dos o más acelerómetros en el material y mide cuándo llega la onda a cada uno, la diferencia de tiempo le indica dónde está la fuente.

NVH Source Locator toma:

- **Calibración**: la distancia entre sensores y el tiempo que tarda una onda en recorrer esa distancia (utilizado para calcular la velocidad del sonido del material)
- **Evento**: la diferencia de tiempo entre sensores que detectan el evento de ruido/vibración

Luego calcula dónde se encuentra la fuente en la estructura.

Cuantos más sensores utilice, con mayor precisión podrá localizar la fuente:

- **2 sensores** → distancia a lo largo de una línea
- **3 sensores** → posición en una superficie 2D (X, Y)
- **4 sensores** → posición en el espacio 3D (X, Y, Z)

---

## Antes de empezar

Necesitará:

- **Un osciloscopio o sistema de medición** que pueda mostrar la diferencia de tiempo entre los canales del acelerómetro en microsegundos (µs)
- **Al menos 2 acelerómetros** físicamente conectados a la estructura (más sensores = mayor precisión)
- **Una forma de medir la distancia** entre sensores (cinta métrica, calibres)
- **Una forma de generar una onda** en una ubicación conocida para la calibración (impacto de martillo calibrado, golpe de destornillador u otra señal conocida)

![Pantalla principal con pestaña 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Las pestañas principales

La aplicación tiene pestañas en la parte superior:

![Barra de pestañas](../screenshots/02-tab-bar.png)

| Pestaña | Qué hace | Cuándo usar |
|---|---|---|
| **2-Sensor** | Localización de fuente 1D a lo largo de una línea entre 2 sensores | Comprobaciones rápidas, estructuras tipo viga. **Completamente gratis.** |
| **3-Sensor** | Localización de fuente 2D usando 3 sensores en un triángulo | Uso más general, paneles y superficies |
| **3-Sen+** | 3-Sensor con solucionador de mínimos cuadrados sobredeterminado | Mediciones más exigentes, robusto al ruido |
| **4-Sensor** | Localización 2D usando dos pares (A-B + C-D) | Distribuciones rectangulares de sensores, verificación cruzada |
| **4-Sen+** | Modo 2D avanzado, 4 sensores en cualquier posición | Geometrías no rectangulares, LSQ completo |
| **3D** | Localización de fuente 3D usando 4 sensores con coordenadas XYZ | Estructuras complejas en el espacio 3D |
| **3D+** | 3D con hasta 6 sensores, LSQ sobredeterminado | Geometrías muy complejas, máxima precisión |
| **Materials** | Biblioteca de velocidad del sonido + materiales personalizados | Seleccionar una vez por sesión de medición |
| **Help** | Tutoriales en la aplicación y referencia | Cuando necesite un repaso rápido |

> **Gratis vs Pro**: La pestaña 2-Sensor es completamente gratis. Las otras pestañas son accesibles pero tienen campos de entrada específicos bloqueados para usuarios Pro (marcados con una insignia de candado dorado). Tocar un campo bloqueado muestra la paywall Pro.

Los ajustes se acceden mediante el icono de engranaje ⚙ en la esquina superior derecha (no es una pestaña).

---

## Modo 2-Sensor

La medición más simple: localización de fuente a lo largo de una línea entre dos acelerómetros.

![Pestaña 2-Sensor](../screenshots/01-home-2sensor.png)

### Paso 1: Aplicar un material

Toque la pestaña Materials. Elija el material del que está hecha su estructura (por ejemplo, "Aluminio", "Acero, Mild (1020)"). La aplicación usa la velocidad del sonido conocida del material para rellenar automáticamente el campo de tiempo de calibración.

Si el material de su estructura no está en la lista, puede seleccionar "Aire" temporalmente y anular el tiempo de calibración manualmente en el paso 2.

### Paso 2: Introducir datos de calibración

En la pestaña 2-Sensor, verá dos secciones de pares: **Par A–B** y **Par A–C** (solo se requiere A–B si solo tiene 2 sensores).

Para cada par, complete:

- **Espaciado del sensor** (`d`): distancia física entre sensores, en cm o pulgadas (configurado en Ajustes)
- **Retardo de tiempo de calibración** (`tCal`): tiempo para que una onda viaje entre los sensores a la velocidad del sonido del material — se rellena automáticamente cuando elige un material, pero puede anularlo

### Paso 3: Introducir el tiempo del evento

- **Retardo de tiempo del evento** (`tEvent`): diferencia de tiempo entre sensores que detectan el evento de ruido, en microsegundos
- **Primer sensor**: qué sensor escuchó el evento primero (A o B)

### Paso 4: Leer el resultado

La aplicación muestra la posición de la fuente como una distancia desde el sensor A:
- Resultado = 0: la fuente está en el sensor A
- Resultado = distancia: la fuente está en el sensor B
- Resultado intermedio: la fuente está entre ellos
- Resultado fuera: la fuente está más allá de uno de los sensores (el toast advertirá)

La tarjeta de resultados muestra ambas distancias (desde A, desde B) e indica qué sensor está más cerca.

### Paso 5 (opcional): Anotar una foto

Toque **📷 Anotar foto** para tomar una foto de su configuración. La aplicación superpone marcadores para los sensores A, B y la fuente. Útil para informes.

---

## Modo 3-Sensor

Localiza una fuente en un plano 2D usando tres sensores dispuestos en un triángulo.

![Pestaña 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configuración

Coloque tres sensores en su estructura formando un triángulo. Equilátero, rectángulo o escaleno: la aplicación maneja todas las geometrías.

### Introducir los datos

En la sección **Longitudes de los lados del triángulo**, introduzca la distancia física para los tres lados (A–B, A–C, B–C).

Para cada par (A–B y A–C), introduzca:
- **tCal**: tiempo de calibración (autocompletado desde el material)
- **tEvent**: diferencia de tiempo medida para el evento de ruido
- **Primer sensor**: cuál lo escuchó primero

### Leer el resultado

La aplicación muestra la posición de la fuente como coordenadas X, Y relativas al sensor A (sensor A en el origen, sensor B en el eje X). La visualización muestra los tres sensores y la ubicación de la fuente.

![Resultado del triángulo](../screenshots/04-triangle-result.png)

---

## Modos Pro+

Varias pestañas avanzadas ofrecen solucionadores sobredeterminados y mayor dimensionalidad:

### 3-Sen+ (Pro)

Misma configuración triangular que 3-Sensor, pero calibre Y mida los tres pares (A–B, A–C, B–C). El solucionador usa las 3 TDOAs en un ajuste de mínimos cuadrados, más robusto al ruido de medición y a los materiales anisotrópicos. Se reportan los residuos por par para que pueda detectar mediciones inconsistentes.

### 4-Sensor

Coloque cuatro sensores alrededor del área:
- **A–B** = par horizontal (lados izquierdo/derecho)
- **C–D** = par vertical (lados superior/inferior)

Ejecute el par A–B primero (horizontal), luego el par C–D (vertical). El mapa 2D muestra la intersección. Cada par se calibra por separado, útil cuando el material varía a través de la estructura.

### 4-Sen+ (2D Avanzado)

Cuatro sensores en cualquier posición (no forzados a rectangular). Empareje A con cada uno de B, C, D y calibre por separado. El solucionador de mínimos cuadrados sobredeterminado promedia el ruido de medición por par e informa los residuos por par.

### 3D

Medición 3D completa con 4 sensores colocados en el espacio 3D. Introduzca las coordenadas (X, Y, Z) de cada sensor, además de los tiempos de calibración y de evento para cada par (A–B, A–C, A–D).

### 3D+ (Pro)

Como 3D pero admite hasta **6 sensores** (A a F) con LSQ sobredeterminado. Máxima precisión para geometrías 3D complejas.

---

## La pestaña Materials

Biblioteca de materiales de ingeniería comunes con velocidad del sonido conocida a 20 °C.

![Pestaña Materials](../screenshots/05-materials-tab.png)

### Lista de materiales

La lista incluye aire, fluidos, gomas, polímeros, maderas, vidrios y metales. Las velocidades van desde ~340 m/s (aire) hasta ~13.000 m/s (algunos metales a temperatura ambiente).

### Materiales integrados con compensación de temperatura

14 metales comúnmente utilizados incluyen datos de coeficiente de temperatura. Cuando la Temperatura de referencia en Ajustes difiere de 20 °C, la aplicación ajusta automáticamente las velocidades de estos materiales:

- Aluminio
- Acero, Mild (1020)
- Acero Inoxidable (304)
- Hierro (fundido)
- Hierro
- Cobre
- Latón
- Bronce
- Titanio
- Magnesio
- Plomo
- Zinc
- Níquel
- Tungsteno

Los materiales con compensación muestran dos valores en el selector: la **velocidad compensada** (grande, destacada) y la **velocidad de referencia a 20 °C** (pequeña, gris debajo).

Los materiales sin compensación muestran **"ref only"** en cursiva: su velocidad listada se usa tal cual independientemente de la temperatura.

### Materiales personalizados

Si mide una calibración en la pestaña 2-Sensor, puede guardar el resultado como un material personalizado. Después de una medición 2-Sensor exitosa, busque la opción para guardar la velocidad derivada con un nombre de su elección.

Los materiales personalizados almacenan la velocidad medida in-situ; nunca aplican compensación de temperatura (la velocidad ya se midió a la temperatura de prueba).

### Favoritos

Toque la estrella junto a cualquier material para marcarlo como favorito. Los favoritos aparecen en la parte superior de la lista para acceso rápido.

### Búsqueda

Use la barra de búsqueda en la parte superior para filtrar materiales por nombre. La búsqueda coincide con los nombres canónicos en inglés y los nombres de visualización traducidos.

---

## Compensación de temperatura

La velocidad del sonido en los materiales cambia con la temperatura. En las pruebas NVH automotrices, esto es importante: un compartimento del motor a 80 °C, una cabina enfriada a -10 °C o un área del colector de escape a 200 °C se comportan de manera diferente a las condiciones de laboratorio a temperatura ambiente.

### Configuración de la temperatura

Abra Ajustes (icono ⚙) → Temperatura de referencia. Introduzca la temperatura de su entorno de prueba en °C (rango -40 a +200).

![Panel de ajustes](../screenshots/06-settings.png)

### Qué sucede cuando la temperatura ≠ 20 °C

- Los campos de tiempo de calibración se autocompletan con la velocidad ajustada por temperatura
- El selector de Materials muestra la velocidad ajustada de forma prominente
- Un toast confirma: *"Aluminio aplicado (6.284 m/s @ 60 °C) — N par(es) actualizado(s)"*
- La pista "Material más cercano" compara con velocidades ajustadas por temperatura
- Las entradas de historial guardadas registran la temperatura activa
- Los informes incluyen una línea de pie de página: *"Temperatura de referencia: 60 °C, compensación aplicada"*

### Restablecer al iniciar la aplicación

La Temperatura de referencia **siempre se restablece a 20 °C** cuando inicia la aplicación. Esto evita que configuraciones obsoletas de una sesión de medición pasada afecten silenciosamente el trabajo de hoy. Una pequeña nota en cursiva en Ajustes le recuerda este comportamiento.

Si desea reproducir una medición histórica a su temperatura original, simplemente toque la entrada: la temperatura se restaura automáticamente.

### Materiales sin compensación

La mayoría de los materiales no metálicos no tienen coeficientes de temperatura publicados confiables. La aplicación muestra una insignia **"ref only"** para estos: su velocidad listada se usa independientemente de la configuración de temperatura. Si necesita mediciones precisas a temperaturas no ambientales para estos materiales, realice una calibración in-situ y guarde el resultado como un material personalizado.

---

## Anotación de fotos

Después de un cálculo exitoso, toque el botón **📷 Anotar foto** para superponer marcadores de sensor y fuente en una foto de su configuración.

![Anotación de fotos](../screenshots/08-photo-annotation.png)

### Flujo

1. Toque **Anotar foto**: se abre la cámara del sistema
2. Tome una foto de la colocación de su sensor
3. La aplicación carga la foto en la superposición de anotaciones
4. Los marcadores de sensor (A, B, C, D, E, F según corresponda, hasta 6 sensores) y el marcador de fuente se colocan automáticamente según su cálculo
5. Arrastre cualquier marcador para ajustar finamente la posición. A medida que ajusta, la posición de la fuente se recalcula a partir de las posiciones de sensor corregidas
6. Toque **Guardar** para conservar, o **Volver a tomar** para intentarlo de nuevo

La foto anotada se incluye automáticamente en los informes PDF.

---

## Informes

Toque el botón **Imprimir resultado** en cualquier pantalla de resultados para generar un informe formateado.

![Informe PDF](../screenshots/09-pdf-report.png)

### Contenido del informe

- Encabezado (personalizable en Ajustes → Encabezado del informe)
- Título de la medición y marca de tiempo
- Todos los valores de entrada en una tabla limpia
- Resultado del cálculo
- Texto de conclusión
- Visualización (gráfico de geometría)
- Foto anotada (si tomó una)
- Línea de pie de página de temperatura (si la compensación estaba activa)
- Número de página y línea de crédito

### Formato de salida

- **Android**: generación nativa de PDF, guardar en su teléfono o compartir
- **iOS**: diálogo de impresión del sistema → guardar como PDF, AirPrint o compartir

### Personalizar el encabezado

Ajustes → Encabezado del informe. Introduzca el nombre de su empresa, nombre del laboratorio, información del proyecto o lo que desee en la parte superior de cada informe.

---

## Backup y restauración

Guarde todos sus materiales personalizados, favoritos, configuraciones e historial en un solo archivo. Transferir entre dispositivos.

### Backup

Ajustes → **Backup** → toque "Guardar archivo de backup". La aplicación genera un archivo JSON y abre la hoja para compartir de su teléfono. Guárdelo en su unidad en la nube (Google Drive, iCloud, OneDrive), envíelo por correo electrónico a sí mismo o transfiéralo de cualquier manera.

### Restaurar

Ajustes → **Restaurar** → seleccione el archivo de backup del almacenamiento de su teléfono. La aplicación importa materiales personalizados, favoritos, historial y configuraciones.

⚠️ **Restaurar reemplaza sus datos actuales.** Si tiene mediciones importantes en el dispositivo actual, haga una copia de seguridad primero antes de restaurar desde un backup diferente.

---

## Ajustes

Acceso a través del icono de engranaje ⚙ en la esquina superior derecha. Ajustes es un modal, no una pestaña.

![Ajustes](../screenshots/06-settings.png)

| Ajuste | Qué controla |
|---|---|
| **Actualizar a Pro** | Comprar o aprender sobre las funciones Pro ($19,99) |
| **Idioma** | Idioma de visualización de la aplicación (30 admitidos) |
| **Tema** | Claro, Oscuro o Auto (seguir sistema) |
| **Unidad de distancia** | cm o pulgadas |
| **Temperatura de referencia** | Temperatura activa para la compensación, -40 a +200 °C |
| **Encabezado del informe** | Texto personalizado en la parte superior de los informes generados |
| **Backup** | Exportar todos los datos a un archivo |
| **Restaurar** | Importar datos desde un archivo de backup |
| **Restaurar compra** | Volver a adquirir Pro en un nuevo dispositivo |

---

## Funciones Pro

NVH Source Locator utiliza un **modelo freemium con bloqueo por funciones**:

- **Gratis**: La pestaña 2-Sensor es completamente funcional sin límites
- **Pro**: Todas las demás pestañas tienen campos de entrada específicos bloqueados. La paywall aparece cuando un usuario gratuito toca un campo bloqueado

### Qué está bloqueado

Los campos requeridos por Pro están distribuidos en:
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modos 3D y 3D+
- Backup y Restaurar
- Informes PDF
- Materiales personalizados
- Anotación de fotos

Un usuario gratuito puede ABRIR cualquier pestaña y VER la interfaz. Simplemente no puede introducir valores en los campos de entrada bloqueados por Pro.

![Campo bloqueado por Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Cuando un usuario gratuito toca un campo bloqueado, la paywall se desliza mostrando:
- Icono de la aplicación con insignia PRO
- Lista de funciones
- Botón de desbloqueo con precio ($19,99 por defecto; puede variar según la región)
- Canje de código promocional (solo Android — iOS usa el flujo separado de Código de Oferta de Apple)
- Enlace promocional opcional a canales de la comunidad

### Comprar Pro

Toque cualquier campo bloqueado o toque **Actualizar a Pro** en Ajustes. Utiliza el sistema de pago oficial de su plataforma (Google Play en Android, Apple App Store en iOS).

### Restaurar Pro en un nuevo dispositivo

Si compró en un dispositivo y desea Pro en otro (misma cuenta):

1. Inicie sesión con la **misma** cuenta de Google (Android) o Apple ID (iOS) que usó para comprar
2. Abra NVH Source Locator en el nuevo dispositivo
3. Vaya a Ajustes → **Restaurar compra**
4. La aplicación verifica con los registros de compra de la plataforma y desbloquea Pro

### Auto-restauración al iniciar

Si canjea un código promocional en Google Play Store o App Store mientras NVH Source Locator se ejecuta en segundo plano, al volver a la aplicación detecta automáticamente la nueva compra y desbloquea Pro: no se necesita Restaurar manual.

### Canje de código promocional

**Android**: un botón "¿Tiene un código promocional de Google Play?" en la paywall abre el flujo de canje de Google Play con su código precargado.

**iOS**: La política de App Store 3.1.1 requiere el canje a través del flujo oficial "Canjear código" de Apple. El botón de Google Play está oculto en iOS. Busque "Canjear código de App Store" en Ajustes en su lugar.

---

## Pestaña Help y tutoriales

La pestaña **Help** incluye tutoriales dentro de la aplicación, guías de mejores prácticas e información de referencia.

![Pestaña Help](../screenshots/10-help-tab.png)

Temas cubiertos:
- Qué equipo necesita
- Cómo colocar sensores para la mejor precisión
- Consejos de calibración
- Escenarios de medición comunes
- Consejos para triangulación y colocaciones 3D
- Enrutamiento de cables y calidad de la señal

---

## Resolución de problemas

### El resultado del cálculo es incorrecto o no tiene sentido

1. Verifique su calibración. El `tCal` autocompletado asume la velocidad publicada del material; los materiales reales varían. La calibración más precisa es in-situ: toque una ubicación conocida y deje que la aplicación derive la velocidad real.
2. Verifique la configuración del **Primer sensor**: qué sensor escuchó el evento primero importa para las matemáticas.
3. Verifique sus mediciones de distancia. Los errores de unos pocos mm se propagan.

### Toast dice "Resultado fuera de rango"

Las matemáticas dicen que la fuente no está entre sus sensores. Posibles causas:
- La fuente realmente está fuera de la línea/plano del sensor
- Una de sus entradas es incorrecta
- La velocidad de calibración está demasiado lejos de la realidad

### La pista de velocidad de cálculo muestra un color de advertencia

La velocidad del sonido implícita de sus entradas está lejos de cualquier material común (menos de 50 m/s o más de 20.000 m/s). Verifique sus entradas: probablemente un error tipográfico en tCal o distancia.

### El selector de Materials muestra velocidades diferentes a las esperadas

Verifique la Temperatura de referencia en Ajustes. Si no es 20 °C, las velocidades mostradas reflejan la compensación de temperatura. La aplicación muestra "ref X @ 20°C" debajo de las velocidades compensadas para que pueda verificar.

### La entrada del historial se reproduce con un resultado diferente

Las entradas de historial antiguas creadas antes de la versión 1.75 de la aplicación pueden no haber almacenado la temperatura. Si tomó la medición a una temperatura no de 20 °C, la reproducción usará la configuración actual. Establezca manualmente la temperatura en Ajustes antes de reproducir, O vuelva a medir.

### Marcadores de anotación de fotos no donde esperaba

Los marcadores se colocan automáticamente según la geometría de entrada. Arrástrelos para ajustar. Ajustar los marcadores actualiza la posición de la fuente en la superposición de fotos, pero NO cambia el resultado del cálculo subyacente.

### Falla Backup/Restaurar

Asegúrese de utilizar un archivo de backup generado por la misma versión o una versión más reciente de la aplicación. Los archivos de backup más antiguos pueden carecer de campos de datos actuales.

### Restaurar compra dice "no se encontró ninguna compra"

1. Verifique que está conectado con la misma cuenta de tienda que utilizó para comprar
2. Verifique que la compra no fue reembolsada o ha expirado
3. Intente desinstalar y reinstalar la aplicación (la compra está vinculada a su cuenta de tienda, no a la instalación de la aplicación)
4. Contacte support@evdiag.net si persiste

### La entrada numérica se ajusta a 0 inesperadamente

Por diseño: cuando desenfoca un campo numérico (toca en otro lugar), si está vacío, es negativo o contiene texto no numérico, se ajusta a 0. Evita cálculos silenciosamente rotos por entradas accidentalmente borradas. La entrada de temperatura está exenta (en su lugar, se limita a -40/+200).

### Necesita más ayuda

Contacte `support@evdiag.net` con:
- El modelo de su dispositivo y la versión del SO
- La versión de la aplicación (Ajustes → parte inferior de la página)
- Descripción de lo que intentó
- Capturas de pantalla si es posible

---

*NVH Source Locator es desarrollado por EVDiag. Visite https://evdiag.net para actualizaciones y recursos.*
