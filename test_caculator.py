from unittest import TestCase
from caculator import Calculator
from time import sleep
class TestCalculator(TestCase):
    def test_add(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(3, 7), 10)


    def test_multiply(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.multiply(3, 7), 21)
