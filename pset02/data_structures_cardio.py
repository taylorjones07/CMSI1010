
def third_element(t):
    # check if its a tuple
    if not isinstance(t, tuple):
        raise TypeError

    # check if it has 3 things
    if len(t) < 3:
        raise IndexError

    # get the third thing
    return t[2]


def reverse_pair(t):
    # check if its a tuple
    if not isinstance(t, tuple):
        raise TypeError

    # needs to have 2 things
    if len(t) != 2:
        raise ValueError

    # switch the two things
    return (t[1], t[0])


def middle_element_of_list(a):
    # check if its a list
    if not isinstance(a, list):
        raise TypeError

    # check if its empty
    if len(a) == 0:
        raise IndexError

    # find the middle
    middle = (len(a) - 1) // 2
    return a[middle]


def unique_elements(a):
    # check if its a list
    if not isinstance(a, list):
        raise TypeError

    # get rid of repeats
    return set(a)


def contains_duplicates(a):
    # check if its a list
    if not isinstance(a, list):
        raise TypeError

    # see if anything repeats
    return len(a) != len(set(a))


def is_superset(a, b):
    # check if both are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError

    # see if a has everything in b
    return a.issuperset(b)


def is_subset(a, b):
    # check if both are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError

    # see if a is inside b
    return a.issubset(b)


def is_disjoint(a, b):
    # check if both are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError

    # see if they have nothing in common
    return a.isdisjoint(b)


def most_frequent_value_or_values(d):
    # check if its a dictionary
    if not isinstance(d, dict):
        raise TypeError

    # if its empty return an empty set
    if len(d) == 0:
        return set()

    # count how many times each value shows up
    counts = {}

    for value in d.values():
        counts[value] = counts.get(value, 0) + 1

    # find the biggest count
    highest = max(counts.values())
    result = set()

    # add the values with the biggest count
    for value in counts:
        if counts[value] == highest:
            result.add(value)

    return result


def key_is_in_both_dictionaries(d1, d2, key):
    # check if both are dictionaries
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError

    # see if the key is in both
    return key in d1 and key in d2


def word_frequencies(s):
    # check if its a string
    if not isinstance(s, str):
        raise TypeError

    # make a dictionary for the word counts
    frequencies = {}

    # go through each word
    for word in s.split():
        if word in frequencies:
            # add 1 if we already have the word
            frequencies[word] += 1
        else:
            # start at 1 if its a new word
            frequencies[word] = 1

    return frequencies


def _assert_raises(exception_type, func, *args):
    try:
        func(*args)
        assert False, "Expected exception not raised"
    except exception_type:
        assert True


def test_third_element():
    assert third_element((1, 2, 3, 4)) == 3
    _assert_raises(IndexError, third_element, (1, 2))
    _assert_raises(IndexError, third_element, (1,))
    _assert_raises(TypeError, third_element, "not a tuple")
    _assert_raises(TypeError, third_element, [1, 2, 3])


def test_reverse_pair():
    assert reverse_pair((1, 2)) == (2, 1)
    _assert_raises(ValueError, reverse_pair, (1, 2, 3))
    _assert_raises(ValueError, reverse_pair, (1,))
    _assert_raises(TypeError, reverse_pair, [1, 2])
    _assert_raises(TypeError, reverse_pair, "not a tuple")


def test_middle_element_of_list():
    assert middle_element_of_list([1, 2, 3]) == 2
    assert middle_element_of_list([1, 2]) == 1
    assert middle_element_of_list([10, 20, 30, 40]) == 20
    assert middle_element_of_list([5] * 500) == 5
    _assert_raises(IndexError, middle_element_of_list, [])
    _assert_raises(TypeError, middle_element_of_list, (1, 2))
    _assert_raises(TypeError, middle_element_of_list, "not a list")


def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == {1, 2, 3}
    assert unique_elements([1, 1, 1]) == {1}
    assert unique_elements([]) == set()
    assert unique_elements([1, 2, 3, 4, 5]) == {1, 2, 3, 4, 5}
    assert unique_elements(
        [False, 3, "dog", False, "dog"]) == {False, 3, "dog"}
    _assert_raises(TypeError, unique_elements, "not a list")
    _assert_raises(TypeError, unique_elements, {1, 2, 3})


def test_contains_duplicates():
    assert contains_duplicates([1, 2, 2]) is True
    assert contains_duplicates([1, 2, 3]) is False
    _assert_raises(TypeError, contains_duplicates, "not a list")
    _assert_raises(TypeError, contains_duplicates, {1, 2, 3})


def test_is_superset():
    assert is_superset({1, 2}, {1}) is True
    assert is_superset({1}, {1, 2}) is False
    _assert_raises(TypeError, is_superset, {1}, "not a set")


def test_is_subset():
    assert is_subset({1}, {1, 2}) is True
    assert is_subset({1, 2}, {1}) is False
    _assert_raises(TypeError, is_subset, "not a set", {1})


def test_is_disjoint():
    assert is_disjoint({1}, {2}) is True
    assert is_disjoint({1}, {1}) is False
    _assert_raises(TypeError, is_disjoint, {1}, "not a set")
    _assert_raises(TypeError, is_disjoint, "not a set", {1})


def test_most_frequent_value_or_values():
    assert most_frequent_value_or_values({'a': 1, 'b': 2, 'c': 1}) == {1}
    assert most_frequent_value_or_values({'a': 1, 'b': 2, 'c': 2}) == {2}
    assert most_frequent_value_or_values(
        {'a': 1, 'b': 1, 'c': 2, 'd': 2}) == {1, 2}
    assert most_frequent_value_or_values({}) == set()
    _assert_raises(TypeError, most_frequent_value_or_values, "not a dict")


def test_key_is_in_both_dictionaries():
    assert key_is_in_both_dictionaries(
        {'a': 1, 'b': 2}, {'b': 3, 'c': 4}, 'b') is True
    assert key_is_in_both_dictionaries(
        {'a': 1}, {'b': 2}, 'a') is False
    _assert_raises(
        TypeError,
        key_is_in_both_dictionaries, "not a dict", {'b': 2}, 'b')
    _assert_raises(
        TypeError,
        key_is_in_both_dictionaries, {'a': 1}, "not a dict", 'a')


def test_word_frequencies():
    assert word_frequencies("hello world hello") == {'hello': 2, 'world': 1}
    assert word_frequencies("a b a c b a") == {'a': 3, 'b': 2, 'c': 1}
    assert word_frequencies("test test test") == {'test': 3}
    assert word_frequencies("") == {}
    _assert_raises(TypeError, word_frequencies, 12345)
    _assert_raises(TypeError, word_frequencies, ["not", "a", "string"])
    _assert_raises(TypeError, word_frequencies, {"not": "a string"})


test_third_element()
test_reverse_pair()
test_middle_element_of_list()
test_unique_elements()
test_contains_duplicates()
test_is_superset()
test_is_subset()
test_is_disjoint()
test_most_frequent_value_or_values()
test_key_is_in_both_dictionaries()
test_word_frequencies()

print("All tests passed!")
