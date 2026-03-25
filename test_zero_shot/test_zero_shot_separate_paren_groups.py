import unittest
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):
    
    def test_basic_example_from_docstring(self):
        """Test the example from the docstring"""
        result = separate_paren_groups('( ) (( )) (( )( ))')
        expected = ['()', '(())', '(()())']
        self.assertEqual(result, expected)
    
    def test_simple_balanced_groups(self):
        """Test simple balanced parentheses groups"""
        self.assertEqual(separate_paren_groups('()'), ['()'])
        self.assertEqual(separate_paren_groups('()()'), ['()', '()'])
        self.assertEqual(separate_paren_groups('(())()'), ['(())', '()'])
        self.assertEqual(separate_paren_groups('()(())'), ['()', '(())'])
    
    def test_nested_groups(self):
        """Test nested parentheses within groups"""
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])
        self.assertEqual(separate_paren_groups('((()))()'), ['((()))', '()'])
        self.assertEqual(separate_paren_groups('()((()))'), ['()', '((()))'])
    
    def test_spaces_handling(self):
        """Test that spaces are properly ignored"""
        self.assertEqual(separate_paren_groups('() ()'), ['()', '()'])
        self.assertEqual(separate_paren_groups('( ) ( )'), ['()', '()'])
        self.assertEqual(separate_paren_groups('(  ) (  )'), ['()', '()'])
        self.assertEqual(separate_paren_groups('  ( )  (( ))  '), ['()', '(())'])
    
    def test_complex_balanced_groups(self):
        """Test more complex balanced parentheses"""
        self.assertEqual(separate_paren_groups('(()(()))'), ['(()(()))'])
        self.assertEqual(separate_paren_groups('(()(()))()'), ['(()(()))', '()'])
        self.assertEqual(separate_paren_groups('()(()(()))'), ['()', '(()(()))'])
        self.assertEqual(separate_paren_groups('(()())(())'), ['(()())', '(())'])
    
    def test_multiple_simple_groups(self):
        """Test multiple simple groups in sequence"""
        self.assertEqual(separate_paren_groups('()()()'), ['()', '()', '()'])
        self.assertEqual(separate_paren_groups('()()()()'), ['()', '()', '()', '()'])
    
    def test_mixed_complexity(self):
        """Test mix of simple and complex groups"""
        self.assertEqual(separate_paren_groups('()((()))(()())'), ['()', '((()))', '(()())'])
        self.assertEqual(separate_paren_groups('(()())()((()))'), ['(()())', '()', '((()))'])
    
    def test_deeply_nested(self):
        """Test deeply nested parentheses"""
        self.assertEqual(separate_paren_groups('((((()))))'), ['((((()))))'])
        self.assertEqual(separate_paren_groups('((((()))))()'), ['((((()))))', '()'])
    
    def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(separate_paren_groups(''), [])
    
    def test_only_spaces(self):
        """Test string with only spaces"""
        self.assertEqual(separate_paren_groups(' '), [])
        self.assertEqual(separate_paren_groups('    '), [])
    
    def test_complex_nested_example(self):
        """Test complex nested example"""
        self.assertEqual(separate_paren_groups('((()()))(()())'), ['((()()))', '(()())'])
        self.assertEqual(separate_paren_groups('(()((())))()'), ['(()((())))', '()'])
    
    def test_whitespace_variations(self):
        """Test various whitespace patterns"""
        self.assertEqual(separate_paren_groups('\n()\n()\n'), ['()', '()'])
        self.assertEqual(separate_paren_groups('\t( )\t( )\t'), ['()', '()'])
        self.assertEqual(separate_paren_groups('  (  )  (  )  '), ['()', '()'])

if __name__ == '__main__':
    unittest.main()