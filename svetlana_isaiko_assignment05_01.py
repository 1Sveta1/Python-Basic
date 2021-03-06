# Завдання:
#     * згенерувати лист з рандомними числами (числа від 50 до 100 кожне,
#       довжину листа запитати у користувача, але не коротший за 10 та не
#       довший за 50 елементів;
#     * відсортувати елементи в убуваючому порядку (10, 9, 8...)
#     * напечатати на екран
#     * додати можливість циклічного вводу даних для експеріментів
#
#     * ускладнене завдання: написати та використати bubble-sort алгоритм
#
# Підказки:
#     * .sort()
#     * reverse=True
import random


def input_data():
    """Функція для вводу даних"""
    l = []
    size = int(input("Введите длину массива (от 10 до 50): "))
    for _ in range(0, size):
        l.append(random.randint(50, 100))
    return l, size


def sort_function(l):
    """Функція для сортування за допомогою вбудованої функції для сортування"""
    l.sort(reverse=True)
    return l


def sort_buble(l):
    """Функція використання алгоритма bubble-sort"""
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l


def main():
    """Головна функція, яка зв'язала у собі всі попередні. Додала цикл щоб
    користувач мав можливість циклічного вводу та додани перевірки введених значень"""
    while True:
        l, size = input_data()
        if 10 <= size <= 50:
            choose = input("1 - в убуваючому порядку, 2 - за зростанням: ")
            if choose == "1":
                sort_function(l)
            elif choose == "2":
                sort_buble(l)
            else:
                print("Невірний ввод")
                continue
            print(f"Лист має такий вигляд: {l}")
        else:
            print("Розміри листа повинні бути від 10 до 50")


if __name__ == '__main__':
    main()


