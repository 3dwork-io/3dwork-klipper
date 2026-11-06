# Pack Tondeuse 3Dwork

## Pack de macros, paramètres et autres utilitaires pour Clipper

![Español](https://flagcdn.com/w40/es.png)[![English](https://flagcdn.com/w40/gb.png)](README.en.md)[![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md)[![Italiano](https://flagcdn.com/w40/it.png)](README.it.md)[![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)[![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ AVERTISSEMENT****GUIDE EN COURS !!!****<span style="color: red">Bien que les macros soient entièrement fonctionnelles, elles font l’objet d’un développement continu.</span>****<span style="color: orange">Utilisez-les à vos propres risques !!!</span>**

Journal des modifications

12/07/2023 - Ajout du support pour automatiser la création de firmware pour l'électronique Bigtreetech

Depuis**Travail 3D**Nous avons compilé et affiné un ensemble de macros, de paramètres machines et électroniques, ainsi que d'autres outils pour une gestion simple et puissante de Klipper.

Une grande partie de ce package est basée sur[**Rats**](https://os.ratrig.com/)améliorer les parties que nous jugeons intéressantes, ainsi que d'autres contributions de la communauté.

## Installation

Pour installer notre package pour Klipper, nous suivrons les étapes suivantes

### Télécharger depuis le référentiel

Nous allons nous connecter à notre hôte via SSH et émettre les commandes suivantes :

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ UTILISATION**Si votre répertoire de configuration Klipper est personnalisé, n'oubliez pas d'ajuster la première commande en conséquence pour votre installation.

> **ℹ️ INFORMATIONS POUR LES NOUVELLES INSTALLATIONS**Puisque Klipper ne permet pas l'accès aux macros sans un fichier Printer.cfg valide et une connexion à un MCU, nous pouvons utiliser cette configuration temporaire :
>
> 1.  Assurez-vous d'avoir le[hôte comme deuxième MCU](raspberry-como-segunda-mcu.md)
> 2.  Ajoutez ce fichier Printer.cfg de base pour activer les macros :

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

Cela vous permettra de démarrer Klipper et d'accéder aux macros.

### Utiliser Moonraker pour être toujours à jour

Grâce à Moonraker, nous pouvons utiliser son update_manager pour être au courant des améliorations que nous pourrions introduire dans le futur.

Depuis Mainsail/Fluidd nous éditerons notre moonraker.conf (il doit être à la même hauteur que votre imprimante.cfg) et nous ajouterons à la fin du fichier de configuration :

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ AVERTISSEMENT****Pensez à faire l'étape d'installation au préalable sinon Moonraker générera une erreur et ne pourra pas démarrer.**
>
> **En revanche, si le répertoire de votre configuration Klipper est personnalisé, pensez à ajuster le chemin en fonction de votre installation.**

## Macro

Nous avons toujours dit que RatOS est l'une des meilleures distributions Klipper, avec prise en charge des modules Raspberry et CB1, en grande partie grâce à ses configurations modulaires et à ses excellentes macros.

Quelques macros ajoutées qui nous seront utiles :

### **Macros à usage général**

| Macro                       | Description                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PEUT-ÊTRE_HOME**          | Cela nous permet d'optimiser le processus de référencement uniquement en l'exécutant sur les axes qui ne sont pas référencés.                                                        |
| **PAUSE**                   | Grâce aux variables associées, cela nous permet de gérer une pause avec un stationnement de tête plus polyvalent que les macros normales.                                            |
| **SET_PAUSE_AT_LAYER**      |                                                                                                                                                                                      |
| **SET_PAUSE_AT_NEXT_LAYER** | Une macro très utile que Mainsail intègre dans son UI pour pouvoir faire une pause à la demande dans un calque spécifique... au cas où nous l'aurions oublié lors du laminage.       |
|                             | Nous en avons également un autre pour exécuter la pause sur le calque suivant.                                                                                                       |
| **CONTINUER**               | Amélioré car il nous permet de détecter si notre buse n'est pas à la température d'extrusion afin de le résoudre avant qu'elle ne montre une erreur et n'endommage notre impression. |
| **CANCEL_PRINT**            | Ce qui permet d'utiliser le reste des macros pour effectuer correctement une annulation d'impression.                                                                                |

-   **En pause lors du changement de calque**, des macros très intéressantes qui nous permettent de mettre en pause un calque ou de lancer une commande au démarrage du calque suivant. ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)De plus, un autre avantage est qu'ils sont intégrés à Mainsail, nous aurons donc de nouvelles fonctions dans notre interface utilisateur, comme vous pouvez le voir ci-dessous :![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macros de gestion d'impression**

| Macro           | Description                                                                                                                                                                    |   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | - |
| **START_PRINT** | Cela nous permettra de démarrer nos impressions de manière sûre et à la manière de Klipper. Au sein de celui-ci, nous trouverons quelques fonctions intéressantes telles que : |   |
|                 | • Préchauffage intelligent de la buse lors de l'utilisation d'un capteur à sonde                                                                                               |   |
|                 | • Possibilité d'utiliser l'inclinaison en Z via variable                                                                                                                       |   |
|                 | • Maillage de lit adaptatif, forcé ou à partir d'un maillage enregistré                                                                                                        |   |
|                 | • Ligne de purge personnalisable entre la ligne de purge normale et adaptative ou la chute de purge                                                                            |   |
|                 | • Macro segmentée pour pouvoir être personnalisée comme nous vous le montrerons plus tard                                                                                      |   |
| **END_PRINT**   | Macro de fin d'impression où nous avons également une segmentation pour pouvoir personnaliser notre macro. Nous disposons également d'un stationnement de tête dynamique.      |   |

-   **Cadre de lit adaptatif**Grâce à la polyvalence de Klipper, nous pouvons faire des choses qui semblent aujourd'hui impossibles... un processus important pour l'impression est d'avoir un maillage d'écarts par rapport à notre lit qui nous permet de les corriger pour avoir une parfaite adhérence des premières couches.  
     À de nombreuses reprises, nous effectuons ce maillage avant l'impression pour nous assurer qu'il fonctionne correctement et cela se fait sur toute la surface de notre lit. 
     Avec le maillage adaptatif du lit, cela se fera dans la zone d'impression, ce qui le rend beaucoup plus précis que la méthode traditionnelle... dans les captures d'écran suivantes, nous verrons les différences entre un maillage traditionnel et un maillage adaptatif.
    <div style="display: flex; justify-content: space-between;">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
    </div>

### **Macros de gestion des filaments**

Ensemble de macros qui nous permettront de gérer différentes actions avec notre filament, comme le charger ou le décharger.

| Macro               | Description                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **M600**            | Cela nous permettra la compatibilité avec le gcode M600 normalement utilisé dans les plastifieuses pour le changement de filament. |
| **UNLOAD_FILAMENT** | Configurable à travers les variables, il nous permettra une décharge assistée du filament.                                         |
| **LOAD_FILAMENT**   | Identique au précédent mais lié à la charge du filament.                                                                           |

### **Macros de gestion des bobines de filament (Spoolman)**

> **⚠️ AVERTISSEMENT****SECTION EN COURS !!!**

[**Spoolman**](https://github.com/Donkie/Spoolman)est un gestionnaire de bobines de filament intégré à Moonraker et qui nous permet de gérer notre stock et la disponibilité des filaments.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Nous n'allons pas entrer dans l'installation et la configuration de celui-ci puisque c'est relativement simple grâce au[**instructions de votre Github**](https://github.com/Donkie/Spoolman)**,**dans tous les cas**Nous vous conseillons d'utiliser Docker**pour plus de simplicité et rappelez-vous**activer les paramètres dans Moonraker**requis:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro              | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| SET_ACTIVE_SPOOL   | Cela nous permet d'indiquer quel est l'ID de la bobine à utiliser |
| CLEAR_ACTIVE_SPOOL | Cela nous permet de réinitialiser la bobine active                |

L'idéal dans chaque cas serait d'ajouter à notre plastifieuse,**dans les gcodes du filament pour chaque bobine, l'appel à ceci**, et souviens-toi**changer son identifiant une fois consommé**pour pouvoir garder une trace de ce qu'il reste de filament dedans !!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Macros de gestion des surfaces d'impression**

> **⚠️ AVERTISSEMENT****SECTION EN COURS !!!**

Il est généralement normal que nous ayons des surfaces d'impression différentes en fonction de la finition que nous souhaitons avoir ou du type de filament.

Cet ensemble de macros, créé par[Garethky](https://github.com/garethky), ils nous permettront d'avoir le contrôle de ceux-ci et surtout le réglage correct du ZOffset dans chacun d'eux dans le style que nous avons dans les machines Prusa. Ci-dessous vous pouvez voir certaines de ses fonctions :

-   Nous pouvons stocker le nombre de surfaces d'impression que nous voulons, chacune ayant un nom unique
-   chaque surface d'impression aura son propre ZOffset
-   Si nous effectuons des ajustements Z lors d'une impression (Babystepping) depuis notre Clipper, ce changement sera stocké dans la surface activée à ce moment-là

D'un autre côté, nous avons quelques**exigences pour l'implémenter (nous essaierons de l'ajouter à la logique PRINT_START du bundle dans le futur en activant cette fonction par variable et en créant une macro utilisateur précédente et suivante pour pouvoir insérer des événements utilisateur)**:

-   l'utilisation de**[save_variables]**Dans notre cas, nous utiliserons ~/variables.cfg pour stocker les variables et cela se trouve déjà dans le cfg de ces macros.  
    Cela créera automatiquement un fichier variables_build_sheets.cfg où il enregistrera nos variables sur le disque.

**Exemple de fichier de configuration de variables**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

-   Nous devons inclure un appel à APPLY_BUILD_SHEET_ADJUSTMENT dans notre PRINT_START pour pouvoir appliquer le ZOffset de la surface sélectionnée
-   Il est important que pour que la macro précédente, APPLY_BUILD_SHEET_ADJUSTMENT, fonctionne correctement, il faut ajouter un SET_GCODE_OFFSET Z=0.0 juste avant d'appeler APPLY_BUILD_SHEET_ADJUSTMENT.


    # Load build sheet
    SHOW_BUILD_SHEET ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset

Par contre, il est intéressant de pouvoir avoir des macros pour activer une surface ou une autre ou même la passer en paramètre depuis notre plastifieuse pour qu'avec différents profils d'imprimante ou de filament on puisse charger l'un ou l'autre automatiquement :

> **⚠️ AVERTISSEMENT**Il est important que la valeur dans NAME="xxxx" corresponde au nom que nous avons donné lors de l'installation de notre surface d'impression.

\*\*imprimante.cfg

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

Également dans le cas de KlipperScreen, nous pouvons ajouter un menu spécifique pour gérer le chargement des différentes surfaces, où nous inclurons un appel aux macros précédemment créées pour le chargement de chaque surface :

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

### **Macros de configuration des machines**

| Macro                                                             | Description                                                                                                                                                                                                                |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILE_FIRMWARE**                                              | Avec cette macro, nous pouvons compiler le firmware Klipper de manière simple, rendre le firmware accessible depuis l'interface utilisateur pour plus de simplicité et pouvoir l'appliquer à notre électronique.           |
| Ici vous avez plus de détails sur l’électronique prise en charge. |                                                                                                                                                                                                                            |
| **CALCULATE_BED_MESH**                                            | Une macro extrêmement utile pour calculer la surface de notre maillage car cela peut parfois être un processus compliqué.                                                                                                  |
| **PID_ALL**                                                       |                                                                                                                                                                                                                            |
| **PID_EXTRUDEUSE**                                                |                                                                                                                                                                                                                            |
| **PID_BED**                                                       | Ces macros, où nous pouvons transmettre les températures au PID sous forme de paramètres, nous permettront d'effectuer l'étalonnage de la température de manière extrêmement simple.                                       |
| **TEST_VITESSE**                                                  |                                                                                                                                                                                                                            |
| **TEST_SPEED_DELTA**                                              | Macro originale du compagnon[Élise](https://github.com/AndrewEllis93)Ils nous permettront de manière assez simple de tester la vitesse à laquelle nous pouvons déplacer notre machine avec précision et sans perte de pas. |

\*\_**Firmware compilé pour les appareils électroniques pris en charge**, pour faciliter le processus de création et de maintenance de notre firmware Klipper pour nos MCU, nous avons la macro COMPILE_FIRMWARE qui, une fois exécutée, nous pouvons utiliser notre électronique comme paramètre pour faire uniquement cela, elle compilera Klipper pour toute l'électronique prise en charge par notre bundle :![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)Nous les retrouverons facilement accessibles depuis notre interface web dans le répertoire firmware_binaries de notre onglet MACHINE (si nous utilisons Mainsail) :![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)Vous trouverez ci-dessous la liste des appareils électroniques pris en charge :

> ⚠️**IMPORTANTE!!!**
>
> Ces scripts sont prêts à fonctionner sur un système >Raspbian avec un utilisateur pi, si ce n'est pas votre cas vous devrez l'adapter.
>
> Les firmwares sont générés pour être utilisés avec une connexion USB, ce qui est toujours ce que nous recommandons. De plus, le point de montage USB est toujours le même, donc la configuration de votre connexion MCU ne changera pas si elle est générée avec notre macro/script.
>
> **Pour que Klipper puisse exécuter des macros shell, une extension doit être installée, grâce au compagnon**[**arc sinus**](https://github.com/Arksine)**, cela le permet.**
>
> **Selon la distribution Klipper utilisée, ils peuvent déjà être activés.**
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> Le plus simple est d'utiliser[**keoh**](../instalacion/#instalando-kiauh)où l'on retrouvera dans une de ses options la possibilité d'installer cette extension :
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Nous pouvons également effectuer le processus à la main, nous copierons manuellement le plugin pour Klipper &lt;[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)dans notre annuaire`_**~/klipper/klippy/extras**_`en utilisant SSH ou SCP et en redémarrant Klipper.

| Électronique      | Nom du paramètre à utiliser dans la macro |
| ----------------- | ----------------------------------------- |
| Manta E           | Avec fierté                               |
| Oubliez M4P       | btt-manta-m4p                             |
| Manta M4P v2.a    | btt-manta-m4p-22                          |
| Oubliez le M8P    | btt-manta-m8p                             |
| Oubliez M8P v1.1  | btt-manta-m8p-11                          |
| Octopus Max EST   | btt-octopus-max-ez                        |
| Poulpe Pro (446)  | btt-octopus-pro-446                       |
| Poulpe Pro (429)  | btt-octopus-pro-429                       |
| Poulpe Pro (H723) | btt-octopus-pro-h723                      |
| Poulpe v1.1       | btt-octopus-11                            |
| Poulpe v1.1 (407) | btt-octopus-11-407                        |
| SKR Pro v1.2      | skr_pro_12                                |
| 3 SKR             | btt_skr_3                                 |
| Saqr A (Haha)     | Tu le saoules                             |
| SKR 3EZ           | btt-skr-3-ez                              |
| SKR 3EZ (H723)    | Elle est très ivre                        |
| 2 SKR (429)       | btt-skr-2-429                             |
| 2 SKR (407)       | btt-skr-2-407                             |
| SKR RAT           | btt-court-circuit-10                      |
| SKR1.4 Turbo      | btt-skr-14-turbo                          |
| SKR Mini Ez vz    | btt_skr_mini_e3_30                        |

| Tête d'outil (CAN) | Nom du paramètre à utiliser dans la macro |
| ------------------ | ----------------------------------------- |
| EBB42 v1           | btt_ebb42_10                              |
| EBB36v1            | btt_ebb36_10                              |
| EBB42 v1.1         | btt_ebb42_11                              |
| EBB36 v1.1         | btt_ebb36_11                              |
| EBB42 v1.2         | btt_ebb42_12                              |
| EBB36 v1.2         | btt_ebb36_12                              |

| **Électronique**              | **Nom du paramètre à utiliser dans la macro** |
| ----------------------------- | --------------------------------------------- |
| MKS Aigle v1.x                | mks-aigle-10                                  |
| ISS Robin Nano vz             | mks-robin-nano-30                             |
| MKS Robin Nano v2             | mks-robin-nano-20                             |
| MKS Gen L                     | mks-gen-l                                     |
| Le cours sin nano do de Rubin | Il fait chaud                                 |

| Tête d'outil (CAN) | Nom du paramètre à utiliser dans la macro |
| ------------------ | ----------------------------------------- |
| Mellow FLY SHT42   | mellow_fly_sht_42                         |
| Mellow FLY SHT36   | mellow_fly_sht_36                         |

| Électronique    | Nom du paramètre à utiliser dans la macro |
| --------------- | ----------------------------------------- |
| Araignée Fysetc | araignée fysetc                           |

| Électronique         | Nom du paramètre à utiliser dans la macro |
| -------------------- | ----------------------------------------- |
| Artillerie Ruby v1.x | artillerie-rubis-12                       |

| Électronique          | Nom du paramètre à utiliser dans la macro |
| --------------------- | ----------------------------------------- |
| Framboise Pico/RP2040 | rpi-rp2040                                |

| Électronique   | Nom du paramètre à utiliser dans la macro |
| -------------- | ----------------------------------------- |
| Léviathan v1.2 | Léviathan-12                              |

### Ajout de macros 3Dwork à notre installation

Depuis notre interface, Mainsail/Fluidd, nous allons éditer notre imprimante.cfg et ajouter :

**imprimante.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️**INFOS !!!**Il est important d'ajouter ces lignes à la fin de notre fichier de configuration... juste au dessus de la section pour que s'il y a des macros dans notre cfg ou include, elles soient écrasées par les nôtres : 
> \#\*# \\&lt;--- SAVE_CONFIG --->

> ⚠️**IMPORTANTE!!!**Les macros normales ont été séparées de**shell de macros**étant donné que**Pour les activer, il est nécessaire d'effectuer manuellement des étapes supplémentaires, en plus du fait qu'elles sont actuellement en cours de test.**et\*\*Ils peuvent avoir besoin d'autorisations supplémentaires pour attribuer des autorisations d'exécution pour lesquelles les instructions n'ont pas été indiquées puisqu'ils tentent d'automatiser.\*\***Si vous les utilisez, c'est à vos propres risques.**

### Configuration de notre plastifieuse

Puisque nos macros sont dynamiques, elles extrairont certaines informations de la configuration de notre imprimante et de la plastifieuse elle-même. Pour ce faire, nous vous conseillons de configurer vos plastifieuses comme suit :

-   **démarrer le gcode START_PRINT**, en utilisant des espaces réservés pour transmettre dynamiquement les valeurs de température du filament et du lit :

**PrusaSlicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer**- nous avons la possibilité d'ajuster la température de l'enceinte (CHAMBRE)

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

**Bamboo Studio/OrcaSlicer**

```ini
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

**Traitement**

```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

> ⚠️**Avis!!!**Il va falloir installer le plugin[**Plugin de post-traitement (par frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)du menu_**Aide/Afficher**_Dossier de configuration... nous copierons le script du lien précédent dans le dossier du script.  
> On redémarre Cura et on ira à_**Extensions/Post-traitement/Modifier le G-Code**_et nous sélectionnerons_**Taille d'impression du maillage**_.

**Créateur d'idées**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplifier3D**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️**INFOS !!!**Le**les espaces réservés sont des "alias" ou des variables que les plastifieurs utilisent pour que lors de la génération du gcode, ils soient remplacés par les valeurs configurées dans le profil**impression.
>
> Dans les liens suivants, vous pouvez en trouver une liste pour :[**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(en plus de ceux ci-dessus),[**Studio Bambou**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)et[**Traitement**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> L'utilisation de ceux-ci permet à nos macros d'être dynamiques.

-   **gcode de final END_PRINT**, dans ce cas, en n'utilisant pas d'espaces réservés, il est commun à toutes les plastifieuses

```ini
END_PRINT
```

### Variables

Comme nous l'avons déjà mentionné, ces nouvelles macros nous permettront d'avoir des fonctions très utiles comme nous l'avons listé ci-dessus.

Pour les ajuster à notre machine nous utiliserons les variables que nous retrouverons dans macros/macros_var_globals.cfg et que nous détaillons ci-dessous.

#### Langue des messages/notifications

Étant donné que de nombreux utilisateurs aiment recevoir des notifications de macros dans leur langue, nous avons conçu un système de notification multilingue, actuellement en espagnol (es) et en anglais (en). Dans la variable suivante, nous pouvons l'ajuster :

| Variable        | Description                                                                                                          | Valeurs possibles | Valeur par défaut |
| --------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| langue_variable | Il nous permet de sélectionner la langue des notifications. S'il n'est pas bien défini, il sera utilisé en (anglais) | est / dans        | est               |

#### Extrusion relative

Cela nous permet de contrôler le mode d'extrusion que nous utiliserons lors de la fin de notre START_PRINT. La valeur dépendra de la configuration de notre plastifieuse.

> 💡**Conseil**Il est conseillé de configurer votre plastifieuse pour utiliser l'extrusion relative et de définir cette variable sur True.

| Variable                    | Description                                                                    | Valeurs possibles | Valeur par défaut |
| --------------------------- | ------------------------------------------------------------------------------ | ----------------- | ----------------- |
| variable_relative_extrusion | Il nous permet d'indiquer le mode d'extrusion utilisé dans notre plastifieuse. | Vrai / Faux       | Vrai              |

#### Vitesses

Pour gérer les vitesses utilisées dans les macros.

| Variable                    | Description                       | Valeurs possibles | Valeur par défaut |   |
| --------------------------- | --------------------------------- | ----------------- | ----------------- | - |
| variable_macro_travel_speed | Vitesse de transfert              | numérique         | 150               |   |
| variable_macro_z_speed      | Vitesse de transfert pour l'axe Z | numérique         | 15                |   |

#### Retour à destination

Ensemble de variables liées au processus de référencement.

| Variable | Description | Valeurs possibles | Valeur par défaut |
| -------- | ----------- | ----------------- | ----------------- |

#### Chauffage

Variables liées au processus de chauffage de notre machine.

| Variable                                   | Description                                                                                     | Valeurs possibles | Valeur par défaut |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_preheat_extruder                  | Permet le préchauffage de la buse à la température indiquée dans variable_preheat_extruder_temp | Vrai / Faux       | Vrai              |
| variable_preheat_extruder_temp             | Température de préchauffage de la buse                                                          | numérique         | 150               |
| variable_start_print_heat_chamber_bed_temp | Température du lit pendant le processus de chauffage de notre enceinte                          | numérique         | 100               |

> 💡**Conseil**Avantages de l'utilisation d'une buse préchauffée :

-   Cela nous laisse du temps supplémentaire pour que le lit puisse atteindre sa température de manière uniforme.
-   Si nous utilisons un capteur inductif sans compensation de température, cela permettra à nos mesures d'être plus cohérentes et précises.
-   Permet de ramollir tout filament restant dans la buse, ce qui signifie que, dans certaines configurations, ces restes n'affectent pas l'activation du capteur. 
    {% indice de fin %}

#### Filet de lit

Pour contrôler le processus de mise à niveau, nous disposons de variables qui peuvent être très utiles. Par exemple, nous pouvons contrôler le type de nivellement que nous souhaitons utiliser en créant toujours un nouveau maillage, en chargeant un maillage précédemment stocké ou en utilisant un maillage adaptatif.

| Variable                                                                                                              | Description                                                                                        | Valeurs possibles | Valeur par défaut |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_calibrate_bed_mesh                                                                                           | Cela nous permet de sélectionner le type de maillage que nous utiliserons dans notre START_PRINT : |                   |                   |
| - nouveau maillage, il maillera chaque impression                                                                     |                                                                                                    |                   |                   |
| - storemesh, chargera un maillage stocké et n'effectuera pas le sondage du lit                                        |                                                                                                    |                   |                   |
| - adaptatif, il fera un nouveau maillage mais adapté à la zone d'impression, améliorant souvent nos premières couches |                                                                                                    |                   |                   |
| -nomesh, au cas où nous n'aurions pas de capteur ou si nous utilisons un maillage pour ignorer le processus           | nouveau maillage / maillage stocké / adaptatif /                                                   |                   |                   |
| noms                                                                                                                  | adaptative                                                                                         |                   |                   |
| variable_bed_mesh_profile                                                                                             | Le nom utilisé pour notre maillage stocké                                                          | texte             | défaut            |

> ⚠️**Avis!!!**Nous vous conseillons d'utiliser le nivellement adaptatif puisqu'il ajustera toujours le maillage à la taille de notre impression, vous permettant ainsi d'avoir une zone de maillage ajustée.
>
> Il est important que nous ayons dans notre[démarrer le gcode de notre plastifieuse](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), dans l'appel à notre START_PRINT, les valeurs PRINT_MAX et PRINT_MIN.

#### purgé

Une phase importante de notre démarrage d'impression est une purge correcte de notre buse pour éviter les restes de filament ou que ceux-ci pourraient endommager notre impression à un moment donné. Ci-dessous vous avez les variables qui interviennent dans ce processus :
| Variables | Descriptif | Valeurs possibles | Valeur par défaut |
\| --- \| --- \| --- \| --- \|
| variable_nozzle_priming | Nous pouvons choisir entre différentes options de purge :<br>- primeline : dessine la ligne de purge typique<br>- primelineadaptive : générer une ligne de fond perdu adaptée à la zone d'impression en utilisant variable_nozzle_priming_objectdistance comme marge<br>- primeblob : fait une goutte de filament dans un coin du lit | primeline / primelineadaptive / primeblob / Faux | primelineadaptatif |
| variable_nozzle_priming_objectdistance | Si nous utilisons une ligne de fond perdu adaptative, ce sera la marge à utiliser entre la ligne de fond perdu et l'objet imprimé | numérique | 5 |
| variable_nozzle_prime_start_x | Où localiser notre ligne de purge en X :<br>- min : X=0 (plus de marge de sécurité)<br>- max : X=max (moins la marge de sécurité)<br>- nombre : coordonnée X spécifique | min/max/nombre | maximum |
| variable_nozzle_prime_start_y | Où localiser notre ligne de purge Y :<br>- min : Y=0 (plus de marge de sécurité)<br>- max : Y=max (moins la marge de sécurité)<br>- numéro : coordonnée Y spécifique | min/max/nombre | min |
| variable_nozzle_prime_direction | Direction de ligne ou de chute :<br>- vers l'arrière : vers l'avant<br>- en avant : en arrière<br>- auto : vers le centre selon variable_nozzle_prime_start_y | auto / avant / arrière | voiture |

#### Chargement/déchargement de filaments

Dans ce cas, ce groupe de variables nous permettra de gérer plus facilement le chargement et le déchargement de notre filament utilisé en émulation du M600 par exemple, ou lors du lancement des macros de chargement et déchargement du filament :

| Variable                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   | Valeurs possibles | Valeur par défaut |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_filament_unload_length | De combien rétracter le filament en mm, ajustez à votre machine, normalement la mesure de votre buse aux engrenages de votre extrudeuse en ajoutant une marge supplémentaire.                                                                                                                                                                                                                                                                 | nombre            | 130               |
| variable_filament_unload_speed  | Vitesse de rétraction du filament en mm/sec, normalement une vitesse lente est utilisée.                                                                                                                                                                                                                                                                                                                                                      | nombre            | 5                 |
| variable_filament_load_length   | Distance en mm pour charger le nouveau filament... tout comme dans variable_filament_unload_length nous utiliserons la mesure de votre équipement à l'extrudeuse en ajoutant une marge supplémentaire, dans ce cas cette valeur supplémentaire dépendra de la quantité que vous souhaitez purger... normalement vous pouvez lui donner plus de marge que la valeur précédente pour garantir que l'extrusion du filament précédent est propre. | nombre            | 150               |
| variable_filament_load_speed    | Vitesse de chargement du filament en mm/sec, normalement une vitesse plus rapide est utilisée que la vitesse de déchargement.                                                                                                                                                                                                                                                                                                                 | nombre            | 10                |

> ⚠️**Avis!!!**Un autre paramètre nécessaire pour votre section**[extrudeuse]**indiquer le[**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)...la valeur recommandée est généralement >101 (si elle n'est pas définie, utilisez 50) pour, par exemple, permettre des tests d'étalonnage typiques d'une extrudeuse.  
> Vous devez ajuster la valeur en fonction de ce qui a été mentionné précédemment concernant le test ou la configuration de votre**variable_filament_unload_length**je**variable_filament_load_length**.

#### Parking

Dans certains processus de notre imprimante, comme en pause, il est conseillé de garer la tête. Les macros de notre bundle ont cette option en plus des variables suivantes à gérer :

| Variable                           | Description                                                                                                                                                                                                                                                                                                               | Valeurs possibles | Valeur par défaut |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_start_print_park_in       | Emplacement où garer la tête pendant le préchauffage.                                                                                                                                                                                                                                                                     | dos /             |                   |
| centre /                           |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                             | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_start_print_park_z_height | Hauteur Z pendant le préchauffage                                                                                                                                                                                                                                                                                         | nombre            | 50                |
| variable_end_print_park_in         | Emplacement où garer la tête lors de la fin ou de l’annulation d’une impression.                                                                                                                                                                                                                                          | dos /             |                   |
| centre /                           |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                             | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_end_print_park_z_hop      | Distance à monter en Z en fin d'impression.                                                                                                                                                                                                                                                                               | nombre            | 20                |
| variable_pause_print_park_in       | Emplacement où garer la tête lors d’une pause d’impression.                                                                                                                                                                                                                                                               | dos /             |                   |
| centre /                           |                                                                                                                                                                                                                                                                                                                           |                   |                   |
| devant                             | dos                                                                                                                                                                                                                                                                                                                       |                   |                   |
| variable_pause_idle_timeout        | Valeur, en secondes, de l'activation du processus d'inactivité de la machine qui libère les moteurs et provoque la perte des coordonnées,**Une valeur élevée est conseillée afin que lors de l'activation de la macro PAUSE, il faille suffisamment de temps pour effectuer une action avant de perdre les coordonnées.** | nombre            | 43200             |

#### Inclinaison en Z

Tirer le meilleur parti de notre machine pour qu'elle s'auto-nivelle et veiller à ce que notre machine soit toujours dans les meilleures conditions est essentiel.

**Z-TILT est essentiellement un processus qui nous aide à aligner nos moteurs Z par rapport à notre axe/portique X (Cartésien) ou XY (CoreXY).**. avec ça**nous veillons à ce que notre Z soit toujours parfaitement aligné, précisément et automatiquement**.

| Variable                  | Description                                                                        | Valeurs possibles | Valeur par défaut |
| ------------------------- | ---------------------------------------------------------------------------------- | ----------------- | ----------------- |
| variable_calibrate_z_tilt | Permet, si activé dans notre configuration Klipper, le processus de réglage Z-Tilt | Vrai / Faux       | FAUX              |

#### Fausser

L'utilisation de[FAUSSER](broken-reference)Pour la correction ou l'ajustement précis de nos imprimantes, il est extrêmement conseillé si nous avons des écarts dans nos impressions. En utilisant la variable suivante, nous pouvons autoriser l'utilisation dans nos macros :

| Variable              | Description                                                                                                                                                                                                                    | Valeurs possibles | Valeur par défaut |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | ----------------- |
| variable_skew_profile | Cela nous permet de prendre en compte notre profil de biais qui sera chargé dans notre macro START_PRINT. Pour l'activer, nous devons décommenter la variable et utiliser le nom du profil asymétrique de notre configuration. | texte             | mon_skew_profile  |

### Personnalisation des macros

Notre module pour Klipper utilise le système de configuration modulaire utilisé dans RatOS et profite des avantages de Klipper dans le traitement séquentiel de ses fichiers de configuration. C'est pourquoi l'ordre des inclusions et des paramètres personnalisés que l'on souhaite appliquer à ces modules est essentiel.

> ℹ️**INFOS !!!**Lorsqu'elles sont utilisées en tant que module, les configurations 3Dwork NE PEUVENT PAS être modifiées directement à partir du répertoire 3dwork-klipper dans votre répertoire de configuration Klipper car elles seront en lecture seule pour des raisons de sécurité.
>
> C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules pour votre machine.

#### **Personnalisation des variables**

Normalement, ce sera ce que nous devrons ajuster, faire des ajustements aux variables que nous avons par défaut dans notre module**Travail 3D**para Falaises.

Simplement, il suffit de coller le contenu de la macro**[gcode_macro GLOBAL_VARS]**que l'on peut trouver dans macros/macros var_globals.cfg dans notre imprimante.cfg.

Nous vous rappelons ce que nous avons mentionné précédemment sur la façon dont Klipper traite les configurations de manière séquentielle, il est donc conseillé de le coller après les inclusions que nous avons mentionnées.[ici](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Nous aurons quelque chose comme ceci (c'est juste un exemple visuel) :

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

> ⚠️**Avis!!!**Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.

> ℹ️**INFOS !!!**
>
> -   Nous vous conseillons d'ajouter des commentaires comme vous le voyez dans le cas précédent pour identifier ce que fait chaque section.
> -   Bien qu'il ne soit pas nécessaire de toucher à toutes les variables, nous vous conseillons de copier tout le contenu de**[gcode_macro GLOBAL_VARS]**

#### Personnalisation des macros

Les macros ont été configurées de manière modulaire afin de pouvoir être facilement ajustées. Comme nous l'avons mentionné précédemment, si nous voulons les ajuster, nous devrons procéder de la même manière que pour les variables, copier la macro en question dans notre imprimante.cfg (ou une autre inclusion de notre choix) et nous assurer que c'est après l'inclusion où nous avons ajouté notre module 3Dwork pour Klipper.

Nous avons deux groupes de macros :

-   Macros pour ajouter des paramètres utilisateur, ces macros peuvent être facilement ajoutées et personnalisées car elles ont été ajoutées afin que tout utilisateur puisse personnaliser les actions à sa guise dans certaines parties des processus effectués par chaque macro.

**START_PRINT**

| Nombre Macro                              | Description                                                                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| \_USER_START_PRINT_HEAT_CHAMBER           | Il est exécuté juste après que notre enceinte commence à chauffer, si CHAMBER_TEMP est passé en paramètre à notre START_PRINT |
| \_USER_START_PRINT_BEFORE_HOMING          | Exécuté avant la prise d'origine initiale du début de l'impression                                                            |
| \_USER_START_PRINT_AFTER_HEATING_BED      | Il est exécuté lorsque notre lit atteint sa température, avant le \_START_PRINT_AFTER_HEATING_BED                             |
| \_USER\_ START_PRINT BED_MESH             | Lancé avant \_START_PRINT_BED_MESH                                                                                            |
| \_USER_START_PRINT_PARK                   | Lancé avant \_START_PRINT_PARK                                                                                                |
| \_USER_START_PRINT_AFTER_HEATING_EXTRUDER | Se lanza antes de \_START_PRINT_AFTER_HEATING_EXTRUDER                                                                        |

**END_PRINT**

| Nombre Macro                        | Description                                                                          |
| ----------------------------------- | ------------------------------------------------------------------------------------ |
| \_USER_END_PRINT_BEFORE_HEATERS_OFF | Il est exécuté avant d'éteindre les radiateurs, avant \_END_PRINT_BEFORE_HEATERS_OFF |
| \_USER_END_PRINT_AFTER_HEATERS_OFF  | Exécuté après l'arrêt des radiateurs, avant \_END_PRINT_AFTER_HEATERS_OFF            |
| \_USER_END_PRINT_PARK               | Exécuté avant le stationnement de la tête, avant le \_END_PRINT_PARK                 |

**PRINT_BASICS**

| Nombre Macro        | Description                  |
| ------------------- | ---------------------------- |
| \_USER_PAUSE_START  | Exécuté au début d'une PAUSE |
| \_USER_PAUSE_END    | Exécuté à la fin d'une PAUSE |
| \_USER_RESUME_START | Exécuté au début d'un RESUME |
| \_USER_RESUME_END   | Exécuté à la fin d'un CV     |

-   Les macros internes sont des macros permettant de diviser la macro principale en processus et sont importantes pour cela. Il est conseillé de copier tels quels si des ajustements sont nécessaires.

**START_PRINT**

| Nombre Macro                         | Description                                                                                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \_START_PRINT_HEAT_CHAMBER           | Chauffe le boîtier au cas où le paramètre CHAMBER_TEMP serait reçu par notre macro START_PRINT du laminateur                                                                                                 |
| \_START_PRINT_AFTER_HEATING_BED      | Il est exécuté lorsque le lit atteint la température, après \_USER_START_PRINT_AFTER_HEATING_BED. Normalement, il est utilisé pour traiter les calibrations du lit (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...) |
| \_START_PRINT_BED_MESH               | Il gère la logique de maillage du lit.                                                                                                                                                                       |
| \_START_PRINT_PARK                   | Garez la tête d'impression tout en chauffant la buse à la température d'impression.                                                                                                                          |
| \_START_PRINT_AFTER_HEATING_EXTRUDER | Purger la buse et charger le profil SKEW si celui-ci est défini dans les variables                                                                                                                           |

## Imprimantes et électronique

Comme nous travaillons avec différents modèles d'imprimantes et d'électronique, nous ajouterons ceux qui ne sont pas directement supportés par RatOS, qu'il s'agisse de contributions de notre part ou de la communauté.

-   imprimantes, dans ce répertoire nous aurons toutes les configurations d'imprimantes
-   cartes, nous trouverons ici les cartes électroniques

### Paramètres et broches

Notre module pour Klipper utilise le système de configuration modulaire utilisé dans RatOS et profite des avantages de Klipper dans le traitement séquentiel de ses fichiers de configuration. C'est pourquoi l'ordre des inclusions et des paramètres personnalisés que l'on souhaite appliquer à ces modules est essentiel.

> ℹ️**INFOS !!!**Lorsqu'elles sont utilisées en tant que module, les configurations 3Dwork NE PEUVENT PAS être modifiées directement à partir du répertoire 3dwork-klipper dans votre répertoire de configuration Klipper car elles seront en lecture seule pour des raisons de sécurité.
>
> C'est pourquoi il est très important de comprendre le fonctionnement de Klipper et comment personnaliser nos modules pour votre machine.

Comme nous l'avons expliqué dans "[personnalisation des macros](3dwork-klipper-bundle.md#personalizando-macros)"Nous utiliserons le même processus pour ajuster les paramètres ou les broches en fonction de nos besoins.

#### Paramètres de personnalisation

Tout comme nous vous conseillons de créer une section dans votre imprimante.cfg appelée USER OVERRIDES, placée après les inclusions de nos configurations, pour pouvoir ajuster et personnaliser n'importe quel paramètre utilisé dans celles-ci.

Dans l'exemple suivant, nous verrons comment dans notre cas nous souhaitons personnaliser les paramètres de notre nivellement de lit (bed_mesh) en ajustant les points de sonde (probe_count) par rapport à la configuration que nous avons par défaut dans les configurations de notre module Klipper :

**imprimante.cfg**

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

> ⚠️**Avis!!!**Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.

Nous pouvons utiliser ce même processus avec n’importe quel paramètre que nous souhaitons ajuster.

#### Personnalisation de la configuration des broches

Nous procéderons exactement comme nous l'avons fait précédemment, dans notre zone USER OVERRIDES, nous ajouterons les sections de broches que nous souhaitons ajuster à notre guise.

Dans l'exemple suivant, nous allons personnaliser la broche de notre ventilateur électronique (controller_fan) pour l'attribuer à une autre que celle par défaut :

**imprimante.cfg**

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

> ⚠️**Avis!!!**Les trois points (...) dans les exemples précédents ont simplement pour but d'indiquer que vous pouvez avoir plus de configurations entre les sections... en aucun cas il ne faut les ajouter.
