* * *

## Beschreibung: Paket mit Makros, Einstellungen und anderen Dienstprogrammen für Klipper

# 3Dwork Clipper-Paket

> [!WARNUNG]**LEITFADEN IN BEARBEITUNG!!! Obwohl die Makros voll funktionsfähig sind, werden sie kontinuierlich weiterentwickelt.****Die Nutzung erfolgt auf eigene Gefahr!!!**</mark>

Aus**Deine Ausreden**Wir haben eine Reihe von Makros, Maschinen- und Elektronikeinstellungen sowie anderen Tools für eine einfache und leistungsstarke Klipper-Verwaltung zusammengestellt und verfeinert.

Ein Großteil dieses Pakets basiert auf[**Ratten**](https://os.ratrig.com/)Verbesserung der Teile, die wir für interessant halten, sowie anderer Beiträge aus der Community.

## Installation

Um unser Paket für Klipper zu installieren, führen wir die folgenden Schritte aus

### Aus dem Repository herunterladen

Wir verbinden uns über SSH mit unserem Host und geben die folgenden Befehle aus:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> [!WARNUNG]Wenn Ihr Klipper-Konfigurationsverzeichnis angepasst ist, denken Sie daran, den ersten Befehl entsprechend Ihrer Installation anzupassen.

Bei Neuinstallationen:

Da Klipper keinen Zugriff auf Makros zulässt, bis es über eine korrekte Printer.cfg verfügt und eine Verbindung zu einer MCU herstellt, können wir Klipper mit den folgenden Schritten „austricksen“, die es uns ermöglichen, die Makros in unserem Bundle zu verwenden, um beispielsweise die zu starten Klipper-Firmware-Kompilierungsmakro, wenn wir kompatible Elektronik verwenden:

-   Wir stellen sicher, dass wir unsere haben[Host als zweite MCU](raspberry-como-segunda-mcu.md)
-   Als nächstes fügen wir eine Printer.cfg hinzu. Denken Sie daran, dass diese Schritte für eine Neuinstallation gelten, bei der Sie keine Printer.cfg haben und das Makro zum Erstellen von Firmware starten möchten, wie das, das Sie unten sehen können:

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

Damit können wir Klipper starten, um Zugriff auf unsere Makros zu erhalten.
{% endhint %}

### Mit Moonraker immer auf dem neuesten Stand bleiben

Dank Moonraker können wir das Update nutzen_Manager, um über die Verbesserungen, die wir möglicherweise in der Zukunft einführen, auf dem Laufenden zu bleiben.

Von Mainsail/Fluidd aus bearbeiten wir unsere Moonraker.conf (sie sollte auf der gleichen Höhe wie Ihre Printer.cfg sein) und fügen am Ende der Konfigurationsdatei Folgendes hinzu:

```django
[include 3dwork-klipper/moonraker.conf]
```

{% hint style="warning" %}<mark style="color:orange;">**Denken Sie daran, den Installationsschritt vorher durchzuführen, da Moonraker sonst einen Fehler generiert und nicht gestartet werden kann.**</mark>

**Wenn andererseits das Verzeichnis Ihrer Klipper-Konfiguration angepasst ist, denken Sie daran, den Pfad entsprechend Ihrer Installation anzupassen.**{% endint %}

## Makros

Wir haben immer darauf hingewiesen, dass RatOS eine der besten Klipper-Distributionen ist und Raspberry- und CB1-Module unterstützt, vor allem aufgrund seiner modularen Konfiguration und seiner großartigen Makros.

Einige hinzugefügte Makros, die für uns nützlich sein werden:

### **Allzweckmakros**

| Makro                                                                                  | Beschreibung                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VIELLEICHT_HEIM**                                                                    | Dadurch können wir den Referenzierungsprozess nur optimieren, indem wir ihn auf den Achsen durchführen, die nicht referenziert werden.                                                                                                                                                             |
| **PAUSE**                                                                              | Durch die zugehörigen Variablen können wir eine Pause mit einem vielseitigeren Kopfparkmodus verwalten als mit normalen Makros.                                                                                                                                                                    |
| <p><strong>SET_PAUSE_AT_LAYER</strong><br><strong>SET_PAUSE_AT_NEXT_LAYER</strong></p> | <p>Ein sehr nützliches Makro, das Mainsail in seine Benutzeroberfläche integriert, um bei Bedarf in einer bestimmten Ebene pausieren zu können ... für den Fall, dass wir es beim Laminieren vergessen haben.<br>Wir haben auch eine weitere, um die Pause auf der nächsten Ebene auszuführen.</p> |
| **WIEDER AUFNEHMEN**                                                                   | Verbessert, da wir damit erkennen können, ob unsere Düse nicht die Extrusionstemperatur hat, um das Problem zu beheben, bevor ein Fehler auftritt und unser Drucksystem beschädigt wird.                                                                                                           |
| **STORNIEREN_DRUCKEN**                                                                 | Dies ermöglicht die Verwendung der restlichen Makros, um einen Druckabbruch korrekt durchzuführen.                                                                                                                                                                                                 |

-   **Bei Ebenenwechsel angehalten**, einige sehr interessante Makros, die es uns ermöglichen, eine Ebene anzuhalten oder einen Befehl zu starten, wenn wir die nächste Ebene starten. \\![](<../../.gitbook/assets/image (6) (5) (1) (2).png>)![](<../../.gitbook/assets/image (1) (1) (8).png>)\\
    Ein weiterer Vorteil besteht darin, dass sie in Mainsail integriert sind, sodass wir neue Funktionen in unserer Benutzeroberfläche haben werden, wie Sie unten sehen können:\\![](<../../.gitbook/assets/image (3) (15).png>)![](<../../.gitbook/assets/image (29) (1) (2).png>)

### **Makros zur Druckverwaltung**

<table><thead><tr><th width="170">Macro</th><th>Descripción</th></tr></thead><tbody><tr><td><strong>START_PRINT</strong></td><td>Nos permitirá poder iniciar nuestras impresiones de una forma segura y al estilo Klipper. Dentro de esta encontraremos algunas funciones interesantes como:<br>- precalentado de nozzle inteligente en el caso de contar con sensor probe<br>- posibilidad de uso de z-tilt mediante variable<br>- mallado de cama adaptativo, forzado o desde una malla guardada<br>- línea de purga personalizable entre normal, línea de purgado adaptativa o gota de purgado<br>- macro segmentada para poder personalizarse tal como os mostraremos más adelante</td></tr><tr><td><strong>END_PRINT</strong></td><td>Macro de fin de impresión donde también disponemos de segmentación para poder personalizar nuestra macro. También contamos con aparcado dinámico del cabezal.</td></tr></tbody></table>

-   **Adaptives Bettnetz**Dank der Vielseitigkeit von Klipper können wir Dinge tun, die heute unmöglich erscheinen ... Ein wichtiger Prozess beim Drucken besteht darin, ein Netz von Abweichungen von unserem Bett zu erstellen, das es uns ermöglicht, diese zu korrigieren, um eine perfekte Haftung der ersten Schichten zu erreichen. \\
    Bei vielen Gelegenheiten führen wir diese Vernetzung vor dem Drucken durch, um sicherzustellen, dass es ordnungsgemäß funktioniert, und zwar auf der gesamten Oberfläche unseres Bettes.\\
    Bei der adaptiven Bettvernetzung erfolgt dies im Druckbereich und ist damit viel präziser als die herkömmliche Methode. In den folgenden Screenshots sehen wir die Unterschiede zwischen einem herkömmlichen und einem adaptiven Netz.\\![](<../../.gitbook/assets/image (6) (12) (1).png>)![](<../../.gitbook/assets/image (2) (1) (4).png>)

### **Makros zur Filamentverwaltung**

| Makro                  | Beschreibung                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **M600**               | Dies ermöglicht uns die Kompatibilität mit dem M600-Gcode, der normalerweise in Laminatoren für den Filamentwechsel verwendet wird. |
| **ENTLADEN_FILAMENT**  | Über die Variablen konfigurierbar, ermöglicht es uns eine unterstützte Filamententladung.                                           |
| **BELASTUNG_FILAMENT** | Wie das vorherige, jedoch bezogen auf die Filamentlast.                                                                             |

### **Maschinenkonfigurationsmakros**

| Makro                                                                                        | Beschreibung                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KOMPILIEREN_FIRMWARE**                                                                     | <p>Mit diesem Makro können wir die Klipper-Firmware auf einfache Weise kompilieren, zur Vereinfachung über die Benutzeroberfläche auf die Firmware zugreifen und sie auf unsere Elektronik anwenden.<br>Hier finden Sie weitere Details zur unterstützten Elektronik.</p> |
| **BERECHNUNG_BETT_GITTERGEWEBE**                                                             | Ein äußerst nützliches Makro zur Berechnung der Fläche für unser Netz, da dies manchmal ein komplizierter Prozess sein kann.                                                                                                                                              |
| <p><strong>PID_ALL</strong><br><strong>PID_EXTRUDER</strong><br><strong>PID_BED</strong></p> | Mithilfe dieser Makros, mit denen wir die Temperaturen in Form von Parametern an den PID übergeben können, können wir die Temperaturkalibrierung auf äußerst einfache Weise durchführen.                                                                                  |
| <p><strong>TESTGESCHWINDIGKEIT</strong><br><strong>TEST_SPEED_DELTA</strong></p>             | Das Originalmakro des Companion[Ellis](https://github.com/AndrewEllis93)Sie werden es uns auf relativ einfache Weise ermöglichen, die Geschwindigkeit zu testen, mit der wir unsere Maschine präzise und ohne Schrittverluste bewegen können.                             |

-   **Kompilierte Firmware für unterstützte Elektronik**Um den Prozess der Erstellung und Wartung unserer Klipper-Firmware für unsere MCUs zu erleichtern, haben wir das Makro COMPILE_FIRMWARE, dass wir bei der Ausführung unsere Elektronik als Parameter verwenden können, um nur dies zu tun. Klipper kompiliert für alle von unserem Bundle unterstützten Elektronikkomponenten:\\![](<../../.gitbook/assets/image (7) (5) (1).png>)\\
    Wir finden diese leicht zugänglich über unsere Web-Benutzeroberfläche im Firmware-Verzeichnis_Binärdateien in unserem MASCHINEN-Tab (wenn wir Großsegel verwenden):\\![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)\\
    Nachfolgend finden Sie die Liste der unterstützten Elektronikgeräte:

{% hint style="warning" %}**WICHTIG!!!**

-   Diese Skripte sind für die Arbeit auf einem Raspbian-System mit Pi-Benutzer vorbereitet. Wenn dies nicht der Fall ist, müssen Sie sie anpassen.
-   Die Firmwares werden für die Verwendung mit einer USB-Verbindung generiert, was wir immer empfehlen. Darüber hinaus ist der USB-Montagepunkt immer derselbe, sodass sich Ihre MCU-Verbindungskonfiguration nicht ändert, wenn sie mit unserem Makro/Skript generiert werden.
-   **Damit Klipper Shell-Makros ausführen kann, muss dank des Companion eine Erweiterung installiert werden**[**Arkussinus**](https://github.com/Arksine)**, das erlaubt es.**

        <mark style="color:green;">**Dependiendo de la distro de Klipper usada pueden venir ya habilitadas.**</mark>

        ![](<../../.gitbook/assets/image (1179).png>)

        La forma más sencilla es usando [**Kiauh**](../instalacion/#instalando-kiauh) donde encontraremos en una de sus opciones la posibilidad de instalar esta extensión:

        ![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x\_partial.jpg)

        También podemos realizar el proceso a mano copiaremos manualmente el plugin para Klipper[ **gcode\_shell\_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode\_shell\_command.py) dentro de nuestro directorio _**`~/klipper/klippy/extras`**_ usando SSH o SCP y reiniciamos Klipper.

    {% endint %}

{% tabs %}
{% tab title="Bigtreetech" %}
| Elektronik | Parametername zur Verwendung im Makro |
\| ------------------- \| ----------------------------------- \|
| Octopus Pro (446) | Oktopus_Profi_446 |
| Octopus Pro (429) | Oktopus_Profi_429 |
| Octopus v1.1 | Oktopus_11 |
| Octopus v1.1 (407) | Oktopus_11_407 |
| SKR Pro v1.2 | skr_Profi_12 |
| 3 SEK | Übrigens_skr_3 |
| SKR 2 (429) | skr_2_429 |
| SKR Mini E3 v3 | Übrigens_skr_Mini_ez_30              |

| Werkzeugkopf (CAN) | Parametername, der im Makro verwendet werden soll |
| ------------------ | ------------------------------------------------- |
| EBB42 v1           | Übrigens_ebb42_10                                 |
| EBB36 v1           | Übrigens_Ebbe36_10                                |
| EBB42 v1.1         | Übrigens_ebb42_11                                 |
| EBB36 v1.1         | Übrigens_Ebbe36_11                                |
| EBB42 v1.2         | Übrigens_ebb42_12                                 |
| EBB36 v1.2         | Übrigens_Ebbe36_12                                |

{% Endverlust %}

{% tab title="MKS/ZNP" %}
| Elektronik | Parametername zur Verwendung im Makro |
\| -------------------- \| ----------------------------------- \|
| ZNP Robin Nano DW v2 | znp_Robin_Nano_dw_v2 |
{% endtab %}

{% tab title="Mellow" %}
| Werkzeugkopf (CAN) | Parametername zur Verwendung im Makro |
\| ----------------- \| ----------------------------------- \|
| Mellow FLY SHT 42 | weich_Fliege_Scheiße_42 |
| Mellow FLY SHT 36 | weich_Fliege_Scheiße_36 |
{% Endverlust %}

{% tab title="Fysetc" %}
| Elektronik | Parametername zur Verwendung im Makro |
\| ------------- \| ----------------------------------- \|
| Fysetc Spinne | fysetc_Spinne |
{% endtab %}
{% endtabs %}

### Hinzufügen von 3Dwork-Makros zu unserer Installation

Über unsere Schnittstelle „Mainsail/Fluidd“ bearbeiten wir unsere Datei „printer.cfg“ und fügen Folgendes hinzu:

{% code title="printer.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{%endcode%}

{% hint style="info" %}
Es ist wichtig, dass wir diese Zeilen am Ende unserer Konfigurationsdatei hinzufügen ... direkt über dem Abschnitt, damit Makros in unserer CFG oder in Includes von unseren überschrieben werden:\\#\*# &lt;---------------------- SPEICHERN_KONFIG -------->
{% endhint %}

{% hint style="warning" %}
Normale Makros wurden abgetrennt**Makros-Shell**angesichts dessen**Um diese zu aktivieren, müssen zusätzlich zu der Tatsache, dass sie derzeit getestet werden, weitere Schritte manuell durchgeführt werden.**Und**Sie benötigen möglicherweise zusätzliche Berechtigungen, um Ausführungsberechtigungen zuzuweisen, für die keine Anweisungen angegeben wurden, da sie eine Automatisierung anstreben.**\\<mark style="color:red;">**Die Nutzung geschieht auf eigenes Risiko.**</mark>{% endint %}

### Konfiguration unseres Laminators

Da unsere Makros dynamisch sind, extrahieren sie bestimmte Informationen aus unserer Druckerkonfiguration und dem Laminator selbst. Hierzu empfehlen wir Ihnen, Ihre Laminatoren wie folgt zu konfigurieren:

-   **Starten Sie den Gcode START_DRUCKEN**, unter Verwendung von Platzhaltern, um Filament- und Betttemperaturwerte dynamisch zu übergeben:

{% tabs %}
{% tab title="PrusaSlicer-SuperSlicer" %}**Prusa-Schneider**

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer**- Wir haben die Möglichkeit, die Gehäusetemperatur (KAMMER) anzupassen

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](<../../.gitbook/assets/image (210).png>){% Endverlust %}

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
Wir müssen das Plugin installieren[**Post Process Plugin (von frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)aus dem Menü_**Hilfe/Anzeigen**_Konfigurationsordner... wir kopieren das Skript vom vorherigen Link in den Skriptordner. \\
Wir starten Cura neu und gehen zu_**Erweiterungen/Nachbearbeitung/G-Code ändern**_und wir werden auswählen_**Mesh-Druckgröße**_,
{% endint %}
{% indtab %}

{% tab title="IdeaMaker" %}

```gcode
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

{% Endverlust %}

{% tab title="Simplify3D" %}

```gcode
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

{% Endverlust %}
{% Endverlust %}

{% hint style="info" %}
Los**Platzhalter sind „Aliase“ oder Variablen, die die Laminatoren verwenden, damit sie bei der Generierung des GCodes durch die im Profil konfigurierten Werte ersetzt werden**des Eindrucks.

Unter den folgenden Links finden Sie eine Liste davon für:[**Prusa-Schneider**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(zusätzlich zu den oben genannten),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)Und[**Behandlung**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

Durch deren Verwendung können unsere Makros dynamisch sein.
{% endhint %}

-   **gcode das endgültige ENDE_DRUCKEN**, in diesem Fall ist es für alle Laminatoren gleich, da keine Platzhalter verwendet werden

```gcode
END_PRINT
```

### Variablen

Wie bereits erwähnt, ermöglichen uns diese neuen Makros einige sehr nützliche Funktionen, die wir oben aufgeführt haben.

Um diese an unsere Maschine anzupassen, verwenden wir die Variablen, die wir in Makros/Makros finden_War_globals.cfg, auf die wir weiter unten näher eingehen.

#### Nachrichten-/Benachrichtigungssprache

Da viele Benutzer gerne Makrobenachrichtigungen in ihrer Sprache haben, haben wir ein mehrsprachiges Benachrichtigungssystem entwickelt, derzeit Spanisch (es) und Englisch (en). In der folgenden Variablen können wir es anpassen:

<table><thead><tr><th width="189">Variable</th><th width="247">Descripción</th><th width="163">Valores posibles</th><th>Valor por defecto</th></tr></thead><tbody><tr><td>variable_language</td><td>Nos permite seleccionar el idioma de las notificaciones. En el caso de no estar bien definido se usará en (inglés)</td><td>es / en</td><td>es</td></tr></tbody></table>

#### Relative Extrusion

Damit können wir steuern, welchen Extrusionsmodus wir am Ende unseres START verwenden.\_DRUCKEN Der Wert hängt von der Konfiguration unseres Laminators ab.

{% hint style="success" %}
Es empfiehlt sich, Ihren Laminator für die Verwendung der relativen Extrusion zu konfigurieren und diese Variable auf „True“ zu setzen.
{% endhint %}

| Variable                   | Beschreibung                                                                   | Mögliche Werte | Standardwert |
| -------------------------- | ------------------------------------------------------------------------------ | -------------- | ------------ |
| Variable_relativ_Extrusion | Damit können wir den in unserem Laminator verwendeten Extrusionsmodus angeben. | Wahr falsch    | WAHR         |

#### Geschwindigkeiten

Zum Verwalten der in Makros verwendeten Geschwindigkeiten.

| Variable                              | Beschreibung                            | Mögliche Werte | Standardwert |   |
| ------------------------------------- | --------------------------------------- | -------------- | ------------ | - |
| Variable_Makro_reisen_Geschwindigkeit | Übertragungsgeschwindigkeit             | numerisch      | 150          |   |
| Variable_Makro_Mit_Geschwindigkeit    | Übertragungsgeschwindigkeit für Z-Achse | numerisch      | 15           |   |

#### Heimkehr

Satz von Variablen, die sich auf den Referenzierungsprozess beziehen.

| Variable | Beschreibung | Mögliche Werte | Standardwert |
| -------- | ------------ | -------------- | ------------ |
|          |              |                |              |

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
-   Ermöglicht das Aufweichen des restlichen Filaments in der Düse, was bedeutet, dass diese Reste in bestimmten Konfigurationen keinen Einfluss auf die Aktivierung des Sensors haben.
    {% endhint %}

#### Bettgitter

Um den Nivellierungsprozess zu steuern, verfügen wir über Variablen, die sehr nützlich sein können. Beispielsweise können wir die Art der Nivellierung steuern, die wir verwenden möchten, indem wir immer ein neues Netz erstellen, ein zuvor gespeichertes laden oder adaptive Vernetzung verwenden.

| Variable                               | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Mögliche Werte                                   | Standardwert |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------ |
| Variable_kalibrieren_Bett_Gittergewebe | <p>Damit können wir auswählen, welche Art von Netz wir in unserem START_PRINT verwenden:<br>- Neues Netz, es wird jeden Druck vernetzen<br>- Storedmesh, lädt ein gespeichertes Mesh und führt keine Bettabfrage durch<br>- Adaptiv, es wird ein neues Netz erstellt, das jedoch an den Druckbereich angepasst ist, wodurch häufig unsere ersten Schichten verbessert werden<br>- Nomesh, falls wir keinen Sensor haben oder Mesh verwenden, um den Vorgang zu überspringen</p> | <p>Nevmesh / Storedmesh / Adaptiv /<br>Namen</p> | adaptiv      |
| Variable_Bett_Gittergewebe_Profil      | Der Name, der für unser gespeichertes Mesh verwendet wird                                                                                                                                                                                                                                                                                                                                                                                                                       | Text                                             | Standard     |

{% hint style="warning" %}
Wir empfehlen Ihnen, die adaptive Nivellierung zu verwenden, da dadurch das Netz immer an die Größe unseres Drucks angepasst wird, sodass Sie über einen angepassten Netzbereich verfügen.

Es ist wichtig, dass wir in unserem[Start-Gcode unseres Laminators](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), im Aufruf zu unserem START_PRINT, PRINT-Werte_MAX y DRUCKEN_Mann.
{% endint %}

#### gesäubert

Eine wichtige Phase unseres Druckstarts ist das korrekte Spülen unserer Düse, um zu verhindern, dass Filamentreste zurückbleiben oder dass diese unseren Druck irgendwann beschädigen könnten. Nachfolgend finden Sie die Variablen, die in diesen Prozess eingreifen:

| Variable                                   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                  | Mögliche Werte                                                        | Standardwert        |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------- |
| Variable_Düse_Grundierung                  | <p>Wir können zwischen verschiedenen Spüloptionen wählen:<br>- primeline zeichnet die typische Reinigungslinie<br>- primelineadaptative generiert eine Spüllinie, die sich an die Fläche des gedruckten Teils anpasst, wobei variable_nozzle_priming_objectdistance als Rand verwendet wird<br>- Mit Primeblob werfen wir einen Tropfen Filament in eine Ecke unseres Bettes, sehr effektiv zum Reinigen der Düse und leicht zu entfernen</p> | <p>Hauptlinie /</p><p>primelineadaptiv /<br>primeblob /<br>FALSCH</p> | adaptive Primlinien |
| Variable_Düse_Grundierung_Objektentfernung | Wenn wir eine adaptive Beschnittlinie verwenden, ist dies der Rand, der zwischen der Beschnittlinie und dem gedruckten Objekt verwendet werden soll                                                                                                                                                                                                                                                                                           | numerisch                                                             | 5                   |
| Variable_Düse_Primzahl_Start_X             | <p>Wo wir unsere Spülleitung platzieren möchten:<br>- min wird es bei X=0 tun (plus einer kleinen Sicherheitsmarge)<br>- max wird dies bei X=max tun (abzüglich einer kleinen Sicherheitsmarge)<br>- Die Zahl ist die X-Koordinate, an der die Spülung erfolgen soll</p>                                                                                                                                                                      | <p>Mindest /<br>max. /<br>Nummer</p>                                  | max                 |
| Variable_Düse_Primzahl_Start_Und           | <p>Wo wir unsere Spülleitung platzieren möchten:<br>- min wird es bei Y=0 tun (plus einer kleinen Sicherheitsmarge)<br>- max wird dies bei Y=max tun (abzüglich einer kleinen Sicherheitsmarge)<br>- Die Zahl ist die Y-Koordinate, an der die Spülung erfolgen soll</p>                                                                                                                                                                      | <p>Mindest /<br>max. /<br>Nummer</p>                                  | Mindest             |
| Variable_Düse_Primzahl_Richtung            | <p>Die Adresse unserer Leitung oder Zustellung:<br>- Nach hinten bewegt sich der Kopf zur Vorderseite des Druckers<br>- Vorwärts bewegt sich nach hinten<br>- Auto bewegt sich abhängig von variable_nozzle_prime_start_y zur Mitte</p>                                                                                                                                                                                                       | <p>automatisch /<br>vorwärts /<br>rückwärts</p>                       | Auto                |

#### Laden/Entladen des Filaments

In diesem Fall erleichtert uns diese Gruppe von Variablen die Verwaltung des Ladens und Entladens unseres Filaments, das beispielsweise in der M600-Emulation verwendet wird, oder beim Starten der Makros zum Laden und Entladen von Filamenten:

| Variable                                    | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                            | Mögliche Werte | Standardwert |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_Filament_entladen_Länge            | Wie viel mm das Filament zurückgezogen werden muss, passen Sie an Ihre Maschine an, normalerweise das Maß von Ihrer Düse bis zu den Zahnrädern Ihres Extruders, wobei ein zusätzlicher Spielraum hinzukommt.                                                                                                                                                                                                                                            | Nummer         | 130          |
| Variable_Filament_entladen_Geschwindigkeit  | Filamentrückzugsgeschwindigkeit in mm/s. Normalerweise wird eine langsame Geschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                                                    | Nummer         | 5            |
| Variable_Filament_Belastung_Länge           | Abstand in mm zum Laden des neuen Filaments... sowie variabel_Filament_entladen_Länge verwenden wir das Maß von Ihrem Getriebe bis zum Extruder und fügen einen zusätzlichen Spielraum hinzu. In diesem Fall hängt dieser zusätzliche Wert davon ab, wie viel gespült werden soll. Normalerweise können Sie ihm einen größeren Spielraum als den vorherigen Wert geben, um sicherzustellen, dass die Die Extrusion des vorherigen Filaments ist sauber. | Nummer         | 150          |
| Variable_Filament_Belastung_Geschwindigkeit | Filamentladegeschwindigkeit in mm/s, normalerweise wird eine höhere Geschwindigkeit als die Entladegeschwindigkeit verwendet.                                                                                                                                                                                                                                                                                                                           | Nummer         | 10           |

{% hint style="warning" %}
Eine weitere notwendige Einstellung für Ihren Abschnitt\[Extruder] zeigt an[<mark style="color:green;">**max_extrudieren_nur_Distanz**</mark>](https://www.klipper3d.org/Config_Reference.html#extruder)...der empfohlene Wert ist normalerweise >101 (falls nicht definiert, verwenden Sie 50), um beispielsweise typische Extruder-Kalibrierungstests zu ermöglichen. \\
Sie sollten den Wert basierend auf dem, was zuvor über den Test oder die Konfiguration Ihres Geräts erwähnt wurde, anpassen**Variable_Filament_entladen_Länge**ICH**Variable_Filament_Belastung_Länge**,
{% endint %}

#### Parken

Bei bestimmten Vorgängen unseres Druckers, wie z. B. Pausen, empfiehlt es sich, den Kopf zu parken. Die Makros in unserem Bundle verfügen zusätzlich zu den folgenden zu verwaltenden Variablen über diese Option:

| Variable                             | Beschreibung                                                                                                                                                                                                                                                                                                     | Mögliche Werte                             | Standardwert |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------ |
| Variable_Start_drucken_Park_In       | Standort, an dem der Kopf während des Vorheizens abgestellt werden soll.                                                                                                                                                                                                                                         | <p>zurück /<br>Center /<br>Vorderseite</p> | zurück       |
| Variable_Start_drucken_Park_Mit_Höhe | Z-Höhe während des Vorheizens                                                                                                                                                                                                                                                                                    | Nummer                                     | 50           |
| Variable_Ende_drucken_Park_In        | Position, an der der Kopf geparkt werden soll, wenn ein Druckvorgang beendet oder abgebrochen wird.                                                                                                                                                                                                              | <p>zurück /<br>Center /<br>Vorderseite</p> | zurück       |
| Variable_Ende_drucken_Park_Mit_Hop   | Steigungsabstand in Z am Ende des Druckvorgangs.                                                                                                                                                                                                                                                                 | Nummer                                     | 20           |
| Variable_pause_drucken_Park_In       | Position, an der der Kopf beim Anhalten des Druckvorgangs geparkt werden soll.                                                                                                                                                                                                                                   | <p>zurück /<br>Center /<br>Vorderseite</p> | zurück       |
| Variable_pause_Leerlauf_Auszeit      | Wert (in Sekunden) der Aktivierung des Inaktivitätsprozesses in der Maschine, der Motoren freigibt und zum Verlust von Koordinaten führt,**Ein hoher Wert ist empfehlenswert, damit beim Aktivieren des PAUSE-Makros genügend Zeit zum Ausführen einer Aktion benötigt wird, bevor Koordinaten verloren gehen.** | Nummer                                     | 43200        |

#### Z-Neigung

Es ist wichtig, das Beste aus unserer Maschine herauszuholen, damit sie sich selbst nivelliert und dafür sorgt, dass sich unsere Maschine immer im besten Zustand befindet.

**Z-TILT ist im Grunde ein Prozess, der uns hilft, unsere Z-Motoren in Bezug auf unsere X- (kartesische) oder XY- (CoreXY) Achse/Gantry auszurichten.**. Mit diesem**Wir stellen sicher, dass unser Z immer perfekt, präzise und automatisch ausgerichtet ist**.

| Variable                         | Beschreibung                                                                                | Mögliche Werte | Standardwert |
| -------------------------------- | ------------------------------------------------------------------------------------------- | -------------- | ------------ |
| Variable_kalibrieren_Mit_Neigung | Ermöglicht, sofern in unserer Klipper-Konfiguration aktiviert, den Z-Tilt-Anpassungsprozess | Wahr falsch    | FALSCH       |

#### Schräg

Die Verwendung von[SCHRÄG](../../guias-impresion-3d/calibracion_3d.md#7.-pasos-ejes)Für die Korrektur bzw. Feinjustierung unserer Drucker ist es äußerst ratsam, wenn wir Abweichungen in unseren Ausdrucken haben. Mit der folgenden Variablen können wir die Verwendung in unseren Makros ermöglichen:

| Variable                  | Beschreibung                                                                                                                                                                                                                         | Mögliche Werte | Standardwert          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | --------------------- |
| Variable_verzerren_Profil | Dadurch können wir unser Skew-Profil berücksichtigen, das in unser START-Makro geladen wird_DRUCKEN Um es zu aktivieren, müssen wir die Variable auskommentieren und den Namen des Skew-Profils aus unserer Konfiguration verwenden. | Text           | Mein_verzerren_Profil |

### Makroanpassung

Unser Modul für Klipper nutzt das in RatOS verwendete modulare Konfigurationssystem und nutzt die Vorteile von Klipper bei der sequentiellen Verarbeitung seiner Konfigurationsdateien. Aus diesem Grund ist die Reihenfolge der Includes und benutzerdefinierten Einstellungen, die wir auf diese Module anwenden möchten, von entscheidender Bedeutung.

{% hint style="info" %}
Bei Verwendung als Modul können 3Dwork-Konfigurationen NICHT direkt aus dem Verzeichnis 3dwork-klipper in Ihrem Klipper-Konfigurationsverzeichnis bearbeitet werden, da es aus Sicherheitsgründen schreibgeschützt ist.

Deshalb ist es sehr wichtig zu verstehen, wie Klipper funktioniert und wie wir unsere Module an Ihre Maschine anpassen können.
{% endhint %}

#### **Anpassen von Variablen**

Normalerweise müssen wir das anpassen, um Anpassungen an den Variablen vorzunehmen, die wir standardmäßig in unserem Modul haben**Deine Ausreden**para Cliffs.

Wir müssen lediglich den Inhalt des Makros einfügen\[gcode_Makro GLOBAL_VARS], die wir in Makros/Makros finden können_War_globals.cfg in unserer Printer.cfg.

Wir erinnern Sie an das, was wir zuvor darüber erwähnt haben, wie Klipper die Konfigurationen nacheinander verarbeitet. Daher ist es ratsam, es nach den von uns erwähnten Includes einzufügen.[Hier](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

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
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}

{% hint style="info" %}

-   Wir empfehlen Ihnen, Kommentare hinzuzufügen, wie Sie es im vorherigen Fall gesehen haben, um herauszufinden, was die einzelnen Abschnitte bewirken.
-   Obwohl Sie nicht alle Variablen berühren müssen, empfehlen wir Ihnen, den gesamten Inhalt von zu kopieren\[gcode_Makro GLOBAL_Jahr]
    {% endint %}

#### Anpassen von Makros

Die Makros sind modular aufgebaut, sodass sie leicht angepasst werden können. Wie bereits erwähnt, müssen wir, wenn wir sie anpassen möchten, genauso vorgehen wie bei den Variablen, das betreffende Makro in unsere Printer.cfg (oder ein anderes eigenes Include) kopieren und sicherstellen, dass es so ist nach dem Include, wo wir unser 3Dwork-Modul für Klipper hinzugefügt haben.

Wir haben zwei Gruppen von Makros:

-   Makros zum Hinzufügen von Benutzereinstellungen. Diese Makros können einfach hinzugefügt und angepasst werden, da sie so hinzugefügt wurden, dass jeder Benutzer die Aktionen in bestimmten Teilen der von jedem Makro ausgeführten Prozesse nach seinen Wünschen anpassen kann.

**START_DRUCKEN**

<table><thead><tr><th width="400">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_USER_START_PRINT_HEAT_CHAMBER</td><td>Se ejecuta justo después que nuestro cerramiento empiece a calentar, si CHAMBER_TEMP se pasa como parámetro a nuestro START_PRINT</td></tr><tr><td>_USER_START_PRINT_BEFORE_HOMING</td><td>Se ejecuta antes del homing inicial de inicio de impresión</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar nuestra cama a su temperatura, antes de _START_PRINT_AFTER_HEATING_BED</td></tr><tr><td>_USER_START_PRINT_BED_MESH</td><td>Se lanza antes de _START_PRINT_BED_MESH</td></tr><tr><td>_USER_START_PRINT_PARK</td><td>Se lanza antes de _START_PRINT_PARK</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Se lanza antes de _START_PRINT_AFTER_HEATING_EXTRUDER</td></tr></tbody></table>

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

<table><thead><tr><th width="405">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_START_PRINT_HEAT_CHAMBER</td><td>Calienta el cerramiento en el caso de que el parámetro CHAMBER_TEMP sea recibido por nuestra macro START_PRINT desde el laminador</td></tr><tr><td>_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar la cama a la temperatura, después de _USER_START_PRINT_AFTER_HEATING_BED. Normalmente, se usa para el procesado de calibraciones de cama (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...)</td></tr><tr><td>_START_PRINT_BED_MESH</td><td>Se encarga de la lógica de mallado de cama.</td></tr><tr><td>_START_PRINT_PARK</td><td>Aparca el cabezal de impresión mientras calienta el nozzle a la temperatura de impresión.</td></tr><tr><td>_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Realiza el purgado del nozzle y carga el perfil SKEW en caso de que así definamos en las variables</td></tr></tbody></table>

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

{%endcode%}

{% hint style="warning" %}
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}

Wir können denselben Prozess mit jedem Parameter verwenden, den wir anpassen möchten.

#### Anpassen der Pin-Konfiguration

Wir werden genau wie zuvor vorgehen und in unserem Bereich USER OVERRIDES die Pin-Abschnitte hinzufügen, die wir nach unseren Wünschen anpassen möchten.

Im folgenden Beispiel werden wir den Pin unseres elektronischen Lüfters (Controllers) anpassen_Ventilator), um ihn einem anderen als dem Standard-Lüfter zuzuweisen:

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

{%endcode%}

{% hint style="warning" %}
Die drei Punkte (...) in den vorherigen Beispielen sollen lediglich darauf hinweisen, dass Sie weitere Konfigurationen zwischen Abschnitten vornehmen können... auf keinen Fall sollten sie hinzugefügt werden.
{% endhint %}
