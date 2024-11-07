import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    ### ADD ###
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
    
    ### SUBTRACT ###
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-3, -1), -2)

    ### MULTIPLY ###
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_both_negative(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    ### DIVIDE ###
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(5, 1), 5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_both_negative(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_by_zero(self):
            self.assertEqual(self.calc.divide(5, 0), "Undefined")
    
    ### MODULO ###
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)

    def test_modulo_without_remainder(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)

    def test_modulo_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-5, 3), 1)

if __name__ == '__main__':
    unittest.main()