# 3Dwork Klipper Wizard

## Descripción

El **3Dwork Klipper Wizard** es un asistente interactivo que facilita la configuración de impresoras 3D con Klipper. Permite seleccionar electrónica, configurar la impresora, generar archivos `printer.cfg` y compilar firmware de forma guiada.

Versión: **2.0.0-dev**

## Características

- **CLI Interactivo** — Menú guiado paso a paso en terminal
- **Web Wizard** — Interfaz visual en el navegador
- **+50 Electrónicas** — BigTreeTech, MKS, Fysetc, Creality, Mellow, etc.
- **Generador de Config** — Crea `printer.cfg` personalizado con templates
- **Biblioteca de Configs** — Presets de Klipper examples, RatOS, Creality Sonic Pad
- **Instalación One-liner** — Instalación en un solo comando

## Requisitos

- Raspberry Pi (o cualquier host con Linux)
- Python 3.8+
- Git
- Conexión a Internet
- (Opcional) Flask para Web Wizard

## Instalación

### Instalación Rápida (One-liner)

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

### Instalación Manual

```bash
# 1. Clonar el repositorio (rama dev)
cd ~/printer_data/config
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git

# 2. (Opcional) Instalar dependencias para Web Wizard
pip3 install flask

# 3. Ejecutar el wizard
python3 3dwork-klipper/wizard/cli.py
```

## Uso

### CLI Interactivo

```bash
python3 ~/printer_data/config/3dwork-klipper/wizard/cli.py
```

### Web Wizard

```bash
cd ~/printer_data/config/3dwork-klipper
python3 wizard/web/app.py
# Acceder a http://tu-raspberry:5000
```

### Menú Principal

```
╔════════════════════════════════════════════════╗
║              MENÚ PRINCIPAL                ║
╠════════════════════════════════════════════════╣
║  1. Seleccionar Electrónica                   ║
║  2. Configurar Impresora                       ║
║  3. Generar printer.cfg                         ║
║  4. Compilar Firmware                          ║
║  5. Instalar 3Dwork-klipper                    ║
║  6. Actualizar Instalación                     ║
║  7. Configuración Actual                        ║
║  8. Biblioteca de Configs                       ║
║  9. Web Wizard (servidor local)                ║
║  0. Salir                                       ║
╚════════════════════════════════════════════════╝
```

## Flujo de Uso

### 1. Seleccionar Electrónica

Elige tu electrónica de la lista de +50 boards soportados:

- **BigTreeTech**: Manta (E3 EZ, M4P, M8P), Octopus, SKR (Pro, 3, Mini E3)
- **MKS**: Robin Nano, Eagle, Gen L
- **Fysetc**: Spider, Cheetah
- **Creality**: v4.2.x, K1
- **Mellow**: FLY-GEM, FLY SHT (CAN)
- **BTT CAN**: EBB42, EBB36

### 2. Configurar Impresora

Define los parámetros de tu impresora:

- **Kinematics**: Cartesian, CoreXY, CoreXY (UART), Delta
- **Velocidad máxima**: mm/s
- **Aceleración**: mm/s²
- **Rotation Distance**: para cada eje
- **Microsteps**: 16, 32, 64

### 3. Características Adicionales

Añade features opcionales:

- **Probe**: BLTouch, Inductivo, Capacitivo
- **Display**: ST7920, SSD1306, HD44780
- **Sensor de filamento**

### 4. Generar printer.cfg

El wizard genera un `printer.cfg` completo con:

- Configuración de steppers
- Extruder y heaters
- Probe y bed_mesh (si está configurado)
- Display (si está configurado)
- Includes para macros de 3dwork-klipper

## Electrónicas Soportadas

### BigTreeTech Manta
| ID | Nombre | MCU | CAN |
|-----|--------|-----|-----|
| btt-manta-e3ez | Manta E3 EZ | stm32g0b1 | ✓ |
| btt-manta-m4p | Manta M4P | stm32h743 | ✓ |
| btt-manta-m8p | Manta M8P | stm32h743 | ✓ |
| btt-manta-m8p-11 | Manta M8P v1.1 | stm32h743 | ✓ |
| btt-manta-m8p-v2 | Manta M8P v2.0 | stm32h743 | ✓ |

### BigTreeTech Octopus
| ID | Nombre | MCU |
|-----|--------|-----|
| btt-octopus-max-ez | Octopus Max EZ | stm32h723 |
| btt-octopus-pro-446 | Octopus Pro (446) | stm32f446 |
| btt-octopus-pro-429 | Octopus Pro (429) | stm32f429 |
| btt-octopus-pro-h723 | Octopus Pro (H723) | stm32h723 |
| btt-octopus-11 | Octopus v1.1 | stm32f407 |

### BigTreeTech SKR
| ID | Nombre | MCU |
|-----|--------|-----|
| skr_pro_12 | SKR Pro v1.2 | stm32f407 |
| btt-skr-3 | SKR 3 | stm32h743 |
| btt-skr-3-ez | SKR 3 EZ | stm32h743 |
| btt-skr-2-407 | SKR 2 (407) | stm32f407 |
| btt-skrat-10 | SKR RAT | stm32f407 |
| btt-skr-14-turbo | SKR 1.4 Turbo | stm32f407 |
| btt_skr_mini_e3_30 | SKR Mini E3 v3.0 | stm32g0b1 |

### MKS Instruments
| ID | Nombre |
|-----|--------|
| mks-robin-nano-v3 | MKS Robin Nano v3 |
| mks-robin-nano-20 | MKS Robin Nano v2 |
| mks-eagle-10 | MKS Eagle v1.0 |
| mks-gen-l | MKS Gen L |

### CAN Toolheads
| ID | Nombre |
|-----|--------|
| btt-ebb42-12 | EBB42 v1.2 (CAN) |
| btt-ebb36-12 | EBB36 v1.2 (CAN) |
| mellow-fly-sht-42 | FLY SHT 42 (CAN) |
| mellow-fly-sht-36 | FLY SHT 36 (CAN) |

## Solución de Problemas

### El wizard no inicia

```bash
# Verificar Python
python3 --version

# Si hay errores de permisos
chmod +x ~/printer_data/config/3dwork-klipper/wizard/cli.py
```

### Error al generar config

```bash
# Verificar permisos del directorio
ls -la ~/printer_data/config/

# Crear directorio si no existe
mkdir -p ~/printer_data/config
```

### Web Wizard no funciona

```bash
# Instalar Flask
pip3 install flask

# Verificar que el puerto 5000 está libre
netstat -tuln | grep 5000
```

### La compilación de firmware falla

Asegúrate de tener instalado:

```bash
# Debian/Ubuntu
sudo apt install build-essential libncurses-dev

# Verificar Klipper instalado
ls ~/klipper/
```

## Bibliotecas de Configuración

El wizard puede acceder a configs de múltiples fuentes:

- **3Dwork-klipper** — Configuraciones propias
- **Klipper Examples** — Ejemplos oficiales de Klipper
- **RatOS** — Configuraciones de RatOS
- **Creality Sonic Pad** — Presets de Sonic Pad

## Actualización

```bash
# Opción 1: Desde el wizard
python3 3dwork-klipper/wizard/cli.py
# Seleccionar "Actualizar Instalación"

# Opción 2: Manual
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

## Contribuir

¿Encontraste un bug? ¿Tienes sugerencias?

1. Crea un issue en GitHub
2. Haz fork y PR a la rama `dev`

## Licencia

MIT License - libre como un mammoth en la pradera.

---

**3Dwork** — El referente en español sobre impresión 3D

- Web: https://3dwork.io
- GitHub: https://github.com/3dwork-io
- Tools: https://3dwork.io/tools/