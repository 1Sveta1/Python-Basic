def fizzbuzz(n):
    """Функція яка є рішенням задачі fizzbuzz"""
    lst = ["Fizzbuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for
           i in range(1, n + 1)]
    return lst


if __name__ == '__main__':
    lst = fizzbuzz(20)
    print(lst)