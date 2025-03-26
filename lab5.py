import random

def task1():
    number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Вгадайте число від 1 до 10: "))
            if guess < number:
                print("Більше")
            elif guess > number:
                print("Менше")
            else:
                print("Вітаю! Ви вгадали!")
                break
        except ValueError:
            print("Будь ласка, введіть число!")

def task2():
    number = random.randint(1, 50)
    while True:
        try:
            guess = int(input("Вгадайте число від 1 до 50: "))
            difference = abs(guess - number)
            if difference == 0:
                print("Вітаю! Ви вгадали!")
                break
            elif difference <= 3:
                print("Дуже близько!")
            elif difference <= 10:
                print("Близько")
            else:
                print("Далеко")
        except ValueError:
            print("Будь ласка, введіть число!")

def task3():
    number = random.randint(1, 20)
    attempts = 3
    while attempts > 0:
        try:
            guess = int(input(f"Вгадайте число від 1 до 20 (Залишилось спроб: {attempts}): "))
            if guess == number:
                print("Вітаю! Ви вгадали!")
                return
            attempts -= 1
            if attempts:
                print(f"Невірно. Залишилось {attempts} спроб.")
            else:
                print(f"Ви програли! Загадане число: {number}")
        except ValueError:
            print("Будь ласка, введіть число!")

def task4():
    pin = str(random.randint(1000, 9999))
    attempts = 5
    while attempts > 0:
        guess = input(f"Введіть 4-значний PIN-код (Залишилось спроб: {attempts}): ")
        if len(guess) != 4 or not guess.isdigit():
            print("Будь ласка, введіть чотири цифри!")
            continue
        if guess == pin:
            print("Вітаю! Ви вгадали PIN-код!")
            return
        correct_positions = sum(1 for a, b in zip(guess, pin) if a == b)
        print(f"Невірно. Правильних цифр на правильних місцях: {correct_positions}")
        attempts -= 1
    print(f"Спроби закінчились. Правильний PIN-код: {pin}")

def task5():
    colors = {"червоний": "теплий", "жовтий": "теплий", "синій": "холодний", "зелений": "холодний", "фіолетовий": "холодний"}
    secret_color = random.choice(list(colors.keys()))
    attempts = 3
    while attempts > 0:
        guess = input(f"Вгадайте колір (Залишилось спроб: {attempts}): ").strip().lower()
        if guess not in colors:
            print("Некоректний ввід! Виберіть один із запропонованих кольорів.")
            continue
        if guess == secret_color:
            print("Вітаю! Ви вгадали колір!")
            return
        else:
            print(f"Невірно. Колір належить до категорії: {colors[secret_color]}")
        attempts -= 1
    print(f"Спроби закінчились. Загаданий колір: {secret_color}")

def main():
    while True:
        print("\nОберіть завдання (1-5), '0' для виходу:")
        choice = input()
        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "0":
            print("Дякуємо за гру! До побачення!")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")
        
        # Повернення до вибору завдання після завершення кожного
        continue_game = input("\nБажаєте спробувати інше завдання? (так/ні): ").strip().lower()
        if continue_game != "так":
            print("Дякуємо за гру! До побачення!")
            break

if __name__ == "__main__":
    main()
