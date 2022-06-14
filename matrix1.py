import random
import quicksort as quick


def generate_matrix(n, m):
    """Функція створення матриці"""
    lst = [[random.randint(0, 100)  for _ in range(n)] for _ in range(m)]
    return lst


def sort_matrix(lst, n):
    """Функція для сортування  матриці"""
    l = [elem[i] for elem in lst for i in range(n)]
    quick.quicksort(l, 0, len(l) - 1)
    lst = [l[i:i + n] for i in range(0, len(l), n)]
    return lst


def print_matrix(lst):
    """Функція для виводу  матриці на екран"""
    print(lst)



