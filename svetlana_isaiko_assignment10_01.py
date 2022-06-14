# Завдання: посортувати, рандомно згенеровану, матрицю
#           з розмірністю NxM
#
# Деталі:
#          1. код для роботи з матрицею відокрмити у власний модуль
#             (matrix.py, generate_matrix(n, m), sort_matrix(m), print_matrix(m))
#          2. Використати зовнішній модуль quicksort (доданий до завдання) для
#             сортування матриці
#          3. використати assignment10_01.py для main функції з основною
#             логікою программи (запитати розміри матриці, згенерувати матрицю,
#             відсортувати та вивести на екран, використовуючи зовнішній модуль
#             matrix)
#
# Підказка:
#            * відсортувати потрібно усі елементи а не окремо у к ожному рядку
#            * за допомогою list comprehension можно зконевртувати двовимірну
#              матрицю у одновимірну, посортувати її, зконвертувати у зворотньому
#              напрямку - з 1 у 2-вимірну (можно повернути нову матрицю як результат
#              функції сортування - sort_matrix - або "перезалити" в оригінальну,
#              m[row] = [comprehension] (у цьому випадку можно не конвертувати
#              1 вимірну відсортовану матриці у двовимірну та використати range(0, len(m), M)
#              та вибираючи підсписки за допомогою слайсів m[i:i+M]).
import matrix


def main():
    """Функція  з основною логікою программи"""
    while True:
        print("Введіть розмірність матриці")
        n = int(input("кількість строк: "))
        m = int(input("кількість столбців: "))
        lst = matrix.generate_matrix(n, m)
        lst = matrix.sort_matrix(lst, n)
        matrix.print_matrix(lst)


if __name__ == '__main__':
    main()
