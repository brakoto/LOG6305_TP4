def test_find_closest_elements(find_closest_elements):
    # Test with a list of numbers where the closest pair is at the beginning
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

    # Test with a list of numbers where the closest pair is at the end
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)

    # Test with a list of numbers where the closest pair is in the middle
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (3.0, 4.0)

    # Test with a list of numbers where the closest pair is the first and last elements
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the first and second elements
    assert find_closest_elements([1.0, 1.1, 3.0, 4.0, 5.0]) == (1.0, 1.1)

    # Test with a list of numbers where the closest pair is the last and second last elements
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.9]) == (4.9, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.1]) == (1.0, 1.1)

    # Test with a list of numbers where the closest pair is the first and second elements (different values)
    assert find_closest_elements([1.0, 1.1, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.9]) == (4.9, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the first and second elements (same value)
    assert find_closest_elements([1.0, 1.0, 3.0, 4.0, 5.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 5.0]) == (5.0, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.1]) == (1.0, 1.1)

    # Test with a list of numbers where the closest pair is the first and second elements (different values)
    assert find_closest_elements([1.0, 1.1, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.9]) == (4.9, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the first and second elements (same value)
    assert find_closest_elements([1.0, 1.0, 3.0, 4.0, 5.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 5.0]) == (5.0, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.1]) == (1.0, 1.1)

    # Test with a list of numbers where the closest pair is the first and second elements (different values)
    assert find_closest_elements([1.0, 1.1, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.9]) == (4.9, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the first and second elements (same value)
    assert find_closest_elements([1.0, 1.0, 3.0, 4.0, 5.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (same value)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 5.0]) == (5.0, 5.0)

    # Test with a list of numbers where the closest pair is the first and last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.1]) == (1.0, 1.1)

    # Test with a list of numbers where the closest pair is the first and second elements (different values)
    assert find_closest_elements([1.0, 1.1, 3.0, 4.0, 5.0, 1.0]) == (1.0, 1.0)

    # Test with a list of numbers where the closest pair is the last and second last elements (different values)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 4.9]) == (4.9, 5.0)
