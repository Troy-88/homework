# это варинант задания после того, как я посмотрел разбор. Попробовал сделать по своему, но по верным условиям.

from datetime import datetime


class TrafficLight:
    __color = ''
    __counter = 0
    __stop = 20

    def running(self):
        while True:
            current_dt = datetime.now()
            time_in_sec = int(current_dt.hour) * 3600 + int(current_dt.minute) * 60 + int(current_dt.second)
            current_color = self.__color  # эта строчка была ниже, но там она почему-то не работала
            time = time_in_sec % run_cicle
            if time <= run_red:
                self.__color = 'Красный'
            elif (time > run_red) and (time <= run_yellow + run_red):  # сделал в скобках - Pep8 ругался
                self.__color = 'Желтый'
            else:
                self.__color = 'Зеленый'
            if current_color != self.__color:
                print(f'Сейчас горит {self.__color} сигнал светофора')
                self.__counter += 1
            #  current_color = self.__color  - тут она была изначально. Можешь объяснить, почему она не работала?
            if self.__counter == self.__stop:
                break


run_red = 5
run_yellow = 2
run_green = 3
run_cicle = run_red + run_yellow + run_green

traf_light_1 = TrafficLight()
traf_light_1.running()
