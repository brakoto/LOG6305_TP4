import unittest
from poly_llm.to_test.closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):
    """Unit tests for closest_integer function."""

    def test_integer_strings(self):
        """Test with integer strings."""
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("-5"), -5)

    def test_rounding_away_from_zero(self):
        """Test rounding away from zero for .5 cases."""
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("2.5"), 3)
        self.assertEqual(closest_integer("-2.5"), -3)

    def test_normal_rounding(self):
        """Test normal rounding for non-.5 cases."""
        self.assertEqual(closest_integer("14.4"), 14)
        self.assertEqual(closest_integer("14.6"), 15)
        self.assertEqual(closest_integer("-14.4"), -14)
        self.assertEqual(closest_integer("-14.6"), -15)

    def test_trailing_zeros(self):
        """Test handling of trailing zeros after decimal."""
        self.assertEqual(closest_integer("10.0"), 10)
        self.assertEqual(closest_integer("10.00"), 10)
        self.assertEqual(closest_integer("10.50"), 11)
        self.assertEqual(closest_integer("10.500"), 11)

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("0.4"), 0)
        self.assertEqual(closest_integer("-0.4"), 0)

    def test_decimal_rounding(self):
        """Test various decimal numbers."""
        self.assertEqual(closest_integer("3.2"), 3)
        self.assertEqual(closest_integer("3.7"), 4)
        self.assertEqual(closest_integer("-3.2"), -3)
        self.assertEqual(closest_integer("-3.7"), -4)


if __name__ == '__main__':
    unittest.main()