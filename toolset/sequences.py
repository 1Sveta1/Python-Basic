import random


def count_element(l, el):
    """підрахунок елементу у послідовності"""
    return l.count(el)


def sort_buble(l):
    """Функція використання алгоритма bubble-sort"""
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l


def input_data(n, a, b):
    """рандомний список довжиною N, з елементами у діапазоні a-b """
    l = []
    for _ in range(0, n):
        l.append(random.randint(a, b))
    return l


def letter_stats(text):
    """Функція яка рахує кількість  повторень кожної літери в реченні"""
    letter_count = {}
    for i in text:
        if i != '':
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    return letter_count


def word_stats(text):
    """Функція яка рахує кількість  повторень кожного слова в реченні"""
    count_word = {}
    for i in text:
        if i != '':
            if i in count_word:
                count_word[i] += 1
            else:
                count_word[i] = 1
    return count_word


def partition(seq, left_idx, right_idx):
    pivot = left_idx

    for i in range(left_idx + 1, right_idx + 1):
        if seq[i] < seq[left_idx]:
            pivot += 1
            seq[i], seq[pivot] = seq[pivot], seq[i]
    seq[left_idx], seq[pivot] = seq[pivot], seq[left_idx]
    return pivot


def quicksort(seq, left_idx, right_idx):
    """Функція для сортування. Використовує функцію partition"""
    if left_idx >= right_idx:
        return
    pivot = partition(seq, left_idx, right_idx)
    quicksort(seq, left_idx, pivot - 1)
    quicksort(seq, pivot + 1, right_idx)


def linear_search(seq, element):
    """Лінейний пошук"""
    for i in range(len(seq)):
        if seq[i] == element:
            return i
    return -1


def binary_search(seq, element, start, end):
    """Бінарний пошук з використанням  рекурсії"""
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == seq[mid]:
        return mid

    if element < seq[mid]:
        return binary_search(seq, element, start, mid - 1)
    else:
        return binary_search(seq, element, mid + 1, end)
