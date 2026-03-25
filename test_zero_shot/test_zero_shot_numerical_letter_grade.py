import unittest
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):
    
    def test_basic_example_from_docstring(self):
        """Test the example from the docstring"""
        result = numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(result, expected)
    
    def test_exact_grade_boundaries(self):
        """Test exact grade boundary values"""
        # A+ boundary
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])
        
        # A- boundary
        self.assertEqual(numerical_letter_grade([3.7]), ['A-'])  # exactly 3.7
        
        # B+ boundary  
        self.assertEqual(numerical_letter_grade([3.3]), ['B+'])  # exactly 3.3
        
        # B- boundary
        self.assertEqual(numerical_letter_grade([3.0]), ['B-'])  # exactly 3.0
        
        # C+ boundary
        self.assertEqual(numerical_letter_grade([2.7]), ['C+'])  # exactly 2.7
        
        # C- boundary
        self.assertEqual(numerical_letter_grade([2.3]), ['C-'])  # exactly 2.3
        
        # D+ boundary
        self.assertEqual(numerical_letter_grade([2.0]), ['D+'])  # exactly 2.0
        
        # D- boundary
        self.assertEqual(numerical_letter_grade([1.7]), ['D-'])  # exactly 1.7
        self.assertEqual(numerical_letter_grade([1.3]), ['D-'])  # exactly 1.3
        
        # E boundary
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
    
    def test_boundary_values_just_above_thresholds(self):
        """Test values just above each threshold"""
        self.assertEqual(numerical_letter_grade([3.71]), ['A-'])  # just above 3.7
        self.assertEqual(numerical_letter_grade([3.31]), ['B+'])  # just above 3.3
        self.assertEqual(numerical_letter_grade([3.01]), ['B-'])  # just above 3.0
        self.assertEqual(numerical_letter_grade([2.71]), ['C+'])  # just above 2.7
        self.assertEqual(numerical_letter_grade([2.31]), ['C-'])  # just above 2.3
        self.assertEqual(numerical_letter_grade([2.01]), ['D+'])  # just above 2.0
        self.assertEqual(numerical_letter_grade([1.71]), ['D-'])  # just above 1.7
        self.assertEqual(numerical_letter_grade([1.31]), ['D-'])  # just above 1.3
        self.assertEqual(numerical_letter_grade([0.71]), ['D-'])  # just above 0.7
    
    def test_boundary_values_just_below_thresholds(self):
        """Test values just below each threshold"""
        self.assertEqual(numerical_letter_grade([3.69]), ['B+'])  # just below 3.7
        self.assertEqual(numerical_letter_grade([3.29]), ['B-'])  # just below 3.3
        self.assertEqual(numerical_letter_grade([2.99]), ['C+'])  # just below 3.0
        self.assertEqual(numerical_letter_grade([2.69]), ['C-'])  # just below 2.7
        self.assertEqual(numerical_letter_grade([2.29]), ['D+'])  # just below 2.3
        self.assertEqual(numerical_letter_grade([1.99]), ['D-'])  # just below 2.0
        self.assertEqual(numerical_letter_grade([1.69]), ['C-'])  # just below 1.7
        self.assertEqual(numerical_letter_grade([1.29]), ['D+'])  # just below 1.3
        self.assertEqual(numerical_letter_grade([0.69]), ['D-'])  # just below 0.7
    
    def test_edge_cases(self):
        """Test edge cases including zero and very low values"""
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
        self.assertEqual(numerical_letter_grade([-1.0]), ['E'])  # negative GPA
        self.assertEqual(numerical_letter_grade([0.01]), ['D-'])
        
        # Very high GPA (above 4.0)
        self.assertEqual(numerical_letter_grade([4.5]), ['A+'])
    
    def test_all_grades_in_one_call(self):
        """Test all grade categories in a single call"""
        gpa_list = [4.0, 3.8, 3.5, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.5, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(gpa_list), expected)
    
    def test_empty_list(self):
        """Test with empty list"""
        self.assertEqual(numerical_letter_grade([]), [])
    
    def test_repeated_values(self):
        """Test with repeated GPA values"""
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 4.0]), ['A+', 'A+', 'A+'])
        self.assertEqual(numerical_letter_grade([2.0, 2.0, 1.5]), ['D+', 'D+', 'C-'])
    
    def test_mixed_precision(self):
        """Test with various decimal precision"""
        self.assertEqual(numerical_letter_grade([3.75, 3.33, 2.99]), ['A-', 'B+', 'B-'])
        self.assertEqual(numerical_letter_grade([1.001, 0.999]), ['D+', 'D-'])

if __name__ == '__main__':
    unittest.main()