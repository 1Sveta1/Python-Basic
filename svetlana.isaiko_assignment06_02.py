# Є словник з ключами-строками та елементами-списками строк, наприклад:
#

#
# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.
#

d = {
    'colors': ['red', 'green', 'blue', 'purple'],
    'fruits': ['pineapple', 'orange', 'banana'],
    'clothes': ['coat', 'tshirt']
}

for k in list(d.keys()):
    v = d.pop(k)
    for i in v:
        d[i] = k
print(d)