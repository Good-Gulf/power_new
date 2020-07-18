import unittest
from my_power import *


class TestPower(unittest.TestCase):
    def setUp(self) -> None:
        self.basis = 2
        self.exponent = 2

    def test_basic(self):
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_negative(self):
        self.basis = (-2)
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_fractions(self):
        self.basis = 0.5
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))

    def test_fractions2(self):
        self.basis = 2
        self.exponent = 0.5
        result = pow(self.basis, self.exponent)
        self.assertEqual(result,my_power(self.basis, self.exponent))


if __name__ == '__main__':
    unittest.main()