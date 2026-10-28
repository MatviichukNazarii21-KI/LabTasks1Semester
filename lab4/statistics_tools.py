import statistics
from rich import print


def average():
    grades = [10, 12, 9, 11, 8]

    result = statistics.mean(grades)

    print("[bold cyan]Статистика оцінок[/bold cyan]")
    print(f"Оцінки: {grades}")
    print(f"Середня оцінка: {result}")