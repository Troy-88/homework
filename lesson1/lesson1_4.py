number = int(input('Введите число: '))
i = 0
max_of_number = 0

while i - 2 < len(str(number)):
    if max_of_number < number % 10:
        max_of_number = number % 10
    number //= 10
    i += 1

print(max_of_number)
