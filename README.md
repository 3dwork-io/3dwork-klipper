# 3Dwork Klipper Bundle 

## Paquete de macros, configuraciones y otras utilidades para Klipper

![Español](https://flagcdn.com/w40/es.png)[![English](https://flagcdn.com/w40/gb.png)](README.en.md) [![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md) [![Italiano](https://flagcdn.com/w40/it.png)](README.it.md) [![Français](https://flagcdn.com/w40/fr.png)](README.fr.md) [![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ ADVERTENCIA** 
> **GUÍA EN PROCESO!!!** **<span style="color: red">Aunque las macros son totalmente funcionales, están en continuo desarrollo.</span>**
> **<span style="color: orange">Úsalas bajo tu propia responsabilidad!!!</span>**

Changelog

07/12/2023 - Añadido soporte para automatizar la creación de firmware para electrónicas Bigtreetech

Desde **3Dwork** hemos recopilado y ajustando un conjunto de macros, configuraciones de máquinas y electrónicas, así como otras herramientas para una gestión sencilla y potente de Klipper.

Gran parte de este paquete está basado en [**RatOS**](https://os.ratrig.com/) mejorando las partes que creemos interesantes, así como otras aportaciones de la comunidad.

## Instalación

Para instalar nuestro paquete para Klipper seguiremos los siguientes pasos

### Descarga del repositorio

Nos conectaremos a nuestro host por SSH y lanzaremos los siguientes comandos:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTA** 
> Si el directorio de tu configuración de Klipper está personalizado, recuerda ajustar el primer comando adecuadamente a tu instalación.

> **ℹ️ INFORMACIÓN PARA NUEVAS INSTALACIONES** 
> Dado que Klipper no permite el acceso a las macros sin un printer.cfg válido y conexión a una MCU, podemos usar esta configuración temporal: 
> 
> 1. Asegúrate de tener el [host como segunda MCU](raspberry-como-segunda-mcu.md) 
> 2. Añade este printer.cfg básico para habilitar las macros: 
 
 ```ini
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
   {% if printer.webhooks.state|lower == 'ready' %}
     {% if printer.pause_resume.is_paused|lower == 'false' %}
       M117 Idle timeout reached
       TURN_OFF_HEATERS
       M84
     {% endif %}
   {% endif %}
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
 
 Esto permitirá iniciar Klipper y acceder a las macros.

### Usando Moonraker para estar siempre actualizado

Gracias a Moonraker podemos usar su update_manager para poder estar al día de las mejoras que podamos ir introduciendo en el futuro.

Desde Mainsail/Fluidd editaremos nuestro moonraker.conf (debería encontrarse a la misma altura que vuestro printer.cfg) y añadiremos al final del fichero de configuración:

```ini
[include 3dwork-klipper/moonraker.conf]
```


> **⚠️ ADVERTENCIA** 
>**Recuerda hacer el paso de instalación previamente si no Moonraker generará un error y no podrá iniciar.**
>
>**Por otro lado en el caso que el directorio de tu configuración de Klipper esté personalizado recuerda ajustar el path de forma adecuada a tu instalación.** 


## Macros

Siempre hemos comentado que RatOS es una de las mejores distribuciones de Klipper, con soporte a Raspberry y a módulos CB1, en gran medida por sus configuraciones modulares y sus estupendas macros.

Algunas macros añadidas que nos van a ser de utilidad:

### **Macros de uso general**

| Macro | Descripción |
| --- | --- |
| **MAYBE_HOME** | Nos permite optimizar el proceso de homing solamente realizando este en aquellos ejes que no están con homing. |
| **PAUSE** | Mediante las variables relacionadas nos permite gestionar una pausa con un parking del cabezal más versátil que las macros normales. |
| **SET_PAUSE_AT_LAYER** |   |
| **SET_PAUSE_AT_NEXT_LAYER** | Una muy útil macro que integra Mainsail en su UI para poder realizar una pausa a demanda en una capa en concreto... por si se nos olvidó al realizar el laminado. |
|| También contamos con otra para ejecutar el pausado en la capa siguiente. |
| **RESUME** | Mejorada dado que permite detectar si nuestro nozzle no está a la temperatura de extrusión para poder solventarlo antes de que muestre un error y dañe nuestra impresión. |
| **CANCEL_PRINT** | Que permite el uso del resto de macros para realizar una cancelación de impresiónn correctamente. |

* **Pausado en cambio de capa**, unas macros muy interesantes que nos permiten hacer un pausado programado en una capa o lanzar un comando al iniciar la siguiente capa.  
![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)
Además otra ventaja de ellas es que están integradas con Mainsail con lo que tendremos nuevas funciones en nuestra UI como podéis ver a continuación: 
![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macros de gestión de impresión**

| Macro | Descripción |
| --- | --- |
| **START_PRINT** | Nos permitirá poder iniciar nuestras impresiones de una forma segura y al estilo Klipper. Dentro de esta encontraremos algunas funciones interesantes como: |
|| • Smart nozzle preheating when using a probe sensor |
|| • Posibilidad de uso de z-tilt mediante variable |
|| • Mallado de cama adaptativo, forzado o desde una malla guardada |   
|| • Línea de purga personalizable entre normal, línea de purgado adaptativa o gota de purgado |   
|| • Macro segmentada para poder personalizarse tal como os mostraremos más adelante |   
| **END_PRINT** | Macro de fin de impresión donde también disponemos de segmentación para poder personalizar nuestra macro. También contamos con aparcado dinámico del cabezal. |

* **Mallado de cama adaptativo**, gracias a la versatilidad de Klipper podemos hacer cosas que a día de hoy parecen imposibles... un proceso importante para la impresion es tener un mallado de desviaciones de nuestra cama que nos permita corregir estas para tener una adherencia de primeras capas perfecta.  
 En muchas ocasiones hacemos este mallado antes de las impresiones para asegurarnos que funcione correctamente y este se hace en toda la superficie de nuestra cama. 
 Con el mallado de cama adaptativo esta se va a realizar en la zona de impresión haciendo que sea mucho más precisa que el método tradicional... en las siguientes capturas veremos las diferencias de una malla tradicional y una adaptativa. 
<div style="display: flex; justify-content: space-between;">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
</div>

### **Macros de gestión de filamento**

Conjunto de macros que nos van a permitir gestionar diferentes acciones con nuestro filamento como la carga o descarga de este.

| Macro | Descripción |
| --- | --- |
| **M600** | Nos va a permitir compatibilidad con el gcode M600 normalmente usado en los laminadores para el cambio de filamento. |
| **UNLOAD_FILAMENT** | Configurable mediante las variables nos va a permitir una descarga de filamentos asistida. |
| **LOAD_FILAMENT** | Igual que la anterior pero relacionada con la carga del filamento. |

### **Macros de gestión de bobinas de filamentos (Spoolman)**

> **⚠️ ADVERTENCIA** 
>**SECCIÓN EN PROCESO!!!** 


[**Spoolman**](https://github.com/Donkie/Spoolman) es un gestor de bobinas de filamento que se integra en Moonraker y que nos permite gestionar nuestro stock y disponibilidad de filamentos.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

No vamos a entrar en la instalación y configuración de este dado que es relativamente sencillo utilizando las [**instrucciones de su Github**](https://github.com/Donkie/Spoolman)**,** en cualquier caso **os aconsejamos utilizar Docker** por simplicidad y recordad **activar la configuración en Moonraker** requerida:

**moonraker.conf**
```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro | Descripción |
| --- | --- |
| SET_ACTIVE_SPOOL | Nos permite indicar cual es el ID de la bobina a usar |
| CLEAR_ACTIVE_SPOOL | Nos permite resetear la bobina activa |

Lo ideal en cada caso sería el añadir en nuestro laminador, **en los gcodes de filamentos para cada bobina la llamada a esta**, y recuerda **cambiar el ID de esta una vez consumida** para poder llevar un control de lo que resta de filamento en la misma!!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Macros de gestión de superficies de impresión**

> **⚠️ ADVERTENCIA** 
>**SECCIÓN EN PROCESO!!!** 

Suele ser normal que contemos con diferentes superficies de impresión dependiendo del acabado que queramos tener o el tipo de filamento.

Este conjunto de macros, creadas por [Garethky](https://github.com/garethky), van a permitirnos tener tener un control de estas y en especial el ajuste correcto de ZOffset en cada una de ellas al estilo que contamos en máquinas Prusa. A continuación podéis ver algunas de sus funciones:

* podremos almacenar el numero de superficies de impresión que queramos, teniendo cada una un nombre único
* cada superficie de impresión va a tener un ZOffset propio
* si realizamos ajustes de Z durante una impresión (Babystepping) desde nuestro Klipper este cambio se va a almacentar en la superficie habilitada en ese momento

Por otro lado tenemos algunos **requerimientos para implementarlo (se intentará agregar en la lógica del PRINT_START del bundle en un futuro activando por variable esta función y creando una macro de usuario previa y posterior para poder meter eventos de usuario)**:

* se necesita el uso de **[save_variables]**, en nuestro caso usaremos ~/variables.cfg para almacenar las variables y que ya esta dentro del cfg de estas macros.  
 Esto nos creará automáticamente un fichero variables_build_sheets.cfg donde guardara nuestras variables en disco.

**Ejemplo de archivo de configuración de variables**
```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

* deberemos incluis una llamada a APPLY_BUILD_SHEET_ADJUSTMENT en nuestro PRINT_START para poder aplicar el ZOffset de la superficie seleccionada
* es importante que para que la macro anterior, APPLY_BUILD_SHEET_ADJUSTMENT, funcione correctamente hemos de añadir un SET_GCODE_OFFSET Z=0.0 justo antes de llamar a APPLY_BUILD_SHEET_ADJUSTMENT

```
# Load build sheet
SHOW_BUILD_SHEET ; show loaded build sheet on console
SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset
```

Por otro lado es interesante poder disponer de unas macros para activar una superficie u otra o incluso pasarlo como parámetro desde nuestro laminador para con diferentes perfiles de impresora o de filamento poder cargar una u otra de forma automática:

> **⚠️ ADVERTENCIA** 
>Es importante que el valor en NAME="xxxx" coincida con el nombre que dimos a la hora de instalar nuestra superficie de impresión 


**printer.cfg
```ini
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

También en el caso de contar con KlipperScreen podremos añadir un menú específico para poder gestionar la carga de las diferentes superficies, donde incluiremos una llamada a las macros anteriormente creadas para la carga de cada superficie:

**~/printer_data/config/KlipperScreen.conf**
```ini
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


| Macro | Descripción |
| --- | --- |
| INSTALL_BUILD_SHEET |   |
| SHOW_BUILD_SHEET |   |
| SHOW_BUILD_SHEETS |   |
| SET_BUILD_SHEET_OFFSET |   |
| RESET_BUILD_SHEET_OFFSET |   |
| SET_GCODE_OFFSET |   |
| APPLY_BUILD_SHEET_ADJUSTMENT |   |

### **Macros de configuración de máquina**

| Macro | Descripción |
| --- | --- |
| **COMPILE_FIRMWARE** | Con esta macro podremos compilar el firmware Klipper de una forma sencilla, tener el firmware accesible desde la UI para mayor simplicidad y poder aplicarlo a nuestra electrónica. |
| Aquí tenéis más detalle de las electrónicas soportadas. |   |
| **CALCULATE_BED_MESH** | Una macro extremadamente útil para calcular el área para nuestro mallado porque en ocasiones puede resultar un proceso complicado. |
| **PID_ALL** |   |
| **PID_EXTRUDER** |   |
| **PID_BED** | Estas macros, donde podemos pasar las temperaturas para el PID en forma de parámetros, nos van a permitir poder realizar la calibración de temperatura de una forma extremadamente sencilla. |
| **TEST_SPEED** |   |
| **TEST_SPEED_DELTA** | Macro original del compañero [Ellis](https://github.com/AndrewEllis93) nos van a permitir de una forma bastante sencilla testear la velocidad a la que podemos mover nuestra máquina de una forma precisa y sin pérdida de pasos. |

*_ **Compilado de firmware para electronicas soportadas**, para facilitar el proceso de creación y mantenimiento de nuestro firmware Klipper para nuestras MCU contamos con la macro COMPILE_FIRMWARE que al ejecutarla, podemos usar como parámetro nuestra electrónica para hacer solamente esta, compilará Klipper para todas las electrónicas soportadas por nuestro bundle: 
![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)
 Encontraremos estas accesibles de forma sencilla desde nuestra UI web en el directorio firmware_binaries en nuestra pestaña MACHINE (si usamos Mainsail): 
![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)
 A continuación tenéis la lista de electrónicas soportadas:


> ⚠️ **IMPORTANTE!!!**
>
>estos scripts están preparados para funcionar sobre un >sistema Raspbian con usuario pi, si no es tu caso deberás adaptarlo.
>
>los firmwares son generados para su uso con conexión USB que siempre es lo que aconsejamos, además el punto de montaje USB siempre es el mismo por lo que vuestra configuración de la conexión de vuestra MCU no va a cambiar si se generan con nuestra macro/script
>
>**Para que Klipper pueda ejecutar shell macros se ha de instalar una extensión, gracias al compañero** [**Arksine**](https://github.com/Arksine)**, que lo permita.**
>
>**Dependiendo de la distro de Klipper usada pueden venir ya habilitadas.**
>
>![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
>La forma más sencilla es usando [**Kiauh**](../instalacion/#instalando-kiauh) donde encontraremos en una de sus opciones la posibilidad de instalar esta extensión:
>
>![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
>También podemos realizar el proceso a mano copiaremos manualmente el plugin para Klipper <[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py) dentro de nuestro directorio `_**~/klipper/klippy/extras**_` usando SSH o SCP y reiniciamos Klipper.

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
| SKR Pro v1.2 | skr_pro_12 |
| SKR 3 | btt_skr_3 |
| SKR 3 (H723) | btt-skr-3-h723 |
| SKR 3 EZ | btt-skr-3-ez |
| SKR 3 EZ (H723) | btt-skr-3-ez-h723 |
| SKR 2 (429) | btt-skr-2-429 |
| SKR 2 (407) | btt-skr-2-407 |
| SKR RAT | btt-skrat-10 |
| SKR 1.4 Turbo | btt-skr-14-turbo |
| SKR Mini E3 v3 | btt_skr_mini_e3_30 |

| Toolhead (CAN) | Nombre de parámetro a usar en macro |
| --- | --- |
| EBB42 v1 | btt_ebb42_10 |
| EBB36 v1 | btt_ebb36_10 |
| EBB42 v1.1 | btt_ebb42_11 |
| EBB36 v1.1 | btt_ebb36_11 |
| EBB42 v1.2 | btt_ebb42_12 |
| EBB36 v1.2 | btt_ebb36_12 |

| **Electrónica** | **Nombre de parámetro a usar en macro** |
| --- | --- |
| MKS Eagle v1.x | mks-eagle-10 |
| MKS Robin Nano v3 | mks-robin-nano-30 |
| MKS Robin Nano v2 | mks-robin-nano-20 |
| MKS Gen L | mks-gen-l |
| ZNP Robin Nano DW v2 | znp_robin_nano_dw_v2 |

| Toolhead (CAN) | Nombre de parámetro a usar en macro |
| --- | --- |
| Mellow FLY SHT 42 | mellow_fly_sht_42 |
| Mellow FLY SHT 36 | mellow_fly_sht_36 |

| Electrónica | Nombre de parámetro a usar en macro |
| --- | --- |
| Fysetc Spider | fysetc_spider |

|Electrónica|Nombre de parámetro a usar en macro|
| --- | --- |
|Artillery Ruby v1.x| artillery-ruby-12|

|Electrónica|Nombre de parámetro a usar en macro|
| --- | --- |
|Raspberry Pico/RP2040|rpi-rp2040

|Electrónica|Nombre de parámetro a usar en macro|
| --- | --- |
|Leviathan v1.2|leviathan-12|

### Añadiendo las macros 3Dwork a nuestra instalación

Desde nuestra interfaz, Mainsail/Fluidd, editaremos nuestro printer.cfg y añadiremos:

**printer.cfg**
```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️ **INFO!!!**
>Es importante que añadamos estas líneas al final de nuestro fichero de configuración... justo por encima de la sección para que en el caso de existir macros en nuestro cfg o includes estas sean sobreescritas por las nuestras : 
>#\*# \<--- SAVE_CONFIG ---> 

> ⚠️ **IMPORTANTE!!!**
>Se han separado las macros normales de las **macros shell** ya que **para habilitar estas es necesario realizar pasos adicionales de forma manual además que están actualmente testeandose** y \*\*pueden requerir de permisos extras para atribuir permisos de ejecución para lo que no se han indicado las instrucciones ya que se esta intentando automatizar.\*\* 
>**Si las utilizas es bajo tu propia responsabilidad.** 


### Configuración de nuestro laminador

Dado que nuestras macros son dinámicas van a extraer cierta información de nuestra configuración de impresora y del propio laminador. Para ello os aconsejamos configurar vuestros laminadores de la siguiente forma:

* **gcode de inicio START_PRINT**, usando placeholders para pasar los valores de temperatura de filamento y cama de forma dinámica:

**PrusaSlicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer** - contamos con la opción de poder ajustar la temperatura de cerramiento (CHAMBER)

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)



**Bambu Studio/OrcaSlicer**
```ini
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

** Cura**
```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```


> ⚠️ **Aviso!!!**
>Deberemos de instalar el plugin [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff) desde el menú _**Help/Show**_ configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.  
>Reiniciamos Cura e iremos a _**Extensions/Post processing/Modify G-Code**_ y seleccionaremos _**Mesh Print Size**_. 


**IdeaMaker**
```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplify3D**
```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️ **INFO!!!**
>Los **placeholders son unos "alias" o variables que usan los laminadores para que a la hora de generar el gcode sustituyen por los valores configurados en el perfil** de impresión.
>
>En los siguientes links podéis encontrar un listado de estos para: [**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (además de los del anterior), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list) y [**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
>El uso de estos permiten que nuestras macros sean dinámicas. 

* **gcode de final END_PRINT**, en este caso al no usar placeholders es común a todos los laminadores

```ini
END_PRINT
```

### Variables

Como ya hemos comentado, estas nuevas macros nos van a permitir disponer de algunas funciones muy útiles como os listamos anteriormente.

Para el ajuste de estas a nuestra máquina utilizaremos las variables que encontraremos en macros/macros_var_globals.cfg y que os detallamos a continuación.

#### Idioma de mensajes/notificaciones

Dado que a muchos usuarios les gusta tener las notificaciones de las macros en su idioma hemos ideado un sistema de notificaciones multi-lenguaje, actualmente español (es) e inglés (en). En la siguiente variable podremos ajustarlo:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_language | Nos permite seleccionar el idioma de las notificaciones. En el caso de no estar bien definido se usará en (inglés) | es / en | es |

#### Extrusión Relativa

Permite controlar que modo de extrusión usaremos al terminar nuestro START_PRINT. El valor dependerá de la configuración de nuestro laminador.

> 💡 **Consejo**
>Es aconsejable que configures tu laminador para el uso de extrusión relativa y ajustar esta variable a True. 


| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_relative_extrusion | Nos permite indicar el modo de extrusión usado en nuestro laminador. | True / False | True |

#### Velocidades

Para gestionar las velocidades empleadas en las macros.

| Variable | Descripción | Valores posibles | Valor por defecto |   |
| --- | --- | --- | --- | --- |
| variable_macro_travel_speed | Velocidad en translados | numérico | 150 |   |
| variable_macro_z_speed | Velocidad en translados para eje Z | numérico | 15 |   |

#### Homing

Conjunto de variables relacionadas con el proceso de homing.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |

#### Heating

Variables relacionadas con el proceso de calentado de nuestra máquina.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_preheat_extruder | Habilita el precalentado del nozzle a la temperatura indicada en variable_preheat_extruder_temp | True / False | True |
| variable_preheat_extruder_temp | Temperatura de precalentado del nozzle | numérico | 150 |
| variable_start_print_heat_chamber_bed_temp | Temperatura de la cama durante el proceso de calentar nuestro cerramiento | numérico | 100 |

> 💡 **Consejo**
>Beneficios de utilizar el precalentado del nozzle:

* nos permite un tiempo adicional para que la cama pueda llegar a su temperatura de una forma uniforme
* si usamos un sensor indutivo que no tiene compensación de temperatura nos va a permitir que nuestras medidas sean mas consistentes y precisas
* permite ablandar cualquier resto de filamento en el nozzle lo que permite que, en determinadas configuraciones, estos restos no afecten a la activación del sensor 
 {% endhint %}

#### Mallado de cama (Bed Mesh)

Para controlar el proceso de nivelación contamos con variables que pueden sernos muy útiles. Por ejemplo, podremos controlar el tipo de nivelación que queremos utilizar creando una nueva malla siempre, cargando una almacenada anteriormente o utilizar un mallado adaptativo.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_calibrate_bed_mesh | Nos permite seleccionar que tipo de mallado usaremos en nuestro START_PRINT: |   |   |
| - new mesh, nos hará un mallado en cada impresión |   |   |   |
| - storedmesh, cargará un mallado almacenado y no realizará el sondeo de cama |   |   |   |
| - adaptative, nos hará un nuevo mallado pero adaptado a la zona de impresión mejorando en muchas ocasiones nuestras primeras capas |   |   |   |
| \- nomesh, en el caso que no tengamos sensor o utilicemos mallado para saltarnos el proceso | newmesh / storedmesh / adaptative / |   |   |
| nomesh | adaptative |   |   |
| variable_bed_mesh_profile | El nombre usado para nuestra malla almacenada | texto | default |

> ⚠️ **Aviso!!!**
>Os aconsejamos usar el nivelado adaptative ya que va a ajustar siempre el mallado al tamaño de nuesta impresión permitiendo tener un área de mallado ajustado.
>
>Es importante que tengamos en nuestro [gcode de incio de nuestro laminador](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), en la llamada a nuestro START_PRINT, los valores PRINT_MAX y PRINT_MIN. 

#### Purgado

Una fase importante de nuestro inicio de impresión es un correcto purgado de nuestro nozzle para evitar restos de filamento o que estos puedan dañar nuestra impresión en algún momento. A continuación tienes las variables que intervienen en este proceso:
| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_nozzle_priming | Podemos elegir entre diferentes opciones de purgado:<br>- primeline: dibuja la típica línea de purgado<br>- primelineadaptative: genera una línea de purga adaptada a la zona de impresión usando variable_nozzle_priming_objectdistance como margen<br>- primeblob: hace una gota de filamento en una esquina de la cama | primeline / primelineadaptative / primeblob / False | primelineadaptative |
| variable_nozzle_priming_objectdistance | Si usamos línea de purga adaptativa será el margen a utilizar entre la línea de purga y el objeto impreso | numérico | 5 |
| variable_nozzle_prime_start_x | Donde ubicar nuestra línea de purga en X:<br>- min: X=0 (más margen de seguridad)<br>- max: X=max (menos margen de seguridad)<br>- número: coordenada X específica | min / max / número | max |
| variable_nozzle_prime_start_y | Donde ubicar nuestra línea de purga en Y:<br>- min: Y=0 (más margen de seguridad)<br>- max: Y=max (menos margen de seguridad)<br>- número: coordenada Y específica | min / max / número | min |
| variable_nozzle_prime_direction | Dirección de la línea o gota:<br>- backwards: hacia el frontal<br>- forwards: hacia atrás<br>- auto: hacia el centro según variable_nozzle_prime_start_y | auto / forwards / backwards | auto |

#### Carga/Descarga de filamento

En este caso este grupo de variables nos van a facilitar la gestión de carga y descarga de nuestro filamento usado en emulación del M600 por ejemplo o al lanzar las macros de carga y descarga de filamento:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_filament_unload_length | Cuanto retraer en mm el filamento, ajustar a tu máquina, normalmente la medida desde tu nozzle a los engranajes de tu extrusor añadiendo un margen extra. | número | 130 |
| variable_filament_unload_speed | Velocidad de retraccíon del filamento en mm/seg normalmente se usa una velocidad lenta. | número | 5 |
| variable_filament_load_length | Distancia en mm para cargar el nuevo filamento... al igual que en variable_filament_unload_length usaremos la medida desde tu engranaje a extrusor añadiendo un margen extra, en este caso este valor extra dependerá de cuanto quieres que se purgue... normalmente puedes darle más margen que el valor anterior para asegurar que quede limpia la extrusion del filamento anterior. | número | 150 |
| variable_filament_load_speed | Velocidad de carga del filamento en mm/seg normalmente se usa una velocidad más rápida que le de descarga. | número | 10 |

> ⚠️ **Aviso!!!**
>Otro ajuste necesario para vuestra sección **[extruder]** se indique el [**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... el valor aconsejable suele ser >101 (en caso de no estar definido usa 50) para por ejemplo permitir los tests típicos de calibración del extrusor.  
>Deberías ajustar el valor en base a lo comentado anteriormente del test o la configuración de tu **variable_filament_unload_length** y/o **variable_filament_load_length**. 

#### Parking

En determinados procesos de nuestra impresora, como el pausado, es aconsejable hacer un parking de nuestro cabezal. Las macros de nuestro bundle disponen de esta opción además de las siguientes variables para gestionar:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_start_print_park_in | Ubicación donde aparcar el cabezal durante el pre-calentado. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable_start_print_park_z_height | Altura en Z durante el pre-calentado | número | 50 |
| variable_end_print_park_in | Ubicación donde aparcar el cabezal al finalizar o cancelar una impresión. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable_end_print_park_z_hop | Distancia a subir en Z al finalizar la impresión. | número | 20 |
| variable_pause_print_park_in | Ubicación donde aparcar el cabezal al pausar la impresión. | back / |   |
| center / |   |   |   |
| front | back |   |   |
| variable_pause_idle_timeout | Valor, en segundos, de la activación de proceso de inactividad en la máquina que libera motores y hacer perder coordenadas, **es aconsejable un valor alto para que al activar la macro PAUSE tarde suficiente para realizar cualquier acción antes de perder coordenadas.** | número | 43200 |

#### Z-Tilt

Aprovechar al máximo nuestra máquina para que esta se autonivele y facilitar que nuestra máquina siempre esté en las mejores condiciones es fundamental.

**Z-TILT básicamente es un proceso que nos ayuda a alinear nuestros motores de Z con respecto a nuestro eje/gantry X (cartesiana) o XY (CoreXY)**. Con esto **aseguramos que tenemos siempre alineado nuestro Z perfectamente y de forma precisa y automática**.

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_calibrate_z_tilt | Permite, en el caso de tenerlo habilitado en nuestra configuración de Klipper, el proceso de ajuste Z-Tilt | True / False | False |

#### Skew

El uso de [SKEW](broken-reference) para la corrección o ajuste preciso de nuestras impresoras es extremadamente aconsejable si tenemos desviaciones en nuestras impresiones. Usando la siguiente variable podemos permitir el uso en nuestras macros:

| Variable | Descripción | Valores posibles | Valor por defecto |
| --- | --- | --- | --- |
| variable_skew_profile | Permite tener en cuenta nuestro perfil de skew que será cargado en nuestra macro START_PRINT. Para activarlo deberemos des comentar la variable y usar el nombre del perfil de skew de nuestra configuración. | texto | my_skew_profile |

### Personalización de las macros

Nuestro módulo para Klipper emplea el sistema de configuración modular empleado en RatOS y que aprovecha las ventajas de Klipper en el procesado de ficheros de configuración de forma secuencial de este. Por esto es fundamental el orden de los include y ajustes personalizados que queramos aplicar sobre estos módulos.

> ℹ️ **INFO!!!**
>Al usarse como uno módulo las configuraciones de 3Dwork NO pueden editarse directamente desde el directorio 3dwork-klipper dentro de tu directorio de configuración de Klipper dado que estará en read-only (restringido a solo lectura) por seguridad.
>
>Por eso es muy importante entender el funcionamiento de Klipper y como poder personalizar nuestros módulos a tu máquina. 

#### **Personalizando variables**

Normalmente, será lo que tendremos que ajustar, para realizar ajustes sobre las variables que tengamos por defecto en nuestro módulo **3Dwork** para Klipper.

Simplemente, lo que tengamos que hacer es pegar el contenido de la macro **[gcode_macro GLOBAL_VARS]** que podremos encontrar en macros/macros_var_globals.cfg en nuestro printer.cfg.

Os recordamos lo comentado anteriormente de como procesa Klipper las configuraciones de forma secuencial, por lo que es aconsejable pegarlo después de los includes que os comentamos [aquí](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nos quedará algo así (solo es un ejemplo visual):

```ini
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
variable_language: "es" # Possible values: "en", "es"
...

#_# <---------------------- SAVE_CONFIG ----------------------> #_#
#_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#

```

> ⚠️ **Aviso!!!**
>Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.


> ℹ️ **INFO!!!**
>* os aconsejamos añadir comentarios tal como veis en el caso anterior para identificar que hace cada sección
>* aunque no necesites tocar todas las variables te aconsejamos copiar todo el contenido de **[gcode_macro GLOBAL_VARS]**

#### Personalizando macros

Las macros se han montado de una forma modular para que se puedan ajustar de una forma sencilla. Tal como os hemos comentado anteriormente, si queremos ajustarlas deberemos proceder igual que hicimos con las variables, copiar la macro en cuestión en nuestro printer.cfg (u otro include nuestro propio) y asegurarnos que está después del include donde añadimos nuestro módulo 3Dwork para Klipper.

Tenemos dos grupos de macros:

* Macros para añadir ajustes de usuario, estas macros se pueden añadir y personalizar fácilmente porque se añadieron para que cualquier usuario pueda personalizar las acciones a su gusto en determinadas parte de los procesos que hace cada macro.

**START_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| _USER_START_PRINT_HEAT_CHAMBER | Se ejecuta justo después que nuestro cerramiento empiece a calentar, si CHAMBER_TEMP se pasa como parámetro a nuestro START_PRINT |
| _USER_START_PRINT_BEFORE_HOMING | Se ejecuta antes del homing inicial de inicio de impresión |
| _USER_START_PRINT_AFTER_HEATING_BED | Se ejecuta al llegar nuestra cama a su temperatura, antes de _START_PRINT_AFTER_HEATING_BED |
| _USER_START_PRINT_BED_MESH | Se lanza antes de _START_PRINT_BED_MESH |
| _USER_START_PRINT_PARK | Se lanza antes de _START_PRINT_PARK |
| _USER_START_PRINT_AFTER_HEATING_EXTRUDER | Se lanza antes de _START_PRINT_AFTER_HEATING_EXTRUDER |

**END_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| _USER_END_PRINT_BEFORE_HEATERS_OFF | Se ejecuta antes de realizar el apagado de los calentadores, antes de _END_PRINT_BEFORE_HEATERS_OFF |
| _USER_END_PRINT_AFTER_HEATERS_OFF | Se ejecuta después del apagado de los calentadores, antes de _END_PRINT_AFTER_HEATERS_OFF |
| _USER_END_PRINT_PARK | Se ejecuta antes del aparcado del cabezal, antes de _END_PRINT_PARK |

**PRINT_BASICS**

| Nombre Macro | Descripción |
| --- | --- |
| _USER_PAUSE_START | Se ejecuta al inicio de un PAUSE |
| _USER_PAUSE_END | Se ejecuta al finalizar un PAUSE |
| _USER_RESUME_START | Se ejecuta al inicio de un RESUME |
| _USER_RESUME_END | Se ejecuta al finalizar un RESUME |

* Macros internas, son macros para dividir la macro principal en procesos y es importante para este. Es aconsejable que en caso de requerir ajustarse estas se copien tal cual.

**START_PRINT**

| Nombre Macro | Descripción |
| --- | --- |
| _START_PRINT_HEAT_CHAMBER | Calienta el cerramiento en el caso de que el parámetro CHAMBER_TEMP sea recibido por nuestra macro START_PRINT desde el laminador |
| _START_PRINT_AFTER_HEATING_BED | Se ejecuta al llegar la cama a la temperatura, después de _USER_START_PRINT_AFTER_HEATING_BED. Normalmente, se usa para el procesado de calibraciones de cama (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...) |
| _START_PRINT_BED_MESH | Se encarga de la lógica de mallado de cama. |
| _START_PRINT_PARK | Aparca el cabezal de impresión mientras calienta el nozzle a la temperatura de impresión. |
| _START_PRINT_AFTER_HEATING_EXTRUDER | Realiza el purgado del nozzle y carga el perfil SKEW en caso de que así definamos en las variables |

## Impresoras y electrónicas

A medida que trabajemos con diferentes modelos de impresoras y electrónicas iremos añadiendo aquellas que no estén directamente soportadas por RatOS ya sean aportaciones nuestras o de la comunidad.

* printers, en este directorio tendremos todas las configuraciones de impresoras
* boards, aquí encontraremos las de electrónicas

### Parámetros y pines

Nuestro módulo para Klipper emplea el sistema de configuración modular empleado en RatOS y que aprovecha las ventajas de Klipper en el procesado de ficheros de configuración de forma secuencial de este. Por esto es fundamental el orden de los include y ajustes personalizados que queramos aplicar sobre estos módulos.

> ℹ️ **INFO!!!**
>Al usarse como uno módulo las configuraciones de 3Dwork NO pueden editarse directamente desde el directorio 3dwork-klipper dentro de tu directorio de configuración de Klipper dado que estará en read-only (restringido a solo lectura) por seguridad.
>
>Por eso es muy importante entender el funcionamiento de Klipper y como poder personalizar nuestros módulos a tu máquina.

Tal como os explicábamos en "[personalizando macros](3dwork-klipper-bundle.md#personalizando-macros)" usaremos el mismo proceso para ajustar parámetros o pines para ajustarlos a nuestras necesidades.

#### Personalizando parámetros

Tal como os aconsejamos crear un apartado en vuestro printer.cfg que se llame USER OVERRIDES, colocado después de los includes a nuestras configuraciones, para poder ajustar y personalizar cualquier parámetro usado en ellos.

En el siguiente ejemplo veremos como en nuestro caso estamos interesados en personalizar los parámetros de nuestra nivelación de cama (bed_mesh) ajustando los puntos de sondeo (probe_count) con respecto en la configuración que tenemos por defecto en las configuraciones de nuestro módulo Klipper:

**printer.cfg**
```ini

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

#_# <---------------------- SAVE_CONFIG ----------------------> #_#
#_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#
```

> ⚠️ **Aviso!!!**
>Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.

Podemos emplear este mismo proceso con cualquier parámetro que queramos ajustar.

#### Personalizando configuración de pines

Procederemos exactamente tal como hemos hecho anteriormente, en nuestra zona USER OVERRIDES añadiremos aquellas secciones de pins que queramos ajustar a nuestro gusto.

En el siguiente ejemplo vamos a personalizar cual es el pin de nuestro ventilador de electrónica (controller_fan) para asignarlo a uno diferente al de por defecto:

**printer.cfg**
```ini

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

#_# <---------------------- SAVE_CONFIG ----------------------> #_#
#_# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#\*#

```
> ⚠️ **Aviso!!!**
>Los tres puntos (...) de los ejemplos anteriores son meramente para indicar que puedes tener más configuraciones entre secciones... en ningún caso han de ponerse.