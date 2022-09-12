from fractions import Fraction

class Fraction_1():
    def fraction_1(self):
        x1 = int(input("Введите числитель первой дроби: "))
        y1 = int(input("Введите знаменатель первой дроби: "))
        self.value1 = Fraction(x1, y1)
        print("A =", self.value1)
        return self.value1

class Fraction_2():
    def fraction_2(self):
        x2 = int(input("Введите числитель второй дроби: "))
        y2 = int(input("Введите знаменатель второй дроби: "))
        self.value2 = Fraction(x2, y2)
        print("B =", self.value2)
        return self.value2

frac1 = Fraction_1()
a = frac1.fraction_1()

frac2 = Fraction_2()
b = frac2.fraction_2()

sum = a + b
print("A+B =", sum)

minus = a - b
print("A-B =", minus)

multiplication = a * b
print("A*B =", multiplication)

divide = a / b
print("A/B =", divide)
