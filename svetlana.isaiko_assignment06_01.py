# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.

def input_data():
    """Функція для вводу даних"""
    text = input("Введіть речення: ")
    return text


def func_count_letter(text):
    """Функція яка рахує кількість  повторень кожної літери в реченні"""
    letter_count = {}
    for i in text:
        if i != '':
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    return letter_count


def func_count_word(new_text):
    """Функція яка рахує кількість  повторень кожного слова в реченні"""
    count_word = {}
    for i in new_text:
        if i != '':
            if i in count_word:
                count_word[i] += 1
            else:
                count_word[i] = 1
    return count_word


def main():
    """Головна функція, яка зв'язала у собі всі попередні. Додала цикл щоб
    користувач мав можливість циклічного вводу та додани перевірки введених значень"""
    while True:
        text = input_data()
        if len(text) > 0:
            new_text = text.split()
            letter_count = func_count_letter(text)
            count_word = func_count_word(new_text)
            print(f"Статистика по кожному слову {count_word} \nСтатистика по кожній букві {letter_count}")
        else:
            continue


if __name__ == '__main__':
    main()
