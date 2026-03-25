import unittest
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):
    
    def test_top_grade_4_0(self):
        """Test that 4.0 maps to A+"""
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])
    
    def test_above_3_7(self):
        """Test grades above 3.7 but less than 4.0 map to A"""
        self.assertEqual(numerical_letter_grade([3.8, 3.9]), ['A', 'A'])
    
    def test_boundary_3_7(self):
        """Test that exactly 3.7 maps to A- (not A)"""
        self.assertEqual(numerical_letter_grade([3.7]), ['A-'])
    
    def test_above_3_3(self):
        """Test grades above 3.3 but less than 3.7 map to A-"""
        self.assertEqual(numerical_letter_grade([3.4, 3.5, 3.6]), ['A-', 'A-', 'A-'])
    
    def test_boundary_3_3(self):
        """Test that exactly 3.3 maps to B+ (not A-)"""
        self.assertEqual(numerical_letter_grade([3.3]), ['B+'])
    
    def test_above_3_0(self):
        """Test grades above 3.0 but less than 3.3 map to B+"""
        self.assertEqual(numerical_letter_grade([3.1, 3.2]), ['B+', 'B+'])
    
    def test_boundary_3_0(self):
        """Test that exactly 3.0 maps to B (not B+)"""
        self.assertEqual(numerical_letter_grade([3.0]), ['B'])
    
    def test_above_2_7(self):
        """Test grades above 2.7 but less than 3.0 map to B"""
        self.assertEqual(numerical_letter_grade([2.8, 2.9]), ['B', 'B'])
    
    def test_boundary_2_7(self):
        """Test that exactly 2.7 maps to B- (not B)"""
        self.assertEqual(numerical_letter_grade([2.7]), ['B-'])
    
    def test_above_2_3(self):
        """Test grades above 2.3 but less than 2.7 map to B-"""
        self.assertEqual(numerical_letter_grade([2.4, 2.5, 2.6]), ['B-', 'B-', 'B-'])
    
    def test_boundary_2_3(self):
        """Test that exactly 2.3 maps to C+ (not B-)"""
        self.assertEqual(numerical_letter_grade([2.3]), ['C+'])
    
    def test_above_2_0(self):
        """Test grades above 2.0 but less than 2.3 map to C+"""
        self.assertEqual(numerical_letter_grade([2.1, 2.2]), ['C+', 'C+'])
    
    def test_boundary_2_0(self):
        """Test that exactly 2.0 maps to C (not C+)"""
        self.assertEqual(numerical_letter_grade([2.0]), ['C'])
    
    def test_above_1_7(self):
        """Test grades above 1.7 but less than 2.0 map to C"""
        self.assertEqual(numerical_letter_grade([1.8, 1.9]), ['C', 'C'])
    
    def test_boundary_1_7(self):
        """Test that exactly 1.7 maps to C- (not C)"""
        self.assertEqual(numerical_letter_grade([1.7]), ['C-'])
    
    def test_above_1_3(self):
        """Test grades above 1.3 but less than 1.7 map to C-"""
        self.assertEqual(numerical_letter_grade([1.4, 1.5, 1.6]), ['C-', 'C-', 'C-'])
    
    def test_boundary_1_3(self):
        """Test that exactly 1.3 maps to D+ (not C-)"""
        self.assertEqual(numerical_letter_grade([1.3]), ['D+'])
    
    def test_above_1_0(self):
        """Test grades above 1.0 but less than 1.3 map to D+"""
        self.assertEqual(numerical_letter_grade([1.1, 1.2]), ['D+', 'D+'])
    
    def test_boundary_1_0(self):
        """Test that exactly 1.0 maps to D (not D+)"""
        self.assertEqual(numerical_letter_grade([1.0]), ['D'])
    
    def test_above_0_7(self):
        """Test grades above 0.7 but less than 1.0 map to D"""
        self.assertEqual(numerical_letter_grade([0.8, 0.9]), ['D', 'D'])
    
    def test_boundary_0_7(self):
        """Test that exactly 0.7 maps to D- (not D)"""
        self.assertEqual(numerical_letter_grade([0.7]), ['D-'])
    
    def test_above_0_0(self):
        """Test grades above 0.0 but less than 0.7 map to D-"""
        self.assertEqual(numerical_letter_grade([0.1, 0.2, 0.3, 0.5, 0.6]), 
                        ['D-', 'D-', 'D-', 'D-', 'D-'])
    
    def test_boundary_0_0(self):
        """Test that exactly 0.0 maps to E (not D-)"""
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
    
    def test_below_zero(self):
        """Test grades below 0.0 map to E"""
        self.assertEqual(numerical_letter_grade([-0.5, -1.0, -2.0]), ['E', 'E', 'E'])
    
    def test_example_case(self):
        """Test the example case from the docstring"""
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), 
                        ['A+', 'B', 'C-', 'C', 'A-'])
    
    def test_empty_list(self):
        """Test that empty list returns empty list"""
        self.assertEqual(numerical_letter_grade([]), [])
    
    def test_multiple_same_grades(self):
        """Test multiple students with same GPA"""
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 4.0]), ['A+', 'A+', 'A+'])
    
    def test_all_boundary_values(self):
        """Test all boundary values"""
        self.assertEqual(numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 
                                               1.7, 1.3, 1.0, 0.7, 0.0]), 
                        ['A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'])
    
    def test_mixed_values(self):
        """Test mixed values across different ranges"""
        self.assertEqual(numerical_letter_grade([0.5, 1.5, 2.5, 3.5, 4.0]), 
                        ['D-', 'C-', 'B-', 'A-', 'A+'])

if __name__ == '__main__':
    unittest.main()