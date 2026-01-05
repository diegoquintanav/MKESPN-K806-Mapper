from typer import Typer


app = Typer(help="MKESPN K806/K815 Key Mapper CLI")


@app.command()
def list_devices():
    """List input devices connected to the system."""
    from mkespn_mapper.utils import list_devices_info

    list_devices_info()


@app.command()
def run_daemon():
    """Run the background daemon to listen to the keypad."""
    from mkespn_mapper.daemon import main as daemon_main

    daemon_main()


@app.command()
def gui():
    """Launch the GUI application."""
    from mkespn_mapper.gui import main as gui_main

    gui_main()


@app.callback()
def callback():
    # https://typer.tiangolo.com/tutorial/commands/one-or-multiple/#one-command-and-one-callback
    pass


if __name__ == "__main__":
    app()
