#!/usr/bin/python3
from math import sqrt


# Assignment 03-01
#
# Задача: знайти та виведіть на екран - чи належіть точка кільцю 
#      (площа між двома колами з однаковим центром та різним радіусом)
#
# Варіанти виводу на екран:
#
#      1. "Точка (Px, Py) належить кільцю за центром у точці (Cx, Cy), та r1 = R1, r2 = R2"
#      2. "Точка (Px, Py) не належить кільцю за центром у точці (Cx, Cy), та r1 = R1, r2 = R2"
#
# Формула відстані від заданої до центру кола: 
#           
#      L = sqrt((Px-Cx)^2 + (Py-Cy)^2), 
#          
#      якщо умова - r1 < L < r2 - виконується - точка належить кільцю, 
#      інакше - ні
#
#      де: 
#          L - відстань між двома точками з коордінатами
#          Px, Py - координата точки
#          Cx, Cy - координата центру кола r1 та r2
#          r1, r2 - радіус внутрішньго/зовнішнього кола 
#
# Приклад приналежності:
#
# Cx = 0, Cy = 0
# r1 = 3
# r2 = 7
# Px = 4, Py = 5
#
# L = sqrt((4-0)^2 + (5-0)^2) == 6.4
# 3 < 6.4 < 7 то ж точка з такою координатою лежить у площі кільця
#

# Px = int(input("Введіть Px:"))  # приклад зчитування значення від користувача

# частина інструкції if для виводу остаточного результату
# else:
#    print(f"Точка ({Px}, {Py}) не належить кільцю за центром у точці ({Cx}, {Cy}), та r1 = {r1}, r2 = {r2}")

def read():
    return {"Px": float(input("Point coordinate Px: ")),
            "Py": float(input("Point coordinate Py: ")),
            "Cx": float(input("Point coordinate Cx: ")),
            "Cy": float(input("Point coordinate Cy: ")),
            "r1": float(input("radius of the inner circle: ")),
            "r2": float(input("radius of the outer circle: "))}


def calculation(d):
    l = sqrt((d.get("Px") - d.get("Cx")) ** 2 + (d.get("Py") - d.get("Cy")) ** 2)
    return l


def value_check():
    d = read()
    l = calculation(d)
    if d.get("r1") < l < d.get("r2"):
        a = "The point ({0}, {1}) belongs to the ring centered at the point ({2}, {3}) and {4} = R1, {5} = R2"
    else:
        a = "The point ({0}, {1}) does not belongs to the ring centered at the point ({2}, {3}) and {4} = R1, {5} = R2"
    print(a.format(d.get("Px"), d.get("Py"), d.get("Cx"), d.get("Cy"), d.get("r1"), d.get("r2")))


if __name__ == '__main__':
    d = {}
    while True:
        choose = int(input("1 - check if a point belongs to a circle: "))
        if choose == 1:
            value_check()
        else:
            break
