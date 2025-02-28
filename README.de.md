* * *

## Beschreibung: Makros -Paket, Konfigurationen und andere Dienstprogramme für Klipper

# 3dwork Clope Bündel

[<img width="171" alt="kofi" src="https://github.com/3dwork-io/3dwork-klipper/blob/master/Ko-fi-Logo.png">](https://ko-fi.com/jjr3d)

[![](../../.gitbook/assets/image%20(1986).png)- Englisch](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{ % Hint style = "Danger" %}  
**Leitfaden im Prozess !!! Obwohl Makros völlig funktionsfähig sind, sind diese in kontinuierlicher Entwicklung.**

**Verwenden Sie sie unter Ihrer eigenen Verantwortung !!!**  
{% von EndHint%}

Changelog

12/07/2023 - Support für die Automatisierung der Erstellung von elektronischen BigReteech -Firmware hinzugefügt

Aus**3dwork**Wir haben eine Reihe von Makros, Maschinen- und elektronischen Konfigurationen sowie andere Tools für eine einfache und leistungsstarke Verwaltung von Klipper zusammengestellt und angepasst.

Ein Großteil dieses Pakets basiert auf[**Ratten**](https://os.ratrig.com/)Verbesserung der Parteien, die wir für interessant halten, sowie andere Beiträge der Gemeinschaft.

## Installation

Um unser Paket für Klipper zu installieren, werden wir die folgenden Schritte ausführen

### Entladung des Repositorys

Wir werden eine Verbindung zu unserem Host mit SSH herstellen und die folgenden Befehle starten:

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{ % Hint style = "Warnung" %}  
Wenn das Verzeichnis Ihrer Klipper -Konfiguration angepasst wird, denken Sie daran, den ersten Befehl ordnungsgemäß an Ihre Installation anzupassen.  
{% von EndHint%}

{ % Hint style = "info" %}  
In neuen Einrichtungen:

Da Klipper den Zugriff auf Makros erst zulässt, wenn es einen korrekten Drucker hat.

-   Wir versichern uns, dass wir unsere haben[Gastgeber als zweite MCU](raspberry-como-segunda-mcu.md)
-   Als nächstes fügen wir einen Drucker hinzu.


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

Damit können wir Klipper starten, um auf unsere Makros zuzugreifen.  
{% von EndHint%}

### Verwenden von Moonraker, um immer aktualisiert zu werden

Vielen Dank an Moonraker können sein Update nutzen_Manager, um über die Verbesserungen auf dem neuesten Stand zu sein, die wir in Zukunft vorstellen können.

Von MainSail/Fluidd bearbeiten wir unseren Moonraker.conf (es sollte auf der gleichen Höhe wie bei Ihrem Drucker sein) und wir werden am Ende der Konfigurationsdatei hinzufügen:

    [include 3dwork-klipper/moonraker.conf]

{ % Hint style = "Warnung" %}  
**Denken Sie daran, den Installationsschritt zuvor zu machen, wenn Sie keinen Fehler generieren und nicht starten können.**

**Denken Sie hingegen daran, den Pfad ordnungsgemäß an Ihre Installation anzupassen.**  
{% von EndHint%}

## Makros

Wir haben immer kommentiert, dass Times eine der besten Verteilungen von Klipper mit Raspberry -Support und CB1 -Modulen ist, hauptsächlich aufgrund seiner modularen Konfigurationen und seiner großen Makros.

Einige zusätzliche Makros, die nützlich sein werden:

### **Makros für den allgemeinen Gebrauch**

| Makro                                                                                 | Beschreibung                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VIELLEICHT_HEIM**                                                                   | Es ermöglicht es uns, den Homing -Prozess nur durch diese in den Achsen zu optimieren, die nicht mit Homing enthalten sind.                                                                               |
| **PAUSE**                                                                             | Durch verwandte Variablen können wir eine Pause mit einem vielseitigeren Kopfparkplatz mit normalem Makros verwalten.                                                                                     |
| **SATZ_PAUSE_BEI_SCHICHT**                                                            |                                                                                                                                                                                                           |
| **SATZ_PAUSE_BEI_NÄCHSTE_SCHICHT**                                                    | Ein sehr nützliches Makro, das Hauptsegel in seine Benutzeroberfläche integriert, um in einer bestimmten Ebene auf Bedarf innehalten zu können ... falls wir beim Ausführen des Laminats vergessen haben. |
| Wir haben auch einen anderen, um das gemächliche in der nächsten Schicht auszuführen. |                                                                                                                                                                                                           |
| **WIEDER AUFNEHMEN**                                                                  | Verbessert, da es ermöglicht, festzustellen, ob unsere Düse nicht an der Extrusionstemperatur liegt, um sie zu lösen, bevor sie einen Fehler aufweist und unseren Eindruck schädigt.                      |
| **STORNIEREN_DRUCKEN**                                                                | Dies ermöglicht die Verwendung des Restes der Makros, eine Abdrehungsstörung korrekt durchzuführen.                                                                                                       |

-   **Stattdessen in der Pause**, sehr interessante Makros, die es uns ermöglichen, einen gemächlichen in einer Ebene geplant zu machen oder einen Befehl zu starten, wenn wir die nächste Schicht starten.   
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    Ein weiterer Vorteil von ihnen besteht darin, dass sie in das Mainsegel mit den neuen Funktionen in unserer Benutzeroberfläche integriert sind, wie Sie unten sehen können:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Druckverwaltung Makros**

| Makro                                                                                    | Beschreibung                                                                                                                                            |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **START_DRUCKEN**                                                                        | Es ermöglicht es uns, unsere Eindrücke auf sichere Weise und im Klipper -Stil zu starten. In diesem Fall finden wir einige interessante Funktionen wie: |
| -vorgewärmt von intelligenter Düse bei einem Sondensensor                                |                                                                                                                                                         |
| -Möglichkeit der Verwendung von Z-Tilt durch Variable                                    |                                                                                                                                                         |
| -Adaptives Bett Molelada, gezwungen aus der Una Malla gezwungen, gehalten                |                                                                                                                                                         |
| -Anpassbare Säuberung zwischen normaler, adaptiver Säuberungslinie oder Säuberungsabfall |                                                                                                                                                         |
| -Segmentiertes Makro, um personalisieren zu können, wie wir Ihnen später zeigen werden   |                                                                                                                                                         |
| **ENDE_DRUCKEN**                                                                         | Makro des Drucks des Drucks, bei dem wir auch eine Segmentierung haben, um unser Makro anzupassen. Wir haben auch einen dynamischen Kopf des Kopfes.    |

-   **Adaptive Bettrolle**Dank der Vielseitigkeit von Klipper können wir Dinge tun, die heute unmöglich erscheinen ... Ein wichtiger Prozess des Eindrucks ist es, eine Mahlzeit von Abweichungen von unserem Bett zu haben, die es uns ermöglichen, diese zu korrigieren, um eine Einhaltung der perfekten ersten Schichten zu haben.   
    Bei vielen Gelegenheiten machen wir diesen Malley vor den Eindrücken, um sicherzustellen, dass es richtig funktioniert, und dies erfolgt auf der gesamten Oberfläche unseres Bettes.  
    Mit dem Elend des adaptiven Bettes wird es in der Druckzone durchgeführt, was es viel präziser macht als die traditionelle Methode ... In den folgenden Fängen werden wir die Unterschiede eines traditionellen und adaptiven Netzes sehen.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Filamentverwaltung Makros**

Makros, die es uns ermöglichen, verschiedene Aktionen mit unserem Filament wie der Last oder Entladung davon zu verwalten.

| Makro                 | Beschreibung                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Der M600**          | Es ermöglicht uns die Kompatibilität mit dem M600 -Gcode, der normalerweise in Laminatoren für die Änderung des Filaments verwendet wird. |
| **ENTLADEN_Filament** | Konfigurierbar über die Variablen ermöglicht es uns, assistierte Filamente herunterzuladen.                                               |
| **LADEN_Filament**    | Sowie die vorherige, aber im Zusammenhang mit der Last des Filaments.                                                                     |

### **Filamentspulenverwaltung Makros (Spoolman)**

{ % Hint style = "Warnung" %}  
**Abschnitt im Prozess !!!**  
{% von EndHint%}

[**Spoolman**](https://github.com/Donkie/Spoolman)Er ist ein Filamentspulenmanager, der in Moonraker integriert ist und es uns ermöglicht, unsere Aktien und Verfügbarkeit von Filamenten zu verwalten.

!\[](../../.gitbook/assets/image (1990) .png)

Wir werden die Installation und Konfiguration nicht eingeben, da sie mit dem relativ einfach ist[**Anweisungen Ihres Githubs**](https://github.com/Donkie/Spoolman)**,**In jedem Fall**Wir empfehlen Ihnen, Docker zu verwenden**Durch Einfachheit und Erinnerung**Aktivieren Sie die Konfiguration in Moonraker**erforderlich:

{ % Code title = "mondraker.conf" %}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{ % Endcode %}

| Makro            | Beschreibung                                                                           |
| ---------------- | -------------------------------------------------------------------------------------- |
| SATZ_AKTIV_SPULE | Es ermöglicht uns anzunehmen, welches ID der Spule verwendet wird, um sie zu verwenden |
| KLAR_AKTIV_SPULE | Ermöglicht es uns, die aktive Spule zurückzusetzen                                     |

Das Ideal in jedem Fall wäre, unseren Laminator hinzuzufügen,**Im Filament -GCODES für jede Spule den Aufruf dazu**und erinnere dich**Ändern Sie die ID davon einst konsumiert**Um den Rest des Filaments darin kontrollieren zu können !!!

!\[](../../.gitbook/assets/image (1991) .png)

### **Makros der Oberflächenmanagement aus Druckdrucken**

{ % Hint style = "Warnung" %}  
**Abschnitt im Prozess !!!**  
{% von EndHint%}

In der Regel ist es normal, dass wir je nach Finish, die wir haben möchten, oder der Art des Filaments unterschiedliche Druckflächen haben.

Dieser Satz von Makros, erstellt von[Garethky](https://github.com/garethky)Sie ermöglichen es uns, diese und insbesondere die korrekte Einstellung von Zoffset in jedem von ihnen in dem Stil zu haben, den wir in Prise -Maschinen haben. Unten können Sie einige Ihrer Funktionen sehen:

-   Wir können die Anzahl der gewünschten Druckoberflächen speichern, die jeweils einen eindeutigen Namen haben
-   Jede Druckoberfläche hat einen eigenen Zoffset
-   Wenn wir während eines Eindrucks (Babystepping) von unserem Klipper Z -Einstellungen vornehmen

Andererseits haben wir einige**Anforderungen an die Implementierung (Versuchen Sie, die Logik des Drucks hinzuzufügen_Starten Sie das Bundle in Zukunft, um diese Funktion durch Variable zu aktivieren und ein früheres und posteriores Benutzermakro zu erstellen, um Benutzerereignisse einzulegen).**:

-   Die Verwendung von\[speichern_Variablen]In unserem Fall werden wir ~/variablen.cfg verwenden, um die Variablen zu speichern, und das liegt bereits innerhalb des CFG dieser Makros.   
    Dadurch wird automatisch eine variable Datei erstellt_bauen_Sheets.cfg Wo werden Sie unsere Scheibenvariablen behalten.

{ % code title = "Beispiel für Variablen -Konfigurationsdatei" %}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{ % Endcode %}

-   Wir müssen einen Anrufantrag beigeben_BAUEN_BLATT_Anpassung in unserem Druck_Beginnen Sie in der Lage, das ausgewählte Oberflächenzoffset aufzutragen können
-   Es ist wichtig, dass sich für das vordere Makro anwenden,\_BAUEN_BLATT_Anpassung, ordnungsgemäß arbeiten Wir müssen einen Satz hinzufügen_Gcode_Offset z = 0.0 Kurz vor dem Aufrufen anwenden_BAUEN_BLATT_EINSTELLUNG


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

Andererseits ist es interessant, einige Makros zu haben, um die eine oder andere Oberfläche zu aktivieren oder sogar als Parameter von unserem Laminator an verschiedene Drucker- oder Filamentprofile zu übergeben, um die eine oder andere automatisch laden zu können:

{ % Hint style = "Warnung" %}  
Es ist wichtig, dass der Wert in name = "xxxx" mit dem Namen zusammenfällt, den wir bei der Installation unserer Druckoberfläche angegeben haben  
{% von EndHint%}

{ % code title = "drucker.cfg oder integrieren cfg" %}

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

{ % Endcode %}

Auch im Falle von Klipperscreen können wir ein bestimmtes Menü hinzufügen, um die Last der verschiedenen Oberflächen verwalten zu können, wobei wir einen Aufruf an die zuvor für die Belastung jeder Oberfläche erstellten Makros aufnehmen können:

{% code title = "~/drucker_Data/config/klipperscreen.conf " %}

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

{ % Endcode %}

| Makro                            | Beschreibung |
| -------------------------------- | ------------ |
| INSTALLIEREN_BAUEN_BLATT         |              |
| ZEIGEN_BAUEN_BLATT               |              |
| ZEIGEN_BAUEN_Blätter             |              |
| SATZ_BAUEN_BLATT_Offset          |              |
| ZURÜCKSETZEN_BAUEN_BLATT_Offset  |              |
| SATZ_Gcode_Offset                |              |
| ANWENDEN_BAUEN_BLATT_EINSTELLUNG |              |

### **Maschinenmakros**

| Makro                                                         | Beschreibung                                                                                                                                                                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KOMPILIEREN_Firmware**                                      | Mit diesem Makro können wir die Klipper -Firmware auf einfache Weise kompilieren, die Firmware für mehr Einfachheit aus der Benutzeroberfläche zugänglich machen und sie auf unsere Elektronik anwenden können.                 |
| Hier haben Sie mehr Details der elektronischen Unterstützung. |                                                                                                                                                                                                                                 |
| **BERECHNEN_BETT_Netz**                                       | Ein äußerst nützliches Makro zur Berechnung des Bereichs für unser Netz, da es manchmal ein komplizierter Prozess sein kann.                                                                                                    |
| **PID_ALLE**                                                  |                                                                                                                                                                                                                                 |
| **PID_Extruder**                                              |                                                                                                                                                                                                                                 |
| **PID_BETT**                                                  | Diese Makros, bei denen wir die Temperaturen für die PID in Form von Parametern übergeben können, ermöglichen es uns, die Temperaturkalibrierung auf extrem einfache Weise durchzuführen.                                       |
| **PRÜFEN_GESCHWINDIGKEIT**                                    |                                                                                                                                                                                                                                 |
| **PRÜFEN_GESCHWINDIGKEIT_DELTA**                              | Originalmakro des Partners[Ellis](https://github.com/AndrewEllis93)Sie ermöglichen uns auf eine recht einfache Weise, die Geschwindigkeit zu testen, mit der wir unsere Maschine genau und ohne Schritteverlust bewegen können. |

-   **Firmware -Zusammenstellung für unterstützte Elektronik**Um den Prozess der Erstellung und Wartung unserer Klipper -Firmware für unsere MCU zu erleichtern, haben wir das Makrokompilieren_Firmware, dass wir bei der Ausführung unsere Elektronik als Parameter verwenden können, um nur dies zu tun, wird Klipper für alle elektronischen, die von unserem Bündel unterstützt werden:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Wir werden diese auf unserer UI -Website im Firmware -Verzeichnis leicht zugänglich finden_Binärdateien in unserer Registerkarte Maschine (wenn wir Hauptsegel verwenden):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Dann haben Sie die Liste der unterstützten elektronischen:

**WICHTIG!!!**

Diese Skripte sind bereit, mit PI -Benutzer an einem Raspbian -System zu arbeiten. Wenn es nicht Ihr Fall ist, müssen Sie es anpassen.

Firmawares werden zur Verwendung mit USB -Verbindung generiert, die immer das ist, was wir empfehlen. Außerdem ist der USB -Montagepunkt immer gleich, indem Ihre Konfiguration Ihrer MCU -Verbindung nicht geändert wird, wenn sie mit unserem Makro/Skript generiert werden

**So dass Klipper Shell -Makros ausführen kann, dank des Partners muss eine Erweiterung installiert werden**[**Arksin**](https://github.com/Arksine)**, lass es.**

**Abhängig vom gebrauchten Klipper -Dystro können sie bereits aktiviert werden.**

![](../../.gitbook/assets/image%20(770).png)

Der einfachste Weg ist die Verwendung[**Kioh**](../instalacion/#instalando-kiauh)Wo wir in einer Ihrer Optionen die Möglichkeit haben, diese Erweiterung zu installieren:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Wir können den Prozess auch von Hand ausführen. Wir werden das Plugin für Klipper manuell kopieren[**Gcode_Hülse_Verlängerung**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)In unserem Verzeichnis`_**~/klipper/klippy/extras**_`Mit SSH SCP Y starten wir Klipper neu.

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
| SKR Pro v1.2            | Skr_pro_12                       |
| Skr 3                   | BTT_Skr_3                        |
| Saqr a (heha)           | Smarted                          |
| Skr 3 dies              | BTT-SC-3-EZ                      |
| SKR 3 this (H723)       | Skirzhahah                       |
| SKR 2 (429)             | BTT-SRC-2-429                    |
| SKR 2 (407)             | BTT-SRC-2-407                    |
| Schreit                 | BTT-SKRAT-10                     |
| Von 1,4 Turbo           | BTT-SC-14-Turbo                  |
| Skri Mini               | BTT_Skr_Mini_ez_30               |

| Toolhead (CAN) | Parametername im Makro verwendet |
| -------------- | -------------------------------- |
| EBB42 V1       | BTT_Ebb42_10                     |
| Ebb36 v1       | BTT_Ebb36_10                     |
| EBB42 V1.1     | BTT_Ebb42_11                     |
| EBB36 V1.1     | BTT_Ebb36_11                     |
| EBB42 V1.2     | BTT_Ebb42_12                     |
| Ebb36 v1.2     | BTT_Ebb36_12                     |

| **Elektronisch**             | **Parametername im Makro verwendet** |
| ---------------------------- | ------------------------------------ |
| MKS Eagle v1.x               | MKS-EEGLE-10                         |
| MCS Robin Nano backt         | MKS-Robin-Nano-30                    |
| MKS Robin Nano V2            | MKS-Robin-Nano-20                    |
| Mks gen l                    | MKS-General-l                        |
| Die Schuld von Robin Nano DU | ZnP_Robin_Nano_dw_Kategorie          |

| Toolhead (CAN)    | Parametername im Makro verwendet |
| ----------------- | -------------------------------- |
| Mellow Fly SHT 42 | weich_fliegen_Zeuge_42           |
| Mellow Fly SHT 36 | weich_fliegen_Zeuge_36           |

| Elektronisch  | Parametername im Makro verwendet |
| ------------- | -------------------------------- |
| Fysetc Spider | fysetc_Spinne                    |

### Hinzufügen von 3DWork -Makros zu unserer Installation

Von unserer Schnittstelle, Mainseail/Fluidd, werden wir unseren Drucker.CFG bearbeiten und hinzufügen:

{ % code title = "drucker.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{ % Endcode %}

{ % Hint style = "info" %}  
Es ist wichtig, dass wir diese Zeilen am Ende unserer Konfigurationsdatei hinzufügen ... direkt über dem Abschnitt, so dass im Fall von Makros in unserem CFG oder einbezogen werden oder diese von uns überfordert sind:  
#\*# \\ &lt;---------------------- Speichern_Config ---------------------->  
{% von EndHint%}

{ % Hint style = "Warnung" %}  
Normale Makros wurden von getrennt von**Makros -Shell**Angesichts dessen**Um diese zu aktivieren, müssen zusätzlich manuelle Schritte durchgeführt werden, die derzeit testen**Und\*\*Möglicherweise erfordern sie zusätzliche Berechtigungen, um Ausführungsberechtigungen zuzuweisen, für die die Anweisungen nicht angegeben wurden, da versucht wird, zu automatisieren.\*\*  
**Wenn Sie sie verwenden, liegt es in Ihrer eigenen Verantwortung.**  
{% von EndHint%}

### Einstellungen unseres Laminators

Da unsere Makros dynamisch sind, extrahieren sie bestimmte Informationen aus unserer Druckerkonfiguration und dem Laminator selbst. Dazu raten wir Ihnen, Ihre Laminatoren wie folgt zu konfigurieren:

-   **Start Start GCODE_DRUCKEN**Verwenden Sie Platzhalter, um die Filament- und Betttemperaturwerte dynamisch zu übergeben:

{ % Tabs %}  
{ % tab title = "prusaslicer-superslicer" %}  
**Prusaslicer**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**Superslicer**- Wir haben die Möglichkeit, die Gehäusetemperatur (Kammer) einzustellen,

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{ % endTab %}

{ % tab title = "Bambu Studio/Orcaslicer" %}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760) .png) { % endTab %}

{ % tab title = "cura" %}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{ % Hint style = "Warnung" %}  
Wir müssen das Plugin installieren[**Post -Prozess -Plugin (von Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)Aus der Speisekarte_**Hilfe/Show**_Konfigurationsordner ... Wir kopieren das vorherige Linkskript im Skriptordner.   
Wir starten die Heilung neu und wir werden gehen_**Erweiterungen/Postverarbeitung/Ändern des G-Code**_Und wir werden auswählen_**Maschendruckgröße**_.  
{% von EndHint%}  
{ % endTab %}

{ % tab title = "ideamaker" %}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{ % endTab %}

{ % tab title = "simimifify3d" %}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{ % endTab %}  
{ % endtabs %}

{ % Hint style = "info" %}  
Der**Platzhalter sind "AKA" oder Variable**des Druckens.

In den folgenden Links finden Sie eine Liste davon für:[**Prusaslicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Superslicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(zusätzlich zu denen des vorherigen),[**Studio Bambus**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)Und[**Behandlung**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

Die Verwendung dieser ermöglicht es unseren Makros, dynamisch zu sein.  
{% von EndHint%}

-   **GCODE DE Final End_DRUCKEN**In diesem Fall ist es für alle Laminatoren häufig


    END_PRINT

### Variablen

Wie wir bereits erwähnt haben, ermöglichen diese neuen Makros uns einige sehr nützliche Funktionen, wie wir zuvor auflisten.

Um unsere Maschine anzupassen, werden wir die Variablen verwenden, die wir in Makros/Makros finden werden_unser_Globals.cfg und das detailliert unten.

#### Nachrichten-/Benachrichtigungssprache

Da viele Benutzer die Benachrichtigungen über Makros in ihrer Sprache haben, haben wir ein Multisprachel-Benachrichtigungssystem entwickelt, derzeit Spanisch (en) und Englisch (EN). In der folgenden Variablen können wir es anpassen:

| Variable         | Beschreibung                                                                                                                       | Mögliche Werte | Standardwert |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Sprache | Es ermöglicht uns, die Sprache der Benachrichtigungen auszuwählen. Bei nicht gut definierter Fall wird es in (Englisch) verwendet. | Es ist / in    | es           |

#### Relative Extrusion

Ermöglicht Ihnen zu steuern, welchen Extrusionsmodus wir am Ende unseres Starts verwenden werden_Drucken. Der Wert hängt von der Konfiguration unseres Laminators ab.

{ % Hint style = "Erfolg" %}  
Es ist ratsam, Ihren Laminator für die Verwendung der relativen Extrusion zu konfigurieren und diese Variable an True anzupassen.  
{% von EndHint%}

| Variable                   | Beschreibung                                                                       | Mögliche Werte | Standardwert |
| -------------------------- | ---------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_relativ_Extrusion | Es ermöglicht uns, den in unserem Laminator verwendeten Extrusionsmodus anzugeben. | Wahr / falsch  | WAHR         |

#### Geschwindigkeiten

Um die in Makros verwendeten Geschwindigkeiten zu verwalten.

| Variable                              | Beschreibung                                | Mögliche Werte | Standardwert |   |
| ------------------------------------- | ------------------------------------------- | -------------- | ------------ | - |
| Variable_Makro_reisen_Geschwindigkeit | Geschwindigkeit in übersetzter              | numerisch      | 150          |   |
| Variable_Makro_Mit_Geschwindigkeit    | Geschwindigkeit in übersetzter für Z -Achse | numerisch      | 15           |   |

#### Homing

Satz von Variablen im Zusammenhang mit dem Homing -Prozess.

| Variable | Beschreibung | Mögliche Werte | Standardwert |
| -------- | ------------ | -------------- | ------------ |

#### Heizung

Variablen im Zusammenhang mit dem Heizungsprozess unserer Maschine.

| Variable                                            | Beschreibung                                                                                                  | Mögliche Werte | Standardwert |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_vorheizen_Extruder                         | Aktivieren Sie die vorgeheizte Düse bei der in Variablen angegebenen Temperatur_vorheizen_Extruder_Temperatur | Wahr / falsch  | WAHR         |
| Variable_vorheizen_Extruder_Temperatur              | Düse vorgeheizte Temperatur                                                                                   | numerisch      | 150          |
| Variable_Start_drucken_Hitze_Kammer_Bett_Temperatur | Betttemperatur während des Erhitzens unseres Gehäuses                                                         | numerisch      | 100          |

{ % Hint style = "Erfolg" %}  
Vorteile der Verwendung der vorgeheizten Düse:

-   Es ermöglicht uns zusätzliche Zeit damit, dass das Bett seine Temperatur auf einheitliche Weise erreicht
-   Wenn wir einen Indizessensor verwenden, der keine Temperaturkompensation hat, können wir unsere Maßnahmen konsistenter und präziser machen
-   Es ermöglicht es, einen Rest des Filaments in der Düse zu mildern, was in bestimmten Konfigurationen zulässt, die übrig nicht die Aktivierung des Sensors beeinflussen  
    {% von EndHint%}

#### Bett Mali (Bettnetz)

Um den Nivellierungsprozess zu steuern, haben wir Variablen, die sehr nützlich sein können. Zum Beispiel können wir die Art der Nivellierung steuern, die wir verwenden möchten, indem wir immer ein neues Netz erstellen, ein zuvor gespeichertes Laden oder ein adaptives Netz verwenden.

| Variable                                                                                                                                              | Beschreibung                                                                                     | Mögliche Werte | Standardwert |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------- | ------------ |
| Variable_kalibrieren_Bett_Netz                                                                                                                        | Es ermöglicht uns zu wählen, welche Art von Malel wir in unserem Start verwenden werden_DRUCKEN: |                |              |
| -New Mesh, wird uns in jedem Eindruck zu einem Elend machen                                                                                           |                                                                                                  |                |              |
| -SpeicherndeMeh lädt ein gespeichertes Netz und führt die Bettumfrage nicht durch                                                                     |                                                                                                  |                |              |
| -Adaptiv, wird uns zu einem neuen Elend machen, aber an den Druckbereich angepasst, um unsere ersten Schichten bei vielen Gelegenheiten zu verbessern |                                                                                                  |                |              |
| -Nomesh, in dem Fall, dass wir keinen Sensor haben oder den Prozess verwenden, um den Prozess zu überspringen                                         | neues Netz / gespeichertes Netz / adaptiv / adaptiv /                                            |                |              |
| noma                                                                                                                                                  | adaptiv                                                                                          |                |              |
| Variable_Bett_Netz_Profil                                                                                                                             | Der Name für unser gespeichertes Netz verwendet                                                  | Text           | Standard     |

{ % Hint style = "Warnung" %}  
Wir empfehlen Ihnen, die adaptive Ebene zu verwenden, da es das Elend immer an die Größe unseres Eindrucks anpasst, sodass Sie einen angepassten Malelbereich haben.

Es ist wichtig, dass wir in unserem haben[Start -up GCODE](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), im Anruf nach unserem Start_Druckwerte drucken_Maximal drucken_Min.  
{% von EndHint%}

#### Gereinigt

Eine wichtige Phase unseres Druckenbeginns ist eine korrekte Säuberung unserer Düse, um Überreste des Filaments zu vermeiden, oder dass sie unseren Eindruck irgendwann beschädigen können. Dann haben Sie die Variablen, die an diesem Prozess beteiligt sind:

| Variable                                                                                                                                               | Beschreibung                                                | Mögliche Werte | Standardwert |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | -------------- | ------------ |
| Variable_Düse_Priming                                                                                                                                  | Wir können zwischen verschiedenen Reinheitsoptionen wählen: |                |              |
| -Primelline zeichnet die typische Säuberlinie                                                                                                          |                                                             |                |              |
| -Primelineadaptative erzeugt eine Säuberlinie, die sich mit Variablen an den Bereich des gedruckten Stücks anpasst_Düse_Priming_Objektdistanz als Rand |                                                             |                |              |
| -Primoblob macht uns einen Tropfen Filament in einer Ecke unseres sehr effektiven Bettes, um die Düse zu reinigen und sich leicht zurückzuziehen       |                                                             |                |              |
| Primeline /                                                                                                                                            |                                                             |                |              |

Prime Adaptive /   
PrimeBlob /   
FALSCH

| Primelinea adaptiv |  
| Variable_Düse_Priming_Objektdistanz | Wenn wir die adaptive Spülleitung verwenden, ist es der Rand zwischen der Säuberungslinie und dem gedruckten Objekt | numerisch | 5 |  
| Variable_Düse_Prime_Start_x | Wo wir unsere Säuberlinie finden wollen:  
-Min wird es bei x = 0 tun (plus ein kleiner Sicherheitsmarge)  
-Max wird es bei x = max (minus ein kleiner Sicherheitsmarge) tun  
-Die Nummer ist die X -Koordinate, in der die Säuberung lokalisiert werden soll min /   
max /   
Nummer | Max |  
| Variable_Düse_Prime_Start_und | Wo wir unsere Säuberlinie finden wollen:  
-Min wird es bei y = 0 tun (plus ein kleiner Sicherheitsmarge)  
-Max wird es bei y = max tun (weniger ein kleiner Sicherheitsmarge)  
-Die Nummer ist die Koordinate und wo die Säuberung | min /   
max /   
Nummer | min |  
| Variable_Düse_Prime_Richtung | Die Adresse unserer Linie oder Drop:  
-Rückwärts bewegt sich der Kopf zur Vorderseite des Druckers  
-Stürmer werden nach hinten gehen  
-Das Auto wird je nach Variable in die Mitte gehen_Düse_Prime_Start_und | Auto /   
vorwärts /   
rückwärts | Auto |

#### Dreh-/Entladung/Entladung

In diesem Fall erleichtert diese Gruppe von Variablen die Verwaltung der Belastung und Entladung unseres Filaments, das beispielsweise die zur Emulation des M600 verwendete Lade- und Entladungsmakros des Filaments starten:

| Variable                                   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Mögliche Werte | Standardwert |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ------------ |
| Variable_Filament_entladen_Länge           | Wie viel Abzug in MM das Filament, stellen Sie sich an Ihre Maschine ein, normalerweise die Maßnahme von Ihrer Düse bis zu den Zahnrädern Ihres Extruders, indem Sie einen zusätzlichen Rand hinzufügen.                                                                                                                                                                                                                                                     | Nummer         | 130          |
| Variable_Filament_entladen_Geschwindigkeit | Die Rückzugsgeschwindigkeit des Filaments in mm/s normalerweise wird eine langsame Geschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                                                | Nummer         | 5            |
| Variable_Filament_laden_Länge              | Entfernung in MM, um das neue Filament zu laden ... wie in der Variablen_Filament_entladen_Länge Wir werden die Maßnahme von Ihrem Gang zum Extruder verwenden, indem wir eine zusätzliche Marge hinzufügen. In diesem Fall hängt dieser zusätzliche Wert davon ab, wie viel Sie gelöscht werden möchten. Sie können normalerweise mehr Marge als den vorherigen Wert geben, um sicherzustellen, dass die Extrusion des vorherigen Filaments gereinigt wird. | Nummer         | 150          |
| Variable_Filament_laden_Geschwindigkeit    | Die Filamentlastgeschwindigkeit in mm/s normalerweise wird eine schnellere Geschwindigkeit zur Entlassung verwendet.                                                                                                                                                                                                                                                                                                                                         | Nummer         | 10           |

{ % Hint style = "Warnung" %}  
Eine weitere Anpassung, die für Ihren Abschnitt erforderlich ist\[Extruder]das angegeben[**Max_extrudieren_nur_Distanz**](https://www.klipper3d.org/Config_Reference.html#extruder)... Der ratsame Wert beträgt normalerweise> 101 (falls er nicht definiert ist, verwendet 50), um beispielsweise die typischen Extruderkalibrierungstests zuzulassen.   
Sie sollten den Wert basierend auf der oben genannten Test oder der Konfiguration Ihrer anpassen**Variable_Filament_entladen_Länge**ICH**Variable_Filament_laden_Länge**.  
{% von EndHint%}

#### Parken

In bestimmten Prozessen unseres Druckers, wie der Freizeit, ist es ratsam, einen Parkplatz aus dem Kopf zu machen. Die Makros unseres Bundle haben diese Option zusätzlich zu den folgenden Variablen zum Verwalten:

| Variable                              | Beschreibung                                                                                                                                                                                                                                                        | Mögliche Werte | Standardwert |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Start_drucken_Park_In        | Ort, an dem der Kopf während der Vorabstufung parken kann.                                                                                                                                                                                                          | zurück /       |              |
| Zentrum /                             |                                                                                                                                                                                                                                                                     |                |              |
| Front                                 | zurück                                                                                                                                                                                                                                                              |                |              |
| Variable_Start_drucken_Park_Mit_Höhe  | Z Höhe während vorhörig                                                                                                                                                                                                                                             | Nummer         | 50           |
| Variable_Ende_drucken_Park_In         | Standort, um den Kopf am Ende zu parken oder einen Eindruck abzusagen.                                                                                                                                                                                              | zurück /       |              |
| Zentrum /                             |                                                                                                                                                                                                                                                                     |                |              |
| Front                                 | zurück                                                                                                                                                                                                                                                              |                |              |
| Variable_Ende_drucken_Park_Mit_hüpfen | Entfernung, um am Ende des Eindrucks zu gehen.                                                                                                                                                                                                                      | Nummer         | 20           |
| Variable_pause_drucken_Park_In        | Lage, den Kopf mit Pausar zu parken, den Eindruck.                                                                                                                                                                                                                  | zurück /       |              |
| Zentrum /                             |                                                                                                                                                                                                                                                                     |                |              |
| Front                                 | zurück                                                                                                                                                                                                                                                              |                |              |
| Variable_pause_Leerlauf_Time-out      | Wert, in Sekunden, der Aktivierung des Inaktivitätsprozesses in der Maschine, die Motoren freigibt und Koordinaten verlieren,**Ein hoher Wert ist ratsam, das Pause -Makro ausreichend zu aktivieren, um Maßnahmen auszuführen, bevor Koordinaten verloren gehen.** | Nummer         | 43200        |

#### Z-Tilt

Nehmen Sie das Beste aus unserer Maschine, damit sie selbstniveau ist und erleichtert, dass unsere Maschine immer in den besten Bedingungen ist.

**Z-Tilt ist im Grunde ein Prozess, der uns hilft, unsere Z-Motoren in Bezug auf unsere/gantry x (kartesische) oder XY (COREXY) Achse (Corexy) auszurichten**. Damit**Wir versichern, dass wir unser Z immer perfekt und präzise und automatisch haben**.

| Variable                         | Beschreibung                                                                                          | Mögliche Werte | Standardwert |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_kalibrieren_Mit_Neigung | Es ermöglicht, wenn es in unserer Klipper-Konfiguration aktiviert ist, den Z-Tilt-Einstellungsprozess | Wahr / falsch  | FALSCH       |

#### Schief

Die Verwendung von[Schief](broken-reference)Für die Korrektur oder genaue Anpassung unserer Drucker ist es äußerst ratsam, wenn wir Abweichungen in unseren Eindrücken haben. Mithilfe der folgenden Variablen können wir in unseren Makros die Verwendung zulassen:

| Variable               | Beschreibung                                                                                                                                                                                                                                      | Mögliche Werte | Standardwert       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------ |
| Variable_schief_Profil | Ermöglicht Ihnen das Berücksichtigung unseres Verschließungsprofils, das in unserem Makrostart berechnet wird_Drucken. Um es zu aktivieren, müssen wir die Variable diskutieren und den Namen des Schiefeprofils unserer Konfiguration verwenden. | Text           | Mein_schief_Profil |

### Anpassung von Makros

Unser Klipper -Modul verwendet das in Zeiten verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper im Konfigurationsdateiprozess nacheinander. Aus diesem Grund sind die Reihenfolge der Einschlüsse und personalisierten Anpassungen, die wir für diese Module anwenden möchten, unerlässlich.

{ % Hint style = "info" %}  
Bei Verwendung von 3DWork-Einstellungen als Modul können sie nicht direkt aus dem 3DWork-Klipper-Verzeichnis in Ihrem KLIPPER-Konfigurationsverzeichnis bearbeitet werden, da es nur zur Sicherheit in schreibgeschützt ist (nur auf Lesen beschränkt).

Aus diesem Grund ist es sehr wichtig, die Funktion von Klipper zu verstehen und wie Sie unsere Module an Ihre Maschine anpassen können.  
{% von EndHint%}

#### **Variablen personalisieren**

Normalerweise müssen wir uns anpassen, um Anpassungen an den Variablen vorzunehmen, die wir standardmäßig in unserem Modul haben**3dwork**Para schneidet.

Einfach müssen wir den Makroinhalt einfügen\[Gcode_Makro global_WESSEN]Was können wir in Makros/Makros finden_unser_Globals.cfg in unserem Drucker.cfg.

Wir erinnern Sie daran, was zuvor kommentiert wurde, wie Klipper die Konfigurationen nacheinander verarbeitet. Daher ist es ratsam, sie nach dem Includen zu fügen, das wir Ihnen sagen,[Hier](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Wir werden so etwas haben (es ist nur ein visuelles Beispiel):

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

{ % Hint style = "Warnung" %}
Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.
{ % EndHint %}

{ % Hint style = "info" %}

-   Wir empfehlen Ihnen, Kommentare hinzuzufügen, wie Sie im vorherigen Fall sehen, um zu ermitteln, was jeder Abschnitt macht
-   Obwohl Sie nicht alle Variablen berühren müssen, empfehlen wir Ihnen, den gesamten Inhalt von zu kopieren\[Gcode_Makro global_WESSEN]{% von EndHint%}

#### Makros personalisieren

Makros haben modular montiert, damit sie auf einfache Weise angepasst werden können. Wie bereits erwähnt, müssen wir, wenn wir sie anpassen möchten, genau wie bei den Variablen fortfahren, das fragliche Makro in unserem Drucker kopieren.

Wir haben zwei Gruppen von Makros:

-   Makros Um Benutzereinstellungen hinzuzufügen, können diese Makros einfach hinzugefügt und angepasst werden, da sie hinzugefügt wurden, sodass jeder Benutzer die Aktionen in bestimmten Teilen der Prozesse, die jedes Makro durchführt, nach seinen Vorlieben anpassen kann.

**START_DRUCKEN**

| Makroname                                      | Beschreibung                                                                                                      |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| \_BENUTZER_START_DRUCKEN_HITZE_KAMMER          | Es läuft kurz nach dem Erhitzen unseres Gehäuses, wenn Kammer_Frühe Pässe als Parameter für unseren Start_DRUCKEN |
| \_BENUTZER_START_DRUCKEN_VOR_Homing            | Es wird vor dem anfänglichen Homing zum Start des Druckens ausgeführt                                             |
| \_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_BETT     | Es läuft, wenn unser Bett vor seiner Temperatur ankommt_START_DRUCKEN_NACH_HEIZUNG_BETT                           |
| \_BENUTZER_START_DRUCKEN_BETT_Netz             | Wird schon einmal gestartet_START_DRUCKEN_BETT_Netz                                                               |
| \_BENUTZER_START_DRUCKEN_PARK                  | Wird schon einmal gestartet_START_DRUCKEN_PARK                                                                    |
| \_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_Extruder | Wird schon einmal gestartet_START_DRUCKEN_NACH_HEIZUNG_Extruder                                                   |

**ENDE_DRUCKEN**

| Makroname                                  | Beschreibung                                                                              |
| ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| \_BENUTZER_ENDE_DRUCKEN_VOR_Heizungen_AUS  | Es wird vor der Ausführung der Heizung zuvor ausgeführt_ENDE_DRUCKEN_VOR_Heizungen_AUS    |
| \_BENUTZER_ENDE_DRUCKEN_NACH_Heizungen_AUS | Es wird zuvor nach der Abschaltung der Heizung ausgeführt_ENDE_DRUCKEN_NACH_Heizungen_AUS |
| \_BENUTZER_ENDE_DRUCKEN_PARK               | Es wird vor dem Kopf des Kopfes vor dem Kopf ausgeführt_ENDE_DRUCKEN_PARK                 |

**DRUCKEN_Grundlagen**

| Makroname                         | Beschreibung                                    |
| --------------------------------- | ----------------------------------------------- |
| \_BENUTZER_PAUSE_START            | Wird zu Beginn einer Pause ausgeführt           |
| \_BENUTZER_PAUSE_ENDE             | Es läuft am Ende einer Pause                    |
| \_BENUTZER_WIEDER AUFNEHMEN_START | Wird zu Beginn einer Zusammenfassung ausgeführt |
| \_BENUTZER_WIEDER AUFNEHMEN_ENDE  | Läuft am Ende einer Zusammenfassung             |

-   Interne Makros sind Makros, um das Hauptmakro in Prozesse zu unterteilen, und ist dafür wichtig. Es ist ratsam, dass diese bei Bedürfnissen, diese wie sie sind, kopiert werden.

**START_DRUCKEN**

| Makroname                             | Beschreibung                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_START_DRUCKEN_HITZE_KAMMER          | Erhitzt das Gehäuse, falls der Kammerparameter_Früh erfolgt unser Makro -Start_Drucken aus dem Laminator                                                                                                                        |
| \_START_DRUCKEN_NACH_HEIZUNG_BETT     | Es läuft, wenn das Bett danach bei Temperatur ankommt_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_Bett. Normalerweise wird es für die Verarbeitung der Bettkalibrierung verwendet (z_NEIGUNG_Einstellen, Quad_PORTAL_Nivellierung, ...) |
| \_START_DRUCKEN_BETT_Netz             | Er ist verantwortlich für die Logik des Bettes Elend.                                                                                                                                                                           |
| \_START_DRUCKEN_PARK                  | Berufet den Druckkopf beim Erhitzen der Düse bei der Drucktemperatur.                                                                                                                                                           |
| \_START_DRUCKEN_NACH_HEIZUNG_Extruder | Machen Sie die Nazzle -Säuber                                                                                                                                                                                                   |

## Drucker und elektronisch

Da wir mit verschiedenen Modellen von Druckern und Elektronik arbeiten, werden wir diejenigen hinzufügen, die nicht direkt von Zeiten unterstützt werden, unabhängig davon, ob es sich um Beiträge oder die Gemeinschaft handelt.

-   Drucker, in diesem Verzeichnis haben wir alle Konfigurationen des Druckers
-   Boards, hier finden wir Elektronik

### Parameter und Stifte

Unser Klipper -Modul verwendet das in Zeiten verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper im Konfigurationsdateiprozess nacheinander. Aus diesem Grund sind die Reihenfolge der Einschlüsse und personalisierten Anpassungen, die wir für diese Module anwenden möchten, unerlässlich.

{ % Hint style = "info" %}
Bei Verwendung von 3DWork-Einstellungen als Modul können sie nicht direkt aus dem 3DWork-Klipper-Verzeichnis in Ihrem KLIPPER-Konfigurationsverzeichnis bearbeitet werden, da es nur zur Sicherheit in schreibgeschützt ist (nur auf Lesen beschränkt).

Aus diesem Grund ist es sehr wichtig, die Funktion von Klipper zu verstehen und wie Sie unsere Module an Ihre Maschine anpassen können.
{ % EndHint %}

Wie wir in "erklärten"[Makros personalisieren](3dwork-klipper-bundle.md#personalizando-macros)"Wir werden denselben Prozess verwenden, um Parameter oder Stifte anzupassen, um sie an unsere Anforderungen anzupassen.

#### Personalisierungsparameter

Wenn wir Ihnen empfehlen, einen Abschnitt in Ihrem Drucker zu erstellen.CFG, der als Benutzerüberschreibungen bezeichnet wird und nach dem Include in unsere Konfigurationen platziert wird, um in der Lage zu sein, alle darin verwendeten Parameter anzupassen und anzupassen.

Im folgenden Beispiel werden wir sehen, wie wir in unserem Fall die Parameter unserer Bettniveau (Bett) anpassen möchten_Mesh) Anpassung der Vermessungspunkte (Sonde_Anzahl) in Bezug auf die Konfiguration, die wir standardmäßig in den Konfigurationen unseres Klipper -Moduls haben:

{ % code title = "drucker.cfg" %}

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

{ % Endcode %}

{ % Hint style = "Warnung" %}
Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.
{ % EndHint %}

Wir können diesen Vorgang mit jedem Parameter verwenden, den wir anpassen möchten.

#### Anpassen der Kiefernkonfiguration

Wir werden genau so vorgehen, wie wir es zuvor getan haben. In unserem Benutzerüberschreibungsbereich werden wir diese Abschnitte von Stiften hinzufügen, die wir uns an unseren Geschmack anpassen möchten.

Im folgenden Beispiel werden wir anpassen, was der Stift unseres Elektroniklüfers ist (Controller_Fan) zu einer anderen von der Standardeinstellung zuweisen:

{ % code title = "drucker.cfg" %}

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

{ % Endcode %}

{ % Hint style = "Warnung" %}
Die drei Punkte (...) der vorherigen Beispiele deuten lediglich darauf hin, dass Sie mehr Konfigurationen zwischen Abschnitten haben können ... in keinem Fall, falls sie tragen sollten.
{ % EndHint %}

```

```
