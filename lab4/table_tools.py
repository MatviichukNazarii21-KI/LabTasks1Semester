from tabulate import tabulate


def show_table():
    students = [
        ["Андрій", 10],
        ["Олена", 12],
        ["Максим", 9]
    ]

    print("Таблиця оцінок студентів:")
    print(tabulate(students, headers=["Студент", "Оцінка"], tablefmt="grid"))