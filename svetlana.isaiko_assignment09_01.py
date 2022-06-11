# Завдання: налаштувати flask на локальній машині
#
# 1. інсталювати flask
#
#    > python3 -m pip install flask
#    або
#    > sudo python3 -m pip install flask
#    або, для віндоувс
#    > py -3 -m pip install flask
#    для перевірки що пакет було встановлено
#    > python3 -m flask --version
#    або, для віндоувс
#    > py -3 -m flask --version
# 2. інсталювати postman (опціонально, але бажано)
# 3. запустити розробницький сервер flask (
#    на віндоувс може бути потреба експортувати
#    C:\Users\saen\AppData\Local\Programs\Python\Python37\Scripts\
#    у Environment системи щоб можливо було запускати з будьякого місця)
#    > FLASK_APP=assignment01_02 flask run
# 4. надіслати запит та отримати відповідь
#
#    у браузері набрати http://localhost:5000/hello
#    та побачити World! у відповідь

from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h2>World!</h2>"
