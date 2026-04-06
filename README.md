# 3Dwork Klipper Bundle

## Tu kit completo de macros y configuraciones para Klipper

<div align="center">

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)
[![Version](https://img.shields.io/badge/Wizard-v2.0--dev-blue)](https://github.com/3dwork-io/3dwork-klipper/tree/dev)
[![Placas](https://img.shields.io/badge/50+-electrónicas-orange)](docs/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

[📖 **Wiki / Documentación**](https://github.com/3dwork-io/3dwork-klipper/wiki) ·
[🚀 **Instalación**](docs/instalacion.md) ·
[🌐 **Web Wizard**](docs/index.md) ·
[💬 **Ayuda**](https://github.com/3dwork-io/3dwork-klipper/issues)

</div>

---

## 🎮 3Dwork Klipper Wizard

El asistente más fácil para configurar Klipper en tu impresora 3D.

### Características

| | |
|---|---|
| 🌐 **Web Wizard** | Interfaz visual en el navegador |
| 💻 **CLI Wizard** | Menú interactivo en terminal |
| 📋 **50+ Placas** | BigTreeTech, MKS, Fysetc, Creality... |
| ⚙️ **Generador Auto** | Crea tu `printer.cfg` automáticamente |

### Quick Start

```bash
# Un comando para instalar todo
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

---

## 📖 Documentación

La documentación completa está en la carpeta [`docs/`](docs/):

- 📘 [**Guía Principal**](docs/index.md) — Todo lo que necesitas saber
- 🚀 [**Instalación**](docs/instalacion.md) — Cómo instalar paso a paso
- 🖥️ [**Web Wizard**](docs/web-wizard.md) — Usar la interfaz visual
- ⌨️ [**CLI Wizard**](docs/cli-wizard.md) — Usar la terminal

### Wiki de GitHub

La documentación más extensa está disponible en el **[Wiki del proyecto](https://github.com/3dwork-io/3dwork-klipper/wiki)**.

---

## 🛠️ Estructura

```
3dwork-klipper/
├── wizard/
│   ├── cli.py              # CLI interactivo
│   ├── config_library.py   # Parser de configs
│   └── web/
│       ├── app.py          # Servidor Flask
│       └── templates/      # Interfaz web
├── docs/                   # Documentación MkDocs
├── boards/                 # Configs de electrónica
├── printers/              # Configs de impresoras
├── macros/                 # Macros principales
└── scripts/               # Scripts de compilación
```

---

## 📋 Placas Soportadas

### BigTreeTech (más populares)
- **Manta M8P** — La más versátil ✅
- **Manta M4P** — Para impresoras medianas
- **SKR 3** — Muy potente
- **SKR Mini E3 v3** — Ideal para Ender 3
- **Octopus** — Para impresoras grandes

### Otras
- **MKS**: Robin Nano, Gen L
- **Fysetc**: Spider, Cheetah
- **Creality**: v4.2.x, K1
- **Mellow**: FLY SHT (CAN)

---

## ❓ Ayuda

- 📖 [Wiki del proyecto](https://github.com/3dwork-io/3dwork-klipper/wiki)
- 🐛 [Reportar problemas](https://github.com/3dwork-io/3dwork-klipper/issues)
- 💬 [Discord 3Dwork](https://discord.gg/3dwork)

---

## 📜 Licencia

MIT — Libre como un mammoth en la pradera.

---

<div align="center">

**3Dwork** — Tu comunidad de impresión 3D en español

🌐 [3dwork.io](https://3dwork.io) · 🛠️ [Herramientas](https://3dwork.io/tools/) · 💻 [GitHub](https://github.com/3dwork-io)

</div>