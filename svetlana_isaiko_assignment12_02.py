# Завдання: у наданому коді замінити загальний Exception
#           у блоці обробки ексепшенів на класс ексепшену
#           конкретної помилки яка вилітає з послідовності
#
# підказка: приберіть try/except логіку взагалі а потім поверніть
#           у потрібному вигляді


if __name__ == "__main__":

    try:
        [1, 2, 3, 4, 5][5]
    except IndexError as e:
        print(e)