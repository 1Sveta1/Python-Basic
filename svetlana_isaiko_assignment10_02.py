# Завдання: модіфікувати попереднє завдання для роботи через веб сервер
#           надати можливість доступу через endpoint.
#
# Приклад: GET http://localhost:5000/matrix/5/5/sort
#          response включає result поле с відсортованими елеменатми
#          матриці.

import random
from flask import Flask
import matrix

app = Flask(__name__)


@app.route("/matrix/<int:n>/<int:m>/sort")
def sort_matrix(n, m):
    """Замінити тіло функції на використання власного модуля matrix."""
    lst = matrix.generate_matrix(n, m)
    lst = matrix.sort_matrix(lst, n)
    return dict(rows=n, cols=m, result=lst)