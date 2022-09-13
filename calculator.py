from fractions import Fraction

class Fraction_1():
    def fraction(self):
        x = int(input("Введите числитель первой дроби: "))
        y = int(input("Введите знаменатель первой дроби: "))
        self.value = Fraction(x, y)
        print("A =", self.value)
        return self.value

frac1 = Fraction_1()
a = frac1.fraction()

frac2 = Fraction_1()
b = frac2.fraction()

frac3 = a + b
print("A+B =", frac3)

frac4 = a - b
print("A-B =", frac4)

frac5 = a * b
print("A*B =", frac5)

frac6 = a / b
print("A/B =", frac6)
