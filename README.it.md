* * *

## Descrizione: pacchetto macro, configurazioni e altre utility per Klipper

# Pacchetto clope 3dwork

[<img width="171" alt="kofi" src="https://github.com/3dwork-io/3dwork-klipper/blob/master/Ko-fi-Logo.png">](https://ko-fi.com/jjr3d)

[![](../../.gitbook/assets/image%20(1986).png)- Inglese](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{ % SITTH STYE = "Danger" %}  
**Guida nel processo !!! Sebbene le macro siano totalmente funzionali, questi sono in sviluppo continuo.**

**Usali sotto la tua stessa responsabilità !!!**  
{% di endhint%}

Changelog

12/07/2023 - Aggiunto supporto per automatizzare la creazione del firmware elettronico BigRetech

Da**3dwork**Abbiamo compilato e regolato un set di macro, macchine e configurazioni elettroniche, nonché altri strumenti per una gestione semplice e potente di Klipper.

Gran parte di questo pacchetto si basa su[**Ratti**](https://os.ratrig.com/)Migliorare le parti che crediamo interessanti e altri contributi della comunità.

## Installazione

Per installare il nostro pacchetto per Klipper seguiremo i seguenti passaggi

### Scarico del repository

Ci connetteremo al nostro host di SSH e avviremo i seguenti comandi:

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{ % SIT STYE = "Avviso" %}  
Nel caso in cui la directory della configurazione Klipper sia personalizzata, ricorda di regolare correttamente il primo comando alla tua installazione.  
{% di endhint%}

{ % suggerimenti style = "info" %}  
In nuove strutture:

Poiché Klipper non consente l'accesso alle macro fino a quando non ha una stampante corretta.cfg e si collega a un MCU, possiamo "ingannare" Klipper con i seguenti passaggi che ci consentiranno di utilizzare le macro del nostro pacchetto per, ad esempio, avviare la macro di compilazione del firmware Klipper se utilizziamo una elettronica compatibile:

-   Ci assicuriamo che abbiamo il nostro[Ospita come secondo MCU](raspberry-como-segunda-mcu.md)
-   Successivamente aggiungeremo una stampante.cfg, ricorda che questi passaggi sono per un'installazione pulita in cui non si dispone di stampante.cfg e si desidera avviare la macro per creare firmware, come quello che puoi vedere di seguito:


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

Con questo possiamo iniziare Klipper per accedere alle nostre macro.  
{% di endhint%}

### Usando Moonraker per essere sempre aggiornato

Grazie a Moonraker possiamo usare il suo aggiornamento_Manager per poter essere aggiornato con i miglioramenti che possiamo introdurre in futuro.

Da mainsail/fluidd modificheremo il nostro moonraker.conf (dovrebbe essere alla stessa altezza della tua stampante.cfg) e aggiungeremo alla fine del file di configurazione:

    [include 3dwork-klipper/moonraker.conf]

{ % SIT STYE = "Avviso" %}  
**Ricorda di fare il passaggio di installazione in precedenza se non si genera un errore e non sarai in grado di avviare.**

**D'altra parte, nel caso in cui la directory di configurazione di Klipper sia personalizzata, ricorda di regolare correttamente il percorso alla tua installazione.**  
{% di endhint%}

## Macro

Abbiamo sempre commentato che Times è una delle migliori distribuzioni di Klipper, con supporto Raspberry e moduli CB1, in gran parte a causa delle sue configurazioni modulari e delle sue grandi macro.

Alcune macro aggiunte che saranno utili:

### **Macro per uso generale**

| Macro                                                                      | Descrizione                                                                                                                                                                                                |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FORSE_CASA**                                                             | Ci consente di ottimizzare il processo di homing solo facendo questo in quegli assi che non sono con l'homing.                                                                                             |
| **PAUSA**                                                                  | Attraverso variabili correlate ci consente di gestire una pausa con un parcheggio più versatile che le normali macro.                                                                                      |
| **IMPOSTATO_PAUSA_A_STRATO**                                               |                                                                                                                                                                                                            |
| **IMPOSTATO_PAUSA_A_PROSSIMO_STRATO**                                      | Una macro molto utile che integra la mainsail nell'interfaccia utente per poter mettere su richiesta in uno strato specifico ... nel caso in cui ci siamo dimenticati quando abbiamo eseguito il laminato. |
| Ne abbiamo anche un altro per eseguire i piacevoli nel livello successivo. |                                                                                                                                                                                                            |
| **RIPRENDERE**                                                             | Migliorato poiché consente di rilevare se il nostro ugello non è alla temperatura di estrusione per essere in grado di risolverlo prima che mostri un errore e danneggia la nostra impressione.            |
| **CANCELLARE_STAMPA**                                                      | Che consente all'uso del resto delle macro di eseguire correttamente una cancellazione delle impressioni.                                                                                                  |

-   **In pausa invece**, Macro molto interessanti che ci consentono di fare un tranquillo programmato in un livello o di avviare un comando quando si avvia il livello successivo.   
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    Inoltre, un altro vantaggio di loro è che sono integrati con mainsail con ciò che avremo nuove funzioni nella nostra interfaccia utente come puoi vedere di seguito:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Macro di gestione della stampa**

| Macro                                                                                           | Descrizione                                                                                                                                            |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **INIZIO_STAMPA**                                                                               | Ci permetterà di iniziare le nostre impressioni in modo sicuro e in stile Klipper. All'interno di questo troveremo alcune funzioni interessanti come:  |
| -Preriscaldato di ugello intelligente nel caso di avere un sensore di sonda                     |                                                                                                                                                        |
| -Possibilità di utilizzo di z-tilt per variabile                                                |                                                                                                                                                        |
| -Adattivo, forzato o da una mesh immagazzinata                                                  |                                                                                                                                                        |
| -Linea di spurgo personalizzabile tra la normale linea di spurgo adattiva o la caduta di spurgo |                                                                                                                                                        |
| -Macro segmentata per poter personalizzare come ti mostreremo più tardi                         |                                                                                                                                                        |
| **FINE_STAMPA**                                                                                 | Macro della fine della stampa in cui abbiamo anche una segmentazione per personalizzare la nostra macro. Abbiamo anche una testa dinamica della testa. |

-   **Rotolo di letto adattivo**, grazie alla versatilità di Klipper, possiamo fare cose che oggi sembrano impossibili ... un processo importante per l'impressione è avere un pasto di deviazioni dal nostro letto che ci consente di correggerle per avere una aderenza ai primi strati perfetti.   
    In molte occasioni facciamo questa Malley prima delle impressioni per garantire che funzioni correttamente e che sia fatto in tutta la superficie del nostro letto.  
    Con la miseria adattiva del letto, verrà eseguita nella zona di stampa rendendola molto più precisa del metodo tradizionale ... nelle seguenti catture vedremo le differenze di una maglia tradizionale e adattiva.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Macro di gestione del filamento**

Insieme di macro che ci consentiranno di gestire diverse azioni con il nostro filamento come il carico o lo scarico di questo.

| Macro                   | Descrizione                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **M600**                | Ci consentirà la compatibilità con il GCODE M600 normalmente utilizzato nei laminatori per il cambio di filamento. |
| **SCARICARE_FILAMENTO** | La configurabile tramite le variabili ci consentirà di scaricare filamenti assistiti.                              |
| **CARICO_FILAMENTO**    | Così come il precedente ma relativo al carico del filamento.                                                       |

### **Filament boil management macro (spoolman)**

{ % SIT STYE = "Avviso" %}  
**Sezione in processo !!!**  
{% di endhint%}

[**Spoolista**](https://github.com/Donkie/Spoolman)È un direttore della bobina di filamenti integrato in Moonraker e che ci consente di gestire le nostre azioni e la disponibilità di filamenti.

!\[](../../.gitbook/assets/image (1990) .png)

Non inseriremo l'installazione e la configurazione di questo poiché è relativamente semplice usando il[**Istruzioni del tuo github**](https://github.com/Donkie/Spoolman)**,**Comunque**Ti consigliamo di usare Docker**Per semplicità e ricordo**Attiva la configurazione in Moonraker**necessario:

{ % code title = "moonraker.conf" %}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{ % Endcode %}

| Macro                   | Descrizione                                                     |
| ----------------------- | --------------------------------------------------------------- |
| IMPOSTATO_ATTIVO_Bobina | Ci consente di indicare quale è l'ID della bobina da utilizzare |
| CHIARO_ATTIVO_Bobina    | Ci consente di ripristinare la bobina attiva                    |

L'ideale in ogni caso sarebbe quello di aggiungere il nostro laminatore,**Nei filamenti gcodes per ogni bobina la chiamata a questo**e ricorda**Cambia l'ID di questo una volta consumato**per poter controllare il resto del filamento in esso !!!

!\[](../../.gitbook/assets/image (1991) .png)

### **Stampa Macro di gestione della superficie**

{ % SIT STYE = "Avviso" %}  
**Sezione in processo !!!**  
{% di endhint%}

Di solito è normale per noi avere diverse superfici di stampa a seconda della finitura che vogliamo avere o del tipo di filamento.

Questo insieme di macro, creata da[Garethky](https://github.com/garethky), ci permetteranno di avere un controllo di questi e in particolare la corretta regolazione di Zoffset in ciascuno di essi nello stile che abbiamo nelle macchine Prussa. Di seguito puoi vedere alcune delle tue funzioni:

-   Possiamo archiviare il numero di superfici di stampa che desideriamo, ognuna con un nome univoco
-   Ogni superficie di stampa avrà il suo zoffset
-   Se facciamo le impostazioni Z durante un'impressione (babystepping) dal nostro klipper, questo cambiamento andrà in magazzino in superficie abilitata in quel momento

D'altra parte ne abbiamo alcuni**Requisiti per implementarlo (prova ad aggiungere la logica della stampa_Inizio del pacchetto in futuro attiva questa funzione per variabile e creando una macro utente precedente e posteriore per mettere gli eventi dell'utente)**:

-   L'uso di\[salva_variabili], nel nostro caso useremo ~/variabili.cfg per archiviare le variabili e che è già all'interno del CFG di queste macro.   
    Questo creerà automaticamente un file variabile_costruire_Sheets.cfg dove manterrai le nostre variabili del disco.

{ % code title = "Esempio di File di configurazione delle variabili" %}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{ % Endcode %}

-   Dobbiamo includere una chiamata applicata_COSTRUIRE_FOGLIO_Regolazione nella nostra stampa_Inizia ad essere in grado di applicare la superficie selezionata Zoffset
-   È importante che per la macro anteriore si applichi_COSTRUIRE_FOGLIO_Regolazione, lavorare correttamente dobbiamo aggiungere un set_Gcode_Offset z = 0,0 poco prima di chiamare applicare_COSTRUIRE_FOGLIO_Regolazione


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

D'altra parte è interessante poter avere alcune macro per attivare una superficie o l'altra o addirittura passarla come parametro dal nostro laminatore a diversi profili di stampante o filamento per poter caricare automaticamente l'uno o l'altro:

{ % SIT STYE = "Avviso" %}  
È importante che il valore in nome = "xxxx" coincida con il nome che abbiamo dato durante l'installazione della nostra superficie di stampa  
{% di endhint%}

{ % code title = "stampa.cfg o include cfg" %}

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

Anche nel caso di avere Klipperscreen possiamo aggiungere un menu specifico per poter gestire il carico delle diverse superfici, in cui includeremo una chiamata alle macro precedentemente create per il caricamento di ciascuna superficie:

{% code title = "~/stampante_Data/config/klipperscreen.conf " %}

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

| Macro                                       | Descrizione |
| ------------------------------------------- | ----------- |
| INSTALLARE_COSTRUIRE_FOGLIO                 |             |
| SPETTACOLO_COSTRUIRE_FOGLIO                 |             |
| SPETTACOLO_COSTRUIRE_FOGLI                  |             |
| IMPOSTATO_COSTRUIRE_FOGLIO_OFFSET           |             |
| RESET_COSTRUIRE_FOGLIO_OFFSET               |             |
| IMPOSTATO_Gcode_OFFSET                      |             |
| FARE DOMANDA A_COSTRUIRE_FOGLIO_Regolazione |             |

### **Macro della macchina**

| Macro                                                  | Descrizione                                                                                                                                                                                                                           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILARE_Firmware**                                 | Con questa macro possiamo compilare il firmware Klipper in modo semplice, avere il firmware accessibile dall'interfaccia utente per una maggiore semplicità ed essere in grado di applicarlo alla nostra elettronica.                 |
| Qui hai maggiori dettagli sull'elettronico supportato. |                                                                                                                                                                                                                                       |
| **CALCOLARE_LETTO_MAGLIA**                             | Una macro estremamente utile per il calcolo dell'area per la nostra mesh perché a volte può essere un processo complicato.                                                                                                            |
| **Pid_TUTTO**                                          |                                                                                                                                                                                                                                       |
| **Pid_Estrusore**                                      |                                                                                                                                                                                                                                       |
| **Pid_LETTO**                                          | Queste macro, dove possiamo passare le temperature per il PID sotto forma di parametri, ci consentiranno di essere in grado di eseguire la calibrazione della temperatura in modo estremamente semplice.                              |
| **TEST_VELOCITÀ**                                      |                                                                                                                                                                                                                                       |
| **TEST_VELOCITÀ_DELTA**                                | Macro originale del partner[Ellis](https://github.com/AndrewEllis93)Ci permetteranno in un modo abbastanza semplice per testare la velocità con cui possiamo spostare la nostra macchina in modo preciso e senza perdita di passaggi. |

-   **Compilazione del firmware per elettronica supportata**, Per facilitare il processo di creazione e manutenzione del nostro firmware Klipper per il nostro MCU abbiamo la macro compilazione_Firmware che durante l'esecuzione, possiamo usare la nostra elettronica come parametro per fare solo questo, Klipper si compilerà per tutti gli elettronici supportati dal nostro pacchetto:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Li troveremo facilmente accessibili dal nostro sito Web dell'interfaccia utente nella directory del firmware_Binari nella scheda Macchina (se utilizziamo la mainsail):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Quindi hai l'elenco dell'elettronica supportata:

**IMPORTANTE!!!**

Questi script sono preparati a funzionare su un sistema a raspbian con l'utente PI, se non è il tuo caso, devi adattarlo.

Le aziende sono generate per l'uso con la connessione USB che è sempre ciò che consigliamo, inoltre il punto di assemblaggio USB è sempre lo stesso per ciò che la tua configurazione della connessione MCU non cambierà se sono generati con il nostro macro/script

**In modo che Klipper possa eseguire macro shell, è necessario installare un'estensione, grazie al partner**[**Arksine**](https://github.com/Arksine)**, lascialo.**

**A seconda del distro di klipper usato, possono già essere abilitati.**

![](../../.gitbook/assets/image%20(770).png)

Il modo più semplice è usare[**Kioh**](../instalacion/#instalando-kiauh)Dove troveremo in una delle tue opzioni la possibilità di installare questa estensione:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Possiamo anche eseguire il processo a mano, copriremo manualmente il plugin per Klipper[**Gcode_conchiglia_estensione**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)all'interno della nostra directory`_**~/klipper/klippy/extras**_`Usando SSH SCP Y Riavvia Klipper.

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
| SKR 3                 | BTT_Skr_3                             |
| Saqr a (heha)         | Intelligente                          |
| Skr 3 questo          | BTT-SC-3-EZ                           |
| SKR 3 this (H723)     | Skirzhahah                            |
| SKR 2 (429)           | BTT-SRC-2-429                         |
| SKR 2 (407)           | BTT-SRC-2-407                         |
| Urla                  | BTT-SKRAT-10                          |
| Di 1.4 Turbo          | BTT-SC-14-Turbo                       |
| Skri Mini             | BTT_Skr_mini_ez_30                    |

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
| La colpa di Robin Nano du | Znp_Robin_nano_dw_Categoria               |

| Testa degli strumenti (can) | Nome parametro da utilizzare in macro |
| --------------------------- | ------------------------------------- |
| Mellow Fly Sht 42           | dolce_volare_testimone_42             |
| Mellow Fly Sht 36           | dolce_volare_testimone_36             |

| Elettronico   | Nome parametro da utilizzare in macro |
| ------------- | ------------------------------------- |
| Spider FySETC | fysetc_ragno                          |

### Aggiunta di macro a 3dwork alla nostra installazione

Dalla nostra interfaccia, Mainsail/Fluidd, modificheremo la nostra stampante.cfg e aggiungeremo:

{ % code title = "printer.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{ % Endcode %}

{ % suggerimenti style = "info" %}  
È importante aggiungere queste righe alla fine del nostro file di configurazione ... appena sopra la sezione in modo che nel caso delle macro nel nostro CFG o includano queste sono sopraffatte dal nostro:  
#\*# \\ &lt;---------------------- salva_Config ---------------------->  
{% di endhint%}

{ % SIT STYE = "Avviso" %}  
Le macro normali sono state separate da**macro shell**dato questo**Per abilitare questi è necessario effettuare ulteriori passaggi manuali che stanno attualmente testando**E\*\*Possono richiedere autorizzazioni extra per attribuire autorizzazioni di esecuzione per le quali le istruzioni non sono state indicate poiché sta cercando di automatizzare.\*\*  
**Se li usi è sotto la tua stessa responsabilità.**  
{% di endhint%}

### Impostazioni del nostro laminatore

Poiché le nostre macro sono dinamiche, estraggerà alcune informazioni dalla nostra configurazione della stampante e dal laminatore stesso. Per fare ciò ti consigliamo di configurare i tuoi laminatori come segue:

-   **Avvia avvia GCode_STAMPA**, usando i segnaposto per passare in modo dinamico il filamento e la temperatura del letto:

{ % tabs %}  
{ % tab title = "Prusaslicer-SupersLicer" %}  
**Prusaslicer**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**Superslicer**- Abbiamo la possibilità di regolare la temperatura del recinto (Camera)

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{ % endtab %}

{% tab title="Bambu Studio/OrcaSlicer" %}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760) .png) { % endtab %}

{% tab title="Cura" %}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{ % SIT STYE = "Avviso" %}  
Dobbiamo installare il plugin[**Plug -in post processo (di Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)Dal menu_**Aiuto/spettacolo**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.   
Riavvia la guarigione e andremo a_**Estensioni/post elaborazione/modifica del codice G.**_E selezioneremo_**Dimensione della stampa in mesh**_.  
{% di endhint%}  
{ % endtab %}

{ % tab title = "Ideamaker" %}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{ % endtab %}

{ % tab title = "semplifica3d" %}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{ % endtab %}  
{ % endtabs %}

{ % suggerimenti style = "info" %}  
IL**I segnaposto sono "aka" o variabili**di stampa.

Nei seguenti link puoi trovare un elenco di questi per:[**Prusaslicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Superslicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(oltre a quelli del precedente),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)E[**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

L'uso di questi consente alle nostre macro di essere dinamiche.  
{% di endhint%}

-   **GCode de Final End_STAMPA**, in questo caso, quando non si utilizzano i palafitti, è comune a tutti i laminatori


    END_PRINT

### Variabili

Come abbiamo già accennato, queste nuove macro ci consentiranno di avere alcune funzioni molto utili come elenchiamo in precedenza.

Per regolare la nostra macchina useremo le variabili che troveremo in macro/macro_Nostro_Globals.cfg e che dettagliamo di seguito.

#### Lingua di messaggio/notifiche

Dal momento che a molti utenti piace avere le notifiche delle macro nella loro lingua, abbiamo ideato un sistema di notifica multi-lingua, attualmente spagnolo e inglese (EN). Nella seguente variabile possiamo regolarlo:

| Variabile        | Descrizione                                                                                                                  | Valori possibili | Valore predefinito |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_lingua | Ci consente di selezionare il linguaggio delle notifiche. Nel caso di non essere ben definito, verrà utilizzato in (inglese) | È / in           | È                  |

#### Estrusione relativa

Ti consente di controllare quale modalità di estrusione utilizzeremo alla fine del nostro inizio_Stampa. Il valore dipenderà dalla configurazione del nostro laminatore.

{ % suggerisce style = "successo" %}  
Si consiglia di configurare il tuo laminatore per l'uso di estrusione relativa e regolare questa variabile su true.  
{% di endhint%}

| Variabile                    | Descrizione                                                                         | Valori possibili | Valore predefinito |
| ---------------------------- | ----------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_parente_estrusione | Ci consente di indicare la modalità di estrusione utilizzata nel nostro laminatore. | Vero / falso     | VERO               |

#### Velocità

Per gestire le velocità utilizzate nelle macro.

| Variabile                        | Descrizione                       | Valori possibili | Valore predefinito |   |
| -------------------------------- | --------------------------------- | ---------------- | ------------------ | - |
| variabile_macro_viaggio_velocità | Velocità in tradotto              | numerico         | 150                |   |
| variabile_macro_Con_velocità     | Velocità in tradotto per l'asse z | numerico         | 15                 |   |

#### Homing

Insieme di variabili relative al processo di homing.

| Variabile | Descrizione | Valori possibili | Valore predefinito |
| --------- | ----------- | ---------------- | ------------------ |

#### Riscaldamento

Variabili relative al processo di riscaldamento della nostra macchina.

| Variabile                                        | Descrizione                                                                                        | Valori possibili | Valore predefinito |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_preriscaldare_estrusore                | Abilita l'ugello preriscaldato alla temperatura indicata in variabile_preriscaldare_estrusore_temp | Vero / falso     | VERO               |
| variabile_preriscaldare_estrusore_temp           | Temperatura preriscaldata da ugello                                                                | numerico         | 150                |
| variabile_inizio_stampa_Calore_camera_letto_temp | Temperatura del letto durante il processo di riscaldamento del nostro recinto                      | numerico         | 100                |

{ % suggerisce style = "successo" %}  
Vantaggi dell'utilizzo dell'ugello preriscaldato:

-   Ci consente di ulteriori tempo per il letto per raggiungere la sua temperatura in modo uniforme
-   Se utilizziamo un sensore affini che non ha una compensazione della temperatura, ci consentirà di rendere le nostre misure più coerenti e precise
-   Permette di ammorbidire qualsiasi resto del filamento nell'ugello che consente, in alcune configurazioni, questi resti non influiscono sull'attivazione del sensore  
    {% di endhint%}

#### Letto mali (mesh da letto)

Per controllare il processo di livellamento abbiamo variabili che possono essere molto utili. Ad esempio, possiamo controllare il tipo di livellamento che vogliamo utilizzare creando sempre una nuova mesh, caricando una mesh precedentemente memorizzata o utilizzando una mesh adattiva.

| Variabile                                                                                                                   | Descrizione                                                                      | Valori possibili | Valore predefinito |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrare_letto_maglia                                                                                            | Ci consente di selezionare il tipo di malle che useremo al nostro inizio_STAMPA: |                  |                    |
| -Nuova mesh, ci renderà una miseria in ogni impressione                                                                     |                                                                                  |                  |                    |
| -Immagazzinato, caricherà una maglia immagazzinata e non eseguirà il sondaggio del letto                                    |                                                                                  |                  |                    |
| -Adattivo, ci renderà una nuova miseria ma adattati all'area di stampa migliorando i nostri primi strati in molte occasioni |                                                                                  |                  |                    |
| -Nomesh, nel caso in cui non abbiamo un sensore o utilizziamo il processo per saltare il processo                           | Nuova mesh / mesh memorizzato / adattivo /                                       |                  |                    |
| Noma                                                                                                                        | adattivo                                                                         |                  |                    |
| variabile_letto_maglia_profilo                                                                                              | Il nome usato per la nostra maglia memorizzata                                   | testo            | predefinito        |

{ % SIT STYE = "Avviso" %}  
Ti consigliamo di utilizzare il livello adattivo poiché regolerà sempre la miseria alle dimensioni della nostra impressione permettendoti di avere un'area di Malle modificata.

È importante che abbiamo nel nostro[Start -Up GCode](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), nella chiamata al nostro inizio_Valori di stampa, stampa_Max Y Stampa_Min.  
{% di endhint%}

#### Spurgato

Una fase importante del nostro inizio della stampa è una corretta spurgo del nostro ugello per evitare resti di filamento o che possono danneggiare la nostra impressione ad un certo punto. Quindi hai le variabili coinvolte in questo processo:

| Variabile                                                                                                                                                  | Descrizione                                        | Valori possibili | Valore predefinito |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------- | ------------------ |
| variabile_ugello_innesco                                                                                                                                   | Possiamo scegliere tra diverse opzioni di purezza: |                  |                    |
| -Primelline disegnerà la tipica linea di spurgo                                                                                                            |                                                    |                  |                    |
| -PrimelineAdaptative genererà una linea di spurgo che si adatta all'area del pezzo stampato usando la variabile_ugello_innesco_ObjectDistance come margine |                                                    |                  |                    |
| -Primoblob ci renderà una goccia di filamento in un angolo del nostro letto molto efficace per pulire l'ugello e facile da ritirare                        |                                                    |                  |                    |
| PRIMINAZIONE /                                                                                                                                             |                                                    |                  |                    |

Prime -adaptive /   
Primoblob /   
Falso

| primelineadaptive |  
| variabile_ugello_innesco_ObjectDistance | Se utilizziamo la linea di spurgo adattiva, sarà il margine da utilizzare tra la linea di spurgo e l'oggetto stampato | numerico | 5 |  
| variabile_ugello_Prime_inizio_x | Dove vogliamo individuare la nostra linea di spurgo:  
-Min lo farà a x = 0 (più un piccolo margine di sicurezza)  
-Max lo farà a x = max (meno un piccolo margine di sicurezza)  
-Il numero sarà la coordinata X dove individuare lo spurgo | min /   
max /   
Numero | Max |  
| variabile_ugello_Prime_inizio_e | Dove vogliamo individuare la nostra linea di spurgo:  
-Min lo farà a y = 0 (più un piccolo margine di sicurezza)  
-Max lo farà a y = max (meno un piccolo margine di sicurezza)  
-Il numero sarà la coordinata e dove individuare lo spurgo | min /   
max /   
numero | min |  
| variabile_ugello_Prime_direzione | L'indirizzo della nostra linea o caduta:  
-All'indietro la testa si sposterà nella parte anteriore della stampante  
-Gli attaccanti si sposteranno sul retro  
-L'auto andrà al centro a seconda della variabile_ugello_Prime_inizio_e | auto /   
in avanti /   
all'indietro | auto |

#### Carico/scarico delle riprese

In questo caso, questo gruppo di variabili faciliterà la gestione del carico e dello scarico del nostro filamento utilizzato nell'emulazione dell'M600, ad esempio o lanciando le macro del filamento di carico e scarico:

| Variabile                               | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                         | Valori possibili | Valore predefinito |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_filamento_scaricare_lunghezza | Quanto si ritira in mm il filamento, regola la macchina, normalmente la misura dall'ugello agli ingranaggi del tuo estrusore aggiungendo un margine extra.                                                                                                                                                                                                                                                          | numero           | 130                |
| variabile_filamento_scaricare_velocità  | Velocità di ritrattazione del filamento in mm/sec Normalmente viene utilizzata una velocità lenta.                                                                                                                                                                                                                                                                                                                  | numero           | 5                  |
| variabile_filamento_carico_lunghezza    | Distanza in mm per caricare il nuovo filamento ... come in variabile_filamento_scaricare_Lunghezza utilizzeremo la misura dalla tua attrezzatura a Extrusder aggiungendo un margine extra, in questo caso questo valore extra dipenderà da quanto si desidera essere spurgati ... Di solito puoi dargli più margine del valore precedente per assicurarsi che sia purificato l'estrusione del filamento precedente. | numero           | 150                |
| variabile_filamento_carico_velocità     | La velocità di carico del filamento in mm/sec normalmente viene utilizzata una velocità più rapida.                                                                                                                                                                                                                                                                                                                 | numero           | 10                 |

{ % SIT STYE = "Avviso" %}  
Un'altra regolazione necessaria per la tua sezione\[estrusore]L'indicato[**max_estrudere_soltanto_distanza**](https://www.klipper3d.org/Config_Reference.html#extruder)... Il valore consigliabile è generalmente> 101 (se non è definito utilizza 50) per consentire i tipici test di calibrazione degli estrusore.   
È necessario regolare il valore in base a quanto sopra del test o sulla configurazione del tuo**variabile_filamento_scaricare_lunghezza**IO**variabile_filamento_carico_lunghezza**.  
{% di endhint%}

#### Parcheggio

In alcuni processi della nostra stampante, come il tempo libero, è consigliabile fare un parcheggio della nostra testa. Le macro del nostro pacchetto hanno questa opzione oltre alle seguenti variabili da gestire:

| Variabile                                 | Descrizione                                                                                                                                                                                                                                                                | Valori possibili | Valore predefinito |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_inizio_stampa_parco_In          | Posizione dove parcheggiare la testa durante il pre-scansion.                                                                                                                                                                                                              | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                                   | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_inizio_stampa_parco_Con_altezza | Z altezza durante il prezioso                                                                                                                                                                                                                                              | numero           | 50                 |
| variabile_FINE_stampa_parco_In            | Posizione per parcheggiare la testa alla fine o annullare un'impressione.                                                                                                                                                                                                  | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                                   | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_FINE_stampa_parco_Con_salto     | Distanza per salire alla fine dell'impressione.                                                                                                                                                                                                                            | numero           | 20                 |
| variabile_pausa_stampa_parco_In           | Posizione per parcheggiare la testa di Pausar l'impressione.                                                                                                                                                                                                               | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                            |                  |                    |
| davanti                                   | Indietro                                                                                                                                                                                                                                                                   |                  |                    |
| variabile_pausa_oziare_tempo scaduto      | Valore, in pochi secondi, dell'attivazione del processo di inattività nella macchina che rilascia motori e perdita di coordinate,**È consigliabile un valore elevato per attivare la macro pausa abbastanza da eseguire qualsiasi azione prima di perdere le coordinate.** | numero           | 43200              |

#### Z-Tilt

Prendi il massimo dalla nostra macchina in modo che sia auto -livello e faciliti che la nostra macchina sia sempre nelle migliori condizioni è essenziale.

**Z-Tilt è fondamentalmente un processo che ci aiuta ad allineare i nostri motori Z rispetto al nostro asse x (cartesiano) o XY (corexy) (corexy)**. Con questo**Assicuriamo di avere sempre la nostra Z perfettamente e in modo preciso e automatico**.

| Variabile                         | Descrizione                                                                                                   | Valori possibili | Valore predefinito |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrare_Con_inclinare | Consente, nel caso di averlo abilitato nella nostra configurazione Klipper, il processo di regolazione Z-Tilt | Vero / falso     | Falso              |

#### Inclinarsi

L'uso di[Inclinarsi](broken-reference)Per la correzione o l'adeguamento preciso delle nostre stampanti è estremamente consigliabile se abbiamo deviazioni nelle nostre impressioni. Usando la seguente variabile possiamo consentire l'uso nelle nostre macro:

| Variabile                    | Descrizione                                                                                                                                                                                                                                   | Valori possibili | Valore predefinito     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------- |
| variabile_inclinarsi_profilo | Ti consente di tenere conto del nostro profilo di disgusto che verrà addebitato nella nostra macro start_Stampa. Per attivarlo, dobbiamo discutere la variabile e utilizzare il nome del profilo di inclinazione della nostra configurazione. | testo            | Mio_inclinarsi_profilo |

### Personalizzazione delle macro

Il nostro modulo Klipper utilizza il sistema di configurazione modulare utilizzato in tempi e sfrutta i vantaggi di Klipper nel processo del file di configurazione in sequenza. Questo è il motivo per cui è essenziale che l'ordine degli aggiustamenti includono e personalizzati che vogliamo applicare su questi moduli.

{ % suggerimenti style = "info" %}  
Quando si utilizzano le impostazioni di 3dwork come modulo, non possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura (limitato alla solo lettura) per sicurezza.

Ecco perché è molto importante capire il funzionamento di Klipper e come personalizzare i nostri moduli sulla macchina.  
{% di endhint%}

#### **Personalizzare le variabili**

Normalmente, sarà ciò che dovremo regolare, per apportare modifiche alle variabili che abbiamo per impostazione predefinita nel nostro modulo**3dwork**Para tagli.

Semplicemente, quello che dobbiamo fare è incollare il contenuto macro\[Gcode_macro globale_DI CHI]Cosa possiamo trovare in macro/macro_Nostro_Globals.cfg nella nostra stampa.cfg.

Ti ricordiamo cosa è stato precedentemente commentato su come Klipper elabora le configurazioni in sequenza, quindi è consigliabile incollarle dopo le incluse[Qui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Avremo qualcosa del genere (è solo un esempio visivo):

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

{ % SIT STYE = "Avviso" %}
I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.
{ % endhint %}

{ % suggerimenti style = "info" %}

-   Ti consigliamo di aggiungere commenti come vedi nel caso precedente per identificare ciò che ogni sezione fa
-   Anche se non è necessario toccare tutte le variabili che ti consigliano di copiare l'intero contenuto di\[Gcode_macro globale_DI CHI]{% di endhint%}

#### Personalizzazione delle macro

Le macro si sono montate in modo modulare in modo che possano essere regolate in modo semplice. Come abbiamo detto prima, se vogliamo regolarli dobbiamo procedere proprio come abbiamo fatto con le variabili, copiare la macro in questione nella nostra stampante.cfg (o altro includi il nostro) e assicurati che sia dopo l'inclusione di dove aggiungiamo il nostro modulo di 3dwork per Klipper.

Abbiamo due gruppi di macro:

-   Macro Per aggiungere le impostazioni dell'utente, queste macro possono essere facilmente aggiunte e personalizzate perché sono state aggiunte in modo che qualsiasi utente possa personalizzare le azioni a loro piacimento in una certa parte dei processi che ogni macro fa.

**INIZIO_STAMPA**

| Nome macro                                          | Descrizione                                                                                                                            |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| \_UTENTE_INIZIO_STAMPA_CALORE_CAMERA                | Funziona subito dopo che il nostro recinto inizia il riscaldamento, se la camera_Passi iniziali come parametro al nostro inizio_STAMPA |
| \_UTENTE_INIZIO_STAMPA_PRIMA_Homing                 | Viene eseguito prima dell'homing iniziale per l'inizio della stampa                                                                    |
| \_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO     | Funziona quando il nostro letto arriva alla sua temperatura, prima_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO                              |
| \_UTENTE_INIZIO_STAMPA_LETTO_MAGLIA                 | È lanciato prima_INIZIO_STAMPA_LETTO_MAGLIA                                                                                            |
| \_UTENTE_INIZIO_STAMPA_PARCO                        | È lanciato prima_INIZIO_STAMPA_PARCO                                                                                                   |
| \_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_Estrusore | È lanciato prima_INIZIO_STAMPA_DOPO_RISCALDAMENTO_Estrusore                                                                            |

**FINE_STAMPA**

| Nome macro                                     | Descrizione                                                                                   |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------- |
| \_UTENTE_FINE_STAMPA_PRIMA_Riscaldatori_SPENTO | Viene eseguito prima di eseguire il riscaldatore, prima_FINE_STAMPA_PRIMA_Riscaldatori_SPENTO |
| \_UTENTE_FINE_STAMPA_DOPO_Riscaldatori_SPENTO  | Viene eseguito dopo l'arresto del riscaldatore, prima_FINE_STAMPA_DOPO_Riscaldatori_SPENTO    |
| \_UTENTE_FINE_STAMPA_PARCO                     | Viene eseguito prima della testa della testa, prima_FINE_STAMPA_PARCO                         |

**STAMPA_Nozioni di base**

| Nome macro                 | Descrizione                               |
| -------------------------- | ----------------------------------------- |
| \_UTENTE_PAUSA_INIZIO      | Viene eseguito all'inizio di una pausa    |
| \_UTENTE_PAUSA_FINE        | Funziona alla fine di una pausa           |
| \_UTENTE_RIPRENDERE_INIZIO | Viene eseguito all'inizio di un riassunto |
| \_UTENTE_RIPRENDERE_FINE   | Corre alla fine di un riassunto           |

-   Macro interne, sono macro per dividere la macro principale in processi ed è importante per questo. È consigliabile che, in caso di richiedere che vengano copiati così com'è.

**INIZIO_STAMPA**

| Nome macro                                   | Descrizione                                                                                                                                                                                                                             |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_INIZIO_STAMPA_CALORE_CAMERA                | Riscalda il recinto nel caso in cui il parametro della camera_Early è ricevuto dalla nostra macro inizio_Stampare dal laminatore                                                                                                        |
| \_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO     | Funziona quando il letto arriva a temperatura, dopo_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_Letto. Normalmente, viene utilizzato per l'elaborazione della calibrazione del letto (Z_INCLINARE_Regola, quad_Cavalletto_LIVELLAMENTO,...) |
| \_INIZIO_STAMPA_LETTO_MAGLIA                 | È responsabile della logica della miseria del letto.                                                                                                                                                                                    |
| \_INIZIO_STAMPA_PARCO                        | Attacco la testa di stampa mentre riscalda l'ugello alla temperatura di stampa.                                                                                                                                                         |
| \_INIZIO_STAMPA_DOPO_RISCALDAMENTO_Estrusore | Fai spurgare e carica il profilo di inclinazione nel caso in cui definiamo nelle variabili                                                                                                                                              |

## Stampanti ed elettronici

Mentre lavoriamo con diversi modelli di stampanti ed elettronici, aggiungeremo quelli che non sono direttamente supportati da volte, sia che si tratti di contributi o di comunità.

-   Stampanti, in questa directory avremo tutte le configurazioni della stampante
-   Assi, qui troveremo l'elettronica

### Parametri e pin

Il nostro modulo Klipper utilizza il sistema di configurazione modulare utilizzato in tempi e sfrutta i vantaggi di Klipper nel processo del file di configurazione in sequenza. Questo è il motivo per cui è essenziale che l'ordine degli aggiustamenti includono e personalizzati che vogliamo applicare su questi moduli.

{ % suggerimenti style = "info" %}
Quando si utilizzano le impostazioni di 3dwork come modulo, non possono essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura (limitato alla solo lettura) per sicurezza.

Ecco perché è molto importante capire il funzionamento di Klipper e come personalizzare i nostri moduli sulla macchina.
{ % endhint %}

Come abbiamo spiegato in "[Personalizzazione delle macro](3dwork-klipper-bundle.md#personalizando-macros)"Useremo lo stesso processo per regolare i parametri o i pin per regolare le nostre esigenze.

#### Personalizzazione dei parametri

Mentre ti consigliamo di creare una sezione nella tua stampante.cfg che si chiama overrides utente, posizionata dopo l'inclusione delle nostre configurazioni, per poter regolare e personalizzare qualsiasi parametro utilizzato in esse.

Nel seguente esempio vedremo come nel nostro caso siamo interessati a personalizzare i parametri del nostro livellamento (letto_mesh) Regolazione dei punti di rilevamento (sonda_Conteggio) per quanto riguarda la configurazione che abbiamo per impostazione predefinita nelle configurazioni del nostro modulo Klipper:

{ % code title = "printer.cfg" %}

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

{ % SIT STYE = "Avviso" %}
I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.
{ % endhint %}

Possiamo usare lo stesso processo con qualsiasi parametro che vogliamo regolare.

#### Personalizzazione della configurazione dei pini

Procederemo esattamente come abbiamo fatto prima, nella nostra area di sostituzione dell'utente aggiungeremo quelle sezioni di pin che vogliamo adattarci ai nostri gusti.

Nel seguente esempio personalizzeremo qual è il perno della nostra ventola di elettronica (controller_Fan) per assegnarlo a uno diverso dal valore predefinito:

{ % code title = "printer.cfg" %}

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

{ % SIT STYE = "Avviso" %}
I tre punti (...) degli esempi precedenti devono semplicemente indicare che è possibile avere più configurazioni tra le sezioni ... in nessun caso se indossano.
{ % endhint %}

```

```
