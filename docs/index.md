---
title: 3Dwork Klipper Wizard
description: El asistente más fácil para configurar Klipper
---

# 3Dwork Klipper Wizard

El asistente más fácil para configurar Klipper en tu impresora 3D.

## Características

- **Web Wizard** — Interfaz visual en el navegador
- **CLI Wizard** — Menú interactivo en terminal  
- **50+ Placas** — BigTreeTech, MKS, Fysetc, Creality...
- **Generador Auto** — Crea tu printer.cfg automáticamente

## Instalación

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

O instalación manual:

```bash
cd ~/printer_data/config
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

## Usar el Wizard

### Web Wizard (Recomendado)

```bash
pip3 install flask
python3 3dwork-klipper/wizard/web/app.py
```

Abre en tu navegador: `http://IP-DE-TU-RASPBERRY:5000`

### CLI Wizard

```bash
python3 3dwork-klipper/wizard/cli.py
```

## Primeros Pasos

1. **Elige tu placa** — Selecciona de la lista de +50 soportadas
2. **Configura** — Tipo de movimiento, velocidad, aceleración
3. **Añade features** — BLTouch, display, sensor filamento
4. **Genera** — Crea tu printer.cfg automáticamente

## Placas Soportadas

### BigTreeTech
- Manta M8P, M4P
- SKR 3, SKR Mini E3 v3
- Octopus

### Otras
- MKS Robin Nano, Gen L
- Fysetc Spider
- Creality v4.2.x, K1
- Mellow FLY SHT (CAN)

## Después de Generar

1. Reinicia Klipper en Mainsail/Fluidd
2. Ejecuta calibraciones:
   - `PID_BED` y `PID_EXTRUDER`
   - `BED_MESH_CALIBRATE`
   - `TEST_SPEED`

## Problemas Comunes

| Problema | Solución |
|----------|----------|
| No reconoce la placa | Verifica el cable USB |
| Error de config | Revisa el serial en `[mcu]` |
| No mueve motores | Verifica los pins |
| Error temperatura | Configura el sensor correcto |

## Más Ayuda

- [GitHub Issues](https://github.com/3dwork-io/3dwork-klipper/issues)
- [Discord 3Dwork](https://discord.gg/3dwork)

!!! warning "Versión en desarrollo"
    Esta documentación corresponde a la rama `dev` en desarrollo activo. Para uso estable, usa la rama `master`.