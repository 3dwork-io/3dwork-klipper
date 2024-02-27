#!/bin/bash

workspace_klipper="/home/pi/klipper"
workspace_3dwork="/home/pi/printer_data/config"
workspace_firmware_binaries="/home/pi/printer_data/config"

compile_btt-manta-e3ez() {
    echo "Compiling firmware for BTT Manta E3 EZ"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-manta-e3ez/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-manta-e3ez.bin
}

compile_btt-manta-m4p() {
    echo "Compiling firmware for BTT Manta M4P"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-manta-m4p/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-manta-m4p.bin
}

compile_btt-manta-m4p-22() {
    echo "Compiling firmware for BTT Manta M4P v2.2"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-manta-m4p-22/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-manta-m4p-22.bin
}

compile_btt-manta-m8p() {
    echo "Compiling firmware for BTT Manta M8P"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-manta-m8p/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-manta-m8p.bin
}

compile_btt-manta-m8p-11() {
    echo "Compiling firmware for BTT Manta M8P v1.1"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-manta-m8p-11/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-manta-m8p-11.bin
}

compile_btt-octopus-max-ez() {
    echo "Compiling firmware for BTT Octopus Max EZ"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-max-ez/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-max-ez.bin
}

compile_btt-octopus-pro-446() {
    echo "Compiling firmware for BTT Octopus Pro 446"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-pro-446/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-pro-446.bin
}

compile_btt-octopus-pro-429() {
    echo "Compiling firmware for BTT Octopus Pro 429"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-pro-429/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-pro-429.bin
}

compile_btt-octopus-pro-h723() {
    echo "Compiling firmware for BTT Octopus Pro H723"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-pro-h723/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-pro-h723.bin
}

compile_btt-octopus-11() {
    echo "Compiling firmware for BTT Octopus v1.1"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-11/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-11.bin
}

compile_btt-octopus-11-407() {
    echo "Compiling firmware for BTT Octopus v1.1 (407)"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-octopus-11-407/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-octopus-11-407.bin
}

compile_fysetc_spider() {
    echo "Compiling firmware for Fysetc Spider v1.1"
    cp -f $workspace_3dwork/3dwork-klipper/boards/fysetc-spider/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-fysetc-spider.bin
}

compile_skr_pro_12() {
    echo "Compiling firmware for SKR Pro 1.2"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-pro-12/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-pro-12.bin
}

compile_btt-skr-2-429() {
    echo "Compiling firmware for SKR 2 429"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-2-429/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-2-429.bin
}

compile_btt-skr-2-407() {
    echo "Compiling firmware for SKR 2 407"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-2-407/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-2-407.bin
}

compile_btt_ebb42_10() {
    echo "Compiling firmware for BTT EBB42 v1.0"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb42-10/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb42-10.bin
}

compile_btt_ebb36_10() {
    echo "Compiling firmware for BTT EBB36 v1.0"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb36-10/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb36-10.bin
}

compile_btt_ebb42_11() {
    echo "Compiling firmware for BTT EBB42 v1.1"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb42-11/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb42-11.bin
}

compile_btt_ebb36_11() {
    echo "Compiling firmware for BTT EBB36 v1.1"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb36-11/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb36-11.bin
}

compile_btt_ebb42_12() {
    echo "Compiling firmware for BTT EBB42 v1.2"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb42-12/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb42-12.bin
}

compile_btt_ebb36_12() {
    echo "Compiling firmware for BTT EBB36 v1.2"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-ebb36-12/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-ebb36-12.bin
}

compile_mellow_fly_sht_42() {
    echo "Compiling firmware for Mellow FLY-SHT42"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mellow-fly-sht-42/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-mellow-fly-sht-42.bin
}

compile_mellow_fly_sht_36() {
    echo "Compiling firmware for Mellow FLY-SHT36"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mellow-fly-sht-36/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-mellow-fly-sht-36.bin
}

compile_btt_skr_mini_e3_30() {
    echo "Compiling firmware for BTT SKR E3 Mini V3.0"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-mini-e3-30/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-mini-e3-30.bin
}

compile_btt_skr_3() {
    echo "Compiling firmware for SKR 3"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-3/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-3.bin
}

compile_btt-skr-3-h723() {
    echo "Compiling firmware for SKR 3 (H723)"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-3-h723/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-3-h723.bin
}

compile_btt-skr-3-ez() {
    echo "Compiling firmware for SKR 3 EZ"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-3-ez/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-3-ez.bin
}

compile_btt-skr-3-ez-h723() {
    echo "Compiling firmware for SKR 3 EZ (H723)"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-3-ez-h723/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-3-ez-h723.bin
}

compile_btt-skrat-10() {
    echo "Compiling firmware for SKR RAT v1.0"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skrat-10/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skrat-10.bin
}

compile_btt-skr-14-turbo() {
    echo "Compiling firmware for SKR 1.4 Turbo"
    cp -f $workspace_3dwork/3dwork-klipper/boards/btt-skr-14-turbo/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-btt-skr-14-turbo.bin
}

compile_znp_robin_nano_dw_v2() {
    echo "Compiling firmware for ZNP Robin Nano DW v2"
    cp -f $workspace_3dwork/3dwork-klipper/boards/znp-robin-nano-dw-v2/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-znp-robin-nano-dw-v2.bin
}

compile_mks-eagle-10() {
    echo "Compiling firmware for MKS Eagle v1.x"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mks-eagle-10/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-mks-eagle-10.bin
}

compile_mks-robin-nano-30() {
    echo "Compiling firmware for MKS Robin Nano v3.x"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mks-robin-nano-30/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-mks-robin-nano-30.bin
}

compile_mks-robin-nano-20() {
    echo "Compiling firmware for MKS Robin Nano v2.x"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mks-robin-nano-20/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-mks-robin-nano-20.bin
}

compile_mks-gen-l() {
    echo "Compiling firmware for MKS Gen L"
    cp -f $workspace_3dwork/3dwork-klipper/boards/mks-gen-l/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.elf.hex $workspace_firmware_binaries/firmware_binaries/firmware-mks-gen-l.hex
}

compile_artillery-ruby-12() {
    echo "Compiling firmware for Artillery Ruby v1.x"
    cp -f $workspace_3dwork/3dwork-klipper/boards/artillery-ruby-12/firmware.config $workspace_klipper/.config
    make olddefconfig
    make clean
    make
    cp $workspace_klipper/out/klipper.bin $workspace_firmware_binaries/firmware_binaries/firmware-artillery-ruby-12.bin
}

#####################################
# NOT ADDED TO KLIPPER AUTO BUILDER #
#####################################

# Force script to exit if an error occurs
set -e

if [ ! -d "$workspace_firmware_binaries/firmware_binaries" ]
then
    mkdir $workspace_firmware_binaries/firmware_binaries
    chown pi:pi $workspace_firmware_binaries/firmware_binaries
fi


pushd $workspace_klipper


# Check the parameter and call the corresponding compilation function
if [ -z "$1" ]; then
    # If no parameter is provided, compile firmware for all boards
    # Run make scripts for the supported boards.
    compile_btt-manta-e3ez
    compile_btt-manta-m4p
    compile_btt-manta-m4p-22
    compile_btt-manta-m8p
    compile_btt-manta-m8p-11
    compile_btt-octopus-max-ez
    compile_btt-octopus-pro-446
    compile_btt-octopus-pro-429
    compile_btt-octopus-pro-h723
    compile_btt-octopus-11
    compile_btt-octopus-11-407
    compile_skr_pro_12
    compile_btt_skr_mini_e3_30
    compile_btt_skr_3
    compile_btt-skr-3-h723
    compile_btt-skr-3-ez
    compile_btt-skr-3-ez-h723
    compile_btt-skr-2-429
    compile_btt-skr-2-407
    compile_btt-skrat-10
    compile_btt-skr-14-turbo
    # Elegoo
    compile_znp_robin_nano_dw_v2
    # Makerbase
    compile_mks-eagle-10
    compile_mks-robin-nano-30
    compile_mks-robin-nano-20
    compile_mks-gen-l
    # Artillery
    compile_artillery-ruby-12
    # Fysetc
    compile_fysetc_spider
    # Mellow
    compile_mellow_fly_sht_42
    compile_mellow_fly_sht_36
    # Toolheads
    compile_btt_ebb42_10
    compile_btt_ebb36_10
    compile_btt_ebb42_11
    compile_btt_ebb36_11
    compile_btt_ebb42_12
    compile_btt_ebb36_12
else
    compile_function="compile_$1"
    if declare -f "$compile_function" >/dev/null; then
        eval "$compile_function"
    else
        echo "Invalid board selection: $1"
        exit 1
    fi
fi

chown pi:pi $workspace_firmware_binaries/firmware_binaries/*.bin

popd
