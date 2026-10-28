from validators import email
from rich import print


def check_email():
    address = "student@example.com"

    if email(address):
        print(f"[green]Електронна пошта {address} правильна[/green]")
    else:
        print("[red]Електронна пошта неправильна[/red]")