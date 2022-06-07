"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""


def input_data(choose):
    """Функція введення даних"""
    if choose == "1":
        var_1 = input("var_1: ")
    else:
        var_1 = int(input("var_1: "))
    sign = input('Sign (+,-,*,/): ')
    var_2 = int(input("var_2: "))
    return var_1, sign, var_2


def calculate(var_1, sign, var_2):
    """Функція виконання арифметичних оперцій для двух операндів"""
    if sign == '+':
        return var_1 + var_2
    elif sign == '-':
        return var_1 - var_2
    elif sign == '*':
        return var_1 * var_2
    elif sign == '/':
        if var_2 != 0:
            return var_1 / var_2
        else:
            print("Деление на ноль!")
    else:
        print("Неверный знак операции!")


def main():
    """Головна функція яка  з'єднує всі попередні та додає циклічний ввод"""
    while True:
        choose = input("1 - арифметические операции со строками(+, *). По умолчанию над числами: ")
        var_1, sign, var_2 = input_data(choose)
        otv = calculate(var_1, sign, var_2)
        print(f"{var_1} {sign} {var_2} = {otv}")


if __name__ == "__main__":
    main()
