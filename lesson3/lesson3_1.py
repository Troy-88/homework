def num_div(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError as zer:
        return 'Нельзя делить на 0'


a = int(input('Введите первое число (делимое): '))
b = int(input('Введите второе число (делитель): '))
print(num_div(a, b))
