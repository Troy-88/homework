numbers = [8, 7, 5, 5, 2, 2]
i = 0
user_number = int(input('Введите натуральное число: '))

while i < len(numbers):
    if user_number > numbers[i]:
        numbers.insert(i, user_number)
        break
    i += 1
else:
    numbers.append(user_number)

print(numbers)
