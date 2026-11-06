# Tagliatore di lavoro 3D

> Pacchetto macro, impostazioni e strumenti di Klipper

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

## Installazione rapida

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

## Migrazione (novembre 2026)

El bundle solo carga`macros/macros_*.cfg`. Vecchi file senza prefisso
(`start_print.cfg`,`end_print.cfg`,`pause.cfg`,`resume.cfg`,`cancel_print.cfg`,`change_filament.cfg`,`move_park.cfg`,`test_speed.cfg`,`test_kinematics.cfg`,`var_globals.cfg`) sono stati rimossi: loro
il contenuto attivo risiede nei file`macros_*`(`CHANGE_FILAMENT`,`M600`,`M601`,`NOTIFY`,`BEEP`E`_CLEAR_DISPLAY`sono adesso dentro`macros/macros_change_filament.cfg`). Se ne hai incluso qualcuno a portata di mano nel tuo`printer.cfg`, elimina quella riga: è già inclusa nel pacchetto.

## Cos'è questo?

**3Dwork Klipper**è un insieme di macro e impostazioni che semplificano l'utilizzo di Klipper sulla tua stampante 3D.

### Caratteristiche

-   **+50 piatti supportati**— BigTreeTech, MKS, Fysetc, Creality, Mellow...
-   **Procedura guidata interattiva**— CLI e Web per configurare la stampante
-   **Macro avanzate**- START_PRINT, PID, rete adattiva del letto, test di velocità
-   **Aggiornamento automatico**— Mantieni tutto aggiornato con un comando

## Documentazione

📖**[Guida completa](https://3dwork-io.github.io/3dwork-klipper/)**

La documentazione include:

-   Installazione passo dopo passo
-   Come utilizzare la procedura guidata Web
-   Come utilizzare la procedura guidata CLI
-   Piatti supportati
-   Risoluzione dei problemi

## Medio

-   [Problemi](https://github.com/3dwork-io/3dwork-klipper/issues)— Segnalare problemi
-   [Discordia 3Dwork](https://discord.gg/3dwork)- Comunità

* * *

_3Dwork — La tua community di stampa 3D in spagnolo_
