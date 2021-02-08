from functools import reduce


def reduce_func(prev_el, el):
    return prev_el * el


lst = [el for el in range(100, 1001) if el % 2 == 0]
print(lst)

print(reduce(reduce_func, lst))

# делал для сравнения, решил оставить
"""
res = 1
for el in lst:
    res *= el

print(res)
"""