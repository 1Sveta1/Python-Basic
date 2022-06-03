# Є словник з ключами-строками та елементами-списками строк, наприклад:
#

#
# Завдання: перебудувати словник таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника. Вирішити за допомогою dict
#           comprehensions.

d = {
    'colors': ['red', 'green', 'blue', 'purple'],
    'fruits': ['pineapple', 'orange', 'banana'],
    'clothes': ['coat', 'tshirt']
}

d = {i: k for k, v in d.items() for i in v}
print(d)



