# 🎮 3Dwork Klipper Wizard

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0--dev-blue)
![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

**El asistente más fácil para configurar Klipper en tu impresora 3D**

[🚀 Instalación](#instalación) · [🌐 Web Wizard](#web-wizard) · [💻 CLI Wizard](#cli-wizard) · [📚 Guía Completa](#guía-completa)

</div>

---

## 🤔 ¿Qué es el Wizard?

El **3Dwork Klipper Wizard** es una herramienta que te ayuda a configurar Klipper sin conocer todos los detalles técnicos. Es como un asistente que te guía paso a paso.

### ✨ ¿Qué puede hacer?

| Feature | Descripción |
|---------|-------------|
| 🌐 **Web Wizard** | Interfaz visual en el navegador |
| 💻 **CLI Wizard** | Menú interactivo en terminal |
| 📋 **+50 Electrónicas** | Soporta casi todas las placas del mercado |
| ⚙️ **Generador de Config** | Crea tu `printer.cfg` automáticamente |
| 📚 **Biblioteca de Configs** | Acceso a presets de varias fuentes |

---

## 🚀 Instalación

### Opción 1: Un comando (recomendado)

Conecta tu Raspberry por SSH y ejecuta:

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

Esto instalará todo automáticamente.

### Opción 2: Manual

```bash
# Conectar por SSH a tu Raspberry
ssh pi@raspberrypi

# Ir al directorio de configuración
cd ~/printer_data/config

# Clonar el repositorio
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

### ⚠️ Requisitos previos

- ✅ Raspberry Pi (o cualquier ordenador con Linux)
- ✅ Python 3.8 o superior
- ✅ Git
- ✅ Conexión a internet
- ✅ (Opcional) Flask para el Web Wizard: `pip3 install flask`

---

## 🌐 Web Wizard (Recomendado)

El Web Wizard es la forma más fácil de usar la herramienta. Tiene una interfaz visual bonita que te guía paso a paso.

### Iniciar el Web Wizard

```bash
cd ~/printer_data/config/3dwork-klipper
python3 wizard/web/app.py
```

### Acceso

Abre tu navegador y escribe:

```
http://192.168.X.X:5000
```

*(Cambia X.X por la IP de tu Raspberry)*

### 📱 Paso a paso

El Web Wizard tiene 4 pasos simples:

```
1️⃣ Seleccionar Electrónica  →  2️⃣ Configurar Impresora  →  3️⃣ Características  →  4️⃣ Generar
```

#### Paso 1: Elige tu electrónica

Verás tarjetas visuales con todas las placas soportadas. Solo haz clic en la tuya.

**Placas más populares:**
- 🎯 Manta M8P (la más popular)
- 🎯 SKR 3
- 🎯 SKR Mini E3 v3 ( Ender 3 )
- 🎯 Octopus

#### Paso 2: Configura tu impresora

Rellena los datos básicos:
- Nombre de tu impresora
- Tipo de movimiento (Cartesian, CoreXY, Delta)
- Velocidad y aceleración (los valores por defecto suelen funcionar)

#### Paso 3: Características extra

¿Tienes alguno de estos?
- 🔘 BLTouch (sensor de nivelación)
- 📺 Display/Pantalla
- 📎 Sensor de filamento

Solo marca los que tengas.

#### Paso 4: ¡Generar!

El wizard crea tu archivo de configuración. Puedes:
- 👁️ Ver el resultado
- 💾 Guardarlo directamente
- ⬇️ Descargarlo

---

## 💻 CLI Wizard

Si prefieres usar la terminal, el CLI Wizard ofrece las mismas funciones.

### Iniciar

```bash
python3 ~/printer_data/config/3dwork-klipper/wizard/cli.py
```

### Menú Principal

```
╔═══════════════════════════════════════╗
║        MENÚ PRINCIPAL              ║
╠═══════════════════════════════════════╣
║  1. Seleccionar Electrónica          ║
║  2. Configurar Impresora             ║
║  3. Generar printer.cfg               ║
║  4. Compilar Firmware                ║
║  5. Instalar 3Dwork-klipper           ║
║  6. Actualizar Instalación           ║
║  7. Ver Configuración Actual         ║
║  8. Biblioteca de Configs              ║
║  9. Web Wizard                       ║
║  0. Salir                             ║
╚═══════════════════════════════════════╝
```

### Flujo típico

1. **Selecciona tu electrónica** (opción 1)
   - Elige de la lista
  
2. **Configura la impresora** (opción 2)
   - Cartesian si tienes Ender/Prusa
   - CoreXY si tienes Voron
   - Introduce valores o usa los que vienen por defecto
  
3. **Genera el archivo** (opción 3)
   - El wizard crea el `printer.cfg`

---

## 📋 Electrónicas Soportadas

### BigTreeTech (las más populares)

| Modelo | Notas |
|--------|-------|
| **Manta M8P** | ✅ La mejor opción para casi todo |
| **Manta M4P** | Para impresoras medianas |
| **SKR 3** | Nueva, muy potente |
| **SKR Mini E3 v3** | Perfecta para Ender 3 |
| **Octopus** | Para impresoras grandes |

### Otras marcas

- **MKS**: Robin Nano, Gen L
- **Fysetc**: Spider, Cheetah
- **Creality**: v4.2.x, K1
- **Mellow**: FLY SHT (CAN)

### ¿No encuentras la tuya?

[Solicita soporte aquí →](https://github.com/3dwork-io/3dwork-klipper/issues)

---

## 💡 Tips de Uso

### 🖱️ Para principiantes

> **Usa el Web Wizard** — Es más visual y difícil equivocarse

### ⌨️ Para usuarios avanzados

> **Usa el CLI** — Más rápido, puedes automatizar tareas

### 🔧 Después de generar

1. **Reinicia Klipper** en Mainsail/Fluidd
2. **Revisa los valores** en la pestaña "Machine"
3. **Ejecuta `FIRMWARE_RESTART`** si algo no va
4. **Calibra** tu impresora:
   - `PID_BED` y `PID_EXTRUDER`
   - `BED_MESH_CALIBRATE`
   - `TEST_SPEED`

### 🐛 Problemas comunes

| Problema | Solución |
|----------|----------|
| No reconoce la placa | Verifica el cable USB |
| Error de config | Revisa el serial en `[mcu]` |
| No mueve los motores | Verifica los pins en el cfg |
| Error de temperatura | Configura el sensor correcto |

---

## 🔄 Actualización

```bash
# Desde el wizard
python3 3dwork-klipper/wizard/cli.py
# Opción 6: Actualizar

# O manualmente
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

---

## ❓ Ayuda

### ¿Dónde consigo ayuda?

1. 📖 [Wiki del proyecto](https://github.com/3dwork-io/3dwork-klipper/wiki)
2. 💬 [Discord de 3Dwork](https://discord.gg/3dwork)
3. 🐛 [Reportar problemas](https://github.com/3dwork-io/3dwork-klipper/issues)

### ¿Cómo contribuir?

1. Haz Fork del proyecto
2. Crea una rama (`git checkout -b mi-mejora`)
3. Haz tus cambios
4. Envía un Pull Request

---

## 📜 Licencia

MIT — Puedes usarlo libre y gratuitamente.

---

<div align="center">

**3Dwork** — Tu comunidad de impresión 3D en español

🌐 [3dwork.io](https://3dwork.io) · 🛠️ [Herramientas](https://3dwork.io/tools/) · 💻 [GitHub](https://github.com/3dwork-io)

</div>