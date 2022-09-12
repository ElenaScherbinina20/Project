from fractions import Fraction

class Calculator():
    """Создаем калькулятор"""

    def __init__(self):
        pass
        """Указываем значения дробей"""
        print("Дробные значения")

    def fraction_1(self):
        x1 = int(input("Введите числитель первой дроби: "))
        y1 = int(input("Введите знаменатель первой дроби: "))
        self.value1 = Fraction(x1, y1)
        print("A =", self.value1)

    def fraction_2(self):
        x2 = int(input("Введите числитель второй дроби: "))
        y2 = int(input("Введите знаменатель второй дроби: "))
        self.value2 = Fraction(x2, y2)
        print("A =", self.value2)

    def sum_f(self):
        """Суммируем выражение"""
        sum =  self.value1+ self.value2
        print("A+B =", sum)

    def minus_f(self):
        """Находим разницу"""
        minus = self.value1 - self.value2
        print("A-B =", minus)

    def divide_f(self):
        """Делим"""
        divide = self.value1 / self.value2
        print("A/B =", divide)

    def multiplication_f(self):
        """Умножаем"""
        multiplication = self.value1 * self.value2
        print("A*B =", multiplication)

numbers = Calculator()
numbers.fraction_1()
numbers.fraction_2()
numbers.sum_f()
numbers.minus_f()
numbers.divide_f()
numbers.multiplication_f()
