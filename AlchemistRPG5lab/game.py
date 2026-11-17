from inventory import (
    show_ingredient_inventory,
    show_potion_inventory
)

from economy import show_gold, sell_potion
import economy

from days import start_new_day, show_day
from potions import show_potion_recipes, craft_potion


def start_game():
    try:
        print("Вітаємо у світі алхімії!")
        print("Ви — молодий алхімік.")
        print("Ваша пригода починається!")

        while True:
            print("\n===== МЕНЮ ГРИ =====")
            print("1. Інвентар інгредієнтів")
            print("2. Інвентар зіль")
            print("3. Переглянути золото")
            print("4. Продати зілля")
            print("5. Почати новий день")
            print("6. Переглянути поточний день")
            print("7. Переглянути рецепти")
            print("8. Зварити зілля")
            print("0. Вийти з гри")

            choice = input("Оберіть дію: ")

            if choice == "1":
                show_ingredient_inventory()

            elif choice == "2":
                show_potion_inventory()

            elif choice == "3":
                show_gold()

            elif choice == "4":
                name = input("Введіть назву зілля: ")

                try:
                    quantity = int(input("Введіть кількість: "))
                    sell_potion(name, quantity)
                except ValueError:
                    print("Потрібно ввести число!")

            elif choice == "5":
                result = start_new_day()

                if not result:
                    if economy.gold >= 5000:
                        print("\n===== ПЕРЕМОГА! =====")
                        print("Ви стали найвідомішим алхіміком королівства!")
                        print(f"Ваше золото: {economy.gold}")
                    else:
                        print("\n===== ПРОГРАШ! =====")
                        print("Ви не змогли накопичити 5000 золотих.")
                        print(f"Ваше золото: {economy.gold}")

                    break

            elif choice == "6":
                show_day()

            elif choice == "7":
                show_potion_recipes()

            elif choice == "8":
                show_potion_recipes()

                try:
                    number = int(input("\nОберіть номер рецепта: "))
                    craft_potion(number)
                except ValueError:
                    print("Потрібно ввести число!")

            elif choice == "0":
                print("Дякуємо за гру!")
                break

            else:
                print("Невідома команда!")

    except Exception as error:
        print(f"Помилка гри: {error}")