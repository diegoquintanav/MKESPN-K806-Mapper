from abc import ABC

try:
    from evdev import ecodes
except Exception as e:
    raise SystemExit(
        "Requires python3-evdev. Install: sudo apt install -y python3-evdev\n" + str(e)
    )


class DeviceMapper(ABC):
    DEVICE_NAME: str
    DEFAULT_LABELS: dict[int, str] = {}
    SUGGESTED_DEFAULTS: dict[int, tuple[str, str]] = {}


class MkespnK806(DeviceMapper):
    DEVICE_NAME = "MKESPN K806 Mini Keypad"
    # Common key codes for mini keyboards - expand this based on your device
    DEFAULT_LABELS = {
        # Standard keypad keys
        ecodes.KEY_KP1: "1",
        ecodes.KEY_KP2: "2",
        ecodes.KEY_KP3: "3",
        ecodes.KEY_KP4: "4",
        ecodes.KEY_KP5: "5",
        ecodes.KEY_KP6: "6",
        ecodes.KEY_KP7: "7",
        ecodes.KEY_KP8: "8",
    }

    SUGGESTED_DEFAULTS = {
        ecodes.KEY_KP1: ("combo", "Ctrl+Alt+T"),
        ecodes.KEY_KP2: ("combo", "Super+A"),
        ecodes.KEY_KP3: ("combo", "Super"),
        ecodes.KEY_KP4: ("combo", "Super+E"),
        ecodes.KEY_KP5: ("combo", "Super+Tab"),
        ecodes.KEY_KP6: ("combo", "Alt+Tab"),
        ecodes.KEY_KP7: ("combo", "Super+L"),
        ecodes.KEY_KP8: ("combo", "Super+H"),
    }


class MkespnK815(DeviceMapper):
    DEVICE_NAME = "MKESPN MKESPN K815 Keyboard"

    DEFAULT_LABELS = {
        # Standard keypad keys
        ecodes.KEY_KP1: "1",
        ecodes.KEY_KP2: "2",
        ecodes.KEY_KP3: "3",
        ecodes.KEY_KP4: "4",
        ecodes.KEY_KP5: "5",
        ecodes.KEY_KP6: "6",
        ecodes.KEY_KP7: "7",
        ecodes.KEY_KP8: "8",
    }

    SUGGESTED_DEFAULTS = {
        ecodes.KEY_KP1: ("combo", "Ctrl+Alt+T"),
        ecodes.KEY_KP2: ("combo", "Super+A"),
        ecodes.KEY_KP3: ("combo", "Super"),
        ecodes.KEY_KP4: ("combo", "Super+E"),
        ecodes.KEY_KP5: ("combo", "Super+Tab"),
        ecodes.KEY_KP6: ("combo", "Alt+Tab"),
        ecodes.KEY_KP7: ("combo", "Super+L"),
        ecodes.KEY_KP8: ("combo", "Super+H"),
    }


SUPPORTED_DEVICES: list[DeviceMapper] = [MkespnK806, MkespnK815]
