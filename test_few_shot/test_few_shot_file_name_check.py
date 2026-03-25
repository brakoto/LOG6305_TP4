import unittest
from poly_llm.to_test.file_name_check import file_name_check

class TestFileNameCheck(unittest.TestCase):
    def test_valid_filenames(self):
        # Valid filenames with valid extensions
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("file.exe"), "Yes")
        self.assertEqual(file_name_check("document.dll"), "Yes")
        
        # Valid filenames with uppercase letters
        self.assertEqual(file_name_check("Example.TXT"), "Yes")
        self.assertEqual(file_name_check("FILE.exe"), "Yes")
        self.assertEqual(file_name_check("Document.DLL"), "Yes")
        
        # Valid filenames with up to 3 digits
        self.assertEqual(file_name_check("a1b2c3.txt"), "Yes")
        self.assertEqual(file_name_check("test123.exe"), "Yes")
        self.assertEqual(file_name_check("file9.dll"), "Yes")
        
        # Valid filenames starting with letter and containing letters/numbers
        self.assertEqual(file_name_check("abc123.txt"), "Yes")
        self.assertEqual(file_name_check("file1name.exe"), "Yes")

    def test_invalid_filenames(self):
        # Filenames starting with digit
        self.assertEqual(file_name_check("1example.txt"), "No")
        self.assertEqual(file_name_check("9file.exe"), "No")
        
        # Filenames with more than 3 digits
        self.assertEqual(file_name_check("file1234.txt"), "No")
        self.assertEqual(file_name_check("test12345.exe"), "No")
        
        # Filenames without dot
        self.assertEqual(file_name_check("exampletxt"), "No")
        self.assertEqual(file_name_check("file"), "No")
        
        # Filenames with multiple dots
        self.assertEqual(file_name_check("file.txt.exe"), "No")
        self.assertEqual(file_name_check("a.b.c.txt"), "No")
        
        # Empty prefix before dot
        self.assertEqual(file_name_check(".txt"), "No")
        self.assertEqual(file_name_check(".exe"), "No")
        self.assertEqual(file_name_check(".dll"), "No")
        
        # Invalid extensions
        self.assertEqual(file_name_check("file.pdf"), "No")
        self.assertEqual(file_name_check("file.doc"), "No")
        self.assertEqual(file_name_check("file.txt.exe"), "No")
        
        # Empty filename
        self.assertEqual(file_name_check(""), "No")
        
        # Filenames with special characters
        self.assertEqual(file_name_check("file_name.txt"), "No")
        self.assertEqual(file_name_check("file-name.exe"), "No")
        self.assertEqual(file_name_check("file name.dll"), "No")

    def test_boundary_cases(self):
        # Exactly 3 digits (should be valid)
        self.assertEqual(file_name_check("a123.txt"), "Yes")
        self.assertEqual(file_name_check("abc999.exe"), "Yes")
        
        # 4 digits (should be invalid)
        self.assertEqual(file_name_check("a1234.txt"), "No")
        
        # Mixed case extensions
        self.assertEqual(file_name_check("file.Txt"), "No")  # case-sensitive
        self.assertEqual(file_name_check("file.EXE"), "No")  # case-sensitive
        self.assertEqual(file_name_check("file.DLL"), "No")  # case-sensitive

if __name__ == '__main__':
    unittest.main()