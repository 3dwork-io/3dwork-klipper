# 3Dwork Klipper Bundle ![English](https://flagcdn.com/w40/gb.png)

## Bundle of macros, configurations, and other utilities for Klipper

[![Espñol](https://flagcdn.com/w40/es.png)](README.md) [![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md) [![Italiano](https://flagcdn.com/w40/it.png)](README.it.md) [![Français](https://flagcdn.com/w40/fr.png)](README.fr.md) [![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)


[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ WARNING**
> **GUIDE IN PROGRESS\!\!\!** **<span style="color: red">Although the macros are fully functional, they are under continuous development.</span>**
> **<span style="color: orange">Use them at your own risk\!\!\!</span>**

Changelog

07/12/2023 - Added support for automating firmware creation for Bigtreetech electronics

From **3Dwork**, we have compiled and adjusted a set of macros, machine and electronics configurations, as well as other tools for simple and powerful Klipper management.

Much of this package is based on [**RatOS**](https://os.ratrig.com/), improving the parts we find interesting, as well as incorporating other contributions from the community.

## Installation

To install our Klipper package, follow these steps:

### Download the repository

Connect to your host via SSH and run the following commands:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTE**
> If your Klipper configuration directory is customized, remember to adjust the first command accordingly for your setup.
>
> **ℹ️ INFORMATION FOR NEW INSTALLATIONS**
> Since Klipper does not allow access to macros without a valid printer.cfg and a connection to an MCU, you can use this temporary configuration:

 1.  Make sure you have the [host as a secondary MCU](raspberry-como-segunda-mcu.md)
 2.  Add this basic printer.cfg to enable the macros:

 <!-- end list -->

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

### Using Moonraker to stay updated

Thanks to Moonraker, we can use its `update_manager` to stay up-to-date with improvements we may introduce in the future.

From Mainsail/Fluidd, edit your `moonraker.conf` (it should be located in the same directory as your `printer.cfg`) and add the following at the end of the configuration file:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ WARNING**
> **Remember to perform the installation step first, otherwise Moonraker will generate an error and fail to start.**
>
> **Additionally, if your Klipper configuration directory is customized, remember to adjust the path accordingly for your installation.**

## Macros

We have always mentioned that RatOS is one of the best Klipper distributions, supporting Raspberry Pi and CB1 modules, largely due to its modular configurations and excellent macros.

Some added macros that will be useful:

### **General Use Macros**

| Macro                     | Description                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAYBE\_HOME** | Allows us to optimize the homing process by only homing axes that are not already homed.                                                             |
| **PAUSE** | Using related variables, it allows managing a pause with more versatile toolhead parking than standard macros.                                     |
| **SET\_PAUSE\_AT\_LAYER** |                                                                                                                                                    |
| **SET\_PAUSE\_AT\_NEXT\_LAYER** | A very useful macro integrated into the Mainsail UI to perform an on-demand pause at a specific layer... in case you forgot during slicing.         |
|                           | We also have another one (`SET_PAUSE_AT_NEXT_LAYER`) to execute the pause on the next layer.                                                              |
| **RESUME** | Improved to detect if the nozzle is not at extrusion temperature, allowing it to be corrected before showing an error and potentially damaging the print. |
| **CANCEL\_PRINT** | Allows using other macros to perform a print cancellation correctly.                                                                               |

 **Layer Change Pause**, very interesting macros (`SET_PAUSE_AT_LAYER`, `SET_PAUSE_AT_NEXT_LAYER`) that allow us to schedule a pause at a specific layer or run a command when the next layer starts.
![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)
    Another advantage is that they are integrated with Mainsail, giving us new functions in our UI as you can see below:
![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Print Management Macros**

| Macro         | Description                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| **START\_PRINT** | Allows us to start our prints safely in the Klipper style. It includes some interesting features such as: |
|               | • Smart nozzle preheating when using a probe sensor                                                         |
|               | • Option to use z-tilt via variable                                                                         |
|               | • Adaptive bed meshing, forced meshing, or using a saved mesh                                               |
|               | • Customizable purge line (normal, adaptive purge line, or purge blob)                                      |
|               | • Segmented macro for easy customization, as shown later                                                    |
| **END\_PRINT** | End print macro, also segmented for customization. Includes dynamic toolhead parking.                       |

  * **Adaptive bed meshing**, thanks to Klipper's versatility, we can do things that seem impossible today... an important process for printing is having a mesh of our bed's deviations to correct them for perfect first-layer adhesion.
    Often, we perform this mesh before prints to ensure it works correctly, and it's done over the entire bed surface.
    With adaptive bed meshing, the mesh is performed only in the print area, making it much more precise than the traditional method... in the following captures, we'll see the differences between a traditional mesh and an adaptive one.
      <div style="display: flex; justify-content: space-between;">
       <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
       <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
      </div>

### **Filament Management Macros**

Set of macros that allow us to manage different actions with our filament, such as loading or unloading it.

| Macro             | Description                                                                           |
| ----------------- | ------------------------------------------------------------------------------------- |
| **M600** | Provides compatibility with the M600 gcode, commonly used in slicers for filament changes. |
| **UNLOAD\_FILAMENT** | Configurable via variables, allows for assisted filament unloading.                 |
| **LOAD\_FILAMENT** | Same as above, but related to filament loading.                                       |

### **Filament Spool Management (Spoolman) Macros**

> **⚠️ WARNING**
> **SECTION IN PROGRESS\!\!\!**

[**Spoolman**](https://github.com/Donkie/Spoolman) is a filament spool manager that integrates with Moonraker and allows us to manage our filament stock and availability.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

We won't detail its installation and configuration as it's relatively simple using the [**instructions on its Github**](https://github.com/Donkie/Spoolman). In any case, **we recommend using Docker** for simplicity, and remember to **activate the required configuration in Moonraker**:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro                | Description                                 |
| -------------------- | ------------------------------------------- |
| SET\_ACTIVE\_SPOOL   | Allows us to specify the ID of the spool to use |
| CLEAR\_ACTIVE\_SPOOL | Allows us to reset the active spool           |

Ideally, you should add the call to this macro (`SET_ACTIVE_SPOOL ID=X`) in your slicer, **within the filament gcode settings for each spool**, and remember to **change its ID once consumed** to keep track of the remaining filament\!\!\!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Print Surface Management Macros**

> **⚠️ WARNING**
> **SECTION IN PROGRESS!!!**

It's common to have different print surfaces (build sheets) depending on the desired finish or the type of filament.

This set of macros, created by [Garethky](https://github.com/garethky), allows us to manage these surfaces and, especially, the correct Z-Offset adjustment for each one, similar to how it's done on Prusa machines. Below are some of its functions:

* We can store as many build sheets as we want, each with a unique name.
* Each build sheet will have its own Z-Offset.
* If we make Z adjustments during a print (Babystepping) from Klipper, this change will be saved to the currently enabled build sheet.

On the other hand, there are some **requirements for implementation (we will try to add this logic to the bundle's PRINT_START in the future, enabling it via a variable and creating pre/post user macros for custom events)**:

* The use of **`[save_variables]`** is required. In our case, we will use `~/variables.cfg` to store the variables, which is already included in the config for these macros.
    This will automatically create a `variables_build_sheets.cfg` file where our variables will be saved to disk.

**Example variable configuration file (`variables_build_sheets.cfg`)**
```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
````

  * We must include a call to `APPLY_BUILD_SHEET_ADJUSTMENT` in our `PRINT_START` macro to apply the Z-Offset of the selected build sheet.
  * It is important that for the previous macro, `APPLY_BUILD_SHEET_ADJUSTMENT`, to work correctly, we must add a `SET_GCODE_OFFSET Z=0.0` right before calling `APPLY_BUILD_SHEET_ADJUSTMENT`.

<!-- end list -->

```gcode
# Load build sheet
SHOW_BUILD_SHEET ; show loaded build sheet on console
SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset
```

Furthermore, it's useful to have macros to activate one surface or another, or even pass it as a parameter from our slicer, so that different printer or filament profiles can automatically load the corresponding build sheet:

> **⚠️ WARNING**
> It is important that the value in `NAME="xxxx"` matches the name assigned when installing the build sheet.

**printer.cfg**

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

Also, if you use KlipperScreen, you can add a specific menu to manage the loading of different surfaces, where we will include a call to the previously created macros for loading each surface:

**\~/printer\_data/config/KlipperScreen.conf**

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
| INSTALL\_BUILD\_SHEET          |             |
| SHOW\_BUILD\_SHEET             |             |
| SHOW\_BUILD\_SHEETS            |             |
| SET\_BUILD\_SHEET\_OFFSET       |             |
| RESET\_BUILD\_SHEET\_OFFSET     |             |
| SET\_GCODE\_OFFSET             |             |
| APPLY\_BUILD\_SHEET\_ADJUSTMENT |             |

*(Note: Descriptions for the build sheet macros were not provided in the original text)*

### **Machine Configuration Macros**

| Macro                | Description                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILE\_FIRMWARE** | With this macro, we can compile Klipper firmware easily, have the firmware accessible from the UI for simplicity, and apply it to our electronics/board.                             |
|                      | More details on supported electronics are available below.                                                                                                                       |
| **CALCULATE\_BED\_MESH** | An extremely useful macro to calculate the area for our bed mesh, as this process can sometimes be complicated.                                                                  |
| **PID\_ALL** |                                                                                                                                                                                  |
| **PID\_EXTRUDER** |                                                                                                                                                                                  |
| **PID\_BED** | These macros, where we can pass PID temperatures as parameters, allow us to perform temperature calibration (PID tuning) in an extremely simple way.                             |
| **TEST\_SPEED** |                                                                                                                                                                                  |
| **TEST\_SPEED\_DELTA** | This macro, originally from [Ellis](https://github.com/AndrewEllis93), allows us to easily test the speed at which we can move our machine precisely and without losing steps. |

\*\_ **Firmware compilation for supported electronics**, to facilitate the process of creating and maintaining our Klipper firmware for our MCUs, we have the `COMPILE_FIRMWARE` macro. When executed (you can use the board name as a parameter to compile only for that specific board), it will compile Klipper for all electronics supported by our bundle:
![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)
We will find these easily accessible from our web UI in the `firmware_binaries` directory under the MACHINE tab (if using Mainsail):
![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)
Below is the list of supported electronics:

> ⚠️ **IMPORTANT\!\!\!**
>
>   * These scripts are prepared to run on a Raspbian system with the user `pi`. If this is not your case, you will need to adapt them.
>   * The firmwares are generated for use with a USB connection, which we always recommend. Additionally, the USB mount point is always the same, so your MCU connection configuration will not change if generated with our macro/script.
>   * **For Klipper to execute shell macros, an extension must be installed, thanks to contributor** [**Arksine**](https://github.com/Arksine)**.**
>   * **Depending on the Klipper distribution used, they may already be enabled.**
>
>![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> The easiest way is using [**Kiauh**](../instalacion/#instalando-kiauh), where you will find an option to install this extension:
>
>![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> You can also perform the process manually: copy the plugin for Klipper \<[**gcode\_shell\_command.py**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)\> manually into your `_**~/klipper/klippy/extras**_` directory using SSH or SCP and restart Klipper.

| Electronics        | Parameter name to use in macro |
| ------------------ | ------------------------------ |
| Manta E3 EZ        | btt-manta-e3ez                 |
| Manta M4P        | btt-manta-m4p                  |
| Manta M4P v2.2     | btt-manta-m4p-22               |
| Manta M8P        | btt-manta-m8p                  |
| Manta M8P v1.1     | btt-manta-m8p-11               |
| Octopus Max EZ     | btt-octopus-max-ez             |
| Octopus Pro (446)  | btt-octopus-pro-446            |
| Octopus Pro (429)  | btt-octopus-pro-429            |
| Octopus Pro (H723) | btt-octopus-pro-h723           |
| Octopus v1.1       | btt-octopus-11                 |
| Octopus v1.1 (407) | btt-octopus-11-407             |
| SKR Pro v1.2       | skr\_pro\_12                     |
| SKR 3              | btt\_skr\_3                      |
| SKR 3 (H723)       | btt-skr-3-h723                 |
| SKR 3 EZ           | btt-skr-3-ez                   |
| SKR 3 EZ (H723)    | btt-skr-3-ez-h723              |
| SKR 2 (429)        | btt-skr-2-429                  |
| SKR 2 (407)        | btt-skr-2-407                  |
| SKR RAT            | btt-skrat-10                   |
| SKR 1.4 Turbo      | btt-skr-14-turbo               |
| SKR Mini E3 v3     | btt\_skr\_mini\_e3\_30             |

| Toolhead (CAN) | Parameter name to use in macro |
| -------------- | ------------------------------ |
| EBB42 v1       | btt\_ebb42\_10                   |
| EBB36 v1       | btt\_ebb36\_10                   |
| EBB42 v1.1     | btt\_ebb42\_11                   |
| EBB36 v1.1     | btt\_ebb36\_11                   |
| EBB42 v1.2     | btt\_ebb42\_12                   |
| EBB36 v1.2     | btt\_ebb36\_12                   |

| **Electronics** | **Parameter name to use in macro** |
| --------------------- | ---------------------------------- |
| MKS Eagle v1.x        | mks-eagle-10                       |
| MKS Robin Nano v3   | mks-robin-nano-30                  |
| MKS Robin Nano v2   | mks-robin-nano-20                  |
| MKS Gen L             | mks-gen-l                          |
| ZNP Robin Nano DW v2  | znp\_robin\_nano\_dw\_v2               |

| Toolhead (CAN)    | Parameter name to use in macro |
| ----------------- | ------------------------------ |
| Mellow FLY SHT 42 | mellow\_fly\_sht\_42              |
| Mellow FLY SHT 36 | mellow\_fly\_sht\_36              |

| Electronics   | Parameter name to use in macro |
| ------------- | ------------------------------ |
| Fysetc Spider | fysetc\_spider                  |

| Electronics       | Parameter name to use in macro |
| ----------------- | ------------------------------ |
| Artillery Ruby v1.x | artillery-ruby-12              |

| Electronics          | Parameter name to use in macro |
| -------------------- | ------------------------------ |
| Raspberry Pico/RP2040 | rpi-rp2040                     |

| Electronics | Parameter name to use in macro |
| ----------- | ------------------------------ |
| Leviathan v1.2 | leviathan-12                 |

### Adding the 3Dwork macros to our installation

From our interface (Mainsail/Fluidd), we will edit our `printer.cfg` and add:
`
**printer.cfg**
```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
````

> ℹ️ **INFO\!\!\!**
> It's important to add these lines at the end of your configuration file... just above the section:
> `#*# <--- SAVE_CONFIG --->`
> This ensures that if macros exist in your cfg or other includes, they are overridden by ours.

> ⚠️ **IMPORTANT\!\!\!**
> The standard macros have been separated from the **shell macros** because **enabling shell macros requires additional manual steps, they are currently under testing**, and **may require extra permissions (execution permissions) for which instructions have not been provided as we are trying to automate this.**
> **Use them at your own risk.**

### Configuring your slicer

Since our macros are dynamic, they will extract certain information from your printer configuration and the slicer itself. For this, we recommend configuring your slicers as follows:

  * **Start G-code `START_PRINT`**, using placeholders to dynamically pass filament and bed temperature values:

    **PrusaSlicer**

    ```gcode
    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
    ```

    **SuperSlicer** - includes the option to set the enclosure (CHAMBER) temperature

    ```gcode
    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
    ```
![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

    **Bambu Studio/OrcaSlicer**

    ```gcode
    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
    ```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

    **Cura**

    ```gcode
    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
    ```

    > ⚠️ **Notice\!\!\!**
    > You must install the [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff). Go to the menu ***Help/Show Configuration Folder...***, copy the script from the link above into the `scripts` folder.
    > Restart Cura, then go to ***Extensions/Post processing/Modify G-Code*** and select ***Mesh Print Size***. This makes the `%MINX%`, `%MINY%`, `%MAXX%`, `%MAXY%` variables available.

    **ideaMaker**

    ```gcode
    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
    ```

    **Simplify3D**

    ```gcode
    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
    ```

    > ℹ️ **INFO\!\!\!**
    > **Placeholders are "aliases" or variables that slicers use**, replacing them with the values configured in the print profile when generating the G-code.

    > You can find lists of these placeholders in the following links: [**PrusaSlicer**](https://help.prusa3d.com/en/article/list-of-placeholders_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (includes PrusaSlicer's), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list), and [**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

    > Using these allows our macros to be dynamic.

  * **End G-code `END_PRINT`**, in this case, since it doesn't use placeholders, it's common to all slicers:

    ```gcode
    END_PRINT
    ```

### Variables

As mentioned, these new macros provide some very useful functions listed earlier.

To adjust them to your machine, use the variables found in `macros/macros_var_globals.cfg`, detailed below.

#### Language for messages/notifications

Since many users like to have macro notifications in their language, we have devised a multi-language notification system, currently supporting Spanish (es) and English (en). You can adjust it with the following variable:

| Variable          | Description                                                                           | Possible Values | Default Value |
| ----------------- | ------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable\_language | Allows selecting the notification language. If not defined correctly, 'en' (English) will be used. | es / en         | es            |

#### Relative Extrusion

Controls the extrusion mode used at the end of `START_PRINT`. The value depends on your slicer's configuration.

> 💡 **Tip**
> It is advisable to configure your slicer to use relative extrusion and set this variable to `True`.

| Variable                    | Description                                              | Possible Values | Default Value |
| --------------------------- | -------------------------------------------------------- | --------------- | ------------- |
| variable\_relative\_extrusion | Indicates the extrusion mode used in your slicer. | True / False    | True          |

#### Speeds

To manage the speeds used in the macros.

| Variable                    | Description                    | Possible Values | Default Value |   |
| --------------------------- | ------------------------------ | --------------- | ------------- | --|
| variable\_macro\_travel\_speed | Travel speed during moves (mm/s) | numeric         | 150           |   |
| variable\_macro\_z\_speed      | Travel speed for Z-axis (mm/s) | numeric         | 15            |   |

#### Homing

Set of variables related to the homing process.

| Variable | Description | Possible Values | Default Value |
| -------- | ----------- | --------------- | ------------- |
|          |             |                 |               |

*(Note: Homing variables are not listed in the original text)*

#### Heating

Variables related to the machine heating process.

| Variable                               | Description                                                              | Possible Values | Default Value |
| -------------------------------------- | ------------------------------------------------------------------------ | --------------- | ------------- |
| variable\_preheat\_extruder              | Enables nozzle preheating to the temperature in `variable_preheat_extruder_temp` | True / False    | True          |
| variable\_preheat\_extruder\_temp         | Nozzle preheating temperature (°C)                                       | numeric         | 150           |
| variable\_start\_print\_heat\_chamber\_bed\_temp | Bed temperature during the enclosure heating process (°C)             | numeric         | 100           |

> 💡 **Tip**
> Benefits of using nozzle preheating:
>
>   * Allows extra time for the bed to reach its temperature uniformly.
>   * If using an inductive probe without temperature compensation, it allows readings to be more consistent and accurate.
>   * Helps soften any filament residue in the nozzle, which, in certain configurations, prevents these residues from affecting probe activation.

#### Bed Mesh

To control the leveling process, we have variables that can be very useful. For example, we can control the type of leveling we want to use: always creating a new mesh, loading a previously stored one, or using adaptive meshing.

| Variable                    | Description                                                                                                                                                                                                                                 | Possible Values                   | Default Value |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------- |
| variable\_calibrate\_bed\_mesh | Selects the type of mesh to use in `START_PRINT`: <br>- `newmesh`: performs a mesh for every print<br>- `storedmesh`: loads a stored mesh and does not perform bed probing<br>- `adaptative`: performs a new mesh adapted to the print area, often improving first layers<br>- `nomesh`: skips the meshing process (if no probe or mesh is not used) | newmesh / storedmesh / adaptative / nomesh | adaptative    |
| variable\_bed\_mesh\_profile   | The name used for your stored mesh profile                                                                                                                                                                                                    | text                              | default       |

> ⚠️ **Notice\!\!\!**
> We recommend using `adaptative` leveling as it always adjusts the mesh to the size of your print, allowing for a fine-tuned mesh area.
>
> It's important to have the `PRINT_MAX` and `PRINT_MIN` values included in the `START_PRINT` call within your [slicer's start G-code](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print).

#### Purging

An important phase of our print start is proper purging of the nozzle to avoid filament residues or prevent them from damaging the print at some point. Below are the variables involved in this process:

| Variable                               | Description                                                                                                                                                                                                                         | Possible Values                        | Default Value       |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------- |
| variable\_nozzle\_priming                | Choose between different purge options:<br>- `primeline`: draws the typical purge line<br>- `primelineadaptative`: generates a purge line adapted to the print area using `variable_nozzle_priming_objectdistance` as margin<br>- `primeblob`: creates a filament blob in a corner of the bed<br>- `False`: disable purging | primeline / primelineadaptative / primeblob / False | primelineadaptative |
| variable\_nozzle\_priming\_objectdistance | If using adaptive purge line, this is the margin (mm) to use between the purge line and the printed object                                                                                                                          | numeric                                | 5                   |
| variable\_nozzle\_prime\_start\_x          | Where to locate the purge line/blob on X:<br>- `min`: X=min\_coord (+ safety margin)<br>- `max`: X=max\_coord (- safety margin)<br>- number: specific X coordinate                                                                        | min / max / number                     | max                 |
| variable\_nozzle\_prime\_start\_y          | Where to locate the purge line/blob on Y:<br>- `min`: Y=min\_coord (+ safety margin)<br>- `max`: Y=max\_coord (- safety margin)<br>- number: specific Y coordinate                                                                        | min / max / number                     | min                 |
| variable\_nozzle\_prime\_direction        | Direction of the line or blob extrusion:<br>- `backwards`: towards the front<br>- `forwards`: towards the back<br>- `auto`: towards the center based on `variable_nozzle_prime_start_y`                                              | auto / forwards / backwards            | auto                |

#### Filament Load/Unload

This group of variables facilitates the management of filament loading and unloading, used for M600 emulation or when running the filament load/unload macros:

| Variable                        | Description                                                                                                                                                                                                                            | Possible Values | Default Value |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable\_filament\_unload\_length | How much filament to retract (mm). Adjust to your machine; typically the distance from your nozzle to your extruder gears plus an extra margin.                                                                                     | numeric         | 130           |
| variable\_filament\_unload\_speed  | Filament retraction speed (mm/s); usually a slow speed is used.                                                                                                                                                                        | numeric         | 5             |
| variable\_filament\_load\_length   | Distance (mm) to load the new filament. Similar to `variable_filament_unload_length`, use the distance from your gears to the nozzle plus an extra margin. This extra margin depends on how much you want to purge; usually give it more margin than the unload length to ensure the previous filament is purged cleanly. | numeric         | 150           |
| variable\_filament\_load\_speed    | Filament loading speed (mm/s); usually a faster speed than unloading is used.                                                                                                                                                            | numeric         | 10            |

> ⚠️ **Notice\!\!\!**
> Another necessary setting for your **`[extruder]`** section is [**`max_extrude_only_distance`**](https://www.klipper3d.org/Config_Reference.html#extruder). The recommended value is usually \>101 (if undefined, it defaults to 50) to allow, for example, typical extruder calibration tests.
> You should adjust the value based on the test mentioned above or your configuration of **`variable_filament_unload_length`** and/or **`variable_filament_load_length`**.

### Parking

During certain printer processes, like pausing, it is advisable to park the toolhead. Our bundle's macros include this option along with the following variables to manage it:

*(Note: Parking variables are not listed in the original text)*

| Variable                           | Description                                                                                                                                                                                          | Possible Values    | Default Value |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------- |
| variable_start_print_park_in       | Location where the toolhead parks during pre-heating.                                                                                                                                                    | back / center / front | back          |
| variable_start_print_park_in       | Location where the toolhead parks during pre-heating.                                                                                                                                                    | back / center / front | back          |
| variable_start_print_park_z_height | Z height (mm) during pre-heating.                                                                                                                                                                    | numeric            | 50            |
| variable_end_print_park_in         | Location where the toolhead parks when finishing or canceling a print.                                                                                                                                 | back / center / front | back          |
| variable_end_print_park_z_hop      | Distance (mm) to hop in Z at the end of the print.                                                                                                                                                   | numeric            | 20            |
| variable_pause_print_park_in       | Location where the toolhead parks when pausing the print.                                                                                                                                              | back / center / front | back          |
| variable_pause_idle_timeout        | Value (in seconds) for activating the machine's idle timeout process, which disables motors causing loss of coordinates. **A high value is advisable so that activating the PAUSE macro allows sufficient time for actions before coordinates are lost.** | numeric            | 43200         |

### Z-Tilt

Maximizing our machine's ability to self-level and ensuring it's always in the best condition is fundamental.

**Z-TILT is basically a process that helps us align our Z motors with respect to our X axis/gantry (Cartesian) or XY gantry (CoreXY)**. With this, **we ensure our Z is always perfectly aligned, precisely and automatically**.

| Variable                  | Description                                                                               | Possible Values | Default Value |
| ------------------------- | ----------------------------------------------------------------------------------------- | --------------- | ------------- |
| variable_calibrate_z_tilt | Enables the Z-Tilt adjustment process, if enabled in our Klipper configuration. | True / False    | False         |

#### Skew

Using [SKEW](broken-reference) for correction or precise adjustment of our printers is highly advisable if we have deviations in our prints. Using the following variable, we can enable its use in our macros:

| Variable              | Description                                                                                                                                          | Possible Values | Default Value     |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| variable_skew_profile | Allows taking into account our skew profile, which will be loaded in our START_PRINT macro. To activate it, uncomment the variable and use the skew profile name from your configuration. | text            | my_skew_profile |

### Customizing macros

Our Klipper module uses the modular configuration system employed in RatOS, leveraging Klipper's advantage in sequentially processing configuration files. Therefore, the order of includes and custom adjustments we want to apply over these modules is fundamental.

> ℹ️ **INFO!!!**
> Since they are used as a module, the 3Dwork configurations CANNOT be edited directly from the `3dwork-klipper` directory within your Klipper config directory, as it will be read-only for security.
>
> Therefore, it's very important to understand how Klipper works and how to customize our modules for your machine.

#### **Customizing variables**

Typically, this is what we will need to adjust to modify the default variables in our **3Dwork** Klipper module.

Simply, what we need to do is copy the content of the **`[gcode_macro GLOBAL_VARS]`** macro, which can be found in `macros/macros_var_globals.cfg`, into our `printer.cfg`.

We remind you of what was mentioned earlier about how Klipper processes configurations sequentially, so it is advisable to paste it *after* the includes mentioned [here](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

It will look something like this (this is just a visual example):

```ini
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES
## 3DWORK VARIABLES
[gcode_macro GLOBAL_VARS]
description: GLOBAL_VARS variable storage macro, will echo variables to the console when run.
# Configuration Defaults
# This is only here to make the config backwards compatible.
# Configuration should exclusively happen in printer.cfg.

# Possible language values: "en" or "es" (if the language is not well defined, "en" is assigned by default.)
variable_language: "es" # Possible values: "en", "es"
...

#*# <---------------------- SAVE_CONFIG ----------------------> #*#
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#

```

> ⚠️ **Notice!!!**
> The three dots (...) in the previous examples are merely to indicate that you might have more configurations between sections... they should not be included literally.

> ℹ️ **INFO!!!**
> * We advise adding comments as seen in the previous example to identify what each section does.
> * Even if you don't need to change all variables, we recommend copying the entire content of **`[gcode_macro GLOBAL_VARS]`**.

#### Customizing macros

The macros have been set up in a modular way so they can be easily adjusted. As mentioned earlier, if we want to adjust them, we should proceed the same way as with variables: copy the macro in question into our `printer.cfg` (or another custom include file) and ensure it is placed *after* the include where we added our 3Dwork Klipper module.

We have two groups of macros:

* Macros for adding user adjustments: These macros can be easily added and customized because they were included so any user can customize actions to their liking at specific parts of the processes each macro performs.

    **START_PRINT**
    | Macro Name                            | Description                                                                                           |
    | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
    | _USER_START_PRINT_HEAT_CHAMBER        | Executes just after our enclosure starts heating, if `CHAMBER_TEMP` is passed as a parameter to `START_PRINT` |
    | _USER_START_PRINT_BEFORE_HOMING       | Executes before the initial homing at the start of the print                                          |
    | _USER_START_PRINT_AFTER_HEATING_BED   | Executes when our bed reaches its temperature, before `_START_PRINT_AFTER_HEATING_BED`              |
    | _USER_START_PRINT_BED_MESH            | Runs before `_START_PRINT_BED_MESH`                                                                   |
    | _USER_START_PRINT_PARK                | Runs before `_START_PRINT_PARK`                                                                       |
    | _USER_START_PRINT_AFTER_HEATING_EXTRUDER | Runs before `_START_PRINT_AFTER_HEATING_EXTRUDER`                                                   |

    **END_PRINT**
    | Macro Name                          | Description                                                                               |
    | ----------------------------------- | ----------------------------------------------------------------------------------------- |
    | _USER_END_PRINT_BEFORE_HEATERS_OFF  | Executes before turning off the heaters, before `_END_PRINT_BEFORE_HEATERS_OFF`           |
    | _USER_END_PRINT_AFTER_HEATERS_OFF   | Executes after turning off the heaters, before `_END_PRINT_AFTER_HEATERS_OFF`             |
    | _USER_END_PRINT_PARK                | Executes before parking the toolhead, before `_END_PRINT_PARK`                            |

    **PRINT_BASICS** (Pause/Resume)
    | Macro Name           | Description                    |
    | -------------------- | ------------------------------ |
    | _USER_PAUSE_START    | Executes at the start of a PAUSE |
    | _USER_PAUSE_END      | Executes at the end of a PAUSE   |
    | _USER_RESUME_START   | Executes at the start of a RESUME|
    | _USER_RESUME_END     | Executes at the end of a RESUME  |

* Internal macros: These are macros used to divide the main macro into processes and are important for it. It is advisable that if these need adjustment, they are copied exactly as they are.

    **START_PRINT**
    | Macro Name                            | Description                                                                                                     |
    | ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
    | _START_PRINT_HEAT_CHAMBER             | Heats the enclosure if the `CHAMBER_TEMP` parameter is received by our `START_PRINT` macro from the slicer      |
    | _START_PRINT_AFTER_HEATING_BED        | Executes when the bed reaches temperature, after `_USER_START_PRINT_AFTER_HEATING_BED`. Typically used for processing bed calibrations (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...) |
    | _START_PRINT_BED_MESH                 | Handles the bed meshing logic.                                                                                  |
    | _START_PRINT_PARK                     | Parks the print head while heating the nozzle to print temperature.                                             |
    | _START_PRINT_AFTER_HEATING_EXTRUDER | Performs nozzle purging and loads the SKEW profile if defined in the variables.                                   |

## Printers and Electronics

As we work with different printer models and electronics, we will add those not directly supported by RatOS, whether they are our contributions or from the community.

* `printers`: This directory will contain all printer configurations.
* `boards`: Here we will find configurations for electronics.

### Parameters and Pins

Our Klipper module uses the modular configuration system employed in RatOS, leveraging Klipper's advantage in sequentially processing configuration files. Therefore, the order of includes and custom adjustments we want to apply over these modules is fundamental.

> ℹ️ **INFO!!!**
> Since they are used as a module, the 3Dwork configurations CANNOT be edited directly from the `3dwork-klipper` directory within your Klipper config directory, as it will be read-only for security.
>
> Therefore, it's very important to understand how Klipper works and how to customize our modules for your machine.

As explained in "[Customizing macros](3dwork-klipper-bundle.md#personalizando-macros)", we will use the same process to adjust parameters or pins to suit our needs.

#### Customizing parameters

As advised, create a section in your `printer.cfg` called `USER OVERRIDES`, placed *after* the includes for our configurations, to adjust and customize any parameters used in them.

In the following example, we'll see how, in our case, we are interested in customizing the parameters of our bed leveling (`bed_mesh`) by adjusting the probe points (`probe_count`) relative to the default configuration in our Klipper module:

**printer.cfg**
```ini
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES

## 3DWORK VARIABLES
[gcode_macro GLOBAL_VARS]
...

## 3Dwork PARAMETERS
[bed_mesh]
probe_count: 11,11
...

#*# <---------------------- SAVE_CONFIG ----------------------> #*#
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
```

> ⚠️ **Notice!!!**
> The three dots (...) in the previous examples are merely to indicate that you might have more configurations between sections... they should not be included literally.

We can use this same process with any parameter we want to adjust.

#### Customizing pin configuration

We will proceed exactly as done before. In our `USER OVERRIDES` section, we will add those pin sections we want to adjust to our liking.

In the following example, we will customize the pin for our electronics fan (`controller_fan`) to assign it to a different one than the default:

**printer.cfg**
```ini
### 3Dwork Klipper Includes
[include 3dwork-klipper/macros/macros_*.cfg]

### USER OVERRIDES

## 3DWORK VARIABLES
```english
[gcode_macro GLOBAL_VARS]
...

## 3Dwork PARAMETERS

[bed_mesh]
probe_count: 11,11
...

## 3Dwork PINS

[controller_fan controller_fan]
pin: PA8

#*# <---------------------- SAVE_CONFIG ----------------------> #*#
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#

```
> ⚠️ **Notice!!!**
> The three dots (...) in the previous examples are merely to indicate that you might have more configurations between sections... they should not be included literally.
```
