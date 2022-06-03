# Є два списка (не питонівських списка, а загалом) чисел.
# Порахувати скільки унікальних (є тільки в одному з двох)
# чисел в обох списках.
#
# Наприклад:
#   е  1, 2, 3, 4, 5 та 2, 3, 6, 8
#   унікальних чисел в обох списках: 5 (1, 4, 5, 6, 8)


def data_to_count():
    """Функція яка повертяє дані"""
    l = 1, 3, 4, 5, 6, 6, 7
    l1 = 3, 4, 5, 8, 9, 0
    return l, l1


def unique_in_two_sets(l, l1):
    """Функція повертає унікальні значення двох списків разом"""
    uniq_numbers = set.union(set(l), set(l1))
    return uniq_numbers


def unique_in_set(l, l1, choose):
    """Залежно від умови функція повертає уникальні значання списка l або списка l1"""
    if choose == 1:
        uniq_l = set.difference(set(l), set(l1))
        return uniq_l
    elif choose == 2:
        uniq_l1 = set.difference(set(l1), set(l))
        return uniq_l1


def main():
    """Головна функція,  зв'язує всі попередні функції ,реалізується можливість
     вибору дії над списками користувачу,"""
    l, l1 = data_to_count()
    text = ""
    while True:
        print("Список можливіх дій:"
              "\n1 - вивід унікальніх значень списка l (немає в списку l1)"
              "\n2 - вивід унікальніх значень списка l1 (немає в списку l)"
              "\n3 - вивід унікальних значень в обох списках"
              "\n4 - вихід")
        choose = int(input("Ваш вибір: "))
        uniq = unique_in_set(l, l1, choose)
        uniq_two_sets = unique_in_two_sets(l, l1)
        if choose == 1:
            text = f" унікальніх значень списка l: {uniq}"
        elif choose == 2:
            text = f" унікальніх значень списка l1: {uniq}"
        elif choose == 3:
            text = f" унікальніх значення в обох списках: {uniq_two_sets}"
        elif choose == 4:
            break
        else:
            continue
        print(text)


if __name__ == "__main__":
    main()
