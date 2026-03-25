import unittest
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
        self.assertEqual(separate_paren_groups('(()()) ((())) () ((())()())'), [
            '(()())', '((()))', '()', '((())()())'
        ])
        self.assertEqual(separate_paren_groups('() (()) ((())) (((())))'), [
            '()', '(())', '((()))', '(((())))'
        ])

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_single_group(self):
        self.assertEqual(separate_paren_groups('(())'), ['(())'])
        self.assertEqual(separate_paren_groups('()'), ['()'])

    def test_ignore_spaces(self):
        self.assertEqual(separate_paren_groups('  (  )   (())  '), ['()', '(())'])

    def test_deeply_nested(self):
        self.assertEqual(separate_paren_groups('(((())))'), ['(((())))'])

    def test_multiple_simple_groups(self):
        self.assertEqual(separate_paren_groups('() () ()'), ['()', '()', '()'])

    def test_complex_mixed_groups(self):
        self.assertEqual(separate_paren_groups('(()(())) ((())) (())'), ['(()(()))', '((()))', '(())'])


if __name__ == '__main__':
    unittest.main()