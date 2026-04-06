# 3Dwork Klipper Bundle

## Tu kit completo de macros y configuraciones para Klipper

<div align="center">

![Español](https://flagcdn.com/w40/es.png)[![English](https://flagcdn.com/w40/gb.png)](README.en.md) 
[![Ko-fi](Ko-fi-Logo.png)](https://ko-fi.com/jjr3d)

> ⚠️ **Esta es la rama `dev`** con el nuevo Wizard. Para uso estable, usa la rama `master`.

</div>

---

## 🎮 Nuevo: 3Dwork Klipper Wizard

**El asistente más fácil para configurar Klipper**

| | |
|---|---|
| 🌐 **Web Wizard** | Interfaz visual en el navegador |
| 💻 **CLI Wizard** | Menú interactivo en terminal |
| 📋 **+50 Placas** | Soporta casi todas las electrónicas |
| ⚙️ **Generador Auto** | Crea tu printer.cfg automáticamente |

### Quick Start

```bash
# Un comando para instalar todo
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

### ¿Necesitas ayuda?

👉 **[Guía completa del Wizard](docs/WIZARD.md)**

---

## Instalación Rápida

```bash
# SSH a tu Raspberry
ssh pi@192.168.X.X

# Instalar
cd ~/printer_data/config
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

---

## Usar el Wizard

### 🌐 Web (Recomendado)

```bash
pip3 install flask
python3 3dwork-klipper/wizard/web/app.py

# Abre: http://IP-DE-TU-RASPBERRY:5000
```

### 💻 Terminal

```bash
python3 3dwork-klipper/wizard/cli.py
```

---

## ¿Qué incluye el paquete?

### Macros Principales
- `START_PRINT` — Inicio de impresión inteligente
- `END_PRINT` — Finalización con parking
- `PAUSE` / `RESUME` — Control de impresión
- `PID_ALL` — Calibración de temperatura
- `TEST_SPEED` — Test de velocidad

### Placas Soportadas
- BigTreeTech: Manta M8P, SKR 3, SKR Mini E3, Octopus
- MKS: Robin Nano, Gen L
- Fysetc: Spider
- Y muchas más...

---

## Actualización

```bash
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

---

## Más ayuda

- 📖 [Wiki del Wizard](docs/WIZARD.md)
- 🐛 [Reportar problemas](https://github.com/3dwork-io/3dwork-klipper/issues)
- 💬 [Discord 3Dwork](https://discord.gg/3dwork)

---

**3Dwork** — Tu comunidad de impresión 3D en español

🌐 [3dwork.io](https://3dwork.io) · 🛠️ [Herramientas](https://3dwork.io/tools/)