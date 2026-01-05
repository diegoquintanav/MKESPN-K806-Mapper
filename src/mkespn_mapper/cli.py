from typer import Typer


app = Typer(help="MKESPN K806/K815 Key Mapper CLI")


@app.command()
def list_devices():
    """List input devices connected to the system."""
    from mkespn_mapper.utils import list_devices_info

    list_devices_info()


@app.callback()
def callback():
    # https://typer.tiangolo.com/tutorial/commands/one-or-multiple/#one-command-and-one-callback
    pass


if __name__ == "__main__":
    app()
