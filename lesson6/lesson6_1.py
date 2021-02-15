# Есть немаленький шанс что я неверно понял условие задачи.
# В общем я подумал и решил сделать привязку к текущему времени.
# Т.е. при расчете я исхожу из того, что цикл смены цветов обнуляется в 00:00 каждый день.

from datetime import datetime


class TrafficLight:
    __color = ''

    def running(self, time):
        time = time % run_cicle
        if time <= run_red:
            self.__color = 'Красный'
        elif (time > run_red) and (time <= run_yellow + run_red):  # сделал в скобках - Pep8 ругался
            self.__color = 'Желтый'
        else:
            self.__color = 'Зеленый'
        print(f'Сейчас горит {self.__color} сигнал светофора')


current_dt = datetime.now()
time_in_sec = int(current_dt.hour) * 3600 + int(current_dt.minute) * 60 + int(current_dt.second)
run_red = 7
run_yellow = 2
run_green = 15
run_cicle = run_red + run_yellow + run_green

# Насчет усложнения. Как я понимаю, я уже изначально заложил корректность цикла смены цветов.
# И как можно в таком формате нарушить я не понимаю. Соответственно теряется смысл проверки.

traf_light_1 = TrafficLight()

traf_light_1.running(time_in_sec)
