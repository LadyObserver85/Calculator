import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 5), 10)
        self.assertEqual(self.calculator.result, 10)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(4, 2), float(2))
        self.assertEqual(self.calculator.result, float(2))

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(5), float(25))
        self.assertEqual(self.calculator.result, float(25))

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.square_root(16), float(4))
        self.assertEqual(self.calculator.result, float(4))


if __name__ == '__main__':
    unittest.main()
