"""Завдання: написати програму яка будет використовувати пакет створений у попередньому завданні.

Написати top-level Пайтон скрипт який буде використовувати будь-яку функцію з пакету.

Наприклад: запитати число у корисувача та вивести послідовність n за допомогою fizzbuzz(n)

    n = int(input())
    for el in fun.fizzbuzz(n):
        print(el)

"""

from toolset import fun


def input_data():
    """Функція щоб користувач """
    n = int(input("Введіть n: "))
    return n


def main():
    """Головна функція програми  з'єднує імпортовану функцію та попередні функції"""
    while True:
        n = input_data()
        lst = fun.fizzbuzz(n)
        print(lst)


if __name__ == '__main__':
    main()