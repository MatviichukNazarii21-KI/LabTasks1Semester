import os
import platform
from rich import print


def show_system():
    print("[bold cyan]Інформація про систему[/bold cyan]")
    print(f"Операційна система: {platform.system()}")
    print(f"Версія Python: {platform.python_version()}")
    print(f"Поточна папка: {os.getcwd()}")