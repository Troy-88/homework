# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, bi):
        self.num_comp = complex(a, bi)

    def __add__(self, other):
        res = self.num_comp + other.num_comp
        return ComplexNumber(res.real, res.imag)

    def __mul__(self, other):
        res = self.num_comp * other.num_comp
        return ComplexNumber(res.real, res.imag)


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(a.num_comp)
print(b.num_comp)

c = a + b
print(c.num_comp)

d = a * b
print(d.num_comp)
