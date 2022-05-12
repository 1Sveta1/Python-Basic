#!/usr/bin/python3
# Assignment 02-01
from math import pi


def volume_calculation():
    r, h = input_data()
    volume = pi * r ** 2 * h
    return volume


def input_data():
    r = float(input("input radius"))
    h = float(input("input height"))
    return r, h


if __name__ == '__main__':
    while True:
        choose = int(input("We continue? 1 - yes, 0 - no"))
        if choose == 1:
            volume = volume_calculation()
            print("cylinder volume = " + str(volume))
        if choose == 0:
            break
