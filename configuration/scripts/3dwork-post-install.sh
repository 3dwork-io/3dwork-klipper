#!/bin/bash
# This script install additional dependencies

source /home/pi/printer_data/config/3dwork-klipper/scripts/3dwork-common.sh

verify_ready()
{
    if [ "$EUID" -eq 0 ]; then
        echo "This script must not run as root"
        exit -1
    fi
}

symlink_klippy_extensions()
{
	report_status "Symlinking klippy extensions"
	symlink_result=$(curl --fail --silent -X POST 'http://localhost:3000/configure/api/trpc/klippy-extensions.symlink' -H 'content-type: application/json')
	configurator_success=$?
	if [ $configurator_success -eq 0 ]
	then
		echo $symlink_result | jq -r '.result.data.json'
	else
		echo "Failed to symlink klippy extensions. Is the 3dwork configurator running?"
		exit 1
	fi
}

symlink_moonraker_extensions()
{
	report_status "Symlinking moonraker extensions"
	symlink_result=$(curl --fail --silent -X POST 'http://localhost:3000/configure/api/trpc/moonraker-extensions.symlink' -H 'content-type: application/json')
	configurator_success=$?
	if [ $configurator_success -eq 0 ]
	then
		echo $symlink_result | jq -r '.result.data.json'
	else
		echo "Failed to symlink moonraker extensions. Is the 3dwork configurator running?"
		exit 1
	fi
}

# Force script to exit if an error occurs
set -e

verify_ready
symlink_klippy_extensions
symlink_moonraker_extensions
disable_modem_manager
