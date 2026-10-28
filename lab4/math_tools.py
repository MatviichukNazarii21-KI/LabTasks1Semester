import math
from rich import print


def square():
    number = 25

    print("[bold cyan]Математичні обчислення[/bold cyan]")
    print(f"Число: {number}")
    print(f"Квадратний корінь: {math.sqrt(number)}")
    print(f"Факторіал: {math.factorial(number)}")