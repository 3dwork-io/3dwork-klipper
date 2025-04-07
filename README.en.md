# 3DWORK CLOPE BUNDLE

## Macros package, configurations and other utilities for klipper

![Español](https://flagcdn.com/w40/es.png)[![English](https://flagcdn.com/w40/gb.png)](README.en.md)[![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md)[![Italiano](https://flagcdn.com/w40/it.png)](README.it.md)[![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)[![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ Warning****Guide in process !!!****<span style="color: red">Although macros are totally functional, they are in continuous development.</span>****<span style="color: orange">Use them under your own responsibility !!!</span>**

Changelog

12/07/2023 - Added support to automate the creation of firmware for Bigreteech electronics

From**3Dwork**We have compiled and adjusting a set of macros, machine and electronic configurations, as well as other tools for a simple and powerful management of Klipper.

Much of this package is based on[**Rats**](https://os.ratrig.com/)improving the parties we believe interesting, as well as other contributions from the community.

## Installation

To install our package for Klipper we will follow the following steps

### Discharge of the repository

We will connect to our host by SSH and launch the following commands:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ Use**If the directory of your Klipper configuration is personalized, remember to adjust the first command properly to your installation.

> **ℹ️ Information for new facilities**Since Klipper does not allow access to macros without a valid printer.
>
> 1.  Be sure to have the[host as second MCU](raspberry-como-segunda-mcu.md)
> 2.  Add this basic printer.cfg to enable macros:

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

This will allow Klipper to start and access the macros.

### Using moonraker to always be updated

Thanks to Moonraker we can use its Update_Manager to be able to be up to date with the improvements that we can introduce in the future.

From mainsail/fluidd we will edit our moonraker.conf (it should be at the same height as your printer.cfg) and we will add at the end of the configuration file:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ Warning****Remember to take the installation step previously if you do not generate an error and you will not be able to start.**
>
> **On the other hand, in the event that the Klipper configuration directory is customized, remember to adjust the PATH properly to your installation.**

## Macros

We have always commented that times is one of Klipper's best distributions, with Raspberry support and CB1 modules, largely because of its modular configurations and its great macros.

Some added macros that will be useful:

### **Macros for general use**

| Macro                       | Description                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAYBE_HOME**              | It allows us to optimize the homing process only by doing this in those axes that are not with Homing.                                                           |
| **PAUSE**                   | Through related variables it allows us to manage a pause with a more versatile head parking that normal macros.                                                  |
| **SET_PAUSE_AT_LAYER**      |                                                                                                                                                                  |
| **SET_PAUSE_AT_NEXT_LAYER** | A very useful macro that integrates mainsail into its UI to be able to pause on demand in a specific layer ... In case we forgot when performing the laminate.   |
|                             | We also have another to execute the leisurely in the next layer.                                                                                                 |
| **RESUME**                  | Improved since it allows to detect if our Nozzle is not at the extrusion temperature to be able to solve it before it shows an error and damages our impression. |
| **CANCEL_PRINT**            | Which allows the use of the rest of the macros to carry out an impression cancellation correctly.                                                                |

-   **Paused instead**, very interesting macros that allow us to make a leisurely scheduled in a layer or launch a command when starting the next layer. ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)In addition, another advantage of them is that they are integrated with mainsail with what we will have new functions in our UI as you can see below:![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Print management macros**

| Macro           | Description                                                                                                                                    |   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **START_PRINT** | It will allow us to start our impressions in a safe way and in the Klipper style. Within this we will find some interesting functions such as: |   |
|                 | • Smart nozzle preheating when using a probe sensor                                                                                            |   |
|                 | • Possibility of use of Z-Tilt by variable                                                                                                     |   |
|                 | • Adaptive, forced or from a stored mesh misery                                                                                                |   |
|                 | • Customizable purge line between normal, adaptive purge line or purge drop                                                                    |   |
|                 | • Segmented macro to be able to personalize as we will show you later                                                                          |   |
| **END_PRINT**   | Macro of end of printing where we also have segmentation to customize our macro. We also have dynamic head of the head.                        |   |

-   **Adaptive bed roll**, thanks to the versatility of Klipper we can do things that today seem impossible ... An important process for impression is to have a meal of deviations from our bed that allows us to correct these to have an adherence of the perfect first layers.  
     On many occasions we make this malley before the impressions to ensure that it works correctly and this is done throughout the surface of our bed. 
     With the adaptive bed misery, it will be carried out in the printing zone making it much more precise than the traditional method ... In the following catches we will see the differences of a traditional and an adaptive mesh.
    <div style="display: flex; justify-content: space-between;">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
    </div>

### **FILAMENT MANAGEMENT MACROS**

Set of macros that will allow us to manage different actions with our filament such as the load or discharge of this.

| Macro               | Description                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| **The M600**        | It will allow us compatibility with the M600 GCODE normally used in laminators for the change of filament. |
| **UNLOAD_FILAMENT** | Configurable through the variables will allow us to download assisted filaments.                           |
| **LOAD_FILAMENT**   | As well as the previous one but related to the load of the filament.                                       |

### **Filament coil management macros (Spoolman)**

> **⚠️ Warning****Section in process !!!**

[**Spoolman**](https://github.com/Donkie/Spoolman)He is a filament coil manager that is integrated into Moonraker and that allows us to manage our stock and availability of filaments.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

We are not going to enter the installation and configuration of this since it is relatively simple using the[**Instructions of your github**](https://github.com/Donkie/Spoolman)**,** en cualquier caso **We advise you to use Docker**By simplicity and remembrance**activate the configuration in Moonraker**required:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro              | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| SET_ACTIVE_SPOOL   | It allows us to indicate which is the ID of the coil to use |
| CLEAR_ACTIVE_SPOOL | Allows us to reset the active coil                          |

The ideal in each case would be to add in our laminator,**In the filament gcodes for each coil the call to this**, and remember**Change the ID of this once consumed**to be able to control the remainder of filament in it !!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Print surface management macros**

> **⚠️ Warning****Section in process !!!**

It is usually normal for us to have different printing surfaces depending on the finish we want to have or the type of filament.

This set of macros, created by[Garethky](https://github.com/garethky), they will allow us to have a control of these and especially the correct adjustment of Zoffset in each of them in the style that we have in Prussa machines. Below you can see some of your functions:

-   We can store the number of print surfaces we want, each having a unique name
-   Each printing surface will have its own zoffset
-   If we make Z settings during an impression (Babystepping) from our klipper this change is going to warehouse on the surface enabled at that time

On the other hand we have some**Requirements to implement it (it will be tried to add in the logic of the Bundle print**:

-   The use of**[save_variables]**, in our case we will use ~/variables.cfg to store the variables and that is already within the CFG of these macros.  
    This will automatically create a variables_build_sheets.cfg file where our disk variables will keep.

**Ejemplo de archivo de configuración de variables**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

-   We must include a call to apply_build_sheet_adjustment in our print_start to be able to apply the selected surface zoffset
-   It is important that for the anterior macro, apply_build_sheet_adjustment, it works properly we must add a set_gcode_offset z = 0.0 just before calling apply_build_sheet_adjustment


    # Load build sheet
    SHOW_BUILD_SHEET ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset

On the other hand it is interesting to be able to have some macros to activate one surface or another or even pass it as a parameter from our laminator to different printer or filament profiles to be able to load one or the other automatically:

> **⚠️ Warning**It is important that the value in name = "xxxx" coincides with the name we gave when installing our printing surface

\*\*printer.cfg

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

Also in the case of having Klipperscreen we can add a specific menu to be able to manage the load of the different surfaces, where we will include a call to the macros previously created for the loading of each surface:

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

| Macro                        | Description |
| ---------------------------- | ----------- |
| INSTALL_BUILD_SHEET          |             |
| SHOW_BUILD_SHEET             |             |
| SHOW_BUILD_SHEETS            |             |
| SET_BUILD_SHEET_OFFSET       |             |
| RESET_BUILD_SHEET_OFFSET     |             |
| SET_GCODE_OFFSET             |             |
| APPLY_BUILD_SHEET_ADJUSTMENT |             |

### **Machine Macros**

| Macro                                                  | Description                                                                                                                                                                                                   |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILE_FIRMWARE**                                   | With this macro we can compile the Klipper firmware in a simple way, have the firmware accessible from the UI for greater simplicity and be able to apply it to our electronics.                              |
| Here you have more detail of the electronic supported. |                                                                                                                                                                                                               |
| **CALCULATE_BED_MESH**                                 | An extremely useful macro for calculating the area for our mesh because sometimes it can be a complicated process.                                                                                            |
| **PID_ALL**                                            |                                                                                                                                                                                                               |
| **PID_EXTRUDER**                                       |                                                                                                                                                                                                               |
| **PID_BED**                                            | These macros, where we can pass the temperatures for the PID in the form of parameters, will allow us to be able to perform the temperature calibration in an extremely simple way.                           |
| **TEST_SPEED**                                         |                                                                                                                                                                                                               |
| **TEST_SPEED_DELTA**                                   | Original Macro of the partner[Ellis](https://github.com/AndrewEllis93)They will allow us in a quite simple way to test the speed at which we can move our machine in a precise way and without loss of steps. |

\*\_**Firmware compilation for supported electronics**, To facilitate the process of creation and maintenance of our Klipper firmware for our MCU we have the macro compile_firmware that when executing it, we can use our electronics as a parameter to do only this, Klipper will compile for all electronics supported by our Bundle:![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)We will find these accessible in a simple way from our UI website in the Firmware_binaries directory in our Machine tab (if we use mainsail):![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)Then you have the list of supported electronic:

> ⚠️**IMPORTANT!!!**
>
> These scripts are prepared to work on a> Raspbian system with Pi user, if you are not your case you must adapt it.
>
> Firmwares are generated for use with USB connection that is always what we advise, in addition the USB assembly point is always the same by what your configuration of your MCU connection will not change if they are generated with our macro/script
>
> **So that Klipper can execute Shell Macros, an extension must be installed, thanks to the partner**[**Arksine**](https://github.com/Arksine)**, let it.**
>
> **Depending on used klipper dystro they can already be enabled.**
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> The simplest way is using[**Kioh**](../instalacion/#instalando-kiauh)Where we will find in one of your options the possibility of installing this extension:
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> We can also perform the process by hand we will manually copy the plugin for klipper &lt;[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)within our directory`_**~/klipper/klippy/extras**_`Using SSH SCP Y We restart Klipper.

| Electronic         | Parameter name to use in macro |
| ------------------ | ------------------------------ |
| Manta E3 No        | I am proud                     |
| Manta M4P          | btt-manta-m4p                  |
| Manta M4P V2.      | btt-manta-m4p-22               |
| Manta M8P          | btt-manta-m8p                  |
| Manta m8p v1.1     | btt-manta-m8p-11               |
| Octopus max this   | btt-octopus-max-ez             |
| Octopus Pro (446)  | btt-octopus-pro-446            |
| Octopus Pro (429)  | btt-octopus-pro-429            |
| Octopus Pro (H723) | btt-octopus-pro-h723           |
| Octopus v1.1       | btt-octopus-11                 |
| Octopus v1.1 (407) | btt-octopus-11-407             |
| SKR Pro v1.2       | Skr_Pro_12                     |
| SKR 3              | btt screw 3                    |
| Saqr A (Heha)      | Smarted                        |
| SKR 3 this         | BTT-SC-3-EZ                    |
| SKR 3 this (H723)  | Skirzhahah                     |
| SKR 2 (429)        | BTT-SRC-2-429                  |
| SKR 2 (407)        | BTT-SRC-2-407                  |
| Screams            | BTT-SKRA-10                    |
| By 1.4 Turbo       | BTT-SC-14-TURBO                |
| Skri mini          | btt_skr_mini_e3_30             |

| Toolhead (CAN) | Parameter name to use in macro |
| -------------- | ------------------------------ |
| EBB42 V1       | BTT EBB42 10                   |
| Ebb36 v1       | BTT_BB36_10                    |
| EBB42 V1.1     | BTT EBB42 11                   |
| Ebb36 v1.1     | BTT_BB36_11                    |
| EBB42 V1.2     | BTT EBB42 12                   |
| Ebb36 v1.2     | BTT_BB36_12                    |

| **Electronic**       | **Parameter name to use in macro** |
| -------------------- | ---------------------------------- |
| MKS Eagle v1.x       | mks-eagle-10                       |
| MCS Robin Nano Baked | mks-robin-nano-30                  |
| MKS Robin Nano v2    | mks-robin-nano-20                  |
| MKS Gen L            | mks-gen-l                          |
| ZNP Robin Nano DW V2 | znp_robin_nano_dw_v2               |

| Toolhead (CAN)    | Parameter name to use in macro |
| ----------------- | ------------------------------ |
| Mellow FLY SHT 42 | mellow_fly_sht_42              |
| Mellow FLY SHT 36 | mellow_fly_sht_36              |

| Electronic    | Parameter name to use in macro |
| ------------- | ------------------------------ |
| Fysetc Spider | fysetc_spider                  |

| Electronic          | Parameter name to use in macro |
| ------------------- | ------------------------------ |
| Artillery Ruby v1.x | artillery-ruby-12              |

| Electronic            | Parameter name to use in macro |
| --------------------- | ------------------------------ |
| Raspberry Pico/RP2040 | rpi-rp2040                     |

| Electronic     | Parameter name to use in macro |
| -------------- | ------------------------------ |
| Leviathan v1.2 | leviathan-12                   |

### Adding 3Dwork macros to our installation

From our interface, mainsail/fluidd, we will edit our printer.cfg and add:

**printer.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️**INFO!!!**It is important that we add these lines at the end of our configuration file ... just above the section so that in the case of macros in our CFG or include these are overwhelmed by ours: 
> \#\*# \\&lt;--- SAVE_CONFIG --->

> ⚠️**IMPORTANT!!!**Normal macros have been separated from**macros shell**given that**To enable these it is necessary to make additionally manual steps that are currently testing**y\*\*They may require extra permissions to attribute execution permissions for which the instructions have not been indicated since it is trying to automate.\*\***If you use them it is under your own responsibility.**

### Settings of our Laminator

Since our macros are dynamic they will extract certain information from our printer configuration and the laminator itself. To do this we advise you to configure your laminators as follows:

-   **GCode start start_print**, using Placeholders to pass the filament and bed temperature values ​​dynamically:

**PrusaSlicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer**- We have the option to adjust the enclosure temperature (Chamber)

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

**Studio/Orcaslicer bamboo**

```ini
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

**Treatment**

```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

> ⚠️**Notice!!!**We must install the plugin[**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)From the menu_**Help/Show**_Configuration Folder ... We will copy the previous link script inside the script folder.  
> We restart cure and we will go to_**Extensions/Post processing/Modify G-Code**_And we will select_**Mesh Print Size**_.

**IdeaMaker**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplify3D**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️**INFO!!!**Los**Placeholders are "aka" or variable**of printing.
>
> In the following links you can find a list of these for:[**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(in addition to those of the previous one),[**Studio Bamboo**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)y[**Treatment**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> The use of these allow our macros to be dynamic.

-   **gcode de final END_PRINT**, in this case when not using pleaceholders it is common to all laminators

```ini
END_PRINT
```

### Variables

As we have already mentioned, these new macros will allow us to have some very useful functions as we list previously.

For the adjustment of these to our machine we will use the variables that we will find in macros/macros_var_globals.cfg and that we detail below.

#### Message/Notifications Language

Since many users like to have the notifications of macros in their language we have devised a multi-language notification system, currently Spanish (s) and English (en). In the following variable we can adjust it:

| Variable          | Description                                                                                                               | Possible values | Default value |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_language | It allows us to select the language of notifications. In the case of not being well defined, it will be used in (English) | It is / in      | es            |

#### Relative extrusion

It allows to control what extrusion mode we will use at the end of our start_print. The value will depend on the configuration of our laminator.

> 💡**Advice**It is advisable to configure your laminator for the use of relative extrusion and adjust this variable to True.

| Variable                    | Description                                                        | Possible values | Default value |
| --------------------------- | ------------------------------------------------------------------ | --------------- | ------------- |
| variable_relative_extrusion | It allows us to indicate the extrusion mode used in our laminator. | True / False    | True          |

#### Velocities

To manage the speeds used in macros.

| Variable                    | Description                      | Possible values | Default value |   |
| --------------------------- | -------------------------------- | --------------- | ------------- | - |
| variable_macro_travel_speed | Speed ​​in translated            | numeric         | 150           |   |
| variable_macro_z_speed      | Speed ​​in translated for z axis | numeric         | 15            |   |

#### Homing

Set of variables related to the homing process.

| Variable | Description | Possible values | Default value |
| -------- | ----------- | --------------- | ------------- |

#### Heating

Variables related to the heating process of our machine.

| Variable                                   | Description                                                                               | Possible values | Default value |
| ------------------------------------------ | ----------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_preheat_extruder                  | Enable the preheated nozzle at the temperature indicated in variable_preheat_xtruder_temp | True / False    | True          |
| variable_preheat_extruder_temp             | Nozzle preheated temperature                                                              | numeric         | 150           |
| variable_start_print_heat_chamber_bed_temp | Bed temperature during the process of heating our enclosure                               | numeric         | 100           |

> 💡**Advice**Benefits of using the preheated Nozzle:

-   It allows us additional time for the bed to reach its temperature in a uniform way
-   If we use an indictive sensor that does not have temperature compensation, it will allow us to make our measures more consistent and precise
-   It allows to soften any rest of the filament in the Nozzle which allows, in certain configurations, these remains do not affect the activation of the sensor 
    { % endhint %}

#### Bed Mali (Bed Mesh)

To control the leveling process we have variables that can be very useful. For example, we can control the type of leveling that we want to use by creating a new mesh always, loading a previously stored or using an adaptive mesh.

| Variable                                                                                                            | Description                                                                | Possible values | Default value |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------- | ------------- |
| variable_calibrate_bed_mesh                                                                                         | It allows us to select what type of misery we will use in our start_print: |                 |               |
| - New Mesh, will make us a misery in each impression                                                                |                                                                            |                 |               |
| - StoredMeh, will load a stored mesh and will not perform the bed poll                                              |                                                                            |                 |               |
| - Adaptive, will make us a new misery but adapted to the printing zone improving our first layers on many occasions |                                                                            |                 |               |
| -Nomesh, in the case that we do not have a sensor or use the process to skip the process                            | newmesh / storedmesh / adaptative /                                        |                 |               |
| noma                                                                                                                | adaptive                                                                   |                 |               |
| variable_bed_mesh_profile                                                                                           | The name used for our stored mesh                                          | text            | default       |

> ⚠️**Notice!!!**We advise you to use the adaptive level since it will always adjust the misery to the size of our impression allowing you to have an adjusted malle area.
>
> It is important that we have in our[start -up gcode](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), in the call to our start_print, the print_max and print_min values.

#### Purged

An important phase of our beginning of printing is a correct purge of our Nozzle to avoid remains of filament or that they can damage our impression at some point. Then you have the variables involved in this process:
| Variable | Description | Possible values ​​| Default value |
\| --- \| --- \| --- \| --- \|
| Variable_NoZZLE_PRIMING | We can choose between different purity options:<br>- Primelline: Draw the typical purged line<br>- Primellineadaptive: generates a purge line adapted to the printing zone using variable_nazzle_priming_objectdistance as margin<br>- Primoblob: makes a drop of filament in a corner of the bed | Primelline / Primellineadaptive / Primeblob / False | Primelineadaptative |
| Variable_NoZZLE_PRIMING_OBJECTDISTANCE | If we use adaptive purge line, it will be the margin to be used between the purge line and the printed object | numerical | 5 |
| Variable_NoZZLE_PRIME_START_X | Where to locate our purge line in X:<br>- Min: x = 0 (more security margin)<br>- Max: X = Max (less security room)<br>- Number: Specific X coordinate | min / max / number | Max |
| Variable_NoZZLE_PRIME_START_Y | Where to locate our purge line in Y:<br>- Min: y = 0 (more security margin)<br>- Max: y = Max (less security room)<br>- Number: coordinate and specific | min / max / number | min |
| Variable_NoZZLE_PRIME_DIRECTION | Line or drop address:<br>- Backwards: towards the front<br>- Forwards: backward<br>- Auto: Towards the center according to variable_nazzle_prime_start_y | AUTO / FORWARDS / BACKWARDS | Auto |

#### Filming load/discharge

In this case, this group of variables will facilitate the management of loading and discharge of our filament used in emulation of the M600 for example or by launching the loading and discharge macros of filament:

| Variable                        | Description                                                                                                                                                                                                                                                                                                                                                                 | Possible values | Default value |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_filament_unload_length | How much withdraw in mm the filament, adjust to your machine, normally the measure from your nozzle to the gears of your extruder by adding an extra margin.                                                                                                                                                                                                                | number          | 130           |
| variable_filament_unload_speed  | Retraction speed of the filament in mm/sec normally a slow speed is used.                                                                                                                                                                                                                                                                                                   | number          | 5             |
| variable_filament_load_length   | Distance in mm to load the new filament ... As in variable_filament_unload_length we will use the measure from your extruder gear adding an extra margin, in this case this extra value will depend on how much you want to be purged ... you can usually give it more margin than the previous value to ensure that it is cleansed the extrusion of the anterior filament. | number          | 150           |
| variable_filament_load_speed    | Filament load speed in mm/sec Normally a faster speed is used to discharge.                                                                                                                                                                                                                                                                                                 | number          | 10            |

> ⚠️**Notice!!!**Another adjustment necessary for your section**[extruder]**the indicated[**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... The advisable value is usually> 101 (if it is not defined uses 50) to for example allow the typical extruder calibration tests.  
> You should adjust the value based on the above of the test or the configuration of your**variable_filament_unload_length**I**variable_filament_load_length**.

#### Parking

In certain processes of our printer, such as the leisure, it is advisable to make a parking lot of our head. The macros of our Bundle have this option in addition to the following variables to manage:

| Variable                           | Description                                                                                                                                                                                                                                     | Possible values | Default value |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_start_print_park_in       | Location where to park the head during the pre-scallion.                                                                                                                                                                                        | back /          |               |
| center /                           |                                                                                                                                                                                                                                                 |                 |               |
| front                              | back                                                                                                                                                                                                                                            |                 |               |
| variable_start_print_park_z_height | Z height during pre-heavy                                                                                                                                                                                                                       | number          | 50            |
| variable_end_print_park_in         | Location to park the head at the end or cancel an impression.                                                                                                                                                                                   | back /          |               |
| center /                           |                                                                                                                                                                                                                                                 |                 |               |
| front                              | back                                                                                                                                                                                                                                            |                 |               |
| variable_end_print_park_z_hop      | Distance to go up at the end of the impression.                                                                                                                                                                                                 | number          | 20            |
| variable_pause_print_park_in       | Location to park the head by pausar the impression.                                                                                                                                                                                             | back /          |               |
| center /                           |                                                                                                                                                                                                                                                 |                 |               |
| front                              | back                                                                                                                                                                                                                                            |                 |               |
| variable_pause_idle_timeout        | Value, in seconds, of the activation of the process of inactivity in the machine that releases engines and losing coordinates,**A high value is advisable to activate the pause macro enough to perform any action before losing coordinates.** | number          | 43200         |

#### Z-Tilt

Take the most of our machine so that it is self -level and facilitate that our machine is always in the best conditions is essential.

**Z-Tilt is basically a process that helps us align our Z engines with respect to our/Gantry X (Cartesian) or XY (Corexy) axis (Corexy)**. With this**We assure that we always have our z perfectly and in a precise and automatic way**.

| Variable                  | Description                                                                                             | Possible values | Default value |
| ------------------------- | ------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_calibrate_z_tilt | It allows, in the case of having it enabled in our Klipper configuration, the Z-Tilt adjustment process | True / False    | False         |

#### Skew

The use of[SKEW](broken-reference)For the correction or precise adjustment of our printers it is extremely advisable if we have deviations in our impressions. Using the following variable we can allow use in our macros:

| Variable              | Description                                                                                                                                                                                              | Possible values | Default value   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --------------- |
| variable_skew_profile | It allows us to take into account our SKEW profile that will be charged in our Macro Start_Print. To activate it we must discuss the variable and use the name of the SKEW profile of our configuration. | text            | my_skew_profile |

### Customization of macros

Our Klipper module uses the modular configuration system used in times and takes advantage of Klipper's advantages in the configuration file process sequentially. This is why the order of the include and personalized adjustments that we want to apply on these modules are essential.

> ℹ️**INFO!!!**When using 3DWork settings as a module, they cannot be edited directly from the 3DWork-Klipper directory within your Klipper configuration directory since it will be in Read-only (restricted to only reading) for safety.
>
> That is why it is very important to understand Klipper's functioning and how to customize our modules to your machine.

#### **Personalizing variables**

Normally, it will be what we will have to adjust, to make adjustments on the variables that we have by default in our module**3Dwork**Para cuts.

Simply, what we have to do is paste the macro content**[gcode_macro GLOBAL_VARS]**that we can find in macros/macros var globals.cfg in our printer.cfg.

We remind you what was previously commented on how Klipper processes the configurations sequentially, so it is advisable to paste it after the includs we tell you[here](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

We will have something like that (it is only a visual example):

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

> ⚠️**Notice!!!**The three points (...) of the previous examples are merely to indicate that you can have more configurations between sections ... in no case should they wear.

> ℹ️**INFO!!!**
>
> -   We advise you to add comments as you see in the previous case to identify what each section makes
> -   Although you do not need to touch all the variables we advise you to copy the entire content of**[gcode_macro GLOBAL_VARS]**

#### Personalizing Macros

Macros have mounted in a modular way so that they can be adjusted in a simple way. As we have mentioned before, if we want to adjust them we must proceed just as we did with the variables, copy the macro in question in our printer.cfg (or other include our own) and make sure that it is after the include where we add our 3DWork module for Klipper.

We have two groups of macros:

-   Macros To add user settings, these macros can be easily added and customized because they were added so that any user can customize the actions to their liking in certain part of the processes that each macro does.

**START_PRINT**

| Macro name                                | Description                                                                                                  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| \_USER_START_PRINT_HEAT_CHAMBER           | It runs just after our enclosure starts to heat, if Chamber_Temp is passed as a parameter to our start_print |
| \_USER_START_PRINT_BEFORE_HOMING          | It is executed before the initial homing for the start of printing                                           |
| \_USER_START_PRINT_AFTER_HEATING_BED      | It runs when our bed arrives at its temperature, before \_start_print_after_heating_bed                      |
| \_USER_START_PRINT_BED_MESH               | It is launched before \_start_print_bed_mesh                                                                 |
| \_USER_START_PRINT_PARK                   | It is launched before \_start_print_park                                                                     |
| \_USER_START_PRINT_AFTER_HEATING_EXTRUDER | Se lanza antes de \_START_PRINT_AFTER_HEATING_EXTRUDER                                                       |

**END_PRINT**

| Macro name                          | Description                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------- |
| \_USER_END_PRINT_BEFORE_HEATERS_OFF | It is executed before performing the heater, before \_end_print_before_heaters_off |
| \_USER_END_PRINT_AFTER_HEATERS_OFF  | It runs after heating, before \_end_print_after_heaters_off                        |
| \_USER_END_PRINT_PARK               | It is executed before the head of the head, before \_end_print_park                |

**PRINT_BASICS**

| Macro name          | Description                               |
| ------------------- | ----------------------------------------- |
| \_USER_PAUSE_START  | Is executed at the beginning of a pause   |
| \_USER_PAUSE_END    | It runs at the end of a pause             |
| \_USER_RESUME_START | Is executed at the beginning of a summary |
| \_USER_RESUME_END   | Runs at the end of a summary              |

-   Internal macros, they are macros to divide the main macro into processes and is important for this. It is advisable that in case of requiring these are copied as is.

**START_PRINT**

| Macro name                           | Description                                                                                                                                                                             |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_START_PRINT_HEAT_CHAMBER           | Heats the enclosure in the event that the Chamber_Temp parameter is received by our Macro Start_print from the Laminator                                                                |
| \_START_PRINT_AFTER_HEATING_BED      | It runs when the bed arrives at temperature, after \_user_start_print_after_heating_bed. Normally, it is used for bed calibration processing (Z_Tilt_adjust, quad_gantry_leveling, ...) |
| \_START_PRINT_BED_MESH               | He is in charge of the logic of bed misery.                                                                                                                                             |
| \_START_PRINT_PARK                   | Appeals the print head while heating the nozzle at the print temperature.                                                                                                               |
| \_START_PRINT_AFTER_HEATING_EXTRUDER | Make the Nazzle purge and load the SKEW profile in case we define in the variables                                                                                                      |

## Printers and electronic

As we work with different models of printers and electronic we will add those that are not directly supported by times whether they are contributions or the community.

-   Printers, in this directory we will have all the configurations of printer
-   Boards, here we will find electronics

### Parameters and pins

Our Klipper module uses the modular configuration system used in times and takes advantage of Klipper's advantages in the configuration file process sequentially. This is why the order of the include and personalized adjustments that we want to apply on these modules are essential.

> ℹ️**INFO!!!**When using 3DWork settings as a module, they cannot be edited directly from the 3DWork-Klipper directory within your Klipper configuration directory since it will be in Read-only (restricted to only reading) for safety.
>
> That is why it is very important to understand Klipper's functioning and how to customize our modules to your machine.

As we explained in "[Personalizing Macros](3dwork-klipper-bundle.md#personalizando-macros)"We will use the same process to adjust parameters or pins to adjust them to our needs.

#### Personalizing parameters

As we advise you to create a section in your printer.cfg that is called User Overrides, placed after the include to our configurations, to be able to adjust and customize any parameter used in them.

In the following example we will see how in our case we are interested in customizing the parameters of our bed leveling (Bed_MEH) adjusting the survey points (probe_count) with respect to the configuration we have by default in the configurations of our Klipper module:

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

> ⚠️**Notice!!!**The three points (...) of the previous examples are merely to indicate that you can have more configurations between sections ... in no case should they wear.

We can use this same process with any parameter we want to adjust.

#### Customizing pine configuration

We will proceed exactly as we have done before, in our User Overrides area we will add those sections of Pins that we want to adjust to our liking.

In the following example we will customize what is the pin of our electronics fan (Controller_FAN) to assign it to a different one from default:

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

> ⚠️**Notice!!!**The three points (...) of the previous examples are merely to indicate that you can have more configurations between sections ... in no case should they wear.
