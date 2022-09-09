from fractions import Fraction

class Calculator():
    """Создаем калькулятор"""

    def __init__(self):
        """Указываем значения дробей"""
        
        print("Дробные значения")
        x1 = int(input("Введите числитель первой дроби: "))
        y1 = int(input("Введите знаменатель первой дроби: "))
        self.num1 = Fraction(x1, y1)
        print("A =", self.num1)

        x2 = int(input("Введите числитель второй дроби: "))
        y2 = int(input("Введите знаменатель второй дроби: "))
        self.num2 = Fraction(x2, y2)
        print("B =", self.num2)

    def sum_f(self):
        """Суммируем выражение"""
        sum = self.num1+self.num2
        print("A+B =", sum)

    def minus_f(self):
        """Находим разницу"""
        minus = self.num1-self.num2
        print("A-B =", minus)

    def divide_f(self):
        """Делим"""
        divide = self.num1/self.num2
        print("A/B =", divide)

    def multiplication_f(self):
        """Умножаем"""
        multiplication = self.num1 * self.num2
        print("A*B =", multiplication)

numbers = Calculator()
numbers.sum_f()
numbers.minus_f()
numbers.divide_f()
numbers.multiplication_f()
