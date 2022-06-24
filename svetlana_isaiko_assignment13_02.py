# Завдання: допрацювати наданий код до робочого варіанту.
#           Зчитує матрицю з файла (з попереднього завдання,
#           generated_matrix.txt), розгортає, сортує квіксортом,
#           та згортає у одновимірну відсортовану матрицю, яку
#           виводить на екран. Програма повинна на вхід отримувати
#           файл у такомож форматі як генерується попереднім завданням
#           спочатку розмірність, потім, одразу, матриця (для спрощення)
#
#           Зчитати n, m можно в один рядок коду, також можно зчитати
#           і matrix, але можно використати построковий підхид для срощення
#           виконання
#
# Підказки: split, strip (щоб "обрізати" пробільні символи у строках),
#           int, map, list()
from toolset import matrices, sequences

MATRIX_STORE_FILE = "generated_matrix.txt"


def load_matrix(filename):

    n, m, matrix = None, None, []

    with open(filename) as inp:
        n, m = map(int, inp.readline().strip(' \n').split(' '))
        # зчитуємо перший рядок файлу - n m - підказка inp.readline()
        # matrix.append()  # list-comprehension, по-елментно додаємо числа з вичитаного рядка у matrix
        for line in inp:
            matrix.append([i for i in list(map(int, line.split()))])
    inp.close()
    return n, m, matrix


def main():
    n, m, matrix = load_matrix(MATRIX_STORE_FILE)
    if not (n and m and matrix):
        print("No input")
        return
    flat_matrix = matrices.flatten(matrix, n)
    sequences.quicksort(flat_matrix, 0, len(flat_matrix)-1)
    matrix = matrices.roll(flat_matrix, m)
    print("Sorted matrix")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()