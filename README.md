# 3Dwork Klipper Bundle

## Paquete de macros, configuraciones y utilidades para Klipper

![Español](https://flagcdn.com/w40/es.png)[![English](https://flagcdn.com/w40/gb.png)](README.en.md) [![Deutsch](https://flagcdn.com/w40/de.png)](README.de.md) [![Italiano](https://flagcdn.com/w40/it.png)](README.it.md) [![Français](https://flagcdn.com/w40/fr.png)](README.fr.md) [![Português](https://flagcdn.com/w40/pt.png)](README.pt.md)

[![Ko-fi Logo](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> **⚠️ ADVERTENCIA** Esta rama `dev` incluye el **3Dwork Klipper Wizard** en desarrollo activo. Para producción, usa la rama `master`.

---

## NEW — 3Dwork Klipper Wizard

### ¿Qué es el Wizard?

El **3Dwork Klipper Wizard** es un asistente interactivo que facilita la configuración de impresoras 3D con Klipper, tanto para noveles como para usuarios avanzados.

### Características

- **CLI Interactivo** — Menú guiado paso a paso en terminal
- **Web Wizard** — Interfaz visual en el navegador (Flask)
- **+50 Electrónicas** — BigTreeTech, MKS, Fysetc, Creality, Mellow, etc.
- **Generador de Config** — Crea `printer.cfg` personalizado
- **Biblioteca de Configs** — Presets de Klipper examples, RatOS, Creality Sonic Pad
- **Instalación One-liner** — Instalación en un solo comando

---

## Instalación

### Instalación Rápida (Wizard)

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

### Instalación Manual

```bash
cd ~/printer_data/config
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

---

## Usar el Wizard

### CLI Interactivo

```bash
python3 ~/printer_data/config/3dwork-klipper/wizard/cli.py
```

Menú:
```
╔════════════════════════════════════════════════╗
║              MENÚ PRINCIPAL                ║
╠════════════════════════════════════════════════╣
║  1. Seleccionar Electrónica                   ║
║  2. Configurar Impresora                       ║
║  3. Generar printer.cfg                         ║
║  4. Compilar Firmware                           ║
║  5. Instalar 3Dwork-klipper                    ║
║  6. Actualizar Instalación                      ║
║  7. Configuración Actual                        ║
║  8. Biblioteca de Configs                       ║
║  9. Web Wizard                                  ║
║  0. Salir                                       ║
╚════════════════════════════════════════════════╝
```

### Web Wizard

```bash
# Instalar Flask si no lo tienes
pip3 install flask

# Iniciar servidor
cd ~/printer_data/config/3dwork-klipper
python3 wizard/web/app.py
```

Luego abre en tu navegador: `http://tu-raspberry:5000`

---

## Electrónicas Soportadas

### BigTreeTech
| Categoría | Modelos |
|-----------|---------|
| **Manta** | E3 EZ, M4P, M4P v2.2, M8P, M8P v1.1, M8P v2 |
| **Octopus** | Max EZ, Pro (446/429/H723), v1.1 |
| **SKR** | Pro v1.2, 3, 3 EZ, 2, RAT, 1.4 Turbo, Mini E3 v3 |

### MKS Instruments
- Robin Nano v3/v2, Eagle v1.x, Gen L

### Fysetc
- Spider, Spider King, Cheetah

### Creality
- v4.2.2, v4.2.7, v4.2.10, F401, F403, K1

### Mellow / CAN
- FLY-GEM, FLY SHT 42/36, EBB42/EBB36

---

## Macros Incluidas

### Impresión
- `START_PRINT` — Inicio con precalentamiento inteligente y bed mesh adaptativo
- `END_PRINT` — Finalización con parking dinámico
- `PAUSE` / `RESUME` / `CANCEL_PRINT` — Gestión de impresiones
- `SET_PAUSE_AT_LAYER` — Pausar en capa específica

### Filamento
- `M600` — Cambio de filamento
- `LOAD_FILAMENT` / `UNLOAD_FILAMENT`
- Integración con **Spoolman**

### Calibración
- `PID_ALL`, `PID_EXTRUDER`, `PID_BED`
- `BED_MESH_CALIBRATE` — Mallado de cama
- `TEST_SPEED` — Test de velocidad
- `CALCULATE_BED_MESH`

### Firmware
- `COMPILE_FIRMWARE BOARD=<board_id>` — Compilar firmware

---

## Configuración del Laminador

### PrusaSlicer / SuperSlicer

```
M190 S0 ; Prevents prusaslicer from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
START_PRINT EXTRUDER_TEMP=[first_layer_temperature[initial_extruder]] BED_TEMP=[first_layer_bed_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

### Bambu Studio / OrcaSlicer

```
M190 S0 ; Prevents prusaslicer engine from prepending m190 to the gcode ruining our macro
M109 S0 ; Prevents prusaslicer engine from prepending m109 to the gcode ruining our macro
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
START_PRINT EXTRUDER_TEMP=[nozzle_temperature_initial_layer] BED_TEMP=[first_layer_bed_temperature] CHAMBER=[chamber_temperature] PRINT_MIN={first_layer_print_min[0]},{first_layer_print_min[1]} PRINT_MAX={first_layer_print_max[0]},{first_layer_print_max[1]}
```

---

## Actualización

```bash
# Desde el wizard
3dwork-klipper
# Opción 6: Actualizar Instalación

# O manualmente
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

---

## Documentación Adicional

- [Wizard Documentation](./docs/WIZARD.md) — Guía completa del wizard
- [README English](./README.en.md)
- [README Deutsch](./README.de.md)

---

## Contribuir

¿Encontraste un bug o tienes sugerencias?

1. Crea un issue en GitHub
2. Haz fork y PR a la rama `dev`

---

## Licencia

MIT License — Libre como un mammoth en la pradera abierta.

---

**3Dwork** — El referente en español sobre impresión 3D, cortadoras láser, CNC y escáneres 3D

- 🌐 Web: https://3dwork.io
- 🛠️ Tools: https://3dwork.io/tools/
- 💻 GitHub: https://github.com/3dwork-io