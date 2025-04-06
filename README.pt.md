
# 3Dwork Klipper Bundle ![Português](https://flagcdn.com/w40/pt.png)

## Pacote de macros, definições e outros utilitários para o Klipper

[![Español](https://flagcdn.com/w40/es.png)](README.md) [![English](https://flagcdn.com/w40/gb.png)](README.en.md) [![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md) [![Italiano](https://flagcdn.com/w40/it.png)](README.it.md) [![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ AVISO** 
> **GUIA EM DESENVOLVIMENTO!!!** **<span style="color: red">Embora as macros sejam totalmente funcionais, estão em desenvolvimento contínuo.</span>** > **<span style="color: orange">Use por sua própria conta e risco!!!</span>**

Changelog

07/12/2023 - Adicionado suporte para automatizar a criação de firmware para eletrônicas Bigtreetech

Da **3Dwork** compilamos e ajustamos um conjunto de macros, configurações de máquinas e eletrônicas, bem como outras ferramentas para uma gestão simples e poderosa do Klipper.

Grande parte deste pacote é baseado no [**RatOS**](https://os.ratrig.com/) melhorando as partes que consideramos interessantes, bem como outras contribuições da comunidade.

## Instalação

Para instalar nosso pacote para Klipper, seguiremos os seguintes passos

### Download do repositório

Vamos nos conectar ao nosso host via SSH e executar os seguintes comandos:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTA** 
> Se o diretório da sua configuração do Klipper estiver personalizado, lembre-se de ajustar o primeiro comando adequadamente à sua instalação.

> **ℹ️ INFORMAÇÃO PARA NOVAS INSTALAÇÕES** 
> Como o Klipper não permite acesso às macros sem um printer.cfg válido e conexão a uma MCU, podemos usar esta configuração temporária:
>
> 1. Certifique-se de ter o [host como segunda MCU](raspberry-como-segunda-mcu.md)
> 2. Adicione este printer.cfg básico para habilitar as macros:

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

Isso permitirá iniciar o Klipper e acessar as macros.

### Usando o Moonraker para manter-se sempre atualizado

Graças ao Moonraker, podemos usar seu update_manager para nos mantermos atualizados com as melhorias que possamos introduzir no futuro.

A partir do Mainsail/Fluidd, editaremos nosso moonraker.conf (deve estar no mesmo nível que seu printer.cfg) e adicionaremos ao final do arquivo de configuração:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **⚠️ AVISO** 
> **Lembre-se de fazer o passo de instalação previamente, caso contrário o Moonraker gerará um erro e não poderá iniciar.**
>
> **Por outro lado, caso o diretório da sua configuração do Klipper esteja personalizado, lembre-se de ajustar o caminho adequadamente à sua instalação.**

## Macros

Sempre comentamos que o RatOS é uma das melhores distribuições do Klipper, com suporte para Raspberry e módulos CB1, em grande parte por suas configurações modulares e suas excelentes macros.

Algumas macros adicionadas que serão úteis:

### **Macros de uso geral**

| Macro | Descrição |
| --- | --- |
| **MAYBE_HOME** | Permite-nos otimizar o processo de homing realizando-o apenas nos eixos que não estão com homing. |
| **PAUSE** | Através das variáveis relacionadas, permite-nos gerenciar uma pausa com um estacionamento do cabeçote mais versátil que as macros normais. |
| **SET_PAUSE_AT_LAYER** | |
| **SET_PAUSE_AT_NEXT_LAYER** | Uma macro muito útil que integra o Mainsail em sua UI para poder realizar uma pausa sob demanda em uma camada específica... caso tenhamos esquecido ao fazer o fatiamento. |
| | Também contamos com outra para executar a pausa na próxima camada. |
| **RESUME** | Melhorada pois permite detectar se nosso bico não está na temperatura de extrusão para poder resolver antes que mostre um erro e danifique nossa impressão. |
| **CANCEL_PRINT** | Que permite o uso das demais macros para realizar um cancelamento de impressão corretamente. |

- **Pausa na mudança de camada**, macros muito interessantes que nos permitem fazer uma pausa programada em uma camada ou lançar um comando ao iniciar a próxima camada.
 ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)

 - Além disso, outra vantagem delas é que estão integradas com o Mainsail, o que nos dará novas funções em nossa UI como você pode ver a seguir:
 ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macros de gestão de impressão**

| Macro | Descrição |
| --- | --- |
| **START_PRINT** | Nos permitirá iniciar nossas impressões de forma segura e ao estilo Klipper. Dentro desta encontraremos algumas funções interessantes como: |
| | • Pré-aquecimento inteligente do bico quando usando um sensor de sonda |
| | • Possibilidade de uso de z-tilt através de variável |
| | • Malha de mesa adaptativa, forçada ou a partir de uma malha salva |
| | • Linha de purga personalizável entre normal, linha de purga adaptativa ou gota de purga |
| | • Macro segmentada para poder ser personalizada como mostraremos mais adiante |
| **END_PRINT** | Macro de fim de impressão onde também dispomos de segmentação para poder personalizar nossa macro. Também contamos com estacionamento dinâmico do cabeçote. |

- **Malha de mesa adaptativa**, graças à versatilidade do Klipper podemos fazer coisas que hoje parecem impossíveis... um processo importante para a impressão é ter uma malha de desvios da nossa mesa que nos permita corrigi-los para ter uma aderência perfeita das primeiras camadas. 
 Em muitas ocasiões fazemos esta malha antes das impressões para garantir que funcione corretamente e isto é feito em toda a superfície da nossa mesa. 
 Com a malha de mesa adaptativa, esta será realizada na zona de impressão fazendo com que seja muito mais precisa que o método tradicional... nas seguintes capturas veremos as diferenças de uma malha tradicional e uma adaptativa.
<div style="display: flex; justify-content: space-between;">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
 <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
</div>

### **Macros de gestão de filamento**

Conjunto de macros que nos permitirão gerenciar diferentes ações com nosso filamento, como a carga ou descarga deste.

| Macro | Descrição |
| --- | --- |
| **M600** | Nos permitirá compatibilidade com o gcode M600 normalmente usado nos laminadores para a troca de filamento. |
| **UNLOAD_FILAMENT** | Configurável através das variáveis, nos permitirá uma descarga de filamentos assistida. |
| **LOAD_FILAMENT** | Igual à anterior, mas relacionada com a carga do filamento. |

### **Macros de gestão de bobinas de filamentos (Spoolman)**

> **⚠️ AVISO** 
> **SEÇÃO EM PROCESSO!!!**

[**Spoolman**](https://github.com/Donkie/Spoolman) é um gestor de bobinas de filamento que se integra ao Moonraker e que nos permite gerenciar nosso estoque e disponibilidade de filamentos.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Não vamos entrar na instalação e configuração deste, já que é relativamente simples usando as [**instruções do seu Github**](https://github.com/Donkie/Spoolman)**,** em qualquer caso **aconselhamos usar Docker** por simplicidade e lembre-se de **ativar a configuração no Moonraker** necessária:

**moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro | Descrição |
| --- | --- |
| SET_ACTIVE_SPOOL | Nos permite indicar qual é o ID da bobina a usar |
| CLEAR_ACTIVE_SPOOL | Nos permite resetar a bobina ativa |

O ideal em cada caso seria adicionar em nosso fatiador, **nos gcodes de filamentos para cada bobina a chamada a esta**, e lembre-se de **mudar o ID desta uma vez consumida** para poder levar um controle do que resta de filamento na mesma!!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Macros de gestão da superfície de impressão**

> **⚠️ ADVERTÊNCIA** 
> **SECÇÃO EM CURSO!!!**

É normal que tenhamos diferentes superfícies de impressão dependendo do acabamento que queremos ter ou do tipo de filamento.

Este conjunto de macros, criado por [Garethky](https://github.com/garethky), permitir-nos-á ter o controlo destas e especialmente o ajuste correto do ZOffset em cada uma delas ao estilo do que temos nas máquinas Prusa. Aqui podem ver algumas das suas funções:

- poderemos armazenar o número de superfícies de impressão que quisermos, tendo cada uma um nome único.
- cada superfície de impressão vai ter o seu próprio ZOffset
- se fizermos ajustes Z durante uma impressão (Babystepping) a partir do nosso Klipper, esta alteração será armazenada na superfície activada nesse momento.

Por outro lado, temos alguns **requisitos para implementá-lo (tentaremos adicionar na lógica do PRINT_START do pacote no futuro activando por variável esta função e criando uma macro de utilizador antes e depois para poder colocar eventos de utilizador)**:

- é necessário o uso de save_variables, no nosso caso usaremos ~/variables.cfg para armazenar as variáveis, que já está dentro do cfg destas macros.
 Isto irá criar automaticamente um ficheiro variables_build_sheets.cfg onde irá guardar as nossas variáveis no disco.

**Archivo de configuración de variables de ejemplo**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

- deberemos incluir uma chamada a APPLY_BUILD_SHEET_ADJUSTMENT no nosso PRINT_START para poder aplicar o ZOffset da superfície selecionada.
- es importante que, para que a macro anterior, APPLY_BUILD_SHEET_ADJUSTMENT, funcione corretamente, devemos adicionar um SET_GCODE_OFFSET Z=0.0 logo antes de chamar APPLY_BUILD_SHEET_ADJUSTMENT.

```
# Load build sheet
SHOW_BUILD_SHEET ; show loaded build sheet on console
SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset
```

Por otro lado es interessante poder dispor de macros para ativar uma superfície ou outra, ou até mesmo passar como parâmetro a partir do nosso laminador para, com diferentes perfis de impressora ou de filamento, poder carregar uma ou outra automaticamente:

> **⚠️ ADVERTÊNCIA** 
> É importante que o valor em NAME="xxxx" coincida com o nome que demos ao instalar nossa superfície de impressão

\*\*printer.cfg

```ini
## Cada placa de impressão que você deseja usar precisa de uma macro de instalação
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

Também no caso de ter KlipperScreen, podemos adicionar um menu específico para gerenciar o carregamento das diferentes superfícies, onde incluiremos uma chamada às macros anteriormente criadas para o carregamento de cada superfície:

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

| Macro | Descrição |
| --- | --- |
| INSTALL_BUILD_SHEET | |
| SHOW_BUILD_SHEET | |
| SHOW_BUILD_SHEETS | |
| SET_BUILD_SHEET_OFFSET | |
| RESET_BUILD_SHEET_OFFSET | |
| SET_GCODE_OFFSET | |
| APPLY_BUILD_SHEET_ADJUSTMENT | |

### **Macros de configuração da máquina**
| Macro | Descrição |
| --- | --- |
| **COMPILE_FIRMWARE** | Com esta macro podemos compilar o firmware Klipper de forma simples, ter o firmware acessível a partir da UI para maior simplicidade e poder aplicá-lo à nossa eletrônica. |
| Aqui você tem mais detalhes das eletrônicas suportadas. | |
| **CALCULATE_BED_MESH** | Uma macro extremamente útil para calcular a área para nossa malha porque às vezes pode ser um processo complicado. |
| **PID_ALL** | |
| **PID_EXTRUDER** | |
| **PID_BED** | Estas macros, onde podemos passar as temperaturas para o PID em forma de parâmetros, nos permitirão realizar a calibração de temperatura de uma forma extremamente simples. |
| **TEST_SPEED** | |
| **TEST_SPEED_DELTA** | Macro original do colega [Ellis](https://github.com/AndrewEllis93) nos permitirá de uma forma bastante simples testar a velocidade na qual podemos mover nossa máquina de uma forma precisa e sem perda de passos. |

- **Compilação de firmware para eletrônicas suportadas**, para facilitar o processo de criação e manutenção do nosso firmware Klipper para nossas MCUs, contamos com a macro COMPILE_FIRMWARE que ao executá-la, podemos usar como parâmetro nossa eletrônica para fazer somente esta, compilará o Klipper para todas as eletrônicas suportadas pelo nosso bundle: nosso bundle:
 ![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)
 Estes são facilmente acessíveis a partir da nossa interface Web no diretório firmware_binaries no nosso separador MACHINE (se utilizar o Mainsail): 
 ![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)
 Segue-se a lista de produtos electrónicos suportados:

> ⚠️ **IMPORTANTE!!!**
>
>Estes scripts estão preparados para correr num sistema Raspbian com o utilizador pi, se este não for o seu caso terá de os adaptar.
>
>Os firmwares são gerados para serem utilizados com ligação USB, que é sempre o que recomendamos, também o ponto de montagem USB é sempre o mesmo, pelo que a configuração da ligação do seu MCU não será alterada se forem gerados com a nossa macro/script.
>
>Para permitir que o Klipper execute macros de shell, é necessário instalar uma extensão, graças ao nosso colega [**Arksine**](https://github.com/Arksine), para permitir a sua execução.
>
>**Dependendo da distro Klipper utilizada, estas podem já estar activadas**.
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> A maneira mais fácil é usar [**Kiauh**](../instalacion/#instalando-kiauh) onde encontrará numa das suas opções a possibilidade de instalar esta extensão:
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Também podemos fazer o processo manualmente, copiando o plugin Klipper <[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py) para nosso diretório `_**~/klipper/klippy/extras**_` usando SSH ou SCP e reiniciando o Klipper.

| Eletrônica | Nome do parâmetro a usar na macro |
| --- | --- |
| Manta E3 EZ | btt-manta-e3ez |
| Manta M4P | btt-manta-m4p |
| Manta M4P v2.2 | btt-manta-m4p-22 |
| Manta M8P | btt-manta-m8p |
| Manta M8P v1.1 | btt-manta-m8p-11 |
| Octopus Max EZ | btt-octopus-max-ez |
| Octopus Pro (446) | btt-octopus-pro-446 |
| Octopus Pro (429) | btt-octopus-pro-429 |
| Octopus Pro (H723) | btt-octopus-pro-h723 |
| Octopus v1.1 | btt-octopus-11 |
| Octopus v1.1 (407) | btt-octopus-11-407 |
| SKR Pro v1.2 | skr_pro_12 |
| SKR 3 | btt_skr_3 |
| SKR 3 (H723) | btt-skr-3-h723 |
| SKR 3 EZ | btt-skr-3-ez |
| SKR 3 EZ (H723) | btt-skr-3-ez-h723 |
| SKR 2 (429) | btt-skr-2-429 |
| SKR 2 (407) | btt-skr-2-407 |
| SKR RAT | btt-skrat-10 |
| SKR 1.4 Turbo | btt-skr-14-turbo |
| SKR Mini E3 v3 | btt_skr_mini_e3_30 |

| Cabeçote (CAN) | Nome do parâmetro a usar na macro |
| --- | --- |
| EBB42 v1 | btt_ebb42_10 |
| EBB36 v1 | btt_ebb36_10 |
| EBB42 v1.1 | btt_ebb42_11 |
| EBB36 v1.1 | btt_ebb36_11 |
| EBB42 v1.2 | btt_ebb42_12 |
| EBB36 v1.2 | btt_ebb36_12 |

| **Eletrônica** | **Nome do parâmetro a usar na macro** |
| --- | --- |
| MKS Eagle v1.x | mks-eagle-10 |
| MKS Robin Nano v3 | mks-robin-nano-30 |
| MKS Robin Nano v2 | mks-robin-nano-20 |
| MKS Gen L | mks-gen-l |
| ZNP Robin Nano DW v2 | znp_robin_nano_dw_v2 |

| Cabeçote (CAN) | Nome do parâmetro a usar na macro |
| --- | --- |
| Mellow FLY SHT 42 | mellow_fly_sht_42 |
| Mellow FLY SHT 36 | mellow_fly_sht_36 |

| Eletrônica | Nome do parâmetro a usar na macro |
| --- | --- |
| Fysetc Spider | fysetc_spider |

| Eletrônica | Nome do parâmetro a usar na macro |
| --- | --- |
| Artillery Ruby v1.x | artillery-ruby-12 |

| Eletrônica | Nome do parâmetro a usar na macro |
| --- | --- |
| Raspberry Pico/RP2040 | rpi-rp2040 |

| Eletrônica | Nome do parâmetro a usar na macro |
| --- | --- |
| Leviathan v1.2 | leviathan-12 |

### Adicionando as macros 3Dwork à nossa instalação

Da nossa interface, Mainsail/Fluidd, editaremos nosso printer.cfg e adicionaremos:

**printer.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️ **INFO!!!**
> É importante que adicionemos estas linhas ao final do nosso arquivo de configuração... logo acima da seção para que no caso de existirem macros em nosso cfg ou includes estas sejam sobrescritas pelas nossas:
> #\*# \#_# <---------------------- SAVE_CONFIG ----------------------> #_#

> ⚠️ **IMPORTANTE!!!**
> As macros normais foram separadas das **macros shell** já que **para habilitar estas é necessário realizar passos adicionais de forma manual além de estarem atualmente em teste** e **podem requerer permissões extras para atribuir permissões de execução para as quais não foram indicadas as instruções já que está se tentando automatizar.**
> **Se você as utiliza é por sua própria conta e risco.**

### Configuração do nosso laminador

Como nossas macros são dinâmicas, elas vão extrair certas informações da nossa configuração de impressora e do próprio laminador. Para isso, aconselhamos configurar seus laminadores da seguinte forma:

- **gcode de início START_PRINT**, usando placeholders para passar os valores de temperatura do filamento e mesa de forma dinâmica:

**PrusaSlicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**SuperSlicer** - temos a possibilidade de regular a temperatura do compartimento (CHAMBER).

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

** Cura**

```ini
START_PRINT EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} PRINT_MIN=%MINX%,%MINY% PRINT_MAX=%MAXX%,%MAXY%
```

> ⚠️ **Aviso!!!**
> Deveremos instalar o plugin [**Post Process Plugin (by frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff) a partir do menu _**Help/Show**_ configuration Folder... copiaremos o script do link anterior dentro da pasta script.
> Reiniciamos o Cura e iremos para _**Extensions/Post processing/Modify G-Code**_ e selecionaremos _**Mesh Print Size**_.

**IdeaMaker**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplify3D**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️ **INFO!!!**
> Os **placeholders são "alias" ou variáveis que os fatiadores usam para substituir pelos valores configurados no perfil** de impressão ao gerar o gcode.
>
> Nos seguintes links você pode encontrar uma lista deles para: [**PrusaSlicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643), [**SuperSlicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list) (além dos anteriores), [**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list) e [**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> O uso destes permite que nossas macros sejam dinâmicas.

- **gcode final END_PRINT**, neste caso, como não usa placeholders, é comum a todos os fatiadores
```ini
END_PRINT
```

### Variáveis

Como já mencionamos, essas novas macros nos permitirão ter algumas funções muito úteis, como listamos anteriormente.

Para ajustá-las à nossa máquina, usaremos as variáveis que encontraremos em macros/macros_var_globals.cfg e que detalhamos a seguir.

#### Idioma das mensagens/notificações

Como muitos usuários gostam de ter as notificações das macros em seu idioma, desenvolvemos um sistema de notificações multilíngue, atualmente em espanhol (es) e inglês (en). Na seguinte variável poderemos ajustá-lo:

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_language | Nos permite selecionar o idioma das notificações. Caso não esteja bem definido, será usado en (inglês) | es / en | es |

#### Extrusão Relativa

Permite controlar qual modo de extrusão usaremos ao terminar nosso START_PRINT. O valor dependerá da configuração do nosso fatiador.

> 💡 **Dica**
> É aconselhável configurar seu fatiador para usar extrusão relativa e ajustar esta variável para True.

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_relative_extrusion | Nos permite indicar o modo de extrusão usado em nosso fatiador. | True / False | True |

#### Velocidades

Para gerenciar as velocidades utilizadas nas macros.

| Variável | Descrição | Valores possíveis | Valor padrão | |
| --- | --- | --- | --- | --- |
| variable_macro_travel_speed | Velocidade em movimentações | numérico | 150 | |
| variable_macro_z_speed | Velocidade em movimentos eixo Z| numérico | 15 | |

#### Homing

Conjunto de variáveis relacionadas com o processo de homing.

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |

#### Aquecimento

Variáveis relacionadas com o processo de aquecimento da nossa máquina.

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_preheat_extruder | Habilita o pré-aquecimento do bico à temperatura indicada em variable_preheat_extruder_temp | True / False | True |
| variable_preheat_extruder_temp | Temperatura de pré-aquecimento do bico | numérico | 150 |
| variable_start_print_heat_chamber_bed_temp | Temperatura da mesa durante o processo de aquecer nosso compartimento | numérico | 100 |

> 💡 **Dica**
> Benefícios de utilizar o pré-aquecimento do bico:

- nos permite um tempo adicional para que a mesa possa chegar à sua temperatura de forma uniforme
- se usamos um sensor indutivo que não tem compensação de temperatura, nos permitirá que nossas medidas sejam mais consistentes e precisas
- permite amolecer qualquer resto de filamento no bico, o que permite que, em determinadas configurações, estes restos não afetem a ativação do sensor

#### Malha da Mesa (Bed Mesh)

Para controlar o processo de nivelamento, contamos com variáveis que podem ser muito úteis. Por exemplo, poderemos controlar o tipo de nivelamento que queremos utilizar criando uma nova malha sempre, carregando uma armazenada anteriormente ou utilizar uma malha adaptativa.

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_calibrate_bed_mesh | Nos permite selecionar que tipo de malha usaremos em nosso START_PRINT: | | |
| - new mesh, nos fará uma malha em cada impressão | | |
| - storedmesh, carregará uma malha armazenada e não realizará a sondagem da mesa | | | |
| - adaptative, nos fará uma nova malha mas adaptada à zona de impressão melhorando em muitas ocasiões nossas primeiras camadas | | | |
| - nomesh, no caso que não tenhamos sensor ou utilizemos malha para pular o processo | newmesh / storedmesh / adaptative / | | |
| nomesh | adaptative | | |
| variable_bed_mesh_profile | O nome usado para nossa malha armazenada | texto | default |

> ⚠️ **Aviso!!!**
> Aconselhamos usar o nivelamento adaptative já que vai ajustar sempre a malha ao tamanho da nossa impressão permitindo ter uma área de malha ajustada.
>
> É importante que tenhamos em nosso gcode de início do nosso fatiador, na chamada ao nosso START_PRINT, os valores PRINT_MAX e PRINT_MIN. PRINT_MIN.
#### Purga

Uma fase importante do início da nossa impressão é uma purga adequada do nosso bico para evitar restos de filamento ou que estes possam danificar nossa impressão em algum momento. A seguir você tem as variáveis que intervêm neste processo:
| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_nozzle_priming | Podemos escolher entre diferentes opções de purga:<br>- primeline: desenha a típica linha de purga<br>- primelineadaptative: gera uma linha de purga adaptada à zona de impressão usando variable_nozzle_priming_objectdistance como margem<br>- primeblob: faz uma gota de filamento em um canto da mesa | primeline / primelineadaptative / primeblob / False | primelineadaptative |
| variable_nozzle_priming_objectdistance | Se usamos linha de purga adaptativa será a margem a utilizar entre a linha de purga e o objeto impresso | numérico | 5 |
| variable_nozzle_prime_start_x | Onde localizar nossa linha de purga em X:<br>- min: X=0 (mais margem de segurança)<br>- max: X=max (menos margem de segurança)<br>- número: coordenada X específica | min / max / número | max |
| variable_nozzle_prime_start_y | Onde localizar nossa linha de purga em Y:<br>- min: Y=0 (mais margem de segurança)<br>- max: Y=max (menos margem de segurança)<br>- número: coordenada Y específica | min / max / número | min |
| variable_nozzle_prime_direction | Direção da linha ou gota:<br>- backwards: para a frente<br>- forwards: para trás<br>- auto: para o centro segundo variable_nozzle_prime_start_y | auto / forwards / backwards | auto |

#### Carga/Descarga de filamento

Neste caso este grupo de variáveis vai nos facilitar a gestão de carga e descarga do nosso filamento usado em emulação do M600 por exemplo ou ao lançar as macros de carga e descarga de filamento:

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_filament_unload_length | Quanto retrair em mm o filamento, ajustar à sua máquina, normalmente a medida desde seu bico até as engrenagens do seu extrusor adicionando uma margem extra. | número | 130 |
| variable_filament_unload_speed | Velocidade de retração do filamento em mm/seg normalmente se usa uma velocidade lenta. | número | 5 |
| variable_filament_load_length | Distância em mm para carregar o novo filamento... assim como em variable_filament_unload_length usaremos a medida desde sua engrenagem até extrusor adicionando uma margem extra, neste caso este valor extra dependerá de quanto você quer que se purgue... normalmente pode dar mais margem que o valor anterior para assegurar que fique limpa a extrusão do filamento anterior. | número | 150 |
| variable_filament_load_speed | Velocidade de carga do filamento em mm/seg normalmente se usa uma velocidade mais rápida que a de descarga. | número | 10 |

> ⚠️ **Aviso!!!**
> Outro ajuste necessário para sua seção \[extruder\] é indicar o [**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... o valor aconselhável costuma ser >101 (caso não esteja definido usa 50) para por exemplo permitir os testes típicos de calibração do extrusor. 
> Você deve ajustar o valor com base no comentado anteriormente do teste ou a configuração do seu **variable_filament_unload_length** e/ou **variable_filament_load_length**.

#### Estacionamento

Em determinados processos da nossa impressora, como a pausa, é aconselhável fazer um estacionamento do nosso cabeçote. As macros do nosso bundle dispõem desta opção além das seguintes variáveis para gerenciar:

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_start_print_park_in | Localização onde estacionar o cabeçote durante o pré-aquecimento. | back / center / front | back |
| variable_start_print_park_z_height | Altura em Z durante o pré-aquecimento | número | 50 |
| variable_end_print_park_in | Localização onde estacionar o cabeçote ao finalizar ou cancelar uma impressão. | back / center / front | back |
| variable_end_print_park_z_hop | Distância a subir em Z ao finalizar a impressão. | número | 20 |
| variable_pause_print_park_in | Localização onde estacionar o cabeçote ao pausar a impressão. | back / center / front | back |
| variable_pause_idle_timeout | Valor, em segundos, da ativação do processo de inatividade na máquina que libera motores e faz perder coordenadas, **é aconselhável um valor alto para que ao ativar a macro PAUSE demore o suficiente para realizar qualquer ação antes de perder coordenadas.** | número | 43200 |

#### Z-Tilt

Aproveitar ao máximo nossa máquina para que ela se auto-nivele e garantir que nossa máquina esteja sempre nas melhores condições é fundamental.

**Z-TILT é basicamente um processo que nos ajuda a alinhar nossos motores Z em relação ao nosso eixo/gantry X (cartesiana) ou XY (CoreXY)**. Com isso **garantimos que nosso Z esteja sempre alinhado perfeitamente e de forma precisa e automática**.

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_calibrate_z_tilt | Permite, caso esteja habilitado em nossa configuração do Klipper, o processo de ajuste Z-Tilt | True / False | False |

#### Skew

O uso de [SKEW](broken-reference) para a correção ou ajuste preciso de nossas impressoras é extremamente aconselhável se tivermos desvios em nossas impressões. Usando a seguinte variável podemos permitir o uso em nossas macros:

| Variável | Descrição | Valores possíveis | Valor padrão |
| --- | --- | --- | --- |
| variable_skew_profile | Permite levar em conta nosso perfil de skew que será carregado em nossa macro START_PRINT. Para ativá-lo devemos descomentar a variável e usar o nome do perfil de skew de nossa configuração. | texto | my_skew_profile |

### Personalização das macros

Nosso módulo para Klipper emprega o sistema de configuração modular usado no RatOS e aproveita as vantagens do Klipper no processamento sequencial de arquivos de configuração. Por isso é fundamental a ordem dos includes e ajustes personalizados que queremos aplicar sobre estes módulos.

> ℹ️ **INFO!!!**
> Ao ser usado como um módulo, as configurações do 3Dwork NÃO podem ser editadas diretamente do diretório 3dwork-klipper dentro do seu diretório de configuração do Klipper, pois estará em read-only (restrito a somente leitura) por segurança.
>
> Por isso é muito importante entender o funcionamento do Klipper e como poder personalizar nossos módulos para sua máquina.

#### **Personalizando variáveis**

Normalmente, será o que teremos que ajustar, para realizar ajustes sobre as variáveis que temos por padrão em nosso módulo **3Dwork** para Klipper.

Simplesmente, o que temos que fazer é colar o conteúdo da macro [gcode_macro GLOBAL_VARS] que podemos encontrar em macros/macros_var_globals.cfg em nosso printer.cfg.

Lembramos o comentado anteriormente de como o Klipper processa as configurações de forma sequencial, por isso é aconselhável colá-lo depois dos includes que comentamos [aqui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Ficará algo assim (apenas um exemplo visual):

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

> ⚠️ **Aviso!!!**
> Os três pontos (...) dos exemplos anteriores são meramente para indicar que você pode ter mais configurações entre seções... em nenhum caso devem ser colocados.

> ℹ️ **INFO!!!**
>
> - aconselhamos adicionar comentários como você vê no caso anterior para identificar o que cada seção faz
> - mesmo que você não precise ajustar todas as variáveis, aconselhamos copiar todo o conteúdo de [gcode_macro GLOBAL_VARS]

#### Personalizando macros

As macros foram montadas de forma modular para que possam ser ajustadas de forma simples. Como mencionamos anteriormente, se quisermos ajustá-las devemos proceder igual ao que fizemos com as variáveis, copiar a macro em questão em nosso printer.cfg (ou outro include próprio) e garantir que está depois do include onde adicionamos nosso módulo 3Dwork para Klipper.

Temos dois grupos de macros:

- Macros para adicionar ajustes de usuário, estas macros podem ser adicionadas e personalizadas facilmente porque foram adicionadas para que qualquer usuário possa personalizar as ações ao seu gosto em determinadas partes dos processos que cada macro faz.
**START_PRINT**

| Nome da Macro | Descrição |
| --- | --- |
| _USER_START_PRINT_HEAT_CHAMBER | É executada logo após nosso compartimento começar a aquecer, se CHAMBER_TEMP for passado como parâmetro para nosso START_PRINT |
| _USER_START_PRINT_BEFORE_HOMING | É executada antes do homing inicial de início de impressão |
| _USER_START_PRINT_AFTER_HEATING_BED | É executada quando nossa mesa atinge sua temperatura, antes de _START_PRINT_AFTER_HEATING_BED |
| _USER_START_PRINT_BED_MESH | É lançada antes de _START_PRINT_BED_MESH |
| _USER_START_PRINT_PARK | É lançada antes de _START_PRINT_PARK |
| _USER_START_PRINT_AFTER_HEATING_EXTRUDER | É lançada antes de _START_PRINT_AFTER_HEATING_EXTRUDER |

**END_PRINT**

| Nome da Macro | Descrição |
| --- | --- |
| _USER_END_PRINT_BEFORE_HEATERS_OFF | É executada antes de realizar o desligamento dos aquecedores, antes de _END_PRINT_BEFORE_HEATERS_OFF |
| _USER_END_PRINT_AFTER_HEATERS_OFF | É executada após o desligamento dos aquecedores, antes de _END_PRINT_AFTER_HEATERS_OFF |
| _USER_END_PRINT_PARK | É executada antes do estacionamento do cabeçote, antes de _END_PRINT_PARK |

**PRINT_BASICS**

| Nome da Macro | Descrição |
| --- | --- |
| _USER_PAUSE_START | É executada no início de um PAUSE |
| _USER_PAUSE_END | É executada ao finalizar um PAUSE |
| _USER_RESUME_START | É executada no início de um RESUME |
| _USER_RESUME_END | É executada ao finalizar um RESUME |

- Macros internas, são macros para dividir a macro principal em processos e é importante para este. É aconselhável que em caso de necessidade de ajuste estas sejam copiadas exatamente como estão.

**START_PRINT**

| Nome da Macro | Descrição |
| --- | --- |
| _START_PRINT_HEAT_CHAMBER| Aquece o compartimento caso o parâmetro CHAMBER_TEMP seja recebido por nossa macro START_PRINT do fatiador |
| _START_PRINT_AFTER_HEATING_BED | É executada quando a mesa atinge a temperatura, após _USER_START_PRINT_AFTER_HEATING_BED. Normalmente, é usada para o processamento de calibrações da mesa (Z_TILT_ADJUST, QUAD_GANTRY_LEVELING,...) |
| _START_PRINT_BED_MESH | Responsável pela lógica de malha da mesa. |
| _START_PRINT_PARK | Estaciona o cabeçote de impressão enquanto aquece o bico à temperatura de impressão. |
| _START_PRINT_AFTER_HEATING_EXTRUDER | Realiza a purga do bico e carrega o perfil SKEW caso assim definamos nas variáveis |

## Impressoras e eletrônicas

À medida que trabalharmos com diferentes modelos de impressoras e eletrônicas, iremos adicionando aquelas que não estão diretamente suportadas pelo RatOS, sejam contribuições nossas ou da comunidade.

- printers, neste diretório teremos todas as configurações de impressoras
- boards, aqui encontraremos as de eletrônicas

### Parâmetros e pinos

Nosso módulo para Klipper emprega o sistema de configuração modular usado no RatOS e aproveita as vantagens do Klipper no processamento sequencial de arquivos de configuração. Por isso é fundamental a ordem dos includes e ajustes personalizados que queremos aplicar sobre estes módulos.

> ℹ️ **INFO!!!**
> Ao ser usado como um módulo, as configurações do 3Dwork NÃO podem ser editadas diretamente do diretório 3dwork-klipper dentro do seu diretório de configuração do Klipper, pois estará em read-only (restrito a somente leitura) por segurança.
>
> Por isso é muito importante entender o funcionamento do Klipper e como poder personalizar nossos módulos para sua máquina.

Como explicamos em "[personalizando macros](3dwork-klipper-bundle.md#personalizando-macros)" usaremos o mesmo processo para ajustar parâmetros ou pinos para ajustá-los às nossas necessidades.

#### Personalizando parâmetros

Como aconselhamos criar uma seção em seu printer.cfg chamada USER OVERRIDES, colocada depois dos includes para nossas configurações, para poder ajustar e personalizar qualquer parâmetro usado neles.

No exemplo a seguir veremos como em nosso caso estamos interessados em personalizar os parâmetros do nosso nivelamento de mesa (bed_mesh) ajustando os pontos de sondagem (probe_count) em relação à configuração que temos por padrão nas configurações do nosso módulo Klipper: Klipper:
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

> ⚠️ **Aviso!!!**
> Os três pontos (...) dos exemplos anteriores são meramente para indicar que você pode ter mais configurações entre seções... em nenhum caso devem ser colocados.

Podemos empregar este mesmo processo com qualquer parâmetro que queiramos ajustar.

#### Personalizando configuração de pinos

Procederemos exatamente como fizemos anteriormente, em nossa zona USER OVERRIDES adicionaremos aquelas seções de pinos que queremos ajustar ao nosso gosto.

No exemplo a seguir vamos personalizar qual é o pino do nosso ventilador de eletrônica (controller_fan) para atribuí-lo a um diferente do padrão:

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

> ⚠️ **Aviso!!!**
> Os três pontos (...) dos exemplos anteriores são meramente para indicar que você pode ter mais configurações entre seções... em nenhum caso devem ser colocados.
