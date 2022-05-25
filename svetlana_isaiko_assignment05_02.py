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

def input_data():
    """Функція для зчитування даних"""
    text = input("Введіть речення: ")
    return text


def letter_sorting(text, sor_letter):
    """Функція виконує сортування літер в кожному слові у спадаючому/зростаючому порядку"""
    new_text = text.split()
    i = 0
    l = []
    while i < len(new_text):
        n = list(new_text[i])
        if sor_letter == 1:
            n.sort()
        elif sor_letter == 2:
            n.sort(reverse=True)
        l.append("".join(map(str, n)))
        i += 1
    return l


def word_sorting(choose, text, sor_letter):
    """Функція виконує сортування слів в реченні у спадаючому/зростаючому порядку"""
    l = letter_sorting(text, sor_letter)
    if choose == 1:
        l.sort(key=lambda x: x.lower())
    elif choose == 2:
        l.sort(reverse=True, key=lambda x: x.lower())
    return l


def sort_selection():
    sor_letter = int(input("Оберіть тип сортування літер у словах 1 - по зростанню 2 - навпаки: "))
    choose = int(input("Оберіть тип сортування слів у реченні 1 - по зростанню 2 - навпаки: "))
    return sor_letter, choose


def main():
    """Головна функція програми, яка з'єднує всі попередні, дадаючи  можливість декілька разів користувачу
    вводити данні, відбується спочатку сортування літер, а потім слів"""
    i = 0
    while i < 5:
        text = input_data()
        if not len(text):
            continue
        sor_letter, choose = sort_selection()
        l = word_sorting(choose, text, sor_letter)
        print(" ".join(l))
        i += 1


if __name__ == '__main__':
    main()
