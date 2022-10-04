from unittest import TestCase, main
from Fraction import Fraction
import math

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

        self.assertTrue(str(self.A2) == (str(-3) + "/" + str(65)))
        self.assertTrue(str(self.B2) == (str(-2) + "/" + str(-3)))

    def test_add(self):
        self.assertEqual(((int(self.A1.num) * int(self.B1.den) + int(self.B1.num)*int(self.A1.den)),
                          (int(self.A1.den) * int(self.B1.den))), (29, 35))

        self.assertEqual(((int(self.A2.num) * int(self.B2.den) + int(self.B2.num) * int(self.A2.den)),
                          (int(self.A2.den) * int(self.B2.den))), (-7, 6))

    def test_sub(self):
        self.assertEqual(((int(self.A1.num) * int(self.B1.den) - int(self.B1.num) * int(self.A1.den)),
                          (int(self.A1.den) * int(self.B1.den))), (-1, 35))

        self.assertEqual(((int(self.A2.num) * int(self.B2.den) - int(self.B2.num) * int(self.A2.den)),
                          (int(self.A2.den) * int(self.B2.den))), (1, 6))

    def test_mul(self):
        self.assertEqual((int(self.A1.num) * int(self.B1.num),
                          (int(self.A1.den) * int(self.B1.den))), (6, 35))
       
        self.assertEqual((int(self.A2.num) * int(self.B2.num),
                          (int(self.A2.den) * int(self.B2.den))), (2, 6))

    def test_div(self):
        self.assertEqual((int(self.A1.num) * int(self.B1.den),
                          (int(self.A1.den)* int(self.B1.num))), (14, 15))

        self.assertEqual((int(self.A2.num) * int(self.B2.den),
                          (int(self.A2.den) * int(self.B2.num))), (-3, -4))

    def test_types(self):
        self.assertRaises(TypeError, Fraction, ("2", 2))
        self.assertRaises(TypeError, Fraction, (5+2j, 2))
        self.assertRaises(TypeError, Fraction, ([16, 22], 2))
        self.assertRaises(TypeError, Fraction, ([42], 2))

if __name__ == "__main__":
    main()
