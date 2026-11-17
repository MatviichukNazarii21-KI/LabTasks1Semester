from ingredients import get_random_ingredients
from inventory import add_ingredient


# Поточний день
current_day = 1

# Максимальна кількість днів
MAX_DAYS = 30


# Початок нового дня
def start_new_day():
    global current_day

    try:
        if current_day >= MAX_DAYS:
            print("\nВи досягли останнього ігрового дня!")
            return False

        current_day += 1

        print(f"\n===== ДЕНЬ {current_day} =====")
        print("Ви отримали 5 випадкових інгредієнтів!")

        new_ingredients = get_random_ingredients(5)

        for ingredient in new_ingredients:
            if add_ingredient(ingredient):
                print(f"+ {ingredient}")
            else:
                print(f"Не вдалося додати: {ingredient}")

        return True

    except Exception as error:
        print(f"Помилка початку дня: {error}")
        return False


# Показ поточного дня
def show_day():
    try:
        print(f"Поточний день: {current_day}/{MAX_DAYS}")

    except Exception as error:
        print(f"Помилка показу дня: {error}")