import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(1, 2, '+'), 3)

    def test_subtract(self):
        self.assertEqual(calculate(5, 3, '-'), 2)

    def test_multiply(self):
        self.assertEqual(calculate(4, 3, '*'), 12)

    def test_divide(self):
        self.assertEqual(calculate(10, 2, '/'), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, '/')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, '%')

if __name__ == '__main__':
    unittest.main()
