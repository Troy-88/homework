time = int(input('Введите время в секундах: '))

hours = time // 60 // 60
minutes = time // 60 % 60
seconds = time % 60 % 60

print(f'Вы ввели время в секундах: {time}. Получится такое время (чч:мм:сс): {hours:02d}:{minutes:02d}:{seconds:02d}')
