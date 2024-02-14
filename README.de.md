* * *

## Beschreibung: Paket mit Makros, Einstellungen und anderen Dienstprogrammen für Klipper

# 3Dwork Clipper-Paket

[![](../../.gitbook/assets/image%20(1986).png)- Englisch](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{% hint style="danger" %}  
**LEITFADEN IN BEARBEITUNG!!! Obwohl die Makros voll funktionsfähig sind, werden sie kontinuierlich weiterentwickelt.**

**Die Nutzung erfolgt auf eigene Gefahr!!!**  
{% endint %}

Änderungsprotokoll

07.12.2023 – Unterstützung hinzugefügt, um die Erstellung der elektronischen Firmware von Bigtreetech zu automatisieren

Aus**Deine Ausreden**Wir haben eine Reihe von Makros, Maschinen- und Elektronikeinstellungen sowie anderen Tools für eine einfache und leistungsstarke Klipper-Verwaltung zusammengestellt und verfeinert.

Ein Großteil dieses Pakets basiert auf[**Ratten**](https://os.ratrig.com/)Verbesserung der Teile, die wir für interessant halten, sowie anderer Beiträge aus der Community.

## Installation

Um unser Paket für Klipper zu installieren, führen wir die folgenden Schritte aus

### Aus dem Repository herunterladen

Wir verbinden uns über SSH mit unserem Host und geben die folgenden Befehle aus:

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{% hint style="warning" %}  
Wenn Ihr Klipper-Konfigurationsverzeichnis angepasst ist, denken Sie daran, den ersten Befehl entsprechend Ihrer Installation anzupassen.  
{% endint %}

{% hint style="info" %}  
Bei Neuinstallationen:

Da Klipper keinen Zugriff auf Makros zulässt, bis es über eine korrekte Printer.cfg verfügt und eine Verbindung zu einer MCU herstellt, können wir Klipper mit den folgenden Schritten „austricksen“, die es uns ermöglichen, die Makros in unserem Bundle zu verwenden, um beispielsweise die zu starten Klipper-Firmware-Kompilierungsmakro, wenn wir kompatible Elektronik verwenden:

-   Wir stellen sicher, dass wir unsere haben[Host als zweite MCU](raspberry-como-segunda-mcu.md)
-   Als nächstes fügen wir eine Printer.cfg hinzu. Denken Sie daran, dass diese Schritte für eine Neuinstallation gelten, bei der Sie keine Printer.cfg haben und das Makro zum Erstellen von Firmware starten möchten, wie das, das Sie unten sehen können:


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

Damit können wir Klipper starten, um Zugriff auf unsere Makros zu erhalten.  
{% endint %}

### Mit Moonraker immer auf dem neuesten Stand bleiben

Dank Moonraker können wir das Update nutzen_Manager, um über die Verbesserungen, die wir möglicherweise in der Zukunft einführen, auf dem Laufenden zu bleiben.

Von Mainsail/Fluidd aus bearbeiten wir unsere Moonraker.conf (sie sollte auf der gleichen Höhe wie Ihre Printer.cfg sein) und fügen am Ende der Konfigurationsdatei Folgendes hinzu:

    [include 3dwork-klipper/moonraker.conf]

{% hint style="warning" %}  
**Denken Sie daran, den Installationsschritt vorher durchzuführen, da Moonraker sonst einen Fehler generiert und nicht gestartet werden kann.**

**Wenn andererseits das Verzeichnis Ihrer Klipper-Konfiguration angepasst ist, denken Sie daran, den Pfad entsprechend Ihrer Installation anzupassen.**  
{% endint %}

## Makros

Wir haben immer darauf hingewiesen, dass RatOS eine der besten Klipper-Distributionen ist und Raspberry- und CB1-Module unterstützt, vor allem aufgrund seiner modularen Konfiguration und seiner großartigen Makros.

Einige hinzugefügte Makros, die für uns nützlich sein werden:

### **Allzweckmakros**

| Makro                                                                         | Beschreibung                                                                                                                                                                                               |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VIELLEICHT_HEIM**                                                           | Dadurch können wir den Referenzierungsprozess nur optimieren, indem wir ihn auf den Achsen durchführen, die nicht referenziert werden.                                                                     |
| **PAUSE**                                                                     | Durch die zugehörigen Variablen können wir eine Pause mit einem vielseitigeren Kopfparkmodus verwalten als mit normalen Makros.                                                                            |
| **SATZ_PAUSE_BEI_SCHICHT**                                                    |                                                                                                                                                                                                            |
| **SATZ_PAUSE_BEI_NÄCHSTE_SCHICHT**                                            | Ein sehr nützliches Makro, das Mainsail in seine Benutzeroberfläche integriert, um bei Bedarf in einer bestimmten Ebene pausieren zu können ... für den Fall, dass wir es beim Laminieren vergessen haben. |
| Wir haben auch eine weitere, um die Pause auf der nächsten Ebene auszuführen. |                                                                                                                                                                                                            |
| **WIEDER AUFNEHMEN**                                                          | Verbessert, da wir damit erkennen können, ob unsere Düse nicht die Extrusionstemperatur hat, um das Problem zu beheben, bevor ein Fehler auftritt und unser Drucksystem beschädigt wird.                   |
| **STORNIEREN_DRUCKEN**                                                        | Dies ermöglicht die Verwendung der restlichen Makros, um einen Druckabbruch korrekt durchzuführen.                                                                                                         |

-   **Bei Ebenenwechsel angehalten**, einige sehr interessante Makros, die es uns ermöglichen, eine Ebene anzuhalten oder einen Befehl zu starten, wenn wir die nächste Ebene starten.  
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    Ein weiterer Vorteil besteht darin, dass sie in Mainsail integriert sind, sodass wir neue Funktionen in unserer Benutzeroberfläche haben werden, wie Sie unten sehen können:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Makros zur Druckverwaltung**

| Makro                                                                                     | Beschreibung                                                                                                                                     |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **START_DRUCKEN**                                                                         | Dadurch können wir unsere Ausdrucke sicher und im Klipper-Stil starten. Darin finden wir einige interessante Funktionen wie:                     |
| -Intelligente Düsenvorwärmung bei Verwendung eines Sondensensors                          |                                                                                                                                                  |
| -Möglichkeit der Verwendung der Z-Neigung durch Variable                                  |                                                                                                                                                  |
| -adaptives Bettnetz, erzwungen oder aus einem gespeicherten Netz                          |                                                                                                                                                  |
| -anpassbare Spülleitung zwischen normaler, adaptiver Spülleitung oder Spülabfall          |                                                                                                                                                  |
| -segmentiertes Makro, um es personalisieren zu können, wie wir Ihnen später zeigen werden |                                                                                                                                                  |
| **ENDE_DRUCKEN**                                                                          | End-of-Print-Makro, bei dem wir auch eine Segmentierung haben, um unser Makro anpassen zu können. Wir verfügen auch über dynamisches Kopfparken. |

-   **Adaptives Bettnetz**Dank der Vielseitigkeit von Klipper können wir Dinge tun, die heute unmöglich erscheinen ... Ein wichtiger Prozess beim Drucken besteht darin, ein Netz von Abweichungen von unserem Bett zu erstellen, das es uns ermöglicht, diese zu korrigieren, um eine perfekte Haftung der ersten Schichten zu erreichen.  
    In vielen Fällen führen wir diese Vernetzung vor dem Drucken durch, um sicherzustellen, dass sie ordnungsgemäß funktioniert, und zwar auf der gesamten Oberfläche unseres Bettes.  
    Bei der adaptiven Bettvernetzung erfolgt dies im Druckbereich und ist damit viel präziser als die herkömmliche Methode. In den folgenden Screenshots sehen wir die Unterschiede zwischen einem herkömmlichen und einem adaptiven Netz.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Makros zur Filamentverwaltung**

Eine Reihe von Makros, die es uns ermöglichen, verschiedene Aktionen mit unserem Filament zu verwalten, wie zum Beispiel das Laden oder Entladen.

| Makro                  | Beschreibung                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **M600**               | Dies ermöglicht uns die Kompatibilität mit dem M600-Gcode, der normalerweise in Laminatoren für den Filamentwechsel verwendet wird. |
| **ENTLADEN_FILAMENT**  | Über die Variablen konfigurierbar, ermöglicht es uns eine unterstützte Filamententladung.                                           |
| **BELASTUNG_FILAMENT** | Wie das vorherige, jedoch bezogen auf die Filamentlast.                                                                             |

### **Makros zur Filamentspulenverwaltung (Spoolman)**

{% hint style="warning" %}  
**ABSCHNITT IN BEARBEITUNG!!!**  
{% endint %}

[**Spoolman**](https://github.com/Donkie/Spoolman)ist ein in Moonraker integrierter Filamentspulenmanager, mit dem wir unseren Filamentbestand und die Verfügbarkeit verwalten können.

!\[](../../.gitbook/assets/image (1990).png)

Wir werden nicht auf die Installation und Konfiguration eingehen, da die Verwendung relativ einfach ist[**Anweisungen von Ihrem Github**](https://github.com/Donkie/Spoolman)**,**in jedem Fall**Wir empfehlen Ihnen, Docker zu verwenden**der Einfachheit halber und zur Erinnerung**Aktivieren Sie die Einstellungen in Moonraker**erforderlich:

{% code title="moonraker.conf" %}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{%endcode%}

| Makro            | Beschreibung                                              |
| ---------------- | --------------------------------------------------------- |
| SATZ_AKTIV_SPULE | Damit können wir die ID der zu verwendenden Spule angeben |
| KLAR_AKTIV_SPULE | Dadurch können wir die aktive Spule zurücksetzen          |

Ideal wäre in jedem Fall die Ergänzung unseres Laminators,**in den Filament-Gcodes für jede Spule der Aufruf dazu**, und merke dir**Ändern Sie seine ID, sobald es verbraucht ist**um den Überblick darüber behalten zu können, was an Filament darin übrig bleibt!!!

!\[](../../.gitbook/assets/image (1991).png)

### **Makros zur Druckoberflächenverwaltung**

{% hint style="warning" %}  
**ABSCHNITT IN BEARBEITUNG!!!**  
{% endint %}

Normalerweise ist es normal, dass wir je nach gewünschter Oberfläche oder Filamentart unterschiedliche Druckoberflächen haben.

Dieser Satz von Makros, erstellt von[Garethky](https://github.com/garethky)Sie ermöglichen uns die Kontrolle über diese und insbesondere über die korrekte Einstellung von ZOffset in jedem von ihnen in der Art, wie wir es bei Prusa-Maschinen haben. Unten sehen Sie einige seiner Funktionen:

-   Wir können die gewünschte Anzahl von Druckoberflächen speichern, wobei jede einen eindeutigen Namen hat
-   Jede Druckoberfläche verfügt über einen eigenen ZOffset
-   Wenn wir während eines Drucks (Babystepping) von unserem Klipper aus Z-Anpassungen vornehmen, wird diese Änderung in der zu diesem Zeitpunkt aktivierten Oberfläche gespeichert

Andererseits haben wir welche**Anforderungen, um es zu implementieren (wir werden versuchen, die PRINT-Logik hinzuzufügen).\_START des Bundles in der Zukunft durch Aktivierung dieser Funktion per Variable und Erstellung eines vorherigen und nachfolgenden Benutzermakros, um Benutzerereignisse eingeben zu können)**:

-   die Verwendung von\[speichern_Variablen]In unserem Fall verwenden wir ~/variables.cfg, um die Variablen zu speichern, und das ist bereits in der CFG dieser Makros enthalten.  
    Dadurch wird automatisch eine Variablendatei für uns erstellt_bauen_sheet.cfg, wo unsere Variablen auf der Festplatte gespeichert werden.

{% code title="Beispiel einer Variablenkonfigurationsdatei" %}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{%endcode%}

-   Wir müssen einen Aufruf zur Bewerbung einschließen_BAUEN_BLATT_ANPASSUNG in unserem DRUCK_START, um den ZOffset der ausgewählten Oberfläche anwenden zu können
-   Es ist wichtig, dass für das vorherige Makro APPLY gilt_BAUEN_BLATT_ANPASSUNG, um richtig zu funktionieren, müssen wir ein SET hinzufügen_GCODE_OFFSET Z=0,0 kurz vor dem Aufruf von APPLY_BAUEN_BLATT_EINSTELLUNG


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

Andererseits ist es interessant, über Makros verfügen zu können, um die eine oder andere Oberfläche zu aktivieren oder sie sogar als Parameter von unserem Laminator zu übergeben, sodass wir bei unterschiedlichen Drucker- oder Filamentprofilen die eine oder andere automatisch laden können:

{% hint style="warning" %}  
Es ist wichtig, dass der Wert in NAME="xxxx" mit dem Namen übereinstimmt, den wir bei der Installation unserer Druckoberfläche angegeben haben  
{% endint %}

{% code title="printer.cfg or include cfg" %}

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

{%endcode%}

Auch wenn wir über KlipperScreen verfügen, können wir ein spezielles Menü hinzufügen, um das Laden der verschiedenen Oberflächen zu verwalten, in das wir einen Aufruf der zuvor für das Laden jeder Oberfläche erstellten Makros einfügen:

{% code title="~/printer_data/config/KlipperScreen.conf" %}

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

{%endcode%}

| Makro                            | Beschreibung |
| -------------------------------- | ------------ |
| INSTALLIEREN_BAUEN_BLATT         |              |
| ZEIGEN_BAUEN_BLATT               |              |
| ZEIGEN_BAUEN_BLÄTTER             |              |
| SATZ_BAUEN_BLATT_OFFSET          |              |
| ZURÜCKSETZEN_BAUEN_BLATT_OFFSET  |              |
| SATZ_GCODE_OFFSET                |              |
| ANWENDEN_BAUEN_BLATT_EINSTELLUNG |              |

### **Maschinenkonfigurationsmakros**

| Makro                                                         | Beschreibung                                                                                                                                                                                                                                  |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KOMPILIEREN_FIRMWARE**                                      | Mit diesem Makro können wir die Klipper-Firmware auf einfache Weise kompilieren, zur Vereinfachung über die Benutzeroberfläche auf die Firmware zugreifen und sie auf unsere Elektronik anwenden.                                             |
| Hier finden Sie weitere Details zur unterstützten Elektronik. |                                                                                                                                                                                                                                               |
| **BERECHNUNG_BETT_GITTERGEWEBE**                              | Ein äußerst nützliches Makro zur Berechnung der Fläche für unser Netz, da dies manchmal ein komplizierter Prozess sein kann.                                                                                                                  |
| **PID_ALLE**                                                  |                                                                                                                                                                                                                                               |
| **PID_EXTRUDER**                                              |                                                                                                                                                                                                                                               |
| **PID_BETT**                                                  | Mithilfe dieser Makros, mit denen wir die Temperaturen in Form von Parametern an den PID übergeben können, können wir die Temperaturkalibrierung auf äußerst einfache Weise durchführen.                                                      |
| **PRÜFEN_GESCHWINDIGKEIT**                                    |                                                                                                                                                                                                                                               |
| **PRÜFEN_GESCHWINDIGKEIT_DELTA**                              | Das Originalmakro des Companion[Ellis](https://github.com/AndrewEllis93)Sie werden es uns auf relativ einfache Weise ermöglichen, die Geschwindigkeit zu testen, mit der wir unsere Maschine präzise und ohne Schrittverluste bewegen können. |

-   **Kompilierte Firmware für unterstützte Elektronik**Um den Prozess der Erstellung und Wartung unserer Klipper-Firmware für unsere MCUs zu erleichtern, haben wir das Makro COMPILE_Die FIRMWARE, bei deren Ausführung wir unsere Elektronik als Parameter verwenden können, um nur dies zu tun, kompiliert Klipper für die gesamte von unserem Bundle unterstützte Elektronik:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Wir finden diese leicht zugänglich über unsere Web-Benutzeroberfläche im Firmware-Verzeichnis_Binärdateien in unserem MASCHINEN-Tab (wenn wir Großsegel verwenden):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Nachfolgend finden Sie die Liste der unterstützten Elektronikgeräte:

**WICHTIG!!!**

Diese Skripte sind für die Arbeit auf einem Raspbian-System mit Pi-Benutzer vorbereitet. Wenn dies nicht der Fall ist, müssen Sie sie anpassen.

Die Firmwares werden für die Verwendung mit einer USB-Verbindung generiert, was wir immer empfehlen. Darüber hinaus ist der USB-Montagepunkt immer derselbe, sodass sich Ihre MCU-Verbindungskonfiguration nicht ändert, wenn sie mit unserem Makro/Skript generiert werden.

**Damit Klipper Shell-Makros ausführen kann, muss dank des Companion eine Erweiterung installiert werden**[**Arkussinus**](https://github.com/Arksine)**, das erlaubt es.**

**Abhängig von der verwendeten Klipper-Distribution sind sie möglicherweise bereits aktiviert.**

![](../../.gitbook/assets/image%20(770).png)

Der einfachste Weg ist die Verwendung[**keoh**](../instalacion/#instalando-kiauh)wo wir in einer seiner Optionen die Möglichkeit finden, diese Erweiterung zu installieren:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Wir können den Vorgang auch manuell durchführen, wir kopieren das Plugin manuell für Klipper[**gcode_Hülse_Verlängerung**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)in unserem Verzeichnis`_**~/klipper/klippy/extras**_`Verwenden Sie SSH oder SCP und starten Sie Klipper neu.

| Elektronik         | Parametername, der im Makro verwendet werden soll |
| ------------------ | ------------------------------------------------- |
| Manta E            | Mit Stolz                                         |
| Vergessen Sie M4P  | btt-manta-m4p                                     |
| Manta M4P v2.a     | btt-manta-m4p-22                                  |
| Manta Qab          | btt-manta-m8p                                     |
| Manda MthP b1.1    | btt-manta-m8p-11                                  |
| KEIN Oktopus Max   | btt-octopus-max-it                                |
| Octopus Pro (446)  | btt-octopus-pro-446                               |
| Octopus Pro (429)  | btt-octopus-pro-429                               |
| Octopus Pro (H723) | btt-octopus-pro-h723                              |
| Octopus v1.1       | BTT-Oktopus-11                                    |
| Octopus v1.1 (407) | btt-octopus-11-407                                |
| SKR Pro v1.2       | skr_Profi_12                                      |
| SKR 3              | Übrigens_skr_3                                    |
| Saqr A (Haha)      | Du machst ihn betrunken                           |
| SKR 3 EZ           | btt-skr-3-ez                                      |
| Saqr A Idha (Haha) | Sie wird sehr betrunken                           |
| SKR 2 (429)        | btt-skr-2-429                                     |
| SKR 2 (407)        | btt-skr-2-407                                     |
| SKR RAT            | BTT-Kurzschluss-10                                |
| SKR 1.4 Turbo      | btt-skr-14-turbo                                  |
| SKR Mini Ez vz     | Übrigens_skr_Mini_ez_30                           |

| Werkzeugkopf (CAN) | Parametername, der im Makro verwendet werden soll |
| ------------------ | ------------------------------------------------- |
| EBB42 v1           | Übrigens_ebb42_10                                 |
| EBB36 v1           | Übrigens_Ebbe36_10                                |
| EBB42 v1.1         | Übrigens_ebb42_11                                 |
| EBB36 v1.1         | Übrigens_Ebbe36_11                                |
| EBB42 v1.2         | Übrigens_ebb42_12                                 |
| EBB36 v1.2         | Übrigens_Ebbe36_12                                |

| **Elektronik**            | **Parametername, der im Makro verwendet werden soll** |
| ------------------------- | ----------------------------------------------------- |
| MKS Eagle v1.x            | mks-eagle-10                                          |
| ISS Robin Nano vz         | mks-robin-nano-30                                     |
| MKS Robin Nano v2         | mks-robin-nano-20                                     |
| MKS Gen L                 | mks-gen-l                                             |
| Rubins Sünden-Nano-Klasse | zeg_Robin_Nano_dw_Klasse                              |

| Werkzeugkopf (CAN) | Parametername, der im Makro verwendet werden soll |
| ------------------ | ------------------------------------------------- |
| Mellow FLY SHT 42  | weich_Fliege_Scheiße_42                           |
| Mellow FLY SHT 36  | weich_Fliege_Scheiße_36                           |

| Elektronik    | Parametername, der im Makro verwendet werden soll |
| ------------- | ------------------------------------------------- |
| Fysetc-Spinne | fysetc_Spinne                                     |

### Hinzufügen von 3Dwork-Makros zu unserer Installation

Über unsere Schnittstelle „Mainsail/Fluidd“ bearbeiten wir unsere Datei „printer.cfg“ und fügen Folgendes hinzu:

{% code title="printer.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{%endcode%}

{% hint style="info" %}  
Es ist wichtig, dass wir diese Zeilen am Ende unserer Konfigurationsdatei hinzufügen ... direkt über dem Abschnitt, damit Makros in unserer CFG oder in unseren Includes von unseren überschrieben werden:  
#\*# \\&lt;-------- SPEICHERN_KONFIG -------->  
{% endint %}

{% hint style="warning" %}  
Normale Makros wurden abgetrennt**Makros-Shell**angesichts dessen**Um diese zu aktivieren, müssen zusätzlich zu der Tatsache, dass sie derzeit getestet werden, weitere Schritte manuell durchgeführt werden.**Und\*\*Sie benötigen möglicherweise zusätzliche Berechtigungen, um Ausführungsberechtigungen zuzuweisen, für die keine Anweisungen angegeben wurden, da sie eine Automatisierung anstreben.\*\*  
**Die Nutzung geschieht auf eigenes Risiko.**  
{% endint %}

### Konfiguration unseres Laminators

Da unsere Makros dynamisch sind, extrahieren sie bestimmte Informationen aus unserer Druckerkonfiguration und dem Laminator selbst. Hierzu empfehlen wir Ihnen, Ihre Laminatoren wie folgt zu konfigurieren:

-   **Starten Sie den Gcode START_DRUCKEN**, unter Verwendung von Platzhaltern, um Filament- und Betttemperaturwerte dynamisch zu übergeben:

{% tabs %}  
{% tab title="PrusaSlicer-SuperSlicer" %}  
**Prusa-Schneider**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**SuperSlicer**- Wir haben die Möglichkeit, die Gehäusetemperatur (KAMMER) anzupassen

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{% Endverlust %}

{% tab title="Bambu Studio/OrcaSlicer" %}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760).png){% endtab %}

{% tab title="Cura" %}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{% hint style="warning" %}  
Wir müssen das Plugin installieren[**Post Process Plugin (von frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)aus dem Menü_**Hilfe/Anzeigen**_Konfigurationsordner... wir kopieren das Skript vom vorherigen Link in den Skriptordner.  
Wir starten Cura neu und gehen zu_**Erweiterungen/Nachbearbeitung/G-Code ändern**_und wir werden auswählen_**Mesh-Druckgröße**_.  
{% endint %}  
{% Endverlust %}

{% tab title="IdeaMaker" %}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{% Endverlust %}

{% tab title="Simplify3D" %}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{% Endverlust %}  
{% Endverlust %}

{% hint style="info" %}  
Der**Platzhalter sind „Aliase“ oder Variablen, die die Laminatoren verwenden, damit sie bei der Generierung des GCodes durch die im Profil konfigurierten Werte ersetzt werden**des Eindrucks.

Unter den folgenden Links finden Sie eine Liste davon für:[**Prusa-Schneider**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(zusätzlich zu den oben genannten),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)Und[**Behandlung**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

Durch deren Verwendung können unsere Makros dynamisch sein.  
{% endint %}

-   **gcode das endgültige ENDE_DRUCKEN**, in diesem Fall ist es für alle Laminatoren gleich, da keine Platzhalter verwendet werden


    END_PRINT

### Variablen

Wie bereits erwähnt, ermöglichen uns diese neuen Makros einige sehr nützliche Funktionen, die wir oben aufgeführt haben.

Um diese an unsere Maschine anzupassen, verwenden wir die Variablen, die wir in Makros/Makros finden_War_globals.cfg, auf die wir weiter unten näher eingehen.

#### Nachrichten-/Benachrichtigungssprache

Da viele Benutzer gerne Makrobenachrichtigungen in ihrer Sprache haben, haben wir ein mehrsprachiges Benachrichtigungssystem entwickelt, derzeit Spanisch (es) und Englisch (en). In der folgenden Variablen können wir es anpassen:

| Variable         | Beschreibung                                                                                                                           | Mögliche Werte | Standardwert |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Sprache | Es ermöglicht uns, die Sprache der Benachrichtigungen auszuwählen. Wenn es nicht genau definiert ist, wird es in (Englisch) verwendet. | ist in         | es           |

#### Relative Extrusion

Damit können wir steuern, welchen Extrusionsmodus wir am Ende unseres START verwenden.\_DRUCKEN Der Wert hängt von der Konfiguration unseres Laminators ab.

{% hint style="success" %}  
Es empfiehlt sich, Ihren Laminator für die Verwendung der relativen Extrusion zu konfigurieren und diese Variable auf „True“ zu setzen.  
{% endint %}

| Variable                   | Beschreibung                                                                   | Mögliche Werte | Standardwert |
| -------------------------- | ------------------------------------------------------------------------------ | -------------- | ------------ |
| Variable_relativ_Extrusion | Damit können wir den in unserem Laminator verwendeten Extrusionsmodus angeben. | Wahr falsch    | WAHR         |

#### Geschwindigkeiten

Zum Verwalten der in Makros verwendeten Geschwindigkeiten.

| Variable                              | Beschreibung                            | Mögliche Werte | Standardwert |   |
| ------------------------------------- | --------------------------------------- | -------------- | ------------ | - |
| Variable_Makro_reisen_Geschwindigkeit | Übertragungsgeschwindigkeit             | numerisch      | 150          |   |
| Variable_Makro_Mit_Geschwindigkeit    | Übertragungsgeschwindigkeit für Z-Achse | numerisch      | 15           |   |

#### Heimkehr

Satz von Variablen im Zusammenhang mit dem Referenzierungsprozess.

| Variable | Beschreibung | Mögliche Werte | Standardwert |
| -------- | ------------ | -------------- | ------------ |

#### Heizung

Variablen im Zusammenhang mit dem Heizprozess unserer Maschine.

| Variable                                      | Beschreibung                                                                                            | Mögliche Werte | Standardwert |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Vorwärmen_Extruder                   | Ermöglicht das Vorheizen der Düse auf die in der Variable angegebene Temperatur_Vorwärmen_Extruder_Temp | Wahr falsch    | WAHR         |
| Variable_Vorwärmen_Extruder_Temp              | Temperatur der Düsenvorwärmung                                                                          | numerisch      | 150          |
| Variable_Start_drucken_Hitze_Kammer_Bett_Temp | Betttemperatur während des Aufheizvorgangs unseres Gehäuses                                             | numerisch      | 100          |

{% hint style="success" %}  
Vorteile der Verwendung einer vorgeheizten Düse:

-   Es gibt uns zusätzliche Zeit, damit das Bett seine Temperatur gleichmäßig erreichen kann.
-   Wenn wir einen induktiven Sensor ohne Temperaturkompensation verwenden, können unsere Messungen konsistenter und präziser sein.
-   Es ermöglicht Ihnen, eventuell in der Düse verbleibendes Filament aufzuweichen, was bedeutet, dass diese Reste in bestimmten Konfigurationen keinen Einfluss auf die Aktivierung des Sensors haben.  
    {% endint %}

#### Bettgitter

Um den Nivellierungsprozess zu steuern, verfügen wir über Variablen, die sehr nützlich sein können. Beispielsweise können wir die Art der Nivellierung steuern, die wir verwenden möchten, indem wir immer ein neues Netz erstellen, ein zuvor gespeichertes laden oder adaptive Vernetzung verwenden.

| Variable                                                                                                                        | Beschreibung                                                                                    | Mögliche Werte | Standardwert |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_kalibrieren_Bett_Gittergewebe                                                                                          | Damit können wir auswählen, welche Art von Netz wir in unserem START verwenden möchten_DRUCKEN: |                |              |
| -Neues Netz, es wird jeden Druck vernetzen                                                                                      |                                                                                                 |                |              |
| -Storedmesh lädt ein gespeichertes Mesh und führt keine Bettabfrage durch                                                       |                                                                                                 |                |              |
| -Adaptiv macht uns zu einem neuen Netz, das jedoch an den Druckbereich angepasst ist und oft unsere ersten Schichten verbessert |                                                                                                 |                |              |
| -Nomesh, falls wir keinen Sensor haben oder Mesh verwenden, um den Vorgang zu überspringen                                      | Nevmesh / Storedmesh / Adaptiv /                                                                |                |              |
| Namen                                                                                                                           | adaptiv                                                                                         |                |              |
| Variable_Bett_Gittergewebe_Profil                                                                                               | Der Name, der für unser gespeichertes Mesh verwendet wird                                       | Text           | Standard     |

{% hint style="warning" %}  
Wir empfehlen Ihnen, die adaptive Nivellierung zu verwenden, da dadurch das Netz immer an die Größe unseres Drucks angepasst wird, sodass Sie über einen angepassten Netzbereich verfügen.

Es ist wichtig, dass wir in unserem[Start-Gcode unseres Laminators](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), im Aufruf zu unserem START_PRINT, PRINT-Werte_MAX y DRUCKEN_MINDEST.  
{% endint %}

#### gesäubert

Eine wichtige Phase unseres Druckstarts ist das korrekte Spülen unserer Düse, um zu verhindern, dass Filamentreste zurückbleiben oder dass diese unseren Druck irgendwann beschädigen könnten. Nachfolgend finden Sie die Variablen, die in diesen Prozess eingreifen:

| Variable                                                                                                                                                               | Beschreibung                                           | Mögliche Werte | Standardwert |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------- | ------------ |
| Variable_Düse_Grundierung                                                                                                                                              | Wir können zwischen verschiedenen Spüloptionen wählen: |                |              |
| -primeline wird die typische Löschlinie zeichnen                                                                                                                       |                                                        |                |              |
| -primelineadaptative generiert mithilfe einer Variablen eine Spüllinie, die sich an die Fläche des gedruckten Teils anpasst_Düse_Grundierung_Objektentfernung als Rand |                                                        |                |              |
| -Mit primeblob werfen wir einen Tropfen Filament in eine Ecke unseres Bettes, der sich sehr effektiv zum Reinigen der Düse eignet und leicht zu entfernen ist          |                                                        |                |              |
| Hauptlinie /                                                                                                                                                           |                                                        |                |              |

primelineadaptiv /  
primeblob /   
FALSCH

| adaptive Primeline |  
| Variable_Düse_Grundierung_Objektentfernung | Wenn wir eine adaptive Beschnittlinie verwenden, ist dies der Rand, der zwischen der Beschnittlinie und dem gedruckten Objekt | verwendet werden soll numerisch | 5 |  
| Variable_Düse_Primzahl_Start_x | Wo wir unsere Spülleitung platzieren möchten:  
-min wird es bei X=0 tun (plus einer kleinen Sicherheitsmarge)  
-max wird dies bei X=max tun (abzüglich einer kleinen Sicherheitsmarge)  
-Die Zahl ist die X-Koordinate, an der sich die Spülung | befindet Mindest /  
max. /  
Zahl | max |  
| Variable_Düse_Primzahl_Start_und | Wo wir unsere Spülleitung platzieren möchten:  
-min wird dies bei Y=0 tun (plus einer kleinen Sicherheitsmarge)  
-max wird dies bei Y=max tun (abzüglich einer kleinen Sicherheitsmarge)  
-Die Zahl ist die Y-Koordinate, an der die Spülung | lokalisiert werden soll Mindest /  
max. /  
Zahl | min |  
| Variable_Düse_Primzahl_Richtung | Die Adresse unserer Leitung oder Zustellung:  
-Nach hinten bewegt sich der Kopf zur Vorderseite des Druckers  
-vorwärts bewegt sich nach hinten  
-Das Auto fährt je nach Variable in Richtung Mitte_Düse_Primzahl_Start_und | Auto /  
vorwärts /  
rückwärts | auto |

#### Laden/Entladen des Filaments

In diesem Fall erleichtert uns diese Gruppe von Variablen die Verwaltung des Ladens und Entladens unseres Filaments, das beispielsweise in der M600-Emulation verwendet wird, oder beim Starten der Makros zum Laden und Entladen von Filamenten:

| Variable                                    | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Mögliche Werte | Standardwert |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Filament_entladen_Länge            | Wie viel mm das Filament zurückgezogen werden muss, passen Sie an Ihre Maschine an, normalerweise das Maß von Ihrer Düse bis zu den Zahnrädern Ihres Extruders, wobei ein zusätzlicher Spielraum hinzukommt.                                                                                                                                                                                                                                                        | Nummer         | 130          |
| Variable_Filament_entladen_Geschwindigkeit  | Filamentrückzugsgeschwindigkeit in mm/s. Normalerweise wird eine langsame Geschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                                                                | Nummer         | 5            |
| Variable_Filament_Belastung_Länge           | Abstand in mm zum Laden des neuen Filaments... sowie variabel_Filament_entladen_Für die Länge verwenden wir die Messung von Ihrem Getriebe bis zum Extruder und fügen einen zusätzlichen Spielraum hinzu. In diesem Fall hängt dieser zusätzliche Wert davon ab, wie viel gespült werden soll. Normalerweise können Sie ihm einen größeren Spielraum als den vorherigen Wert geben, um sicherzustellen, dass der Die Extrusion des vorherigen Filaments ist sauber. | Nummer         | 150          |
| Variable_Filament_Belastung_Geschwindigkeit | Filamentladegeschwindigkeit in mm/s, normalerweise wird eine höhere Geschwindigkeit als die Entladegeschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                                       | Nummer         | 10           |

{% hint style="warning" %}  
Eine weitere notwendige Einstellung für Ihren Abschnitt\[Extruder]geben Sie an[**max_extrudieren_nur_Distanz**](https://www.klipper3d.org/Config_Reference.html#extruder)...der empfohlene Wert ist normalerweise >101 (falls nicht definiert, verwenden Sie 50), um beispielsweise typische Extruder-Kalibrierungstests zu ermöglichen.  
Sie sollten den Wert basierend auf dem, was zuvor über den Test oder die Konfiguration Ihres Geräts erwähnt wurde, anpassen**Variable_Filament_entladen_Länge**ICH**Variable_Filament_Belastung_Länge**.  
{% endint %}

#### Parken

Bei bestimmten Vorgängen unseres Druckers, wie z. B. Pausen, empfiehlt es sich, den Kopf zu parken. Die Makros in unserem Bundle verfügen zusätzlich zu den folgenden zu verwaltenden Variablen über diese Option:

| Variable                             | Beschreibung                                                                                                                                                                                                                                                                                                     | Mögliche Werte | Standardwert |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Start_drucken_Park_In       | Standort, an dem der Kopf während des Vorheizens abgestellt werden soll.                                                                                                                                                                                                                                         | zurück /       |              |
| Center /                             |                                                                                                                                                                                                                                                                                                                  |                |              |
| Vorderseite                          | zurück                                                                                                                                                                                                                                                                                                           |                |              |
| Variable_Start_drucken_Park_Mit_Höhe | Z-Höhe während des Vorheizens                                                                                                                                                                                                                                                                                    | Nummer         | 50           |
| Variable_Ende_drucken_Park_In        | Position, an der der Kopf geparkt werden soll, wenn ein Druckvorgang beendet oder abgebrochen wird.                                                                                                                                                                                                              | zurück /       |              |
| Center /                             |                                                                                                                                                                                                                                                                                                                  |                |              |
| Vorderseite                          | zurück                                                                                                                                                                                                                                                                                                           |                |              |
| Variable_Ende_drucken_Park_Mit_Hop   | Steigungsabstand in Z am Ende des Druckvorgangs.                                                                                                                                                                                                                                                                 | Nummer         | 20           |
| Variable_pause_drucken_Park_In       | Position, an der der Kopf beim Anhalten des Druckvorgangs geparkt werden soll.                                                                                                                                                                                                                                   | zurück /       |              |
| Center /                             |                                                                                                                                                                                                                                                                                                                  |                |              |
| Vorderseite                          | zurück                                                                                                                                                                                                                                                                                                           |                |              |
| Variable_pause_Leerlauf_Auszeit      | Wert (in Sekunden) der Aktivierung des Inaktivitätsprozesses in der Maschine, der Motoren freigibt und zum Verlust von Koordinaten führt,**Ein hoher Wert ist empfehlenswert, damit beim Aktivieren des PAUSE-Makros genügend Zeit zum Ausführen einer Aktion benötigt wird, bevor Koordinaten verloren gehen.** | Nummer         | 43200        |

#### Z-Neigung

Es ist wichtig, das Beste aus unserer Maschine herauszuholen, damit sie sich selbst nivelliert und dafür sorgt, dass sich unsere Maschine immer im besten Zustand befindet.

**Z-TILT ist im Grunde ein Prozess, der uns hilft, unsere Z-Motoren in Bezug auf unsere X- (kartesische) oder XY- (CoreXY) Achse/Gantry auszurichten.**. Mit diesem**Wir stellen sicher, dass unser Z immer perfekt, präzise und automatisch ausgerichtet ist**.

| Variable                         | Beschreibung                                                                                | Mögliche Werte | Standardwert |
| -------------------------------- | ------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_kalibrieren_Mit_Neigung | Ermöglicht, sofern in unserer Klipper-Konfiguration aktiviert, den Z-Tilt-Anpassungsprozess | Wahr falsch    | FALSCH       |

#### Schräg

Die Verwendung von[SCHRÄG](broken-reference)Für die Korrektur bzw. Feinjustierung unserer Drucker ist es äußerst ratsam, wenn wir Abweichungen in unseren Ausdrucken haben. Mit der folgenden Variablen können wir die Verwendung in unseren Makros ermöglichen:

| Variable                  | Beschreibung                                                                                                                                                                                                                         | Mögliche Werte | Standardwert          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | --------------------- |
| Variable_verzerren_Profil | Dadurch können wir unser Skew-Profil berücksichtigen, das in unser START-Makro geladen wird_DRUCKEN Um es zu aktivieren, müssen wir die Variable auskommentieren und den Namen des Skew-Profils aus unserer Konfiguration verwenden. | Text           | Mein_verzerren_Profil |

### Makroanpassung

Unser Modul für Klipper nutzt das in RatOS verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper bei der sequentiellen Verarbeitung seiner Konfigurationsdateien. Aus diesem Grund ist die Reihenfolge der Includes und benutzerdefinierten Einstellungen, die wir auf diese Module anwenden möchten, von entscheidender Bedeutung.

{% hint style="info" %}  
Bei Verwendung als Modul können 3Dwork-Konfigurationen NICHT direkt aus dem Verzeichnis 3dwork-klipper in Ihrem Klipper-Konfigurationsverzeichnis bearbeitet werden, da es aus Sicherheitsgründen schreibgeschützt ist.

Deshalb ist es sehr wichtig zu verstehen, wie Klipper funktioniert und wie wir unsere Module an Ihre Maschine anpassen können.  
{% endint %}

#### **Anpassen von Variablen**

Normalerweise müssen wir das anpassen, um Anpassungen an den Variablen vorzunehmen, die wir standardmäßig in unserem Modul haben**Deine Ausreden**para Cliffs.

Wir müssen lediglich den Inhalt des Makros einfügen\[gcode_Makro GLOBAL_WESSEN]was wir in Makros/Makros finden können_War_globals.cfg in unserer Printer.cfg.

Wir erinnern Sie an das, was wir zuvor darüber erwähnt haben, wie Klipper die Konfigurationen nacheinander verarbeitet. Daher ist es ratsam, es nach den von uns erwähnten Includes einzufügen.[Hier](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

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

{% hint style="warning" %}
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}

{% hint style="info" %}

-   Wir empfehlen Ihnen, Kommentare hinzuzufügen, wie Sie es im vorherigen Fall gesehen haben, um herauszufinden, was die einzelnen Abschnitte bewirken.
-   Obwohl Sie nicht alle Variablen berühren müssen, empfehlen wir Ihnen, den gesamten Inhalt von zu kopieren\[gcode_Makro GLOBAL_WESSEN]
    {% endhint %}

#### Anpassen von Makros

Die Makros sind modular aufgebaut, sodass sie leicht angepasst werden können. Wie bereits erwähnt, müssen wir, wenn wir sie anpassen möchten, genauso vorgehen wie bei den Variablen, das betreffende Makro in unsere Printer.cfg (oder ein anderes eigenes Include) kopieren und sicherstellen, dass es so ist nach dem Include, wo wir unser 3Dwork-Modul für Klipper hinzugefügt haben.

Wir haben zwei Gruppen von Makros:

-   Makros zum Hinzufügen von Benutzereinstellungen. Diese Makros können einfach hinzugefügt und angepasst werden, da sie so hinzugefügt wurden, dass jeder Benutzer die Aktionen in bestimmten Teilen der von jedem Makro ausgeführten Prozesse nach seinen Wünschen anpassen kann.

**START_DRUCKEN**

| Makroname                                      | Beschreibung                                                                                                                              |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| \_BENUTZER_START_DRUCKEN_HITZE_KAMMER          | Es wird ausgeführt, sobald sich unser Gehäuse zu erwärmen beginnt, wenn KAMMER_TEMP wird als Parameter an unseren START übergeben_DRUCKEN |
| \_BENUTZER_START_DRUCKEN_VOR_HOMING            | Wird vor der ersten Referenzierung des Druckstarts ausgeführt                                                                             |
| \_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_BETT     | Es wird ausgeführt, wenn unser Bett vorher seine Temperatur erreicht_START_DRUCKEN_NACH_HEIZUNG_BETT                                      |
| \_BENUTZER_START_DRUCKEN_BETT_GITTERGEWEBE     | Es wird vorher veröffentlicht_START_DRUCKEN_BETT_GITTERGEWEBE                                                                             |
| \_BENUTZER_START_DRUCKEN_PARK                  | Es wird vorher veröffentlicht_START_DRUCKEN_PARK                                                                                          |
| \_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_EXTRUDER | Es wird vorher veröffentlicht_START_DRUCKEN_NACH_HEIZUNG_EXTRUDER                                                                         |

**ENDE_DRUCKEN**

| Makroname                                  | Beschreibung                                                                                          |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| \_BENUTZER_ENDE_DRUCKEN_VOR_HEIZUNGEN_AUS  | Es wird vor dem Ausschalten der Heizungen ausgeführt_ENDE_DRUCKEN_VOR_HEIZUNGEN_AUS                   |
| \_BENUTZER_ENDE_DRUCKEN_NACH_HEIZUNGEN_AUS | Es wird ausgeführt, nachdem die Heizungen vorher ausgeschaltet wurden_ENDE_DRUCKEN_NACH_HEIZUNGEN_AUS |
| \_BENUTZER_ENDE_DRUCKEN_PARK               | Es wird ausgeführt, bevor der Kopf geparkt wird_ENDE_DRUCKEN_PARK                                     |

**DRUCKEN_GRUNDLAGEN**

| Makroname                         | Beschreibung                           |
| --------------------------------- | -------------------------------------- |
| \_BENUTZER_PAUSE_START            | Wird zu Beginn einer PAUSE ausgeführt  |
| \_BENUTZER_PAUSE_ENDE             | Wird am Ende einer PAUSE ausgeführt    |
| \_BENUTZER_WIEDER AUFNEHMEN_START | Wird zu Beginn eines RESUME ausgeführt |
| \_BENUTZER_WIEDER AUFNEHMEN_ENDE  | Wird am Ende eines RESUME ausgeführt   |

-   Interne Makros sind Makros zur Aufteilung des Hauptmakros in Prozesse und sind hierfür wichtig. Wenn Anpassungen erforderlich sind, empfiehlt es sich, diese unverändert zu kopieren.

**START_DRUCKEN**

| Makroname                             | Beschreibung                                                                                                                                                                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_START_DRUCKEN_HITZE_KAMMER          | Erhitzt das Gehäuse, wenn der CHAMBER-Parameter überschritten wird_TEMP wird von unserem START-Makro empfangen_DRUCKEN vom Laminator                                                                                                  |
| \_START_DRUCKEN_NACH_HEIZUNG_BETT     | Es wird ausgeführt, wenn das Bett die Temperatur erreicht hat_BENUTZER_START_DRUCKEN_NACH_HEIZUNG_BETT. Wird normalerweise zur Verarbeitung von Bettkalibrierungen verwendet (Z_NEIGUNG_EINSTELLEN, VIERFACH_PORTAL_NIVELLIERUNG,...) |
| \_START_DRUCKEN_BETT_GITTERGEWEBE     | Es kümmert sich um die Bettvernetzungslogik.                                                                                                                                                                                          |
| \_START_DRUCKEN_PARK                  | Parken Sie den Druckkopf, während Sie die Düse auf Drucktemperatur erwärmen.                                                                                                                                                          |
| \_START_DRUCKEN_NACH_HEIZUNG_EXTRUDER | Spülen Sie die Düse und laden Sie das SKEW-Profil, wenn dies in den Variablen definiert ist                                                                                                                                           |

## Drucker und Elektronik

Da wir mit verschiedenen Drucker- und Elektronikmodellen arbeiten, werden wir diejenigen hinzufügen, die nicht direkt von RatOS unterstützt werden, unabhängig davon, ob es sich um Beiträge von uns oder aus der Community handelt.

-   Drucker, in diesem Verzeichnis haben wir alle Druckerkonfigurationen
-   Boards, hier finden wir die elektronischen

### Parameter und Pins

Unser Modul für Klipper nutzt das in RatOS verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper bei der sequentiellen Verarbeitung seiner Konfigurationsdateien. Aus diesem Grund ist die Reihenfolge der Includes und benutzerdefinierten Einstellungen, die wir auf diese Module anwenden möchten, von entscheidender Bedeutung.

{% hint style="info" %}
Bei Verwendung als Modul können 3Dwork-Konfigurationen NICHT direkt aus dem Verzeichnis 3dwork-klipper in Ihrem Klipper-Konfigurationsverzeichnis bearbeitet werden, da es aus Sicherheitsgründen schreibgeschützt ist.

Deshalb ist es sehr wichtig zu verstehen, wie Klipper funktioniert und wie wir unsere Module an Ihre Maschine anpassen können.
{% endhint %}

Wie wir in „[Anpassen von Makros](3dwork-klipper-bundle.md#personalizando-macros)„Wir werden den gleichen Prozess verwenden, um Parameter oder Pins an unsere Bedürfnisse anzupassen.

#### Anpassen von Parametern

Ebenso empfehlen wir Ihnen, in Ihrer Printer.cfg einen Abschnitt namens USER OVERRIDES zu erstellen, der nach den Includes unserer Konfigurationen platziert wird, um alle darin verwendeten Parameter anpassen und anpassen zu können.

Im folgenden Beispiel werden wir sehen, wie wir in unserem Fall daran interessiert sind, die Parameter unserer Bettnivellierung (Bett) anzupassen_Netz) durch Anpassen der Sondenpunkte_count) in Bezug auf die Konfiguration, die wir standardmäßig in den Konfigurationen unseres Klipper-Moduls haben:

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

{%endcode%}

{% hint style="warning" %}
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}

Wir können denselben Prozess mit jedem Parameter verwenden, den wir anpassen möchten.

#### Anpassen der Pin-Konfiguration

Wir werden genau wie zuvor vorgehen und in unserem Bereich USER OVERRIDES die Pin-Abschnitte hinzufügen, die wir nach unseren Wünschen anpassen möchten.

Im folgenden Beispiel werden wir den Pin unseres elektronischen Lüfters (Controllers) anpassen_Ventilator), um ihn einem anderen als dem Standard-Lüfter zuzuweisen:

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

{%endcode%}

{% hint style="warning" %}
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}

```

```
