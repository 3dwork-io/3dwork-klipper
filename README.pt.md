# Pacote de clape 3dwork ![Português](https://flagcdn.com/w40/pt.png)

## Pacote de macros, configurações e outros utilitários para Klipper

[![English](https://flagcdn.com/w40/gb.png)](README.en.md)[![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md)[![Italiano](https://flagcdn.com/w40/it.png)](README.it.md)[![Français](https://flagcdn.com/w40/fr.png)](README.fr.md)[![Español](https://flagcdn.com/w40/es.png)](README.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **Aviso Aviso****Guia em processo !!!****<span style="color: red">Embora as macros sejam totalmente funcionais, elas estão em desenvolvimento contínuo.</span>****<span style="color: orange">Use -os sob sua própria responsabilidade !!!</span>**

Changelog

12/07/2023 - Adicionado suporte para automatizar a criação de firmware para a Bigreteech Electronics

Desde**3dwork**Compilamos e ajustamos um conjunto de macros, máquina e configurações eletrônicas, além de outras ferramentas para um gerenciamento simples e poderoso do Klipper.

Grande parte deste pacote é baseada em[**RatOS**](https://os.ratrig.com/)Melhorando as partes que acreditamos interessantes, bem como outras contribuições da comunidade.

## Instalación

Para instalar nosso pacote para Klipper, seguiremos as seguintes etapas

### Descarga do repositório

Vamos nos conectar ao nosso host pelo SSH e lançar os seguintes comandos:

```bash
cd ~/printer_data/config
git clone https://github.com/3dwork-io/3dwork-klipper.git
```

> **⚠️ NOTA**Se o diretório da configuração do Klipper for personalizado, lembre -se de ajustar o primeiro comando corretamente à sua instalação.

> **ℹ️ Informações para novas instalações**Como Klipper não permite o acesso a macros sem uma impressora válida.
>
> 1.  Certifique -se de ter o[host como segunda MCU](raspberry-como-segunda-mcu.md)
> 2.  Adicione esta impressora básica.cfg para habilitar macros:

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

Isso permitirá que o Klipper inicie e acesse as macros.

### Usando Moonraker para sempre ser atualizado

Graças ao MoonRaker, podemos usar seu update_manager para poder estar atualizado com as melhorias que podemos introduzir no futuro.

De MainSail/Fluidd, editaremos nosso Moonraker.conf (deve estar na mesma altura que sua impressora.cfg) e adicionaremos no final do arquivo de configuração:

```ini
[include 3dwork-klipper/moonraker.conf]
```

> **Aviso Aviso****Lembre -se de dar a etapa de instalação anteriormente se você não gerar um erro e não poderá iniciar.**
>
> **Por outro lado, no caso de o diretório de configuração do Klipper ser personalizado, lembre -se de ajustar o caminho corretamente à sua instalação.**

## Macros

Sempre comentamos que o Times é uma das melhores distribuições de Klipper, com suporte de framboesa e módulos CB1, principalmente por causa de suas configurações modulares e de suas grandes macros.

Algumas macros adicionadas que serão úteis:

### **Macros de uso general**

| Macro                       | Descrição                                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Talvez_home**             | Ele nos permite otimizar o processo de retorno apenas fazendo isso nesses eixos que não estão com o Homing.                                                                     |
| **PAUSA**                   | Através de variáveis ​​relacionadas, ele nos permite gerenciar uma pausa com um estacionamento mais versátil da cabeça que as macros normais.                                   |
| **Set_pause_at_layer**      |                                                                                                                                                                                 |
| **Set_pause_at_next_layer** | Uma macro muito útil que integra a vela principal à sua interface do usuário para poder pausar sob demanda em uma camada específica ... Caso esquecemos ao executar o laminado. |
|                             | Também temos outro a executar o lazer na próxima camada.                                                                                                                        |
| **RETOMAR**                 | Melhorado, pois permite detectar se nosso bico não está na temperatura de extrusão para poder resolvê -lo antes de mostrar um erro e danificar nossa impressão.                 |
| **Cancel_print**            | Que permite que o uso do restante das macros realize um cancelamento de impressão corretamente.                                                                                 |

-   **Em vez disso, parou**, macros muito interessantes que nos permitem fazer um agendado de maneira tranquila em uma camada ou iniciar um comando ao iniciar a próxima camada. ![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FngLiLpXtNRNiePaNtbwP%2Fimage.png&width=300&dpr=2&quality=100&sign=dd421b95&sv=2)Além disso, outra vantagem deles é que eles são integrados à vela principal com o que teremos novas funções em nossa interface do usuário, como você pode ver abaixo:![Layer pause feature in Mainsail](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FfhhW30zu2cZp4u4pOSYt%2Fimage.png&width=300&dpr=2&quality=100&sign=9fb93e6f&sv=2)

### **Macros de gerenciamento de impressão**

| Macro           | Descrição                                                                                                                                            |   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| **Start_print** | Isso nos permitirá iniciar nossas impressões de maneira segura e no estilo Klipper. Dentro disso, encontraremos algumas funções interessantes, como: |   |
|                 | • Bicos inteligentes pré -aquecendo ao usar um sensor de sonda                                                                                       |   |
|                 | • Possibilidade de uso de Z-Tilt pela variável                                                                                                       |   |
|                 | • Adaptável, forçado ou de uma miséria de malha armazenada                                                                                           |   |
|                 | • Linha de purga personalizável entre linha de purga normal e adaptável ou queda de purga                                                            |   |
|                 | • Macro segmentado para ser capaz de personalizar como mostraremos mais tarde                                                                        |   |
| **End_print**   | Macro de extremidade da impressão, onde também temos segmentação para personalizar nossa macro. Também temos cabeça dinâmica da cabeça.              |   |

-   **Mallado de cama adaptativo**, graças à versatilidade de Klipper, podemos fazer coisas que hoje parecem impossíveis ... Um processo importante para a impressão é fazer uma refeição de desvios da nossa cama que nos permite corrigir isso para ter uma adesão das primeiras camadas perfeitas.  
     Em muitas ocasiões, fazemos esse Malley antes das impressões para garantir que ele funcione corretamente e isso seja feito em toda a superfície da nossa cama. 
     Com a miséria de cama adaptativa, ela será realizada na zona de impressão, tornando -a muito mais precisa do que o método tradicional ... nas seguintes capturas, veremos as diferenças de uma malha tradicional e adaptativa.
    <div style="display: flex; justify-content: space-between;">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FtzhCFrbnNrVj5L2bkdrr%2Fimage.png&width=300&dpr=2&quality=100&sign=ec43d93c&sv=2" width="40%">
     <img src="https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FwajqLHhuYm3u68A8Sy4x%2Fimage.png&width=300&dpr=2&quality=100&sign=e5613596&sv=2" width="60%">
    </div>

### **Macros de gerenciamento de filamentos**

Conjunto de macros que nos permitirão gerenciar diferentes ações com nosso filamento, como a carga ou a descarga disso.

| Macro               | Descrição                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **O M600**          | Isso nos permitirá a compatibilidade com o M600 Gcode normalmente usado em laminadores para a mudança de filamento. |
| **UNLOOLT_FILIRED** | Configurável através das variáveis ​​nos permitirá baixar filamentos assistidos.                                    |
| **Load_filament**   | Bem como o anterior, mas relacionado à carga do filamento.                                                          |

### **Macros de gerenciamento de bobinas de filamentos (Spoolman)**

> **Aviso Aviso****Seção em processo !!!**

[**Spoolman**](https://github.com/Donkie/Spoolman)Ele é um gerente de bobina de filamentos que é integrado ao Moonraker e que nos permite gerenciar nosso estoque e disponibilidade de filamentos.

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FhiSCtknzBswK3eEWyUKS%252Fimage.png%3Falt%3Dmedia%26token%3D7119c3c4-45da-4baf-a893-614184c68119&width=400&dpr=3&quality=100&sign=f69fd5f6&sv=2)

Não vamos entrar na instalação e configuração disso, pois é relativamente simples usando o[**Instruções do seu github**](https://github.com/Donkie/Spoolman)**,**Em todo o caso**os aconsejamos utilizar Docker**Por simplicidade e lembrança**Ative a configuração em Moonraker**requerida:

**Moonraker.conf**

```ini
[spoolman]
server: http://192.168.0.123:7912
# URL to the Spoolman instance. This parameter must be provided.
sync_rate: 5
# The interval, in seconds, between sync requests with the
# Spoolman server. The default is 5.
```

| Macro              | Descrição                                               |
| ------------------ | ------------------------------------------------------- |
| Set_active_spool   | Ele nos permite indicar qual é o ID da bobina para usar |
| Clear_active_spool | Nos permite redefinir a bobina ativa                    |

O ideal em cada caso seria adicionar ao nosso laminador,**No filamento Gcodes para cada bobina a chamada para este**, e lembre -se**Altere o ID disso uma vez consumido**Para poder controlar o restante do filamento nele !!!

![](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2F276162026-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FH6gCE2fgkkpOScJ72TP7%252Fuploads%252FrmYsCT8o5XCgHPgRdi9o%252Fimage.png%3Falt%3Dmedia%26token%3D0596900f-2b9a-4f26-ac4b-c13c4db3d786&width=400&dpr=3&quality=100&sign=8385ba85&sv=2)

### **Macros de gerenciamento de superfície impressos**

> **Aviso Aviso****Seção em processo !!!**

Geralmente, é normal que tenhamos diferentes superfícies de impressão, dependendo do acabamento que queremos ter ou do tipo de filamento.

Este conjunto de macros, creadas por[Garethky](https://github.com/garethky), eles nos permitirão ter um controle desses e, especialmente, o ajuste correto do Zoffset em cada um deles no estilo que temos nas máquinas de Prussa. Abaixo, você pode ver algumas de suas funções:

-   Podemos armazenar o número de superfícies impressas que queremos, cada uma com um nome único
-   Cada superfície de impressão terá seu próprio Zoffset
-   Se fizermos configurações de Z durante uma impressão (babystepping) de nosso klipper, essa mudança vai para o armazém na superfície habilitada naquele momento

Por outro lado, temos alguns**Requisitos para implementá -lo (será tentado adicionar a lógica da impressão do pacote**:

-   O uso de**[save_variables]**, no nosso caso, usaremos ~/variáveis.cfg para armazenar as variáveis ​​e isso já está dentro do CFG dessas macros.  
    Isso criará automaticamente um arquivo variables_build_sheets.cfg, onde nossas variáveis ​​de disco manterão.

**Exemplo de arquivo de configuração variável**

```ini
[Variables]
build_sheet flat = {'name': 'flat', 'offset': 0.0}
build_sheet installed = 'build_sheet textured_pei'
build_sheet smooth_pei = {'name': 'Smooth PEI', 'offset': -0.08999999999999997}
build_sheet textured_pei = {'name': 'Textured PEI', 'offset': -0.16000000000000003}
```

-   Devemos incluir uma chamada para aplicar_build_sheet_adjustment em nosso print_start para poder aplicar o Zoffset de superfície selecionado
-   É importante que, para a macro anterior, APPL_BUILD_SHEET_ADJUSTment, funcione corretamente, devemos adicionar um set_gcode_offset z = 0.0 antes de ligar


    # Load build sheet
    SHOW_BUILD_SHEET ; show loaded build sheet on console
    SET_GCODE_OFFSET Z=0.0 ; set zoffset to 0
    APPLY_BUILD_SHEET_ADJUSTMENT ; apply build sheet loaded zoffset

Por outro lado, é interessante poder ter algumas macros para ativar uma superfície ou outra ou até passá -lo como um parâmetro de nosso laminador para diferentes perfis de impressora ou filamento para poder carregar um ou outro automaticamente:

> **Aviso Aviso**É importante que o valor em nome = "xxxx" coincide com o nome que demos ao instalar nossa superfície de impressão

\*\* impressora.cfg

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

Também no caso de ter Klipperscreen, podemos adicionar um menu específico para poder gerenciar a carga das diferentes superfícies, onde incluiremos uma chamada para as macros criadas anteriormente para o carregamento de cada superfície:

**~/Printer_data/config/klipperscreen.conf**

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

| Macro                       | Descrição |
| --------------------------- | --------- |
| Install_build_sheet         |           |
| Show_build_sheet            |           |
| Show_build_sheets           |           |
| Set_build_sheet_offset      |           |
| Reset_build_sheet_offset    |           |
| Set_gcode_offset            |           |
| APPL_BUILD_SHEET_ADJUSTMENT |           |

### **Macros da máquina**

| Macro                                              | Descrição                                                                                                                                                                                                                   |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compile_firmware**                               | Com esta macro, podemos compilar o firmware Klipper de uma maneira simples, faça com que o firmware seja acessível a partir da interface do usuário para obter maior simplicidade e aplicá -lo aos nossos eletrônicos.      |
| Aqui você tem mais detalhes do suporte eletrônico. |                                                                                                                                                                                                                             |
| **Calcular_bed_mesh**                              | Uma macro extremamente útil para calcular a área para nossa malha, porque às vezes pode ser um processo complicado.                                                                                                         |
| **Pid_all**                                        |                                                                                                                                                                                                                             |
| **Pid_extruder**                                   |                                                                                                                                                                                                                             |
| **Pid_bed**                                        | Essas macros, onde podemos passar as temperaturas para o PID na forma de parâmetros, nos permitirão executar a calibração de temperatura de uma maneira extremamente simples.                                               |
| **Test_speed**                                     |                                                                                                                                                                                                                             |
| **Test_speed_delta**                               | Macro original do parceiro[Ellis](https://github.com/AndrewEllis93)Eles nos permitirão de uma maneira bastante simples de testar a velocidade com que podemos mover nossa máquina de maneira precisa e sem perda de etapas. |

\*\_**Compilado de firmware para electronicas soportadas**, Para facilitar o processo de criação e manutenção do nosso firmware Klipper para o nosso MCU, temos o Macro Compile_firmware que, ao executá -lo, podemos usar nossos eletrônicos como um parâmetro para fazer apenas isso, o Klipper compilará para todos os eletrônicos suportados por nosso BAGLE:![Firmware compilation options](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FErIelUs1lDcFKMTBIKyR%2Fimage.png&width=300&dpr=2&quality=100&sign=e2d8f5d5&sv=2)Encontraremos esses acessíveis de maneira simples em nosso site de interface do usuário no diretório Firmware_binaries em nossa guia Máquina (se usarmos a vela principal):![Firmware binaries accessible from Mainsail UI](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FYmubeTDwxD5Yjk7xR6gS%2Ftelegram-cloud-photo-size-4-6019366631093943185-y.jpg&width=300&dpr=2&quality=100&sign=2df66da&sv=2)Então você tem a lista de eletrônicos suportados:

> ⚠️**IMPORTANTE!!!**
>
> Esses scripts estão preparados para trabalhar em um sistema de raspbian com usuário de PI, se você não for o seu caso, você deve adaptá -lo.
>
> Os firmes são gerados para uso com a conexão USB que é sempre o que aconselhamos, além disso, o ponto de montagem USB é sempre o mesmo pela sua configuração da sua conexão MCU não mudará se forem gerados com nossa macro/script
>
> **Para que o Klipper possa executar macros de shell, uma extensão deve ser instalada, graças ao parceiro**[**Arksine**](https://github.com/Arksine)**, deixe isso.**
>
> **Dependendo do Klipper Dystro usado, eles já podem ser ativados.**
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2FTfVEVUxY0srHCQCN3Gjw%2Fimage.png&width=300&dpr=2&quality=100&sign=84a15271&sv=2)
>
> A maneira mais simples é usar[**Kioh**](../instalacion/#instalando-kiauh)Onde encontraremos em uma de suas opções a possibilidade de instalar esta extensão:
>
> ![Shell command extension installation](https://klipper.3dwork.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FH6gCE2fgkkpOScJ72TP7%2Fblobs%2F0FjYUlWC4phJ8vcuaeqT%2Ftelegram-cloud-photo-size-4-5837048490604215201-x_partial.jpg&width=300&dpr=2&quality=100&sign=7172f9eb&sv=2)
>
> Também podemos executar o processo manualmente, copiaremos manualmente o plug -in para Klipper &lt;[**gcode_shell_extension**](https://raw.githubusercontent.com/Rat-OS/RatOS/master/src/modules/ratos/filesystem/home/pi/klipper/klippy/extras/gcode_shell_command.py)dentro do nosso diretório`_**~/klipper/klippy/extras**_`usando SSH o SCP y reiniciamos Klipper.

| Electrónica        | Nome do parâmetro para usar na macro |
| ------------------ | ------------------------------------ |
| Manta              | Estou orgulhoso                      |
| Faça M4p           | BTT-MANTA-M4P                        |
| Manta M4P v2.      | BTT-MANTA-M4P-22                     |
| Faça M8p           | BTT-MANTA-M8P                        |
| Marking M8P v1.1   | BTT-MANTA-M8P-11                     |
| Octopus max isso   | BTT-Octopus-max-ez                   |
| Octopus Pro (446)  | BTT-OCTOPUS-PRO-446                  |
| Octopus Pro (429)  | BTT-Octopus-Pro-429                  |
| Octopus Pro (H723) | BTT-Octopus-Pro-H723                 |
| Octopus v1.1       | BTT-Octopus-11                       |
| Octopus v1.1 (407) | BTT-Octopus-11-407                   |
| Skr Pro v1.2       | Skr_pro_12                           |
| Skr 3              | BTT parafuso 3                       |
| Saqr a (heha)      | Inteligente                          |
| Skr 3 isso         | BTT-SC-3-EZ                          |
| Skr 3 This (H723)  | Skirzhahah                           |
| Skr 2 (429)        | BTT-SRC-2-429                        |
| Skr 2 (407)        | BTT-SRC-2-407                        |
| Grita              | BTT-SKRAT-10                         |
| Por 1,4 turbo      | BTT-SC-14-TURBO                      |
| Skri Mini          | BTT_SKR_MINI_E3_30                   |

| Toolhead (lata) | Nome do parâmetro para usar na macro |
| --------------- | ------------------------------------ |
| EBB42 v1        | BTT_EBB42_10                         |
| EBB36 V1        | BTT_EBB36_10                         |
| EBB42 v1.1      | BTT_EBB42_11                         |
| EBB36 v1.1      | BTT_EBB36_11                         |
| EBB42 v1.2      | BTT_EBB42_12                         |
| EBB36 v1.2      | BTT_EBB36_12                         |

| **Electrónica**          | **Nome do parâmetro para usar na macro** |
| ------------------------ | ---------------------------------------- |
| MKS EAGLE V1.X           | MKS-EGLE-10                              |
| MCS Robin Nano assado    | MKS-ROBIN-NANO-30                        |
| Mks robin nano v2        | MKS-ROBIN-NANO-20                        |
| Mks gen l                | MKS-GEN-L                                |
| A culpa de Robin Nano du | Zinbennanda                              |

| Toolhead (lata)   | Nome do parâmetro para usar na macro |
| ----------------- | ------------------------------------ |
| Mellow Fly Sht 42 | Mellow_fly_sht_42                    |
| Mellow Fly Sht 36 | Mellow_fly_sht_36                    |

| Electrónica   | Nome do parâmetro para usar na macro |
| ------------- | ------------------------------------ |
| Aranha fysetc | aranha fysetc                        |

| Electrónica          | Nome do parâmetro para usar na macro |
| -------------------- | ------------------------------------ |
| Artilharia Ruby v1.x | Artilharia-Ruby-12                   |

| Electrónica           | Nome do parâmetro para usar na macro |
| --------------------- | ------------------------------------ |
| Raspberry Pico/RP2040 | RPI-RP2040                           |

| Electrónica    | Nome do parâmetro para usar na macro |
| -------------- | ------------------------------------ |
| Leviathan v1.2 | Leviathan-12                         |

### Adicionando macros 3DWork à nossa instalação

A partir da nossa interface, mainsail/fluidd, editaremos nossa impressora.cfg e adicionaremos:

**impressora.cfg**

```ini
## 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]
## 3Dwork shell macros
[include 3dwork-klipper/shell-macros.cfg]
```

> ℹ️**Informação !!!**É importante que adicionemos essas linhas no final de nosso arquivo de configuração ... logo acima da seção, para que, no caso de macros em nosso CFG, sejam sobrecarregadas por nossas: 
> \#\*# \\ &lt;--- save_config --->

> ⚠️**IMPORTANTE!!!**Macros normais foram separadas de**Macros Shell**dado que**Para habilitá -las, é necessário fazer etapas manuais adicionais que estão testando atualmente**e\*\*Eles podem exigir permissões extras para atribuir permissões de execução para as quais as instruções não foram indicadas, pois estão tentando automatizar.\*\***Se você os usar, está sob sua própria responsabilidade.**

### Configurações do nosso laminador

Como nossos macros são dinâmicos, eles extrairão certas informações da configuração da impressora e do próprio laminador. Para fazer isso, aconselhamos você a configurar seus laminadores da seguinte forma:

-   **gcode de inicio START_PRINT**, usando espaços reservados para passar os valores de temperatura do filamento e do leito dinamicamente:

**Prusaslicer**

```ini
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count] ; Provide layer information
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

**Superslicer**- Temos a opção de ajustar a temperatura do gabinete (câmara)

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

> ⚠️**Aviso!!!**Devemos instalar o plugin[**Plugin de pós -processo (de Frankbags)**](https://gist.github.com/frankbags/c85d37d9faff7bce67b6d18ec4e716ff)Do menu_**Ajuda/show**_configuration Folder... copiaremos el script del link anterior dentro de la carpeta script.  
> Reiniciamos Cura e iremos a_**Extensões/pós-processamento/modifique o código G.**_E vamos selecionar_**Tamanho de impressão de malha**_.

**IDEAMAKER**

```ini
START_PRINT EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed}
```

**Simplificar3d**

```ini
START_PRINT EXTRUDER_TEMP=[extruder0_temperature] BED_TEMP=[bed0_temperature]
```

> ℹ️**Informação !!!**O**Os espaços reservados são "aka" ou variável**de impressão.
>
> Nos links a seguir, você pode encontrar uma lista deles para:[**Prusaslicer**](https://help.prusa3d.com/es/article/lista-de-placeholders_205643),[**Superslicer**](https://github.com/supermerill/SuperSlicer/wiki/Macro-&-Variable-list)(além dos do anterior),[**Bambu Studio**](https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list)e[**Cura**](http://files.fieldofview.com/cura/Replacement_Patterns.html).
>
> O uso destes permite que nossas macros sejam dinâmicas.

-   **gcode de final END_PRINT**, neste caso, quando não estiver usando os suportes dos portadores, é comum a todos os laminadores

```ini
END_PRINT
```

### Variáveis

Como já mencionamos, essas novas macros nos permitirão ter algumas funções muito úteis, como listamos anteriormente.

Para o ajuste destes em nossa máquina, usaremos as variáveis ​​que encontraremos em macros/macros_var_globals.cfg e que detalhamos abaixo.

#### Linguagem de mensagem/notificações

Como muitos usuários gostam de ter as notificações de macros em seu idioma, desenvolvemos um sistema de notificação em vários idiomas, atualmente espanhol (s) e inglês (EN). Na variável a seguir, podemos ajustá -la:

| Variável          | Descrição                                                                                                         | Valores posibles | Valor por defecto |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable_language | Ele nos permite selecionar o idioma das notificações. No caso de não ser bem definido, ele será usado em (inglês) | É / em           | é                 |

#### Extrusão relativa

Ele permite controlar o modo de extrusão que usaremos no final do nosso start_print. O valor dependerá da configuração do nosso laminador.

> 💡**Conselho**É aconselhável configurar seu laminador para o uso de extrusão relativa e ajustar essa variável para true.

| Variável                    | Descrição                                                            | Valores posibles   | Valor por defecto |
| --------------------------- | -------------------------------------------------------------------- | ------------------ | ----------------- |
| variable_relative_extrusion | Ele nos permite indicar o modo de extrusão usado em nosso laminador. | Verdadeiro / falso | Verdadeiro        |

#### Velocidades

Para gerenciar as velocidades usadas em macros.

| Variável                    | Descrição                            | Valores posibles | Valor por defecto |   |
| --------------------------- | ------------------------------------ | ---------------- | ----------------- | - |
| variable_macro_travel_speed | Velocidade em tradução               | numérico         | 150               |   |
| variable_macro_z_speed      | Velocidade em tradução para o eixo z | numérico         | 15                |   |

#### Homing

Conjunto de variáveis ​​relacionadas ao processo de homing.

| Variável | Descrição | Valores posibles | Valor por defecto |
| -------- | --------- | ---------------- | ----------------- |

#### Aquecimento

Variáveis ​​relacionadas ao processo de aquecimento de nossa máquina.

| Variável                                   | Descrição                                                                           | Valores posibles   | Valor por defecto |
| ------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------ | ----------------- |
| variable_preseat_extruder                  | Ativar o bico pré -aquecido na temperatura indicada em variable_preeat_xtruder_temp | Verdadeiro / falso | Verdadeiro        |
| variable_preseat_extruder_temp             | Temperatura pré -aquecida do bico                                                   | numérico           | 150               |
| variable_start_print_heat_chamber_bed_temp | Temperatura do leito durante o processo de aquecimento nosso gabinete               | numérico           | 100               |

> 💡**Conselho**Benefícios do uso do bico pré -aquecido:

-   Permite -nos tempo adicional para a cama atingir sua temperatura de uma maneira uniforme
-   Se usarmos um sensor indicativo que não possui compensação de temperatura, ele nos permitirá tornar nossas medidas mais consistentes e precisas
-   Permite suavizar qualquer restante do filamento no bico que permite, em certas configurações, esses restos não afetam a ativação do sensor 
    { % endhint %}

#### Mallado de cama (Bed Mesh)

Para controlar o processo de nivelamento, temos variáveis ​​que podem ser muito úteis. Por exemplo, podemos controlar o tipo de nivelamento que queremos usar criando sempre uma nova malha, carregando um armazenado anteriormente ou usando uma malha adaptativa.

| Variável                                                                                                                             | Descrição                                                                     | Valores posibles | Valor por defecto |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable_calibrate_bed_mesh                                                                                                          | Ele nos permite selecionar que tipo de miséria usaremos em nosso start_print: |                  |                   |
| - Nova malha, nos tornará uma miséria em cada impressão                                                                              |                                                                               |                  |                   |
| - Storedmeh, carregará uma malha armazenada e não executará a enquete da cama                                                        |                                                                               |                  |                   |
| - Adaptativo, nos tornará uma nova miséria, mas adaptada à zona de impressão, melhorando nossas primeiras camadas em muitas ocasiões |                                                                               |                  |                   |
| -Nomesh, no caso de não termos um sensor ou usar o processo para pular o processo                                                    | nova malha / malha armazenada / adaptativa /                                  |                  |                   |
| NOMA                                                                                                                                 | Adaptativo                                                                    |                  |                   |
| variable_bed_mesh_profile                                                                                                            | O nome usado para nossa malha armazenada                                      | texto            | padrão            |

> ⚠️**Aviso!!!**Aconselhamos que você use o nível adaptativo, pois ele sempre ajustará a miséria ao tamanho de nossa impressão, permitindo que você tenha uma área de Malle ajustada.
>
> É importante que tenhamos em nosso[Iniciar -Up Gcode](../empezamos/configuracion-klipper-en-laminadores.md#configurando-nuestro-laminador-para-usar-nustras-macros-start_print-y-end_print), na chamada para o nosso start_print, os valores print_max e print_min.

#### Purgado

Uma fase importante do início da impressão é uma purga correta do nosso bico para evitar restos de filamento ou que eles podem danificar nossa impressão em algum momento. Então você tem as variáveis ​​envolvidas nesse processo:
| Variável | Descrição | Valores possíveis | Valor padrão |
\| --- \| --- \| --- \| --- \|
| Variable_nozled_priMing | Podemos escolher entre diferentes opções de pureza:<br>- Primeline: desenhe a linha purgada típica<br>- Primellineadaptive: gera uma linha de purga adaptada à zona de impressão usando variável_nazzle_priMing_objectDistance como margem<br>- Primoblob: faz uma gota de filamento em um canto da cama | Primeline / primellineadaptive / primeblob / false | PrimelineAdaptative |
| Variable_nozled_pressing_objectDistance | Se usarmos a linha de purga adaptativa, será a margem a ser usada entre a linha de purga e o objeto impresso | numérico | 5 |
| Variable_nozled_prime_start_x | Onde localizar nossa linha de purga em x:<br>- min: x = 0 (mais margem de segurança)<br>- max: X=max (menos margen de seguridad)<br>- Número: Coordenada x específica | min / max / número | Max |
| Variable_nozled_prime_start_y | Onde localizar nossa linha de purga em y:<br>- min: y = 0 (mais margem de segurança)<br>- max: y = max (menos sala de segurança)<br>- Número: coordenada e específica | min / max / número | min |
| Variable_nozled_prime_direction | Endereço de linha ou queda:<br>- para trás: em direção à frente<br>- forwards: hacia atrás<br>- Auto: em direção ao centro de acordo com variável_nazzle_prime_start_y | Auto / Forwards / para trás | Auto |

#### Carga/Descarga de filamento

Nesse caso, esse grupo de variáveis ​​facilitará o gerenciamento do carregamento e descarga do nosso filamento usado na emulação do M600, por exemplo ou lançando as macros de carregamento e descarga do filamento:

| Variável                        | Descrição                                                                                                                                                                                                                                                                                                                                                                             | Valores posibles | Valor por defecto |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable_filament_unload_length | Quanta retirada em mm o filamento, ajuste à sua máquina, normalmente a medida do seu bico para as engrenagens da sua extrusora adicionando uma margem extra.                                                                                                                                                                                                                          | número           | 130               |
| variable_filament_unload_speed  | Velocidade de retração do filamento em mm/s normalmente é usada uma velocidade lenta.                                                                                                                                                                                                                                                                                                 | número           | 5                 |
| variable_filament_load_length   | Distância em mm para carregar o novo filamento ... como em variable_filament_unload_length, usaremos a medida da sua engrenagem de extrusora, adicionando uma margem extra, nesse caso, esse valor extra dependerá de quanto você deseja ser purgado ... Geralmente, você pode dar mais margem do que o valor anterior para garantir que seja limpo a extrusão do filamento anterior. | número           | 150               |
| variable_filament_load_speed    | Velocidade de carga do filamento em mm/s Normalmente, uma velocidade mais rápida é usada para descarregar.                                                                                                                                                                                                                                                                            | número           | 10                |

> ⚠️**Aviso!!!**Outro ajuste necessário para sua seção**[extrusora]**o indicado[**max_extrude_only_distance**](https://www.klipper3d.org/Config_Reference.html#extruder)... O valor aconselhável é geralmente> 101 (se não for definido, usa 50) para, por exemplo, permita os testes de calibração da extrusora típica.  
> Você deve ajustar o valor com base no acima do teste ou na configuração do seu**variable_filament_unload_length**EU**variable_filament_load_length**.

#### Estacionamento

Em certos processos de nossa impressora, como o lazer, é aconselhável fazer um estacionamento da nossa cabeça. As macros do nosso pacote têm essa opção, além das seguintes variáveis ​​a serem gerenciadas:

| Variável                           | Descrição                                                                                                                                                                                                                                           | Valores posibles | Valor por defecto |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable_start_print_park_in       | Localização onde estacionar a cabeça durante o pré-escalão.                                                                                                                                                                                         | voltar /         |                   |
| CENTRO /                           |                                                                                                                                                                                                                                                     |                  |                   |
| frente                             | voltar                                                                                                                                                                                                                                              |                  |                   |
| variable_start_print_park_z_height | Z altura durante o pré-pesado                                                                                                                                                                                                                       | número           | 50                |
| variable_end_print_park_in         | Localização para estacionar a cabeça no final ou cancelar uma impressão.                                                                                                                                                                            | voltar /         |                   |
| CENTRO /                           |                                                                                                                                                                                                                                                     |                  |                   |
| frente                             | voltar                                                                                                                                                                                                                                              |                  |                   |
| variable_end_print_park_z_hop      | Distância para subir no final da impressão.                                                                                                                                                                                                         | número           | 20                |
| variable_pause_print_park_in       | Localização para estacionar a cabeça por Pausar a impressão.                                                                                                                                                                                        | voltar /         |                   |
| CENTRO /                           |                                                                                                                                                                                                                                                     |                  |                   |
| frente                             | voltar                                                                                                                                                                                                                                              |                  |                   |
| variable_pause_idle_timeout        | Valor, em segundos, da ativação do processo de inatividade na máquina que libera motores e perdendo coordenadas,**É aconselhável um valor alto para ativar a macro de pausa o suficiente para executar qualquer ação antes de perder coordenadas.** | número           | 43200             |

#### Z-Tilt

Aproveite ao máximo nossa máquina para que seja auto -nível e facilite que nossa máquina esteja sempre em melhores condições é essencial.

**Z-Tilt é basicamente um processo que nos ajuda a alinhar nossos motores Z em relação ao nosso eixo/eixo de gantry x (cartesiano) ou xy (corexy) (corexy)**. Com isso**Garantimos que sempre tenhamos nosso Z perfeitamente e de uma maneira precisa e automática**.

| Variável                  | Descrição                                                                                  | Valores posibles   | Valor por defecto |
| ------------------------- | ------------------------------------------------------------------------------------------ | ------------------ | ----------------- |
| variable_calibrate_z_tilt | Permite, no caso de ativá-lo em nossa configuração de Klipper, o processo de ajuste Z-Tilt | Verdadeiro / falso | Falso             |

#### Inclinado

O uso de[Inclinado](broken-reference)Para a correção ou ajuste preciso de nossas impressoras, é extremamente aconselhável se tivermos desvios em nossas impressões. Usando a seguinte variável, podemos permitir o uso em nossas macros:

| Variável              | Descrição                                                                                                                                                                                                              | Valores posibles | Valor por defecto |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| variable_skew_profile | Ele nos permite levar em consideração nosso perfil de inclinação que será cobrado em nossa macro start_print. Para ativá -lo, devemos discutir a variável e usar o nome do perfil de inclinação de nossa configuração. | texto            | my_skew_profile   |

### Personalização de macros

Nosso módulo Klipper usa o sistema de configuração modular usado nos tempos e aproveita as vantagens de Klipper no processo de arquivo de configuração sequencialmente. É por isso que a ordem dos ajustes de inclusão e personalização que queremos aplicar nesses módulos é essencial.

> ℹ️**Informação !!!**Ao usar as configurações do 3DWork como módulo, elas não podem ser editadas diretamente do diretório 3DWork-Kipper no diretório de configuração do Klipper, pois ele será somente leitura (restrito à leitura) para segurança.
>
> É por isso que é muito importante entender o funcionamento de Klipper e como personalizar nossos módulos em sua máquina.

#### **Personalizando variables**

Normalmente, será o que teremos que ajustar, para fazer ajustes nas variáveis ​​que temos por padrão em nosso módulo**3dwork**para Klipper.

Simplesmente, o que temos que fazer é colar o conteúdo macro**[gcode_macro global_vars]** que podremos encontrar en macros/macros_var_globals.cfg en nuestro printer.cfg.

Lembramos o que foi comentado anteriormente sobre como o Klipper processa as configurações sequencialmente, por isso é aconselhável colá -lo após os inclusões, dizemos a você[aqui](3dwork-klipper-bundle.md#anadiendo-las-macros-3dwork-a-nuestra-instalacion).

Teremos algo assim (é apenas um exemplo visual):

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

> ⚠️**Aviso!!!**Os três pontos (...) dos exemplos anteriores são apenas para indicar que você pode ter mais configurações entre seções ... em nenhum caso elas devem usar.

> ℹ️**Informação !!!**
>
> -   Aconselhamos você a adicionar comentários como você vê no caso anterior para identificar o que cada seção faz
> -   Embora você não precise tocar em todas as variáveis, recomendamos que você copie todo o conteúdo de**[gcode_macro global_vars]**

#### Personalizando macros

As macros montadas de maneira modular para que possam ser ajustadas de maneira simples. Como mencionamos antes, se queremos ajustá -los, devemos proceder como fizemos com as variáveis, copie a macro em questão em nossa impressora.cfg (ou outra inclui a nossa) e verifique se é após a inclusão de onde adicionamos nosso módulo 3DWork para Klipper.

Temos dois grupos de macros:

-   Macros Para adicionar configurações do usuário, essas macros podem ser facilmente adicionadas e personalizadas porque foram adicionadas para que qualquer usuário possa personalizar as ações ao seu gosto em certa parte dos processos que cada macro faz.

**Start_print**

| Nome macro                                | Descrição                                                                                                                              |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| \_User_start_print_heat_chamber           | Ele é executado logo após o nosso gabinete começar a aquecer, se o Chamber_temp for passado como um parâmetro para o nosso start_print |
| \_User_start_print_before_homing          | É executado antes do lar inicial para o início da impressão                                                                            |
| \_User_start_print_after_heating_bed      | Ele corre quando nossa cama chega à sua temperatura, antes de \_start_print_after_heating_bed                                          |
| \_User\_ start_print bed_mesh             | Se lanza antes de \_START_PRINT_BED_MESH                                                                                               |
| \_User_start_print_park                   | Se lanza antes de \_START_PRINT_PARK                                                                                                   |
| \_User_start_print_after_heating_extruder | Se lanza antes de \_START_PRINT_AFTER_HEATING_EXTRUDER                                                                                 |

**End_print**

| Nome macro                           | Descrição                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------- |
| \_User_end_print_before_heatters_off | Ele é executado antes de executar o aquecedor, antes de \_end_print_before_heaters_off |
| \_USER_END_PRINT_AFTER_HEATERS_OFF   | Ele funciona após o aquecimento, antes de \_end_print_after_heatters_off               |
| \_User_end_print_park                | É executado antes da cabeça da cabeça, antes de \_end_print_park                       |

**Print_basics**

| Nome macro          | Descrição                          |
| ------------------- | ---------------------------------- |
| \_User_pause_start  | É executado no início de uma pausa |
| \_User_pause_end    | Ele corre no final de uma pausa    |
| \_User_resume_start | É executado no início de um resumo |
| \_User_resume_end   | Corre no final de um resumo        |

-   Macros internos, eles são macros para dividir a macro principal em processos e são importantes para isso. É aconselhável que, no caso de exigir que sejam copiados como estão.

**Start_print**

| Nome macro                           | Descrição                                                                                                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_Start_print_heat_chamber           | Aquece o gabinete no caso de o parâmetro Chamber_Temp ser recebido por nossa macro start_print do laminador                                                                                                   |
| \_Start_print_after_heating_bed      | Ele é executado quando a cama chega à temperatura, após \_user_start_print_after_heating_bed. Normalmente, ele é usado para o processamento de calibração do leito (Z_TILT_ADJUST, Quad_Gantry_Leveling, ...) |
| \_Start_print_bed_mesh               | Ele é responsável pela lógica da miséria da cama.                                                                                                                                                             |
| \_Start_print_park                   | Apeita a cabeça de impressão enquanto aquece o bico na temperatura de impressão.                                                                                                                              |
| \_Start_print_after_heating_extruder | Faça o Nazzle Purge e carregue o perfil de inclinação, caso definimos nas variáveis                                                                                                                           |

## Impressoras e eletrônicos

À medida que trabalhamos com diferentes modelos de impressoras e eletrônicos, adicionaremos aqueles que não são suportados diretamente por tempos, sejam contribuições ou a comunidade.

-   Impressoras, neste diretório, teremos todas as configurações da impressora
-   Placas, aqui vamos encontrar eletrônicos

### Parâmetros e pinos

Nosso módulo Klipper usa o sistema de configuração modular usado nos tempos e aproveita as vantagens de Klipper no processo de arquivo de configuração sequencialmente. É por isso que a ordem dos ajustes de inclusão e personalização que queremos aplicar nesses módulos é essencial.

> ℹ️**Informação !!!**Ao usar as configurações do 3DWork como módulo, elas não podem ser editadas diretamente do diretório 3DWork-Kipper no diretório de configuração do Klipper, pois ele será somente leitura (restrito à leitura) para segurança.
>
> É por isso que é muito importante entender o funcionamento de Klipper e como personalizar nossos módulos em sua máquina.

Tal como os explicábamos en "[personalizando macros](3dwork-klipper-bundle.md#personalizando-macros)"Usaremos o mesmo processo para ajustar parâmetros ou pinos para ajustá -los às nossas necessidades.

#### Personalizando parámetros

Enquanto aconselhamos você a criar uma seção em sua impressora.cfg que é chamada de substituição do usuário, colocada após a inclusão de nossas configurações, para poder ajustar e personalizar qualquer parâmetro usado neles.

No exemplo a seguir, veremos como, no nosso caso, estamos interessados ​​em personalizar os parâmetros de nosso nivelamento da cama (Bed_meh) ajustando os pontos de pesquisa (Probe_Count) com relação à configuração que temos por padrão nas configurações do módulo Klipper:

**impressora.cfg**

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

> ⚠️**Aviso!!!**Os três pontos (...) dos exemplos anteriores são apenas para indicar que você pode ter mais configurações entre seções ... em nenhum caso elas devem usar.

Podemos usar esse mesmo processo com qualquer parâmetro que queremos ajustar.

#### Personalizando a configuração do pinheiro

Procederemos exatamente como fizemos antes, em nossa área de substituição do usuário, adicionaremos as seções de pinos que queremos ajustar ao nosso gosto.

No exemplo a seguir, personalizaremos o que é o PIN de nosso ventilador eletrônico (controlador_fan) para atribuí -lo a um diferente de padrão:

**impressora.cfg**

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

> ⚠️**Aviso!!!**Os três pontos (...) dos exemplos anteriores são apenas para indicar que você pode ter mais configurações entre seções ... em nenhum caso elas devem usar.
