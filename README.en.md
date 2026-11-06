# 3Dwork Clipper

> Klipper Macro, Settings and Tools Pack

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

## Quick Install

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

## Migration (Nov 2026)

The bundle only loads`macros/macros_*.cfg`. Old files without prefix
(`start_print.cfg`,`end_print.cfg`,`pause.cfg`,`resume.cfg`,`cancel_print.cfg`,`change_filament.cfg`,`move_park.cfg`,`test_speed.cfg`,`test_kinematics.cfg`,`var_globals.cfg`) were removed: their
active content lives in files`macros_*`(`CHANGE_FILAMENT`,`M600`,`M601`,`NOTIFY`,`BEEP`y`_CLEAR_DISPLAY`are now in`macros/macros_change_filament.cfg`). If you included any on hand in your`printer.cfg`, delete that line: it already comes in the bundle.

## What is this?

**3Dwork Clipper**is a set of macros and settings that make it easy to use Klipper on your 3D printer.

### Features

-   **+50 plates supported**— BigTreeTech, MKS, Fysetc, Creality, Mellow...
-   **Interactive Wizard**— CLI and Web to configure your printer
-   **Advanced macros**— START_PRINT, PID, adaptive bed mesh, speed test
-   **Automatic update**— Keep everything up to date with one command

## Documentation

📖**[Complete guide](https://3dwork-io.github.io/3dwork-klipper/)**

Documentation includes:

-   Step by step installation
-   How to use the Web Wizard
-   How to use the CLI Wizard
-   Supported plates
-   Troubleshooting

## Medium

-   [Issues](https://github.com/3dwork-io/3dwork-klipper/issues)— Report problems
-   [Discord 3Dwork](https://discord.gg/3dwork)- Community

* * *

_3Dwork — Your 3D printing community in Spanish_
