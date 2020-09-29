"""
Unit tests for the calculator library 1
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(1, 7)
        self.assertEqual(result, 8)
        

    def test_subtraction(self):
        result = calculator.subtract(4,0)
        self.assertEqual(result, 4)
        
        
if __name__ == '__main__':
    unittest.main()
