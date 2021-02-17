from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    count_coat = 0
    tissue_cons_all_coat = 0

    def __init__(self, v):
        Coat.count_coat += 1
        self.v = v
        Coat.tissue_cons_all_coat += round(self.v / 6.5 + 0.5, 1)

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v > 200:
            self.__v = 200
        elif v < 100:
            self.__v = 100
        else:
            self.__v = v

    def tissue_consumption(self):
        return round(self.v / 6.5 + 0.5, 1)


class Costume(Clothes):
    count_costume = 0
    tissue_cons_all_costume = 0

    def __init__(self, h):
        Costume.count_costume += 1
        self.h = h
        Costume.tissue_cons_all_costume += round(2 * self.h + 0.3, 1)

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 190:
            self.__h = 190
        elif h < 130:
            self.__h = 130
        else:
            self.__h = h

    def tissue_consumption(self):
        return round(2 * self.h + 0.3, 1)


# решил сделать абстрактный медод подсчета, который можно использовать как родитель для любых других ->
# ткань для аксессуаров, пуговицы и т.д.
class Count(ABC):
    @abstractmethod
    def counting(self):
        pass


class ClothCounting(Count):
    def counting(self):
        return f'Всего на одежду понадобится ткани {Costume.tissue_cons_all_costume + Coat.tissue_cons_all_coat}'


# не стал удалять принты, чтобы можно было сразу проверить
coat_1 = Coat(2000)
print(coat_1.tissue_consumption())

coat_2 = Coat(50)
print(coat_2.tissue_consumption())

coat_3 = Coat(180)
print(coat_3.tissue_consumption())

print(Coat.count_coat)
print(Coat.tissue_cons_all_coat)

costume_1 = Costume(110)
print(costume_1.tissue_consumption())

costume_2 = Costume(200)
print(costume_2.tissue_consumption())

tissue_cons_all = ClothCounting()
print(tissue_cons_all.counting())
