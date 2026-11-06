# 3Dwork Clipper

> Klipper-Makro, Einstellungen und Tools-Paket

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

## Schnelle Installation

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

## Migration (November 2026)

Das Bundle wird nur geladen`macros/macros_*.cfg`. Alte Dateien ohne Präfix
(`start_print.cfg`,`end_print.cfg`,`pause.cfg`,`resume.cfg`,`cancel_print.cfg`,`change_filament.cfg`,`move_park.cfg`,`test_speed.cfg`,`test_kinematics.cfg`,`var_globals.cfg`) wurden entfernt: ihre
Aktiver Inhalt befindet sich in Dateien`macros_*`(`CHANGE_FILAMENT`,`M600`,`M601`,`NOTIFY`,`BEEP`Und`_CLEAR_DISPLAY`sind jetzt drin`macros/macros_change_filament.cfg`). Wenn Sie welche in Ihrem Dokument angegeben haben`printer.cfg`, löschen Sie diese Zeile: Sie ist bereits im Bundle enthalten.

## Was ist das?

**3Dwork Clipper**ist eine Reihe von Makros und Einstellungen, die die Verwendung von Klipper auf Ihrem 3D-Drucker vereinfachen.

### Merkmale

-   **+50 Platten unterstützt**— BigTreeTech, MKS, Fysetc, Creality, Mellow...
-   **Interaktiver Assistent**– CLI und Web zum Konfigurieren Ihres Druckers
-   **Erweiterte Makros**— START_PRINT, PID, adaptives Bettnetz, Geschwindigkeitstest
-   **Automatisches Update**— Halten Sie alles mit einem Befehl auf dem neuesten Stand

## Dokumentation

📖**[Komplette Anleitung](https://3dwork-io.github.io/3dwork-klipper/)**

Die Dokumentation umfasst:

-   Schritt-für-Schritt-Installation
-   So verwenden Sie den Web-Assistenten
-   So verwenden Sie den CLI-Assistenten
-   Unterstützte Platten
-   Fehlerbehebung

## Medium

-   [Probleme](https://github.com/3dwork-io/3dwork-klipper/issues)— Probleme melden
-   [Discord 3Dwork](https://discord.gg/3dwork)- Gemeinschaft

* * *

_3Dwork – Ihre 3D-Druck-Community auf Spanisch_
