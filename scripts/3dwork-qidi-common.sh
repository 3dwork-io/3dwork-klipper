#!/bin/bash
report_status()
{
    echo -e "\n\n###### $1"
}

ensure_sudo_command_whitelisting()
{
	sudo="sudo"
	if [ "$1" = "root" ]
	then
		sudo=""
	fi
    report_status "Updating whitelisted commands"
	# Whitelist 3dwork git hook scripts
	if [[ -e /etc/sudoers.d/030-3dwork-githooks ]]
	then
		$sudo rm /etc/sudoers.d/030-3dwork-githooks
		$sudo rm /tmp/030-3dwork-githooks
	fi
	touch /tmp/030-3dwork-githooks
	cat << '#EOF' > /tmp/030-3dwork-githooks
mks  ALL=(ALL) NOPASSWD: /home/mks/klipper_config/3dwork-klipper/scripts/3dwork-qidi-update.sh
#EOF

	$sudo chown root:root /tmp/030-3dwork-githooks
	$sudo chmod 440 /tmp/030-3dwork-githooks
	$sudo cp --preserve=mode /tmp/030-3dwork-githooks /etc/sudoers.d/030-3dwork-githooks
}

install_hooks()
{
    report_status "Installing git hooks"
	if [[ ! -e /home/pi/printer_data/config/RatOS/.git/hooks/post-merge ]]
	then
 	   ln -s /home/mks/klipper_config/3dwork-klipper/scripts/3dwork-post-merge.sh /home/mks/klipper_config/3dwork-klipper/.git/hooks/post-merge
	fi
}

ensure_ownership() {
  report_status "Ensure Scripts Ownership... chown"
  sudo chown mks:mks -R /home/mks/klipper_config/3dwork-klipper/scripts
  report_status "Ensure Scripts Ownership... chmod"
  sudo chmod +x /home/mks/klipper_config/3dwork-klipper/scripts/*.sh
}