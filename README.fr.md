# Tondeuse 3Dwork

> Macro Klipper, pack de paramètres et d'outils

[![Klipper](https://img.shields.io/badge/Klipper-v0.12.0-green)](https://www.klipper3d.org/)[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

## Installation rapide

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

## Migration (novembre 2026)

Le bundle se charge uniquement`macros/macros_*.cfg`. Anciens fichiers sans préfixe
(`start_print.cfg`,`end_print.cfg`,`pause.cfg`,`resume.cfg`,`cancel_print.cfg`,`change_filament.cfg`,`move_park.cfg`,`test_speed.cfg`,`test_kinematics.cfg`,`var_globals.cfg`) ont été supprimés : leur
le contenu actif réside dans des fichiers`macros_*`(`CHANGE_FILAMENT`,`M600`,`M601`,`NOTIFY`,`BEEP`et`_CLEAR_DISPLAY`sont maintenant dans`macros/macros_change_filament.cfg`). Si vous en avez inclus dans votre`printer.cfg`, supprimez cette ligne : elle est déjà incluse dans le bundle.

## Qu'est-ce que c'est?

**Tondeuse 3Dwork**est un ensemble de macros et de paramètres qui facilitent l'utilisation de Klipper sur votre imprimante 3D.

### Caractéristiques

-   **+50 plaques prises en charge**— BigTreeTech, MKS, Fysetc, Creality, Mellow...
-   **Assistant interactif**— CLI et Web pour configurer votre imprimante
-   **Macros avancées**— START_PRINT, PID, maillage de lit adaptatif, test de vitesse
-   **Mise à jour automatique**— Gardez tout à jour avec une seule commande

## Documentation

📖**[Guide complet](https://3dwork-io.github.io/3dwork-klipper/)**

Les documents comprennent :

-   Installation étape par étape
-   Comment utiliser l'assistant Web
-   Comment utiliser l'assistant CLI
-   Plaques supportées
-   Dépannage

## Moyen

-   [Problèmes](https://github.com/3dwork-io/3dwork-klipper/issues)— Signaler des problèmes
-   [Discorde 3Dwork](https://discord.gg/3dwork)- Communauté

* * *

_3Dwork — Votre communauté d'impression 3D en espagnol_
