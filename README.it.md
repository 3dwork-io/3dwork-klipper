# Pacchetto clope 3dwork![Italiano](https://flagcdn.com/w40/it.png)

## Pacchetto Macros, configurazioni e altre utility per Klipper

[![English](https://flagcdn.com/w40/gb.png)](README.en.md)[![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md)[![Español](https://flagcdn.com/w40/es.png)](README.md)[![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)[![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ Avvertenza****Guida nel processo !!!****<span style="color: red">Sebbene le macro siano totalmente funzionali, sono in sviluppo continuo.</span>****<span style="color: orange">Usali sotto la tua stessa responsabilità !!!</span>**

Changelog

12/07/2023 - Aggiunto supporto per automatizzare la creazione di firmware per BigRetech Electronics

Da**3dwork**Abbiamo compilato e regolato un set di macro, macchine e configurazioni elettroniche, nonché altri strumenti per una gestione semplice e potente di Klipper.

Gran parte di questo pacchetto si basa su[**Ratti**](https://os.ratrig.com/)Migliorare le parti che crediamo interessanti e altri contributi della comunità.

## Installazione

Per installare il nostro pacchetto per Klipper seguiremo i seguenti passaggi

### Scarico del repository

Ci connetteremo al nostro host di SSH e avviremo i seguenti comandi:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTA**Se la directory della configurazione di Klipper è personalizzata, ricorda di regolare correttamente il primo comando all'installazione.

> **ℹ️ Informazioni per nuove strutture**Poiché Klipper non consente l'accesso alle macro senza una stampante valida.
>
> 1.  Assicurati di avere il[Ospita come secondo MCU](raspberry-como-segunda-mcu.md)
> 2.  Aggiungi questa stampante di base.cfg per abilitare le macro:

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

Ciò consentirà a Klipper di iniziare e accedere alle macro.

### Usando Moonraker per essere sempre aggiornato

Grazie a Moonraker possiamo usare il suo update_manager per poter essere aggiornati con i miglioramenti che possiamo introdurre in futuro.

Da mainsail/fluidd modificheremo il nostro moonraker.conf (dovrebbe essere alla stessa altezza della tua stampante.cfg) e aggiungeremo alla fine del file di configurazione:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ Avvertenza****Ricorda di fare il passaggio di installazione in precedenza se non si genera un errore e non sarai in grado di avviare.**
>
> **D'altra parte, nel caso in cui la directory di configurazione di Klipper sia personalizzata, ricorda di regolare correttamente il percorso alla tua installazione.**

## Macro

Abbiamo sempre commentato che Times è una delle migliori distribuzioni di Klipper, con supporto Raspberry e moduli CB1, in gran parte a causa delle sue configurazioni modulari e delle sue grandi macro.

Alcune macro aggiunte che saranno utili:

### **Macro per uso generale**

| Macro                       | Descrizione                                                                                                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Forse_home**              | Ci consente di ottimizzare il processo di homing solo facendo questo in quegli assi che non sono con l'homing.                                                                                             |
| **PAUSA**                   | Attraverso variabili correlate ci consente di gestire una pausa con un parcheggio più versatile che le normali macro.                                                                                      |
| **Set_pause_at_layer**      |                                                                                                                                                                                                            |
| **Set_pause_at_next_layer** | Una macro molto utile che integra la mainsail nell'interfaccia utente per poter mettere su richiesta in uno strato specifico ... nel caso in cui ci siamo dimenticati quando abbiamo eseguito il laminato. |
|                             | Ne abbiamo anche un altro per eseguire i piacevoli nel livello successivo.                                                                                                                                 |
| **RIPRENDERE**              | Migliorato poiché consente di rilevare se il nostro ugello non è alla temperatura di estrusione per essere in grado di risolverlo prima che mostri un errore e danneggia la nostra impressione.            |
| **Cancel_print**            | Che consente all'uso del resto delle macro di eseguire correttamente una cancellazione delle impressioni.                                                                                                  |

-   **In pausa invece**, Macro molto interessanti che ci consentono di fare un tranquillo programmato in un livello o di avviare un comando quando si avvia il livello successivo. ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)Inoltre, un altro vantaggio di loro è che sono integrati con mainsail con ciò che avremo nuove funzioni nella nostra interfaccia utente come puoi vedere di seguito:![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macro di gestione della stampa**

| Macro           | Descrizione                                                                                                                                            |   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | - |
| **Start_print** | Ci permetterà di iniziare le nostre impressioni in modo sicuro e in stile Klipper. All'interno di questo troveremo alcune funzioni interessanti come:  |   |
|                 | • Preriscaldamento degli ugelli intelligenti quando si utilizza un sensore di sonda                                                                    |   |
|                 | • Possibilità di utilizzo di Z-tilt per variabile                                                                                                      |   |
|                 | • Adattivo, forzato o da una miseria a rete immagazzinata                                                                                              |   |
|                 | • Linea di spurgo personalizzabile tra la normale linea di spurgo adattiva o la caduta di spurgo                                                       |   |
|                 | • Macro segmentata per poter personalizzare come ti mostreremo in seguito                                                                              |   |
| **End_print**   | Macro della fine della stampa in cui abbiamo anche una segmentazione per personalizzare la nostra macro. Abbiamo anche una testa dinamica della testa. |   |

-   **Rotolo di letto adattivo**, grazie alla versatilità di Klipper, possiamo fare cose che oggi sembrano impossibili ... un processo importante per l'impressione è avere un pasto di deviazioni dal nostro letto che ci consente di correggerle per avere una aderenza ai primi strati perfetti.  
     In molte occasioni facciamo questa Malley prima delle impressioni per garantire che funzioni correttamente e che sia fatto in tutta la superficie del nostro letto. 
     Con la miseria adattiva del letto, verrà eseguita nella zona di stampa rendendola molto più precisa del metodo tradizionale ... nelle seguenti catture vedremo le differenze di una maglia tradizionale e adattiva.
    <div style="display: flex; justify-content: space-between;">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
    </div>

### **Macro di gestione del filamento**

Insieme di macro che ci consentiranno di gestire diverse azioni con il nostro filamento come il carico o lo scarico di questo.

| Macro               | Descrizione                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Il M600**         | Ci consentirà la compatibilità con il GCODE M600 normalmente utilizzato nei laminatori per il cambio di filamento. |
| **USCLED_FILAMENT** | La configurabile tramite le variabili ci consentirà di scaricare filamenti assistiti.                              |
| **Load_filament**   | Così come il precedente ma relativo al carico del filamento.                                                       |

### **Filament boil management macro (spoolman)**

> **⚠️ Avvertenza****Sezione in processo !!!**

[**Spoolista**](https://github.com/Donkie/Spoolman)È un direttore della bobina di filamenti integrato in Moonraker e che ci consente di gestire le nostre azioni e la disponibilità di filamenti.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Non inseriremo l'installazione e la configurazione di questo poiché è relativamente semplice usando il[**Istruzioni del tuo github**](https://github.com/Donkie/Spoolman)**,**Comunque**Ti consigliamo di usare Docker**Per semplicità e ricordo**Attiva la configurazione in Moonraker**necessario:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro              | Descrizione                                                     |
| ------------------ | --------------------------------------------------------------- |
| Set_active_spool   | Ci consente di indicare quale è l'ID della bobina da utilizzare |
| Clear_active_spool | Ci consente di ripristinare la bobina attiva                    |

L'ideale in ogni caso sarebbe quello di aggiungere il nostro laminatore,**Nei filamenti gcodes per ogni bobina la chiamata a questo**e ricorda**Cambia l'ID di questo una volta consumato**per poter controllare il resto del filamento in esso !!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Stampa Macro di gestione della superficie**

> **⚠️ Avvertenza****Sezione in processo !!!**

Di solito è normale per noi avere diverse superfici di stampa a seconda della finitura che vogliamo avere o del tipo di filamento.

Questo insieme di macro, creata da[Garethky](https://github.com/garethky), ci permetteranno di avere un controllo di questi e in particolare la corretta regolazione di Zoffset in ciascuno di essi nello stile che abbiamo nelle macchine Prussa. Di seguito puoi vedere alcune delle tue funzioni:

-   Possiamo archiviare il numero di superfici di stampa che desideriamo, ognuna con un nome univoco
-   Ogni superficie di stampa avrà il suo zoffset
-   Se facciamo le impostazioni Z durante un'impressione (babystepping) dal nostro klipper, questo cambiamento andrà in magazzino in superficie abilitata in quel momento

D'altra parte ne abbiamo alcuni**Requisiti per implementarlo (verrà tentato di aggiungere la logica della stampa bundle**:

-   L'uso di**[salva_variables]**, nel nostro caso useremo ~/variabili.cfg per archiviare le variabili e che è già all'interno del CFG di queste macro.  
    Questo creerà automaticamente un file VARIABS_BUILD_SHEETS.CFG in cui manterranno le nostre variabili del disco.

**Esempio di file di configurazione variabile**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

-   Dobbiamo includere una chiamata per applicare_build_sheet_adjustment nel nostro print_start per poter applicare la superficie selezionata Zoffset
-   È importante che per la macro anteriore, Applic_Build_Sheet_Adjustment, funziona correttamente dobbiamo aggiungere un set_gcode_offset z = 0.0 appena prima di chiamare Applic_Build_Sheet_Adjustment


    # Load build sheet
    SHOW_BUILD_SHEET ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset

D'altra parte è interessante poter avere alcune macro per attivare una superficie o l'altra o addirittura passarla come parametro dal nostro laminatore a diversi profili di stampante o filamento per poter caricare l'uno o l'altro:

> **⚠️ Avvertenza**È importante che il valore in nome = "xxxx" coincida con il nome che abbiamo dato durante l'installazione della nostra superficie di stampa

\*\* Printer.cfg

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

Anche nel caso di avere klipperscreen possiamo aggiungere un menu specifico per essere in grado di gestire il carico delle diverse superfici, in cui includeremo una chiamata alle macro precedentemente create per il caricamento di ogni superficie:

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

| Macro                          | Descrizione |
| ------------------------------ | ----------- |
| Install_Build_Sheet            |             |
| Show_build_sheet               |             |
| Show_build_sheets              |             |
| Set_build_sheet_offset         |             |
| Reset_build_sheet_offset       |             |
| Set_gcode_offset               |             |
| Applica_Build_Sheet_Adjustment |             |

### **Macro della macchina**

| Macro                                                  | Descrizione                                                                                                                                                                                                                           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compile_firmware**                                   | Con questa macro possiamo compilare il firmware Klipper in modo semplice, avere il firmware accessibile dall'interfaccia utente per una maggiore semplicità ed essere in grado di applicarlo alla nostra elettronica.                 |
| Qui hai maggiori dettagli sull'elettronico supportato. |                                                                                                                                                                                                                                       |
| **CALCOLA_BED_MESH**                                   | Una macro estremamente utile per il calcolo dell'area per la nostra mesh perché a volte può essere un processo complicato.                                                                                                            |
| **Pid_all**                                            |                                                                                                                                                                                                                                       |
| **Pid_extruder**                                       |                                                                                                                                                                                                                                       |
| **Pid_bed**                                            | Queste macro, dove possiamo passare le temperature per il PID sotto forma di parametri, ci consentiranno di essere in grado di eseguire la calibrazione della temperatura in modo estremamente semplice.                              |
| **Test_speed**                                         |                                                                                                                                                                                                                                       |
| **Test_speed_delta**                                   | Macro originale del partner[Ellis](https://github.com/AndrewEllis93)Ci permetteranno in un modo abbastanza semplice per testare la velocità con cui possiamo spostare la nostra macchina in modo preciso e senza perdita di passaggi. |

\*\_**Compilazione del firmware per elettronica supportata**, Per facilitare il processo di creazione e manutenzione del nostro firmware Klipper per il nostro MCU, abbiamo la macro compile_firmware che durante l'esecuzione, possiamo usare la nostra elettronica come parametro per fare solo questo, Klipper compilerà per tutte le elettroniche supportate dal nostro BUNDLE:![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)Troveremo questi accessibili in modo semplice dal nostro sito Web dell'interfaccia utente nella directory firmware_binaries nella nostra scheda macchina (se utilizziamo la mainsail):![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)Quindi hai l'elenco dell'elettronica supportata:

> ⚠️**IMPORTANTE!!!**
>
> Questi script sono pronti a funzionare su un sistema> raspbian con l'utente PI, se non sei il tuo caso devi adattarlo.
>
> Le aziende sono generate per l'uso con la connessione USB che è sempre ciò che consigliamo, inoltre il punto di assemblaggio USB è sempre lo stesso per ciò che la tua configurazione della connessione MCU non cambierà se sono generati con il nostro macro/script
>
> **In modo che Klipper possa eseguire macro shell, è necessario installare un'estensione, grazie al partner**[**Arksine**](https://github.com/Arksine)**, lascialo.**
>
> **A seconda del distro di klipper usato, possono già essere abilitati.**
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> Il modo più semplice è usare[**Kioh**](../instalacion/#instalando-kiauh)Dove troveremo in una delle tue opzioni la possibilità di installare questa estensione:
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Possiamo anche eseguire il processo a mano, copriremo manualmente il plug -in per Klipper &lt;[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)all'interno della nostra directory`_**~/klipper/klippy/extras**_`Usando SSH SCP Y Riavvia Klipper.

| Elettronico           | Nome parametro da utilizzare in macro |
| --------------------- | ------------------------------------- |
| MANTA                 | Sono orgoglioso                       |
| Fare m4p              | BTT-MANTA-M4P                         |
| MANTA M4P V2.         | BTT-MANTA-M4P-22                      |
| Fare m8p              | BTT-MANTA-M8P                         |
| Contrassegna M8P v1.1 | BTT-MANTA-M8P-11                      |
| Octopus max questo    | BTT-Octopus-Max-Ez                    |
| Octopus Pro (446)     | BTT-Octopus-Pro-446                   |
| Octopus Pro (429)     | BTT-Octopus-Pro-429                   |
| Octopus Pro (H723)    | BTT-Octopus-Pro-H723                  |
| Octopus v1.1          | BTT-OCTOPUS-11                        |
| Octopus v1.1 (407)    | BTT-OCTOPUS-11-407                    |
| SKR PRO V1.2          | Skr_pro_12                            |
| SKR 3                 | vite BTT 3                            |
| Saqr a (heha)         | Intelligente                          |
| Skr 3 questo          | BTT-SC-3-EZ                           |
| SKR 3 this (H723)     | Skirzhahah                            |
| SKR 2 (429)           | BTT-SRC-2-429                         |
| SKR 2 (407)           | BTT-SRC-2-407                         |
| Urla                  | BTT-SKRAT-10                          |
| Di 1.4 Turbo          | BTT-SC-14-Turbo                       |
| Skri Mini             | BTT_SKR_MINI_E3_30                    |

| Testa degli strumenti (can) | Nome parametro da utilizzare in macro |
| --------------------------- | ------------------------------------- |
| EBB42 V1                    | BTT_EBB42_10                          |
| EBB36 V1                    | BTT_EBB36_10                          |
| EBB42 V1.1                  | BTT_EBB42_11                          |
| EBB36 V1.1                  | BTT_EBB36_11                          |
| EBB42 V1.2                  | BTT_EBB42_12                          |
| EBB36 V1.2                  | BTT_EBB36_12                          |

| **Elettronico**           | **Nome parametro da utilizzare in macro** |
| ------------------------- | ----------------------------------------- |
| MKS Eagle v1.x            | MKS-EAGLE-10                              |
| Mcs robin nano cotto      | MKS-ROBIN-Nano-30                         |
| MKS Robin Nano V2         | MKS-ROBIN-Nano-20                         |
| MKS GEN L.                | MKS-GEN-L                                 |
| La colpa di Robin Nano du | Zinbennanda                               |

| Testa degli strumenti (can) | Nome parametro da utilizzare in macro |
| --------------------------- | ------------------------------------- |
| Mellow Fly Sht 42           | Mellow_fly_sht_42                     |
| Mellow Fly Sht 36           | Mellowle_fly_sht_36                   |

| Elettronico   | Nome parametro da utilizzare in macro |
| ------------- | ------------------------------------- |
| Spider FySETC | Spider FySETC                         |

| Elettronico           | Nome parametro da utilizzare in macro |
| --------------------- | ------------------------------------- |
| Artiglieria Ruby v1.x | artiglieria-ruby-12                   |

| Elettronico           | Nome parametro da utilizzare in macro |
| --------------------- | ------------------------------------- |
| Raspberry Pico/RP2040 | RPI-RP2040                            |

| Elettronico    | Nome parametro da utilizzare in macro |
| -------------- | ------------------------------------- |
| Leviathan v1.2 | Leviathan-12                          |

### Aggiunta di macro a 3dwork alla nostra installazione

Dalla nostra interfaccia, Mainsail/Fluidd, modificheremo la nostra stampante.cfg e aggiungeremo:

**stampante.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️**INFORMAZIONI!!!**È importante aggiungere queste righe alla fine del nostro file di configurazione ... appena sopra la sezione in modo che nel caso delle macro nel nostro CFG o includano queste sono sopraffatte dal nostro: 
> \#\*# \\ &lt;--- Save_config --->

> ⚠️**IMPORTANTE!!!**Le macro normali sono state separate da**macro shell** ya que **Per abilitare questi è necessario effettuare ulteriori passaggi manuali che stanno attualmente testando**E\*\*Possono richiedere autorizzazioni extra per attribuire autorizzazioni di esecuzione per le quali le istruzioni non sono state indicate poiché sta cercando di automatizzare.\*\***Se li usi è sotto la tua stessa responsabilità.**

### Impostazioni del nostro laminatore

Poiché le nostre macro sono dinamiche, estraggerà alcune informazioni dalla nostra configurazione della stampante e dal laminatore stesso. Per fare ciò ti consigliamo di configurare i tuoi laminatori come segue:

-   **Start_print start gcode**, usando i segnaposto per passare in modo dinamico il filamento e la temperatura del letto:

**Prusaslicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**Superslicer**- Abbiamo la possibilità di regolare la temperatura del recinto (Camera)

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FWdBRcy89NrRtBi4IagKi%2Fimage.png&width=400&dpr=3&quality=100&sign=3adc1f4b&sv=2)

**Bambu Studio/OrcaSlicer**

```ini
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Cura Post Processing Plugin](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F7hv1OPOgkT9d3AlupU1v%2Fimage.png&width=400&dpr=3&quality=100&sign=fad633b1&sv=2)

**Cura**

```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

> ⚠️**Avviso!!!**Dobbiamo installare il plugin[**Plug -in post processo (di Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)Dal menu_**Aiuto/spettacolo**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.  
> Reiniciamos Cura e iremos a_**Estensioni/post elaborazione/modifica del codice G.**_E selezioneremo_**Dimensione della stampa in mesh**_.

**Ideamaker**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Semplificare3d**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️**INFORMAZIONI!!!**IL**I segnaposto sono "aka" o variabili**di stampa.
>
> Nei seguenti link puoi trovare un elenco di questi per:[**Prusaslicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Superslicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(oltre a quelli del precedente),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)E[**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> L'uso di questi consente alle nostre macro di essere dinamiche.

-   **GCode the Final End_print**, in questo caso, quando non si utilizzano i palafitti, è comune a tutti i laminatori

```ini
END_PRINT
```

### Variabili

Come abbiamo già accennato, queste nuove macro ci consentiranno di avere alcune funzioni molto utili come elenchiamo in precedenza.

Per la regolazione di questi sulla nostra macchina useremo le variabili che troveremo in Macros/Macros_var_Globals.cfg e che dettagliamo di seguito.

#### Lingua di messaggio/notifiche

Dal momento che a molti utenti piace avere le notifiche delle macro nella loro lingua, abbiamo ideato un sistema di notifica multi-lingua, attualmente spagnolo e inglese (EN). Nella seguente variabile possiamo regolarlo:

| Variabile          | Descrizione                                                                                                                  | Valori possibili | Valore predefinito |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_language | Ci consente di selezionare il linguaggio delle notifiche. Nel caso di non essere ben definito, verrà utilizzato in (inglese) | È / in           | È                  |

#### Estrusione relativa

Permette di controllare quale modalità di estrusione utilizzeremo alla fine del nostro start_print. Il valore dipenderà dalla configurazione del nostro laminatore.

> 💡**Consiglio**Si consiglia di configurare il tuo laminatore per l'uso di estrusione relativa e regolare questa variabile su true.

| Variabile                    | Descrizione                                                                         | Valori possibili | Valore predefinito |
| ---------------------------- | ----------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_relative_extrusion | Ci consente di indicare la modalità di estrusione utilizzata nel nostro laminatore. | Vero / falso     | VERO               |

#### Velocità

Per gestire le velocità utilizzate nelle macro.

| Variabile                    | Descrizione                       | Valori possibili | Valore predefinito |   |
| ---------------------------- | --------------------------------- | ---------------- | ------------------ | - |
| variabile_macro_travel_speed | Velocità in tradotto              | numerico         | 150                |   |
| variabile_macro_z_speed      | Velocità in tradotto per l'asse z | numerico         | 15                 |   |

#### Homing

Insieme di variabili relative al processo di homing.

| Variabile | Descrizione | Valori possibili | Valore predefinito |
| --------- | ----------- | ---------------- | ------------------ |

#### Riscaldamento

Variabili relative al processo di riscaldamento della nostra macchina.

| Variabile                                   | Descrizione                                                                                | Valori possibili | Valore predefinito |
| ------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------- | ------------------ |
| variabile_preheat_extruder                  | Abilita l'ugello preriscaldato alla temperatura indicata in variabile_preheat_xtruder_temp | Vero / falso     | VERO               |
| variabile_preheat_extruder_temp             | Temperatura preriscaldata da ugello                                                        | numerico         | 150                |
| variabile_start_print_heat_chamber_bed_temp | Temperatura del letto durante il processo di riscaldamento del nostro recinto              | numerico         | 100                |

> 💡**Consiglio**Vantaggi dell'utilizzo dell'ugello preriscaldato:

-   Ci consente di ulteriori tempo per il letto per raggiungere la sua temperatura in modo uniforme
-   Se utilizziamo un sensore affini che non ha una compensazione della temperatura, ci consentirà di rendere le nostre misure più coerenti e precise
-   Permette di ammorbidire qualsiasi resto del filamento nell'ugello che consente, in alcune configurazioni, questi resti non influiscono sull'attivazione del sensore 
    { % endhint %}

#### Letto mali (mesh da letto)

Per controllare il processo di livellamento abbiamo variabili che possono essere molto utili. Ad esempio, possiamo controllare il tipo di livellamento che vogliamo utilizzare creando sempre una nuova mesh, caricando una mesh precedentemente memorizzata o utilizzando una mesh adattiva.

| Variabile                                                                                                                     | Descrizione                                                                       | Valori possibili | Valore predefinito |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrate_bed_mesh                                                                                                  | Ci consente di selezionare il tipo di miseria che useremo nel nostro start_print: |                  |                    |
| - New Mesh, ci renderà una miseria in ogni impressione                                                                        |                                                                                   |                  |                    |
| - SchededMeh, caricherà una mesh memorizzata e non eseguirà il sondaggio del letto                                            |                                                                                   |                  |                    |
| - Adattivo, ci renderà una nuova miseria ma adattati alla zona di stampa migliorando i nostri primi strati in molte occasioni |                                                                                   |                  |                    |
| -Nomesh, nel caso in cui non abbiamo un sensore o utilizziamo il processo per saltare il processo                             | Nuova mesh / mesh memorizzato / adattivo /                                        |                  |                    |
| Noma                                                                                                                          | adattivo                                                                          |                  |                    |
| variabile_bed_mesh_profile                                                                                                    | Il nome usato per la nostra maglia memorizzata                                    | testo            | predefinito        |

> ⚠️**Avviso!!!**Ti consigliamo di utilizzare il livello adattivo poiché regolerà sempre la miseria alle dimensioni della nostra impressione permettendoti di avere un'area di Malle modificata.
>
> È importante che abbiamo nel nostro[Start -Up GCode](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), nella chiamata ai nostri valori start_print, print_max e print_min.

#### Spurgato

Una fase importante del nostro inizio della stampa è una corretta spurgo del nostro ugello per evitare resti di filamento o che possono danneggiare la nostra impressione ad un certo punto. Quindi hai le variabili coinvolte in questo processo:
| Variabile | Descrizione | Valori possibili | Valore predefinito |
\| --- \| --- \| --- \| --- \|
| Variabile_nozzle_priming | Possiamo scegliere tra diverse opzioni di purezza:<br>- Primellina: disegna la linea tipica eliminata<br>- PrimellineAdaptive: genera una linea di spurgo adattata alla zona di stampa usando variabile_nazzle_priming_objectdistance come margine<br>- Primoblob: fa una goccia di filamento in un angolo del letto | Primelline / PrimellineAdaptive / PrimeBlob / False | Primelineadaptative |
| Variabile_nozzle_priming_objectdistance | Se utilizziamo la linea di spurgo adattiva, sarà il margine da utilizzare tra la linea di spurgo e l'oggetto stampato | numerico | 5 |
| Variabile_nozzle_prime_start_x | Dove individuare la nostra linea di spurgo in x:<br>- min: x = 0 (più margine di sicurezza)<br>- max: x = max (meno sala di sicurezza)<br>- Numero: coordinata X specifica | min / max / numero | Max |
| Variabile_nozzle_prime_start_y | Dove individuare la nostra linea di spurgo in y:<br>- min: y = 0 (più margine di sicurezza)<br>- max: y = max (meno sala di sicurezza)<br>- Numero: coordinate e specifiche | min / max / numero | min |
| Variabile_nozzle_prime_direction | Line o indirizzo di caduta:<br>- all'indietro: verso la parte anteriore<br>- Avanti: all'indietro<br>- Auto: verso il centro secondo variabile_nazzle_prime_start_y | Auto / Forward / Backwards | Auto |

#### Carico/scarico delle riprese

In questo caso, questo gruppo di variabili faciliterà la gestione del carico e dello scarico del nostro filamento utilizzato nell'emulazione dell'M600, ad esempio o lanciando le macro del filamento di carico e scarico:

| Variabile                        | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                | Valori possibili | Valore predefinito |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_filament_unload_length | Quanto si ritira in mm il filamento, regola la macchina, normalmente la misura dall'ugello agli ingranaggi del tuo estrusore aggiungendo un margine extra.                                                                                                                                                                                                                                                 | numero           | 130                |
| variabile_filament_unload_speed  | Velocità di ritrattazione del filamento in mm/sec Normalmente viene utilizzata una velocità lenta.                                                                                                                                                                                                                                                                                                         | numero           | 5                  |
| variabile_filament_load_length   | Distanza in mm per caricare il nuovo filamento ... come in variabile_filament_unload_length useremo la misura dall'attrezzatura di estrusore aggiungendo un margine extra, in questo caso questo valore extra dipenderà da quanto si desidera essere spurgata ... Di solito puoi dargli più margine rispetto al valore precedente per assicurarsi che sia purificata l'estrusione del filamento anteriore. | numero           | 150                |
| variabile_filament_load_speed    | La velocità di carico del filamento in mm/sec normalmente viene utilizzata una velocità più rapida.                                                                                                                                                                                                                                                                                                        | numero           | 10                 |

> ⚠️**Avviso!!!**Un'altra regolazione necessaria per la tua sezione**[estrusore]**L'indicato[**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... Il valore consigliabile è generalmente> 101 (se non è definito utilizza 50) per consentire i tipici test di calibrazione degli estrusore.  
> È necessario regolare il valore in base a quanto sopra del test o sulla configurazione del tuo**variabile_filament_unload_length**IO**variabile_filament_load_length**.

#### Parcheggio

In alcuni processi della nostra stampante, come il tempo libero, è consigliabile fare un parcheggio della nostra testa. Le macro del nostro pacchetto hanno questa opzione oltre alle seguenti variabili da gestire:

| Variabile                           | Descrizione                                                                                                                                                                                                                                                                | Valori possibili | Valore predefinito |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_start_print_park_in       | Posizione dove parcheggiare la testa durante il pre-scansion.                                                                                                                                                                                                              | Indietro /       |                    |
| centro /                            |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                             | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_start_print_park_z_height | Z altezza durante il prezioso                                                                                                                                                                                                                                              | numero           | 50                 |
| variabile_end_print_park_in         | Posizione per parcheggiare la testa alla fine o annullare un'impressione.                                                                                                                                                                                                  | Indietro /       |                    |
| centro /                            |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                             | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_end_print_park_z_hop      | Distanza per salire alla fine dell'impressione.                                                                                                                                                                                                                            | numero           | 20                 |
| variabile_pause_print_park_in       | Posizione per parcheggiare la testa di Pausar l'impressione.                                                                                                                                                                                                               | Indietro /       |                    |
| centro /                            |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                             | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_pause_idle_timeout        | Valore, in pochi secondi, dell'attivazione del processo di inattività nella macchina che rilascia motori e perdita di coordinate,**È consigliabile un valore elevato per attivare la macro pausa abbastanza da eseguire qualsiasi azione prima di perdere le coordinate.** | numero           | 43200              |

#### Z-Tilt

Prendi il massimo dalla nostra macchina in modo che sia auto -livello e faciliti che la nostra macchina sia sempre nelle migliori condizioni è essenziale.

**Z-Tilt è fondamentalmente un processo che ci aiuta ad allineare i nostri motori Z rispetto al nostro asse x (cartesiano) o XY (corexy) (corexy)**. Con questo**Assicuriamo di avere sempre la nostra Z perfettamente e in modo preciso e automatico**.

| Variabile                  | Descrizione                                                                                                   | Valori possibili | Valore predefinito |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrate_z_tilt | Consente, nel caso di averlo abilitato nella nostra configurazione Klipper, il processo di regolazione Z-Tilt | Vero / falso     | Falso              |

#### Inclinarsi

L'uso di[Inclinarsi](broken-reference)Per la correzione o l'adeguamento preciso delle nostre stampanti è estremamente consigliabile se abbiamo deviazioni nelle nostre impressioni. Usando la seguente variabile possiamo consentire l'uso nelle nostre macro:

| Variabile              | Descrizione                                                                                                                                                                                                                                    | Valori possibili | Valore predefinito |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_skew_profile | Ci consente di tenere conto del nostro profilo di disgustoso che verrà addebitato nella nostra macro start_print. Per attivarlo, dobbiamo discutere la variabile e utilizzare il nome del profilo di inclinazione della nostra configurazione. | testo            | my_skew_profile    |

### Personalizzazione delle macro

Il nostro modulo Klipper utilizza il sistema di configurazione modulare utilizzato in tempi e sfrutta i vantaggi di Klipper nel processo del file di configurazione in sequenza. Questo è il motivo per cui è essenziale che l'ordine degli aggiustamenti includono e personalizzati che vogliamo applicare su questi moduli.

> ℹ️**INFORMAZIONI!!!**Quando si utilizzano le impostazioni di 3dwork come modulo, non possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura (limitato alla solo lettura) per sicurezza.
>
> Ecco perché è molto importante capire il funzionamento di Klipper e come personalizzare i nostri moduli sulla macchina.

#### **Personalizzare le variabili**

Normalmente, sarà ciò che dovremo regolare, per apportare modifiche alle variabili che abbiamo per impostazione predefinita nel nostro modulo**3dwork**Para tagli.

Semplicemente, quello che dobbiamo fare è incollare il contenuto macro**[GCode_Macro Global_vars]**che possiamo trovare in macros/macros var globals.cfg nella nostra stampa.cfg.

Ti ricordiamo cosa è stato precedentemente commentato su come Klipper elabora le configurazioni in sequenza, quindi è consigliabile incollarle dopo le incluse[Qui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Avremo qualcosa del genere (è solo un esempio visivo):

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

> ⚠️**Avviso!!!**I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.

> ℹ️**INFORMAZIONI!!!**
>
> -   Ti consigliamo di aggiungere commenti come vedi nel caso precedente per identificare ciò che ogni sezione fa
> -   Anche se non è necessario toccare tutte le variabili che ti consigliano di copiare l'intero contenuto di**[GCode_Macro Global_vars]**

#### Personalizzazione delle macro

Le macro si sono montate in modo modulare in modo che possano essere regolate in modo semplice. Come abbiamo detto prima, se vogliamo regolarli dobbiamo procedere proprio come abbiamo fatto con le variabili, copiare la macro in questione nella nostra stampante.cfg (o altro includi il nostro) e assicurati che sia dopo l'inclusione di dove aggiungiamo il nostro modulo di 3dwork per Klipper.

Abbiamo due gruppi di macro:

-   Macro Per aggiungere le impostazioni dell'utente, queste macro possono essere facilmente aggiunte e personalizzate perché sono state aggiunte in modo che qualsiasi utente possa personalizzare le azioni a loro piacimento in una certa parte dei processi che ogni macro fa.

**Start_print**

| Nome macro                                | Descrizione                                                                                                                             |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| \_USER_START_PRINT_HEAT_CHAMBER           | Funziona subito dopo che il nostro recinto ha iniziato a riscaldare, se Chamber_temp viene passato come parametro al nostro start_print |
| \_User_start_print_before_homing          | Viene eseguito prima dell'homing iniziale per l'inizio della stampa                                                                     |
| \_User_start_print_after_heating_bed      | Funziona quando il nostro letto arriva alla sua temperatura, prima di \_start_print_after_heating_bed                                   |
| \_User\_ start_print bed_mesh             | Viene lanciato prima di \_start_print_bed_mesh                                                                                          |
| \_USER_START_PRINT_PARK                   | Viene lanciato prima di \_start_print_park                                                                                              |
| \_User_start_print_after_heating_extruder | Se lanza antes de \_start_print_after_heating_extruder                                                                                  |

**End_print**

| Nome macro                          | Descrizione                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------------------- |
| \_User_end_print_before_heaters_off | Viene eseguito prima di eseguire il riscaldatore, prima di \_end_print_before_heaters_off |
| \_User_end_print_after_heaters_off  | Funziona dopo il riscaldamento, prima di \_end_print_after_heaters_off                    |
| \_User_end_print_park               | Viene eseguito prima della testa della testa, prima di \_end_print_park                   |

**Print_basics**

| Nome macro          | Descrizione                               |
| ------------------- | ----------------------------------------- |
| \_User_pause_start  | Viene eseguito all'inizio di una pausa    |
| \_User_pause_end    | Funziona alla fine di una pausa           |
| \_User_resume_start | Viene eseguito all'inizio di un riassunto |
| \_User_resume_end   | Corre alla fine di un riassunto           |

-   Macro interne, sono macro per dividere la macro principale in processi ed è importante per questo. È consigliabile che, in caso di richiedere che vengano copiati così com'è.

**Start_print**

| Nome macro                           | Descrizione                                                                                                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \_Start_print_heat_chamber           | Riscalda il contenitore nel caso in cui il parametro Chamber_temp sia ricevuto dal nostro macro start_print dal laminatore                                                                                         |
| \_Start_print_after_heating_bed      | Funziona quando il letto arriva a temperatura, dopo \_user_start_print_after_heating_bed. Normalmente, viene utilizzato per l'elaborazione della calibrazione del letto (z_tilt_adjust, quad_gantry_leveling, ...) |
| \_Start_print_bed_mesh               | È responsabile della logica della miseria del letto.                                                                                                                                                               |
| \_Start_print_park                   | Attacco la testa di stampa mentre riscalda l'ugello alla temperatura di stampa.                                                                                                                                    |
| \_Start_print_after_heating_extruder | Fai spurgare e carica il profilo di inclinazione nel caso in cui definiamo nelle variabili                                                                                                                         |

## Stampanti ed elettronici

Mentre lavoriamo con diversi modelli di stampanti ed elettronici, aggiungeremo quelli che non sono direttamente supportati da volte, sia che si tratti di contributi o di comunità.

-   Stampanti, in questa directory avremo tutte le configurazioni della stampante
-   Assi, qui troveremo l'elettronica

### Parametri e pin

Il nostro modulo Klipper utilizza il sistema di configurazione modulare utilizzato in tempi e sfrutta i vantaggi di Klipper nel processo del file di configurazione in sequenza. Questo è il motivo per cui è essenziale che l'ordine degli aggiustamenti includono e personalizzati che vogliamo applicare su questi moduli.

> ℹ️**INFORMAZIONI!!!**Quando si utilizzano le impostazioni di 3dwork come modulo, non possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura (limitato alla solo lettura) per sicurezza.
>
> Ecco perché è molto importante capire il funzionamento di Klipper e come personalizzare i nostri moduli sulla macchina.

Come abbiamo spiegato in "[Personalizzazione delle macro](3dwork-klipper-bundle.md#personalizando-macros)"Useremo lo stesso processo per regolare i parametri o i pin per regolare le nostre esigenze.

#### Personalizzazione dei parametri

Mentre ti consigliamo di creare una sezione nella tua stampante.cfg che si chiama overrides utente, posizionata dopo l'inclusione delle nostre configurazioni, per poter regolare e personalizzare qualsiasi parametro utilizzato in esse.

Nel seguente esempio vedremo come nel nostro caso siamo interessati a personalizzare i parametri del nostro livellamento del letto (BED_MEH) che regola i punti di rilevamento (SUSE_COUNT) rispetto alla configurazione che abbiamo per impostazione predefinita nelle configurazioni del nostro modulo Klipper:

**stampante.cfg**

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

> ⚠️**Avviso!!!**I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.

Possiamo usare lo stesso processo con qualsiasi parametro che vogliamo regolare.

#### Personalizzazione della configurazione dei pini

Procederemo esattamente come abbiamo fatto prima, nella nostra area di sostituzione dell'utente aggiungeremo quelle sezioni di pin che vogliamo adattarci ai nostri gusti.

Nell'esempio seguente personalizzeremo qual è il pin del nostro ventilatore elettronico (controller_fan) per assegnarlo a uno diverso da predefinito:

**stampante.cfg**

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

> ⚠️**Avviso!!!**I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.
