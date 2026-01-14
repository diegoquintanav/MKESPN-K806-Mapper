.DEFAULT_GOAL := help
.PHONY: help

help: ## Print this help
	@grep -E '^[0-9a-zA-Z_\-\.]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

list_devices: ## List input devices matching MK keyboards
	ls -l /dev/input/by-id/ | grep -i mk

inspect_device_by_id: ## Inspect input device by event ID.
	if [ -z "$(ID)" ]; then echo "Please provide an event ID. Usage: ID=<event_id> make inspect-device-by-event-id"; exit 1; fi
	@echo "Inspecting /dev/input/$(ID)..."
	udevadm test /sys/class/input/event$(ID) 2>/dev/null

udev_k815_rules: ## Seed udev rules for MK K815 keyboard
	@echo "To create Udev rules at /etc/udev/rules.d/99-mkespn-k815.rules"
	@echo "You may need to run this command with elevated privileges (e.g., using sudo)."
	@echo "cat example-configs/99-mkespn-k815.rules | sudo tee /etc/udev/rules.d/99-mkespn-k815.rules > /dev/null"
	@echo "Please reload udev rules with: sudo udevadm control --reload-rules && sudo udevadm trigger"

seed_keymaps: ## Seed default keymaps to ~/.mkespn-mapper/keymaps/
	@echo "Seeding default keymaps to ~/.keymap.json"
	@cp example-configs/.keymap.json ~/.keymap.json
	@echo "Keymaps seeded."

list_devices_cli: ## List input devices using mkespn-mapper CLI
	mkespn-mapper list-devices

gui: ## Launch the Mapper GUI
	mkespn-mapper gui

daemon: ## Launch the Mapper Daemon
	mkespn-mapper daemon