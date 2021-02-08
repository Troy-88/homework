from sys import argv

script_name, work_hours, rate_hour, bonus = argv

print(f'Кол-во рабочих часов: {work_hours}. Ставка в час: {rate_hour}. Премия: {bonus}. Итого ЗП: '
      f'{(int(work_hours) * int(rate_hour) + int(bonus))}')
