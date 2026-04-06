#!/usr/bin/env python3
"""
3Dwork Klipper Wizard - CLI Interface v2.0
Main entry point for the interactive wizard with full feature support
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

VERSION = "2.0.0-dev"


class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    BOLD = "\033[1m"
    NC = "\033[0m"


def print_header():
    print(f"{Colors.GREEN}")
    print("╔═══════════════════════════════════════════════════════════╗")
    print(f"║          3DWORK KLIPPER WIZARD v{VERSION}                      ║")
    print(f"║           Asistente de configuración Klipper               ║")
    print(f"║           +40 boards · Templates · Web UI                  ║")
    print(f"╚═══════════════════════════════════════════════════════════╝")
    print(f"{Colors.NC}")


def print_menu():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════╗")
    print("║              MENÚ PRINCIPAL                ║")
    print("╠════════════════════════════════════════════════╣")
    print(f"║  {Colors.YELLOW}1.{Colors.NC} Seleccionar Electrónica           ║")
    print(f"║  {Colors.YELLOW}2.{Colors.NC} Configurar Impresora               ║")
    print(f"║  {Colors.YELLOW}3.{Colors.NC} Generar printer.cfg                ║")
    print(f"║  {Colors.YELLOW}4.{Colors.NC} Compilar Firmware                   ║")
    print(f"║  {Colors.YELLOW}5.{Colors.NC} Instalar 3Dwork-klipper             ║")
    print(f"║  {Colors.YELLOW}6.{Colors.NC} Actualizar Instalación              ║")
    print(f"║  {Colors.YELLOW}7.{Colors.NC} Configuración Actual                ║")
    print(f"║  {Colors.YELLOW}8.{Colors.NC} Biblioteca de Configs              ║")
    print(f"║  {Colors.YELLOW}9.{Colors.NC} Web Wizard (servidor local)         ║")
    print(f"║  {Colors.YELLOW}0.{Colors.NC} Salir                               ║")
    print(f"╚════════════════════════════════════════════════╝{Colors.NC}")


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def get_input(prompt: str, default: str = "") -> str:
    if default:
        result = input(f"{Colors.CYAN}{prompt}{Colors.NC} [{default}]: ").strip()
        return result if result else default
    return input(f"{Colors.CYAN}{prompt}{Colors.NC}: ").strip()


def get_yes_no(prompt: str, default: str = "n") -> bool:
    default_str = "Y/n" if default == "y" else "N/y"
    result = (
        input(f"{Colors.CYAN}{prompt} ({default_str}){Colors.NC}: ").strip().lower()
    )
    return result in ["y", "yes"] if default == "n" else result in ["y", "yes", ""]


def get_choice(prompt: str, options: List[str], default: int = 1) -> int:
    for i, opt in enumerate(options, 1):
        print(f"  {Colors.YELLOW}{i}.{Colors.NC} {opt}")
    choice = get_input(prompt, str(default))
    try:
        return int(choice)
    except:
        return default


class BoardManager:
    """Complete board definitions with pinouts and configurations"""

    BOARDS = {
        "BigTreeTech": {
            "Manta (CAN)": [
                {
                    "id": "btt-manta-e3ez",
                    "name": "Manta E3 EZ",
                    "mcu": "stm32g0b1",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m4p",
                    "name": "Manta M4P",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m4p-22",
                    "name": "Manta M4P v2.2",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m8p",
                    "name": "Manta M8P",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m8p-11",
                    "name": "Manta M8P v1.1",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m8p-v2",
                    "name": "Manta M8P v2.0",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-manta-m8p-v2-1",
                    "name": "Manta M8P v2.1",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
            ],
            "Octopus": [
                {
                    "id": "btt-octopus-max-ez",
                    "name": "Octopus Max EZ",
                    "mcu": "stm32h723",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-pro-446",
                    "name": "Octopus Pro (446)",
                    "mcu": "stm32f446",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-pro-429",
                    "name": "Octopus Pro (429)",
                    "mcu": "stm32f429",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-pro-h723",
                    "name": "Octopus Pro (H723)",
                    "mcu": "stm32h723",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-11",
                    "name": "Octopus v1.1",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-11-407",
                    "name": "Octopus v1.1 (407)",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-octopus-max",
                    "name": "Octopus Max",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
            ],
            "SKR (BTT)": [
                {
                    "id": "skr_pro_12",
                    "name": "SKR Pro v1.2",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skr-3",
                    "name": "SKR 3",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-skr-3-h723",
                    "name": "SKR 3 (H723)",
                    "mcu": "stm32h723",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-skr-3-ez",
                    "name": "SKR 3 EZ",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-skr-3-ez-h723",
                    "name": "SKR 3 EZ (H723)",
                    "mcu": "stm32h723",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "btt-skr-2-429",
                    "name": "SKR 2 (429)",
                    "mcu": "stm32f429",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skr-2-407",
                    "name": "SKR 2 (407)",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skrat-10",
                    "name": "SKR RAT",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skr-14-turbo",
                    "name": "SKR 1.4 Turbo",
                    "mcu": "stm32f407",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skr-14",
                    "name": "SKR 1.4",
                    "mcu": "stm32f407",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt_skr_mini_e3_30",
                    "name": "SKR Mini E3 v3.0",
                    "mcu": "stm32g0b1",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt_skr_mini_e3_20",
                    "name": "SKR Mini E3 v2.0",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "btt-skr-e3-turbo",
                    "name": "SKR E3 Turbo",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "MKS Instruments": {
            "Robin Nano": [
                {
                    "id": "mks-robin-nano-v3",
                    "name": "MKS Robin Nano v3",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-robin-nano-v3-1",
                    "name": "MKS Robin Nano v3.1",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-robin-nano-20",
                    "name": "MKS Robin Nano v2",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-robin-nano-v2-1",
                    "name": "MKS Robin Nano v2.1",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-robin-nano-dw",
                    "name": "MKS Robin Nano DW",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "znp_robin_nano_dw_v2",
                    "name": "ZNP Robin Nano DW v2",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
            "Other": [
                {
                    "id": "mks-eagle-10",
                    "name": "MKS Eagle v1.0",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-gen-l-v2",
                    "name": "MKS Gen L v2.0",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-gen-l",
                    "name": "MKS Gen L",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "mks-sbase",
                    "name": "MKS SBase",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "Fysetc": {
            "Spider": [
                {
                    "id": "fysetc-spider-king",
                    "name": "Fysetc Spider King",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "fysetc_spider",
                    "name": "Fysetc Spider",
                    "mcu": "stm32f407",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "fysetc-spider-207",
                    "name": "Fysetc Spider v2.0",
                    "mcu": "stm32f207",
                    "pins": "EXP1/EXP2",
                    "can": False,
                    "usb": True,
                },
            ],
            "Other": [
                {
                    "id": "fysetc-cheetah",
                    "name": "Fysetc Cheetah",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "fysetc-cheetah-plus",
                    "name": "Fysetc Cheetah Plus",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "Creality": {
            "CR/Ender": [
                {
                    "id": "creality-v4-2-2",
                    "name": "Creality v4.2.2",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "creality-v4-2-7",
                    "name": "Creality v4.2.7",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "creality-v4-2-10",
                    "name": "Creality v4.2.10",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "creality-f401",
                    "name": "Creality F401",
                    "mcu": "stm32f401",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "creality-f403",
                    "name": "Creality F403",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
            "Sonic Pad": [
                {
                    "id": "creality-sonic-pad",
                    "name": "Creality Sonic Pad",
                    "mcu": "rk3326",
                    "pins": "N/A",
                    "can": False,
                    "usb": False,
                },
            ],
        },
        "Artillery": {
            "Ruby/Sidewinder": [
                {
                    "id": "artillery-ruby-12",
                    "name": "Artillery Ruby v1.2",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "artillery-ruby-13",
                    "name": "Artillery Ruby v1.3",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "artillery-sidewinder-x1",
                    "name": "Artillery Sidewinder X1",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "Raspberry": {
            "RP2040": [
                {
                    "id": "rpi-pico",
                    "name": "Raspberry Pi Pico",
                    "mcu": "rp2040",
                    "pins": "GPIO",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "rpi-pico-w",
                    "name": "Raspberry Pi Pico W",
                    "mcu": "rp2040",
                    "pins": "GPIO",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "Mellow": {
            "FLY": [
                {
                    "id": "mellow-fly-gem",
                    "name": "FLY-GEM",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "mellow-fly-sht-42",
                    "name": "FLY SHT 42 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "mellow-fly-sht-36",
                    "name": "FLY SHT 36 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "mellow-fly-sht-v2-42",
                    "name": "FLY SHT v2 42 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "mellow-fly-sht-v2-36",
                    "name": "FLY SHT v2 36 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
            ],
        },
        "BigTreeTech CAN": {
            "EBB": [
                {
                    "id": "btt-ebb42-10",
                    "name": "EBB42 v1.0 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb42-11",
                    "name": "EBB42 v1.1 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb42-12",
                    "name": "EBB42 v1.2 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb36-10",
                    "name": "EBB36 v1.0 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb36-11",
                    "name": "EBB36 v1.1 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb36-12",
                    "name": "EBB36 v1.2 (CAN)",
                    "mcu": "stm32g0b1",
                    "pins": "SHT",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "btt-ebb42-can-v1",
                    "name": "EBB42 CAN v1 (RP2040)",
                    "mcu": "rp2040",
                    "pins": "GPIO",
                    "can": True,
                    "usb": False,
                },
            ],
        },
        "LDO": {
            "LDO MOTHERBOARD": [
                {
                    "id": "ldo-kirigami-bfs",
                    "name": "LDO Kirigami BFS",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
                {
                    "id": "ldo-nema17-spark",
                    "name": "LDO NEMA17 Spark",
                    "mcu": "stm32f103",
                    "pins": "EXP1",
                    "can": False,
                    "usb": True,
                },
            ],
        },
        "Other": {
            "Various": [
                {
                    "id": "leviathan-v12",
                    "name": "Leviathan v1.2",
                    "mcu": "stm32h743",
                    "pins": "EXP1/EXP2",
                    "can": True,
                    "usb": True,
                },
                {
                    "id": "stealthburner-os",
                    "name": "StealthBurner OS",
                    "mcu": "rp2040",
                    "pins": "GPIO",
                    "can": True,
                    "usb": False,
                },
                {
                    "id": "canboard-v1",
                    "name": "CAN Board v1.0",
                    "mcu": "stm32g0b1",
                    "pins": "CAN",
                    "can": True,
                    "usb": False,
                },
            ],
        },
    }

    def get_all_boards(self) -> List[Dict]:
        boards = []
        for manufacturer, categories in self.BOARDS.items():
            for category, board_list in categories.items():
                for board in board_list:
                    board["manufacturer"] = manufacturer
                    board["category"] = category
                    boards.append(board)
        return boards

    def get_board(self, board_id: str) -> Optional[Dict]:
        for categories in self.BOARDS.values():
            for board_list in categories.values():
                for board in board_list:
                    if board["id"] == board_id:
                        return board
        return None

    def display(self):
        print(
            f"\n{Colors.BOLD}╔════════════════════════════════════════════════════════════════╗"
        )
        print("║                 ELECTRÓNICAS SOPORTADAS                    ║")
        print("╠════════════════════════════════════════════════════════════════╣")

        for manufacturer, categories in self.BOARDS.items():
            print(f"\n  {Colors.YELLOW}{manufacturer}{Colors.NC}")
            for category, board_list in categories.items():
                print(f"    {Colors.MAGENTA}{category}:{Colors.NC}")
                for board in board_list:
                    can_str = (
                        f" {Colors.GREEN}[CAN]{Colors.NC}" if board.get("can") else ""
                    )
                    print(
                        f"      {Colors.CYAN}•{Colors.NC} {board['name']} ({board['id']}){can_str}"
                    )


class ConfigGenerator:
    """Advanced printer.cfg generator with templates"""

    DEFAULT_PINS = {
        "cartesian": {
            "x": {"step": "PB0", "dir": "PC5", "enable": "!PC6", "endstop": "^PA5"},
            "y": {"step": "PB1", "dir": "PC2", "enable": "!PC3", "endstop": "^PA6"},
            "z": {"step": "PB2", "dir": "!PC1", "enable": "!PC4", "endstop": "^PA7"},
        },
        "corexy": {
            "x": {"step": "PB0", "dir": "PC5", "enable": "!PC6"},
            "y": {"step": "PB1", "dir": "PC2", "enable": "!PC3"},
            "z": {"step": "PB2", "dir": "!PC1", "enable": "!PC4", "endstop": "^PA7"},
        },
        "corexy_uart": {
            "x": {"step": "PB0", "dir": "PC5", "enable": "!PC6"},
            "y": {"step": "PB1", "dir": "PC2", "enable": "!PC3"},
            "z": {"step": "PB2", "dir": "!PC1", "enable": "!PC4", "endstop": "^PA7"},
        },
        "delta": {
            "stepper_a": {"step": "PB0", "dir": "PC5", "enable": "!PC6"},
            "stepper_b": {"step": "PB1", "dir": "PC2", "enable": "!PC3"},
            "stepper_c": {"step": "PB2", "dir": "!PC1", "enable": "!PC4"},
        },
    }

    def generate(self, board: Dict, printer: Dict, features: Dict) -> str:
        config = f"""# 3Dwork Klipper Configuration
# Generated by 3Dwork Klipper Wizard v{VERSION}
# Board: {board["name"]} ({board["id"]})
# MCU: {board["mcu"]}
# Printer: {printer.get("name", "Custom")}
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# ============================================

[mcu]
serial: /dev/serial/by-id/usb-*
restart_method: command

[printer]
kinematics: {printer.get("kinematics", "cartesian")}
max_velocity: {printer.get("max_velocity", 300)}
max_accel: {printer.get("max_accel", 3000)}
max_z_velocity: {printer.get("max_z_velocity", 20)}
max_z_accel: {printer.get("max_z_accel", 500)}

# ============================================
# Stepper Configuration
# ============================================
"""
        config += self._generate_steppers(printer)

        # Add extruder
        config += self._generate_extruder(printer.get("extruder", {}))

        # Add heater
        config += self._generate_heaters(printer.get("heaters", {}))

        # Add features
        config += self._generate_features(features)

        # Add 3dwork macros
        config += self._generate_3dwork_macros()

        return config

    def _generate_steppers(self, printer: Dict) -> str:
        kinematics = printer.get("kinematics", "cartesian")
        pins = self.DEFAULT_PINS.get(kinematics, self.DEFAULT_PINS["cartesian"])

        stepper_config = ""

        if kinematics in ["cartesian", "corexy", "corexy_uart"]:
            # X Stepper
            stepper_config += f"""
[stepper_x]
step_pin: {pins["x"]["step"]}
dir_pin: {pins["x"]["dir"]}
enable_pin: {pins["x"]["enable"]}
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("x_rotation_distance", 40)}
"""
            if "endstop" in pins["x"]:
                stepper_config += f"endstop_pin: {pins['x']['endstop']}\n"

            # Y Stepper
            stepper_config += f"""
[stepper_y]
step_pin: {pins["y"]["step"]}
dir_pin: {pins["y"]["dir"]}
enable_pin: {pins["y"]["enable"]}
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("y_rotation_distance", 40)}
"""
            if "endstop" in pins["y"]:
                stepper_config += f"endstop_pin: {pins['y']['endstop']}\n"

            # Z Stepper
            stepper_config += f"""
[stepper_z]
step_pin: {pins["z"]["step"]}
dir_pin: {pins["z"]["dir"]}
enable_pin: {pins["z"]["enable"]}
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("z_rotation_distance", 8)}
"""
            if "endstop" in pins["z"]:
                stepper_config += f"endstop_pin: {pins['z']['endstop']}\n"

        elif kinematics == "delta":
            for i, (name, pin_set) in enumerate(pins.items(), 1):
                stepper_config += f"""
[{name}]
step_pin: {pin_set["step"]}
dir_pin: {pin_set["dir"]}
enable_pin: {pin_set["enable"]}
microsteps: {printer.get("microsteps", 16)}
rotation_distance: {printer.get("delta_rotation_distance", 25)}
step_angle: {printer.get("delta_step_angle", 0.9)}
"""

        return stepper_config

    def _generate_extruder(self, extruder: Dict) -> str:
        if not extruder:
            extruder = {
                "type": "extruder",
                "step_pin": "PB3",
                "dir_pin": "!PC0",
                "enable_pin": "!PC7",
            }

        return f"""
# ============================================
# Extruder
# ============================================
[{extruder.get("type", "extruder")}]
step_pin: {extruder.get("step_pin", "PB3")}
dir_pin: {extruder.get("dir_pin", "!PC0")}
enable_pin: {extruder.get("enable_pin", "!PC7")}
microsteps: {extruder.get("microsteps", 16)}
rotation_distance: {extruder.get("rotation_distance", 7.5)}
 nozzle_diameter: {extruder.get("nozzle_diameter", 0.4)}
filament_diameter: {extruder.get("filament_diameter", 1.75)}

[heater_extruder]
heater_pin: {extruder.get("heater_pin", "PA2")}
sensor_type: {extruder.get("sensor_type", "ATC Semitec 104GT")}
sensor_pin: {extruder.get("sensor_pin", "PC5")}
min_temp: 0
max_temp: 300

[temperature_sensor extruder]
sensor_type: {extruder.get("sensor_type", "ATC Semitec 104GT")}
sensor_pin: {extruder.get("sensor_pin", "PC5")}
"""

    def _generate_heaters(self, heaters: Dict) -> str:
        return f"""
# ============================================
# Heated Bed
# ============================================
[heater_bed]
heater_pin: {heaters.get("bed_pin", "PA1")}
sensor_type: {heaters.get("bed_sensor", "Generic 395nm")}
sensor_pin: {heaters.get("bed_sensor_pin", "PC4")}
min_temp: 0
max_temp: 130

[temperature_sensor bed]
sensor_type: {heaters.get("bed_sensor", "Generic 395nm")}
sensor_pin: {heaters.get("bed_sensor_pin", "PC4")}
"""

    def _generate_features(self, features: Dict) -> str:
        config = ""

        # Probe/BLTouch
        if features.get("probe_type") == "bltouch":
            config += f"""
# ============================================
# BLTouch Probe
# ============================================
[probe]
pin: {features.get("probe_pin", "PC15")}
x_offset: {features.get("probe_x_offset", 0)}
y_offset: {features.get("probe_y_offset", 0)}
z_offset: {features.get("probe_z_offset", 0)}
speed: 5
sample_retract_dist: 2
samples: 3
samples_tolerance: 0.06

[bed_mesh]
horizontal_move_z: 5
speed: 150
mesh_min: {features.get("bed_mesh_min", "50, 50")}
mesh_max: {features.get("bed_mesh_max", "230, 230")}
"""

        # Display
        if features.get("display_type"):
            display_types = {
                "st7920": {
                    "lcd_type": "st7920",
                    "cs": "PA4",
                    "sclk": "PB0",
                    "mosi": "PB1",
                },
                "ssd1306": {"lcd_type": "ssd1306", "i2c_address": "0x3C"},
                "hd44780": {
                    "lcd_type": "hd44780",
                    "rs": "PA4",
                    "e": "PB0",
                    "d4": "PB1",
                    "d5": "PB2",
                    "d6": "PB3",
                    "d7": "PB4",
                },
            }
            d = display_types.get(features["display_type"], display_types["st7920"])

            config += f"""
# ============================================
# Display
# ============================================
[display]
lcd_type: {d["lcd_type"]}
"""
            if "i2c_address" in d:
                config += f"i2c_address: {d['i2c_address']}\n"
            else:
                config += f"cs_pin: {d.get('cs', 'PA4')}\nsclk_pin: {d.get('sclk', 'PB0')}\nmosi_pin: {d.get('mosi', 'PB1')}\n"

            config += """
[display_menu]
menu_root: main_menu
"""

        # Fan
        if features.get("has_fan"):
            config += f"""
# ============================================
# Fans
# ============================================
[fan]
pin: {features.get("fan_pin", "PC8")}
kick_start_time: 0.5

[fan_generic part_cooling]
pin: {features.get("part_fan_pin", "PC9")}
"""

        # ADC
        if features.get("has_adc"):
            config += f"""
# ============================================
# ADC Configuration
# ============================================
[adc_voltage]
vref: 5.0
samples: 8
"""

        return config

    def _generate_3dwork_macros(self) -> str:
        return f"""
# ============================================
# 3Dwork Macros
# ============================================
# Include 3Dwork macros
[include 3dwork-klipper/macros/macros_*.cfg]

# Shell macros (requires gcode_shell_extension)
[include 3dwork-klipper/shell-macros.cfg]

# ============================================
# SAVE_CONFIG
# ============================================
#*# <--- SAVE_CONFIG --->
#*# DO NOT EDIT THIS SECTION
#*# It is automatically generated
#*# Generated by 3Dwork Klipper Wizard v{VERSION}
"""


class ConfigLibrary:
    """Configuration library with multi-source parsing"""

    SOURCES = {
        "3dwork-klipper": {
            "url": "https://github.com/3dwork-io/3dwork-klipper/tree/master/printers",
            "type": "local",
            "description": "Configuraciones de impresoras 3Dwork",
        },
        "klipper-examples": {
            "url": "https://github.com/Klipper3d/klipper/tree/master/config",
            "type": "github",
            "description": "Ejemplos oficiales de Klipper",
        },
        "ratos": {
            "url": "https://github.com/Rat-OS/RatOS-configuration/tree/master/configurations",
            "type": "github",
            "description": "Configuraciones RatOS",
        },
        "creality-sonic-pad": {
            "url": "https://github.com/CrealityOfficial/CR-Sonic-Pad-Data",
            "type": "github",
            "description": "Configuraciones Creality Sonic Pad",
        },
    }

    def list_sources(self):
        print(f"\n{Colors.BOLD}BIBLIOTECA DE CONFIGURACIONES{Colors.NC}")
        print(f"\n{Colors.CYAN}Fuentes disponibles:{Colors.NC}")
        for key, source in self.SOURCES.items():
            print(f"  • {Colors.YELLOW}{key}{Colors.NC}: {source['description']}")

    def fetch_configs(self, source: str = None):
        print(
            f"\n{Colors.YELLOW}[INFO] Obteniendo configuraciones de fuentes...{Colors.NC}"
        )
        print("Esta función requerirá conexión a GitHub API.")
        print("Implementación completa en Web Wizard.")


class FirmwareCompiler:
    """Firmware compilation wrapper"""

    def compile(self, board: Dict) -> bool:
        print(f"\n{Colors.BLUE}Compilando firmware para {board['name']}...{Colors.NC}")
        print(f"\n{Colors.YELLOW}Métodos de compilación:{Colors.NC}")
        print("  1. Usar macro COMPILE_FIRMWARE desde Klipper:")
        print(
            f"     SET_GCODE_VARIABLE MACRO=COMPILE_FIRMWARE VARIABLE=BOARD VALUE='\"{board['id']}\"'"
        )
        print("  2. Usar el script de compilación existente:")
        print("     ~/klipper/scripts/install-python-dependencies.sh")
        print("     cd ~/klipper && make menuconfig")
        print("     make")
        return False

    def list_supported(self):
        bm = BoardManager()
        bm.display()


class WebWizard:
    """Web Wizard server manager"""

    def start(self):
        print(f"\n{Colors.BLUE}Web Wizard - Servidor Local{Colors.NC}")
        print("""
El Web Wizard proporciona una interfaz gráfica para:
  • Selección visual de electrónica
  • Configuración paso a paso con formularios
  • Vista previa de printer.cfg
  • Descarga de archivos

Para iniciar el servidor web, ejecuta:
  cd ~/printer_data/config/3dwork-klipper
  python3 wizard/web/app.py

Luego accede a: http://localhost:5000

Nota: El servidor web requiere Flask.
Si no está instalado: pip3 install flask
        """)


class Installer:
    """3dwork-klipper installer"""

    @staticmethod
    def install(printer_config_dir: Path):
        print(f"\n{Colors.BLUE}Instalando 3dwork-klipper...{Colors.NC}")

        target_dir = printer_config_dir / "3dwork-klipper"

        if target_dir.exists():
            print(f"{Colors.YELLOW}3dwork-klipper ya existe en {target_dir}{Colors.NC}")
            if get_yes_no("¿Actualizar?", "y"):
                subprocess.run(["git", "pull", "origin", "dev"], cwd=target_dir)
                print(f"{Colors.GREEN}✓{Colors.NC} Actualizado")
            return

        print(f"Clonando en {target_dir}...")
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
            )
            print(f"{Colors.GREEN}✓{Colors.NC} Instalación completa")
            print(f"\nAhora incluye el wizard en tu printer.cfg:")
            print(f"  [include {target_dir}/mainsail.cfg]")
        except Exception as e:
            print(f"{Colors.RED}Error:{Colors.NC} {e}")

    @staticmethod
    def update(printer_config_dir: Path):
        target_dir = printer_config_dir / "3dwork-klipper"
        if not target_dir.exists():
            print(f"{Colors.RED}3dwork-klipper no está instalado{Colors.NC}")
            return

        print(f"{Colors.BLUE}Actualizando 3dwork-klipper...{Colors.NC}")
        try:
            subprocess.run(["git", "fetch", "origin"], cwd=target_dir, check=True)
            subprocess.run(["git", "checkout", "dev"], cwd=target_dir, check=True)
            subprocess.run(["git", "pull", "origin", "dev"], cwd=target_dir, check=True)
            print(f"{Colors.GREEN}✓{Colors.NC} Actualizado a la última versión")
        except Exception as e:
            print(f"{Colors.RED}Error:{Colors.NC} {e}")


class WizardState:
    """Persist wizard state"""

    STATE_FILE = Path.home() / ".3dwork-klipper-wizard" / "state.json"

    @classmethod
    def load(cls) -> Dict:
        if cls.STATE_FILE.exists():
            try:
                return json.loads(cls.STATE_FILE.read_text())
            except:
                pass
        return {"board": None, "printer": {}, "features": {}}

    @classmethod
    def save(cls, state: Dict):
        cls.STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        cls.STATE_FILE.write_text(json.dumps(state, indent=2))


class Wizard:
    """Main wizard orchestrator"""

    def __init__(self):
        self.home = Path.home()
        self.printer_config = self.home / "printer_data" / "config"
        self.klipper_dir = self.printer_config / "3dwork-klipper"

        self.board_manager = BoardManager()
        self.config_generator = ConfigGenerator(str(Path(__file__).parent.parent))
        self.config_library = ConfigLibrary()
        self.firmware_compiler = FirmwareCompiler()
        self.web_wizard = WebWizard()

        self.state = WizardState.load()

    def run(self):
        while True:
            clear_screen()
            print_header()

            # Check installation
            if not self.klipper_dir.exists():
                print(f"{Colors.YELLOW}⚠️  3Dwork-klipper no instalado{Colors.NC}")

            print_menu()

            choice = get_input("Selecciona una opción", "0")

            if choice == "0":
                print(f"\n{Colors.GREEN}¡Hasta luego! 👋{Colors.NC}")
                break
            elif choice == "1":
                self.select_board()
            elif choice == "2":
                self.configure_printer()
            elif choice == "3":
                self.generate_config()
            elif choice == "4":
                self.compile_firmware()
            elif choice == "5":
                Installer.install(self.printer_config)
            elif choice == "6":
                Installer.update(self.printer_config)
            elif choice == "7":
                self.show_config()
            elif choice == "8":
                self.config_library.list_sources()
            elif choice == "9":
                self.web_wizard.start()
            else:
                print(f"{Colors.RED}Opción inválida{Colors.NC}")

            input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.NC}")

    def select_board(self):
        self.board_manager.display()
        board_id = get_input("\nIntroduce el ID de la electrónica (ej: btt-manta-m8p)")

        board = self.board_manager.get_board(board_id)
        if board:
            self.state["board"] = board
            WizardState.save(self.state)
            print(f"\n{Colors.GREEN}✓{Colors.NC} Seleccionada: {board['name']}")
            print(f"  MCU: {board['mcu']}")
            print(f"  CAN: {'Sí' if board.get('can') else 'No'}")
        else:
            print(f"{Colors.RED}Electrónica no encontrada{Colors.NC}")

    def configure_printer(self):
        print(f"\n{Colors.BOLD}CONFIGURACIÓN DE IMPRESORA{Colors.NC}")

        printer = {}
        printer["name"] = get_input("Nombre de la impresora", "My Printer")

        # Kinematics
        kin_types = ["Cartesian", "CoreXY", "CoreXY (UART)", "Delta"]
        kin_choice = get_choice("Tipo de kinematics:", kin_types, 1)
        printer["kinematics"] = ["cartesian", "corexy", "corexy_uart", "delta"][
            kin_choice - 1
        ]

        # Speeds
        printer["max_velocity"] = int(get_input("Velocidad máxima (mm/s)", "300"))
        printer["max_accel"] = int(get_input("Aceleración máxima (mm/s²)", "3000"))

        # Rotation distances
        printer["x_rotation_distance"] = float(
            get_input("X rotation distance (mm)", "40")
        )
        printer["y_rotation_distance"] = float(
            get_input("Y rotation distance (mm)", "40")
        )
        printer["z_rotation_distance"] = float(
            get_input("Z rotation distance (mm)", "8")
        )

        printer["microsteps"] = int(get_input("Microsteps", "16"))

        # Features
        features = {}
        print(f"\n{Colors.CYAN}Características:{Colors.NC}")

        if get_yes_no("¿BLTouch o sensor de nivelación?", "n"):
            features["probe_type"] = "bltouch"
            features["probe_pin"] = get_input("Pin del probe", "PC15")

        display_types = ["Ninguno", "ST7920", "SSD1306 (I2C)", "HD44780"]
        disp_choice = get_choice("Tipo de display:", display_types, 1)
        if disp_choice > 1:
            features["display_type"] = ["st7920", "ssd1306", "hd44780"][disp_choice - 2]

        if get_yes_no("¿Ventilador de pieza?", "n"):
            features["has_fan"] = True
            features["part_fan_pin"] = get_input("Pin del ventilador", "PC9")

        self.state["printer"] = printer
        self.state["features"] = features
        WizardState.save(self.state)

        print(f"\n{Colors.GREEN}✓{Colors.NC} Configuración guardada")

    def generate_config(self):
        if not self.state.get("board"):
            print(f"{Colors.RED}⚠️  Selecciona una electrónica primero{Colors.NC}")
            return

        config = self.config_generator.generate(
            self.state["board"],
            self.state.get("printer", {}),
            self.state.get("features", {}),
        )

        output_file = self.printer_config / "printer.cfg"

        print(f"\n{Colors.BLUE}Generando printer.cfg...{Colors.NC}")
        print(f"Tamaño: ~{len(config)} caracteres")

        if get_yes_no(f"¿Guardar en {output_file}?", "y"):
            with open(output_file, "w") as f:
                f.write(config)
            print(f"{Colors.GREEN}✓{Colors.NC} Guardado en {output_file}")
        else:
            preview = config[:800]
            print(f"\n{Colors.CYAN}Vista previa:{Colors.NC}")
            print(preview)
            print("...")

    def compile_firmware(self):
        if not self.state.get("board"):
            print(f"{Colors.RED}⚠️  Selecciona una electrónica primero{Colors.NC}")
            return

        self.firmware_compiler.compile(self.state["board"])

    def show_config(self):
        print(f"\n{Colors.BOLD}CONFIGURACIÓN ACTUAL{Colors.NC}")

        board = self.state.get("board")
        printer = self.state.get("printer", {})
        features = self.state.get("features", {})

        if board:
            print(
                f"  {Colors.CYAN}Electrónica:{Colors.NC} {board['name']} ({board['id']})"
            )
            print(f"  {Colors.CYAN}MCU:{Colors.NC} {board['mcu']}")
        else:
            print(f"  {Colors.YELLOW}Electrónica: No seleccionada{Colors.NC}")

        if printer:
            print(f"  {Colors.CYAN}Impresora:{Colors.NC} {printer.get('name', 'N/A')}")
            print(
                f"  {Colors.CYAN}Kinematics:{Colors.NC} {printer.get('kinematics', 'N/A')}"
            )
        else:
            print(f"  {Colors.YELLOW}Impresora: No configurada{Colors.NC}")

        if features:
            print(f"  {Colors.CYAN}Features:{Colors.NC}")
            for k, v in features.items():
                print(f"    - {k}: {v}")


def main():
    wizard = Wizard()
    wizard.run()


if __name__ == "__main__":
    main()
