"""Pines reales de cada placa.

Fuente: boards/<id>/config.cfg, seccion [board_pins ...] con el diccionario
`aliases:` (x_step_pin=PF13, e_heater_pin=PA2...). Es el mismo estilo que usa
RatOS/Voron: el printer.cfg referencia los alias en vez de pines crudos, asi
que sirve para cualquier placa que tenga config.cfg sin datos por placa en
el wizard.
"""

import json
import re
from pathlib import Path


def boards_dir() -> Path:
    return Path(__file__).parent.parent / "boards"


def is_toolboard(board_id: str) -> bool:
    """True si la placa es un toolboard (no puede ser la MCU principal)."""
    p = boards_dir() / board_id / "board-definition.json"
    if not p.exists():
        return False
    try:
        return bool(json.loads(p.read_text()).get("isToolboard"))
    except Exception:
        return False


def has_pin_aliases(board_id: str) -> bool:
    return (boards_dir() / board_id / "config.cfg").exists()


def alias_pins(board_id: str) -> dict:
    """Devuelve {nombre: valor} de la seccion [board_pins] de la placa.

    El bloque de aliases contiene lineas en blanco y comentarios intermedios,
    asi que se lee hasta la siguiente seccion real (linea que empieza por [).
    """
    p = boards_dir() / board_id / "config.cfg"
    if not p.exists():
        return {}
    pins = {}
    in_aliases = False
    for raw in p.read_text().splitlines():
        line = raw.strip()
        if not in_aliases:
            if line.startswith("[board_pins"):
                in_aliases = True
            continue
        if line.startswith("[") and "]" in line:
            break  # siguiente seccion: fin del bloque
        line = line.split("#", 1)[0]
        for item in line.split(","):
            item = item.strip()
            if not item or "=" not in item:
                continue
            k, v = item.split("=", 1)
            pins[k.strip()] = v.strip()
    return pins


# Alias con nombres alternativos por placa (Prusa usa el prefijo p_).
ALIAS_FALLBACKS = {
    "fan_part_cooling_pin": [
        "fan_part_cooling_pin",
        "p_fan_part_cooling_pin",
        "4p_fan_part_cooling_pin",
    ],
}


def resolve(pins: dict, name: str) -> str:
    for candidate in ALIAS_FALLBACKS.get(name, [name]):
        if pins.get(candidate, "null") != "null":
            return pins[candidate]
    return ""


def required_aliases() -> list:
    """Alias que el printer.cfg generado necesita para una MCU principal."""
    return [
        "x_step_pin", "x_dir_pin", "x_enable_pin", "x_endstop_pin",
        "y_step_pin", "y_dir_pin", "y_enable_pin", "y_endstop_pin",
        "z0_step_pin", "z0_dir_pin", "z0_enable_pin",
        "e_step_pin", "e_dir_pin", "e_enable_pin",
        "e_heater_pin", "e_sensor_pin",
        "heater_bed_heating_pin", "heater_bed_sensor_pin",
        "fan_part_cooling_pin",
    ]


def board_ready(board_id: str):
    """Devuelve (ok, motivo). ok=False -> no se puede generar printer.cfg."""
    if is_toolboard(board_id):
        return False, (
            f"{board_id} es un toolboard: no puede ser la MCU principal. "
            "Elige la placa controladora de la impresora."
        )
    pins = alias_pins(board_id)
    if not pins:
        return False, (
            f"La placa {board_id} no tiene boards/{board_id}/config.cfg con la "
            "seccion [board_pins]: el wizard no puede inventarse los pines."
        )
    missing = [a for a in required_aliases() if not resolve(pins, a)]
    if missing:
        return False, (
            f" boards/{board_id}/config.cfg no define: {', '.join(missing)}. "
            "Consultael diagrama de pines de la placa."
        )
    return True, ""
