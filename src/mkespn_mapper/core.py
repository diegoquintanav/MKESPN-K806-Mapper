import json
import os
import subprocess
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, Final, Optional

MOD_MAP = {
    "CTRL": "ctrl",
    "CONTROL": "ctrl",
    "ALT": "alt",
    "SHIFT": "shift",
    "SUPER": "super",
    "META": "super",
    "WIN": "super",
}
KEYSYM_MAP = {
    "TAB": "Tab",
    "RETURN": "Return",
    "ENTER": "Return",
    "ESC": "Escape",
    "ESCAPE": "Escape",
    "SPACE": "space",
}
for i in range(1, 25):
    KEYSYM_MAP[f"F{i}"] = f"F{i}"


class ActionKind(str, Enum):
    COMMAND = "command"
    COMBO = "combo"


@dataclass
class Action:
    kind: ActionKind
    value: str


@dataclass
class Profile:
    device_path: str = ""
    enabled: bool = True
    mapping: Optional[Dict[int, Action]] = None

    @staticmethod
    def from_json(d: dict) -> "Profile":
        path = d.get("device_path", "")
        enabled = d.get("enabled", True)
        mapping = {}
        for k, v in d.get("mapping", {}).items():
            mapping[int(k)] = Action(v["kind"], v["value"])
        return Profile(path, enabled, mapping)

    @property
    def absolute_device_path(self) -> Optional[str]:
        """Resolve symlinks like /dev/input/by-id/... to the actual event device."""
        if self.device_path.startswith("/dev/input/by-id/"):
            real_path = os.path.realpath(self.device_path)
            if os.path.exists(real_path):
                return real_path
            else:
                print(f"[DAEMON] by-id symlink not valid: {self.device_path}")
                return None
        elif os.path.exists(self.device_path):
            return self.device_path
        else:
            return None


def combo_to_xdotool(combo: str) -> str:
    """Convert a combo string like "CTRL+ALT+T" to xdotool format."""
    parts = [p.strip() for p in combo.replace("-", "+").split("+") if p.strip()]
    out = []
    for p in parts:
        u = p.upper()
        if u in MOD_MAP:
            out.append(MOD_MAP[u])
        elif len(p) == 1 and p.isalnum():
            out.append(p.lower())
        elif u in KEYSYM_MAP:
            out.append(KEYSYM_MAP[u])
        else:
            out.append(p)
    return "+".join(out)


def execute_action(act: Action):
    try:
        if act.kind == ActionKind.COMMAND:
            subprocess.Popen(act.value, shell=True)
            print(f"[DAEMON] Run: {act.value}")
        elif act.kind == ActionKind.COMBO:
            seq = combo_to_xdotool(act.value)
            subprocess.Popen(["xdotool", "key", seq])
            print(f"[DAEMON] Combo: {act.value}")
    except Exception as e:
        print(f"[ERROR] {e}")
