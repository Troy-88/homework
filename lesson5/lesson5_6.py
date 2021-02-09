with open('lesson5_6.txt', 'r', encoding='utf-8')as f:
    file_data = f.readlines()

print(file_data)
dict_timetable = {}

for el_line in file_data:
    el_line = el_line.split(' ')
    disc_time = 0
    for i in range(1, len(el_line)):
        new_str = ''
        for j in range(len(el_line[i])):
            if el_line[i][j].isdigit():
                new_str += el_line[i][j]
        if new_str.isdigit():
            disc_time += int(new_str)
    dict_timetable[el_line[0].replace(':', '')] = disc_time

print(dict_timetable)
