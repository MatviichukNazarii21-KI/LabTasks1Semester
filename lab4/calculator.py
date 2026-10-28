from rich import print
from humanize import intcomma


def calculate():
    a = 15
    b = 5

    print("[bold cyan]Калькулятор[/bold cyan]")
    print(f"Додавання: {a} + {b} = {intcomma(a + b)}")
    print(f"Віднімання: {a} - {b} = {a - b}")
    print(f"Множення: {a} * {b} = {a * b}")
    print(f"Ділення: {a} / {b} = {a / b}")