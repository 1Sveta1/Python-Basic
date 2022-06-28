# вибрати довільний об'єкт з довкілля (фізичний) та задати class для нього як потребує синтаксіс Пайтону
# Клас об'єекта повинен включати один атрибут (властивість) та один метод (поведінку) об'екта
# Конструктор (метод ініціалізації) повинен бути присутній (див. атрибут)
# Надати елементарний код-приклад використання (створення та виклик методу) класу

# марка
# модель
# год выпуска
# цвет
# объем двигателя
# количество колес
# вид топлива
# brand
# model
# year of issue
# color
# engine volume
# number of wheels
# Type of fuel

class Student:

    def __int__(self, name, record_book_number, number_of_debts):
        self.name = name
        self.record_book_number = record_book_number
        self.number_of_debts = number_of_debts

    def delivery_of_debt(self):
        self.number_of_debts -= 1
        return self.number_of_debts


def main():
    st1 = Student()
    st1.name = input("Имя студента: ")
    st1.record_book_number = input("Номер зачетной книги: ")
    st1.number_of_debts = int(input("Количество задолжностей: "))
    while True:
        print(f"1 - Вся информаци о студенте {st1.name}, 2 - cдача задолжностей")
        choose = input("Выбор: ")
        if choose == '1':
            print(f"Имя: {st1.name} \nНомер зачетной книги: {st1.record_book_number} \nКоличество задолжностей: {st1.number_of_debts }")
        elif choose == '2':
            st1.number_of_debts = st1.delivery_of_debt()
            print(f"Количество долгов: {st1.number_of_debts}")
        else:
            continue


if __name__ == '__main__':
    main()
