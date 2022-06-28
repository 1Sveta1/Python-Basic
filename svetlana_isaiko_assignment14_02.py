"""Завдання: додати відсутній код (завершити імплементацию.

   Надані класи використовуються для надання функціональності бібліотеки.
   Абстрація бібліотеки (class Library) надає такий інтерфейс (-> - повертаєме значення):
    * add(Book) -> None - додати книгу у бібліотеку
    * search(title) -> int - відповисти на запит - чи інснує така книга (linear search)
    * lend(title) -> Book - "позичити" книгу (видалити з списку книг)
    * remove(title) - видалати кингу з бібліотеки
    Library об'ект утримує усі його книги у списку book_list

   Абстракція книги (class Book) не надає поведінки (методів) тільки
   властивості (атрибути):
    * isbn - унікальний код ідентификатор книги (книги з різним isbn - різні)
    * title - назва
    * author - автор
    * year  - рік видання
"""
import uuid  # генерує унікальне значення, не isbn але ж легше використати


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


BOOKS_TO_LOAD = [  # https://en.wikipedia.org/wiki/List_of_best-selling_books
    (uuid.uuid4(), "A Tale of Two Cities", "Charles Dickens", 1859),
    (uuid.uuid4(), "The Little Prince", "Antoine de Saint-Exupéry", 1943),
    (uuid.uuid4(), "Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997),
    (uuid.uuid4(), "And Then There Were None", "Agatha Christie", 1939),
    (uuid.uuid4(), "Dream of the Red Chamber", "Cao Xueqin", 1791),
    (uuid.uuid4(), "The Hobbit", "J. R. R. Tolkien", 1937),
]


def upload_books(library):
    for isbn, title, author, year in BOOKS_TO_LOAD:
        library.add(Book(isbn, title, author, year))


if __name__ == "__main__":
    one_citys_library = Library()
    upload_books(one_citys_library)
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
