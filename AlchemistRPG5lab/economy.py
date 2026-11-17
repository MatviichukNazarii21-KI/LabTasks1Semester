from inventory import potion_inventory
from potions import POTIONS

gold = 100


def sell_potion(potion_name, quantity):
    global gold

    try:
        if not isinstance(quantity, int) or quantity <= 0:
            print("Неправильна кількість!")
            return False

        if potion_name not in POTIONS:
            print("Такого зілля не існує!")
            return False

        for potion in potion_inventory:
            if potion["name"] == potion_name:

                if potion["quantity"] < quantity:
                    print("Недостатньо зіль для продажу!")
                    return False

                price = POTIONS[potion_name]["price"]
                total_price = price * quantity

                potion["quantity"] -= quantity
                gold += total_price

                if potion["quantity"] == 0:
                    potion_inventory.remove(potion)

                print(f"Продано {quantity} шт. зілля!")
                print(f"Отримано золота: {total_price}")
                print(f"Ваш баланс: {gold}")

                return True

        print("Такого зілля немає в інвентарі!")
        return False

    except Exception as error:
        print(f"Помилка продажу: {error}")
        return False


def show_gold():
    try:
        print(f"Ваше золото: {gold}")

    except Exception as error:
        print(f"Помилка: {error}")