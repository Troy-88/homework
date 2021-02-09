import json

firm_lst = []
all_firm_dict = {}
unprof_firm_lst = []
unprof_firm_dict = {}
zero_firm_list = []
zero_firm_dict = {}
average_profit_dict = {}

with open('lesson5_7.txt', 'r', encoding='utf-8') as f:
    count = 0
    average_profit = 0
    while True:
        file_data = f.readline()
        if not file_data:
            break
        firm_date = file_data.split(' ')
        profit = round(float(firm_date[2]) - float(firm_date[3]), 2)
        print(f'{firm_date[0]}. Форма собственности: {firm_date[1]}. Прибыль: {profit}')
        if profit < 0:
            unprof_firm_lst.append([firm_date[0], profit])
        else:
            average_profit += profit
            count += 1
            # про фирмы с нулевым балансом ничего не сказано, поэтому включил тоже в расчет средней прибыли
        if profit == 0:
            zero_firm_list.append([firm_date[0], profit])
        all_firm_dict[firm_date[0]] = profit

average_profit = round(average_profit / count, 2)
print(f'Средняя прибыль у доходных фирм: {average_profit}')

average_profit_dict['average_profit'] = average_profit
unprof_firm_dict['unprofitable'] = unprof_firm_lst
firm_lst.extend([all_firm_dict, average_profit_dict, unprof_firm_dict or 'Убыточных фирм нет',
                 zero_firm_dict or 'Нет фирм с нулевой прибылью'])

with open('lesson5_7.json', 'w', encoding='utf-8') as f:
    json.dump(firm_lst, f)

# проверка
with open('lesson5_7.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
