def user_data(name, surname, bir_year, city, email, phone_num):
    return print(f'{name} {surname}. Дата рождения: {bir_year}. Место проживания: {city}. Эл. почта: {email}. Телефон: {phone_num}')


# Не стал заморачиваться с вводом данных с клавиатуры, так как в задании не было указано.
user_data(name='Имя', surname='Фамилия', bir_year=1998, city='Питер', email='Моя эл. почта', phone_num='Мой номер тел.')
