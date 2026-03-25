import unittest
from poly_llm.to_test.file_name_check import file_name_check

class TestFileNameCheck(unittest.TestCase):
    
    def test_valid_file_names(self):
        """Test valid file names that should return 'Yes'"""
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("test.exe"), "Yes")
        self.assertEqual(file_name_check("document.dll"), "Yes")
        self.assertEqual(file_name_check("a.txt"), "Yes")
        self.assertEqual(file_name_check("MyFile123.dll"), "Yes")  # 3 digits is allowed
        self.assertEqual(file_name_check("file1.exe"), "Yes")      # 1 digit is allowed
        self.assertEqual(file_name_check("A1b2c3.txt"), "Yes")     # mixed case with 3 digits
    
    def test_invalid_more_than_three_digits(self):
        """Test file names with more than three digits"""
        self.assertEqual(file_name_check("file1234.txt"), "No")    # 4 digits
        self.assertEqual(file_name_check("test12345.exe"), "No")   # 5 digits
        self.assertEqual(file_name_check("doc123456.dll"), "No")   # 6 digits
    
    def test_invalid_missing_dot(self):
        """Test file names without a dot"""
        self.assertEqual(file_name_check("exampletxt"), "No")
        self.assertEqual(file_name_check("testexe"), "No")
        self.assertEqual(file_name_check("file"), "No")
    
    def test_invalid_multiple_dots(self):
        """Test file names with multiple dots"""
        self.assertEqual(file_name_check("file.name.txt"), "No")
        self.assertEqual(file_name_check("test.exe.bak"), "No")
        self.assertEqual(file_name_check("a.b.c.dll"), "No")
    
    def test_invalid_empty_before_dot(self):
        """Test file names with empty prefix before dot"""
        self.assertEqual(file_name_check(".txt"), "No")
        self.assertEqual(file_name_check(".exe"), "No")
        self.assertEqual(file_name_check(".dll"), "No")
    
    def test_invalid_starts_with_non_letter(self):
        """Test file names that don't start with a letter"""
        self.assertEqual(file_name_check("1example.dll"), "No")
        self.assertEqual(file_name_check("123file.txt"), "No")
        self.assertEqual(file_name_check("_test.exe"), "No")
        self.assertEqual(file_name_check("-file.dll"), "No")
        self.assertEqual(file_name_check(".txt"), "No")  # already covered but relevant
    
    def test_invalid_extension(self):
        """Test file names with invalid extensions"""
        self.assertEqual(file_name_check("file.pdf"), "No")
        self.assertEqual(file_name_check("document.md"), "No")
        self.assertEqual(file_name_check("test.txt.bak"), "No")  # multiple dots
        self.assertEqual(file_name_check("file.txt2"), "No")     # extension not in list
    
    def test_valid_case_sensitivity(self):
        """Test that uppercase letters are valid for prefix"""
        self.assertEqual(file_name_check("FILE.txt"), "Yes")
        self.assertEqual(file_name_check("FILE123.EXE"), "Yes")
        self.assertEqual(file_name_check("MyFile.dll"), "Yes")
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(file_name_check("a123.dll"), "Yes")       # exactly 3 digits
        self.assertEqual(file_name_check("A.txt"), "Yes")          # single letter
        self.assertEqual(file_name_check("a1234.dll"), "No")       # 4 digits

if __name__ == '__main__':
    unittest.main()