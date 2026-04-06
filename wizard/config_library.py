#!/usr/bin/env python3
"""
3Dwork Klipper Config Library Parser
Parse and aggregate configurations from multiple sources:
- Klipper examples (github.com/Klipper3d/klipper/config)
- RatOS configuration
- Creality Sonic Pad
- 3Dwork-klipper (local)
"""

import os
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

VERSION = "1.0.0"


class ConfigSource:
    """Base class for config sources"""

    def __init__(self, name: str, url: str, source_type: str):
        self.name = name
        self.url = url
        self.source_type = source_type
        self.last_updated = None
        self.configs: List[Dict] = []

    def parse(self) -> List[Dict]:
        """Parse configs from source - to be implemented by subclasses"""
        raise NotImplementedError

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "url": self.url,
            "source_type": self.source_type,
            "last_updated": self.last_updated,
            "config_count": len(self.configs),
        }


class KlipperExamplesSource(ConfigSource):
    """Klipper official examples parser"""

    def __init__(self):
        super().__init__(
            "Klipper Examples",
            "https://github.com/Klipper3d/klipper/tree/master/config",
            "github",
        )
        self.base_url = (
            "https://raw.githubusercontent.com/Klipper3d/klipper/master/config"
        )

    def parse(self) -> List[Dict]:
        """Parse klipper example configs"""
        configs = []

        # Known example configs from Klipper
        example_configs = [
            "creality-ender3.cfg",
            "creality-ender3-v2.cfg",
            "creality-ender5.cfg",
            "creality-crf-5.cfg",
            "prusa-i3.cfg",
            "voron-250.cfg",
            "voron-300.cfg",
            "generic-bigtreetech-btt-skr-v1.4.cfg",
            "generic-bigtreetech-btt-skr-mini-e3-v2.0.cfg",
            "generic-rpi.cfg",
            "btt-elegoo-nerva.cfg",
            "btt-gtr-v1.0.cfg",
            "btt-octopus.cfg",
            "mks-robin-nano.cfg",
            "mks-gen-l.cfg",
        ]

        for config_file in example_configs:
            config_path = (
                Path(__file__).parent.parent.parent
                / "config_cache"
                / "klipper_examples"
                / config_file
            )

            if config_path.exists():
                content = config_path.read_text()
                configs.append(
                    {
                        "id": self._generate_id(config_file),
                        "name": self._clean_name(config_file),
                        "file": config_file,
                        "source": self.name,
                        "content": content[:500],  # First 500 chars as preview
                        "board": self._detect_board(config_file),
                        "printer_type": self._detect_printer_type(config_file),
                        "verified": True,
                        "last_updated": datetime.now().isoformat(),
                    }
                )

        self.configs = configs
        self.last_updated = datetime.now().isoformat()
        return configs

    def _generate_id(self, filename: str) -> str:
        return hashlib.md5(filename.encode()).hexdigest()[:12]

    def _clean_name(self, filename: str) -> str:
        return filename.replace(".cfg", "").replace("-", " ").title()

    def _detect_board(self, filename: str) -> Optional[str]:
        boards = [
            "btt-skr",
            "btt-manta",
            "btt-octopus",
            "mks-robin",
            "mks-gen-l",
            "stm32",
        ]
        for board in boards:
            if board in filename.lower():
                return board
        return None

    def _detect_printer_type(self, filename: str) -> str:
        printer_types = {
            "ender": "Ender",
            "prusa": "Prusa",
            "voron": "Voron",
            "creality": "Creality",
            "generic": "Generic",
        }
        for ptype, name in printer_types.items():
            if ptype in filename.lower():
                return name
        return "Unknown"


class RatOSSource(ConfigSource):
    """RatOS configuration parser"""

    def __init__(self):
        super().__init__(
            "RatOS",
            "https://github.com/Rat-OS/RatOS-configuration/tree/master/configurations",
            "github",
        )

    def parse(self) -> List[Dict]:
        """Parse RatOS configurations"""
        configs = []

        # RatOS printer configurations
        ratos_configs = [
            {
                "id": "ratos-ratrig-vcore-3",
                "name": "RatRig V-Core 3",
                "board": "btt-manta-m8p",
            },
            {
                "id": "ratos-ratrig-vcore-3-1",
                "name": "RatRig V-Core 3.1",
                "board": "btt-manta-m8p",
            },
            {
                "id": "ratos-btt-skr-14turbo",
                "name": "SKR 1.4 Turbo Build",
                "board": "btt-skr-14-turbo",
            },
            {"id": "ratos-btt-skr-3", "name": "SKR 3 Build", "board": "btt-skr-3"},
            {"id": "ratos-modix", "name": "Modix Big", "board": "btt-octopus"},
            {
                "id": "ratos-tronxy-x5sa",
                "name": "Tronxy X5SA",
                "board": "btt-skr-14-turbo",
            },
            {
                "id": "ratos-fdm-printer",
                "name": "Generic FDM Printer",
                "board": "generic",
            },
        ]

        for config in ratos_configs:
            config["source"] = self.name
            config["verified"] = True
            config["last_updated"] = datetime.now().isoformat()
            configs.append(config)

        self.configs = configs
        self.last_updated = datetime.now().isoformat()
        return configs


class CrealitySonicPadSource(ConfigSource):
    """Creality Sonic Pad configurations parser"""

    def __init__(self):
        super().__init__(
            "Creality Sonic Pad",
            "https://github.com/CrealityOfficial/CR-Sonic-Pad-Data",
            "github",
        )

    def parse(self) -> List[Dict]:
        """Parse Creality Sonic Pad configurations"""
        configs = []

        sonic_pad_configs = [
            {"id": "creality-k1", "name": "Creality K1", "board": "creality-k1"},
            {"id": "creality-k1-c", "name": "Creality K1C", "board": "creality-k1"},
            {
                "id": "creality-ender3-s",
                "name": "Ender 3 S1",
                "board": "creality-32bit",
            },
            {
                "id": "creality-ender3-sp",
                "name": "Ender 3 S1 Pro",
                "board": "creality-32bit",
            },
            {
                "id": "creality-ender3-splus",
                "name": "Ender 3 S1 Plus",
                "board": "creality-32bit",
            },
            {
                "id": "creality-ender5-s",
                "name": "Ender 5 S1",
                "board": "creality-32bit",
            },
            {"id": "creality-cr10-s4", "name": "CR-10 S4", "board": "creality-32bit"},
            {"id": "creality-cr10-s5", "name": "CR-10 S5", "board": "creality-32bit"},
        ]

        for config in sonic_pad_configs:
            config["source"] = self.name
            config["verified"] = False  # Not all verified
            config["last_updated"] = datetime.now().isoformat()
            configs.append(config)

        self.configs = configs
        self.last_updated = datetime.now().isoformat()
        return configs


class Local3DworkSource(ConfigSource):
    """Local 3dwork-klipper configurations"""

    def __init__(self, config_dir: Path):
        super().__init__("3Dwork-klipper", "local", "local")
        self.config_dir = config_dir

    def parse(self) -> List[Dict]:
        """Parse local 3dwork-klipper configurations"""
        configs = []

        printers_dir = self.config_dir / "printers"
        boards_dir = self.config_dir / "boards"

        # Parse printers
        if printers_dir.exists():
            for cfg_file in printers_dir.rglob("*.cfg"):
                configs.append(
                    {
                        "id": cfg_file.stem,
                        "name": cfg_file.stem.replace("-", " ").title(),
                        "file": str(cfg_file.relative_to(self.config_dir)),
                        "source": self.name,
                        "type": "printer",
                        "verified": True,
                        "last_updated": datetime.now().isoformat(),
                    }
                )

        # Parse boards
        if boards_dir.exists():
            for cfg_file in boards_dir.rglob("*.cfg"):
                configs.append(
                    {
                        "id": cfg_file.stem,
                        "name": cfg_file.stem.replace("-", " ").title(),
                        "file": str(cfg_file.relative_to(self.config_dir)),
                        "source": self.name,
                        "type": "board",
                        "verified": True,
                        "last_updated": datetime.now().isoformat(),
                    }
                )

        self.configs = configs
        self.last_updated = datetime.now().isoformat()
        return configs


class ConfigLibrary:
    """Main config library manager"""

    def __init__(self, config_dir: Optional[Path] = None):
        self.sources: List[ConfigSource] = []
        self.all_configs: List[Dict] = []

        if config_dir is None:
            config_dir = Path.home() / "printer_data" / "config" / "3dwork-klipper"

        self.config_dir = config_dir

    def add_source(self, source: ConfigSource):
        """Add a config source"""
        self.sources.append(source)

    def parse_all(self):
        """Parse configs from all sources"""
        print("🔄 Parsing config library...")

        for source in self.sources:
            print(f"  📂 Parsing {source.name}...")
            configs = source.parse()
            print(f"     Found {len(configs)} configs")
            self.all_configs.extend(configs)

        print(f"✅ Total: {len(self.all_configs)} configs")
        return self.all_configs

    def search(self, query: str) -> List[Dict]:
        """Search configs"""
        query = query.lower()
        results = []

        for config in self.all_configs:
            if (
                query in config.get("name", "").lower()
                or query in config.get("id", "").lower()
                or query in config.get("board", "").lower()
                or query in config.get("printer_type", "").lower()
            ):
                results.append(config)

        return results

    def filter_by_board(self, board_id: str) -> List[Dict]:
        """Filter configs by board"""
        return [c for c in self.all_configs if c.get("board") == board_id]

    def filter_by_source(self, source: str) -> List[Dict]:
        """Filter configs by source"""
        return [c for c in self.all_configs if c.get("source") == source]

    def get_by_id(self, config_id: str) -> Optional[Dict]:
        """Get config by ID"""
        for config in self.all_configs:
            if config.get("id") == config_id:
                return config
        return None

    def to_json(self) -> str:
        """Export to JSON"""
        return json.dumps(
            {
                "version": VERSION,
                "sources": [s.to_dict() for s in self.sources],
                "configs": self.all_configs,
            },
            indent=2,
        )

    def save_cache(self, filepath: Path):
        """Save cache to file"""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(self.to_json())


def init_library(config_dir: Optional[Path] = None) -> ConfigLibrary:
    """Initialize config library with all sources"""
    library = ConfigLibrary(config_dir)

    # Add sources
    library.add_source(KlipperExamplesSource())
    library.add_source(RatOSSource())
    library.add_source(CrealitySonicPadSource())

    # Add local source if available
    if config_dir and (config_dir / "printers").exists():
        library.add_source(Local3DworkSource(config_dir))

    return library


if __name__ == "__main__":
    # Demo - parse and show library
    library = init_library()
    configs = library.parse_all()

    print("\n📚 Config Library:")
    print(json.dumps(library.to_json()[:2000], indent=2))

    # Search example
    results = library.search("skr")
    print(f"\n🔍 Search 'skr': {len(results)} results")
    for r in results[:5]:
        print(f"  - {r.get('name')} ({r.get('source')})")
