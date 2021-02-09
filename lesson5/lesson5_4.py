def fuck_change_word(lst):
    for el_f in lst:
        el_f = el_f.split(' ')
        yield ' '.join([dict_numbers[el_f[0]], el_f[1], el_f[2]])


dict_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('lesson5_4.txt', 'r', encoding='utf-8') as f:
    file_data = f.readlines()

gen_lines = fuck_change_word(file_data)

with open('lesson5_4_new.txt', 'w', encoding='utf-8') as f:
    for el in gen_lines:
        f.write(el)
