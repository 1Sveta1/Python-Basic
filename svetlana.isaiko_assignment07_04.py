# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0
#

n = int(input("Введіть розмір матриці: "))
a = [[j+1 if i == j else 0 for i in range(n)] for j in range(n)]
for i in range(n):
    print(a[i])
