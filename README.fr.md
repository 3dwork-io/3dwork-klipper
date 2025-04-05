* * *

## Description: package de macros, configurations et autres utilitaires pour Klipper

# Bundle de clôtures en 3D

[<img width="171" alt="kofi" src="https://github.com/3dwork-io/3dwork-klipper/blob/master/Ko-fi-Logo.png">](https://ko-fi.com/jjr3d)

[![](../../.gitbook/assets/image%20(1986).png)- Anglais](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{% hint style = "danger"%}  
**Guide en processus !!! Bien que les macros soient totalement fonctionnelles, elles sont en développement continu.**

**Utilisez-les sous votre propre responsabilité !!!**  
{% de endthint%}

Changelog

12/07/2023 - Ajout d'un support pour automatiser la création du firmware électronique BigRetEech

Depuis**Travail 3D**Nous avons compilé et ajusté un ensemble de macros, de configurations machine et électronique, ainsi que d'autres outils pour une gestion simple et puissante de Klipper.

Une grande partie de ce package est basé sur[**Rats**](https://os.ratrig.com/)Améliorer les parties que nous croyons intéressantes, ainsi que d'autres contributions de la communauté.

## Installation

Pour installer notre package pour Klipper, nous suivrons les étapes suivantes

### Décharge du référentiel

Nous nous connecterons à notre hôte par SSH et lancerons les commandes suivantes:

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{% hint style = "avertissement"%}  
Dans le cas où le répertoire de votre configuration Klipper est personnalisé, n'oubliez pas d'ajuster correctement la première commande à votre installation.  
{% de endthint%}

{% hint style = "info"%}  
Dans les nouvelles installations:

Étant donné que Klipper n'autorise pas l'accès aux macros avant d'avoir une imprimante correcte.cfg et se connecte avec un MCU, nous pouvons "tromper" Klipper avec les étapes suivantes qui nous permettront d'utiliser les macros de notre pack pour, par exemple, lancer la macro de compilation de firmware Klipper si nous utilisons un électronique compatble:

-   Nous nous assurons que nous avons notre[hôte comme deuxième MCU](raspberry-como-segunda-mcu.md)
-   Ensuite, nous ajouterons une imprimante.cfg, n'oubliez pas que ces étapes sont pour une installation propre où vous n'avez pas d'imprimante.cfg et que vous souhaitez lancer la macro pour créer un micrologiciel, comme celui que vous pouvez voir ci-dessous:


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

Avec cela, nous pouvons commencer Klipper pour accéder à nos macros.  
{% de endthint%}

### Utiliser Moonraker pour toujours être mis à jour

Grâce à Moonraker, nous pouvons utiliser sa mise à jour_Gestionnaire pour pouvoir être à jour avec les améliorations que nous pouvons introduire à l'avenir.

Depuis MoilSail / FLUIDD, nous modifierons notre Moonraker.conf (il devrait être à la même hauteur que votre imprimante.cfg) et nous ajouterons à la fin du fichier de configuration:

    [include 3dwork-klipper/moonraker.conf]

{% hint style = "avertissement"%}  
**N'oubliez pas de passer l'étape d'installation précédemment si vous ne générez pas d'erreur et que vous ne pourrez pas démarrer.**

**D'un autre côté, dans le cas où le répertoire de configuration de Klipper est personnalisé, n'oubliez pas d'ajuster correctement le chemin à votre installation.**  
{% de endthint%}

## Macros

Nous avons toujours commenté que Times est l'une des meilleures distributions de Klipper, avec le support de framboise et les modules CB1, en grande partie en raison de ses configurations modulaires et de ses grandes macros.

Certaines macros ajoutées qui seront utiles:

### **Macros pour une utilisation générale**

| Macro                                                                                 | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PEUT ÊTRE_MAISON**                                                                  | Il nous permet d'optimiser le processus de homing qu'en faisant cela dans les axes qui ne sont pas avec le homing.                                                                                                 |
| **PAUSE**                                                                             | Grâce à des variables connexes, il nous permet de gérer une pause avec un parking de tête plus polyvalent que les macros normales.                                                                                 |
| **ENSEMBLE_PAUSE_À_COUCHE**                                                           |                                                                                                                                                                                                                    |
| **ENSEMBLE_PAUSE_À_SUIVANT_COUCHE**                                                   | Une macro très utile qui intègre la main-d'œuvre dans son interface utilisateur pour pouvoir s'arrêter à la demande dans une couche spécifique ... au cas où nous aurions oublié lors de l'exécution du stratifié. |
| Nous en avons également un autre pour exécuter le tranquille dans la couche suivante. |                                                                                                                                                                                                                    |
| **CONTINUER**                                                                         | Améliorée car elle permet de détecter si notre buse n'est pas à la température d'extrusion pour pouvoir la résoudre avant qu'elle ne montre une erreur et endommage notre impression.                              |
| **ANNULER_IMPRIMER**                                                                  | Qui permet à l'utilisation du reste des macros de réaliser correctement une annulation d'impression.                                                                                                               |

-   **Une pause à la place**, des macros très intéressantes qui nous permettent de faire un programme tranquille dans une couche ou de lancer une commande lors du démarrage de la couche suivante.   
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    De plus, un autre avantage de leur part est qu'ils sont intégrés à MoilSail avec ce que nous aurons de nouvelles fonctions dans notre interface utilisateur comme vous pouvez le voir ci-dessous:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Macros de gestion de l'impression**

| Macro                                                                                                | Description                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMMENCER_IMPRIMER**                                                                               | Cela nous permettra de commencer nos impressions d'une manière sûre et dans le style Klipper. En cela, nous trouverons des fonctions intéressantes telles que: |
| -préchauffé de buse intelligente dans le cas d'avoir un capteur de sonde                             |                                                                                                                                                                |
| -Possibilité d'utilisation de z-tilt par variable                                                    |                                                                                                                                                                |
| -Adaptatif, forcé ou d'un maillage stocké moussé                                                     |                                                                                                                                                                |
| -ligne de purge personnalisable entre une ligne de purge ou une chute de purge normale et adaptative |                                                                                                                                                                |
| -macro segmenté pour pouvoir personnaliser comme nous vous le montrerons plus tard                   |                                                                                                                                                                |
| **FIN_IMPRIMER**                                                                                     | Macro de fin d'impression où nous avons également une segmentation pour personnaliser notre macro. Nous avons également la tête dynamique de la tête.          |

-   **Rouleau de lit adaptatif**, grâce à la polyvalence de Klipper, nous pouvons faire des choses qui semblent aujourd'hui impossibles ... Un processus important d'impression est d'avoir un repas de déviations par rapport à notre lit qui nous permet de les corriger pour avoir une adhésion des premières couches parfaites.   
    À plusieurs reprises, nous faisons ce malley avant les impressions pour nous assurer qu'il fonctionne correctement et cela se fait dans toute la surface de notre lit.  
    Avec la misère de lit adaptatif, il sera effectué dans la zone d'impression, ce qui le rend beaucoup plus précis que la méthode traditionnelle ... dans les captures suivantes, nous verrons les différences d'un maillage traditionnel et adaptatif.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Macros de gestion des filaments**

Ensemble de macros qui nous permettra de gérer différentes actions avec notre filament tel que la charge ou la décharge de cela.

| Macro                  | Description                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **M600**               | Il nous permettra de compatibilité avec le M600 GCODE normalement utilisé dans les laminateurs pour le changement de filament. |
| **DÉCHARGER_FILAMENT** | Configurable via les variables nous permettra de télécharger des filaments assistés.                                           |
| **CHARGER_FILAMENT**   | Ainsi que le précédent mais lié à la charge du filament.                                                                       |

### **Filament Coil Management Macros (Spoolman)**

{% hint style = "avertissement"%}  
**Section en cours !!!**  
{% de endthint%}

[**Bobine**](https://github.com/Donkie/Spoolman)Il est un gestionnaire de bobines de filament qui est intégré à Moonraker et qui nous permet de gérer notre stock et notre disponibilité de filaments.

!\[](../../.gitbook/assets/image (1990) .png)

Nous n'allons pas entrer dans l'installation et la configuration de cela car il est relativement simple en utilisant le[**Instructions de votre github**](https://github.com/Donkie/Spoolman)**,**Dans tous les cas**Nous vous conseillons d'utiliser Docker**Par simplicité et souvenir**activer la configuration dans Moonraker**requis:

{% code title = "moonraker.conf"%}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{% Endcode%}

| Macro                 | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| ENSEMBLE_ACTIF_BOBINE | Il nous permet d'indiquer quel est l'ID de la bobine à utiliser |
| CLAIR_ACTIF_BOBINE    | Nous permet de réinitialiser la bobine active                   |

L'idéal dans chaque cas serait d'ajouter notre laminateur,**Dans le filament gcodes pour chaque enroulement l'appel à ce**, et rappelez-vous**Changez l'ID de celle-ci une fois consommé**Pour pouvoir contrôler le reste de Filament dedans !!!

!\[](../../.gitbook/assets/image (1991) .png)

### **Macros de gestion de surface d'impression**

{% hint style = "avertissement"%}  
**Section en cours !!!**  
{% de endthint%}

Il est généralement normal que nous ayons différentes surfaces d'impression en fonction de la finition que nous voulons avoir ou du type de filament.

Cet ensemble de macros, créé par[Garethky](https://github.com/garethky), ils nous permettront d'avoir un contrôle de ceux-ci et surtout le bon ajustement de Zoffset dans chacun d'eux dans le style que nous avons dans les machines Prussa. Ci-dessous, vous pouvez voir certaines de vos fonctions:

-   Nous pouvons stocker le nombre de surfaces d'impression que nous voulons, chacune ayant un nom unique
-   Chaque surface d'impression aura son propre zoffset
-   Si nous faisons des paramètres z pendant une impression (babystepping) de notre Klipper, ce changement va à l'entrepôt à la surface activé à ce moment-là

D'un autre côté, nous en avons**Exigences pour l'implémenter (essayez d'ajouter la logique de l'impression_Début du bundle dans le futur activant cette fonction par variable et créant une macro utilisateur précédente et postérieure pour mettre des événements utilisateur)**:

-   L'utilisation de\[sauvegarder_variables], dans notre cas, nous utiliserons ~ / variables.cfg pour stocker les variables et qui est déjà dans le CFG de ces macros.   
    Cela créera automatiquement un fichier variable_construire_Sheets.cfg où vous garderez nos variables de disque.

{% code title = "Exemple de variables Fichier de configuration"%}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{% Endcode%}

-   Nous devons inclure un appel applicable_CONSTRUIRE_FEUILLE_Ajustement dans notre impression_Commencez à pouvoir appliquer la surface sélectionnée Zoffset
-   Il est important que pour la macro antérieure, appliquez_CONSTRUIRE_FEUILLE_Ajustement, travailler correctement, nous devons ajouter un ensemble_Gcode_Décalage z = 0,0 juste avant l'appel s'appliquer_CONSTRUIRE_FEUILLE_AJUSTEMENT


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

D'un autre côté, il est intéressant de pouvoir avoir des macros pour activer une surface ou une autre ou même la passer comme paramètre de notre laminateur à différents profils d'imprimante ou de filament pour pouvoir charger l'une ou l'autre automatiquement:

{% hint style = "avertissement"%}  
Il est important que la valeur dans nom = "xxxx" coïncide avec le nom que nous avons donné lors de l'installation de notre surface d'impression  
{% de endthint%}

{% code title = "imprimante.cfg ou inclure CFG"%}

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

{% Endcode%}

Également dans le cas d'avoir Klipperscreen, nous pouvons ajouter un menu spécifique pour pouvoir gérer la charge des différentes surfaces, où nous inclurons un appel aux macros précédemment créés pour le chargement de chaque surface:

{% Code Title = "~ / Imprimante_data / config / klipperscreen.conf "%}

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

{% Endcode%}

| Macro                                      | Description |
| ------------------------------------------ | ----------- |
| INSTALLER_CONSTRUIRE_FEUILLE               |             |
| MONTRER_CONSTRUIRE_FEUILLE                 |             |
| MONTRER_CONSTRUIRE_FEUILLES                |             |
| ENSEMBLE_CONSTRUIRE_FEUILLE_COMPENSER      |             |
| RÉINITIALISER_CONSTRUIRE_FEUILLE_COMPENSER |             |
| ENSEMBLE_Gcode_COMPENSER                   |             |
| APPLIQUER_CONSTRUIRE_FEUILLE_AJUSTEMENT    |             |

### **Macros de machine**

| Macro                                                          | Description                                                                                                                                                                                                                            |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILER_Firmware**                                          | Avec cette macro, nous pouvons compiler le firmware Klipper de manière simple, avoir le firmware accessible à partir de l'interface utilisateur pour une plus grande simplicité et être en mesure de l'appliquer à notre électronique. |
| Ici, vous avez plus de détails sur les supports électroniques. |                                                                                                                                                                                                                                        |
| **CALCULER_LIT_ENGRENER**                                      | Une macro extrêmement utile pour calculer la zone pour notre maillage, car parfois elle peut être un processus compliqué.                                                                                                              |
| **Piquer_TOUS**                                                |                                                                                                                                                                                                                                        |
| **Piquer_Extrudeuse**                                          |                                                                                                                                                                                                                                        |
| **Piquer_LIT**                                                 | Ces macros, où nous pouvons passer les températures du PID sous forme de paramètres, nous permettront de pouvoir effectuer l'étalonnage de la température d'une manière extrêmement simple.                                            |
| **TEST_VITESSE**                                               |                                                                                                                                                                                                                                        |
| **TEST_VITESSE_DELTA**                                         | Macro d'origine du partenaire[Ellis](https://github.com/AndrewEllis93)Ils nous permettront de manière assez simple de tester la vitesse à laquelle nous pouvons déplacer notre machine de manière précise et sans perte d'étapes.      |

-   **Compilation de micrologiciel pour l'électronique prise en charge**, Pour faciliter le processus de création et de maintenance de notre firmware Klipper pour notre MCU, nous avons la macro compilation_Firmware que lors de l'exécution, nous pouvons utiliser notre électronique comme paramètre pour ne faire que cela, Klipper se compilera pour tous les électroniques pris en charge par notre bundle:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Nous les trouverons facilement accessibles à partir de notre site Web d'interface utilisateur dans le répertoire du micrologiciel_Binaires dans notre onglet Machine (si nous utilisons Maysail):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Ensuite, vous avez la liste des électroniques pris en charge:

**IMPORTANTE!!!**

Ces scripts sont prêts à travailler sur un système Raspbian avec l'utilisateur PI, si ce n'est pas votre cas, vous devez l'adapter.

Firmwares est généré pour une utilisation avec une connexion USB qui est toujours ce que nous conseillons, en outre, le point d'assemblage USB est toujours le même par ce que votre configuration de votre connexion MCU ne changera pas si elles sont générées avec notre macro / script

**Pour que Klipper puisse exécuter des macros de coquille, une extension doit être installée, grâce au partenaire**[**Arksine**](https://github.com/Arksine)**, laissez-le.**

**Selon Klipper Dystro utilisé, ils peuvent déjà être activés.**

![](../../.gitbook/assets/image%20(770).png)

Le moyen le plus simple consiste à utiliser[**Kioh**](../instalacion/#instalando-kiauh)Où nous trouverons dans l'une de vos options, la possibilité d'installer cette extension:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Nous pouvons également effectuer le processus à la main, nous copierons manuellement le plugin pour Klipper[**Gcode_coquille_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)Dans notre répertoire`_**~/klipper/klippy/extras**_`SECONDO SSHO SCP RESTrace Cleeper.

| Électronique       | Nom du paramètre à utiliser en macro |
| ------------------ | ------------------------------------ |
| Manta              | Je suis fier                         |
| Faire m4p          | btt-manta-m4p                        |
| Manta M4P V2.      | btt-manta-m4p-22                     |
| Faire m8p          | btt-manta-m8p                        |
| Marquer M8P v1.1   | btt-manta-m8p-11                     |
| Octopus max ceci   | btt-octopus-max-ez                   |
| Octopus Pro (446)  | btt-octopus-pro-446                  |
| Octopus Pro (429)  | btt-octopus-pro-429                  |
| Octopus Pro (H723) | btt-octopus-pro-h723                 |
| Octopus v1.1       | btt-octopus-11                       |
| Octopus v1.1 (407) | BTT-Octopus-11-407                   |
| Skr pro v1.2       | skr_pro_12                           |
| Skr 3              | btt_skr_3                            |
| Saqr a (heha)      | Enraciné                             |
| Skr 3 ceci         | BTT-SC-3-EZ                          |
| Skr 3 ceci (H723)  | Skirzhahah                           |
| SKR 2 (429)        | BTT-SRC-2-429                        |
| SKR 2 (407)        | BTT-SRC-2-407                        |
| Cris               | BTT-SKRAT-10                         |
| Par 1,4 turbo      | BTT-SC-14-TURBO                      |
| Skri mini          | btt_skr_mini_EZ_30                   |

| Toolhead (CAN) | Nom du paramètre à utiliser en macro |
| -------------- | ------------------------------------ |
| Ebb42 V1       | btt_Ebb42_10                         |
| Ebb36 v1       | btt_Ebb36_10                         |
| Ebb42 v1.1     | btt_Ebb42_11                         |
| Ebb36 v1.1     | btt_Ebb36_11                         |
| Ebb42 v1.2     | btt_Ebb42_12                         |
| Ebb36 v1.2     | btt_Ebb36_12                         |

| **Électronique**                | **Nom du paramètre à utiliser en macro** |
| ------------------------------- | ---------------------------------------- |
| Mks eagle v1.x                  | MKS-EAGLE-10                             |
| MCS Robin nano cuit             | MKS-ROBIN-NANO-30                        |
| Mks Robin Nano V2               | MKS-ROBIN-NANO-20                        |
| MKS Gen L                       | mks-gen-l                                |
| La culpabilité de Robin Nano du | Znp_roupler_nano_dwing_Catégorie         |

| Toolhead (CAN)      | Nom du paramètre à utiliser en macro |
| ------------------- | ------------------------------------ |
| Mouche douce sht 42 | moelleux_voler_témoin_42             |
| Mouche douce sht 36 | moelleux_voler_témoin_36             |

| Électronique    | Nom du paramètre à utiliser en macro |
| --------------- | ------------------------------------ |
| Araignée Fysetc | fysetc_araignée                      |

### Ajout de macros de travail 3D à notre installation

À partir de notre interface, Mainsail / Fluidd, nous modifierons notre imprimante.cfg et ajouterons:

{% code title = "imprimante.cfg"%}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{% Endcode%}

{% hint style = "info"%}  
Il est important que nous ajoutions ces lignes à la fin de notre fichier de configuration ... juste au-dessus de la section afin que dans le cas des macros dans notre CFG ou incluent ceux-ci sont submergés par le nôtre:  
#\*# \\ &lt;---------------------- Save_Config ---------------------->  
{% de endthint%}

{% hint style = "avertissement"%}  
Les macros normales ont été séparés de**coquille de macros**étant donné que**Pour les activer, il est nécessaire de faire des étapes manuelles en plus qui testent actuellement**et\*\*Ils peuvent nécessiter des autorisations supplémentaires pour attribuer des autorisations d'exécution pour lesquelles les instructions n'ont pas été indiquées car elle essaie d'automatiser.\*\*  
**Si vous les utilisez, c'est sous votre propre responsabilité.**  
{% de endthint%}

### Paramètres de notre laminateur

Étant donné que nos macros sont dynamiques, ils extraire certaines informations de notre configuration d'imprimante et du laminateur lui-même. Pour ce faire, nous vous conseillons de configurer vos laminateurs comme suit:

-   **Démarrer Démarrer Gcode_IMPRIMER**, en utilisant des espaces réservés pour passer le filament et les valeurs de température du lit dynamiquement:

{% Tabs%}  
{% tab title = "Prusasliner-SuperSLICER"%}  
**Prusasliseur**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**Supersliseur**- Nous avons la possibilité d'ajuster la température de l'enceinte (chambre)

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{% endtab%}

{% Tab Title = "Bambu Studio / Orcaslicateur"%}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760) .png) {% endtab%}

{% tab title = "cura"%}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{% hint style = "avertissement"%}  
Nous devons installer le plugin[**Plugin post-processus (par Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)À partir du menu_**Aide / spectacle**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.   
Nous redémarrons la guérison et nous irons à_**Extensions / post-traitement / modifier le code G**_Et nous sélectionnerons_**Taille de l'impression de maillage**_.  
{% de endthint%}  
{% endtab%}

{% tab title = "ideamaker"%}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{% endtab%}

{% tab title = "Simplify3d"%}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{% endtab%}  
{% endtabs%}

{% hint style = "info"%}  
Le**Les espaces réservés sont "alias" ou variables**d'impression.

Dans les liens suivants, vous pouvez en trouver une liste pour:[**Prusasliseur**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Supersliseur**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(en plus de ceux de la précédente),[**Bambou de studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)et[**Traitement**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

L'utilisation de ces macros permet à nos macros d'être dynamiques.  
{% de endthint%}

-   **gcode de final END_IMPRIMER**, dans ce cas, lorsqu'il n'utilise pas les porteurs de plaidoyer, il est commun à tous les laminateurs


    END_PRINT

### Variables

Comme nous l'avons déjà mentionné, ces nouvelles macros nous permettront d'avoir des fonctions très utiles comme nous énumérons précédemment.

Pour ajuster notre machine, nous utiliserons les variables que nous trouverons dans les macros / macros_notre_Globals.cfg et que nous détaillez ci-dessous.

#### Message / notifications Langue

Étant donné que de nombreux utilisateurs aiment avoir les notifications de macros dans leur langue, nous avons conçu un système de notification multicangue, actuellement espagnol (s) et anglais (en). Dans la variable suivante, nous pouvons l'ajuster:

| Variable        | Description                                                                                                                      | Valeurs possibles | Valeur par défaut |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_langue | Il nous permet de sélectionner la langue des notifications. Dans le cas de ne pas être bien défini, il sera utilisé en (anglais) | C'est / dans      | est               |

#### Extrusion relative

Vous permet de contrôler le mode d'extrusion que nous utiliserons à la fin de notre début_Imprimer. La valeur dépendra de la configuration de notre laminateur.

{% Hint Style = "Success"%}  
Il est conseillé de configurer votre laminateur pour l'utilisation de l'extrusion relative et d'ajuster cette variable à true.  
{% de endthint%}

| Variable                   | Description                                                                  | Valeurs possibles | Valeur par défaut |
| -------------------------- | ---------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_relatif_extrusion | Il nous permet d'indiquer le mode d'extrusion utilisé dans notre laminateur. | Vrai / faux       | Vrai              |

#### Vitesses

Pour gérer les vitesses utilisées dans les macros.

| Variable                      | Description                     | Valeurs possibles | Valeur par défaut |   |
| ----------------------------- | ------------------------------- | ----------------- | ----------------- | - |
| variable_macro_voyage_vitesse | Vitesse en traduit              | numérique         | 150               |   |
| variable_macro_Avec_vitesse   | Vitesse en traduit pour l'axe z | numérique         | 15                |   |

#### Hachage

Ensemble de variables liées au processus de homing.

| Variable | Description | Valeurs possibles | Valeur par défaut |
| -------- | ----------- | ----------------- | ----------------- |

#### Chauffage

Variables liées au processus de chauffage de notre machine.

| Variable                                             | Description                                                                                   | Valeurs possibles | Valeur par défaut |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_préchauffer_extrudeuse                      | Activer la buse préchauffée à la température indiquée en variable_préchauffer_extrudeuse_temp | Vrai / faux       | Vrai              |
| variable_préchauffer_extrudeuse_temp                 | Température préchauffée de buse                                                               | numérique         | 150               |
| variable_commencer_imprimer_chaleur_chambre_lit_temp | Température du lit pendant le processus de chauffage de notre enceinte                        | numérique         | 100               |

{% Hint Style = "Success"%}  
Avantages de l'utilisation de la buse préchauffée:

-   Il nous permet de temps supplémentaire pour que le lit atteigne sa température de manière uniforme
-   Si nous utilisons un capteur indictif qui n'a pas de compensation de température, cela nous permettra de rendre nos mesures plus cohérentes et précises
-   Il permet d'adoucir tout reste du filament dans la buse qui permet, dans certaines configurations, ces restes n'affectent pas l'activation du capteur  
    {% de endthint%}

#### Lit Mali (Mesh de lit)

Pour contrôler le processus de mise à niveau, nous avons des variables qui peuvent être très utiles. Par exemple, nous pouvons contrôler le type de nivellement que nous voulons utiliser en créant toujours un nouveau maillage, en chargeant un maillage adaptatif précédemment stocké ou en utilisant un maillage adaptatif.

| Variable                                                                                                                              | Description                                                                                     | Valeurs possibles | Valeur par défaut |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_étalonner_lit_engrener                                                                                                       | Il nous permet de sélectionner le type de malle que nous utiliserons dans notre début_IMPRIMER: |                   |                   |
| -Nouveau maillage, fera de nous une misère dans chaque impression                                                                     |                                                                                                 |                   |                   |
| -StoredMeh, chargera un maillage stocké et n'effectuera pas le sondage de lit                                                         |                                                                                                 |                   |                   |
| -Adaptive, fera de nous une nouvelle misère mais adaptée à la zone d'impression améliorant nos premières couches à plusieurs reprises |                                                                                                 |                   |                   |
| -Nommesh, dans le cas où nous n'avons pas de capteur ou utilisons le processus pour sauter le processus                               | Nouveau maillage / maillage stocké / adaptatif /                                                |                   |                   |
| noma                                                                                                                                  | adaptative                                                                                      |                   |                   |
| variable_lit_engrener_profil                                                                                                          | Le nom utilisé pour notre maillage stocké                                                       | texte             | défaut            |

{% hint style = "avertissement"%}  
Nous vous conseillons d'utiliser le niveau adaptatif car il ajustera toujours la misère à la taille de notre impression vous permettant d'avoir une zone de malle ajustée.

Il est important que nous ayons dans notre[démarrer-up gcode](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), dans l'appel à notre départ_Imprimer, imprimer des valeurs_Impression maximale_Min.  
{% de endthint%}

#### Purgé

Une phase importante de notre début de l'impression est une purge correcte de notre buse pour éviter les restes de filament ou qu'ils peuvent endommager notre impression à un moment donné. Ensuite, vous avez les variables impliquées dans ce processus:

| Variable                                                                                                                                                          | Description                                               | Valeurs possibles | Valeur par défaut |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------- | ----------------- |
| variable_ajutage_amorçage                                                                                                                                         | Nous pouvons choisir entre différentes options de pureté: |                   |                   |
| -Primelline va tracer la ligne de purge typique                                                                                                                   |                                                           |                   |                   |
| -PrimelineAdaptative générera une ligne de purge qui s'adapte à la zone de la pièce imprimée en utilisant la variable_ajutage_amorçage_ObjectDistance comme marge |                                                           |                   |                   |
| -Primoblob nous fera une goutte de filament dans un coin de notre lit très efficace pour nettoyer la buse et facile à retirer                                     |                                                           |                   |                   |
| Primeline /                                                                                                                                                       |                                                           |                   |                   |

Prime -Adaptive /   
Primeblob /   
FAUX

| PrimelineAdaptive |  
| variable_ajutage_amorçage_ObjectDistance | Si nous utilisons la ligne de purge adaptative, ce sera la marge à utiliser entre la ligne de purge et l'objet imprimé | Numérique | 5 |  
| variable_ajutage_prime_commencer_X | Où nous voulons localiser notre ligne de purge:  
-Min le fera à x = 0 (plus une petite marge de sécurité)  
-Max le fera à x = max (moins une petite marge de sécurité)  
-Le numéro sera la coordonnée X où localiser la purge | min /   
max /   
Numéro | Max |  
| variable_ajutage_prime_commencer_et | Où nous voulons localiser notre ligne de purge:  
-Min le fera à y = 0 (plus une petite marge de sécurité)  
-Max le fera à y = max (moins une petite marge de sécurité)  
-Le numéro sera la coordonnée et où localiser la purge | min /   
max /   
Numéro | min |  
| variable_ajutage_prime_Direction | L'adresse de notre ligne ou de notre goutte:  
-En arrière, la tête se déplacera vers l'avant de l'imprimante  
-Les attaquants se déplaceront à l'arrière  
-Auto ira au centre en fonction de la variable_ajutage_prime_commencer_et | voiture /   
avant /   
en arrière | Auto |

#### Charge / filament

Dans ce cas, ce groupe de variables facilitera la gestion de la charge et de la décharge de notre filament utilisé dans l'émulation du M600 par exemple ou en lançant les macros de filament de chargement et de décharge:

| Variable                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Valeurs possibles | Valeur par défaut |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_filament_décharger_longueur | Combien de retrait dans MM le filament, ajustez-le à votre machine, normalement la mesure de votre buse aux engrenages de votre extrudeuse en ajoutant une marge supplémentaire.                                                                                                                                                                                                                                                                                     | nombre            | 130               |
| variable_filament_décharger_vitesse  | La vitesse de rétraction du filament en mm / sec normalement une vitesse lente est utilisée.                                                                                                                                                                                                                                                                                                                                                                         | nombre            | 5                 |
| variable_filament_charger_longueur   | Distance en mm pour charger le nouveau filament ... comme en variable_filament_décharger_Longueur, nous utiliserons la mesure de votre équipement à l'extrudeuse en ajoutant une marge supplémentaire, dans ce cas, cette valeur supplémentaire dépendra de la quantité de purge que vous souhaitez être purgé ... Vous pouvez généralement lui donner plus de marge que la valeur précédente pour vous assurer qu'il est nettoyé l'extrusion du filament précédent. | nombre            | 150               |
| variable_filament_charger_vitesse    | La vitesse de charge du filament en mm / sec normalement, une vitesse plus rapide est utilisée pour décharger.                                                                                                                                                                                                                                                                                                                                                       | nombre            | 10                |

{% hint style = "avertissement"%}  
Un autre ajustement nécessaire pour votre section\[extrudeuse]le indiqué[**max_extruder_seulement_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... La valeur recommandée est généralement> 101 (si elle n'est pas définie utilise 50) pour par exemple, par exemple, permettez les tests d'étalonnage d'extrudeurs typiques.   
Vous devez ajuster la valeur en fonction de ce qui précède le test ou la configuration de votre**variable_filament_décharger_longueur**je**variable_filament_charger_longueur**.  
{% de endthint%}

#### Parking

Dans certains processus de notre imprimante, comme le loisir, il est conseillé de faire un parking de notre tête. Les macros de notre bundle ont cette option en plus des variables suivantes à gérer:

| Variable                                      | Description                                                                                                                                                                                                                                                                         | Valeurs possibles | Valeur par défaut |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_commencer_imprimer_parc_dans         | Emplacement où garer la tête pendant le pré-appel.                                                                                                                                                                                                                                  | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                     |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                 |                   |                   |
| variable_commencer_imprimer_parc_Avec_hauteur | Z hauteur pendant la pré-lourde                                                                                                                                                                                                                                                     | nombre            | 50                |
| variable_fin_imprimer_parc_dans               | Emplacement pour garer la tête à la fin ou annuler une impression.                                                                                                                                                                                                                  | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                     |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                 |                   |                   |
| variable_fin_imprimer_parc_Avec_houblon       | Distance pour monter à la fin de l'impression.                                                                                                                                                                                                                                      | nombre            | 20                |
| variable_pause_imprimer_parc_dans             | Emplacement pour garer la tête par Pausar l'impression.                                                                                                                                                                                                                             | dos /             |                   |
| centre /                                      |                                                                                                                                                                                                                                                                                     |                   |                   |
| devant                                        | dos                                                                                                                                                                                                                                                                                 |                   |                   |
| variable_pause_inactif_temps mort             | Valeur, en quelques secondes, de l'activation du processus d'inactivité dans la machine qui libère les moteurs et la perte de coordonnées,**Une valeur élevée est recommandée d'activer suffisamment la macro de pause pour effectuer une action avant de perdre des coordonnées.** | nombre            | 43200             |

#### Zéro

Prenons la majeure partie de notre machine afin qu'elle soit auto-niveau et facilite que notre machine soit toujours dans les meilleures conditions est essentielle.

**Z-Tilt est essentiellement un processus qui nous aide à aligner nos moteurs Z en ce qui concerne notre axe / cartésien (cartésien) ou XY (Corexy) (Corexy)**. Avec**Nous assurons que nous avons toujours notre z parfaitement et d'une manière précise et automatique**.

| Variable                            | Description                                                                                                  | Valeurs possibles | Valeur par défaut |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------- | ----------------- |
| variable_étalonner_Avec_inclinaison | Il permet, dans le cas de l'avoir activé dans notre configuration de Klipper, le processus de réglage Z-Tilt | Vrai / faux       | FAUX              |

#### Fausser

L'utilisation de[FAUSSER](broken-reference)Pour la correction ou l'ajustement précis de nos imprimantes, il est extrêmement conseillé si nous avons des écarts dans nos impressions. En utilisant la variable suivante, nous pouvons autoriser l'utilisation dans nos macros:

| Variable                | Description                                                                                                                                                                                                                | Valeurs possibles | Valeur par défaut  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------ |
| variable_fausser_profil | Vous permet de prendre en compte notre profil de biais qui sera facturé dans notre start macro_Imprimer. Pour l'activer, nous devons discuter de la variable et utiliser le nom du profil de biais de notre configuration. | texte             | mon_fausser_profil |

### Personnalisation des macros

Notre module Klipper utilise le système de configuration modulaire utilisé dans les temps et tire parti des avantages de Klipper dans le processus de fichier de configuration séquentiellement. C'est pourquoi l'ordre des ajustements inclués et personnalisés que nous voulons appliquer sur ces modules est essentiel.

{% hint style = "info"%}  
Lors de l'utilisation des paramètres de travail 3D comme module, ils ne peuvent pas être modifiés directement à partir du répertoire 3DWork-Klipper dans votre répertoire de configuration Klipper, car il sera en lecture seule (limitée à la lecture uniquement) pour la sécurité.

C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules sur votre machine.  
{% de endthint%}

#### **Personnaliser les variables**

Normalement, ce sera ce que nous devrons régler, pour effectuer des ajustements sur les variables que nous avons par défaut dans notre module**Travail 3D**Para coupe.

Simplement, ce que nous devons faire, c'est coller le contenu macro\[Gcode_macro global_DONT]Que pouvons-nous trouver dans les macros / macros_notre_Globals.cfg dans notre imprimante.cfg.

Nous vous rappelons ce qui a été commenté précédemment sur la façon dont Klipper traite les configurations séquentiellement, il est donc conseillé de le coller après les incluses que nous vous disons[ici](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nous aurons quelque chose comme ça (ce n'est qu'un exemple visuel):

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

{% hint style = "avertissement"%}
Les trois points (...) des exemples précédents sont simplement pour indiquer que vous pouvez avoir plus de configurations entre les sections ... en aucun cas elles ne doivent être portées.
{% EndHint%}

{% hint style = "info"%}

-   Nous vous conseillons d'ajouter des commentaires comme vous le voyez dans le cas précédent pour identifier ce que fait chaque section
-   Bien que vous n'ayez pas besoin de toucher toutes les variables, nous vous conseillons de copier l'intégralité du contenu de\[Gcode_macro global_DONT]{% de endthint%}

#### Personnaliser les macros

Les macros ont monté de manière modulaire afin qu'ils puissent être ajustés de manière simple. Comme nous l'avons mentionné précédemment, si nous voulons les ajuster, nous devons procéder comme nous l'avons fait avec les variables, copiez la macro en question dans notre imprimante.cfg (ou autres incluez la nôtre) et assurez-vous que c'est après l'inclure où nous ajoutons notre module 3DWork pour Klipper.

Nous avons deux groupes de macros:

-   Macros Pour ajouter des paramètres utilisateur, ces macros peuvent être facilement ajoutées et personnalisées car elles ont été ajoutées afin que tout utilisateur puisse personnaliser les actions à leur goût dans une certaine partie des processus que chaque macro fait.

**COMMENCER_IMPRIMER**

| Nombre Macro                                                | Description                                                                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| \_UTILISATEUR_COMMENCER_IMPRIMER_CHALEUR_CHAMBRE            | Il fonctionne juste après que notre enceinte commence à chauffer, si la chambre_Les passes précoces comme paramètre à notre début_IMPRIMER |
| \_UTILISATEUR_COMMENCER_IMPRIMER_AVANT_Hachage              | Il est exécuté avant le homing initial pour le début de l'impression                                                                       |
| \_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT        | Il fonctionne lorsque notre lit arrive à sa température, avant_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT                                      |
| \_UTILISATEUR_COMMENCER_IMPRIMER_LIT_ENGRENER               | Est lancé avant_COMMENCER_IMPRIMER_LIT_ENGRENER                                                                                            |
| \_UTILISATEUR_COMMENCER_IMPRIMER_PARC                       | Est lancé avant_COMMENCER_IMPRIMER_PARC                                                                                                    |
| \_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_Extrudeuse | Est lancé avant_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_Extrudeuse                                                                              |

**FIN_IMPRIMER**

| Nombre Macro                                          | Description                                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| \_UTILISATEUR_FIN_IMPRIMER_AVANT_Radiateurs_DÉSACTIVÉ | Il est exécuté avant d'effectuer le radiateur, avant_FIN_IMPRIMER_AVANT_Radiateurs_DÉSACTIVÉ |
| \_UTILISATEUR_FIN_IMPRIMER_APRÈS_Radiateurs_DÉSACTIVÉ | Il est exécuté après l'arrêt du radiateur, avant_FIN_IMPRIMER_APRÈS_Radiateurs_DÉSACTIVÉ     |
| \_UTILISATEUR_FIN_IMPRIMER_PARC                       | Il est exécuté devant la tête de la tête, avant_FIN_IMPRIMER_PARC                            |

**IMPRIMER_Bases**

| Nombre Macro                      | Description                        |
| --------------------------------- | ---------------------------------- |
| \_UTILISATEUR_PAUSE_COMMENCER     | Est exécuté au début d'une pause   |
| \_UTILISATEUR_PAUSE_FIN           | Il fonctionne à la fin d'une pause |
| \_UTILISATEUR_CONTINUER_COMMENCER | Est exécuté au début d'un résumé   |
| \_UTILISATEUR_CONTINUER_FIN       | Se déroule à la fin d'un résumé    |

-   Les macros internes, ce sont des macros pour diviser la macro principale en processus et sont importantes pour cela. Il est conseillé qu'en cas d'exiger ceux-ci sont copiés tels quels.

**COMMENCER_IMPRIMER**

| Nombre Macro                                    | Description                                                                                                                                                                                                                             |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_COMMENCER_IMPRIMER_CHALEUR_CHAMBRE            | Chauffe l'enceinte dans le cas où le paramètre de la chambre_Tôt est reçu par notre macro start_Imprimer du laminateur                                                                                                                  |
| \_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_LIT        | Il fonctionne lorsque le lit arrive à température, après_UTILISATEUR_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_Lit. Normalement, il est utilisé pour le traitement d'étalonnage du lit (z_INCLINAISON_Ajuster, quad_PORTIQUE_Nivellement, ...) |
| \_COMMENCER_IMPRIMER_LIT_ENGRENER               | Il est en charge de la logique de la misère du lit.                                                                                                                                                                                     |
| \_COMMENCER_IMPRIMER_PARC                       | Séduit la tête d'impression tout en chauffant la buse à la température d'impression.                                                                                                                                                    |
| \_COMMENCER_IMPRIMER_APRÈS_CHAUFFAGE_Extrudeuse | Faire la purge de nazz et charger le profil de biais au cas où nous définirons dans les variables                                                                                                                                       |

## Imprimantes et électroniques

Alors que nous travaillons avec différents modèles d'imprimantes et électroniques, nous ajouterons ceux qui ne sont pas directement soutenus par les moments, qu'il s'agisse de contributions ou de communauté.

-   Imprimantes, dans ce répertoire, nous aurons toutes les configurations d'imprimante
-   Planches, ici nous trouverons l'électronique

### Paramètres et épingles

Notre module Klipper utilise le système de configuration modulaire utilisé dans les temps et tire parti des avantages de Klipper dans le processus de fichier de configuration séquentiellement. C'est pourquoi l'ordre des ajustements inclués et personnalisés que nous voulons appliquer sur ces modules est essentiel.

{% hint style = "info"%}
Lors de l'utilisation des paramètres de travail 3D comme module, ils ne peuvent pas être modifiés directement à partir du répertoire 3DWork-Klipper dans votre répertoire de configuration Klipper, car il sera en lecture seule (limitée à la lecture uniquement) pour la sécurité.

C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules sur votre machine.
{% EndHint%}

Comme nous l'avons expliqué dans "[Personnaliser les macros](3dwork-klipper-bundle.md#personalizando-macros)"Nous utiliserons le même processus pour ajuster les paramètres ou les broches pour les ajuster à nos besoins.

#### Personnalisation des paramètres

Comme nous vous conseillons de créer une section dans votre imprimante.cfg qui s'appelle les remplacements des utilisateurs, placés après l'inclusion de nos configurations, pour pouvoir ajuster et personnaliser tout paramètre qui y est utilisé.

Dans l'exemple suivant, nous verrons comment, dans notre cas, nous voulons personnaliser les paramètres de notre nivellement de lit (lit_Mesh) ajuster les points d'enquête (sonde_Count) concernant la configuration que nous avons par défaut dans les configurations de notre module Klipper:

{% code title = "imprimante.cfg"%}

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

{% Endcode%}

{% hint style = "avertissement"%}
Les trois points (...) des exemples précédents sont simplement pour indiquer que vous pouvez avoir plus de configurations entre les sections ... en aucun cas elles ne doivent être portées.
{% EndHint%}

Nous pouvons utiliser ce même processus avec tout paramètre que nous souhaitons ajuster.

#### Personnalisation de la configuration des pin

Nous procéderons exactement comme nous l'avons fait auparavant, dans notre zone de remplacements utilisateur, nous ajouterons les sections des épingles que nous voulons ajuster à notre goût.

Dans l'exemple suivant, nous allons personnaliser quelle est la broche de notre ventilateur électronique (contrôleur_ventilateur) pour l'affecter à un différent de la valeur par défaut:

{% code title = "imprimante.cfg"%}

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

{% Endcode%}

{% hint style = "avertissement"%}
Les trois points (...) des exemples précédents sont simplement pour indiquer que vous pouvez avoir plus de configurations entre les sections ... en aucun cas elles ne doivent être portées.
{% EndHint%}

```

```
