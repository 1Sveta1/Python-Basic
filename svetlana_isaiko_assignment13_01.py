# Завдання: додати відсутні інструкції у наданому коді.
#           По завершенню програми повинно залишатись два файла
#           generated_sequence.txt з числовою, рандомно сгенерованою,
#           послідовністю (з переносами строк, у колонку)
#           та generated_matrix.txt у якому
#           таж сама послідовність представлена у виді двовимірной матриці
#           (також і візуально, з пробілами між елементами у рядку та переносами строк
#           між рядками, перший рядок файлу - розмірність матриці - n m).
#
# Підказки: використати toolset пакет з попередної домашки,
#           write, f-string/format, close

from toolset import sequences

GENERATED_SEQ_FILE = "generated_sequence.txt"
GENERATED_MATRIX_FILE = "generated_matrix.txt"


def store_sequence(filename, seq):

    if not len(seq):
        return

    output_file = open(filename, "w")
    for el in seq:
        output_file.write(f"{el}  \n")
    output_file.close()
        # зберігаємо елемент у файл
    # повертаємо файл (ресурс) операційній системі


def store_matrix(filename, matrix):
    if not len(matrix) or not len(matrix[0]):
        raise RuntimeError("Strictly two-dimensional matrix is required")

    n, m = len(matrix), len(matrix[0])
    with open(filename, "w") as matrix_file:
        matrix_file.write(f"{n} {m} \n")
        # зберігаємо спочатку розмірність - n m - у файл
        i = 0
        for row in matrix:
            for el in row:
                i += 1
                matrix_file.write(f"{el} ")
                if i == m:
                    matrix_file.write("\n")
                    i = 0
        matrix_file.close()
            # зберігаємо кожний елемент у файл
            # новий рядок (у разі коли це не перша строка матриці)


def main():
    n, m = 5, 5
    seq = sequences.input_data(n*m, 0, n+m)
    store_sequence(GENERATED_SEQ_FILE, seq)
    matrix = [[seq[i*m+j] for j in range(m)] for i in range(n)]
    store_matrix(GENERATED_MATRIX_FILE, matrix)


if __name__ == "__main__":
    main()