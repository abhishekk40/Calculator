"""
Unit tests for the calculator library
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(2, 5)
        self.assertEqual(result, 7)
        

    def test_subtraction(self):
        result = calculator.subtract(5,4)
        self.assertEqual(result, 1)
        
        
if __name__ == '__main__':
    unittest.main()
