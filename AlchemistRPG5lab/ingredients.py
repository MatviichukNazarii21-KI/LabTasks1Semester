import random


# Частини назв інгредієнтів
PREFIXES = [
    "Сонячний", "Місячний", "Темний", "Світлий",
    "Магічний", "Стародавній", "Крижаний", "Вогняний",
    "Отруйний", "Лісовий", "Золотий", "Срібний",
    "Кришталевий", "Древній", "Таємничий", "Небесний",
    "Диявольський", "Королівський", "Примарний", "Чарівний"
]

MATERIALS = [
    "корінь", "листок", "гриб", "кристал", "квітка",
    "пилок", "камінь", "пелюстка", "насіння", "мох"
]


# Створення бази інгредієнтів
INGREDIENTS = {}

for prefix in PREFIXES:
    for material in MATERIALS:
        name = f"{prefix} {material}"

        INGREDIENTS[name] = {
            "price": random.randint(5, 100),
            "rarity": random.choice(
                ["Звичайний", "Рідкісний", "Епічний", "Легендарний"]
            )
        }


# Отримання випадкових інгредієнтів
def get_random_ingredients(amount=5):
    try:
        ingredients = []

        for _ in range(amount):
            name = random.choice(list(INGREDIENTS.keys()))
            ingredients.append(name)

        return ingredients

    except Exception as error:
        print(f"Помилка отримання інгредієнтів: {error}")
        return []


# Перевірка кількості інгредієнтів
def show_ingredients_count():
    try:
        print(f"Кількість інгредієнтів: {len(INGREDIENTS)}")

    except Exception as error:
        print(f"Помилка: {error}")