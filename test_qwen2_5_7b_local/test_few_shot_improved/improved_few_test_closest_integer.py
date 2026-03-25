def test_closest_integer(closest_integer):
    # Test with a positive integer
    assert closest_integer("10") == 10

    # Test with a positive number with a decimal point and no trailing zeros
    assert closest_integer("14.5") == 15

    # Test with a negative integer
    assert closest_integer("-10") == -10

    # Test with a negative number with a decimal point and no trailing zeros
    assert closest_integer("-14.5") == -15

    # Test with a positive number with a decimal point and trailing zeros
    assert closest_integer("14.500") == 15

    # Test with a negative number with a decimal point and trailing zeros
    assert closest_integer("-14.500") == -15

    # Test with a positive number with a decimal point and trailing zeros after the decimal
    assert closest_integer("14.50000") == 15

    # Test with a negative number with a decimal point and trailing zeros after the decimal
    assert closest_integer("-14.50000") == -15

    # Test with a positive number with a decimal point and trailing zeros before the decimal
    assert closest_integer("1000.000") == 1000

    # Test with a negative number with a decimal point and trailing zeros before the decimal
    assert closest_integer("-1000.000") == -1000

    # Test with a positive number with a decimal point and trailing zeros in the middle
    assert closest_integer("100.500") == 101

    # Test with a negative number with a decimal point and trailing zeros in the middle
    assert closest_integer("-100.500") == -101

    # Test with a positive number with a decimal point and trailing zeros in the middle and after the decimal
    assert closest_integer("100.50000") == 101

    # Test with a negative number with a decimal point and trailing zeros in the middle and after the decimal
    assert closest_integer("-100.50000") == -101

    # Test with a positive number with a decimal point and trailing zeros in the middle and before the decimal
    assert closest_integer("1000.500") == 1001

    # Test with a negative number with a decimal point and trailing zeros in the middle and before the decimal
    assert closest_integer("-1000.500") == -1001

    # Test with a positive number with a decimal point and trailing zeros in the middle and before and after the decimal
    assert closest_integer("1000.50000") == 1001

    # Test with a negative number with a decimal point and trailing zeros in the middle and before and after the decimal
    assert closest_integer("-1000.50000") == -1001

    # Test with a positive number with a decimal point and trailing zeros in the middle and before and after the decimal and with a large number
    assert closest_integer("1000000.50000") == 1000001

    # Test with a negative number with a decimal point and trailing zeros in the middle and before and after the decimal and with a large number
    assert closest_integer("-1000000.50000") == -1000001
