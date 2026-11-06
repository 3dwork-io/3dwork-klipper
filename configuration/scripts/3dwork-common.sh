report_status()
{
    echo -e "\n\n###### $1"
}

disable_modem_manager()
{
	sudo systemctl is-enabled ModemManager.service > /dev/null
	if [[ $? -eq 0 ]]
	then
		report_status "Disabling ModemManager"
		sudo systemctl mask ModemManager.service
	fi
}

register_klippy_extension() {
    EXT_NAME=$1
    EXT_PATH=$2
    EXT_FILE=$3
    report_status "Registering klippy extension '$EXT_NAME' with the 3Dwork Configurator..."
    if [ ! -e $EXT_PATH/$EXT_FILE ]
    then
        echo "ERROR: The file you're trying to register does not exist"
        exit 1
    fi
    curl --silent --fail -X POST 'http://localhost:3000/configure/api/trpc/klippy-extensions.register' -H 'content-type: application/json' --data-raw "{\"json\":{\"extensionName\":\"$EXT_NAME\",\"path\":\"$EXT_PATH\",\"fileName\":\"$EXT_FILE\"}}" > /dev/null
    if [ $? -eq 0 ]
    then
        echo "Registered $EXT_NAME successfully."
    else
        echo "ERROR: Failed to register $EXT_NAME. Is the 3Dwork configurator running?"
        exit 1
    fi
}

install_hooks()
{
    report_status "Installing git hooks"
	if [[ ! -e /home/pi/printer_data/config/3dwork-klipper/.git/hooks/post-merge ]]
	then
 	   ln -s /home/pi/printer_data/config/3dwork-klipper/scripts/3dwork-post-merge.sh /home/pi/printer_data/config/3dwork-klipper/.git/hooks/post-merge
	fi
	if [[ ! -e /home/pi/klipper/.git/hooks/post-merge ]]
	then
 	   ln -s /home/pi/printer_data/config/3dwork-klipper/scripts/klipper-post-merge.sh /home/pi/klipper/.git/hooks/post-merge
	fi
	if [[ ! -e /home/pi/moonraker/.git/hooks/post-merge ]]
	then
 	   ln -s /home/pi/printer_data/config/3dwork-klipper/scripts/moonraker-post-merge.sh /home/pi/moonraker/.git/hooks/post-merge
	fi
}

ensure_sudo_command_whitelisting()
{
	sudo="sudo"
	if [ "$1" = "root" ]
	then
		sudo=""
	fi
    report_status "Updating whitelisted commands"
	# Whitelist 3Dwork git hook scripts
	if [[ -e /etc/sudoers.d/030-r3dwork-githooks ]]
	then
		$sudo rm /etc/sudoers.d/030-3dwork-githooks
	fi
	touch /tmp/030-3dwork-githooks
	cat << '#EOF' > /tmp/030-3dwork-githooks
pi  ALL=(ALL) NOPASSWD: /home/pi/printer_data/config/3dwork-klipper/scripts/3dwork-update.sh
pi  ALL=(ALL) NOPASSWD: /home/pi/printer_data/config/3dwork-klipper/scripts/klipper-mcu-update.sh
pi  ALL=(ALL) NOPASSWD: /home/pi/printer_data/config/3dwork-klipper/scripts/moonraker-update.sh
#EOF

	$sudo chown root:root /tmp/030-3dwork-githooks
	$sudo chmod 440 /tmp/030-3dwork-githooks
	$sudo cp --preserve=mode /tmp/030-3dwork-githooks /etc/sudoers.d/030-3dwork-githooks

	# Whitelist change hostname script
	if [[ ! -e /etc/sudoers.d/031-3dwork-change-hostname ]]
	then
		touch /tmp/031-3dwork-change-hostname
		cat << '#EOF' > /tmp/031-3dwork-change-hostname
pi  ALL=(ALL) NOPASSWD: /home/pi/printer_data/config/3dwork-klipper/scripts/change-hostname-as-root.sh
#EOF

		$sudo chown root:root /tmp/031-3dwork-change-hostname
		$sudo chmod 440 /tmp/031-3dwork-change-hostname
		$sudo cp --preserve=mode /tmp/031-3dwork-change-hostname /etc/sudoers.d/031-3dwork-change-hostname
	fi
}
