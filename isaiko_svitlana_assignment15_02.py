"""Завдання: деталізувати працівників бібліотеки, додавші нові класи.

   * Взяти за основу завдання вже виконане isaiko_svitlana_assignment15_01.py (скопіювати в новий файл)
   * Додайте атрибут level до класу Employee
   * Додайте нові класи:
       * Librarian - віднаслідувати від Employee, задати level='librarian' у конструкторі потомка
       * SeniorLibrarian - віданслідувати від Librarian (level="senior_librerian")
       * Cleaner - віднаслідувати від Employee (level="cleaner")
    * Додати новий метод (у кожний з класів ієрархії наслідування - Employee, Librarian, etc)
      get_description який би повертав строку з поясненням про працівника:
          * Employee - I'm an employee keep doing what needs to be done
          * Librarian - I'm a librarian keep books in order, visitors glad
          * SeniorLibrarian - I'm a senior level librarian, keep the papers in order
          * Cleaner - I'm a cleaner, keeping premises shining
    * Замінити об'екти Employee у прегенерованому списку на конкретні - 2 об'єкта Librarian, 1 SeniorLibrarian,
      1 Cleaner
    * Модіфікувати get_details у класі Employee: додати новий ключ description у який виставити
      значення self.get_description()

Попередній вивод повинен змінитися (виводити конкретних працівників).
"""

import uuid  # генерує унікальне значення, не isbn але ж легше використати


class Employee:

    def __init__(self, name, length_of_work, level):
        self.name = name
        self.length_of_work = length_of_work
        self.level = level

    def get_details(self):
        dict_employee = {'name': self.name, 'length of work': self.length_of_work, 'level': self.get_description()}
        return dict_employee

    def get_description(self):
        return "Im an employee keep doing what needs to be done"


class Librarian(Employee):

    def __init__(self):
        self.level = "librarian"

    def get_description(self):
        return "I'm a librarian keep books in order, visitors glad"


class SeniorLibrarian(Librarian):

    def __init__(self):
        self.level = "senior_librarian"

    def get_description(self):
        return "I'm a senior level librarian, keep the papers in order"


class Cleaner(Employee):

    def __init__(self):
        self.level = "cleaner"

    def get_description(self):
        return "I'm a cleaner, keeping premises shining"


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
    ("Nastya Savchina", "1", "librarian"),
    ("Olya Ovsiukhno", "1", "librarian"),
    ("Leonid Veres", "3",  "SeniorLibrarian"),
    ("Vlad Veruxh", "2", "Cleaner"),
]


def upload_books(library):
    for isbn, title, author, year in BOOKS_TO_LOAD:
        library.add(Book(isbn, title, author, year))


def uploads_employee(employee):
    for name, length_of_work, level in Employee_TO_LOAD:
        employee.register_employee(Employee(name, length_of_work, level))
    return employee


if __name__ == "__main__":
    one_citys_library = Library()
    upload_books(one_citys_library)
    uploads_employee(one_citys_library)
    for line in one_citys_library.employees:
        a = Employee(line.name, line.length_of_work, line.level)
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
