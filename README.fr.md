* * *

## description : Pack de macros, paramètres et autres utilitaires pour Klipper

# Pack Tondeuse 3Dwork

[![](../../.gitbook/assets/image%20(1986).png)- Anglais](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{% indice style="danger" %}  
**GUIDE EN COURS !!! Bien que les macros soient entièrement fonctionnelles, elles sont en développement continu.**

**Utilisez-les à vos risques et périls!!!**  
{% finint %}

Journal des modifications

12/07/2023 - Ajout du support pour automatiser la création du firmware électronique Bigtreetech

Depuis**Vos excuses**Nous avons compilé et affiné un ensemble de macros, de paramètres machines et électroniques, ainsi que d'autres outils pour une gestion simple et puissante de Klipper.

Une grande partie de ce package est basée sur[**Les rats**](https://os.ratrig.com/)améliorer les parties que nous jugeons intéressantes, ainsi que d'autres contributions de la communauté.

## Installation

Pour installer notre package pour Klipper, nous suivrons les étapes suivantes

### Télécharger depuis le référentiel

Nous allons nous connecter à notre hôte via SSH et émettre les commandes suivantes :

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{% indice style="avertissement" %}  
Si votre répertoire de configuration Klipper est personnalisé, n'oubliez pas d'ajuster la première commande en conséquence pour votre installation.  
{% finint %}

{% indice style="info" %}  
Dans les nouvelles installations :

Puisque Klipper n'autorise pas l'accès aux macros tant qu'il n'a pas un fichier Printer.cfg correct et qu'il ne se connecte pas à un MCU, nous pouvons "tromper" Klipper avec les étapes suivantes qui nous permettront d'utiliser les macros de notre bundle pour, par exemple, lancer le Macro de compilation du firmware Klipper si nous utilisons des électroniques compatibles :

-   Nous nous assurons d'avoir notre[hôte comme deuxième MCU](raspberry-como-segunda-mcu.md)
-   Ensuite, nous ajouterons un fichier Printer.cfg, rappelez-vous que ces étapes sont destinées à une installation propre où vous n'avez pas de fichier Printer.cfg et que vous souhaitez lancer la macro pour créer un firmware, comme celui que vous pouvez voir ci-dessous :


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

Avec cela, nous pouvons démarrer Klipper pour nous donner accès à nos macros.  
{% finint %}

### Utiliser Moonraker pour être toujours à jour

Grâce à Moonraker nous pouvons utiliser sa mise à jour_manager pour pouvoir rester au courant des améliorations que nous pourrions introduire à l'avenir.

Depuis Mainsail/Fluidd nous éditerons notre moonraker.conf (il doit être à la même hauteur que votre imprimante.cfg) et nous ajouterons à la fin du fichier de configuration :

    [include 3dwork-klipper/moonraker.conf]

{% indice style="avertissement" %}  
**Pensez à faire l'étape d'installation au préalable, sinon Moonraker générera une erreur et ne pourra pas démarrer.**

**En revanche, si le répertoire de votre configuration Klipper est personnalisé, pensez à ajuster le chemin en fonction de votre installation.**  
{% finint %}

## Macro

Nous avons toujours commenté que RatOS est l'une des meilleures distributions Klipper, avec prise en charge des modules Raspberry et CB1, en grande partie grâce à ses configurations modulaires et à ses excellentes macros.

Quelques macros ajoutées qui nous seront utiles :

### **Macros à usage général**

| Macro                                                                          | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PEUT ÊTRE_MAISON**                                                           | Cela nous permet d'optimiser le processus de référencement uniquement en l'exécutant sur les axes qui ne sont pas référencés.                                                        |
| **PAUSE**                                                                      | Grâce aux variables associées, cela nous permet de gérer une pause avec un stationnement de tête plus polyvalent que les macros normales.                                            |
| **ENSEMBLE_PAUSE_À_COUCHE**                                                    |                                                                                                                                                                                      |
| **ENSEMBLE_PAUSE_À_SUIVANT_COUCHE**                                            | Une macro très utile que Mainsail intègre dans son UI pour pouvoir faire une pause à la demande dans un calque spécifique... au cas où nous l'aurions oublié lors du laminage.       |
| Nous en avons également un autre pour exécuter la pause sur le calque suivant. |                                                                                                                                                                                      |
| **CONTINUER**                                                                  | Amélioré car il nous permet de détecter si notre buse n'est pas à la température d'extrusion afin de le résoudre avant qu'elle ne montre une erreur et n'endommage notre impression. |
| **ANNULER_IMPRIMER**                                                           | Ce qui permet d'utiliser le reste des macros pour effectuer correctement une annulation d'impression.                                                                                |

-   **En pause lors du changement de calque**, des macros très intéressantes qui nous permettent de mettre en pause un calque ou de lancer une commande au démarrage du calque suivant.  
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    De plus, un autre avantage est qu'ils sont intégrés à Mainsail, nous aurons donc de nouvelles fonctions dans notre interface utilisateur, comme vous pouvez le voir ci-dessous :  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Macros de gestion d'impression**

| Macro                                                                                              | Description                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **COMMENCER_IMPRIMER**                                                                             | Cela nous permettra de démarrer nos impressions de manière sûre et à la manière de Klipper. Au sein de celui-ci, nous trouverons quelques fonctions intéressantes telles que : |
| -préchauffage intelligent de la buse en cas de présence d'un capteur à sonde                       |                                                                                                                                                                                |
| -possibilité d'utiliser l'inclinaison en z via variable                                            |                                                                                                                                                                                |
| -Matelas de lit adaptatif, forcé ou à partir d'un sac stocké                                       |                                                                                                                                                                                |
| -Ligne de purge personnalisable entre la ligne de purge normale et adaptative ou la chute de purge |                                                                                                                                                                                |
| -macro segmentée pour pouvoir être personnalisée comme nous vous le montrerons plus tard           |                                                                                                                                                                                |
| **FIN_IMPRIMER**                                                                                   | Macro de fin d'impression où nous avons également une segmentation pour pouvoir personnaliser notre macro. Nous disposons également d'un stationnement de tête dynamique.      |

-   **Cadre de lit adaptatif**Grâce à la polyvalence de Klipper, nous pouvons faire des choses qui semblent aujourd'hui impossibles... un processus important pour l'impression est d'avoir un maillage d'écarts par rapport à notre lit qui nous permet de les corriger pour avoir une parfaite adhérence des premières couches.  
    À de nombreuses reprises, nous effectuons ce maillage avant l'impression pour nous assurer qu'il fonctionne correctement et cela se fait sur toute la surface de notre lit.  
    Avec le maillage adaptatif du lit, cela se fera dans la zone d'impression, ce qui le rend beaucoup plus précis que la méthode traditionnelle... dans les captures d'écran suivantes, nous verrons les différences entre un maillage traditionnel et un maillage adaptatif.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Macros de gestion des filaments**

Ensemble de macros qui nous permettront de gérer différentes actions avec notre filament, comme le charger ou le décharger.

| Macro                  | Description                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **M600**               | Cela nous permettra la compatibilité avec le gcode M600 normalement utilisé dans les plastifieuses pour le changement de filament. |
| **DÉCHARGER_FILAMENT** | Configurable à travers les variables, il nous permettra une décharge assistée du filament.                                         |
| **CHARGER_FILAMENT**   | Identique au précédent mais lié à la charge du filament.                                                                           |

### **Macros de gestion des bobines de filament (Spoolman)**

{% indice style="avertissement" %}  
**SECTION EN COURS !!!**  
{% finint %}

[**Spoolman**](https://github.com/Donkie/Spoolman)est un gestionnaire de bobines de filament intégré à Moonraker et qui nous permet de gérer notre stock et notre disponibilité de filament.

!\[](../../.gitbook/assets/image (1990).png)

Nous n'allons pas entrer dans l'installation et la configuration de celui-ci puisque c'est relativement simple grâce au[**instructions de votre Github**](https://github.com/Donkie/Spoolman)**,**dans tous les cas**Nous vous conseillons d'utiliser Docker**pour plus de simplicité et rappelez-vous**activer les paramètres dans Moonraker**requis:

{% code title="moonraker.conf" %}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{%endcode%}

| Macro                 | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| ENSEMBLE_ACTIF_BOBINE | Cela nous permet d'indiquer quel est l'ID de la bobine à utiliser |
| CLAIR_ACTIF_BOBINE    | Cela nous permet de réinitialiser la bobine active                |

L'idéal dans chaque cas serait d'ajouter à notre plastifieuse,**dans les gcodes du filament pour chaque bobine, l'appel à ceci**, Et rappelez-vous**changer son identifiant une fois consommé**pour pouvoir garder une trace de ce qu'il reste de filament dedans !!!

!\[](../../.gitbook/assets/image (1991).png)

### **Macros de gestion des surfaces d'impression**

{% indice style="avertissement" %}  
**SECTION EN COURS !!!**  
{% finint %}

Il est généralement normal que nous ayons des surfaces d'impression différentes en fonction de la finition que nous souhaitons avoir ou du type de filament.

Cet ensemble de macros, créé par[Garethky](https://github.com/garethky), ils nous permettront d'avoir le contrôle de ceux-ci et surtout le réglage correct du ZOffset dans chacun d'eux dans le style que nous avons dans les machines Prusa. Ci-dessous vous pouvez voir certaines de ses fonctions :

-   Nous pouvons stocker le nombre de surfaces d'impression que nous voulons, chacune ayant un nom unique
-   chaque surface d'impression aura son propre ZOffset
-   Si nous effectuons des ajustements Z lors d'une impression (Babystepping) depuis notre Clipper, ce changement sera stocké dans la surface activée à ce moment-là

D'un autre côté, nous avons quelques**exigences pour l'implémenter (nous essaierons d'ajouter dans la logique PRINT_START du bundle dans le futur en activant cette fonction par variable et en créant une macro utilisateur précédente et suivante pour pouvoir saisir les événements utilisateur)**:

-   l'utilisation de\[sauvegarder_variables]Dans notre cas, nous utiliserons ~/variables.cfg pour stocker les variables et cela se trouve déjà dans le cfg de ces macros.  
    Cela créera automatiquement un fichier de variables pour nous_construire_sheet.cfg où il sauvegardera nos variables sur le disque.

{% code title="Exemple de fichier de configuration de variables" %}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{%endcode%}

-   nous devons inclure un appel à postuler_CONSTRUIRE_FEUILLE_AJUSTEMENT dans notre PRINT_START pour pouvoir appliquer le ZOffset de la surface sélectionnée
-   Il est important que pour la macro précédente, APPLIQUER_CONSTRUIRE_FEUILLE_AJUSTEMENT, pour fonctionner correctement il faut ajouter un SET_CODE GCO_OFFSET Z=0.0 juste avant d'appeler APPLY_CONSTRUIRE_FEUILLE_AJUSTEMENT


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

Par contre, il est intéressant de pouvoir avoir des macros pour activer une surface ou une autre ou même la passer en paramètre depuis notre plastifieuse pour qu'avec différents profils d'imprimante ou de filament on puisse charger l'un ou l'autre automatiquement :

{% indice style="avertissement" %}  
Il est important que la valeur dans NAME="xxxx" corresponde au nom que nous avons donné lors de l'installation de notre surface d'impression.  
{% finint %}

{% code title="printer.cfg ou inclure cfg" %}

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

Également dans le cas de KlipperScreen, nous pouvons ajouter un menu spécifique pour gérer le chargement des différentes surfaces, où nous inclurons un appel aux macros précédemment créées pour le chargement de chaque surface :

{% code title="~/imprimante_data/config/KlipperScreen.conf" %}

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

| Macro                                      | Description |
| ------------------------------------------ | ----------- |
| INSTALLER_CONSTRUIRE_FEUILLE               |             |
| MONTRER_CONSTRUIRE_FEUILLE                 |             |
| MONTRER_CONSTRUIRE_FEUILLES                |             |
| ENSEMBLE_CONSTRUIRE_FEUILLE_COMPENSER      |             |
| RÉINITIALISER_CONSTRUIRE_FEUILLE_COMPENSER |             |
| ENSEMBLE_CODE GCO_COMPENSER                |             |
| APPLIQUER_CONSTRUIRE_FEUILLE_AJUSTEMENT    |             |

### **Macros de configuration des machines**

| Macro                                                             | Description                                                                                                                                                                                                                |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILER_MICROLOGICIEL**                                        | Avec cette macro, nous pouvons compiler le firmware Klipper de manière simple, rendre le firmware accessible depuis l'interface utilisateur pour plus de simplicité et pouvoir l'appliquer à notre électronique.           |
| Ici vous avez plus de détails sur l’électronique prise en charge. |                                                                                                                                                                                                                            |
| **CALCULER_LIT_ENGRENER**                                         | Une macro extrêmement utile pour calculer la surface de notre maillage car cela peut parfois être un processus compliqué.                                                                                                  |
| **PID_TOUS**                                                      |                                                                                                                                                                                                                            |
| **PID_EXTRUDEUSE**                                                |                                                                                                                                                                                                                            |
| **PID_LIT**                                                       | Ces macros, où nous pouvons transmettre les températures au PID sous forme de paramètres, nous permettront d'effectuer l'étalonnage de la température de manière extrêmement simple.                                       |
| **TEST_VITESSE**                                                  |                                                                                                                                                                                                                            |
| **TEST_VITESSE_DELTA**                                            | Macro originale du compagnon[Élise](https://github.com/AndrewEllis93)Ils nous permettront de manière assez simple de tester la vitesse à laquelle nous pouvons déplacer notre machine avec précision et sans perte de pas. |

-   **Firmware compilé pour les appareils électroniques pris en charge**, pour faciliter le processus de création et de maintenance de notre firmware Klipper pour nos MCU, nous avons la macro COMPILE_FIRMWARE qui, une fois exécuté, nous pouvons utiliser notre électronique comme paramètre pour faire uniquement cela, compilera Klipper pour toute l'électronique prise en charge par notre bundle :  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Nous les trouverons facilement accessibles depuis notre interface Web dans le répertoire du firmware.\_binaires dans notre onglet MACHINE (si nous utilisons Grand-Voile) :  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Vous trouverez ci-dessous la liste des appareils électroniques pris en charge :

**IMPORTANTE!!!**

Ces scripts sont prêts à fonctionner sur un système Raspbian avec un utilisateur pi, si ce n'est pas votre cas vous devrez l'adapter.

Les firmwares sont générés pour être utilisés avec une connexion USB, ce qui est toujours ce que nous recommandons. De plus, le point de montage USB est toujours le même, donc la configuration de votre connexion MCU ne changera pas s'ils sont générés avec notre macro/script.

**Pour que Klipper puisse exécuter des macros shell, une extension doit être installée, grâce au compagnon**[**arc sinus**](https://github.com/Arksine)**, cela le permet.**

**Selon la distribution Klipper utilisée, ils peuvent déjà être activés.**

![](../../.gitbook/assets/image%20(770).png)

Le plus simple est d'utiliser[**keoh**](../instalacion/#instalando-kiauh)où l'on retrouvera dans une de ses options la possibilité d'installer cette extension :

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Nous pouvons également effectuer le processus à la main, nous copierons manuellement le plugin pour Klipper[**gcode_coquille_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)dans notre annuaire`_**~/klipper/klippy/extras**_`en utilisant SSH ou SCP et redémarrez Klipper.

| Électronique                           | Nom du paramètre à utiliser dans la macro |
| -------------------------------------- | ----------------------------------------- |
| Manta E                                | Avec fierté                               |
| Oubliez M4P                            | btt-manta-m4p                             |
| Manta M4P v2.a                         | btt-manta-m4p-22                          |
| Manta Qab                              | btt-manta-m8p                             |
| Manda MthP b1.1                        | btt-manta-m8p-11                          |
| PAS de poulpe Max                      | btt-octopus-max-it                        |
| Poulpe Pro (446)                       | btt-octopus-pro-446                       |
| Poulpe Pro (429)                       | btt-octopus-pro-429                       |
| Poulpe Pro (H723)                      | btt-octopus-pro-h723                      |
| Poulpe v1.1                            | btt-octopus-11                            |
| Poulpe v1.1 (407)                      | btt-octopus-11-407                        |
| SKR Pro v1.2                           | skr_pro_12                                |
| 3 SKR                                  | btt_skr_3                                 |
| Saqr A (Haha)                          | Tu le saoules                             |
| SKR 3EZ                                | btt-skr-3-ez                              |
| Saqr (que la paix soit sur lui) (Haha) | Elle est très ivre                        |
| 2 SKR (429)                            | btt-skr-2-429                             |
| 2 SKR (407)                            | btt-skr-2-407                             |
| SKR RAT                                | btt-court-circuit-10                      |
| SKR1.4 Turbo                           | btt-skr-14-turbo                          |
| SKR Mini Ez vz                         | btt_skr_mini_ez_30                        |

| Tête d'outil (CAN) | Nom du paramètre à utiliser dans la macro |
| ------------------ | ----------------------------------------- |
| EBB42 v1           | btt_reflux42_10                           |
| EBB36v1            | btt_reflux36_10                           |
| EBB42 v1.1         | btt_reflux42_11                           |
| EBB36 v1.1         | btt_reflux36_11                           |
| EBB42 v1.2         | btt_reflux42_12                           |
| EBB36 v1.2         | btt_reflux36_12                           |

| **Électronique**              | **Nom du paramètre à utiliser dans la macro** |
| ----------------------------- | --------------------------------------------- |
| MKS Aigle v1.x                | mks-aigle-10                                  |
| ISS Robin Nano vz             | mks-robin-nano-30                             |
| MKS Robin Nano v2             | mks-robin-nano-20                             |
| MKS Gen L                     | mks-gen-l                                     |
| Le cours sin nano do de Rubin | zeg_rouge-gorge_nano_dw_Classe                |

| Tête d'outil (CAN) | Nom du paramètre à utiliser dans la macro |
| ------------------ | ----------------------------------------- |
| Mellow FLY SHT42   | moelleux_voler_merde_42                   |
| Mellow FLY SHT36   | moelleux_voler_merde_36                   |

| Électronique    | Nom du paramètre à utiliser dans la macro |
| --------------- | ----------------------------------------- |
| Araignée Fysetc | fysetc_araignée                           |

### Ajout de macros 3Dwork à notre installation

Depuis notre interface, Mainsail/Fluidd, nous allons éditer notre imprimante.cfg et ajouter :

{% code title="imprimante.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{%endcode%}

{% indice style="info" %}  
Il est important d'ajouter ces lignes à la fin de notre fichier de configuration... juste au dessus de la section pour que s'il y a des macros dans notre cfg ou include, elles soient écrasées par les nôtres :  
#\*# \\&lt;------------ SAUVEGARDER_CONFIGURATION ------------>  
{% finint %}

{% indice style="avertissement" %}  
Les macros normales ont été séparées de**shell de macros**car**Pour les activer, il est nécessaire d'effectuer manuellement des étapes supplémentaires, en plus du fait qu'elles sont actuellement en cours de test.**et\*\*Ils peuvent avoir besoin d'autorisations supplémentaires pour attribuer des autorisations d'exécution pour lesquelles les instructions n'ont pas été indiquées puisqu'ils tentent d'automatiser.\*\*  
**Si vous les utilisez, c'est à vos propres risques.**  
{% finint %}

### Configuration de notre plastifieuse

Puisque nos macros sont dynamiques, elles extrairont certaines informations de la configuration de notre imprimante et de la plastifieuse elle-même. Pour ce faire, nous vous conseillons de configurer vos plastifieuses comme suit :

-   **démarrer le gcode DÉBUT_IMPRIMER**, en utilisant des espaces réservés pour transmettre dynamiquement les valeurs de température du filament et du lit :

{% onglets %}  
{% tab title="PrusaSlicer-SuperSlicer" %}  
**Trancheuse Prusa**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**SuperSlicer**- nous avons la possibilité de régler la température de l'enceinte (CHAMBRE)

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{% perte finale %}

{% tab title="Bambu Studio/OrcaSlicer" %}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760).png){% endtab %}

{% tab title="Cura" %}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{% indice style="avertissement" %}  
Il va falloir installer le plugin[**Plugin de post-traitement (par frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)du menu_**Aide/Afficher**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.   
On redémarre Cura et on ira à_**Extensions/Post-traitement/Modifier le G-Code**_et nous sélectionnerons_**Taille d'impression du maillage**_.  
{% finint %}  
{% perte finale %}

{% tab title="IdeaMaker" %}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{% perte finale %}

{% tab title="Simplify3D" %}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{% perte finale %}  
{% de perte finale %}

{% indice style="info" %}  
Les**les espaces réservés sont des "alias" ou des variables que les plastifieurs utilisent pour que lors de la génération du gcode, ils soient remplacés par les valeurs configurées dans le profil**d'impression.

Dans les liens suivants, vous pouvez en trouver une liste pour :[**Trancheuse Prusa**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(en plus de ceux ci-dessus),[**Studio Bambou**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)et[**Traitement**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

L'utilisation de ceux-ci permet à nos macros d'être dynamiques.  
{% finint %}

-   **gcode de final END_IMPRIMER**, dans ce cas, en n'utilisant pas d'espaces réservés, il est commun à toutes les plastifieuses


    END_PRINT

### Variables

Comme nous l'avons déjà mentionné, ces nouvelles macros nous permettront d'avoir des fonctions très utiles comme nous l'avons listé ci-dessus.

Pour les ajuster à notre machine nous utiliserons les variables que nous trouverons dans les macros/macros_était_globals.cfg et que nous détaillons ci-dessous.

#### Langue des messages/notifications

Étant donné que de nombreux utilisateurs aiment recevoir des notifications de macros dans leur langue, nous avons conçu un système de notification multilingue, actuellement en espagnol (es) et en anglais (en). Dans la variable suivante, nous pouvons l'ajuster :

| Variable        | Description                                                                                                          | Valeurs possibles | Valeur par défaut |
| --------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_langue | Il nous permet de sélectionner la langue des notifications. S'il n'est pas bien défini, il sera utilisé en (anglais) | c'est dans        | est               |

#### Extrusion relative

Cela nous permet de contrôler quel mode d'extrusion nous utiliserons à la fin de notre START.\_IMPRIMER La valeur dépendra de la configuration de notre plastifieuse.

{% indice style="succès" %}  
Il est conseillé de configurer votre plastifieuse pour utiliser l'extrusion relative et de définir cette variable sur True.  
{% finint %}

| Variable                   | Description                                                                    | Valeurs possibles | Valeur par défaut |
| -------------------------- | ------------------------------------------------------------------------------ | ----------------- | ----------------- |
| variable_relatif_extrusion | Il nous permet d'indiquer le mode d'extrusion utilisé dans notre plastifieuse. | Vrai faux         | Vrai              |

#### Vitesses

Pour gérer les vitesses utilisées dans les macros.

| Variable                      | Description                       | Valeurs possibles | Valeur par défaut |   |
| ----------------------------- | --------------------------------- | ----------------- | ----------------- | - |
| variable_macro_voyage_vitesse | Vitesse de transfert              | numérique         | 150               |   |
| variable_macro_Avec_vitesse   | Vitesse de transfert pour l'axe Z | numérique         | 15                |   |

#### Retour à destination

Ensemble de variables liées au processus de référencement.

| Variable | Description | Valeurs possibles | Valeur par défaut |
| -------- | ----------- | ----------------- | ----------------- |

#### Chauffage

Variables liées au processus de chauffage de notre machine.

| Variable                                              | Description                                                                                      | Valeurs possibles | Valeur par défaut |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------- | ----------------- |
| variable_Préchauffer_extrudeuse                       | Permet de préchauffer la buse à la température indiquée en variable_Préchauffer_extrudeuse_temp. | Vrai faux         | Vrai              |
| variable_Préchauffer_extrudeuse_temp.                 | Température de préchauffage de la buse                                                           | numérique         | 150               |
| variable_commencer_imprimer_chaleur_chambre_lit_temp. | Température du lit pendant le processus de chauffage de notre enceinte                           | numérique         | 100               |

{% indice style="succès" %}  
Avantages de l'utilisation d'une buse préchauffée :

-   Cela nous laisse du temps supplémentaire pour que le lit puisse atteindre sa température de manière uniforme.
-   Si nous utilisons un capteur inductif sans compensation de température, cela permettra à nos mesures d'être plus cohérentes et précises.
-   Permet de ramollir tout filament restant dans la buse, ce qui signifie que, dans certaines configurations, ces restes n'affectent pas l'activation du capteur.  
    {% finint %}

#### Filet de lit

Pour contrôler le processus de mise à niveau, nous disposons de variables qui peuvent être très utiles. Par exemple, nous pouvons contrôler le type de nivellement que nous souhaitons utiliser en créant toujours un nouveau maillage, en chargeant un maillage précédemment stocké ou en utilisant un maillage adaptatif.

| Variable                                                                                                               | Description                                                                                          | Valeurs possibles | Valeur par défaut |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_étalonner_lit_engrener                                                                                        | Cela nous permet de sélectionner le type de maillage que nous utiliserons dans notre START_IMPRIMER: |                   |                   |
| -nouveau maillage, il maillera chaque impression                                                                       |                                                                                                      |                   |                   |
| -storemesh, chargera un maillage stocké et n'effectuera pas d'interrogation du lit                                     |                                                                                                      |                   |                   |
| -adaptatif, nous fera un nouveau maillage mais adapté à la zone d'impression, améliorant souvent nos premières couches |                                                                                                      |                   |                   |
| -nomesh, au cas où nous n'aurions pas de capteur ou si nous utilisons un maillage pour ignorer le processus            | nouveau maillage / maillage stocké / adaptatif /                                                     |                   |                   |
| des noms                                                                                                               | adaptative                                                                                           |                   |                   |
| variable_lit_engrener_profil                                                                                           | Le nom utilisé pour notre maillage stocké                                                            | texte             | défaut            |

{% indice style="avertissement" %}  
Nous vous conseillons d'utiliser le nivellement adaptatif puisqu'il ajustera toujours le maillage à la taille de notre impression, vous permettant ainsi d'avoir une zone de maillage ajustée.

Il est important que nous ayons dans notre[démarrer le gcode de notre plastifieuse](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), dans l'appel à notre START_IMPRIMER, IMPRIMER les valeurs_MAX et IMPRIMER_MIN.  
{% finint %}

#### purgé

Une phase importante de notre démarrage d'impression est une purge correcte de notre buse pour éviter les restes de filaments ou que ceux-ci pourraient endommager notre impression à un moment donné. Ci-dessous vous avez les variables qui interviennent dans ce processus :

| Variable                                                                                                                                                           | Description                                               | Valeurs possibles | Valeur par défaut |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- | ----------------- | ----------------- |
| variable_buse_amorçage                                                                                                                                             | Nous pouvons choisir entre différentes options de purge : |                   |                   |
| -primeline va tracer la ligne de purge typique                                                                                                                     |                                                           |                   |                   |
| -primelineadaptative générera une ligne de purge qui s'adapte à la zone de la pièce imprimée à l'aide d'une variable_buse_amorçage_distance de l'objet comme marge |                                                           |                   |                   |
| -primeblob nous fera une goutte de filament dans un coin de notre lit, très efficace pour nettoyer la buse et facile à retirer                                     |                                                           |                   |                   |
| ligne principale /                                                                                                                                                 |                                                           |                   |                   |

primelineadaptatif /  
goutte principale /  
FAUX

| ligne principale adaptative |  
| variable_buse_amorçage_distance de l'objet | Si nous utilisons une ligne de fond perdu adaptative, ce sera la marge à utiliser entre la ligne de fond perdu et l'objet imprimé | numérique | 5 |  
| variable_buse_prime_commencer_X | Où nous voulons localiser notre ligne de purge :  
-min le fera à X=0 (plus une petite marge de sécurité)  
-max le fera à X=max (moins une petite marge de sécurité)  
-numéro sera la coordonnée X où localiser la purge | minutes /  
maximum /  
numéro | maximum |  
| variable_buse_prime_commencer_et | Où nous voulons localiser notre ligne de purge :  
-min le fera à Y=0 (plus une petite marge de sécurité)  
-max le fera à Y=max (moins une petite marge de sécurité)  
-numéro sera la coordonnée Y où localiser la purge | minutes /  
maximum /  
numéro | min |  
| variable_buse_prime_direction | L'adresse de notre ligne ou de notre dépôt :  
-vers l'arrière, la tête se déplacera vers l'avant de l'imprimante  
-les avants se déplaceront vers l'arrière  
-la voiture ira vers le centre en fonction de la variable_buse_prime_commencer_et | voiture /  
en avant /  
en arrière | automobile |

#### Chargement/déchargement de filaments

Dans ce cas, ce groupe de variables facilitera la gestion du chargement et du déchargement de notre filament utilisé en émulation du M600 par exemple, ou lors du lancement des macros de chargement et déchargement du filament :

| Variable                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        | Valeurs possibles | Valeur par défaut |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_filament_décharger_longueur | De combien rétracter le filament en mm, ajustez à votre machine, normalement la mesure de votre buse aux engrenages de votre extrudeuse en ajoutant une marge supplémentaire.                                                                                                                                                                                                                                                                      | nombre            | 130               |
| variable_filament_décharger_vitesse  | Vitesse de rétraction du filament en mm/sec, normalement une vitesse lente est utilisée.                                                                                                                                                                                                                                                                                                                                                           | nombre            | 5                 |
| variable_filament_charger_longueur   | Distance en mm pour charger le nouveau filament... ainsi qu'en variable_filament_décharger_longueur, nous utiliserons la mesure de votre équipement à l'extrudeuse en ajoutant une marge supplémentaire, dans ce cas cette valeur supplémentaire dépendra de la quantité que vous souhaitez purger... normalement vous pouvez lui donner plus de marge que la valeur précédente pour garantir que la l'extrusion du filament précédent est propre. | nombre            | 150               |
| variable_filament_charger_vitesse    | Vitesse de chargement du filament en mm/sec, normalement une vitesse plus rapide est utilisée que la vitesse de déchargement.                                                                                                                                                                                                                                                                                                                      | nombre            | 10                |

{% indice style="avertissement" %}  
Un autre paramètre nécessaire pour votre section\[extrudeuse]se indique el[**maximum_extruder_seulement_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)...la valeur recommandée est généralement >101 (si elle n'est pas définie, utilisez 50) pour, par exemple, permettre des tests d'étalonnage typiques d'une extrudeuse.  
Vous devez ajuster la valeur en fonction de ce qui a été mentionné précédemment concernant le test ou la configuration de votre**variable_filament_décharger_longueur**je**variable_filament_charger_longueur**.  
{% finint %}

#### Parking

Dans certains processus de notre imprimante, comme en pause, il est conseillé de garer la tête. Les macros de notre bundle ont cette option en plus des variables suivantes à gérer :

| Variable                                      | Description                                                                                                                                                                                                                                                                                                               | Valeurs possibles | Valeur par défaut |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_commencer_imprimer_parc_dans         | Emplacement où garer la tête pendant le préchauffage.                                                                                                                                                                                                                                                                     | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_commencer_imprimer_parc_Avec_hauteur | Hauteur Z pendant le préchauffage                                                                                                                                                                                                                                                                                         | nombre            | 50                |
| variable_fin_imprimer_parc_dans               | Emplacement où garer la tête lors de la fin ou de l’annulation d’une impression.                                                                                                                                                                                                                                          | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_fin_imprimer_parc_Avec_houblon       | Distance à monter en Z en fin d'impression.                                                                                                                                                                                                                                                                               | nombre            | 20                |
| variable_pause_imprimer_parc_dans             | Emplacement où garer la tête lors d’une pause d’impression.                                                                                                                                                                                                                                                               | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_pause_inactif_temps mort             | Valeur, en secondes, de l'activation du processus d'inactivité de la machine qui libère les moteurs et provoque la perte des coordonnées,**Une valeur élevée est conseillée afin que lors de l'activation de la macro PAUSE, il faille suffisamment de temps pour effectuer une action avant de perdre les coordonnées.** | nombre            | 43200             |

#### Inclinaison en Z

Tirer le meilleur parti de notre machine pour qu'elle s'auto-nivelle et veiller à ce que notre machine soit toujours dans les meilleures conditions est essentiel.

**Z-TILT est essentiellement un processus qui nous aide à aligner nos moteurs Z par rapport à notre axe/portique X (Cartésien) ou XY (CoreXY).**. Avec ça**nous veillons à ce que notre Z soit toujours parfaitement aligné, précisément et automatiquement**.

| Variable                            | Description                                                                        | Valeurs possibles | Valeur par défaut |
| ----------------------------------- | ---------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_étalonner_Avec_inclinaison | Permet, si activé dans notre configuration Klipper, le processus de réglage Z-Tilt | Vrai faux         | FAUX              |

#### Fausser

L'utilisation de[FAUSSER](broken-reference)Pour la correction ou l'ajustement précis de nos imprimantes, il est extrêmement conseillé si nous avons des écarts dans nos impressions. En utilisant la variable suivante, nous pouvons autoriser l'utilisation dans nos macros :

| Variable                | Description                                                                                                                                                                                                                      | Valeurs possibles | Valeur par défaut  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------ |
| variable_fausser_profil | Cela nous permet de prendre en compte notre profil de biais qui sera chargé dans notre macro START_IMPRIMER Pour l'activer, nous devons décommenter la variable et utiliser le nom du profil asymétrique de notre configuration. | texte             | mon_fausser_profil |

### Personnalisation des macros

Notre module pour Klipper utilise le système de configuration modulaire utilisé dans RatOS et profite des avantages de Klipper dans le traitement séquentiel de ses fichiers de configuration. C'est pourquoi l'ordre des inclusions et des paramètres personnalisés que l'on souhaite appliquer à ces modules est essentiel.

{% indice style="info" %}  
Lorsqu'elles sont utilisées en tant que module, les configurations 3Dwork NE PEUVENT PAS être modifiées directement à partir du répertoire 3dwork-klipper dans votre répertoire de configuration Klipper car elles seront en lecture seule pour des raisons de sécurité.

C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules pour votre machine.  
{% finint %}

#### **Personnalisation des variables**

Normalement, ce sera ce que nous devrons ajuster, faire des ajustements aux variables que nous avons par défaut dans notre module**Vos excuses**para Falaises.

Simplement, il suffit de coller le contenu de la macro\[gcode_macroGLOBALE_DONT]ce qu'on peut trouver dans les macros/macros_était_globals.cfg dans notre imprimante.cfg.

Nous vous rappelons ce que nous avons mentionné précédemment sur la façon dont Klipper traite les configurations de manière séquentielle, il est donc conseillé de le coller après les inclusions que nous avons mentionnées.[ici](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nous aurons quelque chose comme ceci (c'est juste un exemple visuel) :

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

{% indice style="avertissement" %}
Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.
{% indice de fin %}

{% indice style="info" %}

-   Nous vous conseillons d'ajouter des commentaires comme vous le voyez dans le cas précédent pour identifier ce que fait chaque section.
-   Bien qu'il ne soit pas nécessaire de toucher à toutes les variables, nous vous conseillons de copier tout le contenu de\[gcode_macroGLOBALE_DONT]{% finint %}

#### Personnalisation des macros

Les macros ont été configurées de manière modulaire afin de pouvoir être facilement ajustées. Comme nous l'avons mentionné précédemment, si nous voulons les ajuster, nous devrons procéder de la même manière que pour les variables, copier la macro en question dans notre imprimante.cfg (ou une autre inclusion de notre choix) et nous assurer qu'elle est après l'inclusion où nous avons ajouté notre module 3Dwork pour Klipper.

Nous avons deux groupes de macros :

-   Macros pour ajouter des paramètres utilisateur, ces macros peuvent être facilement ajoutées et personnalisées car elles ont été ajoutées afin que tout utilisateur puisse personnaliser les actions à sa guise dans certaines parties des processus effectués par chaque macro.

**COMMENCER_IMPRIMER**

| Nombre Macro                                                | Description                                                                                                                         |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| \_UTILISATEUR_COMMENCER_IMPRIMER_CHALEUR_CHAMBRE            | Elle est exécutée juste après que notre enceinte commence à chauffer, si CHAMBRE_TEMP est passé en paramètre à notre START_IMPRIMER |
| \_UTILISATEUR_COMMENCER_IMPRIMER_AVANT_RENDEZ-VOUS          | Exécuté avant la prise d'origine initiale du début de l'impression                                                                  |
| \_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT        | Elle est exécutée lorsque notre lit atteint sa température, avant_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT                            |
| \_UTILISATEUR_COMMENCER_IMPRIMER_LIT_ENGRENER               | Il est publié avant_COMMENCER_IMPRIMER_LIT_ENGRENER                                                                                 |
| \_UTILISATEUR_COMMENCER_IMPRIMER_PARC                       | Il est publié avant_COMMENCER_IMPRIMER_PARC                                                                                         |
| \_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_EXTRUDEUSE | Il est publié avant_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_EXTRUDEUSE                                                                   |

**FIN_IMPRIMER**

| Nombre Macro                                          | Description                                                                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| \_UTILISATEUR_FIN_IMPRIMER_AVANT_CHAUFFAGES_DÉSACTIVÉ | Il est exécuté avant d'éteindre les radiateurs, avant_FIN_IMPRIMER_AVANT_CHAUFFAGES_DÉSACTIVÉ |
| \_UTILISATEUR_FIN_IMPRIMER_APRÈS_CHAUFFAGES_DÉSACTIVÉ | Il est exécuté après l'arrêt des radiateurs, avant_FIN_IMPRIMER_APRÈS_CHAUFFAGES_DÉSACTIVÉ    |
| \_UTILISATEUR_FIN_IMPRIMER_PARC                       | Il est exécuté avant que la tête ne soit garée, avant_FIN_IMPRIMER_PARC                       |

**IMPRIMER_LES BASES**

| Nombre Macro                      | Description                  |
| --------------------------------- | ---------------------------- |
| \_UTILISATEUR_PAUSE_COMMENCER     | Exécuté au début d'une PAUSE |
| \_UTILISATEUR_PAUSE_FIN           | Exécuté à la fin d'une PAUSE |
| \_UTILISATEUR_CONTINUER_COMMENCER | Exécuté au début d'un RESUME |
| \_UTILISATEUR_CONTINUER_FIN       | Exécuté à la fin d'un CV     |

-   Les macros internes sont des macros permettant de diviser la macro principale en processus et sont importantes pour cela. Il est conseillé que si des ajustements sont nécessaires, ils soient copiés tels quels.

**COMMENCER_IMPRIMER**

| Nombre Macro                                    | Description                                                                                                                                                                                                                        |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_COMMENCER_IMPRIMER_CHALEUR_CHAMBRE            | Chauffe l'enceinte dans le cas où le paramètre CHAMBRE_TEMP est reçu par notre macro START_IMPRIMER depuis la plastifieuse                                                                                                         |
| \_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT        | Il est exécuté lorsque le lit atteint la température, après_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT. Généralement utilisé pour traiter les étalonnages de lit (Z_INCLINAISON_AJUSTEMENT, QUAD_PORTIQUE_NIVELLEMENT,...) |
| \_COMMENCER_IMPRIMER_LIT_ENGRENER               | Il gère la logique de maillage du lit.                                                                                                                                                                                             |
| \_COMMENCER_IMPRIMER_PARC                       | Garez la tête d'impression tout en chauffant la buse à la température d'impression.                                                                                                                                                |
| \_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_EXTRUDEUSE | Purger la buse et charger le profil SKEW si celui-ci est défini dans les variables                                                                                                                                                 |

## Imprimantes et électronique

Comme nous travaillons avec différents modèles d'imprimantes et d'électronique, nous ajouterons ceux qui ne sont pas directement supportés par RatOS, qu'il s'agisse de contributions de notre part ou de la communauté.

-   imprimantes, dans ce répertoire nous aurons toutes les configurations d'imprimantes
-   cartes, nous trouverons ici les cartes électroniques

### Paramètres et broches

Notre module pour Klipper utilise le système de configuration modulaire utilisé dans RatOS et profite des avantages de Klipper dans le traitement séquentiel de ses fichiers de configuration. C'est pourquoi l'ordre des inclusions et des paramètres personnalisés que l'on souhaite appliquer à ces modules est essentiel.

{% indice style="info" %}
Lorsqu'elles sont utilisées en tant que module, les configurations 3Dwork NE PEUVENT PAS être modifiées directement à partir du répertoire 3dwork-klipper dans votre répertoire de configuration Klipper car elles seront en lecture seule pour des raisons de sécurité.

C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules pour votre machine.
{% indice de fin %}

Comme nous l'avons expliqué dans "[personnalisation des macros](3dwork-klipper-bundle.md#personalizando-macros)"Nous utiliserons le même processus pour ajuster les paramètres ou les broches en fonction de nos besoins.

#### Paramètres de personnalisation

Tout comme nous vous conseillons de créer une section dans votre imprimante.cfg appelée USER OVERRIDES, placée après les inclusions de nos configurations, pour pouvoir ajuster et personnaliser n'importe quel paramètre utilisé dans celles-ci.

Dans l'exemple suivant, nous verrons comment dans notre cas nous souhaitons personnaliser les paramètres de notre nivellement de lit (lit_mesh) en ajustant les points de sonde_count) par rapport à la configuration que nous avons par défaut dans les configurations de notre module Klipper :

{% code title="imprimante.cfg" %}

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

{% indice style="avertissement" %}
Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.
{% indice de fin %}

Nous pouvons utiliser ce même processus avec n’importe quel paramètre que nous souhaitons ajuster.

#### Personnalisation de la configuration des broches

Nous procéderons exactement comme nous l'avons fait précédemment, dans notre zone USER OVERRIDES, nous ajouterons les sections de broches que nous souhaitons ajuster à notre guise.

Dans l'exemple suivant, nous allons personnaliser quelle est la broche de notre ventilateur électronique (contrôleur_ventilateur) pour l'attribuer à un autre que celui par défaut :

{% code title="imprimante.cfg" %}

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

{% indice style="avertissement" %}
Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.
{% indice de fin %}

```

```
