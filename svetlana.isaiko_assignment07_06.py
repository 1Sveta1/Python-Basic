# Переписати цикл з використанням iter/next функцій
# підказка: idx, s[idx]
s = "Hello world!"
idx = 0
while True:
    it = iter(s[idx])
    a = next(it)
    if a == ' ':
        break
    print(a, end="")
    idx += 1
