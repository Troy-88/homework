def count_lines_str(lst):
    for i in range(len(lst)):
        count = 0
        line = lst[i].replace('\n', '')
        if line[0] != ' ':
            count += 1  # учет первого слова, если строка начинается со слова, а не пробела
        for j in range(len(line) - 1):
            if line[j] == ' ' and line[j + 1] != ' ':
                count += 1
        yield f'В строке {i + 1} слов: {count}.'


# почему-то не сразу до меня дошло, что "не программно", это самому. Удалять не стал, закомментировал.
# with open('lesson5_2.txt', 'w', encoding='utf-8') as f:
#     while True:
#         new_str = input('Введите строку для записи в файл (если строка пустая - запись завершится): ')
#         if not new_str:
#             break
#         else:
#             f.write(new_str + '\n')

with open('lesson5_2.txt', 'r') as f:
    file_data = f.readlines()

generator = count_lines_str(file_data)
for el in generator:
    print(el)

print(f'Всего в файле строк: {len(file_data)}.')
