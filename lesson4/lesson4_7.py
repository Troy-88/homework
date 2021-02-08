def fact(a):
    res = 1
    for i in range(2, a + 1):
        res *= i
        yield res


n = int(input('Введите целое число: '))
for el in fact(n):
    print(el)
