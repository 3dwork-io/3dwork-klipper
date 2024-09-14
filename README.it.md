* * *

## descrizione: Pacchetto di macro, impostazioni e altre utilità per Klipper

# Pacchetto Clipper 3Dwork

[<img width="171" alt="kofi" src="https://github.com/3dwork-io/3dwork-klipper/blob/master/Ko-fi-Logo.png">](https://ko-fi.com/jjr3d)

[![](../../.gitbook/assets/image%20(1986).png)- Inglese](https://klipper-3dwork-io.translate.goog/klipper/mejoras/3dwork-klipper-bundle?_x_tr_sl=es&_x_tr_tl=en&_x_tr_hl=es&_x_tr_pto=wapp)

{% stile suggerimento="pericolo" %}  
**GUIDA IN PROCESSO!!! Sebbene le macro siano completamente funzionali, sono in continuo sviluppo.**

**Usateli a vostro rischio e pericolo!!!**  
{% suggerimento finale %}

Registro delle modifiche

07/12/2023 - Aggiunto il supporto per automatizzare la creazione del firmware elettronico Bigtreetech

Da**Lavoro 3D**Abbiamo raccolto e adattato una serie di macro, impostazioni della macchina e dell'elettronica, nonché altri strumenti per una gestione Klipper semplice e potente.

Gran parte di questo pacchetto è basato su[**Ratti**](https://os.ratrig.com/)migliorare le parti che riteniamo interessanti, così come altri contributi della community.

## Installazione

Per installare il nostro pacchetto per Klipper seguiremo i seguenti passaggi

### Scarica dal repository

Ci collegheremo al nostro host tramite SSH ed emetteremo i seguenti comandi:

    cd ~/printer_data/config
    git clone https://github.com/3dwork-io/3dwork-klipper.git

{% suggerimento stile="avviso" %}  
Se la directory di configurazione di Klipper è personalizzata, ricorda di modificare il primo comando in modo appropriato per la tua installazione.  
{% suggerimento finale %}

{% suggerimento stile="informazioni" %}  
Nelle nuove installazioni:

Dato che Klipper non consente l'accesso alle macro finché non ha un file Printer.cfg corretto e non si connette a un MCU, possiamo "ingannare" Klipper con i seguenti passaggi che ci permetteranno di utilizzare le macro nel nostro bundle, ad esempio, per lanciare il Macro compilazione firmware Klipper se utilizziamo elettroniche compatibili:

-   Ci assicuriamo di avere il nostro[host come secondo MCU](raspberry-como-segunda-mcu.md)
-   Successivamente aggiungeremo un Printer.cfg, ricorda che questi passaggi sono per un'installazione pulita in cui non hai alcun Printer.cfg e vuoi avviare la macro per creare firmware, come quello che puoi vedere qui sotto:


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

Con questo possiamo avviare Klipper per darci accesso alle nostre macro.  
{% suggerimento finale %}

### Usa Moonraker per essere sempre aggiornato

Grazie a Moonraker possiamo utilizzare il suo aggiornamento_manager per poter rimanere aggiornato sui miglioramenti che potremmo introdurre in futuro.

Da Mainsail/Fluidd modificheremo il nostro moonraker.conf (dovrebbe essere alla stessa altezza del vostro Printer.cfg) e aggiungeremo alla fine del file di configurazione:

    [include 3dwork-klipper/moonraker.conf]

{% suggerimento stile="avviso" %}  
**Ricordarsi di eseguire prima la fase di installazione, altrimenti Moonraker genererà un errore e non sarà in grado di avviarsi.**

**D'altra parte, se la directory della configurazione di Klipper è personalizzata, ricordati di adattare il percorso in modo appropriato alla tua installazione.**  
{% suggerimento finale %}

## Macro

Abbiamo sempre commentato che RatOS è una delle migliori distribuzioni Klipper, con supporto per i moduli Raspberry e CB1, in gran parte grazie alle sue configurazioni modulari e alle sue fantastiche macro.

Alcune macro aggiunte che ci saranno utili:

### **Macro per scopi generali**

| Macro                                                                   | Descrizione                                                                                                                                                                                           |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FORSE_CASA**                                                          | Ci consente di ottimizzare il processo di homing solo eseguendolo su quegli assi che non sono in homing.                                                                                              |
| **PAUSA**                                                               | Utilizzando le relative variabili, ci permette di gestire una pausa con un parcheggio della testa più versatile rispetto alle normali macro.                                                          |
| **IMPOSTATO_PAUSA_A_STRATO**                                            |                                                                                                                                                                                                       |
| **IMPOSTATO_PAUSA_A_PROSSIMO_STRATO**                                   | Una macro molto utile che Mainsail integra nella sua interfaccia utente per poter mettere in pausa su richiesta in un livello specifico... nel caso ce ne fossimo dimenticati durante la laminazione. |
| Ne abbiamo anche un altro per eseguire la pausa sul livello successivo. |                                                                                                                                                                                                       |
| **RIPRENDERE**                                                          | Migliorato poiché ci permette di rilevare se il nostro ugello non è alla temperatura di estrusione per risolverlo prima che mostri un errore e danneggi la nostra stampa.                             |
| **CANCELLARE_STAMPA**                                                   | Ciò consente l'utilizzo del resto delle macro per eseguire correttamente un annullamento di stampa.                                                                                                   |

-   **In pausa al cambio di livello**, alcune macro molto interessanti che ci permettono di mettere in pausa un livello o lanciare un comando all'avvio del livello successivo.   
    ![](../../.gitbook/assets/image%20(143).png)![](../../.gitbook/assets/image%20(1003).png)  
    Inoltre, un altro vantaggio è che sono integrati con Mainsail, quindi avremo nuove funzioni nella nostra interfaccia utente, come puoi vedere di seguito:  
    ![](../../.gitbook/assets/image%20(725).png)![](../../.gitbook/assets/image%20(1083).png)

### **Macro di gestione della stampa**

| Macro                                                                                      | Descrizione                                                                                                                                                         |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **INIZIO_STAMPA**                                                                          | Ci permetterà di avviare le nostre stampe in modo sicuro e in stile Klipper. All'interno di questo troveremo alcune funzioni interessanti come:                     |
| -preriscaldamento intelligente degli ugelli in caso di sensore sonda                       |                                                                                                                                                                     |
| -possibilità di utilizzare z-tilt tramite variabile                                        |                                                                                                                                                                     |
| -Materasso da letto adattivo, forzato o da borsa riposta                                   |                                                                                                                                                                     |
| -Linea di spurgo personalizzabile tra linea di spurgo normale, adattiva o goccia di spurgo |                                                                                                                                                                     |
| -macro segmentata per poterla personalizzare come vi mostreremo in seguito                 |                                                                                                                                                                     |
| **FINE_STAMPA**                                                                            | Fine della macro di stampa in cui abbiamo anche la segmentazione per poter personalizzare la nostra macro. Disponiamo anche di un parcheggio dinamico per la testa. |

-   **Rete da letto adattiva**Grazie alla versatilità di Klipper possiamo fare cose che oggi sembrano impossibili... un processo importante per la stampa è avere una rete di deviazioni nel nostro letto che ci permette di correggerle per avere una perfetta adesione dei primi strati.   
    In molte occasioni eseguiamo questo meshing prima della stampa per assicurarci che funzioni correttamente e questo viene fatto su tutta la superficie del nostro letto.  
    Con il meshing del letto adattivo, questo verrà fatto nell'area di stampa, rendendolo molto più preciso rispetto al metodo tradizionale... negli screenshot seguenti vedremo le differenze tra una mesh tradizionale e una adattiva.  
    ![](../../.gitbook/assets/image%20(1220).png)![](../../.gitbook/assets/image%20(348).png)

### **Macro di gestione del filamento**

Insieme di macro che ci permetteranno di gestire diverse azioni con il nostro filamento, come caricarlo o scaricarlo.

| Macro                   | Descrizione                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| **M600**                | Ci consentirà la compatibilità con il gcode M600 normalmente utilizzato nei laminatori per il cambio filamento. |
| **SCARICARE_FILAMENTO** | Configurabile attraverso le variabili, ci consentirà la scarica assistita del filamento.                        |
| **CARICO_FILAMENTO**    | Uguale al precedente ma relativo al carico del filamento.                                                       |

### **Macro di gestione delle bobine di filamento (Spoolman)**

{% suggerimento stile="avviso" %}  
**SEZIONE IN PROCESSO!!!**  
{% suggerimento finale %}

[**Bobinatore**](https://github.com/Donkie/Spoolman)è un gestore di bobine di filamenti integrato in Moonraker e che ci consente di gestire lo stock e la disponibilità dei nostri filamenti.

!\[](../../.gitbook/assets/image (1990).png)

Non entreremo nei dettagli dell'installazione e della configurazione di questo poiché è relativamente semplice utilizzare il file[**istruzioni dal tuo Github**](https://github.com/Donkie/Spoolman)**,**comunque**Ti consigliamo di utilizzare Docker**per semplicità e ricordo**attivare le impostazioni in Moonraker**necessario:

{% code title="moonraker.conf" %}

    [spoolman]
    server: http://192.168.0.123:7912
    #   URL to the Spoolman instance. This parameter must be provided.
    sync_rate: 5
    #   The interval, in seconds, between sync requests with the
    #   Spoolman server.  The default is 5.

{%endcode%}

| Macro                   | Descrizione                                                     |
| ----------------------- | --------------------------------------------------------------- |
| IMPOSTATO_ATTIVO_BOBINA | Ci permette di indicare quale è l'ID della bobina da utilizzare |
| CHIARO_ATTIVO_BOBINA    | Ci permette di resettare la bobina attiva                       |

L’ideale in ogni caso sarebbe aggiungere alla nostra plastificatrice,**nei gcode del filamento per ogni bobina la chiamata a questo**, e ricorda**cambiare il suo ID una volta consumato**per poter tenere traccia di ciò che rimane di filamento al suo interno!!!

!\[](../../.gitbook/assets/image (1991).png)

### **Macro di gestione della superficie di stampa**

{% suggerimento stile="avviso" %}  
**SEZIONE IN PROCESSO!!!**  
{% suggerimento finale %}

Di solito è normale avere superfici di stampa diverse a seconda della finitura che vogliamo ottenere o del tipo di filamento.

Questo set di macro, creato da[Garethky](https://github.com/garethky), ci permetteranno di avere il controllo di questi e soprattutto la corretta regolazione di ZOffset in ciascuno di essi nello stile che abbiamo nelle macchine Prusa. Di seguito puoi vedere alcune delle sue funzioni:

-   Possiamo memorizzare il numero di superfici di stampa che desideriamo, ognuna con un nome univoco
-   ogni superficie di stampa avrà il proprio ZOffset
-   Se effettuiamo regolazioni Z durante una stampa (Babystepping) dal nostro Klipper, questa modifica verrà memorizzata nella superficie abilitata in quel momento

D'altra parte ne abbiamo alcuni**requisiti per implementarlo (cercheremo di aggiungere la logica PRINT_START del bundle in futuro attivando questa funzione tramite variabile e creando una macro utente precedente e successiva per poter inserire eventi utente)**:

-   l'uso di\[salva_variabili]Nel nostro caso utilizzeremo ~/variables.cfg per memorizzare le variabili e questo è già all'interno del cfg di queste macro.   
    Questo creerà automaticamente un file di variabili per noi_costruire_fogli.cfg dove salverà le nostre variabili su disco.

{% code title="Esempio di file di configurazione delle variabili" %}

    [Variables]
    build_sheet flat = {'name': 'flat', 'offset': 0.0}
    build_sheet installed = 'build_sheet textured_pei'
    build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
    build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}

{%endcode%}

-   dobbiamo includere una chiamata a APPLICARE_COSTRUIRE_FOGLIO_REGOLAZIONE nella nostra STAMPA_INIZIA per poter applicare lo ZOffset della superficie selezionata
-   È importante che per la macro precedente, APPLY_COSTRUIRE_FOGLIO_REGOLAZIONE, per funzionare correttamente dobbiamo aggiungere un SET_CODICE G_OFFSET Z=0.0 subito prima di chiamare APPLY_COSTRUIRE_FOGLIO_REGOLAZIONE


    # Load build sheet
    SHOW_BUILD_SHEET                ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0          ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT    ; apply build sheet loaded zoffset

D'altra parte, è interessante avere delle macro per attivare questa o quella superficie o addirittura passarla come parametro dal nostro laminatore in modo che con diversi profili di stampante o filamento possiamo caricare l'una o l'altra automaticamente:

{% suggerimento stile="avviso" %}  
È importante che il valore in NAME="xxxx" corrisponda al nome che abbiamo assegnato durante l'installazione della nostra superficie di stampa  
{% suggerimento finale %}

{% code title="printer.cfg o include cfg" %}

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

Anche nel caso di KlipperScreen possiamo aggiungere un menu specifico per gestire il caricamento delle diverse superfici, dove includeremo una chiamata alle macro precedentemente create per il caricamento di ciascuna superficie:

{% titolo codice="~/printer_dati/config/KlipperScreen.conf" %}

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

| Macro                              | Descrizione |
| ---------------------------------- | ----------- |
| INSTALLARE_COSTRUIRE_FOGLIO        |             |
| SPETTACOLO_COSTRUIRE_FOGLIO        |             |
| SPETTACOLO_COSTRUIRE_FOGLI         |             |
| IMPOSTATO_COSTRUIRE_FOGLIO_OFFSET  |             |
| RESET_COSTRUIRE_FOGLIO_OFFSET      |             |
| IMPOSTATO_CODICE G_OFFSET          |             |
| APPLY_COSTRUIRE_FOGLIO_REGOLAZIONE |             |

### **Macro di configurazione macchina**

| Macro                                                  | Descrizione                                                                                                                                                                                                                      |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILARE_FIRMWARE**                                 | Con questa macro possiamo compilare il firmware di Klipper in modo semplice, avere il firmware accessibile dalla UI per una maggiore semplicità e poterlo applicare alla nostra elettronica.                                     |
| Qui hai maggiori dettagli sull'elettronica supportata. |                                                                                                                                                                                                                                  |
| **CALCOLARE_LETTO_MAGLIA**                             | Una macro estremamente utile per calcolare l'area della nostra mesh perché a volte può essere un processo complicato.                                                                                                            |
| **PID_TUTTO**                                          |                                                                                                                                                                                                                                  |
| **PID_ESTRUSORE**                                      |                                                                                                                                                                                                                                  |
| **PID_LETTO**                                          | Queste macro, dove possiamo passare le temperature al PID sotto forma di parametri, ci permetteranno di eseguire la calibrazione della temperatura in modo estremamente semplice.                                                |
| **TEST_VELOCITÀ**                                      |                                                                                                                                                                                                                                  |
| **TEST_VELOCITÀ_DELTA**                                | La macro originale del compagno[Ellis](https://github.com/AndrewEllis93)Ci permetteranno in modo abbastanza semplice di testare la velocità con cui possiamo muovere la nostra macchina con precisione e senza perdita di passi. |

-   **Firmware compilato per l'elettronica supportata**, per facilitare il processo di creazione e manutenzione del firmware Klipper per i nostri MCU abbiamo la macro COMPILE_FIRMWARE che una volta eseguito, possiamo usare la nostra elettronica come parametro per fare solo questo, compilerà Klipper per tutta l'elettronica supportata dal nostro bundle:  
    ![](../../.gitbook/assets/image%20(1540).png)  
    Li troveremo facilmente accessibili dalla nostra interfaccia utente web nella directory del firmware_binari nella nostra scheda MACCHINA (se usiamo la randa):  
    ![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)  
    Di seguito è riportato l'elenco dei dispositivi elettronici supportati:

**IMPORTANTE!!!**

Questi script sono preparati per funzionare su un sistema Raspbian con utente pi, se non è il tuo caso dovrai adattarlo.

I firmware vengono generati per l'utilizzo con una connessione USB, che è sempre ciò che consigliamo. Inoltre, il punto di montaggio USB è sempre lo stesso, quindi la configurazione della connessione MCU non cambierà se vengono generati con la nostra macro/script.

**Affinché Klipper possa eseguire le macro della shell, deve essere installata un'estensione, grazie al compagno**[**Arcasina**](https://github.com/Arksine)**, che lo consente.**

**A seconda della distribuzione Klipper utilizzata, potrebbero essere già abilitati.**

![](../../.gitbook/assets/image%20(770).png)

Il modo più semplice è usare[**Oh**](../instalacion/#instalando-kiauh)dove troveremo in una delle sue opzioni la possibilità di installare questa estensione:

![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg)

Possiamo anche eseguire il processo manualmente, copieremo manualmente il plugin per Klipper[**gcode_conchiglia_estensione**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)all'interno della nostra directory`_**~/klipper/klippy/extras**_`utilizzando SSH o SCP e riavviare Klipper.

| Elettronica             | Nome del parametro da utilizzare nella macro |
| ----------------------- | -------------------------------------------- |
| Manta E                 | Con orgoglio                                 |
| Dimentica M4P           | btt-manta-m4p                                |
| Manta M4P v2.a          | btt-manta-m4p-22                             |
| Manta M8P               | btt-manta-m8p                                |
| Manta M8P v1.1          | btt-manta-m8p-11                             |
| Polpo Max EZ            | btt-octopus-max-it                           |
| Polpo Pro (446)         | btt-octopus-pro-446                          |
| Polpo Pro (429)         | btt-octopus-pro-429                          |
| Polpo Pro (H723)        | btt-octopus-pro-h723                         |
| Polpo v1.1              | btt-polpo-11                                 |
| Polpo v1.1 (407)        | btt-polpo-11-407                             |
| SKR Pro v1.2            | scr_pro_12                                   |
| SKR 3                   | btt_scr_3                                    |
| Saqr A (Ahah)           | Lo fai ubriacare                             |
| SKR 3EZ                 | questo è btt-skr-3                           |
| Saqr A Idha (Haha)      | btt-skr-3-ez-h723                            |
| 2 corone svizzere (429) | btt-skr-2-429                                |
| 2 corone svizzere (407) | btt-skr-2-407                                |
| RATTO SKR               | btt-risate-10                                |
| SKR 1.4 Turbo           | btt-skr-14-turbo                             |
| SKR Mini Ez vz          | btt_scr_mini_es_30                           |

| Testa portautensili (CAN) | Nome del parametro da utilizzare nella macro |
| ------------------------- | -------------------------------------------- |
| EBB42v1                   | btt_riflusso42_10                            |
| EBB36v1                   | btt_riflusso36_10                            |
| EBB42 v1.1                | btt_riflusso42_11                            |
| EBB36 v1.1                | btt_riflusso36_11                            |
| EBB42 v1.2                | btt_riflusso42_12                            |
| EBB36 v1.2                | btt_riflusso36_12                            |

| **Elettronica**      | **Nome del parametro da utilizzare nella macro** |
| -------------------- | ------------------------------------------------ |
| MKS Eagle v1.x       | mks-eagle-10                                     |
| MKS Robin Nano v3    | mks-robin-nano-30                                |
| MKS Robin Nano v2    | mks-robin-nano-20                                |
| MKS Gen L            | mks-gen-l                                        |
| ZNP Robin Nano DW v2 | zeg_pettirosso_nano_dw_Classe                    |

| Testa portautensili (CAN) | Nome del parametro da utilizzare nella macro |
| ------------------------- | -------------------------------------------- |
| Dolce FLY SHT 42          | dolce_volare_merda_42                        |
| Dolce FLY SHT 36          | dolce_volare_merda_36                        |

| Elettronica   | Nome del parametro da utilizzare nella macro |
| ------------- | -------------------------------------------- |
| Fysetc Spider | fyset ecc_ragno                              |

### Aggiunta di macro 3Dwork alla nostra installazione

Dalla nostra interfaccia, Mainsail/Fluidd, modificheremo il nostro print.cfg e aggiungeremo:

{% titolo codice="printer.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{%endcode%}

{% suggerimento stile="informazioni" %}  
È importante aggiungere queste righe alla fine del nostro file di configurazione... appena sopra la sezione in modo che se ci sono macro nel nostro cfg o include, verranno sovrascritte dalle nostre:  
#\*# \\&lt;---------------------- SALVA_CONFIGURAZIONE ----------------------->  
{% suggerimento finale %}

{% suggerimento stile="avviso" %}  
Le macro normali sono state separate da**shell delle macro**dato questo**Per abilitarli è necessario eseguire manualmente ulteriori passaggi, oltre a quelli attualmente in fase di test.**E\*\*Potrebbero richiedere autorizzazioni aggiuntive per assegnare autorizzazioni di esecuzione per le quali non sono state indicate le istruzioni poiché stanno tentando di automatizzare.\*\*  
**Se li usi è a tuo rischio e pericolo.**  
{% suggerimento finale %}

### Configurazione della nostra plastificatrice

Poiché le nostre macro sono dinamiche, estrarranno determinate informazioni dalla configurazione della nostra stampante e dal laminatore stesso. Per fare ciò, vi consigliamo di configurare le vostre plastificatrici come segue:

-   **avvia gcode INIZIA_STAMPA**, utilizzando i segnaposto per trasmettere dinamicamente i valori della temperatura del filamento e del letto:

{% schede %}  
{% titolo scheda="PrusaSlicer-SuperSlicer" %}  
**PrusaSlicer**

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

**SuperSlicer**- abbiamo la possibilità di regolare la temperatura della custodia (CAMERA)

    M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

![Ejemplo para PrusaSlicer/SuperSlicer](../../.gitbook/assets/image%20(1104).png)  
{% fine perdita %}

{% titolo scheda="Bambu Studio/OrcaSlicer" %}

    M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
    M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
    SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
    START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}

!\[](../../.gitbook/assets/image (1760).png){% endtab %}

{% titolo della scheda="Cura" %}

    START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%

{% suggerimento stile="avviso" %}  
Dovremo installare il plugin[**Plug-in post-processo (di Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)dal menù_**Aiuto/Mostra**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.   
Riavviamo Cura e andremo a_**Estensioni/Post elaborazione/Modifica G-Code**_e selezioneremo_**Dimensioni di stampa mesh**_.  
{% suggerimento finale %}  
{% fine perdita %}

{% titolo scheda="IdeaMaker" %}

    START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}

{% fine perdita %}

{% titolo scheda="Semplifica3D" %}

    START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]

{% fine perdita %}  
{% tabelle finali %}

{% suggerimento stile="informazioni" %}  
IL**i placeholder sono "alias" o variabili che i laminatori utilizzano in modo che durante la generazione del gcode vengano sostituiti dai valori configurati nel profilo**stampa.

Nei seguenti link è possibile trovarne un elenco per:[**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(oltre a quelli sopra),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)E[**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

L'uso di questi consente alle nostre macro di essere dinamiche.  
{% suggerimento finale %}

-   **gcode della fine finale_STAMPA**, in questo caso l'assenza di segnaposto è comune a tutte le plastificatrici


    END_PRINT

### Variabili

Come abbiamo già accennato, queste nuove macro ci permetteranno di avere alcune funzioni molto utili che abbiamo elencato sopra.

Per adattarli alla nostra macchina utilizzeremo le variabili che troveremo in macro/macro_era_globals.cfg e che dettagliamo di seguito.

#### Lingua del messaggio/notifica

Poiché a molti utenti piace avere notifiche macro nella loro lingua, abbiamo ideato un sistema di notifica multilingue, attualmente spagnolo (es) e inglese (en). Nella seguente variabile possiamo regolarlo:

| Variabile        | Descrizione                                                                                                | Valori possibili | Valore predefinito |
| ---------------- | ---------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_lingua | Ci permette di selezionare la lingua delle notifiche. Se non è ben definito, verrà utilizzato in (inglese) | è/in             | È                  |

#### Estrusione relativa

Ci permette di controllare quale modalità di estrusione utilizzeremo alla fine del nostro START.\_STAMPA Il valore dipenderà dalla configurazione del nostro laminatore.

{% suggerimento stile="successo" %}  
È consigliabile configurare la plastificatrice per utilizzare l'estrusione relativa e impostare questa variabile su True.  
{% suggerimento finale %}

| Variabile                     | Descrizione                                                                                | Valori possibili | Valore predefinito |
| ----------------------------- | ------------------------------------------------------------------------------------------ | ---------------- | ------------------ |
| variabile_relativo_estrusione | Ci permette di indicare la modalità di estrusione utilizzata nella nostra plastificatrice. | Vero/falso       | VERO               |

#### Velocità

Per gestire le velocità utilizzate nelle macro.

| Variabile                        | Descrizione                            | Valori possibili | Valore predefinito |   |
| -------------------------------- | -------------------------------------- | ---------------- | ------------------ | - |
| variabile_macro_viaggio_velocità | Velocità di trasferimento              | numerico         | 150                |   |
| variabile_macro_Con_velocità     | Velocità di trasferimento per l'asse Z | numerico         | 15                 |   |

#### Homing

Insieme di variabili relative al processo di homing.

| Variabile | Descrizione | Valori possibili | Valore predefinito |
| --------- | ----------- | ---------------- | ------------------ |

#### Riscaldamento

Variabili legate al processo di riscaldamento della nostra macchina.

| Variabile                                        | Descrizione                                                                                                     | Valori possibili | Valore predefinito |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_preriscaldare_estrusore                | Permette il preriscaldamento dell'ugello alla temperatura indicata nella variabile_preriscaldare_estrusore_temp | Vero/falso       | VERO               |
| variabile_preriscaldare_estrusore_temp           | Temperatura di preriscaldamento dell'ugello                                                                     | numerico         | 150                |
| variabile_inizio_stampa_Calore_camera_letto_temp | Temperatura del letto durante il processo di riscaldamento del nostro recinto                                   | numerico         | 100                |

{% suggerimento stile="successo" %}  
Vantaggi dell'utilizzo dell'ugello preriscaldato:

-   Ci concede tempo aggiuntivo affinché il letto possa raggiungere la sua temperatura in modo uniforme.
-   Se utilizziamo un sensore induttivo che non dispone di compensazione della temperatura, le nostre misurazioni saranno più coerenti e precise.
-   Permette di ammorbidire eventuali residui di filamento nell'ugello, il che significa che, in alcune configurazioni, questi residui non influenzano l'attivazione del sensore.  
    {% suggerimento finale %}

#### Rete da letto

Per controllare il processo di livellamento abbiamo variabili che possono essere molto utili. Ad esempio, possiamo controllare il tipo di livellamento che vogliamo utilizzare creando sempre una nuova mesh, caricandone una precedentemente memorizzata o utilizzando la mesh adattiva.

| Variabile                                                                                                    | Descrizione                                                                         | Valori possibili | Valore predefinito |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrare_letto_maglia                                                                             | Ci permette di selezionare quale tipo di mesh utilizzeremo nel nostro START_STAMPA: |                  |                    |
| -nuova mesh, mesherà ogni stampa                                                                             |                                                                                     |                  |                    |
| -storedmesh, caricherà una mesh memorizzata e non eseguirà il polling del letto                              |                                                                                     |                  |                    |
| -adattivo, ci creerà una nuova mesh ma adattata all'area di stampa, spesso migliorando i nostri primi strati |                                                                                     |                  |                    |
| -nomesh, nel caso in cui non disponiamo di un sensore o utilizziamo la mesh per saltare il processo          | nuova mesh / mesh memorizzata / adattiva /                                          |                  |                    |
| nomi                                                                                                         | adattivo                                                                            |                  |                    |
| variabile_letto_maglia_profilo                                                                               | Il nome utilizzato per la nostra mesh archiviata                                    | testo            | predefinito        |

{% suggerimento stile="avviso" %}  
Ti consigliamo di utilizzare il livellamento adattivo poiché adatterà sempre la mesh alla dimensione della nostra stampa, consentendoti di avere un'area della mesh regolata.

È importante che abbiamo nel nostro[avvia il gcode della nostra plastificatrice](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), nella chiamata al nostro START_STAMPA, STAMPA valori_MAX e STAMPA_MINIMO  
{% suggerimento finale %}

#### epurato

Una fase importante del nostro inizio stampa è un corretto spurgo dei nostri ugelli per evitare che restino filamenti o che questi possano danneggiare la nostra stampa ad un certo punto. Di seguito sono riportate le variabili che intervengono in questo processo:

| Variabile                                                                                                                                                               | Descrizione                                       | Valori possibili | Valore predefinito |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------- | ------------------ |
| variabile_ugello_adescamento                                                                                                                                            | Possiamo scegliere tra diverse opzioni di spurgo: |                  |                    |
| -primeline disegnerà la tipica linea di eliminazione                                                                                                                    |                                                   |                  |                    |
| -primelineadaptative genererà una linea di spurgo che si adatta all'area della parte stampata utilizzando la variabile_ugello_adescamento_distanza oggetto come margine |                                                   |                  |                    |
| -primeblob metterà una goccia di filamento in un angolo del nostro letto, molto efficace per pulire l'ugello e facile da rimuovere                                      |                                                   |                  |                    |
| linea principale /                                                                                                                                                      |                                                   |                  |                    |

primelineadaptive /   
blob principale /   
Falso

| linea primaria adattiva |  
| variabile_ugello_adescamento_distanza oggetto | Se utilizziamo la linea al vivo adattiva sarà il margine da utilizzare tra la linea al vivo e l'oggetto stampato | numerico | 5|  
| variabile_ugello_primo_inizio_x| Dove vogliamo posizionare la nostra linea di spurgo:  
-min lo farà a X=0 (più un piccolo margine di sicurezza)  
-max lo farà a X=max (meno un piccolo margine di sicurezza)  
-number sarà la coordinata X dove localizzare lo spurgo | minimo/   
massimo /   
numero | massimo |  
| variabile_ugello_primo_inizio_e | Dove vogliamo posizionare la nostra linea di spurgo:  
-min lo farà a Y=0 (più un piccolo margine di sicurezza)  
-max lo farà a Y=max (meno un piccolo margine di sicurezza)  
-numero sarà la coordinata Y dove individuare lo spurgo | minimo/   
massimo /   
numero | minimo |  
| variabile_ugello_primo_direzione | L'indirizzo della nostra linea o drop:  
-all'indietro la testa si sposterà verso la parte anteriore della stampante  
-gli avanti si sposteranno indietro  
-l'auto andrà verso il centro a seconda della variabile_ugello_primo_inizio_e | auto /   
avanti /   
all'indietro | automatico |

#### Carico/scarico filamento

In questo caso, questo gruppo di variabili faciliterà la gestione del caricamento e dello scaricamento del nostro filamento utilizzato in emulazione dell'M600, ad esempio, o quando si lanciano le macro di caricamento e scaricamento del filamento:

| Variabile                               | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                | Valori possibili | Valore predefinito |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_filamento_scaricare_lunghezza | Quanto ritrarre il filamento in mm, adattalo alla tua macchina, normalmente la misura dal tuo ugello agli ingranaggi del tuo estrusore aggiungendo un margine extra.                                                                                                                                                                                                                                                       | numero           | 130                |
| variabile_filamento_scaricare_velocità  | Velocità di ritrazione del filamento in mm/sec normalmente viene utilizzata una velocità lenta.                                                                                                                                                                                                                                                                                                                            | numero           | 5                  |
| variabile_filamento_carico_lunghezza    | Distanza in mm per caricare il nuovo filamento... oltre che in variabile_filamento_scaricare_lunghezza utilizzeremo la misura dal tuo ingranaggio all'estrusore aggiungendo un margine extra, in questo caso questo valore extra dipenderà da quanto vuoi che venga spurgato... normalmente puoi dargli più margine rispetto al valore precedente per assicurarti che il l'estrusione del filamento precedente sia pulita. | numero           | 150                |
| variabile_filamento_carico_velocità     | Velocità di caricamento del filamento in mm/sec, normalmente viene utilizzata una velocità maggiore rispetto alla velocità di scarico.                                                                                                                                                                                                                                                                                     | numero           | 10                 |

{% suggerimento stile="avviso" %}  
Un'altra impostazione necessaria per la tua sezione\[estrusore]indicare il[**massimo_estrudere_soltanto_distanza**](https://www.klipper3d.org/Config_Reference.html#extruder)...il valore consigliabile è solitamente >101 (se non definito, utilizzare 50) per consentire, ad esempio, tipici test di calibrazione dell'estrusore.   
Dovresti regolare il valore in base a quanto menzionato in precedenza sul test o sulla configurazione del tuo**variabile_filamento_scaricare_lunghezza**IO**variabile_filamento_carico_lunghezza**.  
{% suggerimento finale %}

#### Parcheggio

In alcuni processi della nostra stampante, come la pausa, è consigliabile parcheggiare la testa. Le macro nel nostro bundle hanno questa opzione oltre alle seguenti variabili da gestire:

| Variabile                                 | Descrizione                                                                                                                                                                                                                                                                                                           | Valori possibili | Valore predefinito |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_inizio_stampa_parco_In          | Posizione dove parcheggiare la testa durante il preriscaldamento.                                                                                                                                                                                                                                                     | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                                                                       |                  |                    |
| anteriore                                 | Indietro                                                                                                                                                                                                                                                                                                              |                  |                    |
| variabile_inizio_stampa_parco_Con_altezza | Altezza Z durante il preriscaldamento                                                                                                                                                                                                                                                                                 | numero           | 50                 |
| variabile_FINE_stampa_parco_In            | Posizione dove parcheggiare la testa quando si termina o si annulla una stampa.                                                                                                                                                                                                                                       | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                                                                       |                  |                    |
| anteriore                                 | Indietro                                                                                                                                                                                                                                                                                                              |                  |                    |
| variabile_FINE_stampa_parco_Con_salto     | Distanza da salire in Z alla fine della stampa.                                                                                                                                                                                                                                                                       | numero           | 20                 |
| variabile_pausa_stampa_parco_In           | Posizione dove parcheggiare la testa quando si mette in pausa la stampa.                                                                                                                                                                                                                                              | Indietro /       |                    |
| centro /                                  |                                                                                                                                                                                                                                                                                                                       |                  |                    |
| anteriore                                 | Indietro                                                                                                                                                                                                                                                                                                              |                  |                    |
| variabile_pausa_oziare_tempo scaduto      | Valore, in secondi, dell'attivazione del processo di inattività della macchina che sblocca i motori e provoca la perdita delle coordinate,**È consigliabile un valore alto in modo che quando si attiva la macro PAUSE ci voglia il tempo sufficiente per eseguire qualsiasi azione prima di perdere le coordinate.** | numero           | 43200              |

#### Inclinazione Z

Sfruttare al massimo la nostra macchina affinché si autolivella e garantire che la nostra macchina sia sempre nelle migliori condizioni è fondamentale.

**Z-TILT è fondamentalmente un processo che ci aiuta ad allineare i nostri motori Z rispetto al nostro asse/gantry X (cartesiano) o XY (CoreXY).**. con questo**ci assicuriamo che la nostra Z sia sempre allineata in modo perfetto, preciso e automatico**.

| Variabile                         | Descrizione                                                                                   | Valori possibili | Valore predefinito |
| --------------------------------- | --------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_calibrare_Con_inclinare | Permette, se abilitato nella nostra configurazione Klipper, il processo di regolazione Z-Tilt | Vero/falso       | Falso              |

#### Inclinare

L'uso di[INCLINAZIONE](broken-reference)Per la correzione o la regolazione precisa delle nostre stampanti è estremamente consigliabile se riscontriamo deviazioni nelle nostre stampe. Utilizzando la seguente variabile possiamo consentirne l'utilizzo nelle nostre macro:

| Variabile                      | Descrizione                                                                                                                                                                                                                                        | Valori possibili | Valore predefinito       |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------ |
| variabile_inclinazione_profilo | Ci consente di prendere in considerazione il nostro profilo di inclinazione che verrà caricato nella nostra macro START_STAMPA Per attivarlo dobbiamo decommentare la variabile e utilizzare il nome del profilo skew dalla nostra configurazione. | testo            | Mio_inclinazione_profilo |

### Personalizzazione macro

Il nostro modulo per Klipper utilizza il sistema di configurazione modulare utilizzato in RatOS e sfrutta i vantaggi di Klipper nell'elaborazione sequenziale dei file di configurazione. Questo è il motivo per cui l'ordine delle inclusioni e delle impostazioni personalizzate che vogliamo applicare a questi moduli è essenziale.

{% suggerimento stile="informazioni" %}  
Se utilizzate come modulo, le configurazioni 3Dwork NON POSSONO essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura per sicurezza.

Ecco perché è molto importante capire come funziona Klipper e come personalizzare i nostri moduli sulla tua macchina.  
{% suggerimento finale %}

#### **Personalizzazione delle variabili**

Normalmente, sarà ciò che dovremo aggiustare, per apportare modifiche alle variabili che abbiamo di default nel nostro modulo**Lavoro 3D**coppia Klipper.

Semplicemente, quello che dobbiamo fare è incollare il contenuto della macro\[gcode_macro GLOBALE_DI CHI]cosa possiamo trovare in macro/macro_era_globals.cfg nel nostro Printer.cfg.

Ricordiamo quanto detto in precedenza riguardo a come Klipper elabora le configurazioni in sequenza, quindi è consigliabile incollarlo dopo gli include di cui abbiamo parlato.[Qui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

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

{% suggerimento stile="avviso" %}
I tre punti (...) degli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}

{% suggerimento stile="informazioni" %}

-   Ti consigliamo di aggiungere commenti come vedi nel caso precedente per identificare cosa fa ciascuna sezione.
-   Sebbene non sia necessario modificare tutte le variabili, ti consigliamo di copiare tutto il contenuto di\[gcode_macro GLOBALE_DI CHI]{% suggerimento finale %}

#### Personalizzazione delle macro

Le macro sono state impostate in modo modulare in modo che possano essere facilmente modificate. Come abbiamo accennato prima, se vogliamo modificarle dovremo procedere come abbiamo fatto con le variabili, copiare la macro in questione nel nostro print.cfg (o in un altro nostro include) e assicurarci che sia dopo l'inclusione in cui abbiamo aggiunto il nostro modulo 3Dwork per Klipper.

Abbiamo due gruppi di macro:

-   Macro per aggiungere impostazioni utente, queste macro possono essere facilmente aggiunte e personalizzate perché sono state aggiunte in modo che qualsiasi utente possa personalizzare le azioni a proprio piacimento in alcune parti dei processi eseguiti da ciascuna macro.

**INIZIO_STAMPA**

| Nome della macro                                    | Descrizione                                                                                                                               |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| \_UTENTE_INIZIO_STAMPA_CALORE_CAMERA                | Viene eseguito subito dopo che il nostro recinto inizia a riscaldarsi, se CAMERA_TEMP viene passato come parametro al nostro START_STAMPA |
| \_UTENTE_INIZIO_STAMPA_PRIMA_RICERCA                | Eseguito prima dell'homing iniziale dell'avvio della stampa                                                                               |
| \_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO     | Viene eseguito quando il nostro letto raggiunge la sua temperatura, prima_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO                          |
| \_UTENTE_INIZIO_STAMPA_LETTO_MAGLIA                 | Viene rilasciato prima_INIZIO_STAMPA_LETTO_MAGLIA                                                                                         |
| \_UTENTE_INIZIO_STAMPA_PARCO                        | Viene rilasciato prima_INIZIO_STAMPA_PARCO                                                                                                |
| \_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_ESTRUSORE | Viene rilasciato prima_INIZIO_STAMPA_DOPO_RISCALDAMENTO_ESTRUSORE                                                                         |

**FINE_STAMPA**

| Nome della macro                               | Descrizione                                                                                     |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| \_UTENTE_FINE_STAMPA_PRIMA_RISCALDATORI_SPENTO | Viene eseguito prima di spegnere i riscaldatori, prima_FINE_STAMPA_PRIMA_RISCALDATORI_SPENTO    |
| \_UTENTE_FINE_STAMPA_DOPO_RISCALDATORI_SPENTO  | Viene eseguito dopo lo spegnimento dei riscaldatori, prima_FINE_STAMPA_DOPO_RISCALDATORI_SPENTO |
| \_UTENTE_FINE_STAMPA_PARCO                     | Viene eseguito prima che la testa sia parcheggiata, prima_FINE_STAMPA_PARCO                     |

**STAMPA_BASI**

| Nome della macro           | Descrizione                      |
| -------------------------- | -------------------------------- |
| \_UTENTE_PAUSA_INIZIO      | Eseguito all'inizio di una PAUSA |
| \_UTENTE_PAUSA_FINE        | Eseguito alla fine di una PAUSA  |
| \_UTENTE_RIPRENDERE_INIZIO | Eseguito all'inizio di un RESUME |
| \_UTENTE_RIPRENDERE_FINE   | Eseguito alla fine di un RESUME  |

-   Le macro interne sono macro per dividere la macro principale in processi e sono importanti per questo. È consigliabile che, se sono necessarie modifiche, queste vengano copiate così come sono.

**INIZIO_STAMPA**

| Nome della macro                             | Descrizione                                                                                                                                                                                                                               |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_INIZIO_STAMPA_CALORE_CAMERA                | Riscalda l'armadio nel caso in cui il parametro CAMERA_TEMP viene ricevuto dalla nostra macro START_STAMPA dalla plastificatrice                                                                                                          |
| \_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO     | Viene eseguito quando il letto raggiunge la temperatura, dopo_UTENTE_INIZIO_STAMPA_DOPO_RISCALDAMENTO_LETTO. Tipicamente utilizzato per l'elaborazione delle calibrazioni del letto (Z_INCLINARE_REGOLARE, QUAD_PORTALE_LIVELLAMENTO,...) |
| \_INIZIO_STAMPA_LETTO_MAGLIA                 | Gestisce la logica del meshing del letto.                                                                                                                                                                                                 |
| \_INIZIO_STAMPA_PARCO                        | Parcheggiare la testina di stampa mentre si riscalda l'ugello alla temperatura di stampa.                                                                                                                                                 |
| \_INIZIO_STAMPA_DOPO_RISCALDAMENTO_ESTRUSORE | Spurgare l'ugello e caricare il profilo SKEW se questo è definito nelle variabili                                                                                                                                                         |

## Stampanti ed elettronica

Poiché lavoriamo con diversi modelli di stampanti ed elettronica, aggiungeremo quelli che non sono direttamente supportati da RatOS, siano essi contributi nostri o della comunità.

-   stampanti, in questa directory avremo tutte le configurazioni della stampante
-   schede, qui troveremo quelle elettroniche

### Parametri e pin

Il nostro modulo per Klipper utilizza il sistema di configurazione modulare utilizzato in RatOS e sfrutta i vantaggi di Klipper nell'elaborazione sequenziale dei file di configurazione. Questo è il motivo per cui l'ordine delle inclusioni e delle impostazioni personalizzate che vogliamo applicare a questi moduli è essenziale.

{% suggerimento stile="informazioni" %}
Se utilizzate come modulo, le configurazioni 3Dwork NON POSSONO essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura per sicurezza.

Ecco perché è molto importante capire come funziona Klipper e come personalizzare i nostri moduli sulla tua macchina.
{% suggerimento finale %}

Come li abbiamo spiegati in "[personalizzazione delle macro](3dwork-klipper-bundle.md#personalizando-macros)"Utilizzeremo lo stesso processo per regolare i parametri o i pin in base alle nostre esigenze.

#### Parametri di personalizzazione

Così come ti consigliamo di creare una sezione nel tuo print.cfg chiamata USER OVERRIDES, posizionata dopo gli include delle nostre configurazioni, per poter regolare e personalizzare qualsiasi parametro utilizzato in esse.

Nell'esempio seguente vedremo come nel nostro caso ci interessa personalizzare i parametri del nostro livellamento letto (bed_mesh) regolando i punti della sonda_count) rispetto alla configurazione che abbiamo di default nelle configurazioni del nostro modulo Klipper:

{% titolo codice="printer.cfg" %}

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

{% suggerimento stile="avviso" %}
I tre punti (...) degli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}

Possiamo utilizzare lo stesso processo con qualsiasi parametro che desideriamo regolare.

#### Personalizzazione della configurazione dei pin

Procederemo esattamente come abbiamo fatto in precedenza, nella nostra area USER OVERRIDES aggiungeremo quelle sezioni di pin che vogliamo adattare a nostro piacimento.

Nell'esempio seguente andremo a personalizzare quale sarà il pin della nostra ventola elettronica (controller_fan) per assegnargli uno diverso da quello predefinito:

{% titolo codice="printer.cfg" %}

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

{% suggerimento stile="avviso" %}
I tre punti (...) degli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}

```

```
