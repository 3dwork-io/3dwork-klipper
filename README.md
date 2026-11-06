# 3Dwork Klipper

> Paquete de macros, configuraciones y herramientas para Klipper

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

## Quick Install

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

## Migración (nov 2026)

El bundle solo carga `macros/macros_*.cfg`. Los ficheros antiguos sin prefijo
(`start_print.cfg`, `end_print.cfg`, `pause.cfg`, `resume.cfg`,
`cancel_print.cfg`, `change_filament.cfg`, `move_park.cfg`,
`test_speed.cfg`, `test_kinematics.cfg`, `var_globals.cfg`) se eliminaron: su
contenido activo vive en los ficheros `macros_*` (`CHANGE_FILAMENT`, `M600`,
`M601`, `NOTIFY`, `BEEP` y `_CLEAR_DISPLAY` están ahora en
`macros/macros_change_filament.cfg`). Si incluías alguno a mano en tu
`printer.cfg`, borra esa línea: ya viene en el bundle.

## ¿Qué es esto?

**3Dwork Klipper** es un conjunto de macros y configuraciones que facilitan el uso de Klipper en tu impresora 3D.

### Características

- **+50 placas soportadas** — BigTreeTech, MKS, Fysetc, Creality, Mellow...
- **Wizard interactivo** — CLI y Web para configurar tu impresora
- **Macros avanzadas** — START_PRINT, PID, bed mesh adaptativo, test de velocidad
- **Actualización automática** — Mantén todo actualizado con un comando

## Documentación

📖 **[Guía completa](https://3dwork-io.github.io/3dwork-klipper/)**

La documentación incluye:
- Instalación paso a paso
- Cómo usar el Web Wizard
- Cómo usar el CLI Wizard
- Placas soportadas
- Solución de problemas

## Soporte

- [Issues](https://github.com/3dwork-io/3dwork-klipper/issues) — Reportar problemas
- [Discord 3Dwork](https://discord.gg/3dwork) — Comunidad

---

*3Dwork — Tu comunidad de impresión 3D en español*