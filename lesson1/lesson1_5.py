proceeds = int(input('Введите какую выручку получила фирма: '))
costs = int(input('Введите какие издержки у фирмы: '))

if proceeds > costs:
    print('Фирма прибыльна!')
    profit = (proceeds - costs) / proceeds
    print(f'Рентабельность равна: {profit:.2f}')
    profit_on_staff = (proceeds - costs) / int(input('Сколько сотрудников в фирме: '))
    print(f'Рентабельность на одного сотрудника: {profit_on_staff:.2f}')
else:
    print('Фирма работает в убыток!')
