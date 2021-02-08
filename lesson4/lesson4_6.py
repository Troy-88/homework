import itertools

# а) итератор, генерирующий целые числа, начиная с указанного
iter_1_param = input('Введите начало итератора, шаг и завершение через пробел: ').split()

iter_1 = itertools.count(int(iter_1_param[0]), int(iter_1_param[1]))

for el in iter_1:
    if el >= int(iter_1_param[2]):
        break
    else:
        print(el, end=' ')

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
iter_2_param = int(input('\nВведите количество повторений для cicle: '))
lst = [1, 2, 5, 6, 3, 2]
iter_2 = itertools.cycle(lst)
count = 0

for el in iter_2:
    if count >= iter_2_param:
        break
    else:
        print(el, end=' ')
        count += 1
