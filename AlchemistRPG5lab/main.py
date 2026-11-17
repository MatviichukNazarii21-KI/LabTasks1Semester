from game import start_game


# Головна функція гри
def main():
    try:
        print("=" * 40)
        print("          ALCHEMIST RPG")
        print("=" * 40)

        start_game()

    except Exception as error:
        print(f"Помилка гри: {error}")


# Запуск програми
if __name__ == "__main__":
    main()