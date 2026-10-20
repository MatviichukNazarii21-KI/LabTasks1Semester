from rich import print
from collections import Counter


def analyze_text():
    text = "Python допомагає студентам навчатися"
    words = text.split()

    print("[bold cyan]Аналіз тексту[/bold cyan]")
    print(f"Текст: {text}")
    print(f"Кількість слів: {len(words)}")
    print(f"Кількість символів: {len(text)}")
    print(f"Кількість літер у словах: {dict(Counter(text.replace(' ', '')))}")