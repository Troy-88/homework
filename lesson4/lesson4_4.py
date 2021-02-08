from random import randint

lst = []
for i in range(10):
    lst.append(randint(1, 10))

print(lst)

print([el for el in lst if lst.count(el) == 1])
