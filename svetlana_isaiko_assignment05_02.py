# Завдання:
#    * запитати у користувача речення на вхід (пуста строка не приймається);
#    * відсортувати літери у кожному слові
#    * вивести результат на екран
#    * дозвольте користувачу вводити дані декілька разім (не безкінечне)
#    * ускладнене завдання: відсортуйте слова між собою (не тільки літери у словах),
#                           у спадаючому/зростаючому порядку -
#    * для саморозвитку: використайте tuple/set для зберігання літер у словах.
#                        що як убрати сортування літер у словах. чи будуть питання?
# Підказки:
#    * str.split()
#    * list(sequence), а також tuple/set конструктори
#    * reverse=True

# text = input("Введіть строку: ")
# a = text.split()
# i = 0
# while i < len(a):
#
#     i += 1
# text = "band aca bdf"
# a = text.split()
# i = 0
# l = []
# while i < len(a):
#     mas = a[i]
#     n = list(mas)
#     n.sort()
#     l.append("".join(map(str, n)))
#     i += 1
# l.sort()
# print(" ".join(l))


def input_data():
    text = input("Введіть речення: ")
    return text


def sor_data(text):
    a = text.split()
    i = 0
    l = []
    while i < len(a):
        n = tuple(a[i])
        sorted(n)
        l.append("".join(map(str, n)))
        i += 1
    print(l)
    return l


def vid_sort(choose, text):
    l = sor_data(text)
    if choose == 1:
        l.sort(key=lambda x: x.lower())
    elif choose == 2:
        l.sort(reverse=True, key=lambda x: x.lower())
    return l


def main():
    i = 0
    while i < 5:
        text = input_data()
        choose = int(input("Виберіть сортування  1 - по зростанню 2 - навпаки: "))
        l = vid_sort(choose, text)
        print(" ".join(l))
        i += 1


if __name__ == '__main__':
    main()
