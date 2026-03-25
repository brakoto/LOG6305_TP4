import unittest
from typing import List, Tuple
from poly_llm.to_test.find_closest_elements import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    
    def test_basic_cases_from_docstring(self):
        """Test the examples from the docstring"""
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
    
    def test_simple_cases(self):
        """Test simple cases with just a few elements"""
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))
        self.assertEqual(find_closest_elements([1.0, 1.5]), (1.0, 1.5))
        self.assertEqual(find_closest_elements([1.0, 1.0]), (1.0, 1.0))
    
    def test_integer_like_floats(self):
        """Test cases with integer-like floats"""
        self.assertEqual(find_closest_elements([1.0, 3.0, 5.0, 7.0]), (1.0, 3.0))
        self.assertEqual(find_closest_elements([10.0, 20.0, 15.0, 25.0]), (10.0, 15.0))
    
    def test_negative_numbers(self):
        """Test cases with negative numbers"""
        self.assertEqual(find_closest_elements([-5.0, -3.0, 1.0, 3.0]), (-3.0, 1.0))
        self.assertEqual(find_closest_elements([-2.0, -1.0, 0.0, 1.0]), (-2.0, -1.0))
        self.assertEqual(find_closest_elements([-10.0, -9.5, -8.0]), (-9.5, -8.0))
    
    def test_duplicates(self):
        """Test cases with duplicate values"""
        self.assertEqual(find_closest_elements([1.0, 1.0, 2.0, 3.0]), (1.0, 1.0))
        self.assertEqual(find_closest_elements([5.0, 3.0, 5.0, 1.0]), (5.0, 5.0))
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0]), (1.0, 1.0))
    
    def test_decimal_precision(self):
        """Test cases with decimal precision"""
        self.assertEqual(find_closest_elements([1.1, 1.11, 1.111]), (1.11, 1.111))
        self.assertEqual(find_closest_elements([1.23, 1.24, 1.25]), (1.24, 1.25))
        self.assertEqual(find_closest_elements([0.1, 0.01, 0.001]), (0.001, 0.01))
    
    def test_large_numbers(self):
        """Test cases with large numbers"""
        self.assertEqual(find_closest_elements([1000.0, 1001.0, 1000.5]), (1000.0, 1000.5))
        self.assertEqual(find_closest_elements([999999.0, 999999.5, 1000000.0]), (999999.5, 1000000.0))
    
    def test_mixed_positive_negative(self):
        """Test cases with mixed positive and negative numbers"""
        self.assertEqual(find_closest_elements([-1.0, 0.0, 1.0]), (-1.0, 0.0))
        self.assertEqual(find_closest_elements([-2.0, -1.5, 0.5, 1.0]), (-1.5, 0.5))
    
    def test_unordered_input(self):
        """Test that unordered input still works correctly"""
        self.assertEqual(find_closest_elements([5.0, 1.0, 3.0, 2.0]), (2.0, 3.0))
        self.assertEqual(find_closest_elements([10.0, 1.0, 5.0, 2.0, 3.0]), (2.0, 3.0))
    
    def test_ties_resolution(self):
        """Test behavior when there are ties (should return first found pair)"""
        # When multiple pairs have the same distance, the function returns the first one found
        # With the algorithm, this would be the pair found earliest in iteration order
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0])
        # Pairs with distance 1: (1,2), (2,3), (3,4) - should return (1.0, 2.0)
        self.assertEqual(result, (1.0, 2.0))

if __name__ == '__main__':
    unittest.main()