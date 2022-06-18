import random
from toolset import sequences


def generate(n, m):
    """Функція створення матриці"""
    lst = [[random.randint(0, 100)  for _ in range(n)] for _ in range(m)]
    return lst


def sort_matrix(r):
    """Функція сортування одновимірної матриці"""
    sequences.quicksort(r, 0, len(r) - 1)
    return r


def flatten(r, n):
    """конвертація двовимірної матриці у одновимцрну"""
    l = [elem[i] for elem in r for i in range(n)]
    return l


def roll(r, n):
    """конвертація одновимірної матриці у двовимірну"""
    lst = [r[i:i + n] for i in range(0, len(r), n)]
    return lst