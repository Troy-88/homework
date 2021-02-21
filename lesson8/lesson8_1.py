class Date:
    date_lst = []
    date_cls = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, date_str):
        self.date_str = date_str
        Date.date_lst = date_str.split('-')
        Date.date_cls = date_str

    @classmethod
    def get_date_dig(cls):
        # cls.date_str = date_str
        # cls.date_lst = date_str.split('-')
        cls.day = int(cls.date_lst[0])
        cls.month = int(cls.date_lst[1])
        cls.year = int(cls.date_lst[2])

# указал только базовые проверки. С соответствием количества дней конкретному месяцу не стал заморачиваться
    @staticmethod
    def check_valid_date_cls():
        Date.get_date_dig()
        if Date.day < 32:
            day_check_valid = 'День указазан верно'
        else:
            day_check_valid = 'День указан некорректно'
        if Date.month < 13:
            month_check_valid = 'Месяц указазан верно'
        else:
            month_check_valid = 'Месяц указан некорректно'
        if 2000 < Date.year:
            year_check_valid = 'Год указазан верно'
        else:
            year_check_valid = 'Год указан некорректно'
        print(f'Дата: {Date.date_cls}. {day_check_valid}. {month_check_valid}. {year_check_valid}.')


date_1 = Date('32-12-2020')
Date.check_valid_date_cls()

date_2 = Date('25-04-5')
Date.check_valid_date_cls()
