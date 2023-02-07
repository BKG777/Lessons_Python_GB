# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def __add__(self, other):
        return ComplexNumber(self.re1 + other.re1, self.re2 + other.re2)

    def __mul__(self, other):
        return ComplexNumber((self.re1 * other.re1 - self.re2 * other.re2),
                             (self.re1 * other.re1 + other.re2 * self.re2))

    def __str__(self):
        return f'{self.re1}{" +" if self.re2 >= 0 else " "}{self.re2}i'


cn_1 = ComplexNumber(4, -1)
cn_2 = ComplexNumber(1, -2)
cn_3 = ComplexNumber(0, 0)

print(cn_1 + cn_2)
print(cn_1 * cn_2)
print(cn_1 + cn_2 + cn_3)
print(cn_1 * cn_2 * cn_3)
