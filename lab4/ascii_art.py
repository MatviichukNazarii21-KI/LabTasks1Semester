import pyfiglet
from rich import print


def show_art():
    art = pyfiglet.figlet_format("STUDENT")
    print(f"[cyan]{art}[/cyan]")