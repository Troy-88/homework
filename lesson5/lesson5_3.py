# почему-то не сразу до меня дошло, что "не программно", это самому. Удалять не стал, закомментировал.
# with open('lesson5_3.txt', 'w', encoding='utf-8') as f:
#     while True:
#         new_str = input('Введите фамилию сотрудника и его зарплату через пробел (пустая строка - конец записи): ')
#         if not new_str:
#             break
#         else:
#             f.write(new_str + '\n')

with open('lesson5_3.txt', 'r', encoding='utf-8') as f:
    data_file = f.readlines()

print(data_file)  # проверка чтения
lst_date = []

for el in data_file:
    lst_date.append(el.replace('\n', '').split(' '))

print(lst_date)  # проверка нового списка
av_salary = 0

for el in lst_date:
    if float(el[1]) < 20000:
        print(f'Сотрудник: {el[0]} имеет ЗП менее 20000. Его ЗП: {el[1]}.')
    av_salary += float(el[1])

print(f'Средняя запрлата сотрудников равна: {av_salary / len(lst_date)}')
