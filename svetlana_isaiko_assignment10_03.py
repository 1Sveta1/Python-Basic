# Завдання: розширити matrix модуль з sort_matrix_bubble
#           де буде імплементоване сортування бульбашкою.
#           Розширити matrix/n/m/sort endpoint з наступного
#           завдання підтримкою бабл сорту поряд з quicksort'ом

import random
from flask import Flask, jsonify
import matrix1

app = Flask(__name__)


# @app.route("/matrix/<int:n>/<int:m>/sort/")  # make sort_algo optional query path
@app.route("/matrix/<int:n>/<int:m>/sort/<sort_algo>")
def sort_matrix(n, m, sort_algo="quick"):
    """Замінити тіло функції на використання власного модуля matrix."""
    lst = matrix1.generate_matrix(n, m)
    l = [elem[i] for elem in lst for i in range(n)]
    if sort_algo == "bubble":
        l = matrix1.bubble.bubble_sort(l)
    elif sort_algo == "quick":  # цей блок треба переюзати з попереднього завдання
        l = matrix1.sort_matrix(l, n)
    else:
        return jsonify("invalid input")
    lst = [l[i:i + n] for i in range(0, len(l), n)]
    return jsonify(lst)

