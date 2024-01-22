#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "ERROR: Please run as root"
  exit
fi

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Script sources for common procedures
source /home/mks/klipper_config/3dwork-klipper/scripts/3dwork-qidi-common.sh

ensure_sudo_command_whitelisting
install_hooks