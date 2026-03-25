def test_numerical_letter_grade(numerical_letter_grade):
    # Test with a list of grades where the letter grades are A+
    assert numerical_letter_grade([4.0, 4.0, 4.0]) == ['A+', 'A+', 'A+']

    # Test with a list of grades where the letter grades are A
    assert numerical_letter_grade([3.8, 3.8, 3.8]) == ['A', 'A', 'A']

    # Test with a list of grades where the letter grades are A-
    assert numerical_letter_grade([3.4, 3.4, 3.4]) == ['A-', 'A-', 'A-']

    # Test with a list of grades where the letter grades are B+
    assert numerical_letter_grade([3.1, 3.1, 3.1]) == ['B+', 'B+', 'B+']

    # Test with a list of grades where the letter grades are B
    assert numerical_letter_grade([2.8, 2.8, 2.8]) == ['B', 'B', 'B']

    # Test with a list of grades where the letter grades are B-
    assert numerical_letter_grade([2.4, 2.4, 2.4]) == ['B-', 'B-', 'B-']

    # Test with a list of grades where the letter grades are C+
    assert numerical_letter_grade([2.1, 2.1, 2.1]) == ['C+', 'C+', 'C+']

    # Test with a list of grades where the letter grades are C
    assert numerical_letter_grade([1.8, 1.8, 1.8]) == ['C', 'C', 'C']

    # Test with a list of grades where the letter grades are C-
    assert numerical_letter_grade([1.4, 1.4, 1.4]) == ['C-', 'C-', 'C-']

    # Test with a list of grades where the letter grades are D+
    assert numerical_letter_grade([1.1, 1.1, 1.1]) == ['D+', 'D+', 'D+']

    # Test with a list of grades where the letter grades are D
    assert numerical_letter_grade([0.8, 0.8, 0.8]) == ['D', 'D', 'D']

    # Test with a list of grades where the letter grades are D-
    assert numerical_letter_grade([0.5, 0.5, 0.5]) == ['D-', 'D-', 'D-']

    # Test with a list of grades where the letter grades are E
    assert numerical_letter_grade([0.0, 0.0, 0.0]) == ['E', 'E', 'E']

    # Test with a list of grades where the letter grades are A+
    assert numerical_letter_grade([4.0, 3.9, 4.0]) == ['A+', 'A+', 'A+']

    # Test with a list of grades where the letter grades are A
    assert numerical_letter_grade([3.8, 3.7, 3.8]) == ['A', 'A', 'A']

    # Test with a list of grades where the letter grades are A-
    assert numerical_letter_grade([3.4, 3.3, 3.4]) == ['A-', 'A-', 'A-']

    # Test with a list of grades where the letter grades are B+
    assert numerical_letter_grade([3.1, 3.0, 3.1]) == ['B+', 'B+', 'B+']

    # Test with a list of grades where the letter grades are B
    assert numerical_letter_grade([2.8, 2.7, 2.8]) == ['B', 'B', 'B']

    # Test with a list of grades where the letter grades are B-
    assert numerical_letter_grade([2.4, 2.3, 2.4]) == ['B-', 'B-', 'B-']

    # Test with a list of grades where the letter grades are C+
    assert numerical_letter_grade([2.1, 2.0, 2.1]) == ['C+', 'C+', 'C+']

    # Test with a list of grades where the letter grades are C
    assert numerical_letter_grade([1.8, 1.7, 1.8]) == ['C', 'C', 'C']

    # Test with a list of grades where the letter grades are C-
    assert numerical_letter_grade([1.4, 1.3, 1.4]) == ['C-', 'C-', 'C-']

    # Test with a list of grades where the letter grades are D+
    assert numerical_letter_grade([1.1, 1.0, 1.1]) == ['D+', 'D+', 'D+']

    # Test with a list of grades where the letter grades are D
    assert numerical_letter_grade([0.8, 0.7, 0.8]) == ['D', 'D', 'D']

    # Test with a list of grades where the letter grades are D-
    assert numerical_letter_grade([0.5, 0.0, 0.5]) == ['D-', 'E', 'D-']

    # Test with a list of grades where the letter grades are E
    assert numerical_letter_grade([0.0, 0.0, 0.0]) == ['E', 'E', 'E']

    # Test with a list of grades where the letter grades are A+
    assert numerical_letter_grade([4.0, 4.0, 4.0]) == ['A+', 'A+', 'A+']

    # Test with a list of grades where the letter grades are A
    assert numerical_letter_grade([3.8, 3.8, 3.8]) == ['A', 'A', 'A']

    # Test with a list of grades where the letter grades are A-
    assert numerical_letter_grade([3.4, 3.4, 3.4]) == ['A-', 'A-', 'A-']

    # Test with a list of grades where the letter grades are B+
    assert numerical_letter_grade([3.1, 3.1, 3.1]) == ['B+', 'B+', 'B+']

    # Test with a list of grades where the letter grades are B
    assert numerical_letter_grade([2.8, 2.8, 2.8]) == ['B', 'B', 'B']

    # Test with a list of grades where the letter grades are B-
    assert numerical_letter_grade([2.4, 2.4, 2.4]) == ['B-', 'B-', 'B-']

    # Test with a list of grades where the letter grades are C+
    assert numerical_letter_grade([2.1, 2.1, 2.1]) == ['C+', 'C+', 'C+']

    # Test with a list of grades where the letter grades are C
    assert numerical_letter_grade([1.8, 1.8, 1.8]) == ['C', 'C', 'C']

    # Test with a list of grades where the letter grades are C-
    assert numerical_letter_grade([1.4, 1.4, 1.4]) == ['C-', 'C-', 'C-']

    # Test with a list of grades where the letter grades are D+
    assert numerical_letter_grade([1.1, 1.1, 1.1]) == ['D+', 'D+', 'D+']

    # Test with a list of grades where the letter grades are D
    assert numerical_letter_grade([0.8, 0.8, 0.8]) == ['D', 'D', 'D']

    # Test with a list of grades where the letter grades are D-
    assert numerical_letter_grade([0.5, 0.5, 0.5]) == ['D-', 'D-', 'D-']

    # Test with a list of grades where the letter grades are E
    assert numerical_letter_grade([0.0, 0.0, 0.0]) == ['E', 'E', 'E']

    # Test with a list of grades where the letter grades are A+
    assert numerical_letter_grade([4.0, 3.9, 4.0]) == ['A+', 'A+', 'A+']

    # Test with a list of grades where the letter grades are A
    assert numerical_letter_grade([3.8, 3.7, 3.8]) == ['A', 'A', 'A']

    # Test with a list of grades where the letter grades are A-
    assert numerical_letter_grade([3.4, 3.3, 3.4]) == ['A-', 'A-', 'A-']

    # Test with a list of grades where the letter grades are B+
    assert numerical_letter_grade([3.1, 3.0, 3.1]) == ['B+', 'B+', 'B+']