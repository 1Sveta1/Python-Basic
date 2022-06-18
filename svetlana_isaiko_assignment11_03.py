"""Завдання: надати деякі функції з пакету першого завдання через web api (набір ендпоінтів на сервері)."""

from flask import Flask
from toolset import maths, matrices, sequences

app = Flask(__name__)


@app.route("/toolset/sequences/<word>/")
def letter_stats_handler(word):
    result = sequences.letter_stats(word)
    return dict(result=result)


@app.route("/toolset/maths/to_celsius/<float:degrees>/")
def to_celsius_handler(degrees):
    result = maths.convert_to_celsius(degrees)
    return dict(result=f"{result}F")


@app.route("/toolset/maths/to_fahrenheit/<float:degrees>/")
def to_fahrengeit_handler(degrees):
    result = maths.convert_to_fahrengeit(degrees)
    return dict(result=f"{result}C")


@app.route("/toolset/matrices/generate/<int:n>/<int:m>/")
def generate_matrix_handler(n, m):
    return {
        "result": matrices.generate(n, m),
    }


if __name__ == "__main__":
    app.run()
