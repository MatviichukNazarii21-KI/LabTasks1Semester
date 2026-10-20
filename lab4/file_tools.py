import os
from rich import print


def save_text():
    filename = "student_notes.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Мій навчальний проєкт на Python.")

    print(f"[green]Файл {filename} успішно створено![/green]")
    print(f"Поточна папка: {os.getcwd()}")