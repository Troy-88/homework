class Vector:
    def __init__(self, arr):
        self.arr = arr

    # def __iadd__(self, other):
    #     self.arr += other.arr
    #     return self
    # В этом случае получается операция .extend

    def __iadd__(self, other):
        for i in range(len(self.arr)):
            self.arr[i] += other.arr[i]
        return self

    def __add__(self, other):
        for i in range(len(self.arr)):
            self.arr[i] += other.arr[i]
        return self

    def __str__(self):
        return f'Вектор {self.arr}'


v_1 = Vector([1, 2, 5, 6, 7])
print(v_1)
v_2 = Vector([3, -1, 2, 4, 1])
print(v_2)
v_3 = v_1 + v_2
print(v_3)

v_1 += v_2
# Как показала практика, их нельзя использовать для одного класса, т.к. __add__ в '+=' также перегружает '+'
# Еще одна разница в том, что __add__ создает новый объект класса, а __iadd__ меняет уже существующий
print(v_1)


# в сети ничего особенного не нашел, только на одном ресурсе это:
# You shouldn't implement __iadd__ if your class represents immutable objects. In that case just implement __add__
# which will be used to override += instead. For example you can use += on immutable types such as strings and integers,
# which couldn't be done using __iadd__
# https://stackoverflow.com/questions/1047021/overriding-in-python-iadd-method
