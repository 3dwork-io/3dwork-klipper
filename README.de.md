# 3dwork Clope Bündel ![Deutsch](https://flagcdn.com/w40/de.png)

## Makros -Paket, Konfigurationen und andere Dienstprogramme für Klipper

[![English](https://flagcdn.com/w40/gb.png)](README.en.md)[![Español](https://flagcdn.com/w40/es.png)](README.md)[![Italiano](https://flagcdn.com/w40/it.png)](README.it.md)[![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)[![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ Warnung****Leitfaden im Prozess !!!****<span style="color: red">Obwohl Makros völlig funktionsfähig sind, sind sie in kontinuierlicher Entwicklung.</span>****<span style="color: orange">Verwenden Sie sie unter Ihrer eigenen Verantwortung !!!</span>**

Changelog

12/07/2023 - Support für die Automatisierung der Firmware für BigReteech -Elektronik hinzugefügt

Aus**3dwork**Wir haben eine Reihe von Makros, Maschinen- und elektronischen Konfigurationen sowie andere Tools für eine einfache und leistungsstarke Verwaltung von Klipper zusammengestellt und angepasst.

Ein Großteil dieses Pakets basiert auf[**Ratten**](https://os.ratrig.com/)Verbesserung der Parteien, die wir für interessant halten, sowie andere Beiträge der Gemeinschaft.

## Installation

Um unser Paket für Klipper zu installieren, werden wir die folgenden Schritte ausführen

### Entladung des Repositorys

Wir werden eine Verbindung zu unserem Host mit SSH herstellen und die folgenden Befehle starten:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ Verwendung**Wenn das Verzeichnis Ihrer Klipper -Konfiguration personalisiert ist, denken Sie daran, den ersten Befehl ordnungsgemäß an Ihre Installation anzupassen.

> **ℹ️ Informationen für neue Einrichtungen**Da Klipper keinen Zugriff auf Makros ohne einen gültigen Drucker erlaubt.
>
> 1.  Achten Sie darauf, die zu haben[Gastgeber als zweite MCU](raspberry-como-segunda-mcu.md)
> 2.  Fügen Sie diesen grundlegenden Drucker hinzu. CFG, um Makros zu aktivieren:

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

Dadurch kann KLIPPER an den Makros beginnen und auf die Makros zugreifen.

### Verwenden von Moonraker, um immer aktualisiert zu werden

Dank Moonraker können wir mit dem Update_Manager mit den Verbesserungen, die wir in Zukunft einführen können, auf dem neuesten Stand sein.

Von MainSail/Fluidd bearbeiten wir unseren Moonraker.conf (es sollte auf der gleichen Höhe wie bei Ihrem Drucker sein) und wir werden am Ende der Konfigurationsdatei hinzufügen:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ Warnung****Denken Sie daran, den Installationsschritt zuvor zu machen, wenn Sie keinen Fehler generieren und nicht starten können.**
>
> **Denken Sie hingegen daran, den Pfad ordnungsgemäß an Ihre Installation anzupassen.**

## Makros

Wir haben immer kommentiert, dass Times eine der besten Verteilungen von Klipper mit Raspberry -Support und CB1 -Modulen ist, hauptsächlich aufgrund seiner modularen Konfigurationen und seiner großen Makros.

Einige zusätzliche Makros, die nützlich sein werden:

### **Makros für den allgemeinen Gebrauch**

| Makro                       | Beschreibung                                                                                                                                                                                              |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vielleicht_home**         | Es ermöglicht es uns, den Homing -Prozess nur durch diese in den Achsen zu optimieren, die nicht mit Homing enthalten sind.                                                                               |
| **PAUSE**                   | Durch verwandte Variablen können wir eine Pause mit einem vielseitigeren Kopfparkplatz mit normalem Makros verwalten.                                                                                     |
| **SET_PAUSE_AT_LAYER**      |                                                                                                                                                                                                           |
| **Set_pause_at_next_layer** | Ein sehr nützliches Makro, das Hauptsegel in seine Benutzeroberfläche integriert, um in einer bestimmten Ebene auf Bedarf innehalten zu können ... falls wir beim Ausführen des Laminats vergessen haben. |
|                             | Wir haben auch einen anderen, um das gemächliche in der nächsten Schicht auszuführen.                                                                                                                     |
| **WIEDER AUFNEHMEN**        | Verbessert, da es ermöglicht, festzustellen, ob unsere Düse nicht an der Extrusionstemperatur liegt, um sie zu lösen, bevor sie einen Fehler aufweist und unseren Eindruck schädigt.                      |
| **Cancel_print**            | Dies ermöglicht die Verwendung des Restes der Makros, eine Abdrehungsstörung korrekt durchzuführen.                                                                                                       |

-   **Stattdessen in der Pause**, sehr interessante Makros, die es uns ermöglichen, einen gemächlichen in einer Ebene geplant zu machen oder einen Befehl zu starten, wenn wir die nächste Schicht starten. ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)Ein weiterer Vorteil von ihnen besteht darin, dass sie in das Mainsegel mit den neuen Funktionen in unserer Benutzeroberfläche integriert sind, wie Sie unten sehen können:![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Druckverwaltung Makros**

| Makro           | Beschreibung                                                                                                                                            |   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **Start_print** | Es ermöglicht es uns, unsere Eindrücke auf sichere Weise und im Klipper -Stil zu starten. In diesem Fall finden wir einige interessante Funktionen wie: |   |
|                 | • Smart Düse Vorheizen bei Verwendung eines Sondensensors                                                                                               |   |
|                 | • Möglichkeit der Verwendung von Z-Tilt durch Variable                                                                                                  |   |
|                 | • Adaptive Bettrolle, erzwang die seit Malla gelagert                                                                                                   |   |
|                 | • Anpassbare Säuberung zwischen normaler, adaptiver Säuberungslinie oder Säuberungsabfall                                                               |   |
|                 | • Segmentiertes Makro, um personalisieren zu können, wie wir Ihnen später zeigen werden                                                                 |   |
| **End_print**   | Makro des Drucks des Drucks, bei dem wir auch eine Segmentierung haben, um unser Makro anzupassen. Wir haben auch einen dynamischen Kopf des Kopfes.    |   |

-   **Adaptive Bettrolle**Dank der Vielseitigkeit von Klipper können wir Dinge tun, die heute unmöglich erscheinen ... Ein wichtiger Prozess des Eindrucks ist es, eine Mahlzeit von Abweichungen von unserem Bett zu haben, die es uns ermöglichen, diese zu korrigieren, um eine Einhaltung der perfekten ersten Schichten zu haben.  
     Bei vielen Gelegenheiten machen wir diesen Malley vor den Eindrücken, um sicherzustellen, dass es richtig funktioniert, und dies erfolgt auf der gesamten Oberfläche unseres Bettes. 
     Mit dem Elend des adaptiven Bettes wird es in der Druckzone durchgeführt, was es viel präziser macht als die traditionelle Methode ... In den folgenden Fängen werden wir die Unterschiede eines traditionellen und adaptiven Netzes sehen.
    <div style="display: flex; justify-content: space-between;">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
    </div>

### **Filamentverwaltung Makros**

Makros, die es uns ermöglichen, verschiedene Aktionen mit unserem Filament wie der Last oder Entladung davon zu verwalten.

| Makro               | Beschreibung                                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Der M600**        | Es ermöglicht uns die Kompatibilität mit dem M600 -Gcode, der normalerweise in Laminatoren für die Änderung des Filaments verwendet wird. |
| **Entlow_Filament** | Konfigurierbar über die Variablen ermöglicht es uns, assistierte Filamente herunterzuladen.                                               |
| **Load_filament**   | Sowie die vorherige, aber im Zusammenhang mit der Last des Filaments.                                                                     |

### **Filamentspulenverwaltung Makros (Spoolman)**

> **⚠️ Warnung****Abschnitt im Prozess !!!**

[**Spoolman**](https://github.com/Donkie/Spoolman)Er ist ein Filamentspulenmanager, der in Moonraker integriert ist und es uns ermöglicht, unsere Aktien und Verfügbarkeit von Filamenten zu verwalten.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Wir werden die Installation und Konfiguration nicht eingeben, da sie mit dem relativ einfach ist[**Anweisungen Ihres Githubs**](https://github.com/Donkie/Spoolman)**,**In jedem Fall**Wir empfehlen Ihnen, Docker zu verwenden**Durch Einfachheit und Erinnerung**Aktivieren Sie die Konfiguration in Moonraker**erforderlich:

**mondraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Makro              | Beschreibung                                                                           |
| ------------------ | -------------------------------------------------------------------------------------- |
| Set_active_spool   | Es ermöglicht uns anzunehmen, welches ID der Spule verwendet wird, um sie zu verwenden |
| Clear_active_spool | Ermöglicht es uns, die aktive Spule zurückzusetzen                                     |

Das Ideal in jedem Fall wäre, unseren Laminator hinzuzufügen,**Im Filament -GCODES für jede Spule den Aufruf dazu**und erinnere dich**Ändern Sie die ID davon einst konsumiert**Um den Rest des Filaments darin kontrollieren zu können !!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Makros der Oberflächenmanagement aus Druckdrucken**

> **⚠️ Warnung****Abschnitt im Prozess !!!**

In der Regel ist es normal, dass wir je nach Finish, die wir haben möchten, oder der Art des Filaments unterschiedliche Druckflächen haben.

Dieser Satz von Makros, erstellt von[Garethky](https://github.com/garethky)Sie ermöglichen es uns, eine Kontrolle über diese und insbesondere die korrekte Einstellung von Zoffset in jedem von ihnen in dem Stil zu haben, den wir in Prussa -Maschinen haben. Unten können Sie einige Ihrer Funktionen sehen:

-   Wir können die Anzahl der gewünschten Druckoberflächen speichern, die jeweils einen eindeutigen Namen haben
-   Jede Druckoberfläche hat einen eigenen Zoffset
-   Wenn wir während eines Eindrucks (Babystepping) von unserem Klipper Z -Einstellungen vornehmen

Andererseits haben wir einige**Anforderungen an die Implementierung (es wird versucht, die Logik des Bundle -Drucks hinzuzufügen**:

-   Die Verwendung von**[Save_variables]**In unserem Fall werden wir ~/variablen.cfg verwenden, um die Variablen zu speichern, und das liegt bereits innerhalb des CFG dieser Makros.  
    Dadurch wird automatisch eine Variablen_build_sheets.cfg -Datei erstellt, in der unsere Festplattenvariablen aufbewahrt werden.

**Beispiel für die variable Konfigurationsdatei**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

-   Wir müssen einen Anruf an uear_build_sheet_adjustment in unserem print_start eingeben, um das ausgewählte Oberflächen -Zoffset anzuwenden
-   Es ist wichtig, dass wir für das vordere Makro die ordnungsgemäße Funktionen für applic_build_sheet_adjust für ein set_gcode_offset z = 0.0 hinzufügen müssen


    # Load build sheet
    SHOW_BUILD_SHEET ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset

Andererseits ist es interessant, einige Makros zu haben, um die eine oder andere Oberfläche zu aktivieren oder sogar als Parameter von unserem Laminator an verschiedene Drucker- oder Filamentprofile zu übergeben, um die eine oder andere automatisch laden zu können:

> **⚠️ Warnung**Es ist wichtig, dass der Wert in name = "xxxx" mit dem Namen zusammenfällt, den wir bei der Installation unserer Druckoberfläche angegeben haben

\*\* drucker.cfg

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

Auch im Falle von Klipperscreen können wir ein bestimmtes Menü hinzufügen, um die Last der verschiedenen Oberflächen verwalten zu können, wobei wir einen Aufruf an die zuvor für die Belastung jeder Oberfläche erstellten Makros aufnehmen können:

**~/printer_data/config/klipperscreen.conf**

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

| Makro                        | Beschreibung |
| ---------------------------- | ------------ |
| Install_build_sheet          |              |
| Show_build_sheet             |              |
| Show_build_sheets            |              |
| Set_build_sheet_offset       |              |
| Reset_build_sheet_offset     |              |
| Set_gcode_offset             |              |
| Apply_build_sheet_adjustment |              |

### **Maschinenmakros**

| Makro                                                         | Beschreibung                                                                                                                                                                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compile_firmware**                                          | Mit diesem Makro können wir die Klipper -Firmware auf einfache Weise kompilieren, die Firmware für mehr Einfachheit aus der Benutzeroberfläche zugänglich machen und sie auf unsere Elektronik anwenden können.                 |
| Hier haben Sie mehr Details der elektronischen Unterstützung. |                                                                                                                                                                                                                                 |
| **Calculate_bed_mesh**                                        | Ein äußerst nützliches Makro zur Berechnung des Bereichs für unser Netz, da es manchmal ein komplizierter Prozess sein kann.                                                                                                    |
| **Pid_all**                                                   |                                                                                                                                                                                                                                 |
| **Pid_extruder**                                              |                                                                                                                                                                                                                                 |
| **Pid_bed**                                                   | Diese Makros, bei denen wir die Temperaturen für die PID in Form von Parametern übergeben können, ermöglichen es uns, die Temperaturkalibrierung auf extrem einfache Weise durchzuführen.                                       |
| **Test_speed**                                                |                                                                                                                                                                                                                                 |
| **Test_speed_delta**                                          | Originalmakro des Partners[Ellis](https://github.com/AndrewEllis93)Sie ermöglichen uns auf eine recht einfache Weise, die Geschwindigkeit zu testen, mit der wir unsere Maschine genau und ohne Schritteverlust bewegen können. |

\*\_**Firmware -Zusammenstellung für unterstützte Elektronik**Um den Prozess der Erstellung und Wartung unserer Klipper -Firmware für unsere MCU zu erleichtern. Wir haben die MACRO COMMIE_FIRMWARE, dass wir beim Ausführen unserer Elektronik als Parameter nur dies tun können, um nur dies zu tun, und für alle Elektronik, die von unserem Bündel unterstützt wird:![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)Wir werden diese auf einfache Weise von unserer UI -Website im Verzeichnis firmware_binaries auf unserer Registerkarte Firmware_Binaries (falls wir an MainSail verwenden) zugänglich finden:![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)Dann haben Sie die Liste der unterstützten elektronischen:

> ⚠️**WICHTIG!!!**
>
> Diese Skripte sind bereit, mit PI -Benutzer an einem Raspbian -System zu arbeiten. Wenn Sie nicht Ihr Fall sind, müssen Sie es anpassen.
>
> Firmawares werden zur Verwendung mit USB -Verbindung generiert, die immer das ist, was wir empfehlen. Außerdem ist der USB -Montagepunkt immer gleich, indem Ihre Konfiguration Ihrer MCU -Verbindung nicht geändert wird, wenn sie mit unserem Makro/Skript generiert werden
>
> **So dass Klipper Shell -Makros ausführen kann, dank des Partners muss eine Erweiterung installiert werden**[**Arksin**](https://github.com/Arksine)**, lass es.**
>
> **Abhängig vom gebrauchten Klipper -Dystro können sie bereits aktiviert werden.**
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> Der einfachste Weg ist die Verwendung[**Kioh**](../instalacion/#instalando-kiauh)Wo wir in einer Ihrer Optionen die Möglichkeit haben, diese Erweiterung zu installieren:
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Wir können den Prozess auch von Hand ausführen. Wir werden das Plugin für Klipper &lt;[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)In unserem Verzeichnis`_**~/klipper/klippy/extras**_`Mit SSH SCP Y starten wir Klipper neu.

| Elektronisch            | Parametername im Makro verwendet |
| ----------------------- | -------------------------------- |
| Manta                   | ich bin stolz                    |
| M4p machen              | BTT-Manta-M4p                    |
| Manta M4p v2.           | BTT-Manta-M4P-22                 |
| M8p machen              | BTT-Manta-M8p                    |
| Markierung M8p v1.1     | BTT-Manta-M8p-11                 |
| Tintenfisch maximal das | btt-octopus-max-ez               |
| Octopus Pro (446)       | BTT-Octopus-Pro-446              |
| Octopus Pro (429)       | BTT-Octopus-Pro-429              |
| Octopus Pro (H723)      | btt-octopus-pro-h723             |
| Oktopus v1.1            | BTT-Octopus-11                   |
| Oktopus v1.1 (407)      | BTT-Octopus-11-407               |
| SKR Pro v1.2            | SKR_PRO_12                       |
| Skr 3                   | BTT -Schraube 3                  |
| Saqr a (heha)           | Smarted                          |
| Skr 3 dies              | BTT-SC-3-EZ                      |
| SKR 3 this (H723)       | Skirzhahah                       |
| SKR 2 (429)             | BTT-SRC-2-429                    |
| SKR 2 (407)             | BTT-SRC-2-407                    |
| Schreit                 | BTT-SKRAT-10                     |
| Von 1,4 Turbo           | BTT-SC-14-Turbo                  |
| Skri Mini               | BTT_SKR_MINI_E3_30               |

| Toolhead (CAN) | Parametername im Makro verwendet |
| -------------- | -------------------------------- |
| EBB42 V1       | BTT_EBB42_10                     |
| Ebb36 v1       | BTT_EBB36_10                     |
| EBB42 V1.1     | BTT_EBB42_11                     |
| EBB36 V1.1     | BTT_EBB36_11                     |
| EBB42 V1.2     | BTT_EBB42_12                     |
| Ebb36 v1.2     | BTT_EBB36_12                     |

| **Elektronisch**             | **Parametername im Makro verwendet** |
| ---------------------------- | ------------------------------------ |
| MKS Eagle v1.x               | MKS-EEGLE-10                         |
| MCS Robin Nano backt         | MKS-Robin-Nano-30                    |
| MKS Robin Nano V2            | MKS-Robin-Nano-20                    |
| Mks gen l                    | MKS-General-l                        |
| Die Schuld von Robin Nano DU | Zinbennanda                          |

| Toolhead (CAN)    | Parametername im Makro verwendet |
| ----------------- | -------------------------------- |
| Mellow Fly SHT 42 | mellow_fly_sht_42                |
| Mellow Fly SHT 36 | mellow_fly_sht_36                |

| Elektronisch  | Parametername im Makro verwendet |
| ------------- | -------------------------------- |
| Fysetc Spider | Fysetc Spider                    |

| Elektronisch         | Parametername im Makro verwendet |
| -------------------- | -------------------------------- |
| Artillerie Ruby v1.x | Artillerie-Ruby-12               |

| Elektronisch          | Parametername im Makro verwendet |
| --------------------- | -------------------------------- |
| Raspberry Pico/RP2040 | RPI-RP2040                       |

| Elektronisch   | Parametername im Makro verwendet |
| -------------- | -------------------------------- |
| Leviathan V1.2 | Leviathan-12                     |

### Hinzufügen von 3DWork -Makros zu unserer Installation

Von unserer Schnittstelle, Mainseail/Fluidd, werden wir unseren Drucker.CFG bearbeiten und hinzufügen:

**drucker.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️**INFO!!!**Es ist wichtig, dass wir diese Zeilen am Ende unserer Konfigurationsdatei hinzufügen ... direkt über dem Abschnitt, so dass im Fall von Makros in unserem CFG oder einbezogen werden oder diese von uns überfordert sind: 
> \#\*# \\ &lt;--- save_config --->

> ⚠️**WICHTIG!!!**Normale Makros wurden von getrennt von**Makros -Shell**Angesichts dessen**Um diese zu aktivieren, müssen zusätzlich manuelle Schritte durchgeführt werden, die derzeit testen**Und\*\*Möglicherweise erfordern sie zusätzliche Berechtigungen, um Ausführungsberechtigungen zuzuweisen, für die die Anweisungen nicht angegeben wurden, da versucht wird, zu automatisieren.\*\***Wenn Sie sie verwenden, liegt es in Ihrer eigenen Verantwortung.**

### Einstellungen unseres Laminators

Da unsere Makros dynamisch sind, extrahieren sie bestimmte Informationen aus unserer Druckerkonfiguration und dem Laminator selbst. Dazu raten wir Ihnen, Ihre Laminatoren wie folgt zu konfigurieren:

-   **START_PRINT START GCODE**Verwenden Sie Platzhalter, um die Filament- und Betttemperaturwerte dynamisch zu übergeben:

**Prusaslicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**Superslicer**- Wir haben die Möglichkeit, die Gehäusetemperatur (Kammer) einzustellen,

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

**Studio/Orcaslicer Bambus**

```ini
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

**Behandlung**

```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

> ⚠️**Beachten!!!**Wir müssen das Plugin installieren[**Post -Prozess -Plugin (von Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)Aus der Speisekarte_**Hilfe/Show**_Konfigurationsordner ... Wir kopieren das vorherige Linkskript im Skriptordner.  
> Wir starten Heilmittel neu und wir werden gehen_**Erweiterungen/Postverarbeitung/Ändern des G-Code**_Und wir werden auswählen_**Maschendruckgröße**_.

**Idenamaker**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Vereinfachen3d**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️**INFO!!!**Der**Platzhalter sind "AKA" oder Variable**des Druckens.
>
> In den folgenden Links finden Sie eine Liste davon für:[**Prusaslicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Superslicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(zusätzlich zu denen des vorherigen),[**Studio Bambus**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)Und[**Behandlung**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> Die Verwendung dieser ermöglicht es unseren Makros, dynamisch zu sein.

-   **GCODE DAS ENTLICHE END_PRINT**In diesem Fall ist es für alle Laminatoren häufig

```ini
END_PRINT
```

### Variablen

Wie wir bereits erwähnt haben, ermöglichen diese neuen Makros uns einige sehr nützliche Funktionen, wie wir zuvor auflisten.

Für die Anpassung dieser Maschine werden wir die Variablen verwenden, die wir in macros/macros_var_globals.cfg finden und die wir unten beschreiben.

#### Nachrichten-/Benachrichtigungssprache

Da viele Benutzer die Benachrichtigungen über Makros in ihrer Sprache haben, haben wir ein Multisprachel-Benachrichtigungssystem entwickelt, derzeit Spanisch (en) und Englisch (EN). In der folgenden Variablen können wir es anpassen:

| Variable          | Beschreibung                                                                                                                       | Mögliche Werte | Standardwert |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Language | Es ermöglicht uns, die Sprache der Benachrichtigungen auszuwählen. Bei nicht gut definierter Fall wird es in (Englisch) verwendet. | Es ist / in    | es           |

#### Relative Extrusion

Es ermöglicht zu steuern, welchen Extrusionsmodus wir am Ende unseres Start_print verwenden werden. Der Wert hängt von der Konfiguration unseres Laminators ab.

> 💡**Beratung**Es ist ratsam, Ihren Laminator für die Verwendung der relativen Extrusion zu konfigurieren und diese Variable an True anzupassen.

| Variable                    | Beschreibung                                                                       | Mögliche Werte | Standardwert |
| --------------------------- | ---------------------------------------------------------------------------------- | -------------- | ------------ |
| variable_relative_extrusion | Es ermöglicht uns, den in unserem Laminator verwendeten Extrusionsmodus anzugeben. | Wahr / falsch  | WAHR         |

#### Geschwindigkeiten

Um die in Makros verwendeten Geschwindigkeiten zu verwalten.

| Variable                    | Beschreibung                                | Mögliche Werte | Standardwert |   |
| --------------------------- | ------------------------------------------- | -------------- | ------------ | - |
| variable_macro_travel_speed | Velocidad en translados                     | numerisch      | 150          |   |
| VARIABLE_MACRO_Z_SPEED      | Geschwindigkeit in übersetzter für Z -Achse | numerisch      | 15           |   |

#### Homing

Satz von Variablen im Zusammenhang mit dem Homing -Prozess.

| Variable | Beschreibung | Mögliche Werte | Standardwert |
| -------- | ------------ | -------------- | ------------ |

#### Heizung

Variablen im Zusammenhang mit dem Heizungsprozess unserer Maschine.

| Variable                                   | Beschreibung                                            | Mögliche Werte | Standardwert |
| ------------------------------------------ | ------------------------------------------------------- | -------------- | ------------ |
| VARIABLE_PREHEAT_EXTRUDER                  | Aktivieren Sie die vorgeheizte Düse bei der Temperatur, | Wahr / falsch  | WAHR         |
| VARIABLE_PREHEAT_EXTRUDER_TEMP             | Düse vorgeheizte Temperatur                             | numerisch      | 150          |
| variable_start_print_heat_chamber_bed_temp | Betttemperatur während des Erhitzens unseres Gehäuses   | numerisch      | 100          |

> 💡**Beratung**Vorteile der Verwendung der vorgeheizten Düse:

-   Es ermöglicht uns zusätzliche Zeit damit, dass das Bett seine Temperatur auf einheitliche Weise erreicht
-   Wenn wir einen Indizessensor verwenden, der keine Temperaturkompensation hat, können wir unsere Maßnahmen konsistenter und präziser machen
-   Es ermöglicht es, einen Rest des Filaments in der Düse zu mildern, was in bestimmten Konfigurationen die Aktivierung des Sensors nicht beeinflussen kann 
    { % EndHint %}

#### Bett Mali (Bettnetz)

Um den Nivellierungsprozess zu steuern, haben wir Variablen, die sehr nützlich sein können. Zum Beispiel können wir die Art der Nivellierung steuern, die wir verwenden möchten, indem wir immer ein neues Netz erstellen, ein zuvor gespeichertes Laden oder ein adaptives Netz verwenden.

| Variable                                                                                                                                            | Beschreibung                                                                                      | Mögliche Werte | Standardwert |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| variable_calibrate_bed_mesh                                                                                                                         | Es ermöglicht uns, auszuwählen, welche Art von Elend wir in unserem Start_print verwenden werden: |                |              |
| - neues Netz, wird uns in jedem Eindruck zu einem Elend machen                                                                                      |                                                                                                   |                |              |
| - StoredMeh, lädt ein gespeichertes Netz und führt die Bettumfrage nicht durch                                                                      |                                                                                                   |                |              |
| - Adaptiv, wird uns zu einem neuen Elend machen, aber an die Druckzone angepasst, um unsere ersten Schichten bei vielen Gelegenheiten zu verbessern |                                                                                                   |                |              |
| -Nomesh, in dem Fall, dass wir keinen Sensor haben oder den Prozess verwenden, um den Prozess zu überspringen                                       | neues Netz / gespeichertes Netz / adaptiv / adaptiv /                                             |                |              |
| noma                                                                                                                                                | adaptiv                                                                                           |                |              |
| variable_bed_mesh_profile                                                                                                                           | Der Name für unser gespeichertes Netz verwendet                                                   | Text           | Standard     |

> ⚠️**Beachten!!!**Wir empfehlen Ihnen, die adaptive Ebene zu verwenden, da es das Elend immer an die Größe unseres Eindrucks anpasst, sodass Sie einen angepassten Malelbereich haben.
>
> Es ist wichtig, dass wir in unserem haben[Start -up GCODE](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print)Im Anruf zu unserem Start_print die Werte print_max und print_min.

#### Gereinigt

Eine wichtige Phase unseres Druckenbeginns ist eine korrekte Säuberung unserer Düse, um Überreste des Filaments zu vermeiden, oder dass sie unseren Eindruck irgendwann beschädigen können. Dann haben Sie die Variablen, die an diesem Prozess beteiligt sind:
| Variable | Beschreibung | Mögliche Werte | Standardwert |
\| --- \| --- \| --- \| --- \|
| Variable_nozzle_priming | Wir können zwischen verschiedenen Reinheitsoptionen wählen:<br>- Primelline: Zeichnen Sie die typische reinigte Linie<br>- PrimellIneAdaptive: Erzeugt eine Säuberlinie, die an der Druckzone unter Verwendung von variable_nazzle_priming_objectDistance als Rand angepasst ist<br>- Primoblob: macht einen Tropfen Filament in einer Ecke des Bettes | Primelline / PrimellineAdaptive / PrimeBlob / False | Primelineadaptative |
| Variable_nozzle_priming_objectDistance | Wenn wir die adaptive Spülleitung verwenden, ist es der Rand zwischen der Säuberungslinie und dem gedruckten Objekt | numerisch | 5 |
| Variable_nozzle_prime_start_x | Wo kann man unsere Säuberlinie in x finden:<br>- min: x = 0 (mehr Sicherheitsmarge)<br>- max: x = max (weniger Sicherheitsraum)<br>- Nummer: Spezifische X -Koordinate | min / max / number | Max |
| Variable_nozzle_prime_start_y | Wo kann man unsere Säuberlinie in y finden:<br>- min: y = 0 (mehr Sicherheitsmarge)<br>- max: y = max (weniger Sicherheitsraum)<br>- Nummer: Koordinate und spezifisch | min / max / number | min |
| Variable_nozzle_prime_direction | Zeilen- oder Drop -Adresse:<br>- rückwärts: nach vorne<br>- Vorwärts: Rückwärts<br>- Auto: Auf dem Zentrum nach VARIABLE_NAZZLE_PRIME_START_Y | Automatisch / vorwärts / rückwärts | Auto |

#### Drehbelastung/Entladung

In diesem Fall erleichtert diese Gruppe von Variablen die Verwaltung der Belastung und Entladung unseres Filaments beispielsweise für die Emulation des M600 oder durch Start der Lade- und Entladungsmakros des Filaments:

| Variable                        | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                     | Mögliche Werte | Standardwert |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| variable_filament_unload_length | Wie viel Abzug in MM das Filament, stellen Sie sich an Ihre Maschine ein, normalerweise die Maßnahme von Ihrer Düse bis zu den Zahnrädern Ihres Extruders, indem Sie einen zusätzlichen Rand hinzufügen.                                                                                                                                                                                                                         | Nummer         | 130          |
| variable_filament_unload_speed  | Die Rückzugsgeschwindigkeit des Filaments in mm/s normalerweise wird eine langsame Geschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                    | Nummer         | 5            |
| variable_filament_load_length   | Entfernung in MM zum Laden des neuen Filaments ... wie in varable_filament_unload_Length werden wir das Maß aus Ihrem Extruder -Gang verwenden, was einen zusätzlichen Rand hinzufügt. In diesem Fall hängt dieser zusätzliche Wert davon ab, wie viel Sie reinigen möchten ... Sie können ihm normalerweise mehr Rand als den vorherigen Wert geben, um sicherzustellen, dass die Extrusion des Vorderfilaments gereinigt wird. | Nummer         | 150          |
| variable_filament_load_speed    | Die Filamentlastgeschwindigkeit in mm/s normalerweise wird eine schnellere Geschwindigkeit zur Entlassung verwendet.                                                                                                                                                                                                                                                                                                             | Nummer         | 10           |

> ⚠️**Beachten!!!**Eine weitere Anpassung, die für Ihren Abschnitt erforderlich ist**[Extruder]**das angegeben[**max_extrode_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... Der ratsame Wert beträgt normalerweise> 101 (falls er nicht definiert ist, verwendet 50), um beispielsweise die typischen Extruderkalibrierungstests zuzulassen.  
> Sie sollten den Wert basierend auf der oben genannten Test oder der Konfiguration Ihrer anpassen**variable_filament_unload_length**ICH**variable_filament_load_length**.

#### Parken

In bestimmten Prozessen unseres Druckers, wie der Freizeit, ist es ratsam, einen Parkplatz aus dem Kopf zu machen. Die Makros unseres Bundle haben diese Option zusätzlich zu den folgenden Variablen zum Verwalten:

| Variable                           | Beschreibung                                                                                                                                                                                                                                                        | Mögliche Werte | Standardwert |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| variable_start_print_park_in       | Ort, an dem der Kopf während der Vorabstufung parken kann.                                                                                                                                                                                                          | zurück /       |              |
| Zentrum /                          |                                                                                                                                                                                                                                                                     |                |              |
| Front                              | zurück                                                                                                                                                                                                                                                              |                |              |
| variable_start_print_park_z_height | Z Höhe während vorhörig                                                                                                                                                                                                                                             | Nummer         | 50           |
| variable_end_print_park_in         | Standort, um den Kopf am Ende zu parken oder einen Eindruck abzusagen.                                                                                                                                                                                              | zurück /       |              |
| Zentrum /                          |                                                                                                                                                                                                                                                                     |                |              |
| Front                              | zurück                                                                                                                                                                                                                                                              |                |              |
| variable_end_print_park_z_hop      | Entfernung, um am Ende des Eindrucks zu gehen.                                                                                                                                                                                                                      | Nummer         | 20           |
| variable_pause_print_park_in       | Lage, den Kopf mit Pausar zu parken, den Eindruck.                                                                                                                                                                                                                  | zurück /       |              |
| Zentrum /                          |                                                                                                                                                                                                                                                                     |                |              |
| Front                              | zurück                                                                                                                                                                                                                                                              |                |              |
| variable_pause_idle_timeout        | Wert, in Sekunden, der Aktivierung des Inaktivitätsprozesses in der Maschine, die Motoren freigibt und Koordinaten verlieren,**Ein hoher Wert ist ratsam, das Pause -Makro ausreichend zu aktivieren, um Maßnahmen auszuführen, bevor Koordinaten verloren gehen.** | Nummer         | 43200        |

#### Z-Tilt

Nehmen Sie das Beste aus unserer Maschine, damit sie selbstniveau ist und erleichtert, dass unsere Maschine immer in den besten Bedingungen ist.

**Z-Tilt ist im Grunde ein Prozess, der uns hilft, unsere Z-Motoren in Bezug auf unsere/gantry x (kartesische) oder XY (COREXY) Achse (Corexy) auszurichten**. Damit**Wir versichern, dass wir unser Z immer perfekt und präzise und automatisch haben**.

| Variable                  | Beschreibung                                                                                          | Mögliche Werte | Standardwert |
| ------------------------- | ----------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| variable_calibrate_z_tilt | Es ermöglicht, wenn es in unserer Klipper-Konfiguration aktiviert ist, den Z-Tilt-Einstellungsprozess | Wahr / falsch  | FALSCH       |

#### Schief

Die Verwendung von[Schief](broken-reference)Für die Korrektur oder genaue Anpassung unserer Drucker ist es äußerst ratsam, wenn wir Abweichungen in unseren Eindrücken haben. Mithilfe der folgenden Variablen können wir in unseren Makros die Verwendung zulassen:

| Variable              | Beschreibung                                                                                                                                                                                                                                   | Mögliche Werte | Standardwert    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------- |
| variable_skew_profile | Es ermöglicht uns, unser Verschleierungsprofil zu berücksichtigen, das in unserem Makro start_print berechnet wird. Um es zu aktivieren, müssen wir die Variable diskutieren und den Namen des Schiefeprofils unserer Konfiguration verwenden. | Text           | my_skew_profile |

### Anpassung von Makros

Unser Klipper -Modul verwendet das in Zeiten verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper im Konfigurationsdateiprozess nacheinander. Aus diesem Grund sind die Reihenfolge der Einschlüsse und personalisierten Anpassungen, die wir für diese Module anwenden möchten, unerlässlich.

> ℹ️**INFO!!!**Bei Verwendung von 3DWork-Einstellungen als Modul können sie nicht direkt aus dem Verzeichnis 3DWORK-Klipper in Ihrem KLIPPER-Konfigurationsverzeichnis bearbeitet werden, da es nur zur Sicherheit in schreibgeschützt ist (nur auf Lesen beschränkt).
>
> Aus diesem Grund ist es sehr wichtig, die Funktion von Klipper zu verstehen und wie Sie unsere Module an Ihre Maschine anpassen können.

#### **Variablen personalisieren**

Normalerweise müssen wir uns anpassen, um Anpassungen an den Variablen vorzunehmen, die wir standardmäßig in unserem Modul haben**3dwork**Para schneidet.

Einfach müssen wir den Makroinhalt einfügen**[gcode_macro global_vars]**Das finden wir in Makros/Makros var globals.cfg in unserem Drucker.cfg.

Wir erinnern Sie daran, was zuvor kommentiert wurde, wie Klipper die Konfigurationen nacheinander verarbeitet. Daher ist es ratsam, sie nach dem Includen zu fügen, das wir Ihnen sagen,[Hier](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Wir werden so etwas haben (es ist nur ein visuelles Beispiel):

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

> ⚠️**Beachten!!!**Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.

> ℹ️**INFO!!!**
>
> -   Wir empfehlen Ihnen, Kommentare hinzuzufügen, wie Sie im vorherigen Fall sehen, um zu ermitteln, was jeder Abschnitt macht
> -   Obwohl Sie nicht alle Variablen berühren müssen, empfehlen wir Ihnen, den gesamten Inhalt von zu kopieren**[gcode_macro global_vars]**

#### Makros personalisieren

Makros haben modular montiert, damit sie auf einfache Weise angepasst werden können. Wie bereits erwähnt, müssen wir, wenn wir sie anpassen möchten, genau wie bei den Variablen fortfahren, das fragliche Makro in unserem Drucker kopieren.

Wir haben zwei Gruppen von Makros:

-   Makros Um Benutzereinstellungen hinzuzufügen, können diese Makros einfach hinzugefügt und angepasst werden, da sie hinzugefügt wurden, sodass jeder Benutzer die Aktionen in bestimmten Teilen der Prozesse, die jedes Makro durchführt, nach seinen Vorlieben anpassen kann.

**Start_print**

| Makroname                                 | Beschreibung                                                                                                                 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| \_User_start_print_heat_chamber           | Es läuft kurz nachdem unser Gehäuse beginnt zu wärmen, wenn Chamber_Temp als Parameter an unseren Start_print übergeben wird |
| \_User_start_print_before_homing          | Es wird vor dem anfänglichen Homing zum Start des Druckens ausgeführt                                                        |
| \_User_start_print_after_heating_bed      | Es läuft, wenn unser Bett bei seiner Temperatur ankommt, bevor \_start_print_after_heating_bed                               |
| \_User\_ start_print Bed_Mesh             | Es wird vor \_start_print_bed_mesh gestartet                                                                                 |
| \_User_start_print_park                   | Es wird vor \_start_print_park gestartet                                                                                     |
| \_User_start_print_after_heating_extruder | SE Lanza Antes de \_start_print_after_heating_extruder                                                                       |

**End_print**

| Makroname                           | Beschreibung                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------ |
| \_User_end_print_before_heaters_off | Es wird vor der Ausführung der Heizung vor \_end_print_before_heaters_off ausgeführt |
| \_User_end_print_after_heaters_off  | Es läuft nach dem Erhitzen vor \_end_print_after_heaters_off                         |
| \_User_end_print_park               | Es wird vor dem Kopf des Kopfes vor \_end_print_park ausgeführt                      |

**Print_basics**

| Makroname           | Beschreibung                                    |
| ------------------- | ----------------------------------------------- |
| \_User_pause_start  | Wird zu Beginn einer Pause ausgeführt           |
| \_USER_PAUSE_END    | Es läuft am Ende einer Pause                    |
| \_User_resume_start | Wird zu Beginn einer Zusammenfassung ausgeführt |
| \_User_resume_end   | Läuft am Ende einer Zusammenfassung             |

-   Interne Makros sind Makros, um das Hauptmakro in Prozesse zu unterteilen, und ist dafür wichtig. Es ist ratsam, dass diese bei Bedürfnissen, diese wie sie sind, kopiert werden.

**Start_print**

| Makroname                            | Beschreibung                                                                                                                                                                            |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_Start_print_heat_chamber           | Erhitzt das Gehäuse, falls der Parameter chamber_temp vom makro start_print vom laminator empfangen wird                                                                                |
| \_Start_print_after_heating_bed      | Es läuft, wenn das Bett nach \_user_start_print_after_heating_bed. Normalerweise wird es für die Verarbeitung der Bettkalibrierung verwendet (z_tilt_adjust, quad_gantry_leveling, ...) |
| \_Start_print_bed_mesh               | Er ist verantwortlich für die Logik des Bettes Elend.                                                                                                                                   |
| \_Start_print_park                   | Berufet den Druckkopf beim Erhitzen der Düse bei der Drucktemperatur.                                                                                                                   |
| \_Start_print_after_heating_extruder | Machen Sie die Nazzle -Säuber                                                                                                                                                           |

## Drucker und elektronisch

Da wir mit verschiedenen Modellen von Druckern und Elektronik arbeiten, werden wir diejenigen hinzufügen, die nicht direkt von Zeiten unterstützt werden, unabhängig davon, ob sie Beiträge oder die Gemeinschaft sind.

-   Drucker, in diesem Verzeichnis haben wir alle Konfigurationen des Druckers
-   Boards, hier finden wir Elektronik

### Parameter und Stifte

Unser Klipper -Modul verwendet das in Zeiten verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper im Konfigurationsdateiprozess nacheinander. Aus diesem Grund sind die Reihenfolge der Einschlüsse und personalisierten Anpassungen, die wir für diese Module anwenden möchten, unerlässlich.

> ℹ️**INFO!!!**Bei Verwendung von 3DWork-Einstellungen als Modul können sie nicht direkt aus dem Verzeichnis 3DWORK-Klipper in Ihrem KLIPPER-Konfigurationsverzeichnis bearbeitet werden, da es nur zur Sicherheit in schreibgeschützt ist (nur auf Lesen beschränkt).
>
> Aus diesem Grund ist es sehr wichtig, die Funktion von Klipper zu verstehen und wie Sie unsere Module an Ihre Maschine anpassen können.

Wie wir in "erklärten"[Makros personalisieren](3dwork-klipper-bundle.md#personalizando-macros)"Wir werden denselben Prozess verwenden, um Parameter oder Stifte anzupassen, um sie an unsere Anforderungen anzupassen.

#### Personalisierungsparameter

Wenn wir Ihnen empfehlen, einen Abschnitt in Ihrem Drucker zu erstellen.CFG, der als Benutzerüberschreibungen bezeichnet wird und nach dem Include in unsere Konfigurationen platziert wird, um in der Lage zu sein, alle darin verwendeten Parameter anzupassen und anzupassen.

Im folgenden Beispiel werden wir in unserem Fall sehen, wie wir die Parameter unserer Bettnivellierung (BED_MEH) an die Anpassung der Umfragepunkte (Sonde_Count) in Bezug auf die Konfiguration anpassen möchten, die wir standardmäßig in den Konfigurationen unseres Klipper -Moduls haben:

**drucker.cfg**

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

> ⚠️**Beachten!!!**Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.

Wir können diesen Vorgang mit jedem Parameter verwenden, den wir anpassen möchten.

#### Anpassen der Kiefernkonfiguration

Wir werden genau so vorgehen, wie wir es zuvor getan haben. In unserem Benutzerüberschreibungsbereich werden wir diese Abschnitte von Stiften hinzufügen, die wir uns an unseren Geschmack anpassen möchten.

Im folgenden Beispiel werden wir anpassen, was der Pin unseres Electronics -Lüfters (Controller_Fan) ist, um ihn einem anderen von Standard zuzuweisen:

**drucker.cfg**

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

> ⚠️**Beachten!!!**Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.
