#!python3

# Assignment 01-01
#
# Assign actual data to the variables below
# and run the script to print the output.
def start_inp():
    global name, profession, facility, city, country, goal
    name = input("name: ")
    profession = input("profession: ")
    facility = input("facility: ")
    city = input("city: ")
    country = input("country: ")
    goal = input("goal: ")
    return name, profession, facility, city, country, goal


def start_prnt():
    global name, profession, facility, city, country, goal
    name = "Sveta"
    profession = "student"
    facility = "college"
    city = "Odesa"
    country = "Ukraine"
    goal = "python developer"
    return name, profession, facility, city, country, goal


name = " "
profession = " "
facility = " "
city = " "
country = " "
goal = " "
choose = int(input("1 - input data or 2 - print data: "))
if choose == 1:
    start_inp()
    d = {'name': name,
         'profession': profession,
         'facility': facility,
         'city': city,
         'country': country,
         'goal': goal,
         }
    print("My name is " + d['name'] + " I am a " + d['profession'] + " at " + d['facility'] + "\nin " + d['city'] + ", "
          + d['country'] + "." + " I want to learn how to program \nin Python to become a " + d['goal'] + ".")
if choose == 2:
    start_prnt()
    print("My name is " + name + " I am a " + profession + " at " + facility + "\nin " + city + ", "
          + country + "." + " I want to learn how to program \nin Python to become a " + goal + ".")
