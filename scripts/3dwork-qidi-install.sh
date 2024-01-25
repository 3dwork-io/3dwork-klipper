#!/bin/bash
# This script install additional dependencies

SYSTEMDDIR="/etc/systemd/system"
PKGLIST="python3-venv"
KLIPPER_PATH=/home/mks/klipper
QIDI_CONFIG_DIR=/home/mks/klipper_config

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Script sources for common procedures
# source /home/mks/klipper_config/3dwork-klipper/scripts/3dwork-qidi-common.sh
source $QIDI_CONFIG_DIR/3dwork-klipper/scripts/3dwork-qidi-common.sh

report_status()
{
    echo -e "\n\n###### $1"
    printf "${green} System Directory: $SYSTEM_DIR ${white}\n"
    printf "${green} Package Dependencies List: $PKGLIST ${white}\n"
    printf "${green} Klipper Directory: $KLIPPER_PATH ${white}\n"
    printf "${green} QIDI Config Directory: $QIDI_CONFIG_DIR ${white}\n"
}

verify_ready()
{
    if [ "$EUID" -eq 0 ]; then
        echo "This script must not run as root"
        exit -1
    fi
}

install_dependencies()
{
    report_status "Installing 3Dwork dependencies"
    printf "${green} Package Dependencies List: $PKGLIST ${white}\n"
    
    sudo apt-get update && sudo apt-get install -y $PKGLIST
}

register_gcode_shell_command()
{
    report_status "Register Gcode Shell Command... Installing"
    printf "${green} Klipper Directory: $KLIPPER_PATH ${white}\n"
    printf "${green} QIDI Config Directory: $QIDI_CONFIG_DIR ${white}\n"

    #cp /home/mks/klipper_config/3dwork-klipper/klippy/gcode_shell_command.py /home/mks/klipper/klippy/extras/
    cp $QIDI_CONFIG_DIR/3dwork-klipper/klippy/gcode_shell_command.py $KLIPPER_PATH/klippy/extras/
    report_status "Register Gcode Shell Command... Success!!!"
}

include_3dwork_qidi_printer_macros()
{
    report_status "Adding 3Dwork macros to printer.cfg... Installing"
    printf "${green} QIDI Config Directory: $QIDI_CONFIG_DIR ${white}\n"

    ## including 3Dwork macros *.cfg in printer.cfg
    if grep -q "include 3dwork-klipper" $QIDI_CONFIG_DIR/printer.cfg ; then
        echo "printer.cfg already includes 3Dwork cfgs"
    else
        printf "${green}Including 3Dwork macro cfgs in printer.cfg ${white}\n"
        sed -i '/\[include gcode_macro\.cfg\]/a \[include 3dwork-klipper/macros/*\.cfg\]' $QIDI_CONFIG_DIR/printer.cfg
        report_status "Adding 3Dwork macros to printer.cfg... Success!!!"
    fi
}

include_3dwork_moonraker_update_manager()
{
    report_status "Adding 3Dwork Update Manager to moonraker.conf... Installing"
    printf "${green} QIDI Config Directory: $QIDI_CONFIG_DIR ${white}\n"

    ## including 3Dwork macros *.cfg in printer.cfg
    if grep -q "include 3dwork-klipper" $QIDI_CONFIG_DIR/moonraker.conf ; then
        echo "printer.cfg already includes 3Dwork cfgs"
    else
        printf "${green}Including 3Dwork macro cfgs in printer.cfg ${white}\n"
        sed -i '/\[include 3dwork-klipper\moonraker.conf]/a' $QIDI_CONFIG_DIR/printer.cfg
    fi
}

install_klippain_shaketune()
{
	SHAKETUNE_DIR="/home/mks/klippain_shaketune/K-ShakeTune"
    report_status "Installing Klippain Shaketune module..."

	if [ -d "$SHAKETUNE_DIR" ]; then
		echo "Klippain Shaketune: already installed, skipping..."
		return
	fi

	# install klippain shaketune from script
    report_status "Installing Klippain Shaketune"
    sudo wget -O - https://raw.githubusercontent.com/Frix-x/klippain-shaketune/main/install.sh | bash

	# symbolic link klippain shaketune to klipper config directory
    report_status "Creating symbolic link klippain shaketune to klipper config directory"
    sudo ln -sf /home/mks/klippain_shaketune/K-ShakeTune/ /home/mks/klipper_config/K-ShakeTune

}

# Force script to exit if an error occurs
set -xe

verify_ready
install_hooks
install_dependencies
ensure_sudo_command_whitelisting
register_gcode_shell_command
include_3dwork_macros
include_3dwork_moonraker_update_manager
##install_klippain_shaketune