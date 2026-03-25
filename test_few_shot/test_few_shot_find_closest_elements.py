import unittest
from typing import List, Tuple
from poly_llm.to_test.find_closest_elements import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    """Unit tests for find_closest_elements function."""

    def test_basic_case(self):
        """Test basic functionality with distinct numbers."""
        self.assertEqual(
            find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]),
            (2.0, 2.2)
        )

    def test_duplicate_numbers(self):
        """Test case with duplicate numbers in the list."""
        self.assertEqual(
            find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]),
            (2.0, 2.0)
        )

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(
            find_closest_elements([-1.0, -2.0, -3.0, -2.2]),
            (-2.2, -2.0)
        )

    def test_mixed_positive_negative(self):
        """Test with both positive and negative numbers."""
        self.assertEqual(
            find_closest_elements([-1.0, 0.0, 1.0, 0.5]),
            (0.0, 0.5)
        )

    def test_precision_case(self):
        """Test with very close floating-point numbers."""
        self.assertEqual(
            find_closest_elements([1.0, 1.0001, 2.0, 3.0]),
            (1.0, 1.0001)
        )

    def test_two_elements(self):
        """Test minimal case with exactly two elements."""
        self.assertEqual(
            find_closest_elements([5.0, 10.0]),
            (5.0, 10.0)
        )

    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(
            find_closest_elements([1000000.0, 1000000.5, 2000000.0]),
            (1000000.0, 1000000.5)
        )

    def test_small_numbers(self):
        """Test with very small numbers."""
        self.assertEqual(
            find_closest_elements([0.001, 0.002, 0.003]),
            (0.001, 0.002)
        )

    def test_zero_included(self):
        """Test list containing zero."""
        self.assertEqual(
            find_closest_elements([0.0, 1.0, -1.0, 0.5]),
            (0.0, 0.5)
        )

    def test_same_distance_pairs(self):
        """Test when multiple pairs have the same minimum distance."""
        self.assertEqual(
            find_closest_elements([1.0, 2.0, 3.0, 4.0]),
            (1.0, 2.0)  # Should return first pair encountered
        )


if __name__ == '__main__':
    unittest.main()