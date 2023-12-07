* * *

## descrizione: Pacchetto di macro, impostazioni e altre utilità per Klipper

# Pacchetto Clipper 3Dwork

> [!AVVERTIMENTO]**GUIDA IN PROCESSO!!! Sebbene le macro siano completamente funzionali, sono in continuo sviluppo.****Usateli a vostro rischio e pericolo!!!**</mark>

Da**Le tue scuse**Abbiamo compilato e messo a punto una serie di macro, impostazioni della macchina e dell'elettronica, nonché altri strumenti per una gestione Klipper semplice e potente.

Gran parte di questo pacchetto è basato su[**Ratti**](https://os.ratrig.com/)migliorare le parti che riteniamo interessanti, così come altri contributi della community.

## Installazione

Per installare il nostro pacchetto per Klipper seguiremo i seguenti passaggi

### Scarica dal repository

Ci collegheremo al nostro host tramite SSH ed emetteremo i seguenti comandi:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> [!AVVERTIMENTO]Se la directory di configurazione di Klipper è personalizzata, ricorda di modificare il primo comando in modo appropriato per la tua installazione.

Nelle nuove installazioni:

Dato che Klipper non consente l'accesso alle macro finché non ha un file Printer.cfg corretto e non si connette a un MCU, possiamo "ingannare" Klipper con i seguenti passaggi che ci permetteranno di utilizzare le macro nel nostro pacchetto per, ad esempio, avviare il Macro compilazione firmware Klipper se utilizziamo elettroniche compatibili:

-   Ci assicuriamo di avere il nostro[host come secondo MCU](raspberry-como-segunda-mcu.md)
-   Successivamente aggiungeremo un Printer.cfg, ricorda che questi passaggi sono per un'installazione pulita in cui non hai alcun Printer.cfg e vuoi avviare la macro per creare firmware, come quello che puoi vedere qui sotto:

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

Con questo possiamo avviare Klipper per darci accesso alle nostre macro.
{% suggerimento finale %}

### Usa Moonraker per essere sempre aggiornato

Grazie a Moonraker possiamo utilizzare il suo aggiornamento_manager per poter rimanere aggiornato sui miglioramenti che potremmo introdurre in futuro.

Da Mainsail/Fluidd modificheremo il nostro moonraker.conf (dovrebbe essere alla stessa altezza del vostro Printer.cfg) e aggiungeremo alla fine del file di configurazione:

```django
[include 3dwork-klipper/moonraker.conf]
```

{% suggerimento stile="avviso" %}<mark style="color:orange;">**Ricordarsi di eseguire prima la fase di installazione, altrimenti Moonraker genererà un errore e non sarà in grado di avviarsi.**</mark>

**D'altra parte, se la directory della configurazione di Klipper è personalizzata, ricordati di adattare il percorso in modo appropriato alla tua installazione.**{% finale %}

## Macro

Abbiamo sempre commentato che RatOS è una delle migliori distribuzioni Klipper, con supporto per i moduli Raspberry e CB1, in gran parte grazie alle sue configurazioni modulari e alle sue fantastiche macro.

Alcune macro aggiunte che ci saranno utili:

### **Macro per scopi generali**

| Macro                                                                                  | Descrizione                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FORSE_CASA**                                                                         | Ci consente di ottimizzare il processo di homing solo eseguendolo su quegli assi che non sono in homing.                                                                                                                                                                                |
| **PAUSA**                                                                              | Utilizzando le relative variabili, ci permette di gestire una pausa con un parcheggio della testa più versatile rispetto alle normali macro.                                                                                                                                            |
| <p><strong>SET_PAUSE_AT_LAYER</strong><br><strong>SET_PAUSE_AT_NEXT_LAYER</strong></p> | <p>Una macro molto utile che Mainsail integra nella sua interfaccia utente per poter mettere in pausa su richiesta in un livello specifico... nel caso ce ne fossimo dimenticati durante la laminazione.<br>Ne abbiamo anche un altro per eseguire la pausa sul livello successivo.</p> |
| **RIPRENDERE**                                                                         | Migliorato poiché ci permette di rilevare se il nostro ugello non è alla temperatura di estrusione per risolverlo prima che mostri un errore e danneggi la nostra stampa.                                                                                                               |
| **ANNULLA_STAMPA**                                                                     | Ciò consente l'utilizzo del resto delle macro per eseguire correttamente un annullamento di stampa.                                                                                                                                                                                     |

-   **In pausa al cambio di livello**, alcune macro molto interessanti che ci permettono di mettere in pausa un livello o lanciare un comando all'avvio del livello successivo. \\![](<../../.gitbook/assets/image (6) (5) (1) (2).png>)![](<../../.gitbook/assets/image (1) (1) (8).png>)\\
    Inoltre, un altro vantaggio è che sono integrati con Mainsail, quindi avremo nuove funzioni nella nostra interfaccia utente, come puoi vedere di seguito:\\![](<../../.gitbook/assets/image (3) (15).png>)![](<../../.gitbook/assets/image (29) (1) (2).png>)

### **Macro di gestione della stampa**

<table><thead><tr><th width="170">Macro</th><th>Descripción</th></tr></thead><tbody><tr><td><strong>START_PRINT</strong></td><td>Nos permitirá poder iniciar nuestras impresiones de una forma segura y al estilo Klipper. Dentro de esta encontraremos algunas funciones interesantes como:<br>- precalentado de nozzle inteligente en el caso de contar con sensor probe<br>- posibilidad de uso de z-tilt mediante variable<br>- mallado de cama adaptativo, forzado o desde una malla guardada<br>- línea de purga personalizable entre normal, línea de purgado adaptativa o gota de purgado<br>- macro segmentada para poder personalizarse tal como os mostraremos más adelante</td></tr><tr><td><strong>END_PRINT</strong></td><td>Macro de fin de impresión donde también disponemos de segmentación para poder personalizar nuestra macro. También contamos con aparcado dinámico del cabezal.</td></tr></tbody></table>

-   **Rete da letto adattiva**Grazie alla versatilità di Klipper possiamo fare cose che oggi sembrano impossibili... un processo importante per la stampa è avere una rete di deviazioni dal nostro letto che ci permette di correggerle per avere una perfetta adesione dei primi strati. \\
    In molte occasioni eseguiamo questo meshing prima della stampa per assicurarci che funzioni correttamente e questo viene fatto su tutta la superficie del nostro letto.\\
    Con il meshing del letto adattivo, questo verrà fatto nell'area di stampa, rendendolo molto più preciso rispetto al metodo tradizionale... negli screenshot seguenti vedremo le differenze tra una mesh tradizionale e una adattiva.\\![](<../../.gitbook/assets/image (6) (12) (1).png>)![](<../../.gitbook/assets/image (2) (1) (4).png>)

### **Macro di gestione del filamento**

| Macro                   | Descrizione                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| **M600**                | Ci consentirà la compatibilità con il gcode M600 normalmente utilizzato nei laminatori per il cambio filamento. |
| **SCARICARE_FILAMENTO** | Configurabile attraverso le variabili, ci consentirà la scarica assistita del filamento.                        |
| **CARICO_FILAMENTO**    | Uguale al precedente ma relativo al carico del filamento.                                                       |

### **Macro di configurazione macchina**

| Macro                                                                                         | Descrizione                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **COMPILARE_FIRMWARE**                                                                        | <p>Con questa macro possiamo compilare il firmware di Klipper in modo semplice, avere il firmware accessibile dalla UI per una maggiore semplicità e poterlo applicare alla nostra elettronica.<br>Qui hai maggiori dettagli sull'elettronica supportata.</p> |
| **CALCOLARE_LETTO_MAGLIA**                                                                    | Una macro estremamente utile per calcolare l'area della nostra mesh perché a volte può essere un processo complicato.                                                                                                                                         |
| <p><strong>PID_ALL</strong><br><strong>PID_ESTRUSORE</strong><br><strong>PID_BED</strong></p> | Queste macro, dove potremo passare le temperature al PID sotto forma di parametri, ci permetteranno di eseguire la calibrazione della temperatura in modo estremamente semplice.                                                                              |
| <p><strong>TEST DI VELOCITÀ</strong><br><strong>TEST_SPEED_DELTA</strong></p>                 | La macro originale di Companion[Ellis](https://github.com/AndrewEllis93)Ci permetteranno in modo abbastanza semplice di testare la velocità con cui possiamo muovere la nostra macchina con precisione e senza perdita di passi.                              |

-   **Firmware compilato per l'elettronica supportata**, per facilitare il processo di creazione e manutenzione del firmware Klipper per i nostri MCU abbiamo la macro COMPILE_FIRMWARE che una volta eseguito, possiamo usare la nostra elettronica come parametro. Per fare solo questo, Klipper compilerà per tutta l'elettronica supportata dal nostro bundle:\\![](<../../.gitbook/assets/image (7) (5) (1).png>)\\
    Li troveremo facilmente accessibili dalla nostra interfaccia utente web nella directory del firmware_binari nella nostra scheda MACCHINA (se usiamo la randa):\\![](../../.gitbook/assets/telegram-cloud-photo-size-4-6019366631093943185-y.jpg)\\
    Di seguito è riportato l'elenco dei dispositivi elettronici supportati:

{% suggerimento stile="avviso" %}**IMPORTANTE!!!**

-   Questi script sono preparati per funzionare su un sistema Raspbian con utente pi, se non è il tuo caso dovrai adattarlo.
-   I firmware sono generati per l'utilizzo con una connessione USB, che è sempre quella che consigliamo. Inoltre, il punto di montaggio USB è sempre lo stesso, quindi la configurazione della connessione MCU non cambierà se vengono generati con la nostra macro/script.
-   **Affinché Klipper possa eseguire le macro della shell, è necessario installare un'estensione, grazie al compagno**[**arcoseno**](https://github.com/Arksine)**, che lo consente.**

        <mark style="color:green;">**Dependiendo de la distro de Klipper usada pueden venir ya habilitadas.**</mark>

        ![](<../../.gitbook/assets/image (1179).png>)

        La forma más sencilla es usando [**Kiauh**](../instalacion/#instalando-kiauh) donde encontraremos en una de sus opciones la posibilidad de instalar esta extensión:

        ![](../../.gitbook/assets/telegram-cloud-photo-size-4-5837048490604215201-x\_partial.jpg)

        También podemos realizar el proceso a mano copiaremos manualmente el plugin para Klipper[ **gcode\_shell\_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode\_shell\_command.py) dentro de nuestro directorio _**`~/klipper/klippy/extras`**_ usando SSH o SCP y reiniciamos Klipper.

    {% finale %}

{% schede %}
{% titolo scheda="Bigtreetech" %}
| Elettronica | Nome del parametro da utilizzare nella macro |
\| ------------------ \| ----------------------------------- \|
| Polpo Pro (446) | polpo_pro_446|
| Polpo Pro (429) | polpo_pro_429|
| Polpo v1.1 | polpo_11|
| Polpo v1.1 (407) | polpo_11_407|
| SKR Pro v1.2 | scr_pro_12|
| 3 corone svedesi | btt_scr_3|
| 2 corone svedesi (429) | scr_2_429|
| SKR Mini E3 v3 | btt_scr_mini_es_30              |

| Testa portautensili (CAN) | Nome del parametro da utilizzare nella macro |
| ------------------------- | -------------------------------------------- |
| EBB42v1                   | btt_riflusso42_10                            |
| EBB36v1                   | btt_riflusso36_10                            |
| EBB42 v1.1                | btt_riflusso42_11                            |
| EBB36 v1.1                | btt_riflusso36_11                            |
| EBB42 v1.2                | btt_riflusso42_12                            |
| EBB36 v1.2                | btt_riflusso36_12                            |

{% fine perdita %}

{% titolo scheda="MKS/ZNP" %}
| Elettronica | Nome del parametro da utilizzare nella macro |
\| -------------------- \| ----------------------------------- \|
| ZNP Robin Nano DW v2 | znp_pettirosso_nano_dw_v2 |
{% tabella finale %}

{% titolo della scheda="Morbido" %}
| Testa portautensile (CAN) | Nome del parametro da utilizzare nella macro |
\| ----------------- \| ----------------------------------- \|
| Dolce FLY SHT 42 | dolce_volare_merda_42|
| Dolce FLY SHT 36 | dolce_volare_merda_36|
{% fine perdita %}

{% titolo scheda="Fysetc" %}
| Elettronica | Nome del parametro da utilizzare nella macro |
\| ------------- \| ----------------------------------- \|
| Fysetc Spider | fyset ecc_ragno |
{% tabella finale %}
{% tabelle finali %}

### Aggiunta di macro 3Dwork alla nostra installazione

Dalla nostra interfaccia, Mainsail/Fluidd, modificheremo il nostro print.cfg e aggiungeremo:

{% titolo codice="printer.cfg" %}

    ## 3Dwork standard macros
    [include 3dwork-klipper/macros/macros_*.cfg]
    ## 3Dwork shell macros
    [include 3dwork-klipper/shell-macros.cfg]

{%endcode%}

{% suggerimento stile="informazioni" %}
È importante aggiungere queste righe alla fine del nostro file di configurazione... appena sopra la sezione in modo che se ci sono macro nel nostro cfg o include verranno sovrascritte dalle nostre:\\#\*# &lt;------------------------------- SALVA_CONFIGURAZIONE ----------------------->
{% suggerimento finale %}

{% suggerimento stile="avviso" %}
Le macro normali sono state separate da**shell delle macro**dato che**Per abilitarli è necessario eseguire manualmente ulteriori passaggi, oltre a quelli attualmente in fase di test.**E**Potrebbero richiedere autorizzazioni aggiuntive per assegnare autorizzazioni di esecuzione per le quali non sono state indicate le istruzioni poiché stanno tentando di automatizzare.**\\<mark style="color:red;">**Se li usi è a tuo rischio e pericolo.**</mark>{% finale %}

### Configurazione della nostra plastificatrice

Poiché le nostre macro sono dinamiche, estrarranno determinate informazioni dalla configurazione della nostra stampante e dal laminatore stesso. Per fare ciò, vi consigliamo di configurare le vostre plastificatrici come segue:

-   **avvia gcode INIZIA_STAMPA**, utilizzando i segnaposto per trasmettere dinamicamente i valori della temperatura del filamento e del letto:

{% schede %}
{% titolo scheda="PrusaSlicer-SuperSlicer" %}**Affettatrice Prusa**

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer**- abbiamo la possibilità di regolare la temperatura della custodia (CAMERA)

```gcode
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

![Ejemplo para PrusaSlicer/SuperSlicer](<../../.gitbook/assets/image (210).png>){% fine perdita %}

{% titolo scheda="Bambu Studio/OrcaSlicer" %}

```gcode
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

<figure><img src="../../.gitbook/assets/image (2) (1) (9) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% titolo scheda="Cura" %}

```gcode
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

{% suggerimento stile="avviso" %}
Dovremo installare il plugin[**Plug-in post-processo (di Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)dal menù_**Aiuto/Mostra**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script. \\
Reiniciamos Cura e iremos a_**Estensioni/Post elaborazione/Modifica G-Code**_e selezioneremo_**Dimensioni di stampa mesh**_,
{% finale %}
{% indtab %}

{% titolo scheda="IdeaMaker" %}

```gcode
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

{% fine perdita %}

{% titolo scheda="Semplifica3D" %}

```gcode
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

{% fine perdita %}
{% perdita %}

{% suggerimento stile="informazioni" %}
Los**i placeholder sono degli "alias" o variabili che i laminatori utilizzano in modo che durante la generazione del gcode li sostituiscano con i valori configurati nel profilo**di impressione.

Nei seguenti link è possibile trovarne un elenco per:[**Affettatrice Prusa**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(oltre a quelli sopra),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)E[**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).

L'uso di questi consente alle nostre macro di essere dinamiche.
{% suggerimento finale %}

-   **gcode la FINE finale_STAMPA**, in questo caso l'assenza di segnaposto è comune a tutte le plastificatrici

```gcode
END_PRINT
```

### Variabili

Come abbiamo già accennato, queste nuove macro ci permetteranno di avere alcune funzioni molto utili che abbiamo elencato sopra.

Per adattarli alla nostra macchina utilizzeremo le variabili che troveremo in macro/macro_era_globals.cfg e che dettagliamo di seguito.

#### Lingua del messaggio/notifica

Poiché a molti utenti piace avere notifiche macro nella loro lingua, abbiamo ideato un sistema di notifica multilingue, attualmente spagnolo (es) e inglese (en). Nella seguente variabile possiamo regolarlo:

<table><thead><tr><th width="189">Variable</th><th width="247">Descripción</th><th width="163">Valores posibles</th><th>Valor por defecto</th></tr></thead><tbody><tr><td>variable_language</td><td>Nos permite seleccionar el idioma de las notificaciones. En el caso de no estar bien definido se usará en (inglés)</td><td>es / en</td><td>es</td></tr></tbody></table>

#### Estrusione relativa

Ci permette di controllare quale modalità di estrusione utilizzeremo alla fine del nostro START.\_STAMPA Il valore dipenderà dalla configurazione del nostro laminatore.

{% suggerimento stile="successo" %}
È consigliabile configurare la plastificatrice per utilizzare l'estrusione relativa e impostare questa variabile su True.
{% suggerimento finale %}

| Variabile                    | Descrizione                                                                                | Valori possibili | Valore di default |
| ---------------------------- | ------------------------------------------------------------------------------------------ | ---------------- | ----------------- |
| variabile_parente_estrusione | Ci permette di indicare la modalità di estrusione utilizzata nella nostra plastificatrice. | Vero falso       | VERO              |

#### Velocità

Per gestire le velocità utilizzate nelle macro.

| Variabile                        | Descrizione                            | Valori possibili | Valore di default |   |
| -------------------------------- | -------------------------------------- | ---------------- | ----------------- | - |
| variabile_macro_viaggio_velocità | Velocità di trasferimento              | numerico         | 150               |   |
| variabile_macro_Con_velocità     | Velocità di trasferimento per l'asse Z | numerico         | 15                |   |

#### Homing

Insieme di variabili relative al processo di homing.

| Variabile | Descrizione | Valori possibili | Valore di default |
| --------- | ----------- | ---------------- | ----------------- |
|           |             |                  |                   |

#### Riscaldamento

Variabili legate al processo di riscaldamento della nostra macchina.

| Variabile                                        | Descrizione                                                                                                     | Valori possibili | Valore di default |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variabile_preriscaldare_estrusore                | Permette il preriscaldamento dell'ugello alla temperatura indicata nella variabile_preriscaldare_estrusore_temp | Vero falso       | VERO              |
| variabile_preriscaldare_estrusore_temp           | Temperatura di preriscaldamento dell'ugello                                                                     | numerico         | 150               |
| variabile_inizio_stampa_Calore_Camera_letto_temp | Temperatura del letto durante il processo di riscaldamento del nostro recinto                                   | numerico         | 100               |

{% suggerimento stile="successo" %}
Vantaggi dell'utilizzo dell'ugello preriscaldato:

-   Ci concede tempo aggiuntivo affinché il letto possa raggiungere la sua temperatura in modo uniforme.
-   Se utilizziamo un sensore induttivo che non dispone di compensazione della temperatura, le nostre misurazioni saranno più coerenti e precise.
-   Permette di ammorbidire eventuali residui di filamento nell'ugello, il che significa che, in alcune configurazioni, questi residui non influenzano l'attivazione del sensore.
    {% suggerimento finale %}

#### Rete da letto

Per controllare il processo di livellamento abbiamo variabili che possono essere molto utili. Ad esempio, possiamo controllare il tipo di livellamento che vogliamo utilizzare creando sempre una nuova mesh, caricandone una precedentemente memorizzata o utilizzando la mesh adattiva.

| Variabile                        | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                          | Valori possibili                                 | Valore di default |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | ----------------- |
| variabile_calibrare_letto_maglia | <p>Nos permite seleccionar que tipo de mallado usaremos en nuestro START_PRINT:<br>- nuova mesh, mesherà ogni stampa<br>- storedmesh, caricherà una mesh memorizzata e non eseguirà il sondaggio del letto<br>- adattivo, creerà una nuova mesh ma adattata all'area di stampa, spesso migliorando i nostri primi strati<br>- nomesh, nel caso in cui non disponiamo di un sensore o utilizziamo la mesh per saltare il processo</p> | <p>nevmesh / storedmesh / adattivo /<br>nomi</p> | adattivo          |
| variabile_letto_maglia_profilo   | Il nome utilizzato per la nostra mesh archiviata                                                                                                                                                                                                                                                                                                                                                                                     | testo                                            | predefinito       |

{% suggerimento stile="avviso" %}
Ti consigliamo di utilizzare il livellamento adattivo poiché adatterà sempre la mesh alla dimensione della nostra stampa, consentendoti di avere un'area della mesh regolata.

È importante che abbiamo nel nostro[avvia il gcode della nostra plastificatrice](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), nella chiamata al nostro START_STAMPA, STAMPA valori_MAX e STAMPA_Uomo.
{% finale %}

#### epurato

Una fase importante del nostro inizio stampa è un corretto spurgo del nostro ugello per evitare resti di filamento o che questi possano prima o poi danneggiare la nostra stampa. Di seguito sono riportate le variabili che intervengono in questo processo:

| Variabile                                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                          | Valori possibili                                                                  | Valore di default       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------- |
| variabile_ugello_adescamento                 | <p>Possiamo scegliere tra diverse opzioni di spurgo:<br>- primeline disegnerà la tipica linea di spurgo<br>- primelineadaptative genererà una linea di spurgo che si adatta all'area della parte stampata utilizzando variable_nozzle_priming_objectdistance come margine<br>- primeblob metterà una goccia di filamento in un angolo del nostro letto, molto efficace per pulire l'ugello e facile da rimuovere</p> | <p>linea principale /</p><p>primelineadaptive /<br>blob principale /<br>Falso</p> | linee primarie adattive |
| variabile_ugello_adescamento_oggettodistanza | Se utilizziamo la linea al vivo adattiva sarà il margine da utilizzare tra la linea al vivo e l'oggetto stampato                                                                                                                                                                                                                                                                                                     | numerico                                                                          | 5                       |
| variabile_ugello_primo_inizio_X              | <p>Dove vogliamo posizionare la nostra linea di spurgo:<br>- min lo farà a X=0 (più un piccolo margine di sicurezza)<br>- max lo farà a X=max (meno un piccolo margine di sicurezza)<br>- il numero sarà la coordinata X dove localizzare lo spurgo</p>                                                                                                                                                              | <p>minimo/<br>massimo /<br>numero</p>                                             | massimo                 |
| variabile_ugello_primo_inizio_E              | <p>Dove vogliamo posizionare la nostra linea di spurgo:<br>- min lo farà a Y=0 (più un piccolo margine di sicurezza)<br>- max lo farà a Y=max (meno un piccolo margine di sicurezza)<br>- il numero sarà la coordinata Y dove localizzare lo spurgo</p>                                                                                                                                                              | <p>minimo/<br>massimo /<br>numero</p>                                             | min                     |
| variabile_ugello_primo_direzione             | <p>L'indirizzo della nostra linea o drop:<br>- all'indietro la testa si sposterà davanti alla stampante<br>- Gli attaccanti si sposteranno dietro<br>- l'auto andrà verso il centro a seconda di variable_nozzle_prime_start_y</p>                                                                                                                                                                                   | <p>auto /<br>avanti /<br>indietro</p>                                             | auto                    |

#### Carico/scarico filamento

In questo caso, questo gruppo di variabili faciliterà la gestione del caricamento e dello scaricamento del nostro filamento utilizzato in emulazione dell'M600, ad esempio, o quando si lanciano le macro di caricamento e scaricamento del filamento:

| Variabile                               | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                | Valori possibili | Valore di default |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variabile_filamento_scaricare_lunghezza | Quanto ritirare il filamento in mm, adattalo alla tua macchina, normalmente la misura dal tuo ugello agli ingranaggi del tuo estrusore aggiungendo un margine extra.                                                                                                                                                                                                                                                       | numero           | 130               |
| variabile_filamento_scaricare_velocità  | Velocità di ritrazione del filamento in mm/sec normalmente viene utilizzata una velocità lenta.                                                                                                                                                                                                                                                                                                                            | numero           | 5                 |
| variabile_filamento_carico_lunghezza    | Distanza in mm per caricare il nuovo filamento... oltre che in variabile_filamento_scaricare_lunghezza utilizzeremo la misura dal tuo ingranaggio all'estrusore aggiungendo un margine extra, in questo caso questo valore extra dipenderà da quanto vuoi che venga spurgato... normalmente puoi dargli più margine rispetto al valore precedente per assicurarti che il l'estrusione del filamento precedente sia pulita. | numero           | 150               |
| variabile_filamento_carico_velocità     | Velocità di caricamento del filamento in mm/sec, normalmente viene utilizzata una velocità maggiore rispetto alla velocità di scarico.                                                                                                                                                                                                                                                                                     | numero           | 10                |

{% suggerimento stile="avviso" %}
Un'altra impostazione necessaria per la tua sezione\[estrusore] indica il[<mark style="color:green;">**massimo_estrudere_soltanto_distanza**</mark>](https://www.klipper3d.org/Config_Reference.html#extruder)...il valore consigliabile è solitamente >101 (se non definito, utilizzare 50) per consentire, ad esempio, tipici test di calibrazione dell'estrusore. \\
Dovresti modificare il valore in base a quanto menzionato in precedenza sul test o sulla configurazione del tuo**variabile_filamento_scaricare_lunghezza**IO**variabile_filamento_carico_lunghezza**,
{% finale %}

#### Parcheggio

In alcuni processi della nostra stampante, come la pausa, è consigliabile parcheggiare la testa. Le macro nel nostro bundle hanno questa opzione oltre alle seguenti variabili da gestire:

| Variabile                                 | Descrizione                                                                                                                                                                                                                                                                                                           | Valori possibili                         | Valore di default |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------- |
| variabile_inizio_stampa_parco_In          | Posizione dove parcheggiare la testa durante il preriscaldamento.                                                                                                                                                                                                                                                     | <p>Indietro /<br>centro /<br>davanti</p> | Indietro          |
| variabile_inizio_stampa_parco_Con_altezza | Altezza Z durante il preriscaldamento                                                                                                                                                                                                                                                                                 | numero                                   | 50                |
| variabile_FINE_stampa_parco_In            | Posizione dove parcheggiare la testa quando si termina o si annulla una stampa.                                                                                                                                                                                                                                       | <p>Indietro /<br>centro /<br>davanti</p> | Indietro          |
| variabile_FINE_stampa_parco_Con_salto     | Distanza da salire in Z alla fine della stampa.                                                                                                                                                                                                                                                                       | numero                                   | 20                |
| variabile_pausa_stampa_parco_In           | Posizione dove parcheggiare la testa quando si mette in pausa la stampa.                                                                                                                                                                                                                                              | <p>Indietro /<br>centro /<br>davanti</p> | Indietro          |
| variabile_pausa_oziare_tempo scaduto      | Valore, in secondi, dell'attivazione del processo di inattività della macchina che sblocca i motori e provoca la perdita delle coordinate,**È consigliabile un valore alto in modo che quando si attiva la macro PAUSE ci voglia il tempo sufficiente per eseguire qualsiasi azione prima di perdere le coordinate.** | numero                                   | 43200             |

#### Inclinazione Z

Sfruttare al massimo la nostra macchina affinché si autolivella e garantire che la nostra macchina sia sempre nelle migliori condizioni è fondamentale.

**Z-TILT è fondamentalmente un processo che ci aiuta ad allineare i nostri motori Z rispetto al nostro asse/gantry X (cartesiano) o XY (CoreXY).**. Con questo**ci assicuriamo di avere sempre la nostra Z allineata perfettamente, in modo preciso e automatico**.

| Variabile                         | Descrizione                                                                                   | Valori possibili | Valore di default |
| --------------------------------- | --------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variabile_calibrare_Con_inclinare | Permette, se abilitato nella nostra configurazione Klipper, il processo di regolazione Z-Tilt | Vero falso       | Falso             |

#### Storto

L'impiego di[STORTO](../../guias-impresion-3d/calibracion_3d.md#7.-pasos-ejes)Per la correzione o la regolazione precisa delle nostre stampanti è estremamente consigliabile se riscontriamo deviazioni nelle nostre stampe. Utilizzando la seguente variabile possiamo consentirne l'utilizzo nelle nostre macro:

| Variabile                | Descrizione                                                                                                                                                                                                                                        | Valori possibili | Valore di default  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ |
| variabile_storto_profilo | Ci consente di prendere in considerazione il nostro profilo di inclinazione che verrà caricato nella nostra macro START_STAMPA Per attivarlo dobbiamo decommentare la variabile e utilizzare il nome del profilo skew dalla nostra configurazione. | testo            | Mio_storto_profilo |

### Personalizzazione macro

Il nostro modulo per Klipper utilizza il sistema di configurazione modulare utilizzato in RatOS e sfrutta i vantaggi di Klipper nell'elaborazione sequenziale dei file di configurazione. Questo è il motivo per cui l'ordine delle inclusioni e delle impostazioni personalizzate che vogliamo applicare a questi moduli è essenziale.

{% suggerimento stile="informazioni" %}
Se utilizzate come modulo, le configurazioni 3Dwork NON POSSONO essere modificate direttamente dalla directory 3dwork-klipper all'interno della directory di configurazione di Klipper poiché sarà di sola lettura per sicurezza.

Ecco perché è molto importante capire come funziona Klipper e come personalizzare i nostri moduli sulla tua macchina.
{% suggerimento finale %}

#### **Personalizzazione delle variabili**

Normalmente, sarà ciò che dovremo aggiustare, per apportare modifiche alle variabili che abbiamo di default nel nostro modulo**Le tue scuse**per Scogliere.

Semplicemente, quello che dobbiamo fare è incollare il contenuto della macro\[gcode_macro GLOBALE_VARS] che possiamo trovare in macro/macros_era_globals.cfg nel nostro Printer.cfg.

Ti ricordiamo quanto accennato in precedenza su come Klipper elabora le configurazioni in sequenza, quindi è consigliabile incollarlo dopo gli include di cui abbiamo parlato.[Qui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Avremo qualcosa del genere (è solo un esempio visivo):

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

{% suggerimento stile="avviso" %}
I tre punti (...) negli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}

{% suggerimento stile="informazioni" %}

-   Ti consigliamo di aggiungere commenti come vedi nel caso precedente per identificare cosa fa ciascuna sezione.
-   Sebbene non sia necessario modificare tutte le variabili, ti consigliamo di copiare tutto il contenuto di\[gcode_macro GLOBALE_Anno]
    {% finale %}

#### Personalizzazione delle macro

Le macro sono state impostate in modo modulare in modo che possano essere facilmente modificate. Come abbiamo accennato prima, se vogliamo modificarle dovremo procedere come abbiamo fatto con le variabili, copiare la macro in questione nel nostro print.cfg (o in un altro nostro include) e assicurarci che sia dopo l'inclusione in cui abbiamo aggiunto il nostro modulo 3Dwork per Klipper.

Abbiamo due gruppi di macro:

-   Macro per aggiungere impostazioni utente, queste macro possono essere facilmente aggiunte e personalizzate perché sono state aggiunte in modo che qualsiasi utente possa personalizzare le azioni a proprio piacimento in alcune parti dei processi eseguiti da ciascuna macro.

**INIZIO_STAMPA**

<table><thead><tr><th width="400">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_USER_START_PRINT_HEAT_CHAMBER</td><td>Se ejecuta justo después que nuestro cerramiento empiece a calentar, si CHAMBER_TEMP se pasa como parámetro a nuestro START_PRINT</td></tr><tr><td>_USER_START_PRINT_BEFORE_HOMING</td><td>Se ejecuta antes del homing inicial de inicio de impresión</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar nuestra cama a su temperatura, antes de _START_PRINT_AFTER_HEATING_BED</td></tr><tr><td>_USER_START_PRINT_BED_MESH</td><td>Se lanza antes de _START_PRINT_BED_MESH</td></tr><tr><td>_USER_START_PRINT_PARK</td><td>Se lanza antes de _START_PRINT_PARK</td></tr><tr><td>_USER_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Se lanza antes de _START_PRINT_AFTER_HEATING_EXTRUDER</td></tr></tbody></table>

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

<table><thead><tr><th width="405">Nombre Macro</th><th>Descripción</th></tr></thead><tbody><tr><td>_START_PRINT_HEAT_CHAMBER</td><td>Calienta el cerramiento en el caso de que el parámetro CHAMBER_TEMP sea recibido por nuestra macro START_PRINT desde el laminador</td></tr><tr><td>_START_PRINT_AFTER_HEATING_BED</td><td>Se ejecuta al llegar la cama a la temperatura, después de _USER_START_PRINT_AFTER_HEATING_BED. Normalmente, se usa para el procesado de calibraciones de cama (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...)</td></tr><tr><td>_START_PRINT_BED_MESH</td><td>Se encarga de la lógica de mallado de cama.</td></tr><tr><td>_START_PRINT_PARK</td><td>Aparca el cabezal de impresión mientras calienta el nozzle a la temperatura de impresión.</td></tr><tr><td>_START_PRINT_AFTER_HEATING_EXTRUDER</td><td>Realiza el purgado del nozzle y carga el perfil SKEW en caso de que así definamos en las variables</td></tr></tbody></table>

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

Come abbiamo spiegato in "[personalizzazione delle macro](3dwork-klipper-bundle.md#personalizando-macros)"Utilizzeremo lo stesso processo per regolare i parametri o i pin in base alle nostre esigenze.

#### Parametri di personalizzazione

Così come ti consigliamo di creare una sezione nel tuo print.cfg chiamata USER OVERRIDES, posizionata dopo gli include delle nostre configurazioni, per poter regolare e personalizzare qualsiasi parametro utilizzato in esse.

Nell'esempio seguente vedremo come nel nostro caso ci interessa personalizzare i parametri del nostro livellamento letto (bed_mesh) regolando i punti della sonda_count) rispetto alla configurazione che abbiamo di default nelle configurazioni del nostro modulo Klipper:

{% titolo codice="printer.cfg" %}

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

{% suggerimento stile="avviso" %}
I tre punti (...) negli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}

Possiamo utilizzare lo stesso processo con qualsiasi parametro che desideriamo regolare.

#### Personalizzazione della configurazione dei pin

Procederemo esattamente come abbiamo fatto in precedenza, nella nostra area USER OVERRIDES aggiungeremo quelle sezioni di pin che vogliamo adattare a nostro piacimento.

Nell'esempio seguente andremo a personalizzare quale sarà il pin della nostra ventola elettronica (controller_fan) per assegnargli uno diverso da quello predefinito:

{% titolo codice="printer.cfg" %}

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

{% suggerimento stile="avviso" %}
I tre punti (...) negli esempi precedenti stanno solo ad indicare che si possono avere più configurazioni tra le sezioni... in nessun caso vanno aggiunti.
{% suggerimento finale %}
