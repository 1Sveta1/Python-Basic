#!python3
import os


# Assignment 01-01
#
# Assign actual data to the variables below
# and run the script to print the output.
def start(d):
    choose = int(input("print data - 1, change - 0"))
    if choose == 1:
        start_prnt(d)
    if choose == 0:
        name = input("name: ")
        profession = input("profession: ")
        facility = input("facility: ")
        city = input("city: ")
        country = input("country: ")
        goal = input("goal: ")
        d = {'name': name,
             'profession': profession,
             'facility': facility,
             'city': city,
             'country': country,
             'goal': goal,
             }
        start_prnt(d)


def start_prnt(d):
    print("My name is " + d['name'] + " I am a " + d['profession'] + " at " + d['facility'] + "\nin " + d['city'] + ", "
          + d['country'] + "." + " I want to learn how to program \nin Python to become a " + d['goal'] + ".")


if __name__ == '__main__':
    d = {'name': 'Sveta',
         'profession': 'student',
         'facility': 'college',
         'city': 'Odesa',
         'country': 'Ukraine',
         'goal': 'Python developer',
         }
    start(d)
