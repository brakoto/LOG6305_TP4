def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.doc") == 'No'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.1234.txt") == 'No'
    assert file_name_check("example.1234.exe") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("example.doc") == 'No'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.1234.txt") == 'No'
    assert file_name_check("example.1234.exe") == 'No'
    assert file_name_check("") == 'No'  # Empty string
    assert file_name_check("example.") == 'No'  # Only one part after split
    assert file_name_check(".example") == 'No'  # No name before dot
    assert file_name_check("example..") == 'No'  # Multiple dots in name part
    assert file_name_check("example..exe") == 'No'  # Multiple dots in extension part
    assert file_name_check("example-123.exe") == 'Yes'  # Dashes allowed in name part
    assert file_name_check("example_123.exe") == 'Yes'  # Underscores allowed in name part
    assert file_name_check("example123.exe") == 'Yes'
