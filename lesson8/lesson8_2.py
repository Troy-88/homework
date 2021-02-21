class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = 5  # делимое
b = 0  # делитель

try:
    if b == 0:
        raise MyZeroDivisionError('Нельзя делить на 0!')
    print(a // b)
except MyZeroDivisionError as err:
    print(err)
finally:
    print('Программа завершена')
