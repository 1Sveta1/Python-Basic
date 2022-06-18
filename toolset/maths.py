def factorial(n):
    """Функція яка обчислює факторіал числа"""
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"{n}! == {factorial}")


def convert_to_celsius(value):
    """Converts degrees value from fahrenheit celsius to."""
    return (value - 32)/1.8


def convert_to_fahrengeit(value):
    """Converts degrees value from celsius to fahrenheit."""
    return value * 1.8 + 32


def fib(n):
    """Функція яка повертає n-елемент Фібоначчі"""
    if n == 0:
        return 0
    elif n < 4:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fibonacci_seq(n):
    """Функція повертає ряд Фібоначчі"""
    l = [0, 1]
    el = 0
    i = 0
    if n == 0:
        return 0
    elif n < 3:
        return 1
    while len(l) < n:
        el = l[i] + l[i + 1]
        l.append(el)
        i += 1
    return l
