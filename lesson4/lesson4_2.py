from random import randint

lst = []
for i in range(16):
    lst.append(randint(1, 100))

print(lst)

new_lst = [el for i, el in enumerate(lst[1:]) if lst[i + 1] > lst[i]]
print(new_lst)
