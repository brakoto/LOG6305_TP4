import unittest
from poly_llm.to_test.closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):
    
    def test_basic_rounding(self):
        """Test basic rounding functionality"""
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("10.3"), 10)
        self.assertEqual(closest_integer("10.7"), 11)
        self.assertEqual(closest_integer("-10.3"), -10)
        self.assertEqual(closest_integer("-10.7"), -11)
    
    def test_round_away_from_zero_positive(self):
        """Test rounding away from zero for positive .5 values"""
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("100.5"), 101)
    
    def test_round_away_from_zero_negative(self):
        """Test rounding away from zero for negative .5 values"""
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("-100.5"), -101)
    
    def test_trailing_zeros(self):
        """Test handling of trailing zeros after decimal point"""
        self.assertEqual(closest_integer("10.500"), 11)
        self.assertEqual(closest_integer("10.50"), 11)
        self.assertEqual(closest_integer("10.400"), 10)
        self.assertEqual(closest_integer("-10.500"), -11)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.0"), 0)
        self.assertEqual(closest_integer("0.4"), 0)
        self.assertEqual(closest_integer("0.6"), 1)
        self.assertEqual(closest_integer("-0.4"), 0)
        self.assertEqual(closest_integer("-0.6"), -1)
    
    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(closest_integer("999999.5"), 1000000)
        self.assertEqual(closest_integer("-999999.5"), -1000000)
        self.assertEqual(closest_integer("1234567.2"), 1234567)
        self.assertEqual(closest_integer("1234567.8"), 1234568)
    
    def test_very_small_decimals(self):
        """Test with very small decimal values"""
        self.assertEqual(closest_integer("0.01"), 0)
        self.assertEqual(closest_integer("0.99"), 1)
        self.assertEqual(closest_integer("-0.01"), 0)
        self.assertEqual(closest_integer("-0.99"), -1)

if __name__ == '__main__':
    unittest.main()