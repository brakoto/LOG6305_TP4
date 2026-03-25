def test_file_name_check(file_name_check):
    # Test with a valid file name
    assert file_name_check("example.txt") == 'Yes'

    # Test with a valid file name with digits in the first part
    assert file_name_check("1example.dll") == 'No'

    # Test with a valid file name with a single character in the first part
    assert file_name_check("a.txt") == 'Yes'

    # Test with a valid file name with a three-digit number in the first part
    assert file_name_check("abc123.txt") == 'Yes'

    # Test with a valid file name with a four-digit number in the first part
    assert file_name_check("abc1234.txt") == 'No'

    # Test with a valid file name with a single character in the first part and a three-digit number in the second part
    assert file_name_check("a123.txt") == 'Yes'

    # Test with a valid file name with a single character in the first part and a four-digit number in the second part
    assert file_name_check("a1234.txt") == 'No'

    # Test with a valid file name with a two-character first part and a three-digit number in the second part
    assert file_name_check("ab123.txt") == 'Yes'

    # Test with a valid file name with a two-character first part and a four-digit number in the second part
    assert file_name_check("ab1234.txt") == 'No'

    # Test with a valid file name with a three-character first part and a three-digit number in the second part
    assert file_name_check("abc123.txt") == 'Yes'

    # Test with a valid file name with a three-character first part and a four-digit number in the second part
    assert file_name_check("abc1234.txt") == 'No'

    # Test with a valid file name with a four-character first part and a three-digit number in the second part
    assert file_name_check("abcd123.txt") == 'Yes'

    # Test with a valid file name with a four-character first part and a four-digit number in the second part
    assert file_name_check("abcd1234.txt") == 'No'

    # Test with a valid file name with a five-character first part and a three-digit number in the second part
    assert file_name_check("abcde123.txt") == 'Yes'

    # Test with a valid file name with a five-character first part and a four-digit number in the second part
    assert file_name_check("abcde1234.txt") == 'No'

    # Test with a valid file name with a six-character first part and a three-digit number in the second part
    assert file_name_check("abcdef123.txt") == 'Yes'

    # Test with a valid file name with a six-character first part and a four-digit number in the second part
    assert file_name_check("abcdef1234.txt") == 'No'

    # Test with a valid file name with a seven-character first part and a three-digit number in the second part
    assert file_name_check("abcdefgh123.txt") == 'Yes'

    # Test with a valid file name with a seven-character first part and a four-digit number in the second part
    assert file_name_check("abcdefgh1234.txt") == 'No'

    # Test with a valid file name with a eight-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghi123.txt") == 'Yes'

    # Test with a valid file name with a eight-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghi1234.txt") == 'No'

    # Test with a valid file name with a nine-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghij123.txt") == 'Yes'

    # Test with a valid file name with a nine-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghij1234.txt") == 'No'

    # Test with a valid file name with a ten-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a ten-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a eleven-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijkl123.txt") == 'Yes'

    # Test with a valid file name with a eleven-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijkl1234.txt") == 'No'

    # Test with a valid file name with a twelve-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a twelve-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a thirteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a thirteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a fourteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a fourteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a fifteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a fifteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a sixteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a sixteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a seventeen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a seventeen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a eighteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a eighteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a nineteen-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a nineteen-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a twenty-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a twenty-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a twenty-one-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'

    # Test with a valid file name with a twenty-one-character first part and a four-digit number in the second part
    assert file_name_check("abcdefghijk1234.txt") == 'No'

    # Test with a valid file name with a twenty-two-character first part and a three-digit number in the second part
    assert file_name_check("abcdefghijk123.txt") == 'Yes'