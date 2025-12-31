#!/usr/bin/env python3
# mini_keypad_daemon.py
# Minimal background daemon for Mini Keypad
# Reads mappings from JSON and listens the device forever
# Adapted to survive reboots: uses /dev/input/by-id symlink if available

import json
import os
import select

from evdev import InputDevice, ecodes

from mkespn_mapper.core import Profile, execute_action
from mkespn_mapper.settings import CONFIG_PATH


# --- Main loop ---
def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"No config found at {CONFIG_PATH}")
        return
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        profile = Profile.from_json(json.load(f))

    if not profile.absolute_device_path:
        print(f"[DAEMON] Device path invalid: {profile.absolute_device_path}")
        return

    print(f"[DAEMON] Listening on {profile.absolute_device_path}, enabled={profile.enabled}")
    device = InputDevice(profile.absolute_device_path)
    device.grab()

    try:
        while True:
            r, _, _ = select.select([device.fileno()], [], [], 0.25)
            if not r:
                continue
            for event in device.read():
                if event.type == ecodes.EV_KEY and event.value == 1:  # key down
                    action = profile.mapping.get(event.code)
                    if profile.enabled and action:
                        execute_action(action)
    except KeyboardInterrupt:
        print("[DAEMON] Stopped by user")
    finally:
        device.ungrab()
        device.close()


if __name__ == "__main__":
    main()
