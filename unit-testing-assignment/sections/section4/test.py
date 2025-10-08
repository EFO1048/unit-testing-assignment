import unittest
from my_calculations import Calculations

# This file shows that the tests don't run if
# They are not prefixed with test

class TestCalculations(unittest.TestCase):
    
    def not_a_test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')
        
    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')
        
    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')
    
    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')
        
if __name__ == '__main__':
    print("SECTION 4:\n\n")
    
    unittest.main()