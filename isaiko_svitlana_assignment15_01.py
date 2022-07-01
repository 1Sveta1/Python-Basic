"""Завдання: додати класс Employee (працівник) до класів з assignment14_02.py

    * Взяти за основу готове завдання assignment14_02.py (з рішенням, скопіювати в новий файл)!
    * Додати новий клас Employee
       * атрибути: ім'я, стаж роботи (на поточному місці)!
       * метод: get_details() - який буде повертати dict з атрибутами працівника!
    * У існуючому класі Library додати:
       * атрибут employees який буде ініціалізуватися пустим списком !
       * метод register_employee(Employee) який буде додавати Employee до employees!
    * Сформувати якийсь лист з об'єектами Employee (видумати працівників, декілька)!
      та написати функцію яка б додавала працівникив до об'єкту бібліотеки
    * Додати код для демонстрації роботи програми - який би виводив працівників бібліотекі та книги.
"""
import uuid  # генерує унікальне значення, не isbn але ж легше використати


class Employee:
    """Represents employee entity"""
    def __init__(self, name, length_of_work):
        self.name = name
        self.length_of_work = length_of_work

    def get_details(self):
        dict_employee = {'name': self.name, 'length of work': self.length_of_work}
        return dict_employee


class Book:
    """Represents book entity (without behavior, only properties)."""

    def __init__(self, isbn, title, author, year):
        self.isbn = uuid.uuid4()
        self.title = title
        self.author = author
        self.year = year


class Library:
    """Represents library providing basic library transactions."""

    def __init__(self):
        self.library = []
        self.employees = []

    def add(self, book):
        self.library.append(book)

    def search(self, query):
        for book in self.library:
            if query == book.title:
                print("yes")

    def lend(self, query):
        for book in self.library:
            if query == book.title:
                self.library.remove(book)
                return book

    def register_employee(self, employee):
        self.employees.append(employee)




BOOKS_TO_LOAD = [  # https://en.wikipedia.org/wiki/List_of_best-selling_books
    (uuid.uuid4(), "A Tale of Two Cities", "Charles Dickens", 1859),
    (uuid.uuid4(), "The Little Prince", "Antoine de Saint-Exupéry", 1943),
    (uuid.uuid4(), "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997),
    (uuid.uuid4(), "And Then There Were None", "Agatha Christie", 1939),
    (uuid.uuid4(), "Dream of the Red Chamber", "Cao Xueqin", 1791),
    (uuid.uuid4(), "The Hobbit", "J. R. R. Tolkien", 1937),
]


Employee_TO_LOAD = [
    ("Nastya Savchina", "2"),
    ("Olya Ovsiukhno", "4"),
    ("Leonid Veres", "1"),
]


def upload_books(library):
    for isbn, title, author, year in BOOKS_TO_LOAD:
        library.add(Book(isbn, title, author, year))


def uploads_employee(employee):
    for name, length_of_work in Employee_TO_LOAD:
        employee.register_employee(Employee(name, length_of_work))
    return employee


if __name__ == "__main__":
    one_citys_library = Library()
    upload_books(one_citys_library)
    uploads_employee(one_citys_library)
    for line in one_citys_library.employees:
        a = Employee(line.name, line.length_of_work)
        list_employees = a.get_details()
        print(list_employees)
    my_reading, query = None, "And Then There Were None"
    if one_citys_library.search(query) != -1:
        print("OMG! They have it")
        my_reading = one_citys_library.lend(query)
    else:
        print("Damn! nothing to read.")
    print("My current reading: ")
    description = "nothing interesting" if my_reading is None \
        else f"{my_reading.isbn}, {my_reading.title}, {my_reading.author}, {my_reading.year}"
    print(description)
