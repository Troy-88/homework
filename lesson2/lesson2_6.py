goods = []
lst_name = []
lst_cost = []
lst_quantity = []
lst_units = []
analit_of_goods = {'название': lst_name, 'цена': lst_cost, 'количество': lst_quantity, 'ед': lst_units}
i = 1

while True:
    name = input('Введите название товара (если хотите завершить, то напечатайте "завершить"): ')
    if name == 'завершить':
        name = ''
        break
    cost = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    units = input('Какие единицы измерения количества используются?: ')
    goods.append((i, {'название': name, 'цена': cost, 'количество': quantity, 'ед': units}))
    lst_name.append(name)
    lst_cost.append(cost)
    lst_quantity.append(quantity)
    lst_units.append(units)
    i += 1

print(goods)
print(analit_of_goods)
