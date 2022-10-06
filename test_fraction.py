from unittest import TestCase, main
from Fraction import Fraction


class Test_Fraction(TestCase):

    def setUp(self):
        self.A1 = Fraction(2, 5)
        self.B1 = Fraction(3, 7)

        self.B2 = Fraction(-2, 3)
        self.A2 = Fraction(-3, 6)

    def test_init(self):
        self.assertEqual((self.A1.num, self.A1.den), (int(2), int(5)))
        self.assertEqual((self.B1.num, self.B1.den), (int(3), int(7)))

        self.assertEqual((self.A2.num, self.A2.den), (int(-1), int(2)))
        self.assertEqual((self.B2.num, self.B2.den), (int(-2), int(3)))

    def test_str(self):
        self.assertTrue(str(self.A1) == (str(2) + "/" + str(5)))
        self.assertTrue(str(self.B1) == (str(3) + "/" + str(7)))

        self.assertTrue(str(self.A2) == (str(-1) + "/" + str(2)))
        self.assertTrue(str(self.B2) == (str(-2) + "/" + str(3)))

    def test_add(self):
        result_add_1 = self.A1 + self.B1
        self.assertEqual((result_add_1.num, result_add_1.den), (29, 35))

        result_add_2 = self.A2 + self.B2
        self.assertEqual((result_add_2.num, result_add_2.den), (-7, 6))

    def test_sub(self):
        result_sub_1 = self.A1 -self.B1
        self.assertEqual((result_sub_1.num, result_sub_1.den), (-1, 35))

        result_sub_2 = self.A2 - self.B2
        self.assertEqual((result_sub_2.num, result_sub_2.den), (1, 6))

    def test_mul(self):
        result_mul_1 = self.A1 * self.B1
        self.assertEqual((result_mul_1.num, result_mul_1.den), (6, 35))

        result_mul_2 = self.A2 * self.B2
        self.assertEqual((result_mul_2.num, result_mul_2.den), (1, 3))

    def test_div(self):
        result_div_1 = self.A1 / self.B1
        self.assertEqual((result_div_1.num, result_div_1.den), (14, 15))

        result_div_2 = self.A2 / self.B2
        self.assertEqual((result_div_2.num, result_div_2.den), (-3, -4))

    def test_types(self):
        self.assertRaises(TypeError, Fraction, ("2", 2))
        self.assertRaises(TypeError, Fraction, (5 + 2j, 2))
        self.assertRaises(TypeError, Fraction, ([16, 22], 2))
        self.assertRaises(TypeError, Fraction, ([42], 2))


if __name__ == "__main__":
    main()
