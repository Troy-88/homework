lst = []
lst_len = int(input('Введите количество элементов в списке: '))
i = 0

# заполнение списка через while
# while i < lst_len:
#     lst.append(input(f'Введите {i} элемент списка: '))
#     i += 1

# заполнение списка через for
for i in range(lst_len):
    lst.append(input(f'Введите {i} элемент списка: '))

print(lst)

for i in range(1, lst_len, 2):
    lst[i], lst[i-1] = lst[i - 1], lst[i]

print(lst)
