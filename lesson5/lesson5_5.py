with open('lesson5_5.txt', 'w') as f:
    f.write(input('Введите несколько чисел, разделенных пробелом: '))

# Получилось компактно, но насчет читаемости со стороны я не уверен.
with open('lesson5_5.txt', 'r') as f:
    print(sum(list(map(int, f.read().split(' ')))))
