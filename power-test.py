import unittest
from my_power import *


class TestPower(unittest.TestCase):
    basis = 2
    exponent = 2

    def test_basic(self):
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_exponent_is_0(self):
        self.exponent = 0
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_negative(self):
        self.basis = (-2)
        self.exponent = 3
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_negative_inverse(self):
        self.basis = 2
        self.exponent = -3
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_fractions(self):
        self.basis = 0.5
        self.exponent = 3
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_fractions2(self):
        self.basis = 2
        self.exponent = 0.5
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    # def test_ZeroDivisionError (self):
    #     self.basis = 0
    #     self.exponent = 1/2
    #     self.assertRaises()


if __name__ == '__main__':
    unittest.main()