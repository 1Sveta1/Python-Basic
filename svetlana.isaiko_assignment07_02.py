# Є список (не пайтонівський) чисел (генерований рандомно
# чи заданий вручну) - порахувати унікальні числа у ньому
#
# Наприклад:
#  e 1, 2, 1, 3, 4, 5, 6, 6, 6
#  унікальних 6 (1 повторюється двічі, 6 тричи - три числа не враховуються)
#
# l = 1, 2, 4, 5, 6, 8, 99, 99, 100, 100, 1, 1, 1
# unique_l = set(l)
# for i in unique_l:
#     amount = l.count(i)
#     if amount > 1:
#         print(f"{i} = {amount}",  end=" ")
# print(f"\nУнікальних значень {len(unique_l)}: {unique_l}")


def data_to_count():
    """Функція яка повертяє дані"""
    l = 1, 2, 4, 5, 6, 8, 99, 99, 100, 100, 1, 1, 1
    unique_l = set(l)
    return l, unique_l


def repetition_count(l, unique_l):
    """Функція рахує кількість повторів кожного елемента. Для виводу використовується словник"""
    number_count = {}
    amount = 0
    for i in unique_l:
        amount = l.count(i)
        if amount > 1:
            number_count[i] = amount
    return number_count


def main():
    """Функція головна, в якій з'єднуються всі попередні та взаємодіють між собою"""
    l, unique_l = data_to_count()
    number_count = repetition_count(l, unique_l)
    print(f"\nУнікальних значень {len(unique_l)}: {unique_l}"
          f"\nЧисла яка повторюються(число - кількість повторів) {number_count}")


if __name__ == "__main__":
    main()
