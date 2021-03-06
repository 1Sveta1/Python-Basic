# Завдання: написати програму обчислення факторіалу числа.
#           Программа запитує ввод від користувача у циклі
#           (вихід можливий за допомогою Ctrl-C/D)
# 
# Факторіал числа: n!
# n! = 1 * 2 * 3 * 4 ... n-1 * n
# 0! = 1
#
# Приклад роботи:
#
# Введіть число для обчислення факторіалу: 5
# 5! == 120
# 
# Введіть число для обчислення факторіалу: -5
# Невірний ввод

def input_data():
    """Функція для вводу даних"""
    number = int(input("Введите число: "))
    return number


def calculation(number):
    """Функція яка обчислює факторіал числа"""
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    print(f"{number}! == {factorial}")


def main():
    """Функція зв'язує функцію ввода даних та обчислення факторіала, додається цикл та умови
    виходу з нього."""
    while True:
        number = input_data()
        if number >= 0:
            calculation(number)
        else:
            print("Невірний ввод")
        choose = int(input("Хочете дізнатися факторіал числа? 1 - да: "))
        if choose == 1:
            continue
        else:
            break


if __name__ == '__main__':
    main()
