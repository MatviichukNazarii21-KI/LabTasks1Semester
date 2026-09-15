users = {
    "student1": {
        "password": "1111",
        "grades": [12, 10, 8, 5, 11, 9]
    },
    "student2": {
        "password": "2222",
        "grades": [4, 3, 5, 7, 2, 6]
    },
    "student3": {
        "password": "3333",
        "grades": [12, 12, 10, 11, 9, 8]
    },
    "student4": {
        "password": "4444",
        "grades": [2, 4, 3, 1, 5, 4]
    }
}

print("===== АВТОРИЗАЦІЯ =====")

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    print("\nВхід успішний!")
    print("Користувач:", login)

    grades = users[login]["grades"]

    print("\nВсі оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\nКількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")
