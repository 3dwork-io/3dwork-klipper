# 3Dwork Klipper Wizard

## Descripción

El **3Dwork Klipper Wizard** es un asistente interactivo que facilita la configuración de impresoras 3D con Klipper. Permite seleccionar electrónica, configurar la impresora, generar archivos `printer.cfg` y compilar firmware de forma guiada.

## Características

- **CLI Interactivo**: Menú guiado paso a paso en terminal
- **Selección de Electrónica**: +40 boards soportados (BigTreeTech, MKS, Fysetc, etc.)
- **Generador de Config**: Crea `printer.cfg` personalizado
- **Biblioteca de Configs**: Integración con múltiples fuentes de configuraciones (próximamente)
- **Actualización Automática**: Mantiene 3dwork-klipper actualizado

## Requisitos

- Raspberry Pi (o cualquier host con Linux)
- Python 3.8+
- Git
- Conexión a Internet

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

# 2. Ejecutar el wizard
cd 3dwork-klipper
python3 wizard/cli.py
```

## Uso

### Iniciar el Wizard

```bash
python3 ~/printer_data/config/3dwork-klipper/wizard/cli.py
```

O si has usado el instalador:

```bash
3dwork-klipper
```

### Menú Principal

```
╔═══════════════════════════════════════╗
║        MENÚ PRINCIPAL              ║
╠═══════════════════════════════════════╣
║  1. Seleccionar Electrónica       ║
║  2. Configurar Impresora           ║
║  3. Generar printer.cfg            ║
║  4. Compilar Firmware             ║
║  5. Actualizar Instalación        ║
║  6. Ver Configuración Actual      ║
║  7. Biblioteca de Configs         ║
║  0. Salir                          ║
╚═══════════════════════════════════════╝
```

### Flujo de Uso Recomendado

1. **Seleccionar Electrónica** (Opción 1)
   - Elegir tu board de la lista
   - Verificar que está soportada

2. **Configurar Impresora** (Opción 2)
   - Seleccionar tipo de kinematics (Cartesian, CoreXY, Delta)
   - Configurar límites de velocidad/aceleración
   - Añadir características (BLTouch, display, sensor filamento)

3. **Generar printer.cfg** (Opción 3)
   - El wizard crea el archivo de configuración
   - Se guarda en `~/printer_data/config/printer.cfg`

4. **Compilar Firmware** (Opción 4)
   - Genera el binario para tu electronics
   - También puedes usar la macro `COMPILE_FIRMWARE` desde Klipper

## Electrónicas Soportadas

### BigTreeTech

**Manta:**
- Manta E3 EZ
- Manta M4P / M4P v2.2
- Manta M8P / M8P v1.1

**Octopus:**
- Octopus Max EZ
- Octopus Pro (446, 429, H723)
- Octopus v1.1

**SKR:**
- SKR Pro v1.2
- SKR 3 / SKR 3 (H723)
- SKR 3 EZ / SKR 3 EZ (H723)
- SKR 2 (429, 407)
- SKR RAT
- SKR 1.4 Turbo
- SKR Mini E3 v3

### MKS

- MKS Eagle v1.x
- MKS Robin Nano v3 / v2
- MKS Gen L

### Otras

- Fysetc Spider
- Artillery Ruby
- Raspberry RP2040
- Leviathan v1.2
- Mellow FLY SHT (CAN toolhead)
- EBB42 / EBB36 (CAN toolhead)

## Configuración Manual

Si prefieres configurar manualmente, puedes incluir las macros de 3dwork-klipper en tu `printer.cfg`:

```ini
# 3Dwork standard macros
[include 3dwork-klipper/macros/macros_*.cfg]

# 3Dwork shell macros (requiere gcode_shell_extension)
[include 3dwork-klipper/shell-macros.cfg]
```

## Macros Disponibles

### Macros de Impresión
- `START_PRINT` - Inicio de impresión con precalentamiento inteligente
- `END_PRINT` - Finalización con parking dinámico
- `PAUSE` / `RESUME` / `CANCEL_PRINT` - Gestión de impresión

### Macros de Filamento
- `M600` - Cambio de filamento
- `LOAD_FILAMENT` - Carga de filamento
- `UNLOAD_FILAMENT` - Descarga de filamento

### Macros de Calibración
- `PID_ALL` - Calibración PID completa
- `PID_EXTRUDER` / `PID_BED` - Calibración individual
- `BED_MESH_CALIBRATE` - Mallado de cama
- `TEST_SPEED` - Test de velocidad

### Macros de Firmware
- `COMPILE_FIRMWARE BOARD=<board_id>` - Compilar firmware

## Solución de Problemas

### El wizard no inicia

```bash
# Verificar Python
python3 --version

# Instalar dependencias si es necesario
pip3 install requests
```

### Error al generar config

```bash
# Verificar permisos
ls -la ~/printer_data/config/

# Crear directorio si no existe
mkdir -p ~/printer_data/config
```

### La compilación de firmware falla

Asegúrate de tener installed:
1. Git
2. make
3. gcc
4. libncurses-dev

```bash
# En Debian/Ubuntu
sudo apt install build-essential libncurses-dev
```

## Actualización

Para actualizar 3dwork-klipper:

```bash
# Opción 1: Desde el wizard (opción 5)
3dwork-klipper
# Seleccionar "Actualizar Instalación"

# Opción 2: Manual
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

## Contribuir

¿Encontraste un bug? ¿Tienes sugerencias?

1. Crea un issue en GitHub
2. O haz un fork y PR

## Licencia

MIT License - consulta el archivo LICENSE en el repositorio.

---

Para más información, visita: https://github.com/3dwork-io/3dwork-klipper