#!/usr/bin/env python3
"""
3Dwork Klipper Web Wizard
Flask-based web interface for Klipper configuration
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file
import json

VERSION = "2.0.0-dev"

app = Flask(__name__)
app.config["SECRET_KEY"] = "3dwork-klipper-wizard-secret-key"

# Get config directory
WIZARD_DIR = Path(__file__).parent.parent
CONFIG_DIR = Path.home() / "printer_data" / "config"


# Board data (same as CLI)
BOARDS = {
    "BigTreeTech": {
        "Manta (CAN)": [
            {
                "id": "btt-manta-e3ez",
                "name": "Manta E3 EZ",
                "mcu": "stm32g0b1",
                "can": True,
            },
            {
                "id": "btt-manta-m4p",
                "name": "Manta M4P",
                "mcu": "stm32h743",
                "can": True,
            },
            {
                "id": "btt-manta-m4p-22",
                "name": "Manta M4P v2.2",
                "mcu": "stm32h743",
                "can": True,
            },
            {
                "id": "btt-manta-m8p",
                "name": "Manta M8P",
                "mcu": "stm32h743",
                "can": True,
            },
            {
                "id": "btt-manta-m8p-11",
                "name": "Manta M8P v1.1",
                "mcu": "stm32h743",
                "can": True,
            },
            {
                "id": "btt-manta-m8p-v2",
                "name": "Manta M8P v2.0",
                "mcu": "stm32h743",
                "can": True,
            },
        ],
        "Octopus": [
            {"id": "btt-octopus-max-ez", "name": "Octopus Max EZ", "mcu": "stm32h723"},
            {
                "id": "btt-octopus-pro-446",
                "name": "Octopus Pro (446)",
                "mcu": "stm32f446",
            },
            {
                "id": "btt-octopus-pro-429",
                "name": "Octopus Pro (429)",
                "mcu": "stm32f429",
            },
            {
                "id": "btt-octopus-pro-h723",
                "name": "Octopus Pro (H723)",
                "mcu": "stm32h723",
            },
            {"id": "btt-octopus-11", "name": "Octopus v1.1", "mcu": "stm32f407"},
        ],
        "SKR": [
            {"id": "skr_pro_12", "name": "SKR Pro v1.2", "mcu": "stm32f407"},
            {"id": "btt-skr-3", "name": "SKR 3", "mcu": "stm32h743"},
            {"id": "btt-skr-3-h723", "name": "SKR 3 (H723)", "mcu": "stm32h723"},
            {"id": "btt-skr-3-ez", "name": "SKR 3 EZ", "mcu": "stm32h743"},
            {"id": "btt-skr-2-429", "name": "SKR 2 (429)", "mcu": "stm32f429"},
            {"id": "btt-skr-2-407", "name": "SKR 2 (407)", "mcu": "stm32f407"},
            {"id": "btt-skrat-10", "name": "SKR RAT", "mcu": "stm32f407"},
            {"id": "btt-skr-14-turbo", "name": "SKR 1.4 Turbo", "mcu": "stm32f407"},
            {
                "id": "btt_skr_mini_e3_30",
                "name": "SKR Mini E3 v3.0",
                "mcu": "stm32g0b1",
            },
        ],
    },
    "MKS Instruments": {
        "Robin Nano": [
            {
                "id": "mks-robin-nano-v3",
                "name": "MKS Robin Nano v3",
                "mcu": "stm32f103",
            },
            {
                "id": "mks-robin-nano-v3-1",
                "name": "MKS Robin Nano v3.1",
                "mcu": "stm32f103",
            },
            {
                "id": "mks-robin-nano-20",
                "name": "MKS Robin Nano v2",
                "mcu": "stm32f103",
            },
        ],
        "Other": [
            {"id": "mks-eagle-10", "name": "MKS Eagle v1.0", "mcu": "stm32f103"},
            {"id": "mks-gen-l", "name": "MKS Gen L", "mcu": "stm32f103"},
        ],
    },
    "Fysetc": {
        "Spider": [
            {"id": "fysetc_spider", "name": "Fysetc Spider", "mcu": "stm32f407"},
            {
                "id": "fysetc-spider-king",
                "name": "Fysetc Spider King",
                "mcu": "stm32f407",
            },
        ],
    },
    "Creality": {
        "CR/Ender": [
            {"id": "creality-v4-2-2", "name": "Creality v4.2.2", "mcu": "stm32f103"},
            {"id": "creality-v4-2-7", "name": "Creality v4.2.7", "mcu": "stm32f103"},
            {"id": "creality-v4-2-10", "name": "Creality v4.2.10", "mcu": "stm32f103"},
        ],
    },
    "Raspberry": {
        "RP2040": [
            {"id": "rpi-pico", "name": "Raspberry Pi Pico", "mcu": "rp2040"},
        ],
    },
    "Mellow": {
        "FLY": [
            {"id": "mellow-fly-gem", "name": "FLY-GEM", "mcu": "stm32h743"},
            {"id": "mellow-fly-sht-42", "name": "FLY SHT 42 (CAN)", "mcu": "stm32g0b1"},
            {"id": "mellow-fly-sht-36", "name": "FLY SHT 36 (CAN)", "mcu": "stm32g0b1"},
        ],
    },
    "BigTreeTech CAN": {
        "EBB": [
            {"id": "btt-ebb42-12", "name": "EBB42 v1.2 (CAN)", "mcu": "stm32g0b1"},
            {"id": "btt-ebb36-12", "name": "EBB36 v1.2 (CAN)", "mcu": "stm32g0b1"},
        ],
    },
}

# Store session data
session_data = {
    "board": None,
    "printer": {},
    "features": {},
}


def generate_printer_cfg(board: dict, printer: dict, features: dict) -> str:
    """Generate printer.cfg content"""

    config = f"""# 3Dwork Klipper Configuration
# Generated by 3Dwork Klipper Web Wizard v{VERSION}
# Board: {board["name"]} ({board["id"]})
# MCU: {board["mcu"]}
# Printer: {printer.get("name", "Custom")}

[mcu]
serial: /dev/serial/by-id/usb-*
restart_method: command

[printer]
kinematics: {printer.get("kinematics", "cartesian")}
max_velocity: {printer.get("max_velocity", 300)}
max_accel: {printer.get("max_accel", 3000)}
max_z_velocity: {printer.get("max_z_velocity", 20)}
max_z_accel: {printer.get("max_z_accel", 500)}

# Stepper Configuration
[stepper_x]
step_pin: PB0
dir_pin: PC5
enable_pin: !PC6
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("x_rotation_distance", 40)}
endstop_pin: ^PA5

[stepper_y]
step_pin: PB1
dir_pin: PC2
enable_pin: !PC3
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("y_rotation_distance", 40)}
endstop_pin: ^PA6

[stepper_z]
step_pin: PB2
dir_pin: !PC1
enable_pin: !PC4
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("z_rotation_distance", 8)}
endstop_pin: ^PA7

# Extruder
[extruder]
step_pin: PB3
dir_pin: !PC0
enable_pin: !PC7
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("extruder_rotation_distance", 7.5)}
nozzle_diameter: {printer.get("nozzle_diameter", 0.4)}
filament_diameter: 1.75

[heater_extruder]
heater_pin: PA2
sensor_type: ATC Semitec 104GT
sensor_pin: PC5
min_temp: 0
max_temp: 300

# Heated Bed
[heater_bed]
heater_pin: PA1
sensor_type: Generic 395nm
sensor_pin: PC4
min_temp: 0
max_temp: 130
"""

    # Add probe if enabled
    if features.get("probe_type") == "bltouch":
        config += f"""
# BLTouch Probe
[probe]
pin: {features.get("probe_pin", "PC15")}
x_offset: {features.get("probe_x_offset", 0)}
y_offset: {features.get("probe_y_offset", 0)}
z_offset: {features.get("probe_z_offset", 0)}
speed: 5
sample_retract_dist: 2

[bed_mesh]
horizontal_move_z: 5
speed: 150
"""

    # Add display if enabled
    if features.get("display_type"):
        config += f"""
# Display
[display]
lcd_type: {features["display_type"]}
"""

    # Add 3dwork macros
    config += f"""
# 3Dwork Macros
[include 3dwork-klipper/macros/macros_*.cfg]
[include 3dwork-klipper/shell-macros.cfg]

#*# <--- SAVE_CONFIG --->
"""

    return config


@app.route("/")
def index():
    """Main page"""
    return render_template("index.html", version=VERSION)


@app.route("/api/boards")
def get_boards():
    """Get all available boards"""
    return jsonify(BOARDS)


@app.route("/api/config", methods=["GET", "POST"])
def config():
    """Get or update configuration"""
    global session_data

    if request.method == "POST":
        data = request.json

        if data.get("board"):
            session_data["board"] = data["board"]
        if data.get("printer"):
            session_data["printer"].update(data["printer"])
        if data.get("features"):
            session_data["features"].update(data["features"])

        return jsonify({"status": "ok", "data": session_data})

    return jsonify(session_data)


@app.route("/api/generate", methods=["POST"])
def generate():
    """Generate printer.cfg"""
    data = request.json

    board = data.get("board", session_data.get("board"))
    printer = data.get("printer", session_data.get("printer", {}))
    features = data.get("features", session_data.get("features", {}))

    if not board:
        return jsonify({"error": "No board selected"}), 400

    config = generate_printer_cfg(board, printer, features)

    return jsonify({"config": config, "length": len(config)})


@app.route("/api/save", methods=["POST"])
def save_config():
    """Save printer.cfg to file"""
    data = request.json
    config_content = data.get("config", "")

    output_file = CONFIG_DIR / "printer.cfg"

    try:
        with open(output_file, "w") as f:
            f.write(config_content)
        return jsonify({"status": "saved", "file": str(output_file)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/download")
def download():
    """Download printer.cfg"""
    config = request.args.get("config", "")

    output_file = CONFIG_DIR / "printer.cfg"

    with open(output_file, "w") as f:
        f.write(config)

    return send_file(output_file, as_attachment=True, download_name="printer.cfg")


@app.route("/api/install")
def install_klipper():
    """Install 3dwork-klipper"""
    import subprocess

    target_dir = CONFIG_DIR / "3dwork-klipper"

    if target_dir.exists():
        return jsonify({"status": "exists", "path": str(target_dir)})

    try:
        subprocess.run(
            [
                "git",
                "clone",
                "-b",
                "dev",
                "https://github.com/3dwork-io/3dwork-klipper.git",
                str(target_dir),
            ],
            check=True,
            capture_output=True,
        )
        return jsonify({"status": "installed", "path": str(target_dir)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║        3DWORK KLIPPER WEB WIZARD v{VERSION}                    ║
╚═══════════════════════════════════════════════════════════╝

Iniciando servidor web...
Accede a: http://localhost:5000

Nota: Si es la primera vez, instala las dependencias:
  pip3 install flask
""")

    app.run(host="0.0.0.0", port=5000, debug=True)
