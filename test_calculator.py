"""
Unit tests for the calculator library
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(2, 7)
        self.assertEqual(result, 9)
        

    def test_subtraction(self):
        result = calculator.subtract(4,1)
        self.assertEqual(result, 3)
        
        
if __name__ == '__main__':
    unittest.main()
