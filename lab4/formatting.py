from tabulate import tabulate
from rich import print


def show_color():
    print("[bold magenta]Форматування інформації[/bold magenta]")

    data = [
        ["Предмет", "Оцінка"],
        ["Історія", 10],
        ["Інформатика", 12],
        ["Математика", 9]
    ]

    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))