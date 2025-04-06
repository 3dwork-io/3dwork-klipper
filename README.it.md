# 3Dwork Klipper Bundle ![Italiano](https://flagcdn.com/w40/it.png)

## Pacchetto di macro, configurazioni e altri strumenti per Klipper

[![Español](https://flagcdn.com/w40/es.png)](README.md) [![English](https://flagcdn.com/w40/gb.png)](README.en.md) [![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md) [![Français](https://flagcdn.com/w40/fr.png)](README.fr.md) [![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ AVVERTENZA** > **GUIDA IN FASE DI SVILUPPO!!!** 
**<span style="color: red">Anche se le macro sono completamente funzionali, sono in continuo sviluppo.</span>**
**<span style="color: orange">Usale a tuo rischio e pericolo!!!</span>**

**Changelog**

07/12/2023 - Aggiunto supporto per automatizzare la creazione di firmware per l'elettronica Bigtreetech

Da **3Dwork** abbiamo raccolto e adattato un insieme di macro, configurazioni di macchine ed elettronica, così come altri strumenti per una gestione semplice e potente di Klipper.

Gran parte di questo pacchetto è basato su [**RatOS**](https://os.ratrig.com/) migliorando le parti che riteniamo interessanti, così come altri contributi della comunità.

## Installazione

Per installare il nostro pacchetto per Klipper seguiremo i seguenti passi

### Download del repository

Ci connetteremo al nostro host tramite SSH e lanceremo i seguenti comandi:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTA**
> Se la directory della tua configurazione di Klipper è personalizzata, ricorda di adattare il primo comando in modo appropriato alla tua installazione.

> **ℹ️ INFORMAZIONI PER NUOVE INSTALLAZIONI**
> Dato che Klipper non permette l'accesso alle macro senza un printer.cfg valido e una connessione a una MCU, possiamo usare questa configurazione temporanea:
>
> 1. Assicurati di avere l'[host come seconda MCU](raspberry-como-segunda-mcu.md)
> 2. Aggiungi questo printer.cfg base per abilitare le macro:

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

Questo permetterà di avviare Klipper e accedere alle macro.

### Usando Moonraker per essere sempre aggiornati

Grazie a Moonraker possiamo usare il suo update_manager per poter essere al passo con i miglioramenti che potremo introdurre in futuro.

Da Mainsail/Fluidd modificheremo il nostro moonraker.conf (dovrebbe trovarsi allo stesso livello del vostro printer.cfg) e aggiungeremo alla fine del file di configurazione:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ AVVERTENZA** > **Ricorda di fare il passo di installazione precedentemente, altrimenti Moonraker genererà un errore e non potrà avviarsi.**
>
> **D'altra parte, nel caso in cui la directory della tua configurazione di Klipper sia personalizzata, ricorda di adattare il percorso in modo appropriato alla tua installazione.**

## Macro

Abbiamo sempre commentato che RatOS è una delle migliori distribuzioni di Klipper, con supporto a Raspberry e ai moduli CB1, in gran parte per le sue configurazioni modulari e le sue eccellenti macro.

Alcune macro aggiunte che ci saranno utili:

### **Macro di uso generale**

| Macro                       | Descrizione                                                                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **MAYBE_HOME**              | Ci permette di ottimizzare il processo di homing eseguendolo solo su quegli assi che non sono già in home.                                                                                 |
| **PAUSE**                   | Mediante le variabili correlate ci permette di gestire una pausa con un parcheggio della testina più versatile rispetto alle macro normali.                                                |
| **SET_PAUSE_AT_LAYER**      |                                                                                                                                                                                            |
| **SET_PAUSE_AT_NEXT_LAYER** | Una macro molto utile che Mainsail integra nella sua UI per poter realizzare una pausa a richiesta in uno strato specifico... nel caso ci fossimo dimenticati di farlo durante lo slicing. |
|                             | Abbiamo anche un'altra macro per eseguire la pausa nel layer successivo.                                                                                                                   |
| **RESUME**                  | Migliorata poiché permette di rilevare se il nostro ugello non è alla temperatura di estrusione per poterlo risolvere prima che mostri un errore e danneggi la nostra stampa.              |
| **CANCEL_PRINT**            | Che permette l'uso del resto delle macro per realizzare una cancellazione della stampa correttamente.                                                                                      |

- **Pausa al cambio di layer**, macro molto interessanti che ci permettono di fare una pausa programmata in un layer o lanciare un comando all'inizio del layer successivo.  
  ![Funzione di pausa layer in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)
  Inoltre, un altro vantaggio di queste è che sono integrate con Mainsail, quindi avremo nuove funzioni nella nostra UI come potete vedere di seguito:
  ![Funzione di pausa layer in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macro di gestione della stampa**

| Macro           | Descrizione                                                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **START_PRINT** | Ci permetterà di poter iniziare le nostre stampe in modo sicuro e nello stile Klipper. All'interno di questa troveremo alcune funzioni interessanti come: |
|                 | • Preriscaldamento intelligente dell'ugello quando si utilizza un sensore di sonda                                                                        |
|                 | • Possibilità di utilizzo di z-tilt mediante variabile                                                                                                    |
|                 | • Mesh del letto adattiva, forzata o da una mesh salvata                                                                                                  |
|                 | • Linea di spurgo personalizzabile tra normale, linea di spurgo adattiva o goccia di spurgo                                                               |
|                 | • Macro segmentata per poter essere personalizzata come mostreremo più avanti                                                                             |
| **END_PRINT**   | Macro di fine stampa dove disponiamo anche di segmentazione per poter personalizzare la nostra macro. Abbiamo anche un parcheggio dinamico della testina. |

- **Mesh del letto adattiva**, grazie alla versatilità di Klipper possiamo fare cose che ad oggi sembrano impossibili... un processo importante per la stampa è avere una mesh delle deviazioni del nostro letto che ci permetta di correggerle per avere un'adesione perfetta dei primi strati.  
 In molte occasioni facciamo questa mesh prima delle stampe per assicurarci che funzioni correttamente e questa viene fatta su tutta la superficie del nostro letto.
Con la mesh del letto adattiva questa verrà realizzata nella zona di stampa, rendendola molto più precisa rispetto al metodo tradizionale... nelle seguenti immagini vedremo le differenze tra una mesh tradizionale e una adattiva.
<div style="display: flex; justify-content: space-between;">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
</div>

### **Macro di gestione del filamento**

Insieme di macro che ci permetteranno di gestire diverse azioni con il nostro filamento come il caricamento o lo scaricamento di questo.

| Macro               | Descrizione                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| **M600**            | Ci permetterà la compatibilità con il gcode M600 normalmente usato negli slicer per il cambio del filamento. |
| **UNLOAD_FILAMENT** | Configurabile mediante le variabili, ci permetterà uno scaricamento assistito dei filamenti.                 |
| **LOAD_FILAMENT**   | Come la precedente ma relativa al caricamento del filamento.                                                 |

### **Macro di gestione delle bobine di filamento (Spoolman)**

> **⚠️ AVVERTENZA** > **SEZIONE IN FASE DI SVILUPPO!!!**

[**Spoolman**](https://github.com/Donkie/Spoolman) è un gestore di bobine di filamento che si integra in Moonraker e che ci permette di gestire il nostro stock e la disponibilità di filamenti.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Non entreremo nell'installazione e configurazione di questo dato che è relativamente semplice utilizzando le [**istruzioni del suo Github**](https://github.com/Donkie/Spoolman)**,** in ogni caso **vi consigliamo di utilizzare Docker** per semplicità e ricordate di **attivare la configurazione in Moonraker** richiesta:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro              | Descrizione                                                |
| ------------------ | ---------------------------------------------------------- |
| SET_ACTIVE_SPOOL   | Ci permette di indicare quale è l'ID della bobina da usare |
| CLEAR_ACTIVE_SPOOL | Ci permette di resettare la bobina attiva                  |

L'ideale in ogni caso sarebbe aggiungere nel nostro slicer, **nei gcode di filamenti per ogni bobina la chiamata a questa**, e ricorda di **cambiare l'ID di questa una volta consumata** per poter tenere un controllo di quanto filamento resta nella stessa!!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Macro di gestione delle superfici di stampa**

> **⚠️ AVVERTENZA** > **SEZIONE IN FASE DI SVILUPPO!!!**

È normale avere diverse superfici di stampa a seconda della finitura che vogliamo ottenere o del tipo di filamento.

Questo insieme di macro, create da [Garethky](https://github.com/garethky), ci permetteranno di avere un controllo di queste e in particolare la corretta regolazione dello ZOffset in ciascuna di esse nello stile che abbiamo nelle macchine Prusa. Di seguito potete vedere alcune delle loro funzioni:

- potremo memorizzare il numero di superfici di stampa che vogliamo, avendo ciascuna un nome unico
- ogni superficie di stampa avrà un proprio ZOffset
- se facciamo aggiustamenti di Z durante una stampa (Babystepping) dal nostro Klipper, questo cambiamento verrà memorizzato nella superficie abilitata in quel momento

D'altra parte abbiamo alcuni **requisiti per implementarlo (si cercherà di aggiungerlo nella logica del PRINT_START del bundle in futuro attivando questa funzione tramite variabile e creando una macro utente precedente e successiva per poter inserire eventi utente)**:

- è necessario l'uso di **[save_variables]**, nel nostro caso useremo ~/variables.cfg per memorizzare le variabili e che è già all'interno del cfg di queste macro.  
  Questo creerà automaticamente un file variables_build_sheets.cfg dove salverà le nostre variabili su disco.

**Esempio di file di configurazione delle variabili**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

- dovremo includere una chiamata a APPLY_BUILD_SHEET_ADJUSTMENT nel nostro PRINT_START per poter applicare lo ZOffset della superficie selezionata
- è importante che affinché la macro precedente, APPLY_BUILD_SHEET_ADJUSTMENT, funzioni correttamente dobbiamo aggiungere un SET_GCODE_OFFSET Z=0.0 appena prima di chiamare APPLY_BUILD_SHEET_ADJUSTMENT

```
# Load build sheet
SHOW_BUILD_SHEET ; show loaded build sheet on console
SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset
```

D'altra parte è interessante poter disporre di macro per attivare una superficie o un'altra o anche passarlo come parametro dal nostro slicer per poter caricare una o l'altra automaticamente con diversi profili di stampante o di filamento:

> **⚠️ AVVERTENZA**
> È importante che il valore in NAME="xxxx" coincida con il nome che abbiamo dato al momento dell'installazione della nostra superficie di stampa

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

Anche nel caso in cui si disponga di KlipperScreen, potremo aggiungere un menu specifico per poter gestire il caricamento delle diverse superfici, dove includeremo una chiamata alle macro precedentemente create per il caricamento di ogni superficie:

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

| Macro                        | Descrizione |
| ---------------------------- | ----------- |
| INSTALL_BUILD_SHEET          |             |
| SHOW_BUILD_SHEET             |             |
| SHOW_BUILD_SHEETS            |             |
| SET_BUILD_SHEET_OFFSET       |             |
| RESET_BUILD_SHEET_OFFSET     |             |
| SET_GCODE_OFFSET             |             |
| APPLY_BUILD_SHEET_ADJUSTMENT |             |

### **Macro di configurazione della macchina**

| Macro                                                 | Descrizione                                                                                                                                                                                                                       |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILE_FIRMWARE**                                  | Con questa macro potremo compilare il firmware Klipper in modo semplice, avere il firmware accessibile dalla UI per maggiore semplicità e poterlo applicare alla nostra elettronica.                                              |
| Qui avete più dettagli sulle elettroniche supportate. |                                                                                                                                                                                                                                   |
| **CALCULATE_BED_MESH**                                | Una macro estremamente utile per calcolare l'area per la nostra mesh perché a volte può risultare un processo complicato.                                                                                                         |
| **PID_ALL**                                           |                                                                                                                                                                                                                                   |
| **PID_EXTRUDER**                                      |                                                                                                                                                                                                                                   |
| **PID_BED**                                           | Queste macro, dove possiamo passare le temperature per il PID sotto forma di parametri, ci permetteranno di poter realizzare la calibrazione della temperatura in modo estremamente semplice.                                     |
| **TEST_SPEED**                                        |                                                                                                                                                                                                                                   |
| **TEST_SPEED_DELTA**                                  | Macro originale del collega [Ellis](https://github.com/AndrewEllis93) che ci permetteranno in modo abbastanza semplice di testare la velocità a cui possiamo muovere la nostra macchina in modo preciso e senza perdita di passi. |

\*\_ **Compilazione del firmware per elettroniche supportate**, per facilitare il processo di creazione e manutenzione del nostro firmware Klipper per le nostre MCU contiamo sulla macro COMPILE_FIRMWARE che quando eseguita, possiamo usare come parametro la nostra elettronica per fare solo questa, compilerà Klipper per tutte le elettroniche supportate dal nostro bundle:
![Opzioni di compilazione del firmware](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)
Troveremo queste accessibili in modo semplice dalla nostra UI web nella directory firmware_binaries nella nostra scheda MACHINE (se usiamo Mainsail):
![Firmware binari accessibili dall'UI di Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)
Di seguito avete la lista delle elettroniche supportate:

> ⚠️ **IMPORTANTE!!!**
>
> questi script sono preparati per funzionare su un >sistema Raspbian con utente pi, se non è il tuo caso dovrai adattarlo.
>
> i firmware sono generati per l'uso con connessione USB che è sempre quello che consigliamo, inoltre il punto di montaggio USB è sempre lo stesso quindi la vostra configurazione della connessione della vostra MCU non cambierà se vengono generati con la nostra macro/script
>
> **Affinché Klipper possa eseguire shell macro è necessario installare un'estensione, grazie al collega** [**Arksine**](https://github.com/Arksine)**, che lo permetta.**
>
> **A seconda della distro di Klipper utilizzata potrebbero essere già abilitate.**
>
> ![Installazione dell'estensione shell command](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> Il modo più semplice è usando [**Kiauh**](../instalacion/#instalando-kiauh) dove troveremo in una delle sue opzioni la possibilità di installare questa estensione:
>
> ![Installazione dell'estensione shell command](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Possiamo anche eseguire il processo manualmente copiando manualmente il plugin per Klipper <[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py) all'interno della nostra directory `_**~/klipper/klippy/extras**_` usando SSH o SCP e riavviando Klipper.

| Elettronica        | Nome del parametro da usare nella macro |
| ------------------ | --------------------------------------- |
| Manta E3 EZ        | btt-manta-e3ez                          |
| Manta M4P          | btt-manta-m4p                           |
| Manta M4P v2.2     | btt-manta-m4p-22                        |
| Manta M8P          | btt-manta-m8p                           |
| Manta M8P v1.1     | btt-manta-m8p-11                        |
| Octopus Max EZ     | btt-octopus-max-ez                      |
| Octopus Pro (446)  | btt-octopus-pro-446                     |
| Octopus Pro (429)  | btt-octopus-pro-429                     |
| Octopus Pro (H723) | btt-octopus-pro-h723                    |
| Octopus v1.1       | btt-octopus-11                          |
| Octopus v1.1 (407) | btt-octopus-11-407                      |
| SKR Pro v1.2       | skr_pro_12                              |
| SKR 3              | btt_skr_3                               |
| SKR 3 (H723)       | btt-skr-3-h723                          |
| SKR 3 EZ           | btt-skr-3-ez                            |
| SKR 3 EZ (H723)    | btt-skr-3-ez-h723                       |
| SKR 2 (429)        | btt-skr-2-429                           |
| SKR 2 (407)        | btt-skr-2-407                           |
| SKR RAT            | btt-skrat-10                            |
| SKR 1.4 Turbo      | btt-skr-14-turbo                        |
| SKR Mini E3 v3     | btt_skr_mini_e3_30                      |

| Toolhead (CAN) | Nome del parametro da usare nella macro |
| -------------- | --------------------------------------- |
| EBB42 v1       | btt_ebb42_10                            |
| EBB36 v1       | btt_ebb36_10                            |
| EBB42 v1.1     | btt_ebb42_11                            |
| EBB36 v1.1     | btt_ebb36_11                            |
| EBB42 v1.2     | btt_ebb42_12                            |
| EBB36 v1.2     | btt_ebb36_12                            |

| **Elettronica**      | **Nome del parametro da usare nella macro** |
| -------------------- | ------------------------------------------- |
| MKS Eagle v1.x       | mks-eagle-10                                |
| MKS Robin Nano v3    | mks-robin-nano-30                           |
| MKS Robin Nano v2    | mks-robin-nano-20                           |
| MKS Gen L            | mks-gen-l                                   |
| ZNP Robin Nano DW v2 | znp_robin_nano_dw_v2                        |

| Toolhead (CAN)    | Nome del parametro da usare nella macro |
| ----------------- | --------------------------------------- |
| Mellow FLY SHT 42 | mellow_fly_sht_42                       |
| Mellow FLY SHT 36 | mellow_fly_sht_36                       |

| Elettronica   | Nome del parametro da usare nella macro |
| ------------- | --------------------------------------- |
| Fysetc Spider | fysetc_spider                           |

| Elettronica         | Nome del parametro da usare nella macro |
| ------------------- | --------------------------------------- |
| Artillery Ruby v1.x | artillery-ruby-12                       |

| Elettronica           | Nome del parametro da usare nella macro |
| --------------------- | --------------------------------------- |
| Raspberry Pico/RP2040 | rpi-rp2040                              |

| Elettronica    | Nome del parametro da usare nella macro |
| -------------- | --------------------------------------- |
| Leviathan v1.2 | leviathan-12                            |

### Aggiungere le macro 3Dwork alla nostra installazione

Dalla nostra interfaccia, Mainsail/Fluidd, modificheremo il nostro printer.cfg e aggiungeremo:

**printer.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️ **INFO!!!**
> È importante aggiungere queste righe alla fine del nostro file di configurazione... appena sopra la sezione in modo che nel caso esistano macro nel nostro cfg o include, queste vengano sovrascritte dalle nostre:
> #\*# \<--- SAVE_CONFIG --->

> ⚠️ **IMPORTANTE!!!**
> Le macro normali sono state separate dalle **macro shell** poiché **per abilitare queste è necessario eseguire passaggi aggiuntivi manualmente oltre al fatto che sono attualmente in fase di test** e **potrebbero richiedere permessi extra per attribuire permessi di esecuzione per i quali non sono state fornite istruzioni poiché si sta cercando di automatizzare.**
> **Se le utilizzi è sotto la tua responsabilità.**

### Configurazione del nostro slicer

Poiché le nostre macro sono dinamiche, estrarranno alcune informazioni dalla nostra configurazione della stampante e dallo slicer stesso. Per questo ti consigliamo di configurare i tuoi slicer nel seguente modo:

- **gcode di avvio START_PRINT**, utilizzando placeholder per passare i valori di temperatura del filamento e del letto in modo dinamico:

**PrusaSlicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer** - abbiamo l'opzione di poter regolare la temperatura della camera (CHAMBER)

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Esempio per PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

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

> ⚠️ **Avviso!!!**
> Dovremo installare il plugin [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff) dal menu _**Help/Show**_ configuration Folder... copieremo lo script dal link precedente nella cartella script.  
> Riavviamo Cura e andremo su _**Extensions/Post processing/Modify G-Code**_ e selezioneremo _**Mesh Print Size**_.

**IdeaMaker**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplify3D**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️ **INFO!!!**
> I **placeholder sono degli "alias" o variabili che gli slicer usano in modo che al momento di generare il gcode vengano sostituiti con i valori configurati nel profilo** di stampa.
>
> Nei seguenti link puoi trovare un elenco di questi per: [**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (oltre a quelli del precedente), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list) e [**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> L'uso di questi permette che le nostre macro siano dinamiche.

- **gcode di fine END_PRINT**, in questo caso non utilizzando placeholder è comune a tutti gli slicer

```ini
END_PRINT
```

### Variabili

Come abbiamo già commentato, queste nuove macro ci permetteranno di disporre di alcune funzioni molto utili come elencato in precedenza.

Per adattarle alla nostra macchina utilizzeremo le variabili che troveremo in macros/macros_var_globals.cfg e che dettagliamo di seguito.

#### Lingua dei messaggi/notifiche

Poiché a molti utenti piace avere le notifiche delle macro nella propria lingua, abbiamo ideato un sistema di notifiche multilingua, attualmente spagnolo (es) e inglese (en). Nella seguente variabile potremo regolarlo:

| Variabile         | Descrizione                                                                                                        | Valori possibili | Valore predefinito |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------ |
| variable_language | Ci permette di selezionare la lingua delle notifiche. Nel caso non sia ben definito, verrà utilizzato en (inglese) | es / en          | es                 |

#### Estrusione Relativa

Permette di controllare quale modalità di estrusione useremo al termine del nostro START_PRINT. Il valore dipenderà dalla configurazione del nostro slicer.

> 💡 **Consiglio**
> È consigliabile configurare il tuo slicer per l'uso dell'estrusione relativa e impostare questa variabile su True.

| Variabile                   | Descrizione                                                                     | Valori possibili | Valore predefinito |
| --------------------------- | ------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_relative_extrusion | Ci permette di indicare la modalità di estrusione utilizzata nel nostro slicer. | True / False     | True               |

#### Velocità

Per gestire le velocità utilizzate nelle macro.

| Variabile                   | Descrizione                           | Valori possibili | Valore predefinito |     |
| --------------------------- | ------------------------------------- | ---------------- | ------------------ | --- |
| variable_macro_travel_speed | Velocità negli spostamenti            | numerico         | 150                |     |
| variable_macro_z_speed      | Velocità negli spostamenti per asse Z | numerico         | 15                 |     |

#### Homing

Insieme di variabili relative al processo di homing.

| Variabile | Descrizione | Valori possibili | Valore predefinito |
| --------- | ----------- | ---------------- | ------------------ |

#### Riscaldamento

Variabili relative al processo di riscaldamento della nostra macchina.

| Variabile                                  | Descrizione                                                                                         | Valori possibili | Valore predefinito |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_preheat_extruder                  | Abilita il preriscaldamento dell'ugello alla temperatura indicata in variable_preheat_extruder_temp | True / False     | True               |
| variable_preheat_extruder_temp             | Temperatura di preriscaldamento dell'ugello                                                         | numerico         | 150                |
| variable_start_print_heat_chamber_bed_temp | Temperatura del letto durante il processo di riscaldamento della nostra camera                      | numerico         | 100                |

> 💡 **Consiglio**
> Benefici dell'utilizzo del preriscaldamento dell'ugello:

- ci permette un tempo aggiuntivo affinché il letto possa raggiungere la sua temperatura in modo uniforme
- se usiamo un sensore induttivo che non ha compensazione di temperatura, ci permetterà di avere misurazioni più consistenti e precise
- permette di ammorbidire qualsiasi residuo di filamento nell'ugello, il che consente, in determinate configurazioni, che questi residui non influenzino l'attivazione del sensore
  {% endhint %}

#### Mesh del letto (Bed Mesh)

Per controllare il processo di livellamento abbiamo variabili che possono essere molto utili. Ad esempio, potremo controllare il tipo di livellamento che vogliamo utilizzare creando sempre una nuova mesh, caricandone una salvata in precedenza o utilizzando una mesh adattiva.

| Variabile                                                                                                                | Descrizione                                                                 | Valori possibili | Valore predefinito |
| ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_calibrate_bed_mesh                                                                                              | Ci permette di selezionare che tipo di mesh useremo nel nostro START_PRINT: |                  |                    |
| - new mesh, ci farà una mesh in ogni stampa                                                                              |                                                                             |                  |                    |
| - storedmesh, caricherà una mesh salvata e non eseguirà il sondaggio del letto                                           |                                                                             |                  |                    |
| - adaptative, ci farà una nuova mesh ma adattata all'area di stampa migliorando in molte occasioni i nostri primi strati |                                                                             |                  |                    |
| \- nomesh, nel caso in cui non abbiamo un sensore o utilizziamo mesh per saltare il processo                             | newmesh / storedmesh / adaptative /                                         |                  |                    |
| nomesh                                                                                                                   | adaptative                                                                  |                  |                    |
| variable_bed_mesh_profile                                                                                                | Il nome usato per la nostra mesh salvata                                    | testo            | default            |

> ⚠️ **Avviso!!!**
> Ti consigliamo di utilizzare il livellamento adaptative poiché adatterà sempre la mesh alle dimensioni della tua stampa permettendo di avere un'area di mesh regolata.
>
> È importante che nel nostro [gcode di inizio del nostro slicer](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), nella chiamata al nostro START_PRINT, ci siano i valori PRINT_MAX e PRINT_MIN.

#### Spurgo

Una fase importante del nostro inizio di stampa è un corretto spurgo del nostro ugello per evitare residui di filamento o che questi possano danneggiare la nostra stampa in qualche momento. Di seguito trovi le variabili che intervengono in questo processo:
| Variabile | Descrizione | Valori possibili | Valore predefinito |
| --- | --- | --- | --- |
| variable_nozzle_priming | Possiamo scegliere tra diverse opzioni di spurgo:<br>- primeline: disegna la tipica linea di spurgo<br>- primelineadaptative: genera una linea di spurgo adattata all'area di stampa usando variable_nozzle_priming_objectdistance come margine<br>- primeblob: fa una goccia di filamento in un angolo del letto | primeline / primelineadaptative / primeblob / False | primelineadaptative |
| variable_nozzle_priming_objectdistance | Se usiamo la linea di spurgo adattativa sarà il margine da utilizzare tra la linea di spurgo e l'oggetto stampato | numerico | 5 |
| variable_nozzle_prime_start_x | Dove posizionare la nostra linea di spurgo in X:<br>- min: X=0 (più margine di sicurezza)<br>- max: X=max (meno margine di sicurezza)<br>- numero: coordinata X specifica | min / max / numero | max |
| variable_nozzle_prime_start_y | Dove posizionare la nostra linea di spurgo in Y:<br>- min: Y=0 (più margine di sicurezza)<br>- max: Y=max (meno margine di sicurezza)<br>- numero: coordinata Y specifica | min / max / numero | min |
| variable_nozzle_prime_direction | Direzione della linea o goccia:<br>- backwards: verso il frontale<br>- forwards: verso il retro<br>- auto: verso il centro secondo variable_nozzle_prime_start_y | auto / forwards / backwards | auto |

#### Caricamento/Scaricamento del filamento

In questo caso questo gruppo di variabili ci faciliterà la gestione del caricamento e scaricamento del nostro filamento utilizzato in emulazione del M600 per esempio o quando si lanciano le macro di caricamento e scaricamento del filamento:

| Variabile                       | Descrizione                                                                                                                                                                                                                                                                                                                                                                                           | Valori possibili | Valore predefinito |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_filament_unload_length | Quanto retrarre in mm il filamento, regolare alla tua macchina, normalmente la misura dal tuo ugello agli ingranaggi del tuo estrusore aggiungendo un margine extra.                                                                                                                                                                                                                                  | numero           | 130                |
| variable_filament_unload_speed  | Velocità di retrazione del filamento in mm/sec normalmente si usa una velocità lenta.                                                                                                                                                                                                                                                                                                                 | numero           | 5                  |
| variable_filament_load_length   | Distanza in mm per caricare il nuovo filamento... come in variable_filament_unload_length useremo la misura dal tuo ingranaggio all'estrusore aggiungendo un margine extra, in questo caso questo valore extra dipenderà da quanto vuoi che venga spurgato... normalmente puoi dargli più margine rispetto al valore precedente per assicurarti che l'estrusione del filamento precedente sia pulita. | numero           | 150                |
| variable_filament_load_speed    | Velocità di caricamento del filamento in mm/sec normalmente si usa una velocità più veloce di quella di scaricamento.                                                                                                                                                                                                                                                                                 | numero           | 10                 |

> ⚠️ **Avviso!!!**
> Un'altra regolazione necessaria per la tua sezione **[extruder]** è indicare il [**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... il valore consigliabile è solitamente >101 (in caso non sia definito usa 50) per esempio per permettere i tipici test di calibrazione dell'estrusore.  
> Dovresti regolare il valore in base a quanto commentato precedentemente del test o la configurazione del tuo **variable_filament_unload_length** e/o **variable_filament_load_length**.

#### Parcheggio

In determinati processi della nostra stampante, come la pausa, è consigliabile fare un parcheggio della nostra testina. Le macro del nostro bundle dispongono di questa opzione oltre alle seguenti variabili per gestire:

| Variabile                          | Descrizione                                                                                                                                                                                                                                                                                          | Valori possibili | Valore predefinito |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_start_print_park_in       | Posizione dove parcheggiare la testina durante il preriscaldamento.                                                                                                                                                                                                                                  | back /           |                    |
| center /                           |                                                                                                                                                                                                                                                                                                      |                  |                    |
| front                              | back                                                                                                                                                                                                                                                                                                 |                  |                    |
| variable_start_print_park_z_height | Altezza in Z durante il preriscaldamento                                                                                                                                                                                                                                                             | numero           | 50                 |
| variable_end_print_park_in         | Posizione dove parcheggiare la testina al termine o annullamento di una stampa.                                                                                                                                                                                                                      | back /           |                    |
| center /                           |                                                                                                                                                                                                                                                                                                      |                  |                    |
| front                              | back                                                                                                                                                                                                                                                                                                 |                  |                    |
| variable_end_print_park_z_hop      | Distanza da sollevare in Z al termine della stampa.                                                                                                                                                                                                                                                  | numero           | 20                 |
| variable_pause_print_park_in       | Posizione dove parcheggiare la testina quando si mette in pausa la stampa.                                                                                                                                                                                                                           | back /           |                    |
| center /                           |                                                                                                                                                                                                                                                                                                      |                  |                    |
| front                              | back                                                                                                                                                                                                                                                                                                 |                  |                    |
| variable_pause_idle_timeout        | Valore, in secondi, dell'attivazione del processo di inattività nella macchina che libera i motori e fa perdere le coordinate, **è consigliabile un valore alto in modo che quando si attiva la macro PAUSE ci sia tempo sufficiente per eseguire qualsiasi azione prima di perdere le coordinate.** | numero           | 43200              |

#### Z-Tilt

Sfruttare al massimo la nostra macchina affinché si autolivelli e facilitare che la nostra macchina sia sempre nelle migliori condizioni è fondamentale.

**Z-TILT è fondamentalmente un processo che ci aiuta ad allineare i nostri motori Z rispetto al nostro asse/gantry X (cartesiana) o XY (CoreXY)**. Con questo **assicuriamo di avere sempre il nostro Z perfettamente allineato in modo preciso e automatico**.

| Variabile                 | Descrizione                                                                                                | Valori possibili | Valore predefinito |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_calibrate_z_tilt | Permette, nel caso sia abilitato nella nostra configurazione di Klipper, il processo di regolazione Z-Tilt | True / False     | False              |

#### Skew

L'uso di [SKEW](broken-reference) per la correzione o regolazione precisa delle nostre stampanti è estremamente consigliabile se abbiamo deviazioni nelle nostre stampe. Usando la seguente variabile possiamo permettere l'uso nelle nostre macro:

| Variabile             | Descrizione                                                                                                                                                                                                       | Valori possibili | Valore predefinito |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variable_skew_profile | Permette di tenere conto del nostro profilo skew che verrà caricato nella nostra macro START_PRINT. Per attivarlo dovremo decommentare la variabile e usare il nome del profilo skew della nostra configurazione. | testo            | my_skew_profile    |

### Personalizzazione delle macro

Il nostro modulo per Klipper utilizza il sistema di configurazione modulare impiegato in RatOS e che sfrutta i vantaggi di Klipper nell'elaborazione sequenziale dei file di configurazione. Per questo è fondamentale l'ordine degli include e delle regolazioni personalizzate che vogliamo applicare su questi moduli.

> ℹ️ **INFO!!!**
> Essendo utilizzato come un modulo, le configurazioni di 3Dwork NON possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della tua directory di configurazione di Klipper poiché sarà in read-only (limitato alla sola lettura) per sicurezza.
>
> Per questo è molto importante capire il funzionamento di Klipper e come poter personalizzare i nostri moduli alla tua macchina.

#### **Personalizzazione delle variabili**

Normalmente, sarà ciò che dovremo regolare, per effettuare regolazioni sulle variabili che abbiamo di default nel nostro modulo **3Dwork** per Klipper.

Semplicemente, quello che dobbiamo fare è incollare il contenuto della macro **[gcode_macro GLOBAL_VARS]** che potremo trovare in macros/macros_var_globals.cfg nel nostro printer.cfg.

Ti ricordiamo quanto commentato precedentemente su come Klipper elabora le configurazioni in modo sequenziale, quindi è consigliabile incollarlo dopo gli include che ti abbiamo commentato [qui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Ci rimarrà qualcosa del genere (è solo un esempio visivo):

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

> ⚠️ **Avviso!!!**
> I tre puntini (...) degli esempi precedenti servono solo per indicare che puoi avere più configurazioni tra le sezioni... in nessun caso devono essere inseriti.

> ℹ️ **INFO!!!**
>
> - ti consigliamo di aggiungere commenti come vedi nel caso precedente per identificare cosa fa ogni sezione
> - anche se non hai bisogno di modificare tutte le variabili, ti consigliamo di copiare tutto il contenuto di **[gcode_macro GLOBAL_VARS]**

#### Personalizzazione delle macro

Le macro sono state strutturate in modo modulare in modo che possano essere regolate in modo semplice. Come ti abbiamo commentato precedentemente, se vogliamo regolarle dovremo procedere allo stesso modo di come abbiamo fatto con le variabili, copiare la macro in questione nel nostro printer.cfg (o un altro include nostro) e assicurarci che sia dopo l'include dove aggiungiamo il nostro modulo 3Dwork per Klipper.

Abbiamo due gruppi di macro:

- Macro per aggiungere regolazioni utente, queste macro possono essere aggiunte e personalizzate facilmente perché sono state aggiunte in modo che qualsiasi utente possa personalizzare le azioni a suo piacimento in determinate parti dei processi che ogni macro esegue.

**START_PRINT**

| Nome Macro                                | Descrizione                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| \_USER_START_PRINT_HEAT_CHAMBER           | Si esegue subito dopo che la nostra camera inizia a riscaldarsi, se CHAMBER_TEMP viene passato come parametro al nostro START_PRINT |
| \_USER_START_PRINT_BEFORE_HOMING          | Si esegue prima dell'homing iniziale di inizio stampa                                                                               |
| \_USER_START_PRINT_AFTER_HEATING_BED      | Si esegue quando il nostro letto raggiunge la sua temperatura, prima di \_START_PRINT_AFTER_HEATING_BED                             |
| \_USER_START_PRINT_BED_MESH               | Si lancia prima di \_START_PRINT_BED_MESH                                                                                           |
| \_USER_START_PRINT_PARK                   | Si lancia prima di \_START_PRINT_PARK                                                                                               |
| \_USER_START_PRINT_AFTER_HEATING_EXTRUDER | Si lancia prima di \_START_PRINT_AFTER_HEATING_EXTRUDER                                                                             |

**END_PRINT**

| Nome Macro                          | Descrizione                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------- |
| \_USER_END_PRINT_BEFORE_HEATERS_OFF | Si esegue prima di spegnere i riscaldatori, prima di \_END_PRINT_BEFORE_HEATERS_OFF    |
| \_USER_END_PRINT_AFTER_HEATERS_OFF  | Si esegue dopo lo spegnimento dei riscaldatori, prima di \_END_PRINT_AFTER_HEATERS_OFF |
| \_USER_END_PRINT_PARK               | Si esegue prima del parcheggio della testina, prima di \_END_PRINT_PARK                |

**PRINT_BASICS**

| Nome Macro          | Descrizione                       |
| ------------------- | --------------------------------- |
| \_USER_PAUSE_START  | Si esegue all'inizio di un PAUSE  |
| \_USER_PAUSE_END    | Si esegue alla fine di un PAUSE   |
| \_USER_RESUME_START | Si esegue all'inizio di un RESUME |
| \_USER_RESUME_END   | Si esegue alla fine di un RESUME  |

- Macro interne, sono macro per dividere la macro principale in processi ed è importante per questo. È consigliabile che in caso sia necessario regolare queste, vengano copiate così come sono.

**START_PRINT**

| Nome Macro                           | Descrizione                                                                                                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_START_PRINT_HEAT_CHAMBER           | Riscalda la camera nel caso in cui il parametro CHAMBER_TEMP venga ricevuto dalla nostra macro START_PRINT dallo slicer                                                                                                |
| \_START_PRINT_AFTER_HEATING_BED      | Si esegue quando il letto raggiunge la temperatura, dopo \_USER_START_PRINT_AFTER_HEATING_BED. Normalmente, viene utilizzato per l'elaborazione delle calibrazioni del letto (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...) |
| \_START_PRINT_BED_MESH               | Si occupa della logica di mesh del letto.                                                                                                                                                                              |
| \_START_PRINT_PARK                   | Parcheggia la testina di stampa mentre riscalda l'ugello alla temperatura di stampa.                                                                                                                                   |
| \_START_PRINT_AFTER_HEATING_EXTRUDER | Esegue lo spurgo dell'ugello e carica il profilo SKEW nel caso in cui lo definiamo nelle variabili                                                                                                                     |

## Stampanti ed elettroniche

Man mano che lavoriamo con diversi modelli di stampanti ed elettroniche, aggiungeremo quelli che non sono direttamente supportati da RatOS, siano essi nostri contributi o della comunità.
* printers, in questa directory avremo tutte le configurazioni delle stampanti
* boards, qui troveremo quelle delle elettroniche

### Parametri e pin

Il nostro modulo per Klipper utilizza il sistema di configurazione modulare impiegato in RatOS che sfrutta i vantaggi di Klipper nell'elaborazione sequenziale dei file di configurazione. Per questo è fondamentale l'ordine degli include e delle regolazioni personalizzate che vogliamo applicare su questi moduli.

> ℹ️ **INFO!!!**
>Essendo utilizzato come un modulo, le configurazioni di 3Dwork NON possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della tua directory di configurazione di Klipper poiché sarà in read-only (limitato alla sola lettura) per sicurezza.
>
>Per questo è molto importante capire il funzionamento di Klipper e come poter personalizzare i nostri moduli alla tua macchina.

Come spiegato in "[personalizzazione delle macro](3dwork-klipper-bundle.md#personalizando-macros)" useremo lo stesso processo per regolare parametri o pin per adattarli alle nostre necessità.

#### Personalizzazione dei parametri

Come ti consigliamo di creare una sezione nel tuo printer.cfg chiamata USER OVERRIDES, posizionata dopo gli include alle nostre configurazioni, per poter regolare e personalizzare qualsiasi parametro utilizzato in essi.

Nel seguente esempio vedremo come nel nostro caso siamo interessati a personalizzare i parametri del nostro livellamento del letto (bed_mesh) regolando i punti di sondaggio (probe_count) rispetto alla configurazione che abbiamo di default nelle configurazioni del nostro modulo Klipper:

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

> ⚠️ **Avvertenza!!!**
>I tre puntini (...) degli esempi precedenti servono solo per indicare che puoi avere più configurazioni tra le sezioni... in nessun caso devono essere inseriti.

Possiamo utilizzare questo stesso processo con qualsiasi parametro che vogliamo regolare.

#### Personalizzazione della configurazione dei pin

Procederemo esattamente come abbiamo fatto in precedenza, nella nostra zona USER OVERRIDES aggiungeremo quelle sezioni di pin che vogliamo regolare a nostro piacimento.

Nel seguente esempio personalizzeremo quale è il pin della nostra ventola dell'elettronica (controller_fan) per assegnarlo a uno diverso da quello predefinito:
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
> ⚠️ **Avvertenza!!!**
>I tre puntini (...) degli esempi precedenti servono solo per indicare che puoi avere più configurazioni tra le sezioni... in nessun caso devono essere inseriti.
