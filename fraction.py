"""Функция для сокращения дробей"""
def reduce_fraction(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

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
        gcd_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // gcd_value, newden // gcd_value)

    """Разность дробей"""
    def __sub__(self, fraction):
        newnum = self.num * fraction.den - self.den * fraction.num
        newden = self.den * fraction.den
        gcd_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // gcd_value, newden // gcd_value)

    """Произведение дробей"""
    def __mul__(self, fraction):
        newnum = self.num * fraction.num
        newden = self.den * fraction.den
        gcd_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // gcd_value, newden // gcd_value)

    """Деление дробей"""
    def __truediv__(self, fraction):
        newnum = self.num * fraction.den
        newden = self.den * fraction.num
        gcd_value = reduce_fraction(newnum, newden)
        return Fraction(newnum // gcd_value, newden // gcd_value)

A = Fraction(2,5)
print("Значение первой дроби: ", A)
B = Fraction(3,7)
print("Значение второй дроби: ", B)
print("A+B=", A+B)
print("A-B=", A-B)
print("A*B=", A*B)
print("A/B=", A/B)
