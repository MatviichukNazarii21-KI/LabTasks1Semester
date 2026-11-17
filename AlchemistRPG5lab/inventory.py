# Максимальна кількість слотів
MAX_INGREDIENT_SLOTS = 25

# Максимальна кількість інгредієнтів в одному слоті
MAX_INGREDIENT_STACK = 25

# Інвентар гравця
ingredient_inventory = []


# Додавання інгредієнта
def add_ingredient(name, amount=1):
    try:
        if not isinstance(amount, int) or amount <= 0:
            print("Неправильна кількість інгредієнтів!")
            return False

        if not isinstance(name, str) or not name:
            print("Неправильна назва інгредієнта!")
            return False

        # Перевіряємо наявні слоти
        for slot in ingredient_inventory:
            if slot["name"] == name:
                if slot["quantity"] < MAX_INGREDIENT_STACK:

                    free_space = MAX_INGREDIENT_STACK - slot["quantity"]
                    added = min(amount, free_space)

                    slot["quantity"] += added
                    amount -= added

                    if amount == 0:
                        return True

        # Створюємо нові слоти, якщо залишилися інгредієнти
        while amount > 0:

            if len(ingredient_inventory) >= MAX_INGREDIENT_SLOTS:
                print("Інвентар заповнений!")
                return False

            added = min(amount, MAX_INGREDIENT_STACK)

            ingredient_inventory.append({
                "name": name,
                "quantity": added
            })

            amount -= added

        return True

    except Exception as error:
        print(f"Помилка додавання інгредієнта: {error}")
        return False


# Показ інвентарю
def show_ingredient_inventory():
    try:
        print("\n===== ІНВЕНТАР ІНГРЕДІЄНТІВ =====")

        if not ingredient_inventory:
            print("Інвентар порожній!")
            return

        for number, slot in enumerate(ingredient_inventory, start=1):

            print(
                f"{number}. {slot['name']} "
                f"— {slot['quantity']}/{MAX_INGREDIENT_STACK}"
            )

        print("-" * 35)

        print(
            f"Зайнято слотів: "
            f"{len(ingredient_inventory)}/{MAX_INGREDIENT_SLOTS}"
        )

    except Exception as error:
        print(f"Помилка показу інвентарю: {error}")

# Максимальна кількість слотів для зіль
MAX_POTION_SLOTS = 10

# Максимальна кількість зіль в одному слоті
MAX_POTION_STACK = 10

# Інвентар готових зіль
potion_inventory = []


# Додавання зілля
def add_potion(name, amount=1):
    try:
        if not isinstance(amount, int) or amount <= 0:
            print("Неправильна кількість зіль!")
            return False

        if not isinstance(name, str) or not name:
            print("Неправильна назва зілля!")
            return False

        # Перевіряємо наявні слоти
        for slot in potion_inventory:
            if slot["name"] == name:

                if slot["quantity"] < MAX_POTION_STACK:

                    free_space = MAX_POTION_STACK - slot["quantity"]
                    added = min(amount, free_space)

                    slot["quantity"] += added
                    amount -= added

                    if amount == 0:
                        return True

        # Створюємо нові слоти
        while amount > 0:

            if len(potion_inventory) >= MAX_POTION_SLOTS:
                print("Інвентар зіль заповнений!")
                return False

            added = min(amount, MAX_POTION_STACK)

            potion_inventory.append({
                "name": name,
                "quantity": added
            })

            amount -= added

        return True

    except Exception as error:
        print(f"Помилка додавання зілля: {error}")
        return False


# Показ інвентарю зіль
def show_potion_inventory():
    try:
        print("\n===== ІНВЕНТАР ЗІЛЬ =====")

        if not potion_inventory:
            print("Готових зіль поки немає!")
            return

        for number, slot in enumerate(potion_inventory, start=1):

            print(
                f"{number}. {slot['name']} "
                f"— {slot['quantity']}/{MAX_POTION_STACK}"
            )

        print("-" * 35)

        print(
            f"Зайнято слотів: "
            f"{len(potion_inventory)}/{MAX_POTION_SLOTS}"
        )

    except Exception as error:
        print(f"Помилка показу зіль: {error}")