"""Функция для сокращения дробей"""
def reduce_fraction(a, b):
    while a % b != 0:
        value_1 = a
        value_2 = b
        a = value_2
        b = value_1 % value_2
    return b

"""Класс дробь"""
class Fraction:

    """Инициализая атрибутов объекта"""
    def __init__(self, num, den):
        self.num = num
        self.den = den

    """Возвращение строки"""
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    """Сумма дробей"""
    def __add__(self, fraction):
        newnum = self.num * fraction.den + self.den * fraction.num
        newden = self.den * fraction.den
        reduce_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // reduce_value, newden // reduce_value)

    """Разность дробей"""
    def __sub__(self, fraction):
        newnum = self.num * fraction.den - self.den * fraction.num
        newden = self.den * fraction.den
        reduce_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // reduce_value, newden // reduce_value)

    """Произведение дробей"""
    def __mul__(self, fraction):
        newnum = self.num * fraction.num
        newden = self.den * fraction.den
        reduce_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // reduce_value, newden // reduce_value)

    """Деление дробей"""
    def __truediv__(self, fraction):
        newnum = self.num * fraction.den
        newden = self.den * fraction.num
        reduce_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // reduce_value, newden // reduce_value)

A = Fraction(2,5)
print("Значение первой дроби: ", A)
B = Fraction(3,7)
print(f"Значение второй дроби: {B}\n"
      f"A+B= {A+B}\n"
      f"A+B= {A-B}\n"
      f"A+B= {A*B}\n"
      f"A+B= {A/B}\n")
