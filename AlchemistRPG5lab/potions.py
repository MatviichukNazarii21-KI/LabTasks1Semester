from ingredients import INGREDIENTS
from inventory import (
    ingredient_inventory,
    potion_inventory,
    add_potion,
    MAX_POTION_SLOTS,
    MAX_POTION_STACK
)


# Назви 50 різних зіль
POTION_NAMES = [
    "Зілля здоров'я",
    "Зілля мани",
    "Зілля сили",
    "Зілля швидкості",
    "Зілля захисту",
    "Зілля витривалості",
    "Зілля невидимості",
    "Зілля мудрості",
    "Зілля удачі",
    "Зілля відновлення",
    "Еліксир життя",
    "Еліксир енергії",
    "Еліксир молодості",
    "Еліксир мудрості",
    "Еліксир сили",
    "Отрута слабкості",
    "Отрута сну",
    "Отрута паралічу",
    "Отрута темряви",
    "Отрута забуття",
    "Зілля вогню",
    "Зілля льоду",
    "Зілля блискавки",
    "Зілля землі",
    "Зілля повітря",
    "Зілля світла",
    "Зілля темряви",
    "Зілля природи",
    "Зілля духів",
    "Зілля часу",
    "Еліксир безсмертя",
    "Еліксир відродження",
    "Еліксир дракона",
    "Еліксир фенікса",
    "Еліксир короля",
    "Зілля мисливця",
    "Зілля мандрівника",
    "Зілля алхіміка",
    "Зілля мага",
    "Зілля воїна",
    "Зілля спокою",
    "Зілля хоробрості",
    "Зілля очищення",
    "Зілля польоту",
    "Зілля телепортації",
    "Зілля перетворення",
    "Зілля сновидінь",
    "Зілля пам'яті",
    "Зілля духовності",
    "Абсолютний еліксир"
]


# Створення бази рецептів
ingredient_names = list(INGREDIENTS.keys())

POTIONS = {}

for number, potion_name in enumerate(POTION_NAMES):

    POTIONS[potion_name] = {
        "recipe": [
            ingredient_names[number * 2],
            ingredient_names[number * 2 + 1]
        ],
        "price": 100 + number * 20
    }


# Показ усіх рецептів
def show_potion_recipes():
    try:
        print("\n===== КНИГА РЕЦЕПТІВ =====")

        for number, (name, data) in enumerate(
            POTIONS.items(), start=1
        ):
            print(f"\n{number}. {name}")
            print("Потрібні інгредієнти:")

            for ingredient in data["recipe"]:
                print(f" - {ingredient}")

            print(f"Ціна: {data['price']} золотих")

        print(f"\nУсього рецептів: {len(POTIONS)}")

    except Exception as error:
        print(f"Помилка показу рецептів: {error}")


# Створення зілля
def craft_potion(number):
    try:
        if not isinstance(number, int):
            print("Потрібно ввести номер рецепта!")
            return False

        if number < 1 or number > len(POTIONS):
            print("Такого рецепта не існує!")
            return False

        # Отримуємо назву та рецепт
        potion_name = list(POTIONS.keys())[number - 1]
        recipe = POTIONS[potion_name]["recipe"]

        # Перевіряємо вільне місце для зілля
        free_space = 0

        for slot in potion_inventory:
            free_space += MAX_POTION_STACK - slot["quantity"]

        free_space += (
            MAX_POTION_SLOTS - len(potion_inventory)
        ) * MAX_POTION_STACK

        if free_space < 1:
            print("Немає місця для готового зілля!")
            return False

        # Перевіряємо наявність інгредієнтів
        for ingredient in recipe:

            total = sum(
                slot["quantity"]
                for slot in ingredient_inventory
                if slot["name"] == ingredient
            )

            if total < 1:
                print(f"Не вистачає інгредієнта: {ingredient}")
                return False

        # Забираємо використані інгредієнти
        for ingredient in recipe:

            for slot in ingredient_inventory:

                if slot["name"] == ingredient and slot["quantity"] > 0:
                    slot["quantity"] -= 1
                    break

        # Видаляємо порожні слоти
        ingredient_inventory[:] = [
            slot for slot in ingredient_inventory
            if slot["quantity"] > 0
        ]

        # Додаємо готове зілля
        if not add_potion(potion_name):
            print("Не вдалося додати зілля до інвентарю!")
            return False

        print(f"\nВітаємо! Ви створили: {potion_name}")
        print(f"Ціна зілля: {POTIONS[potion_name]['price']} золотих")

        return True

    except Exception as error:
        print(f"Помилка створення зілля: {error}")
        return False