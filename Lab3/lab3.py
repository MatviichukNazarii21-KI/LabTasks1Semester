products = [
    {"name": "Ноутбук", "price": 25000, "stock": 5},
    {"name": "Мишка", "price": 800, "stock": 15},
    {"name": "Клавіатура", "price": 1500, "stock": 10},
    {"name": "Навушники", "price": 2200, "stock": 7},
    {"name": "Монітор", "price": 7500, "stock": 4}
]

cart = []


def show_catalog():     # def - створення функції
    print("\n--- КАТАЛОГ ---")
    list(map(    # map - функція
        lambda p: print(  # lambda - анонімна функція
            f"{products.index(p) + 1}. {p['name']} — {p['price']:.2f}грн. "  # f - str стрічка
            f"(залишок: {p['stock']})"     # f - str стрічка
        ),
        products
    ))


def add_to_cart():     # def - функція
    show_catalog()    # show_catalog - виклик функції

    try:   # try - обробка помилки
        number = int(input("Введіть номер товару: ")) - 1

        if 0 <= number < len(products):  # if - умова # len - довжина
            product = products[number]   # product - dict словник

            if product["stock"] > 0:   # if - умова  # stock - int ціле число
                cart.append(product)   # append - додавання
                product["stock"] -= 1
                print(f"{product['name']} додано до кошика.")
            else:   # else - інакше
                print("Товару немає в наявності.")
        else:      # else - інакше
            print("Невірний номер.")
    except ValueError:   # except - обробка помилки
        print("Введіть число.")


def show_cart():   # def - функція
    print("\n--- КОШИК ---")

    if not cart:   # if - умова # not - заперечення
        print("Кошик порожній.")
        return   # return - вихід із функції

    list(map(    # list + map - обробка списку
        lambda p: print(f"{cart.index(p) + 1}. {p['name']} — {p['price']:.2f}грн."),   # lambda - анонімна функція
        cart   # cart - list список
    ))

    total = sum(map(lambda p: p["price"], cart))    # total - int ціле число
    print(f"Разом: {total:.2f}грн.")


def remove_from_cart():    # def - функція
    show_cart()      # show_catalog - виклик функції

    if cart:    # if - умова
        try:    # try - обробка помилки
            number = int(input("Введіть номер товару для видалення: ")) - 1    # number - int ціле число

            if 0 <= number < len(cart):
                product = cart.pop(number)   # product - dict   # pop - видалення
                product["stock"] += 1
                print(f"{product['name']} видалено з кошика.")
            else:    #  else - інакше
                print("Невірний номер.")
        except ValueError:   # except - помилка
            print("Введіть число.")


def buy():
    if not cart:
        print("Кошик порожній.")
        return    # return - вихід

    total = sum(map(lambda p: p["price"], cart))  # total - int

    print(f"Сума покупки: {total:.2f}грн.")
    answer = input("Підтвердити покупку? (так/ні): ").lower()

    if answer == "так":    # answer - str стрічка  # == - порівняння
        cart.clear()    # clear - очищення списку
        print("Покупку здійснено!")
    else:    # else - інакше
        print("Покупку скасовано.")


def admin():
    password = input("Введіть пароль адміністратора: ")   # password - str

    if password != "1234":
        print("Невірний пароль.")
        return     #  return - вихід

    print("\n--- ЗАЛИШКИ ТОВАРІВ ---")

    list(map(
        lambda p: print(f"{p['name']}: {p['stock']} шт."),
        products    #  products - list
    ))


def main():   # def - головна функція
    while True:   # while - цикл  # True - bool
        print("""
--- МІНІ МАГАЗИН ---
1. Переглянути каталог
2. Додати товар у кошик
3. Переглянути кошик
4. Видалити товар з кошика
5. Купити товари
6. Увійти як адміністратор
0. Вихід
""")

        choice = input("Оберіть дію: ")    # choice - str

        match choice:   # match - вибір
            case "1":   # case - варіант
                show_catalog()   # show_catalog - виклик функції
            case "2":
                add_to_cart()    # add_to_cart - виклик функції
            case "3":
                show_cart()
            case "4":
                remove_from_cart()  # remove_from_cart - виклик функції
            case "5":
                buy()      # buy - виклик функції
            case "6":
                admin()    # admin - виклик функції
            case "0":
                print("До побачення!")
                break    # break - зупинка циклу
            case _:  # _  - будь яке інше значення
                print("Невірний вибір.")


main()   # main - запуск функції
