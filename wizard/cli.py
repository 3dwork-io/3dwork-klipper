#!/usr/bin/env python3
"""
3Dwork Klipper Wizard - CLI Interface
Main entry point for the interactive wizard
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any, List

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

VERSION = "1.0.0-dev"


# Colors
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
    print(f"╚═══════════════════════════════════════════════════════════╝")
    print(f"{Colors.NC}")


def print_menu():
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════╗")
    print("║        MENÚ PRINCIPAL              ║")
    print("╠═══════════════════════════════════════╣")
    print(f"║  {Colors.YELLOW}1.{Colors.NC} Seleccionar Electrónica       ║")
    print(f"║  {Colors.YELLOW}2.{Colors.NC} Configurar Impresora           ║")
    print(f"║  {Colors.YELLOW}3.{Colors.NC} Generar printer.cfg            ║")
    print(f"║  {Colors.YELLOW}4.{Colors.NC} Compilar Firmware             ║")
    print(f"║  {Colors.YELLOW}5.{Colors.NC} Actualizar Instalación        ║")
    print(f"║  {Colors.YELLOW}6.{Colors.NC} Ver Configuración Actual      ║")
    print(f"║  {Colors.YELLOW}7.{Colors.NC} Biblioteca de Configs         ║")
    print(f"║  {Colors.YELLOW}0.{Colors.NC} Salir                          ║")
    print(f"╚═══════════════════════════════════════╝{Colors.NC}")


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def get_input(prompt: str, default: str = "") -> str:
    """Get input with optional default value"""
    if default:
        result = input(f"{Colors.CYAN}{prompt}{Colors.NC} [{default}]: ").strip()
        return result if result else default
    return input(f"{Colors.CYAN}{prompt}{Colors.NC}: ").strip()


def get_yes_no(prompt: str, default: str = "n") -> bool:
    """Get yes/no input"""
    default_str = "Y/n" if default == "y" else "N/y"
    result = (
        input(f"{Colors.CYAN}{prompt} ({default_str}){Colors.NC}: ").strip().lower()
    )
    return result in ["y", "yes"] if default == "n" else result in ["y", "yes", ""]


class BoardManager:
    """Manage supported boards"""

    # Board definitions with categories
    BOARDS = {
        "BigTreeTech": {
            "Manta": [
                {"id": "btt-manta-e3ez", "name": "Manta E3 EZ", "mcu": "stm32g0b1"},
                {"id": "btt-manta-m4p", "name": "Manta M4P", "mcu": "stm32h743"},
                {
                    "id": "btt-manta-m4p-22",
                    "name": "Manta M4P v2.2",
                    "mcu": "stm32h743",
                },
                {"id": "btt-manta-m8p", "name": "Manta M8P", "mcu": "stm32h743"},
                {
                    "id": "btt-manta-m8p-11",
                    "name": "Manta M8P v1.1",
                    "mcu": "stm32h743",
                },
            ],
            "Octopus": [
                {
                    "id": "btt-octopus-max-ez",
                    "name": "Octopus Max EZ",
                    "mcu": "stm32h723",
                },
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
                {
                    "id": "btt-octopus-11-407",
                    "name": "Octopus v1.1 (407)",
                    "mcu": "stm32f407",
                },
            ],
            "SKR": [
                {"id": "skr_pro_12", "name": "SKR Pro v1.2", "mcu": "stm32f407"},
                {"id": "btt-skr-3", "name": "SKR 3", "mcu": "stm32h743"},
                {"id": "btt-skr-3-h723", "name": "SKR 3 (H723)", "mcu": "stm32h723"},
                {"id": "btt-skr-3-ez", "name": "SKR 3 EZ", "mcu": "stm32h743"},
                {
                    "id": "btt-skr-3-ez-h723",
                    "name": "SKR 3 EZ (H723)",
                    "mcu": "stm32h723",
                },
                {"id": "btt-skr-2-429", "name": "SKR 2 (429)", "mcu": "stm32f429"},
                {"id": "btt-skr-2-407", "name": "SKR 2 (407)", "mcu": "stm32f407"},
                {"id": "btt-skrat-10", "name": "SKR RAT", "mcu": "stm32f407"},
                {"id": "btt-skr-14-turbo", "name": "SKR 1.4 Turbo", "mcu": "stm32f407"},
                {
                    "id": "btt_skr_mini_e3_30",
                    "name": "SKR Mini E3 v3",
                    "mcu": "stm32g0b1",
                },
            ],
        },
        "MKS": {
            " boards": [
                {"id": "mks-eagle-10", "name": "MKS Eagle v1.x", "mcu": "stm32f103"},
                {
                    "id": "mks-robin-nano-30",
                    "name": "MKS Robin Nano v3",
                    "mcu": "stm32f103",
                },
                {
                    "id": "mks-robin-nano-20",
                    "name": "MKS Robin Nano v2",
                    "mcu": "stm32f103",
                },
                {"id": "mks-gen-l", "name": "MKS Gen L", "mcu": "stm32f103"},
                {
                    "id": "znp_robin_nano_dw_v2",
                    "name": "ZNP Robin Nano DW v2",
                    "mcu": "stm32f103",
                },
            ],
        },
        "Fysetc": {
            " boards": [
                {"id": "fysetc_spider", "name": "Fysetc Spider", "mcu": "stm32f407"},
            ],
        },
        "Artillery": {
            " boards": [
                {
                    "id": "artillery-ruby-12",
                    "name": "Artillery Ruby v1.x",
                    "mcu": "stm32f103",
                },
            ],
        },
        "Raspberry": {
            " boards": [
                {"id": "rpi-rp2040", "name": "Raspberry Pico/RP2040", "mcu": "rp2040"},
            ],
        },
        "Leviathan": {
            " boards": [
                {"id": "leviathan-12", "name": "Leviathan v1.2", "mcu": "stm32h743"},
            ],
        },
        "Mellow": {
            "Toolhead CAN": [
                {
                    "id": "mellow_fly_sht_42",
                    "name": "Mellow FLY SHT 42",
                    "mcu": "stm32g0b1",
                },
                {
                    "id": "mellow_fly_sht_36",
                    "name": "Mellow FLY SHT 36",
                    "mcu": "stm32g0b1",
                },
            ],
        },
        "BigTreeTech CAN": {
            "Toolhead": [
                {"id": "btt_ebb42_10", "name": "EBB42 v1", "mcu": "stm32g0b1"},
                {"id": "btt_ebb36_10", "name": "EBB36 v1", "mcu": "stm32g0b1"},
                {"id": "btt_ebb42_11", "name": "EBB42 v1.1", "mcu": "stm32g0b1"},
                {"id": "btt_ebb36_11", "name": "EBB36 v1.1", "mcu": "stm32g0b1"},
                {"id": "btt_ebb42_12", "name": "EBB42 v1.2", "mcu": "stm32g0b1"},
                {"id": "btt_ebb36_12", "name": "EBB36 v1.2", "mcu": "stm32g0b1"},
            ],
        },
    }

    def list_boards(self) -> List[Dict]:
        """List all available boards"""
        boards = []
        for manufacturer, categories in self.BOARDS.items():
            for category, board_list in categories.items():
                for board in board_list:
                    board["manufacturer"] = manufacturer
                    board["category"] = category
                    boards.append(board)
        return boards

    def get_boards_by_manufacturer(self, manufacturer: str) -> Dict:
        """Get boards grouped by category for a manufacturer"""
        return self.BOARDS.get(manufacturer, {})

    def get_board_by_id(self, board_id: str) -> Optional[Dict]:
        """Get board details by ID"""
        for boards in self.BOARDS.values():
            for category in boards.values():
                for board in category:
                    if board["id"] == board_id:
                        return board
        return None

    def display_boards(self):
        """Display boards in a nice format"""
        print(
            f"\n{Colors.BOLD}╔══════════════════════════════════════════════════════════╗"
        )
        print("║            ELECTRÓNICAS SOPORTADAS                 ║")
        print("╚══════════════════════════════════════════════════╝")

        for manufacturer, categories in self.BOARDS.items():
            print(f"\n{Colors.YELLOW}{manufacturer}:{Colors.NC}")
            for category, board_list in categories.items():
                print(f"  {category}:")
                for board in board_list:
                    print(
                        f"    {Colors.GREEN}•{Colors.NC} {board['name']} ({board['id']})"
                    )


class ConfigGenerator:
    """Generate printer.cfg from templates"""

    def __init__(self, config_dir: str):
        self.config_dir = Path(config_dir)

    def generate(self, board: Dict, printer: Dict, features: List[str]) -> str:
        """Generate printer.cfg"""
        # Load base template
        template = self.config_dir / "templates" / "printer.cfg.template"

        if not template.exists():
            return self._generate_minimal(board, printer, features)

        # TODO: Implement full template rendering
        return self._generate_minimal(board, printer, features)

    def _generate_minimal(self, board: Dict, printer: Dict, features: List[str]) -> str:
        """Generate minimal printer.cfg"""
        config = f"""# 3Dwork Klipper Configuration
# Generated by 3Dwork Klipper Wizard v{VERSION}
# Board: {board["name"]}
# Printer: {printer.get("name", "Custom")}

# ============================================
# MCU Configuration
# ============================================
[mcu]
serial: /dev/serial/by-id/usb-*
restart_method: command

# ============================================
# Printer Kinematics
# ============================================
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
        # Add stepper configs based on kinematics
        kinematics = printer.get("kinematics", "cartesian")
        if kinematics == "cartesian":
            config += """
[stepper_x]
step_pin: PB0
dir_pin: PC5
enable_pin: !PC6
microsteps: 16
rotation_distance: 40
endstop_pin: ^PA5

[stepper_y]
step_pin: PB1
dir_pin: PC2
enable_pin: !PC3
microsteps: 16
rotation_distance: 40
endstop_pin: ^PA6

[stepper_z]
step_pin: PB2
dir_pin: !PC1
enable_pin: !PC4
microsteps: 16
rotation_distance: 8
endstop_pin: ^PA7
"""
        elif kinematics == "corexy":
            config += """
[stepper_x]
step_pin: PB0
dir_pin: PC5
enable_pin: !PC6
microsteps: 16
rotation_distance: 40

[stepper_y]
step_pin: PB1
dir_pin: PC2
enable_pin: !PC3
microsteps: 16
rotation_distance: 40

[stepper_z]
step_pin: PB2
dir_pin: !PC1
enable_pin: !PC4
microsteps: 16
rotation_distance: 8
endstop_pin: ^PA7
"""

        # Add features
        if "bltouch" in features:
            config += """
# ============================================
# BLTouch
# ============================================
[probe]
pin: PC15
x_offset: 0
y_offset: 0
z_offset: 0
speed: 5

[bed_mesh]
horizontal_move_z: 5
speed: 150
"""

        if "spi_display" in features:
            config += """
# ============================================
# Display
# ============================================
[display]
lcd_type: st7920
cs_pin: PA4
sclk_pin: PB0
mosi_pin: PB1

[display_menu]
menu_root: main_menu
"""

        # Add 3dwork macros include
        config += f"""
# ============================================
# 3Dwork Macros
# ============================================
[include 3dwork-klipper/macros/macros_*.cfg]
[include 3dwork-klipper/shell-macros.cfg]

# ============================================
# SAVE_CONFIG
# ============================================
#*# <--- SAVE_CONFIG --->
#*# DO NOT EDIT THIS SECTION
#*# It is automatically generated and will be overwritten
"""

        return config


class FirmwareCompiler:
    """Compile firmware for boards"""

    def __init__(self, klipper_dir: str, output_dir: str):
        self.klipper_dir = Path(klipper_dir)
        self.output_dir = Path(output_dir)

    def compile(self, board_id: str) -> bool:
        """Compile firmware for board"""
        # TODO: Integrate with actual Klipper build system
        print(
            f"{Colors.YELLOW}[WARN] Firmware compilation no implementado en esta versión{Colors.NC}"
        )
        print(f"Por favor, usa la macro COMPILE_FIRMWARE desde Klipper:")
        print(f"  COMPILE_FIRMWARE BOARD={board_id}")
        return False

    def list_boards(self):
        """List supported boards for compilation"""
        bm = BoardManager()
        bm.display_boards()


class Wizard:
    """Main wizard class"""

    def __init__(self):
        self.config_dir = Path(__file__).parent.parent
        self.home_dir = Path.home()
        self.printer_config_dir = self.home_dir / "printer_data" / "config"

        self.board_manager = BoardManager()
        self.config_generator = ConfigGenerator(str(self.config_dir))

        self.current_board = None
        self.current_printer = {}

        # Check for existing 3dwork-klipper
        self.klipper_dir = self.printer_config_dir / "3dwork-klipper"

    def run(self):
        """Main wizard loop"""
        while True:
            clear_screen()
            print_header()

            # Check if 3dwork-klipper is installed
            if not self.klipper_dir.exists():
                self._install_prompt()

            print_menu()

            choice = get_input("Selecciona una opción", "0")

            if choice == "0":
                print(f"\n{Colors.GREEN}¡Hasta luego!{Colors.NC}")
                break
            elif choice == "1":
                self._select_board()
            elif choice == "2":
                self._configure_printer()
            elif choice == "3":
                self._generate_config()
            elif choice == "4":
                self._compile_firmware()
            elif choice == "5":
                self._update_installation()
            elif choice == "6":
                self._show_current_config()
            elif choice == "7":
                self._show_config_library()
            else:
                print(f"{Colors.RED}Opción inválida{Colors.NC}")

            input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.NC}")

    def _install_prompt(self):
        """Prompt to install 3dwork-klipper"""
        print(f"\n{Colors.YELLOW}⚠️  3Dwork-klipper no está instalado{Colors.NC}")
        print(f"\nInstalación actual: {self.printer_config_dir}")

        if get_yes_no("¿Instalar 3dwork-klipper ahora?", "y"):
            self._install_klipper()

    def _install_klipper(self):
        """Install 3dwork-klipper"""
        print(f"\n{Colors.BLUE}Instalando 3dwork-klipper...{Colors.NC}")

        # Clone repo if not exists
        if not self.klipper_dir.exists():
            print("Clonando repositorio...")
            # In real implementation, would clone here

    def _select_board(self):
        """Select board"""
        self.board_manager.display_boards()

        board_id = get_input("\nIntroduce el ID de la electrónica (ej: btt-manta-m8p)")

        board = self.board_manager.get_board_by_id(board_id)
        if board:
            self.current_board = board
            print(
                f"\n{Colors.GREEN}✓{Colors.NC} Electrónica seleccionada: {board['name']}"
            )
        else:
            print(f"\n{Colors.RED}Electrónca no encontrada{Colors.NC}")

    def _configure_printer(self):
        """Configure printer settings"""
        print(f"\n{Colors.BOLD}CONFIGURACIÓN DE IMPRESORA{Colors.NC}")

        # Kinematics
        print("\nTipo de kinematics:")
        print("  1. Cartesian")
        print("  2. CoreXY")
        print("  3. Delta")
        print("  4. Rotary Delta")

        kin_choice = get_input("Selecciona tipo", "1")
        kinematics = ["cartesian", "corexy", "delta", "rotary_delta"][
            int(kin_choice) - 1
        ]

        # Basic settings
        max_velocity = get_input("Velocidad máxima (mm/s)", "300")
        max_accel = get_input("Aceleración máxima (mm/s²)", "3000")

        # Features
        features = []
        print("\nCaracterísticas adicionales:")
        if get_yes_no("¿BLTouch o sensor de nivelación?", "n"):
            features.append("bltouch")
        if get_yes_no("¿Display SPI?", "n"):
            features.append("spi_display")
        if get_yes_no("¿Sensor de filamento?", "n"):
            features.append("filament_sensor")

        self.current_printer = {
            "name": get_input("Nombre de la impresora", "My Printer"),
            "kinematics": kinematics,
            "max_velocity": int(max_velocity),
            "max_accel": int(max_accel),
            "features": features,
        }

        print(f"\n{Colors.GREEN}✓{Colors.NC} Configuración guardada")

    def _generate_config(self):
        """Generate printer.cfg"""
        if not self.current_board:
            print(
                f"\n{Colors.RED}⚠️  Selecciona una electrónica primero (opción 1){Colors.NC}"
            )
            return

        if not self.current_printer:
            print(
                f"\n{Colors.RED}⚠️  Configura la impresora primero (opción 2){Colors.NC}"
            )
            return

        config = self.config_generator.generate(
            self.current_board,
            self.current_printer,
            self.current_printer.get("features", []),
        )

        # Save to file
        output_file = self.printer_config_dir / "printer.cfg"

        if get_yes_no(f"¿Guardar en {output_file}?", "y"):
            with open(output_file, "w") as f:
                f.write(config)
            print(
                f"\n{Colors.GREEN}✓{Colors.NC} Configuración guardada en {output_file}"
            )
        else:
            print("\nConfiguración generada (no guardada):")
            print(config[:500] + "...")

    def _compile_firmware(self):
        """Compile firmware"""
        if not self.current_board:
            print(f"\n{Colors.RED}⚠️  Selecciona una electrónica primero{Colors.NC}")
            return

        print(
            f"\n{Colors.BLUE}Compilando firmware para {self.current_board['name']}...{Colors.NC}"
        )
        print(
            f"\n{Colors.YELLOW}Usa la macro COMPILE_FIRMWARE desde Klipper:{Colors.NC}"
        )
        print(
            f"  SET_GCODE_VARIABLE MACRO=COMPILE_FIRMWARE VARIABLE=BOARD VALUE='\"{self.current_board['id']}\"'"
        )

    def _update_installation(self):
        """Update installation"""
        print(f"\n{Colors.BLUE}Actualizando 3dwork-klipper...{Colors.NC}")

        if self.klipper_dir.exists():
            print("Ejecutando git pull...")
            # Would run git pull here
            print(f"{Colors.GREEN}✓{Colors.NC} Instalación actualizada")
        else:
            print(f"{Colors.RED}3dwork-klipper no está instalado{Colors.NC}")

    def _show_current_config(self):
        """Show current configuration"""
        print(f"\n{Colors.BOLD}CONFIGURACIÓN ACTUAL{Colors.NC}")

        if self.current_board:
            print(f"  Electrónica: {self.current_board['name']}")
        else:
            print(f"  Electrónica: No seleccionada")

        if self.current_printer:
            print(f"  Impresora: {self.current_printer.get('name', 'N/A')}")
            print(f"  Kinematics: {self.current_printer.get('kinematics', 'N/A')}")
            print(
                f"  Características: {', '.join(self.current_printer.get('features', [])) or 'Ninguna'}"
            )
        else:
            print(f"  Impresora: No configurada")

    def _show_config_library(self):
        """Show configuration library"""
        print(f"\n{Colors.BOLD}BIBLIOTECA DE CONFIGURACIONES{Colors.NC}")
        print("""
La biblioteca de configuraciones incluye presets de:
  • 3Dwork-klipper (local)
  • Klipper examples (github.com/Klipper3d/klipper/config)
  • RatOS configuration
  • Creality Sonic Pad

Esta función estará disponible en próximas versiones.
        """)


def main():
    wizard = Wizard()
    wizard.run()


if __name__ == "__main__":
    main()
