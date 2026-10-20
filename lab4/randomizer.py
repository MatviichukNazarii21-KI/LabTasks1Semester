import random
from rich import print


def random_number():
    number = random.randint(1, 100)
    print(f"[green]Випадкове число: {number}[/green]")