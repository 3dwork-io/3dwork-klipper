---
description: Paquete de macros, configuraciones y otras utilidades para Klipper
---

# 3Dwork Klipper Bundle

> [!WARNING]
> **GUÍA EN PROCESO!!! Aunque las macros son totalmente funcionales estas están en continuo desarrollo.**
> **Úsalas bajo tu propia responsabilidad!!!**</mark>

Desde **3Dwork** hemos recopilado y ajustando un conjunto de macros, configuraciones de máquinas y electrónicas, así como otras herramientas para una gestión sencilla y potente de Klipper.&#x20;

Gran parte de este paquete está basado en [**RatOS**](https://os.ratrig.com/) mejorando las partes que creemos interesantes, así como otras aportaciones de la comunidad.

## Instalación

Para instalar nuestro paquete para Klipper seguiremos los siguientes pasos

### Descarga del repositorio

Nos conectaremos a nuestro host por SSH y lanzaremos los siguientes comandos:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

{% hint style="warning" %}
En el caso que el directorio de tu configuración de Klipper esté personalizado recuerda ajustar el primer comando de forma adecuada a tu instalación.
{% endhint %}

{% hint style="info" %}
En nuevas instalaciones:

Dado que Klipper no permite el acceso a las macros hasta que no tiene un printer.cfg correcto y conecta con una MCU podemos "engañar" a Klipper con los siguientes pasos que nos van a permitir utilizar las macros de nuestro bundle para, por ejemplo, lanzar la macro de compilación firmware Klipper si usamos una electrónica compatible:

* Nos aseguramos que tenemos nuestro [host como segunda MCU](raspberry-como-segunda-mcu.md)
* A continuación añadiremos un printer.cfg, recuerda que estos pasos es para una instalación limpia donde no tengas ningún printer.cfg y quieras lanzar la macro de crear firmware, como el que puedes ver a continuación:

```django
[mcu]
serial: /tmp/klipper_host_mcu

[printer]
kinematics: none
max_velocity: 1
max_accel: 1

[gcode_macro PAUSE]
rename_existing: PAUSE_BASE
gcode:
  M118 Please install a config first!

[gcode_macro RESUME]
rename_existing: RESUME_BASE
gcode:
  M118 Please install a config first!

[gcode_macro CANCEL_PRINT]
rename_existing: CANCEL_BASE
gcode:
  M118 Please install a config first!
  
[idle_timeout]
gcode:
  {% raw %}
{% if printer.webhooks.state|lower == 'ready' %}
    {% if printer.pause_resume.is_paused|lower == 'false' %}
      M117 Idle timeout reached
      TURN_OFF_HEATERS
      M84
    {% endif %}
  {% endif %}
{% endraw %}
# 2 hour timeout
timeout: 7200

[temperature_sensor raspberry_pi]
sensor_type: temperature_host

[skew_correction]

[input_shaper]

[virtual_sdcard]
path: ~/printer_data/gcodes

[display_status]

[pause_resume]

[force_move]
enable_force_move: True

[respond]
```

Con esto podremos iniciar Klipper para que nos de acceso a nuestra macros.
{% endhint %}

### Usando Moonraker para estar siempre actualizado

Gracias a Moonraker podemos usar su update\_manager para poder estar al día de las mejoras que podamos ir introduciendo en el futuro.

Desde Mainsail/Fluidd editaremos nuestro moonraker.conf (debería encontrarse a la misma altura que vuestro printer.cfg) y añadiremos al final del fichero de configuración:

```django
[include 3dwork-klipper/moonraker.conf]
```

{% hint style="warning" %}
<mark style="color:orange;">**Recuerda hacer el paso de instalación previamente si no Moonraker generará un error y no podrá iniciar.**</mark>

**Por otro lado en el caso que el directorio de tu configuración de Klipper esté personalizado recuerda ajustar el path de forma adecuada a tu instalación.**
{% endhint %}

## Macros

Siempre hemos comentado que RatOS es una de las mejores distribuciones de Klipper, con soporte a Raspberry y a módulos CB1, en gran medida por sus configuraciones modulares y sus estupendas macros.

Algunas macros añadidas que nos van a ser de utilidad:

### **Macros de uso general**

| Macro                                                                                   | Descripción                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAYBE\_HOME**                                                                         | Nos permite optimizar el proceso de homing solamente realizando este en aquellos ejes que no están con homing.                                                                                                                                       |
| **PAUSE**                                                                               | Mediante las variables relacionadas nos permite gestionar una pausa con un parking del cabezal más versátil que las macros normales.                                                                                                                 |
| <p><strong>SET_PAUSE_AT_LAYER</strong> <br><strong>SET_PAUSE_AT_NEXT_LAYER</strong></p> | <p>Una muy útil macro que integra Mainsail en su UI para poder realizar una pausa a demanda en una capa en concreto... por si se nos olvidó al realizar el laminado.<br>También contamos con otra para ejecutar el pausado en la capa siguiente.</p> |
| **RESUME**                                                                              | Mejorada dado que permite detectar si nuestro nozzle no está a la temperatura de extrusión para poder solventarlo antes de que muestre un error y dañe nuestra impresión.                                                                            |
| **CANCEL\_PRINT**                                                                       | Que permite el uso del resto de macros para realizar una cancelación de impresiónn correctamente.                                                                                                                                                    |

* **Pausado en cambio de capa**, unas macros muy interesantes que nos permiten hacer un pausado programado en una capa o lanzar un comando al iniciar la siguiente capa. \
  ![](<../../.gitbook/assets/image (6) (5) (1) (2).png>)![](<../../.gitbook/assets/image (1) (1) (8).png>)\
  Además otra ventaja de ellas es que están integradas con Mainsail con lo que tendremos nuevas funciones en nuestra UI como podéis ver a continuación:\
  ![](<../../.gitbook/assets/image (3) (15).png>)![](<../../.gitbook/assets/image (29) (1) (2).png>)

### **Macros de gestión de impresión**

<table><thead><tr><th width="170">Macro</th><th>Descripción</th></tr></thead><tbody><tr><td><strong>START_PRINT</strong></td><td>Nos permitirá poder iniciar nuestras impresiones de una forma segura y al estilo Klipper. Dentro de esta encontraremos algunas funciones interesantes como:<br>- precalentado de nozzle inteligente en el caso de contar con sensor probe<br>- posibilidad de uso de z-tilt mediante variable<br>- mallado de cama adaptativo, forzado o desde una malla guardada<br>- línea de purga personalizable entre normal, línea de purgado adaptativa o gota de purgado<br>- macro segmentada para poder personalizarse tal como os mostraremos más adelante</td></tr><tr><td><strong>END_PRINT</strong></td><td>Macro de fin de impresión donde también disponemos de segmentación para poder personalizar nuestra macro. También contamos con aparcado dinámico del cabezal.</td></tr></tbody></table>

* **Mallado de cama adaptativo**, gracias a la versatilidad de Klipper podemos hacer cosas que a día de hoy parecen imposibles... un proceso importante para la impresion es tener un mallado de desviaciones de nuestra cama que nos permita corregir estas para tener una adherencia de primeras capas perfecta. \
  En muchas ocasiones hacemos este mallado antes de las impresiones para asegurarnos que funcione correctamente y este se hace en toda la superficie de nuestra cama.\
  Con el mallado de cama adaptativo esta se va a realizar en la zona de impresión haciendo que sea mucho más precisa que el método tradicional... en las siguientes capturas veremos las diferencias de una malla tradicional y una adaptativa.\
  ![](<../../.gitbook/assets/image (6) (12) (1).png>)![](<../../.gitbook/assets/image (2) (1) (4).png>)

### **Macros de gestión de filamento**

| Macro                | Descripción                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **M600**             | Nos va a permitir compatibilidad con el gcode M600 normalmente usado en los laminadores para el cambio de filamento. |
| **UNLOAD\_FILAMENT** | Configurable mediante las variables nos va a permitir una descarga de filamentos asistida.                           |
| **LOAD\_FILAMENT**   | Igual que la anterior pero relacionada con la carga del filamento.                                                   |

### **Macros de configuración de máquina**

| Macro                                                                                        | Descripción                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILE\_FIRMWARE**                                                                        | <p>Con esta macro podremos compilar el firmware Klipper de una forma sencilla, tener el firmware accesible desde la UI para mayor simplicidad y poder aplicarlo a nuestra electrónica.<br>Aquí tenéis más detalle de las electrónicas soportadas.</p> |
| **CALCULATE\_BED\_MESH**                                                                     | Una macro extremadamente útil para calcular el área para nuestro mallado porque en ocasiones puede resultar un proceso complicado.                                                                                                                    |
| <p><strong>PID_ALL</strong><br><strong>PID_EXTRUDER</strong><br><strong>PID_BED</strong></p> | Estas macros, donde podemos pasar las temperaturas para el PID en forma de parámetros, nos van a permitir poder realizar la calibración de temperatura de una forma extremadamente sencilla.                                                          |
| <p><strong>TEST_SPEED</strong><br><strong>TEST_SPEED_DELTA</strong></p>                      | Macro original del compañero [Ellis](https://github.com/AndrewEllis93) nos van a permitir de una forma bastante sencilla testear la velocidad a la que podemos mover nuestra máquina de una forma precisa y sin pérdida de pasos.                     |

* **Compilado de firmware para electronicas soportadas**, para facilitar el proceso de creación y mantenimiento de nuestro firmware Klipper para nuestras MCU contamos con la macro COMPILE\_FIRMWARE que al ejecutarla, podemos usar como parámetro nuestra electrónica para hacer solamente esta, compilará Klipper para todas las electrónicas soportadas por nuestro bundle:\
  ![](<../../.gitbook/assets/image (7) (5) (1).png>)\
  Encontraremos estas accesibles de forma sencilla desde nuestra UI web en el directorio firmware\_binaries en nuestra pestaña MACHINE (si usamos Mainsail):\
  ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)\
  A continuación tenéis la lista de electrónicas soportadas:

{% hint style="warning" %}
**IMPORTANTE!!!**

* estos scripts están preparados para funcionar sobre un sistema Raspbian con usuario pi, si no es tu caso deberás adaptarlo.
* los firmwares son generados para su uso con conexión USB que siempre es lo que aconsejamos, además el punto de montaje USB siempre es el mismo por lo que vuestra configuración de la conexión de vuestra MCU no va a cambiar si se generan con nuestra macro/script
*   **Para que Klipper pueda ejecutar shell macros se ha de instalar una extensión, gracias al compañero** [**Arksine**](https://github.com/Arksine)**, que lo permita.**&#x20;

    <mark style="color:green;">**Dependiendo de la distro de Klipper usada pueden venir ya habilitadas.**</mark>

    ![](<../../.gitbook/assets/image (1179).png>)

    La forma más sencilla es usando [**Kiauh**](../instalacion/#instalando-kiauh) donde encontraremos en una de sus opciones la posibilidad de instalar esta extensión:

    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x\_partial.jpg)

    También podemos realizar el proceso a mano copiaremos manualmente el plugin para Klipper[ **gcode\_shell\_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode\_shell\_command.py) dentro de nuestro directorio _**`~/klipper/klippy/extras`**_ usando SSH o SCP y reiniciamos Klipper.
{% endhint %}

{% tabs %}
{% tab title="Bigtreetech" %}
| Electrónica        | Nombre de parámetro a usar en macro |
| ------------------ | ----------------------------------- |
| Octopus Pro (446)  | octopus\_pro\_446                   |
| Octopus Pro (429)  | octopus\_pro\_429                   |
| Octopus v1.1       | octopus\_11                         |
| Octopus v1.1 (407) | octopus\_11\_407                    |
| SKR Pro v1.2       | skr\_pro\_12                        |
| SKR 3              | btt\_skr\_3                         |
| SKR 2 (429)        | skr\_2\_429                         |
| SKR Mini E3 v3     | btt\_skr\_mini\_e3\_30              |

| Toolhead (CAN) | Nombre de parámetro a usar en macro |
| -------------- | ----------------------------------- |
| EBB42 v1       | btt\_ebb42\_10                      |
| EBB36 v1       | btt\_ebb36\_10                      |
| EBB42 v1.1     | btt\_ebb42\_11                      |
| EBB36 v1.1     | btt\_ebb36\_11                      |
| EBB42 v1.2     | btt\_ebb42\_12                      |
| EBB36 v1.2     | btt\_ebb36\_12                      |
{% endtab %}

{% tab title="MKS/ZNP" %}
| Electrónica          | Nombre de parámetro a usar en macro |
| -------------------- | ----------------------------------- |
| ZNP Robin Nano DW v2 | znp\_robin\_nano\_dw\_v2            |
{% endtab %}

{% tab title="Mellow" %}
| Toolhead (CAN)    | Nombre de parámetro a usar en macro |
| ----------------- | ----------------------------------- |
| Mellow FLY SHT 42 | mellow\_fly\_sht\_42                |
| Mellow FLY SHT 36 | mellow\_fly\_sht\_36                |
{% endtab %}

{% tab title="Fysetc" %}
| Electrónica   | Nombre de parámetro a usar en macro |
| ------------- | ----------------------------------- |
| Fysetc Spider | fysetc\_spider                      |
{% endtab %}
{% endtabs %}

### Añadiendo las macros 3Dwork a nuestra instalación

Desde nuestra interfaz, Mainsail/Fluidd, editaremos nuestro printer.cfg y añadiremos:

{% code title="printer.cfg" %}
```
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```
{% endcode %}

{% hint style="info" %}
Es importante que añadamos estas líneas al final de nuestro fichero de configuración... justo por encima de la sección para que en el caso de existir macros en nuestro cfg o includes estas sean sobreescritas por las nuestras :\
\#\*# <---------------------- SAVE\_CONFIG ---------------------->
{% endhint %}

{% hint style="warning" %}
Se han separado las macros normales de las **macros shell** ya que **para habilitar estas es necesario realizar pasos adicionales de forma manual además que están actualmente testeandose** y **pueden requerir de permisos extras para atribuir permisos de ejecución para lo que no se han indicado las instrucciones ya que se esta intentando automatizar.**\
<mark style="color:red;">**Si las utilizas es bajo tu propia responsabilidad.**</mark>
{% endhint %}

### Configuración de nuestro laminador

Dado que nuestras macros son dinámicas van a extraer cierta información de nuestra configuración de impresora y del propio laminador. Para ello os aconsejamos configurar vuestros laminadores de la siguiente forma:

* **gcode de inicio START\_PRINT**, usando placeholders para pasar los valores de temperatura de filamento y cama de forma dinámica:

{% tabs %}
{% tab title="PrusaSlicer-SuperSlicer" %}
**PrusaSlicer**

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer** - contamos con la opción de poder ajustar la temperatura de cerramiento (CHAMBER)

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](<../../.gitbook/assets/image (210).png>)
{% endtab %}

{% tab title="Bambu Studio/OrcaSlicer" %}
```gcode
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

<figure><img src="../../.gitbook/assets/image (2) (1) (9) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Cura" %}
```gcode
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

{% hint style="warning" %}
Deberemos de instalar el plugin [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff) desde el menú _**Help/Show**_ configuration Folder... copiaremos el script del link anterior dentro de la carpeta script. \
Reiniciamos Cura e iremos a _**Extensions/Post processing/Modify G-Code**_ y seleccionaremos _**Mesh Print Size**_.
{% endhint %}
{% endtab %}

{% tab title="IdeaMaker" %}
```gcode
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```
{% endtab %}

{% tab title="Simplify3D" %}
```gcode
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Los **placeholders son unos "alias" o variables que usan los laminadores para que a la hora de generar el gcode sustituyen por los valores configurados en el perfil** de impresión.

En los siguientes links podéis encontrar un listado de estos para: [**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders\_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (además de los del anterior), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list) y [**Cura**](http://files.fieldofview.com/cura/Replacement\_Patterns.html).

El uso de estos permiten que nuestras macros sean dinámicas.
{% endhint %}

* **gcode de final END\_PRINT**,  en este caso al no usar placeholders es común a todos los laminadores

```gcode
END_PRINT
```

### Variables

Como ya hemos comentado, estas nuevas macros nos van a permitir disponer de algunas funciones muy útiles como os listamos anteriormente.&#x20;

Para el ajuste de estas a nuestra máquina utilizaremos las variables que encontraremos en macros/macros\_var\_globals.cfg y que os detallamos a continuación.

#### Idioma de mensajes/notificaciones

Dado que a muchos usuarios les gusta tener las notificaciones de las macros en su idioma hemos ideado un sistema de notificaciones multi-lenguaje, actualmente español (es) e inglés (en). En la siguiente variable podremos ajustarlo:

<table><thead><tr><th width="189">Variable</th><th width="247">Descripción</th><th width="163">Valores posibles</th><th>Valor por defecto</th></tr></thead><tbody><tr><td>variable_language</td><td>Nos permite seleccionar el idioma de las notificaciones. En el caso de no estar bien definido se usará en (inglés)</td><td>es / en</td><td>es</td></tr></tbody></table>

#### Extrusión Relativa

Permite controlar que modo de extrusión usaremos al terminar nuestro START\_PRINT. El valor dependerá de la configuración de nuestro laminador.&#x20;

{% hint style="success" %}
Es aconsejable que configures tu laminador para el uso de extrusión relativa y ajustar esta variable a True.
{% endhint %}

| Variable                      | Descripción                                                          | Valores posibles | Valor por defecto |
| ----------------------------- | -------------------------------------------------------------------- | ---------------- | ----------------- |
| variable\_relative\_extrusion | Nos permite indicar el modo de extrusión usado en nuestro laminador. | True / False     | True              |

#### Velocidades

Para gestionar las velocidades empleadas en las macros.

| Variable                       | Descripción                        | Valores posibles | Valor por defecto |   |
| ------------------------------ | ---------------------------------- | ---------------- | ----------------- | - |
| variable\_macro\_travel\_speed | Velocidad en translados            | numérico         | 150               |   |
| variable\_macro\_z\_speed      | Velocidad en translados para eje Z | numérico         | 15                |   |

#### Homing

Conjunto de variables relacionadas con el proceso de homing.

| Variable | Descripción | Valores posibles | Valor por defecto |
| -------- | ----------- | ---------------- | ----------------- |
|          |             |                  |                   |

#### Heating

Variables relacionadas con el proceso de calentado de nuestra máquina.

| Variable                                         | Descripción                                                                                        | Valores posibles | Valor por defecto |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable\_preheat\_extruder                      | Habilita el precalentado del nozzle a la temperatura indicada en variable\_preheat\_extruder\_temp | True / False     | True              |
| variable\_preheat\_extruder\_temp                | Temperatura de precalentado del nozzle                                                             | numérico         | 150               |
| variable\_start\_print\_heat\_chamber\_bed\_temp | Temperatura de la cama durante el proceso de calentar nuestro cerramiento                          | numérico         | 100               |

{% hint style="success" %}
Beneficios de utilizar el precalentado del nozzle:

* nos permite un tiempo adicional para que la cama pueda llegar a su temperatura de una forma uniforme
* si usamos un sensor indutivo que no tiene compensación de temperatura nos va a permitir que nuestras medidas sean mas consistentes y precisas
* permite ablandar cualquier resto de filamento en el nozzle lo que permite que, en determinadas configuraciones, estos restos no afecten a la activación del sensor
{% endhint %}

#### Mallado de cama (Bed Mesh)

Para controlar el proceso de nivelación contamos con variables que pueden sernos muy útiles. Por ejemplo, podremos controlar el tipo de nivelación que queremos utilizar creando una nueva malla siempre, cargando una almacenada anteriormente o utilizar un mallado adaptativo.

| Variable                       | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Valores posibles                                      | Valor por defecto |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------- |
| variable\_calibrate\_bed\_mesh | <p>Nos permite seleccionar que tipo de mallado usaremos en nuestro START_PRINT:<br>- new mesh, nos hará un mallado en cada impresión<br>- storedmesh, cargará un mallado almacenado y no realizará el sondeo de cama<br>- adaptative, nos hará un nuevo mallado pero adaptado a la zona de impresión mejorando en muchas ocasiones nuestras primeras capas<br>- nomesh, en el caso que no tengamos sensor o utilicemos mallado para saltarnos el proceso</p> | <p>newmesh / storedmesh / adaptative / <br>nomesh</p> | adaptative        |
| variable\_bed\_mesh\_profile   | El nombre usado para nuestra malla almacenada                                                                                                                                                                                                                                                                                                                                                                                                                | texto                                                 | default           |

{% hint style="warning" %}
Os aconsejamos usar el nivelado adaptative ya que va a ajustar siempre el mallado al tamaño de nuesta impresión permitiendo tener un área de mallado ajustado.

Es importante que tengamos en nuestro [gcode de incio de nuestro laminador](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start\_print-y-end\_print), en la llamada a nuestro START\_PRINT, los valores PRINT\_MAX y PRINT\_MIN.
{% endhint %}

#### Purgado

Una fase importante de nuestro inicio de impresión es un correcto purgado de nuestro nozzle para evitar restos de filamento o que estos puedan dañar nuestra impresión en algún momento. A continuación tienes las variables que intervienen en este proceso:

| Variable                                  | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                    | Valores posibles                                                          | Valor por defecto   |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | ------------------- |
| variable\_nozzle\_priming                 | <p>Podemos elegir entre diferentes opciones de purgado:<br>- primeline nos va a dibujar la típica línea de purgado<br>- primelineadaptative nos va a generar una línea de purga que se adapta a la zona de la pieza impresa usando variable_nozzle_priming_objectdistance como margen <br>- primeblob nos hará una gota de filamento en una esquina de nuestra cama muy efectiva para limpiar el nozzle y fácil de retirar</p> | <p>primeline / </p><p>primelineadaptative / <br>primeblob / <br>False</p> | primelineadaptative |
| variable\_nozzle\_priming\_objectdistance | Si usamos línea de purga adaptativa será el margen a utilizar entre la línea de purga y el objeto impreso                                                                                                                                                                                                                                                                                                                      | numérico                                                                  | 5                   |
| variable\_nozzle\_prime\_start\_x         | <p>Donde queremos ubicar nuestra línea de purga:<br>- min lo hará en X=0 (más un pequeño margen de seguridad)<br>- max lo hará en X=max (menos un pequeño margen de seguridad)<br>- número será la coordenada X donde ubicar la purga</p>                                                                                                                                                                                      | <p>min / <br>max / <br>número</p>                                         | max                 |
| variable\_nozzle\_prime\_start\_y         | <p>Donde queremos ubicar nuestra línea de purga:<br>- min lo hará en Y=0 (más un pequeño margen de seguridad)<br>- max lo hará en Y=max (menos un pequeño margen de seguridad)<br>- número será la coordenada Y donde ubicar la purga</p>                                                                                                                                                                                      | <p>min / <br>max / <br>número</p>                                         | min                 |
| variable\_nozzle\_prime\_direction        | <p>La dirección de nuestra línea o gota:<br>- backwards el cabezal se moverá al frontal de la impresora<br>- forwards se moverá a la parte trasera<br>- auto irá hacia el centro dependiendo de variable_nozzle_prime_start_y</p>                                                                                                                                                                                              | <p>auto / <br>forwards / <br>backwards</p>                                | auto                |

#### Carga/Descarga de filamento

En este caso este grupo de variables nos van a facilitar la gestión de carga y descarga de nuestro filamento usado en emulación del M600 por ejemplo o al lanzar las macros de carga y descarga de filamento:

| Variable                           | Descripción                                                                                                                                                                                                                                                                                                                                                                               | Valores posibles | Valor por defecto |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable\_filament\_unload\_length | Cuanto retraer en mm el filamento, ajustar a tu máquina, normalmente la medida desde tu nozzle a los engranajes de tu extrusor añadiendo un margen extra.                                                                                                                                                                                                                                 | número           | 130               |
| variable\_filament\_unload\_speed  | Velocidad de retraccíon del filamento en mm/seg normalmente se usa una velocidad lenta.                                                                                                                                                                                                                                                                                                   | número           | 5                 |
| variable\_filament\_load\_length   | Distancia en mm para cargar el nuevo filamento... al igual que en variable\_filament\_unload\_length usaremos la medida desde tu engranaje a extrusor añadiendo un margen extra, en este caso este valor extra dependerá de cuanto quieres que se purgue... normalmente puedes darle más margen que el valor anterior para asegurar que quede limpia la extrusion del filamento anterior. | número           | 150               |
| variable\_filament\_load\_speed    | Velocidad de carga del filamento en mm/seg normalmente se usa una velocidad más rápida que le de descarga.                                                                                                                                                                                                                                                                                | número           | 10                |

{% hint style="warning" %}
Otro ajuste necesario para vuestra sección \[extruder] se indique el [<mark style="color:green;">**max\_extrude\_only\_distance**</mark>](https://www.klipper3d.org/Config\_Reference.html#extruder)... el valor aconsejable suele ser >101 (en caso de no estar definido usa 50) para por ejemplo permitir los tests típicos de calibración del extrusor. \
Deberías ajustar el valor en base a lo comentado anteriormente del test o la configuración de tu **variable\_filament\_unload\_length** y/o **variable\_filament\_load\_length**.
{% endhint %}

#### Parking

En determinados procesos de nuestra impresora, como el pausado, es aconsejable hacer un parking de nuestro cabezal. Las macros de nuestro bundle disponen de esta opción además de las siguientes variables para gestionar:

| Variable                                | Descripción                                                                                                                                                                                                                                                                  | Valores posibles                     | Valor por defecto |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------- |
| variable\_start\_print\_park\_in        | Ubicación donde aparcar el cabezal durante el pre-calentado.                                                                                                                                                                                                                 | <p>back / <br>center / <br>front</p> | back              |
| variable\_start\_print\_park\_z\_height | Altura en Z durante el pre-calentado                                                                                                                                                                                                                                         | número                               | 50                |
| variable\_end\_print\_park\_in          | Ubicación donde aparcar el cabezal al finalizar o cancelar una impresión.                                                                                                                                                                                                    | <p>back / <br>center / <br>front</p> | back              |
| variable\_end\_print\_park\_z\_hop      | Distancia a subir en Z al finalizar la impresión.                                                                                                                                                                                                                            | número                               | 20                |
| variable\_pause\_print\_park\_in        | Ubicación donde aparcar el cabezal al pausar la impresión.                                                                                                                                                                                                                   | <p>back / <br>center / <br>front</p> | back              |
| variable\_pause\_idle\_timeout          | Valor, en segundos, de la activación de proceso de inactividad en la máquina que libera motores y hacer perder coordenadas, **es aconsejable un valor alto para que al activar la macro PAUSE tarde suficiente para realizar cualquier acción antes de perder coordenadas.** | número                               | 43200             |

#### Z-Tilt

Aprovechar al máximo nuestra máquina para que esta se autonivele y facilitar que nuestra máquina siempre esté en las mejores condiciones es fundamental.&#x20;

**Z-TILT básicamente es un proceso que nos ayuda a alinear nuestros motores de Z con respecto a nuestro eje/gantry X (cartesiana) o XY (CoreXY)**. Con esto **aseguramos que tenemos siempre alineado nuestro Z perfectamente y de forma precisa y automática**.

| Variable                     | Descripción                                                                                                | Valores posibles | Valor por defecto |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable\_calibrate\_z\_tilt | Permite, en el caso de tenerlo habilitado en nuestra configuración de Klipper, el proceso de ajuste Z-Tilt | True / False     | False             |

#### Skew

El uso de [SKEW](../../guias-impresion-3d/calibracion\_3d.md#7.-pasos-ejes) para la corrección o ajuste preciso de nuestras impresoras es extremadamente aconsejable si tenemos desviaciones en nuestras impresiones. Usando la siguiente variable podemos permitir el uso en nuestras macros:

| Variable                | Descripción                                                                                                                                                                                                    | Valores posibles | Valor por defecto |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable\_skew\_profile | Permite tener en cuenta nuestro perfil de skew que será cargado en nuestra macro START\_PRINT. Para activarlo deberemos des comentar la variable y usar el nombre del perfil de skew de nuestra configuración. | texto            | my\_skew\_profile |

### Personalización de las macros

Nuestro módulo para Klipper emplea el sistema de configuración modular empleado en RatOS y que aprovecha las ventajas de Klipper en el procesado de ficheros de configuración de forma secuencial de este. Por esto es fundamental el orden de los include y ajustes personalizados que queramos aplicar sobre estos módulos.

{% hint style="info" %}
Al usarse como uno módulo las configuraciones de 3Dwork NO pueden editarse directamente desde el directorio 3dwork-klipper dentro de tu directorio de configuración de Klipper dado que estará en read-only (restringido a solo lectura) por seguridad.

Por eso es muy importante entender el funcionamiento de Klipper y como poder personalizar nuestros módulos a tu máquina.
{% endhint %}

#### **Personalizando variables**

Normalmente, será lo que tendremos que ajustar, para realizar ajustes sobre las variables que tengamos por defecto en nuestro módulo **3Dwork** para Klipper.&#x20;

Simplemente, lo que tengamos que hacer es pegar el contenido de la macro \[gcode\_macro GLOBAL\_VARS] que podremos encontrar en macros/macros\_var\_globals.cfg en nuestro printer.cfg.

Os recordamos lo comentado anteriormente de como procesa Klipper las configuraciones de forma secuencial, por lo que es aconsejable pegarlo después de los includes que os comentamos [aquí](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nos quedará algo así (solo es un ejemplo visual):

<pre class="language-django"><code class="lang-django">### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES
<strong>## VARIABLES 3DWORK
</strong>[gcode_macro GLOBAL_VARS]
description: GLOBAL_VARS variable storage macro, will echo variables to the console when run.
# Configuration Defaults
# This is only here to make the config backwards compatible.
# Configuration should exclusively happen in printer.cfg.

# Possible language values: "en" or "es" (if the language is not well defined, "en" is assigned by default.)
variable_language: "es"                         # Possible values: "en", "es"
...

<strong>
</strong>#*# &#x3C;---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
</code></pre>

{% hint style="warning" %}
Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.
{% endhint %}

{% hint style="info" %}
* os aconsejamos añadir comentarios tal como veis en el caso anterior para identificar que hace cada sección
* aunque no necesites tocar todas las variables te aconsejamos copiar todo el contenido de \[gcode\_macro GLOBAL\_VARS]
{% endhint %}

#### Personalizando macros

Las macros se han montado de una forma modular para que se puedan ajustar de una forma sencilla. Tal como os hemos comentado anteriormente, si queremos ajustarlas deberemos proceder igual que hicimos con las variables, copiar la macro en cuestión en nuestro printer.cfg (u otro include nuestro propio) y asegurarnos que está después del include donde añadimos nuestro módulo 3Dwork para Klipper.

Tenemos dos grupos de macros:

* Macros para añadir ajustes de usuario, estas macros se pueden añadir y personalizar fácilmente porque se añadieron para que cualquier usuario pueda personalizar las acciones a su gusto en determinadas parte de los procesos que hace cada macro.

**START\_PRINT**

<table><thead><tr><th width="400">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_USER_START_PRINT_HEAT_CHAMBER</td><td>Se ejecuta justo después que nuestro cerramiento empiece a calentar, si CHAMBER_TEMP se pasa como parámetro a nuestro START_PRINT</td></tr><tr><td>_USER_START_PRINT_BEFORE_HOMING</td><td>Se ejecuta antes del homing inicial de inicio de impresión</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar nuestra cama a su temperatura, antes de _START_PRINT_AFTER_HEATING_BED</td></tr><tr><td>_USER_START_PRINT_BED_MESH</td><td>Se lanza antes de _START_PRINT_BED_MESH</td></tr><tr><td>_USER_START_PRINT_PARK</td><td>Se lanza antes de _START_PRINT_PARK</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Se lanza antes de _START_PRINT_AFTER_HEATING_EXTRUDER</td></tr></tbody></table>

**END\_PRINT**

| Nombre Macro                             | Descripción                                                                                              |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| \_USER\_END\_PRINT\_BEFORE\_HEATERS\_OFF | Se ejecuta antes de realizar el apagado de los calentadores, antes de \_END\_PRINT\_BEFORE\_HEATERS\_OFF |
| \_USER\_END\_PRINT\_AFTER\_HEATERS\_OFF  | Se ejecuta después del apagado de los calentadores, antes de \_END\_PRINT\_AFTER\_HEATERS\_OFF           |
| \_USER\_END\_PRINT\_PARK                 | Se ejecuta antes del aparcado del cabezal, antes de \_END\_PRINT\_PARK                                   |

**PRINT\_BASICS**

| Nombre Macro          | Descripción                       |
| --------------------- | --------------------------------- |
| \_USER\_PAUSE\_START  | Se ejecuta al inicio de un PAUSE  |
| \_USER\_PAUSE\_END    | Se ejecuta al finalizar un PAUSE  |
| \_USER\_RESUME\_START | Se ejecuta al inicio de un RESUME |
| \_USER\_RESUME\_END   | Se ejecuta al finalizar un RESUME |

* Macros internas, son macros para dividir la macro principal en procesos y es importante para este. Es aconsejable que en caso de requerir ajustarse estas se copien tal cual.

**START\_PRINT**

<table><thead><tr><th width="405">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_START_PRINT_HEAT_CHAMBER</td><td>Calienta el cerramiento en el caso de que el parámetro CHAMBER_TEMP sea recibido por nuestra macro START_PRINT desde el laminador</td></tr><tr><td>_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar la cama a la temperatura, después de _USER_START_PRINT_AFTER_HEATING_BED. Normalmente, se usa para el procesado de calibraciones de cama (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...)</td></tr><tr><td>_START_PRINT_BED_MESH</td><td>Se encarga de la lógica de mallado de cama.</td></tr><tr><td>_START_PRINT_PARK</td><td>Aparca el cabezal de impresión mientras calienta el nozzle a la temperatura de impresión.</td></tr><tr><td>_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Realiza el purgado del nozzle y carga el perfil SKEW en caso de que así definamos en las variables</td></tr></tbody></table>

## Impresoras y electrónicas

A medida que trabajemos con diferentes modelos de impresoras y electrónicas iremos añadiendo aquellas que no estén directamente soportadas por RatOS ya sean aportaciones nuestras o de la comunidad.

* printers, en este directorio tendremos todas las configuraciones de impresoras
* boards, aquí encontraremos las de electrónicas

### Parámetros y pines

Nuestro módulo para Klipper emplea el sistema de configuración modular empleado en RatOS y que aprovecha las ventajas de Klipper en el procesado de ficheros de configuración de forma secuencial de este. Por esto es fundamental el orden de los include y ajustes personalizados que queramos aplicar sobre estos módulos.

{% hint style="info" %}
Al usarse como uno módulo las configuraciones de 3Dwork NO pueden editarse directamente desde el directorio 3dwork-klipper dentro de tu directorio de configuración de Klipper dado que estará en read-only (restringido a solo lectura) por seguridad.

Por eso es muy importante entender el funcionamiento de Klipper y como poder personalizar nuestros módulos a tu máquina.
{% endhint %}

Tal como os explicábamos en "[personalizando macros](3dwork-klipper-bundle.md#personalizando-macros)" usaremos el mismo proceso para ajustar parámetros o pines para ajustarlos a nuestras necesidades.

#### Personalizando parámetros

Tal como os aconsejamos crear un apartado en vuestro printer.cfg que se llame USER OVERRIDES, colocado después de los includes a nuestras configuraciones, para poder ajustar y personalizar cualquier parámetro usado en ellos.

En el siguiente ejemplo veremos como en nuestro caso estamos interesados en personalizar los parámetros de nuestra nivelación de cama (bed\_mesh) ajustando los puntos de sondeo (probe\_count) con respecto en la configuración que tenemos por defecto en las configuraciones de nuestro módulo Klipper:

{% code title="printer.cfg" %}
```django
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES
## VARIABLES 3DWORK
[gcode_macro GLOBAL_VARS]
...

## PARAMETERS 3Dwork
[bed_mesh]
probe_count: 11,11
...

#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
```
{% endcode %}

{% hint style="warning" %}
Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.
{% endhint %}

Podemos emplear este mismo proceso con cualquier parámetro que queramos ajustar.

#### Personalizando configuración de pines

Procederemos exactamente tal como hemos hecho anteriormente, en nuestra zona USER OVERRIDES añadiremos aquellas secciones de pins que queramos ajustar a nuestro gusto.

En el siguiente ejemplo vamos a personalizar cual es el pin de nuestro ventilador de electrónica (controller\_fan) para asignarlo a uno diferente al de por defecto:

{% code title="printer.cfg" %}
```django
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES
## VARIABLES 3DWORK
[gcode_macro GLOBAL_VARS]
...

## PARAMETERS 3Dwork
[bed_mesh]
probe_count: 11,11
...

## PINS 3Dwork
[controller_fan controller_fan]
pin: PA8

#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
```
{% endcode %}

{% hint style="warning" %}
Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.
{% endhint %}
