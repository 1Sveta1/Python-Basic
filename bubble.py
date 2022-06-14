def bubble_sort(l):
    """Функція для сортування списка"""
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l
