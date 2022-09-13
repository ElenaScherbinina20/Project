from fractions import Fraction

class Fraction_1():
    def fraction(self):
        x = int(input("Введите числитель первой дроби: "))
        y = int(input("Введите знаменатель первой дроби: "))
        self.value = Fraction(x, y)
        # print("A =", self.value)
        return self.value

frac1 = Fraction_1()
a = frac1.fraction()
print("A =", a)

frac2 = Fraction_1()
b = frac2.fraction()
print("B =", b)

frac3 = a + b
print("D =", frac3)

frac4 = a - b
print("E =", frac4)

frac5 = a * b
print("I =", frac5)

frac6 = a / b
print("F =", frac6)
