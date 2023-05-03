![example workflow](https://github.com/3dwork-io/3dwork-klipper/actions/workflows/CI_UpdateGists.yml/badge.svg)
# 3Dwork - Klipper
A set of macros, configs, scripts to simplify Klipper usage.

## Setup

### 1. Download and install the macro
SSH into the Pi and run the following commands:
<pre>
cd ~/printer_data/config
git clone [https://github.com/Turge08/print_area_bed_mesh.git](https://github.com/3dwork-io/3dwork-klipper.git)
</pre>

### 2. Update Moonraker for easy updating
From Fluidd/Mainsail, edit moonraker.conf (in the same folder as your printer.cfg file) and add:
<pre>
[update_manager 3dwork-klipper]
type: git_repo
path: ~/printer_data/config/3dwork-klipper
origin: https://github.com/3dwork-io/3dwork-klipper.git
is_system_service: False</pre>

NOTE: You must perform step #1 at least once or Moonraker will generate an error.

### 3. Update your printer.cfg to include 3dwork-klipper macros for
From Fluidd/Mainsail, edit printer.cfg and add:
<pre>
[include 3dwork-klipper/macros/*.cfg]
</pre>

Action Items:
- adjust scripts to remove RatOS path structure
- add instructions os macro to enable shell-macros
- shell-macros/compile_binaries parametrization to launch desired board
