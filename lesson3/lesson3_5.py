def sum_numbers(numbers):
    return sum([int(el) for el in numbers])


print('Это программа по суммированию чисел. Если хотите выйти из программы, то напишите символ "q"')
res = 0

while True:
    user_numbers = input('Введите несколько чисел через пробел: ').split()
    if 'q' in user_numbers:
        res += sum_numbers(user_numbers[:user_numbers.index('q')])
        break
    else:
        res += sum_numbers(user_numbers)
        print(res)

print(f'Проограмма завершена. Сумма всех чисел: {res}')
