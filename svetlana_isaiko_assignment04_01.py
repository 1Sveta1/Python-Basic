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
    number = int(input("Введите число: "))
    return number


def calculation():
    number = input_data()
    factorial = 1
    if number >= 0:
        for i in range(2, number + 1):
            factorial *= i
        print(f"{number}! == {factorial}")
    else:
        print("Введите позитивное число")


if __name__ == '__main__':
    while True:
        calculation()
        choose = int(input("хотите узнать факториал числа? 1 - да: "))
        if choose == 1:
            continue
        else:
            break
