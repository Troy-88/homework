class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_lst = []
print('Заполните список числами:')

while True:
    number = input('Введите число. Если хотите прекратить, наберите "q". ')
    if number == 'q':
        print(f'Получился список: {user_lst}')
        break
    try:
        if not number.isdigit():
            raise MyError('Нужно вводить только числа')
        user_lst.append(int(number))
    except MyError as err:
        print(err)
