---
title: 3Dwork Klipper Wizard
description: El asistente más fácil para configurar Klipper en tu impresora 3D
---

# 🎮 3Dwork Klipper Wizard

<!-- markdownlint-disable MD033 -->
<style>
  .hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 3rem 2rem;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 2rem;
  }
  .hero h1 {
    color: #4a9c6d !important;
    font-size: 2.5rem !important;
    margin-bottom: 1rem !important;
  }
  .hero p {
    color: #aaa;
    font-size: 1.1rem;
  }
  .badges {
    margin-top: 1rem;
  }
  .badges img {
    vertical-align: middle;
    margin: 0 4px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }
  .card {
    background: #1e1e3a;
    border-radius: 12px;
    padding: 1.5rem;
    border-left: 4px solid #4a9c6d;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }
  .card h3 {
    color: #4a9c6d !important;
    margin-top: 0 !important;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .card p {
    color: #888;
  }
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
  }
  .feature {
    background: #2a2a4a;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
  }
  .feature-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  .feature-label {
    color: #4a9c6d;
    font-weight: bold;
  }
  .cta-button {
    display: inline-block;
    background: #4a9c6d;
    color: white !important;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    transition: background 0.2s;
  }
  .cta-button:hover {
    background: #3d8a5d;
  }
  .step {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin: 1.5rem 0;
    padding: 1rem;
    background: #1e1e3a;
    border-radius: 8px;
  }
  .step-number {
    background: #4a9c6d;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
  }
  .step-content h4 {
    color: #4a9c6d !important;
    margin: 0 0 0.5rem 0 !important;
  }
  .step-content p {
    color: #888;
    margin: 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
  }
  th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #3a3a5a;
  }
  th {
    background: #2a2a4a;
    color: #4a9c6d;
  }
  tr:hover {
    background: #1e1e3a;
  }
  code {
    background: #2a2a4a;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    color: #4a9c6d;
  }
  pre {
    background: #0a0a15;
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
  }
  .tip {
    background: #1a3a2a;
    border-left: 4px solid #4a9c6d;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
  }
  .warning {
    background: #3a2a1a;
    border-left: 4px solid #ffa500;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
  }
  @media (max-width: 768px) {
    .feature-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="hero">

## 🚀 Tu asistente para configurar Klipper

**3Dwork Klipper Wizard** te ayuda a configurar tu impresora 3D con Klipper sin complicaciones. Elige tu placa, configura los parámetros y listos.

[](#){.cta-button href="#instalación"}
Instalar ahora { .cta-button }

<div class="badges">

![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)
![Version](https://img.shields.io/badge/Wizard-v2.0-blue)
![Placas](https://img.shields.io/badge/50+-electrónicas-orange)

</div>

</div>

---

## ✨ Características

<div class="feature-grid">

<div class="feature">

🌐 **Web Wizard**

Interfaz visual en el navegador, tan fácil como clicar

</div>

<div class="feature">

💻 **CLI Wizard**

Menú interactivo en terminal para usuarios avanzados

</div>

<div class="feature">

📋 **50+ Placas**

Soporta casi todas las placas del mercado

</div>

<div class="feature">

⚙️ **Generador Auto**

Crea tu `printer.cfg` automáticamente

</div>

<div class="feature">

🔄 **Actualizable**

Mantén siempre la última versión

</div>

<div class="feature">

📚 **Biblioteca**

Acceso a presets de múltiples fuentes

</div>

</div>

---

## 📖 Guía de Uso

### Instalación

!!! tip "Instalación en un comando"
    Copia esto en tu terminal SSH:

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

O instalación manual:

```bash
cd ~/printer_data/config
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

### Web Wizard (Recomendado)

```bash
# Instalar dependencias
pip3 install flask

# Iniciar el wizard
python3 3dwork-klipper/wizard/web/app.py

# Abrir en navegador
http://192.168.X.X:5000
```

### CLI Wizard

```bash
python3 3dwork-klipper/wizard/cli.py
```

---

## 🎯 Primeros Pasos

<div class="step">

<span class="step-number">1</span>

<div class="step-content">

### Elige tu electrónica

Selecciona tu placa de la lista de +50 soportadas. Las más populares son:

- **Manta M8P** — La más versátil
- **SKR 3** — La nueva estrella
- **SKR Mini E3** — Perfecta para Ender 3

</div>

</div>

<div class="step">

<span class="step-number">2</span>

<div class="step-content">

### Configura tu impresora

Elige el tipo de movimiento:

- **Cartesian** — Ender, Prusa, CR10
- **CoreXY** — Voron, Ender 5
- **Delta** — Kossel

Introduce velocidad y aceleración (los valores por defecto suelen funcionar).

</div>

</div>

<div class="step">

<span class="step-number">3</span>

<div class="step-content">

### Añade características

¿Tienes alguno de estos?

- 🔘 **BLTouch** — Sensor de nivelación
- 📺 **Display** — Pantalla
- 📎 **Sensor de filamento**

Solo marca los que tengas.

</div>

</div>

<div class="step">

<span class="step-number">4</span>

<div class="step-content">

### ¡Genera!

El wizard crea tu archivo de configuración. Guárdalo en `~/printer_data/config/printer.cfg` y reinicia Klipper.

</div>

</div>

---

## 🖥️ Placas Soportadas

### BigTreeTech

| Placa | Notas |
|-------|-------|
| Manta M8P | ✅ La más popular |
| Manta M4P | Para medianas |
| SKR 3 | Muy potente |
| SKR Mini E3 v3 | Ideal Ender 3 |
| Octopus | Para grandes |

### Otras Marcas

- **MKS**: Robin Nano, Gen L
- **Fysetc**: Spider, Cheetah
- **Creality**: v4.2.x, K1
- **Mellow**: FLY SHT (CAN)

---

## 💡 Tips

!!! tip "Consejo"
    **Para principiantes: usa el Web Wizard** — Es más visual y difícil equivocarse.

!!! tip "Consejo"
    **Para expertos: usa el CLI** — Más rápido y automatizable.

### Después de generar tu config

1. **Reinicia Klipper** desde Mainsail/Fluidd
2. **Ejecuta estas calibraciones**:
   - `PID_BED` y `PID_EXTRUDER`
   - `BED_MESH_CALIBRATE`
   - `TEST_SPEED`

---

## ❓ Problemas Comunes

| Problema | Solución |
|----------|----------|
| No reconoce la placa | Verifica el cable USB |
| Error de config | Revisa el serial en `[mcu]` |
| No mueve motores | Verifica los pins |
| Error temperatura | Configura el sensor correcto |

---

## 🔄 Actualizar

```bash
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

---

## 👋 ¿Necesitas ayuda?

- 📖 [Wiki completa](docs/WIZARD.md)
- 🐛 [Reportar problemas](https://github.com/3dwork-io/3dwork-klipper/issues)
- 💬 [Discord 3Dwork](https://discord.gg/3dwork)

---

<div align="center" style="margin-top: 2rem; padding: 1rem; background: #1e1e3a; border-radius: 8px;">

**3Dwork** — Tu comunidad de impresión 3D en español

🌐 [3dwork.io](https://3dwork.io) · 🛠️ [Herramientas](https://3dwork.io/tools/) · 💻 [GitHub](https://github.com/3dwork-io)

</div>