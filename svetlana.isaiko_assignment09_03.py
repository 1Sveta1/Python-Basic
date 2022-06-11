# Завдання: надати можливість викликати fibonnaci функцію
#           через HTTP endpoint /fib/<NUM>, у відповідь буде
#           надсилатись послідовнісь елементів ряду Фібоначчі
#
# наприклад: request: http://localhost:5000/fib/7
#            response: "[0, 1, 1, 2, 3, 5, 8]"
#
# замінити тіло у функції з pass інструкцією

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h2>World!</h2>"


@app.route("/fib/<int:n>", methods=['GET'])
def fib(n):
    l = [0, 1]
    el = 0
    i = 0
    if n == 0:
        return jsonify(0)
    while i < (n-2):
        el = l[i] + l[i+1]
        l.append(el)
        i += 1
    return jsonify(l)
