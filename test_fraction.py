from unittest import TestCase, main
from Fraction import Fraction

class Test_Fraction(TestCase):

    def setUp(self):
        self.A1 = Fraction(2, 5)
        self.B1 = Fraction(3, 7)

        self.A2 = Fraction(-3, 65)
        self.B2 = Fraction(-20, -30)

    def test_init(self):
        self.assertEqual((self.A1.num, self.A1.den), (int(2), int(5)))
        self.assertEqual((self.B1.num, self.B1.den), (int(3), int(7)))

        self.assertEqual((self.A2.num, self.A2.den), (int(-3), int(65)))
        self.assertEqual((self.B2.num, self.B2.den), (int(-2), int(-3)))

    def test_str(self):
        self.assertTrue(str(self.A1) == (str(2) + "/" + str(5)))
        self.assertTrue(str(self.B1) == (str(3) + "/" + str(7)))

        self.assertTrue(str(self.A2) == (str(-3) + "/" + str(65)))
        self.assertTrue(str(self.B2) == (str(-2) + "/" + str(-3)))
        
    def test_add(self):
        self.assertEqual(str(self.A1 + self.B1), (str(29) + "/" + str(35)))
        self.assertEqual(str(self.A2 + self.B2), (str(-121) + "/" + str(-195)))

    def test_sub(self):
        self.assertEqual(str(self.A1 - self.B1), (str(-1)+ "/" + str(35)))
        self.assertEqual(str(self.A2 - self.B2), (str(139) + "/" + str(-195)))

    def test_mul(self):
        self.assertEqual(str(self.A1 * self.B1), (str(6) + "/" + str(35)))
        self.assertEqual(str(self.A2 * self.B2), (str(2) + "/" + str(-65)))

    def test_div(self):
        self.assertEqual(str(self.A1 / self.B1), (str(14) + "/" + str(15)))
        self.assertEqual(str(self.A2 / self.B2), (str(9) + "/" + str(-130)))

    def test_types(self):
        self.assertRaises(TypeError, Fraction, ("2", 2))
        self.assertRaises(TypeError, Fraction, (5+2j, 2))
        self.assertRaises(TypeError, Fraction, ([16, 22], 2))
        self.assertRaises(TypeError, Fraction, ([42], 2))

if __name__ == "__main__":
    main()
