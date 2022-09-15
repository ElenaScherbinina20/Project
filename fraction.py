import math
class Fraction:
    """Класс дробь"""

    def __init__(self, num, den):
        """Инициализая атрибутов объекта"""
        k = math.gcd(num, den)
        self.num = num // k
        self.den = den // k

    def __str__(self):
        """Возвращение строки"""
        return str(self.num) + "/" + str(self.den)

    def __add__(self, fraction):
        """Сумма дробей"""
        newnum = self.num * fraction.den + self.den * fraction.num
        newden = self.den * fraction.den

        return Fraction(newnum, newden)

    def __sub__(self, fraction):
        """Разность дробей"""
        newnum = self.num * fraction.den - self.den * fraction.num
        newden = self.den * fraction.den

        return Fraction(newnum, newden)

    def __mul__(self, fraction):
        """Произведение дробей"""
        newnum = self.num * fraction.num
        newden = self.den * fraction.den

        return Fraction(newnum, newden)

    def __truediv__(self, fraction):
        """Деление дробей"""
        newnum = self.num * fraction.den
        newden = self.den * fraction.num

        return Fraction(newnum, newden)

class Exponentiate(Fraction):
    def __init__(self, num, den):
        super().__init__(num, den)

    def __pow__(self, other):
        newnum = self.num**other
        newden = self.den**other

        return Exponentiate(newnum, newden)

E = Exponentiate(2, 5)
print("Дробь возведенна в степень: ", E**3)

A = Fraction(2,5)
print("Значение первой дроби: ", A)

B = Fraction(3,7)
print(f"Значение второй дроби: {B}\n"
      f"A+B= {A+B}\n"
      f"A-B= {A-B}\n"
      f"A*B= {A*B}\n"
      f"A/B= {A/B}\n")
