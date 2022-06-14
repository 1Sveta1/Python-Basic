import random
import quicksort as quick
import bubble


def generate_matrix(n, m):
    """Функція створення матриці"""
    lst = [[random.randint(0, 100) for _ in range(n)] for _ in range(m)]
    return lst


def sort_matrix(l, n):
    """Функція для сортування  матриці"""
    quick.quicksort(l, 0, len(l) - 1)
    return l


def print_matrix(lst):
    """Функція для виводу  матриці на екран"""
    print(lst)



