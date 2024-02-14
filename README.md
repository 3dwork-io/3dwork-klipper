---

## description: Paquete de macros, configuraciones y otras utilidades para Klipper

# 3Dwork Klipper Bundle

 [![](../../.gitbook/assets/image%20(1986).png) - English](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{% hint style="danger" %}  
**GUÍA EN PROCESO!!! Aunque las macros son totalmente funcionales estas están en continuo desarrollo.**

**Úsalas bajo tu propia responsabilidad!!!**  
{% endhint %}

Changelog

07/12/2023 - Añadido soporte para automatizar la creación de firmware electrónicas Bigtreetech

Desde **3Dwork** hemos recopilado y ajustando un conjunto de macros, configuraciones de máquinas y electrónicas, así como otras herramientas para una gestión sencilla y potente de Klipper.

Gran parte de este paquete está basado en [**RatOS**](https://os.ratrig.com/) mejorando las partes que creemos interesantes, así como otras aportaciones de la comunidad.

## Instalación

Para instalar nuestro paquete para Klipper seguiremos los siguientes pasos

### Descarga del repositorio

Nos conectaremos a nuestro host por SSH y lanzaremos los siguientes comandos:

```
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

{% hint style="warning" %}  
En el caso que el directorio de tu configuración de Klipper esté personalizado recuerda ajustar el primer comando de forma adecuada a tu instalación.  
{% endhint %}

{% hint style="info" %}  
En nuevas instalaciones:

Dado que Klipper no permite el acceso a las macros hasta que no tiene un printer.cfg correcto y conecta con una MCU podemos "engañar" a Klipper con los siguientes pasos que nos van a permitir utilizar las macros de nuestro bundle para, por ejemplo, lanzar la macro de compilación firmware Klipper si usamos una electrónica compatible:

*   Nos aseguramos que tenemos nuestro [host como segunda MCU](raspberry-como-segunda-mcu.md)
*   A continuación añadiremos un printer.cfg, recuerda que estos pasos es para una instalación limpia donde no tengas ningún printer.cfg y quieras lanzar la macro de crear firmware, como el que puedes ver a continuación:

```
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

```
[include 3dwork-klipper/moonraker.conf]
```

{% hint style="warning" %}  
**Recuerda hacer el paso de instalación previamente si no Moonraker generará un error y no podrá iniciar.**

**Por otro lado en el caso que el directorio de tu configuración de Klipper esté personalizado recuerda ajustar el path de forma adecuada a tu instalación.**  
{% endhint %}

## Macros

Siempre hemos comentado que RatOS es una de las mejores distribuciones de Klipper, con soporte a Raspberry y a módulos CB1, en gran medida por sus configuraciones modulares y sus estupendas macros.

Algunas macros añadidas que nos van a ser de utilidad:

### **Macros de uso general**

| Macro | Descripción |
| --- | --- |
| **MAYBE\_HOME** | Nos permite optimizar el proceso de homing solamente realizando este en aquellos ejes que no están con homing. |
| **PAUSE** | Mediante las variables relacionadas nos permite gestionar una pausa con un parking del cabezal más versátil que las macros normales. |
| **SET\_PAUSE\_AT\_LAYER** |   |
| **SET\_PAUSE\_AT\_NEXT\_LAYER** | Una muy útil macro que integra Mainsail en su UI para poder realizar una pausa a demanda en una capa en concreto... por si se nos olvidó al realizar el laminado. |
| También contamos con otra para ejecutar el pausado en la capa siguiente. |   |
| **RESUME** | Mejorada dado que permite detectar si nuestro nozzle no está a la temperatura de extrusión para poder solventarlo antes de que muestre un error y dañe nuestra impresión. |
| **CANCEL\_PRINT** | Que permite el uso del resto de macros para realizar una cancelación de impresiónn correctamente. |

*   **Pausado en cambio de capa**, unas macros muy interesantes que nos permiten hacer un pausado programado en una capa o lanzar un comando al iniciar la siguiente capa.   
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    Además otra ventaja de ellas es que están integradas con Mainsail con lo que tendremos nuevas funciones en nuestra UI como podéis ver a continuación:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Macros de gestión de impresión**

| Macro | Descripción |
| --- | --- |
| **START\_PRINT** | Nos permitirá poder iniciar nuestras impresiones de una forma segura y al estilo Klipper. Dentro de esta encontraremos algunas funciones interesantes como: |
| \- precalentado de nozzle inteligente en el caso de contar con sensor probe |   |
| \- posibilidad de uso de z-tilt mediante variable |   |
| \- mallado de cama adaptativo, forzado o desde una malla guardada |   |
| \- línea de purga personalizable entre normal, línea de purgado adaptativa o gota de purgado |   |
| \- macro segmentada para poder personalizarse tal como os mostraremos más adelante |   |
| **END\_PRINT** | Macro de fin de impresión donde también disponemos de segmentación para poder personalizar nuestra macro. También contamos con aparcado dinámico del cabezal. |

*   **Mallado de cama adaptativo**, gracias a la versatilidad de Klipper podemos hacer cosas que a día de hoy parecen imposibles... un proceso importante para la impresion es tener un mallado de desviaciones de nuestra cama que nos permita corregir estas para tener una adherencia de primeras capas perfecta.   
    En muchas ocasiones hacemos este mallado antes de las impresiones para asegurarnos que funcione correctamente y este se hace en toda la superficie de nuestra cama.  
    Con el mallado de cama adaptativo esta se va a realizar en la zona de impresión haciendo que sea mucho más precisa que el método tradicional... en las siguientes capturas veremos las diferencias de una malla tradicional y una adaptativa.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Macros de gestión de filamento**

Conjunto de macros que nos van a permitir gestionar diferentes acciones con nuestro filamento como la carga o descarga de este.

| Macro | Descripción |
| --- | --- |
| **M600** | Nos va a permitir compatibilidad con el gcode M600 normalmente usado en los laminadores para el cambio de filamento. |
| **UNLOAD\_FILAMENT** | Configurable mediante las variables nos va a permitir una descarga de filamentos asistida. |
| **LOAD\_FILAMENT** | Igual que la anterior pero relacionada con la carga del filamento. |

### **Macros de gestión de bobinas de filamentos (Spoolman)**

{% hint style="warning" %}  
**SECCIÓN EN PROCESO!!!**  
{% endhint %}

[**Spoolman**](https://github.com/Donkie/Spoolman) es un gestor de bobinas de filamento que se integra en Moonraker y que nos permite gestionar nuestro stock y disponibilidad de filamentos.

!\[\](../../.gitbook/assets/image (1990).png)

No vamos a entrar en la instalación y configuración de este dado que es relativamente sencillo utilizando las [**instrucciones de su Github**](https://github.com/Donkie/Spoolman)**,** en cualquier caso **os aconsejamos utilizar Docker** por simplicidad y recordad **activar la configuración en Moonraker** requerida:

{% code title="moonraker.conf" %}

```
[spoolman]
server: http://192.168.0.123:7912
#   URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
#   The interval, in seconds, between sync requests with the
#   Spoolman server.  The default is 5.
```

{% endcode %}

| Macro | Descripción |
| --- | --- |
| SET\_ACTIVE\_SPOOL | Nos permite indicar cual es el ID de la bobina a usar |
| CLEAR\_ACTIVE\_SPOOL | Nos permite resetear la bobina activa |

Lo ideal en cada caso sería el añadir en nuestro laminador, **en los gcodes de filamentos para cada bobina la llamada a esta**, y recuerda **cambiar el ID de esta una vez consumida** para poder llevar un control de lo que resta de filamento en la misma!!!

!\[\](../../.gitbook/assets/image (1991).png)

### **Macros de gestión de superficies de impresión**

{% hint style="warning" %}  
**SECCIÓN EN PROCESO!!!**  
{% endhint %}

Suele ser normal que contemos con diferentes superficies de impresión dependiendo del acabado que queramos tener o el tipo de filamento.

Este conjunto de macros, creadas por [Garethky](https://github.com/garethky), van a permitirnos tener tener un control de estas y en especial el ajuste correcto de ZOffset en cada una de ellas al estilo que contamos en máquinas Prusa. A continuación podéis ver algunas de sus funciones:

*   podremos almacenar el numero de superficies de impresión que queramos, teniendo cada una un nombre único
*   cada superficie de impresión va a tener un ZOffset propio
*   si realizamos ajustes de Z durante una impresión (Babystepping) desde nuestro Klipper este cambio se va a almacentar en la superficie habilitada en ese momento

Por otro lado tenemos algunos **requerimientos para implementarlo (se intentará agregar en la lógica del PRINT\_START del bundle en un futuro activando por variable esta función y creando una macro de usuario previa y posterior para poder meter eventos de usuario)**:

*   se necesita el uso de \[save\_variables\], en nuestro caso usaremos ~/variables.cfg para almacenar las variables y que ya esta dentro del cfg de estas macros.   
    Esto nos creará automáticamente un fichero variables\_build\_sheets.cfg donde guardara nuestras variables en disco.

{% code title="Example of variables config file" %}

```
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

{% endcode %}

*   deberemos incluis una llamada a APPLY\_BUILD\_SHEET\_ADJUSTMENT en nuestro PRINT\_START para poder aplicar el ZOffset de la superficie seleccionada
*   es importante que para que la macro anterior, APPLY\_BUILD\_SHEET\_ADJUSTMENT, funcione correctamente hemos de añadir un SET\_GCODE\_OFFSET Z=0.0 justo antes de llamar a APPLY\_BUILD\_SHEET\_ADJUSTMENT

```
# Load build sheet
SHOW_BUILD_SHEET                ; show loaded build sheet on console
SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset
```

Por otro lado es interesante poder disponer de unas macros para activar una superficie u otra o incluso pasarlo como parámetro desde nuestro laminador para con diferentes perfiles de impresora o de filamento poder cargar una u otra de forma automática:

{% hint style="warning" %}  
Es importante que el valor en NAME="xxxx" coincida con el nombre que dimos a la hora de instalar nuestra superficie de impresión  
{% endhint %}

{% code title="printer.cfg or include cfg" %}

```
## Every Build Plate you want to use needs an Install Macro
[gcode_macro INSTALL_TEXTURED_SHEET]
gcode:
    INSTALL_BUILD_SHEET NAME="Textured PEI"

[gcode_macro INSTALL_SMOOTH_SHEET]
gcode:
    INSTALL_BUILD_SHEET NAME="Smooth PEI"
    
[gcode_macro INSTALL_SMOOTH_GAROLITE_SHEET]
gcode:
    INSTALL_BUILD_SHEET NAME="Smooth Garolite"
```

{% endcode %}

También en el caso de contar con KlipperScreen podremos añadir un menú específico para poder gestionar la carga de las diferentes superficies, donde incluiremos una llamada a las macros anteriormente creadas para la carga de cada superficie:

{% code title="~/printer\_data/config/KlipperScreen.conf" %}

```
[menu __main actions build_sheets]
name: Build Sheets
icon: bed-level

[menu __main actions build_sheets smooth_pei]
name: Smooth PEI
method: printer.gcode.script
params: {"script":"INSTALL_SMOOTH_PEI_SHEET"}

[menu __main actions build_sheets textured_pei]
name: Textured PEI
method: printer.gcode.script
params: {"script":"INSTALL_TEXTURED_PEI_SHEET"}

[menu __main actions build_sheets smooth_garolite]
name: Smooth Garolite
method: printer.gcode.script
params: {"script":"INSTALL_SMOOTH_GAROLITE_SHEET"}
```

{% endcode %}

| Macro | Descripción |
| --- | --- |
| INSTALL\_BUILD\_SHEET |   |
| SHOW\_BUILD\_SHEET |   |
| SHOW\_BUILD\_SHEETS |   |
| SET\_BUILD\_SHEET\_OFFSET |   |
| RESET\_BUILD\_SHEET\_OFFSET |   |
| SET\_GCODE\_OFFSET |   |
| APPLY\_BUILD\_SHEET\_ADJUSTMENT |   |

### **Macros de configuración de máquina**

| Macro | Descripción |
| --- | --- |
| **COMPILE\_FIRMWARE** | Con esta macro podremos compilar el firmware Klipper de una forma sencilla, tener el firmware accesible desde la UI para mayor simplicidad y poder aplicarlo a nuestra electrónica. |
| Aquí tenéis más detalle de las electrónicas soportadas. |   |
| **CALCULATE\_BED\_MESH** | Una macro extremadamente útil para calcular el área para nuestro mallado porque en ocasiones puede resultar un proceso complicado. |
| **PID\_ALL** |   |
| **PID\_EXTRUDER** |   |
| **PID\_BED** | Estas macros, donde podemos pasar las temperaturas para el PID en forma de parámetros, nos van a permitir poder realizar la calibración de temperatura de una forma extremadamente sencilla. |
| **TEST\_SPEED** |   |
| **TEST\_SPEED\_DELTA** | Macro original del compañero [Ellis](https://github.com/AndrewEllis93) nos van a permitir de una forma bastante sencilla testear la velocidad a la que podemos mover nuestra máquina de una forma precisa y sin pérdida de pasos. |

*   **Compilado de firmware para electronicas soportadas**, para facilitar el proceso de creación y mantenimiento de nuestro firmware Klipper para nuestras MCU contamos con la macro COMPILE\_FIRMWARE que al ejecutarla, podemos usar como parámetro nuestra electrónica para hacer solamente esta, compilará Klipper para todas las electrónicas soportadas por nuestro bundle:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Encontraremos estas accesibles de forma sencilla desde nuestra UI web en el directorio firmware\_binaries en nuestra pestaña MACHINE (si usamos Mainsail):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    A continuación tenéis la lista de electrónicas soportadas:

**IMPORTANTE!!!**

estos scripts están preparados para funcionar sobre un sistema Raspbian con usuario pi, si no es tu caso deberás adaptarlo.

los firmwares son generados para su uso con conexión USB que siempre es lo que aconsejamos, además el punto de montaje USB siempre es el mismo por lo que vuestra configuración de la conexión de vuestra MCU no va a cambiar si se generan con nuestra macro/script

**Para que Klipper pueda ejecutar shell macros se ha de instalar una extensión, gracias al compañero** [**Arksine**](https://github.com/Arksine)**, que lo permita.**

**Dependiendo de la distro de Klipper usada pueden venir ya habilitadas.**

![](../../.gitbook/assets/image%20(770).png)

La forma más sencilla es usando [**Kiauh**](../instalacion/#instalando-kiauh) donde encontraremos en una de sus opciones la posibilidad de instalar esta extensión:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

También podemos realizar el proceso a mano copiaremos manualmente el plugin para Klipper [**gcode\_shell\_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py) dentro de nuestro directorio `_**~/klipper/klippy/extras**_` usando SSH o SCP y reiniciamos Klipper.

| Electrónica | Nombre de parámetro a usar en macro |
| --- | --- |
| Manta E3 EZ | btt-manta-e3ez |
| Manta M4P | btt-manta-m4p |
| Manta M4P v2.2 | btt-manta-m4p-22 |
| Manta M8P | btt-manta-m8p |
| Manta M8P v1.1 | btt-manta-m8p-11 |
| Octopus Max EZ | btt-octopus-max-ez |
| Octopus Pro (446) | btt-octopus-pro-446 |
| Octopus Pro (429) | btt-octopus-pro-429 |
| Octopus Pro (H723) | btt-octopus-pro-h723 |
| Octopus v1.1 | btt-octopus-11 |
| Octopus v1.1 (407) | btt-octopus-11-407 |
| SKR Pro v1.2 | skr\_pro\_12 |
| SKR 3 | btt\_skr\_3 |
| SKR 3 (H723) | btt-skr-3-h723 |
| SKR 3 EZ | btt-skr-3-ez |
| SKR 3 EZ (H723) | btt-skr-3-ez-h723 |
| SKR 2 (429) | btt-skr-2-429 |
| SKR 2 (407) | btt-skr-2-407 |
| SKR RAT | btt-skrat-10 |
| SKR 1.4 Turbo | btt-skr-14-turbo |
| SKR Mini E3 v3 | btt\_skr\_mini\_e3\_30 |

| Toolhead (CAN) | Nombre de parámetro a usar en macro |
| --- | --- |
| EBB42 v1 | btt\_ebb42\_10 |
| EBB36 v1 | btt\_ebb36\_10 |
| EBB42 v1.1 | btt\_ebb42\_11 |
| EBB36 v1.1 | btt\_ebb36\_11 |
| EBB42 v1.2 | btt\_ebb42\_12 |
| EBB36 v1.2 | btt\_ebb36\_12 |

| **Electrónica** | **Nombre de parámetro a usar en macro** |
| --- | --- |
| MKS Eagle v1.x | mks-eagle-10 |
| MKS Robin Nano v3 | mks-robin-nano-30 |
| MKS Robin Nano v2 | mks-robin-nano-20 |
| MKS Gen L | mks-gen-l |
| ZNP Robin Nano DW v2 | znp\_robin\_nano\_dw\_v2 |

| Toolhead (CAN) | Nombre de parámetro a usar en macro |
| --- | --- |
| Mellow FLY SHT 42 | mellow\_fly\_sht\_42 |
| Mellow FLY SHT 36 | mellow\_fly\_sht\_36 |

| Electrónica | Nombre de parámetro a usar en macro |
| --- | --- |
| Fysetc Spider | fysetc\_spider |

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
Es importante que añadamos estas líneas al final de nuestro fichero de configuración... justo por encima de la sección para que en el caso de existir macros en nuestro cfg o includes estas sean sobreescritas por las nuestras :  
#\*# \<---------------------- SAVE\_CONFIG ---------------------->  
{% endhint %}

{% hint style="warning" %}  
Se han separado las macros normales de las **macros shell** ya que **para habilitar estas es necesario realizar pasos adicionales de forma manual además que están actualmente testeandose** y \*\*pueden requerir de permisos extras para atribuir permisos de ejecución para lo que no se han indicado las instrucciones ya que se esta intentando automatizar.\*\*  
**Si las utilizas es bajo tu propia responsabilidad.**  
{% endhint %}

### Configuración de nuestro laminador

Dado que nuestras macros son dinámicas van a extraer cierta información de nuestra configuración de impresora y del propio laminador. Para ello os aconsejamos configurar vuestros laminadores de la siguiente forma:

*   **gcode de inicio START\_PRINT**, usando placeholders para pasar los valores de temperatura de filamento y cama de forma dinámica:

{% tabs %}  
{% tab title="PrusaSlicer-SuperSlicer" %}  
**PrusaSlicer**

```
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer** - contamos con la opción de poder ajustar la temperatura de cerramiento (CHAMBER)

```
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{% endtab %}

{% tab title="Bambu Studio/OrcaSlicer" %}

```
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

!\[\](../../.gitbook/assets/image (1760).png){% endtab %}

{% tab title="Cura" %}

```
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

{% hint style="warning" %}  
Deberemos de instalar el plugin [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff) desde el menú _**Help/Show**_ configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.   
Reiniciamos Cura e iremos a _**Extensions/Post processing/Modify G-Code**_ y seleccionaremos _**Mesh Print Size**_.  
{% endhint %}  
{% endtab %}

{% tab title="IdeaMaker" %}

```
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

{% endtab %}

{% tab title="Simplify3D" %}

```
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

{% endtab %}  
{% endtabs %}

{% hint style="info" %}  
Los **placeholders son unos "alias" o variables que usan los laminadores para que a la hora de generar el gcode sustituyen por los valores configurados en el perfil** de impresión.

En los siguientes links podéis encontrar un listado de estos para: [**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (además de los del anterior), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list) y [**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

El uso de estos permiten que nuestras macros sean dinámicas.  
{% endhint %}

*   **gcode de final END\_PRINT**, en este caso al no usar placeholders es común a todos los laminadores

```
END_PRINT
```

### Variables

Como ya hemos comentado, estas nuevas macros nos van a permitir disponer de algunas funciones muy útiles como os listamos anteriormente.

Para el ajuste de estas a nuestra máquina utilizaremos las variables que encontraremos en macros/macros\_var\_globals.cfg y que os detallamos a continuación.

#### Idioma de mensajes/notificaciones

Dado que a muchos usuarios les gusta tener las notificaciones de las macros en su idioma hemos ideado un sistema de notificaciones multi-lenguaje, actualmente español (es) e inglés (en). En la siguiente variable podremos ajustarlo:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_language | Nos permite seleccionar el idioma de las notificaciones. En el caso de no estar bien definido se usará en (inglés) | es / en | es |

#### Extrusión Relativa

Permite controlar que modo de extrusión usaremos al terminar nuestro START\_PRINT. El valor dependerá de la configuración de nuestro laminador.

{% hint style="success" %}  
Es aconsejable que configures tu laminador para el uso de extrusión relativa y ajustar esta variable a True.  
{% endhint %}

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_relative\_extrusion | Nos permite indicar el modo de extrusión usado en nuestro laminador. | True / False | True |

#### Velocidades

Para gestionar las velocidades empleadas en las macros.

| Variable | Descripción | Valores posibles | Valor por defecto |   |
| --- | --- | --- | --- | --- |
| variable\_macro\_travel\_speed | Velocidad en translados | numérico | 150 |   |
| variable\_macro\_z\_speed | Velocidad en translados para eje Z | numérico | 15 |   |

#### Homing

Conjunto de variables relacionadas con el proceso de homing.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |

#### Heating

Variables relacionadas con el proceso de calentado de nuestra máquina.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_preheat\_extruder | Habilita el precalentado del nozzle a la temperatura indicada en variable\_preheat\_extruder\_temp | True / False | True |
| variable\_preheat\_extruder\_temp | Temperatura de precalentado del nozzle | numérico | 150 |
| variable\_start\_print\_heat\_chamber\_bed\_temp | Temperatura de la cama durante el proceso de calentar nuestro cerramiento | numérico | 100 |

{% hint style="success" %}  
Beneficios de utilizar el precalentado del nozzle:

*   nos permite un tiempo adicional para que la cama pueda llegar a su temperatura de una forma uniforme
*   si usamos un sensor indutivo que no tiene compensación de temperatura nos va a permitir que nuestras medidas sean mas consistentes y precisas
*   permite ablandar cualquier resto de filamento en el nozzle lo que permite que, en determinadas configuraciones, estos restos no afecten a la activación del sensor  
    {% endhint %}

#### Mallado de cama (Bed Mesh)

Para controlar el proceso de nivelación contamos con variables que pueden sernos muy útiles. Por ejemplo, podremos controlar el tipo de nivelación que queremos utilizar creando una nueva malla siempre, cargando una almacenada anteriormente o utilizar un mallado adaptativo.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_calibrate\_bed\_mesh | Nos permite seleccionar que tipo de mallado usaremos en nuestro START\_PRINT: |   |   |
| \- new mesh, nos hará un mallado en cada impresión |   |   |   |
| \- storedmesh, cargará un mallado almacenado y no realizará el sondeo de cama |   |   |   |
| \- adaptative, nos hará un nuevo mallado pero adaptado a la zona de impresión mejorando en muchas ocasiones nuestras primeras capas |   |   |   |
| \- nomesh, en el caso que no tengamos sensor o utilicemos mallado para saltarnos el proceso | newmesh / storedmesh / adaptative / |   |   |
| nomesh | adaptative |   |   |
| variable\_bed\_mesh\_profile | El nombre usado para nuestra malla almacenada | texto | default |

{% hint style="warning" %}  
Os aconsejamos usar el nivelado adaptative ya que va a ajustar siempre el mallado al tamaño de nuesta impresión permitiendo tener un área de mallado ajustado.

Es importante que tengamos en nuestro [gcode de incio de nuestro laminador](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), en la llamada a nuestro START\_PRINT, los valores PRINT\_MAX y PRINT\_MIN.  
{% endhint %}

#### Purgado

Una fase importante de nuestro inicio de impresión es un correcto purgado de nuestro nozzle para evitar restos de filamento o que estos puedan dañar nuestra impresión en algún momento. A continuación tienes las variables que intervienen en este proceso:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_nozzle\_priming | Podemos elegir entre diferentes opciones de purgado: |   |   |
| \- primeline nos va a dibujar la típica línea de purgado |   |   |   |
| \- primelineadaptative nos va a generar una línea de purga que se adapta a la zona de la pieza impresa usando variable\_nozzle\_priming\_objectdistance como margen |   |   |   |
| \- primeblob nos hará una gota de filamento en una esquina de nuestra cama muy efectiva para limpiar el nozzle y fácil de retirar |   |   |   |
| primeline / |   |   |   |

primelineadaptative /   
primeblob /   
False

| primelineadaptative |  
| variable\_nozzle\_priming\_objectdistance | Si usamos línea de purga adaptativa será el margen a utilizar entre la línea de purga y el objeto impreso | numérico | 5 |  
| variable\_nozzle\_prime\_start\_x | Donde queremos ubicar nuestra línea de purga:  
\- min lo hará en X=0 (más un pequeño margen de seguridad)  
\- max lo hará en X=max (menos un pequeño margen de seguridad)  
\- número será la coordenada X donde ubicar la purga | min /   
max /   
número | max |  
| variable\_nozzle\_prime\_start\_y | Donde queremos ubicar nuestra línea de purga:  
\- min lo hará en Y=0 (más un pequeño margen de seguridad)  
\- max lo hará en Y=max (menos un pequeño margen de seguridad)  
\- número será la coordenada Y donde ubicar la purga | min /   
max /   
número | min |  
| variable\_nozzle\_prime\_direction | La dirección de nuestra línea o gota:  
\- backwards el cabezal se moverá al frontal de la impresora  
\- forwards se moverá a la parte trasera  
\- auto irá hacia el centro dependiendo de variable\_nozzle\_prime\_start\_y | auto /   
forwards /   
backwards | auto |

#### Carga/Descarga de filamento

En este caso este grupo de variables nos van a facilitar la gestión de carga y descarga de nuestro filamento usado en emulación del M600 por ejemplo o al lanzar las macros de carga y descarga de filamento:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_filament\_unload\_length | Cuanto retraer en mm el filamento, ajustar a tu máquina, normalmente la medida desde tu nozzle a los engranajes de tu extrusor añadiendo un margen extra. | número | 130 |
| variable\_filament\_unload\_speed | Velocidad de retraccíon del filamento en mm/seg normalmente se usa una velocidad lenta. | número | 5 |
| variable\_filament\_load\_length | Distancia en mm para cargar el nuevo filamento... al igual que en variable\_filament\_unload\_length usaremos la medida desde tu engranaje a extrusor añadiendo un margen extra, en este caso este valor extra dependerá de cuanto quieres que se purgue... normalmente puedes darle más margen que el valor anterior para asegurar que quede limpia la extrusion del filamento anterior. | número | 150 |
| variable\_filament\_load\_speed | Velocidad de carga del filamento en mm/seg normalmente se usa una velocidad más rápida que le de descarga. | número | 10 |

{% hint style="warning" %}  
Otro ajuste necesario para vuestra sección \[extruder\] se indique el [**max\_extrude\_only\_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... el valor aconsejable suele ser >101 (en caso de no estar definido usa 50) para por ejemplo permitir los tests típicos de calibración del extrusor.   
Deberías ajustar el valor en base a lo comentado anteriormente del test o la configuración de tu **variable\_filament\_unload\_length** y/o **variable\_filament\_load\_length**.  
{% endhint %}

#### Parking

En determinados procesos de nuestra impresora, como el pausado, es aconsejable hacer un parking de nuestro cabezal. Las macros de nuestro bundle disponen de esta opción además de las siguientes variables para gestionar:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_start\_print\_park\_in | Ubicación donde aparcar el cabezal durante el pre-calentado. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable\_start\_print\_park\_z\_height | Altura en Z durante el pre-calentado | número | 50 |
| variable\_end\_print\_park\_in | Ubicación donde aparcar el cabezal al finalizar o cancelar una impresión. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable\_end\_print\_park\_z\_hop | Distancia a subir en Z al finalizar la impresión. | número | 20 |
| variable\_pause\_print\_park\_in | Ubicación donde aparcar el cabezal al pausar la impresión. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable\_pause\_idle\_timeout | Valor, en segundos, de la activación de proceso de inactividad en la máquina que libera motores y hacer perder coordenadas, **es aconsejable un valor alto para que al activar la macro PAUSE tarde suficiente para realizar cualquier acción antes de perder coordenadas.** | número | 43200 |

#### Z-Tilt

Aprovechar al máximo nuestra máquina para que esta se autonivele y facilitar que nuestra máquina siempre esté en las mejores condiciones es fundamental.

**Z-TILT básicamente es un proceso que nos ayuda a alinear nuestros motores de Z con respecto a nuestro eje/gantry X (cartesiana) o XY (CoreXY)**. Con esto **aseguramos que tenemos siempre alineado nuestro Z perfectamente y de forma precisa y automática**.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_calibrate\_z\_tilt | Permite, en el caso de tenerlo habilitado en nuestra configuración de Klipper, el proceso de ajuste Z-Tilt | True / False | False |

#### Skew

El uso de [SKEW](broken-reference) para la corrección o ajuste preciso de nuestras impresoras es extremadamente aconsejable si tenemos desviaciones en nuestras impresiones. Usando la siguiente variable podemos permitir el uso en nuestras macros:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable\_skew\_profile | Permite tener en cuenta nuestro perfil de skew que será cargado en nuestra macro START\_PRINT. Para activarlo deberemos des comentar la variable y usar el nombre del perfil de skew de nuestra configuración. | texto | my\_skew\_profile |

### Personalización de las macros

Nuestro módulo para Klipper emplea el sistema de configuración modular empleado en RatOS y que aprovecha las ventajas de Klipper en el procesado de ficheros de configuración de forma secuencial de este. Por esto es fundamental el orden de los include y ajustes personalizados que queramos aplicar sobre estos módulos.

{% hint style="info" %}  
Al usarse como uno módulo las configuraciones de 3Dwork NO pueden editarse directamente desde el directorio 3dwork-klipper dentro de tu directorio de configuración de Klipper dado que estará en read-only (restringido a solo lectura) por seguridad.

Por eso es muy importante entender el funcionamiento de Klipper y como poder personalizar nuestros módulos a tu máquina.  
{% endhint %}

#### **Personalizando variables**

Normalmente, será lo que tendremos que ajustar, para realizar ajustes sobre las variables que tengamos por defecto en nuestro módulo **3Dwork** para Klipper.

Simplemente, lo que tengamos que hacer es pegar el contenido de la macro \[gcode\_macro GLOBAL\_VARS\] que podremos encontrar en macros/macros\_var\_globals.cfg en nuestro printer.cfg.

Os recordamos lo comentado anteriormente de como procesa Klipper las configuraciones de forma secuencial, por lo que es aconsejable pegarlo después de los includes que os comentamos [aquí](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nos quedará algo así (solo es un ejemplo visual):

```
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES
## VARIABLES 3DWORK
[gcode_macro GLOBAL_VARS]
description: GLOBAL_VARS variable storage macro, will echo variables to the console when run.
# Configuration Defaults
# This is only here to make the config backwards compatible.
# Configuration should exclusively happen in printer.cfg.

# Possible language values: "en" or "es" (if the language is not well defined, "en" is assigned by default.)
variable_language: "es"                         # Possible values: "en", "es"
...

#_# <---------------------- SAVE_CONFIG ----------------------> #_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#

```

{% hint style="warning" %}
Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.
{% endhint %}

{% hint style="info" %}

*   os aconsejamos añadir comentarios tal como veis en el caso anterior para identificar que hace cada sección
*   aunque no necesites tocar todas las variables te aconsejamos copiar todo el contenido de \[gcode\_macro GLOBAL\_VARS\]
    {% endhint %}

#### Personalizando macros

Las macros se han montado de una forma modular para que se puedan ajustar de una forma sencilla. Tal como os hemos comentado anteriormente, si queremos ajustarlas deberemos proceder igual que hicimos con las variables, copiar la macro en cuestión en nuestro printer.cfg (u otro include nuestro propio) y asegurarnos que está después del include donde añadimos nuestro módulo 3Dwork para Klipper.

Tenemos dos grupos de macros:

*   Macros para añadir ajustes de usuario, estas macros se pueden añadir y personalizar fácilmente porque se añadieron para que cualquier usuario pueda personalizar las acciones a su gusto en determinadas parte de los procesos que hace cada macro.

**START\_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| \_USER\_START\_PRINT\_HEAT\_CHAMBER | Se ejecuta justo después que nuestro cerramiento empiece a calentar, si CHAMBER\_TEMP se pasa como parámetro a nuestro START\_PRINT |
| \_USER\_START\_PRINT\_BEFORE\_HOMING | Se ejecuta antes del homing inicial de inicio de impresión |
| \_USER\_START\_PRINT\_AFTER\_HEATING\_BED | Se ejecuta al llegar nuestra cama a su temperatura, antes de \_START\_PRINT\_AFTER\_HEATING\_BED |
| \_USER\_START\_PRINT\_BED\_MESH | Se lanza antes de \_START\_PRINT\_BED\_MESH |
| \_USER\_START\_PRINT\_PARK | Se lanza antes de \_START\_PRINT\_PARK |
| \_USER\_START\_PRINT\_AFTER\_HEATING\_EXTRUDER | Se lanza antes de \_START\_PRINT\_AFTER\_HEATING\_EXTRUDER |

**END\_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| \_USER\_END\_PRINT\_BEFORE\_HEATERS\_OFF | Se ejecuta antes de realizar el apagado de los calentadores, antes de \_END\_PRINT\_BEFORE\_HEATERS\_OFF |
| \_USER\_END\_PRINT\_AFTER\_HEATERS\_OFF | Se ejecuta después del apagado de los calentadores, antes de \_END\_PRINT\_AFTER\_HEATERS\_OFF |
| \_USER\_END\_PRINT\_PARK | Se ejecuta antes del aparcado del cabezal, antes de \_END\_PRINT\_PARK |

**PRINT\_BASICS**

| Nombre Macro | Descripción |
| --- | --- |
| \_USER\_PAUSE\_START | Se ejecuta al inicio de un PAUSE |
| \_USER\_PAUSE\_END | Se ejecuta al finalizar un PAUSE |
| \_USER\_RESUME\_START | Se ejecuta al inicio de un RESUME |
| \_USER\_RESUME\_END | Se ejecuta al finalizar un RESUME |

*   Macros internas, son macros para dividir la macro principal en procesos y es importante para este. Es aconsejable que en caso de requerir ajustarse estas se copien tal cual.

**START\_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| \_START\_PRINT\_HEAT\_CHAMBER | Calienta el cerramiento en el caso de que el parámetro CHAMBER\_TEMP sea recibido por nuestra macro START\_PRINT desde el laminador |
| \_START\_PRINT\_AFTER\_HEATING\_BED | Se ejecuta al llegar la cama a la temperatura, después de \_USER\_START\_PRINT\_AFTER\_HEATING\_BED. Normalmente, se usa para el procesado de calibraciones de cama (Z\_TILT\_ADJUST, QUAD\_GANTRY\_LEVELING,...) |
| \_START\_PRINT\_BED\_MESH | Se encarga de la lógica de mallado de cama. |
| \_START\_PRINT\_PARK | Aparca el cabezal de impresión mientras calienta el nozzle a la temperatura de impresión. |
| \_START\_PRINT\_AFTER\_HEATING\_EXTRUDER | Realiza el purgado del nozzle y carga el perfil SKEW en caso de que así definamos en las variables |

## Impresoras y electrónicas

A medida que trabajemos con diferentes modelos de impresoras y electrónicas iremos añadiendo aquellas que no estén directamente soportadas por RatOS ya sean aportaciones nuestras o de la comunidad.

*   printers, en este directorio tendremos todas las configuraciones de impresoras
*   boards, aquí encontraremos las de electrónicas

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

```

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

#_# <---------------------- SAVE_CONFIG ----------------------> #_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#

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

```

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

#_# <---------------------- SAVE_CONFIG ----------------------> #_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#

```

{% endcode %}

{% hint style="warning" %}
Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.
{% endhint %}
```
