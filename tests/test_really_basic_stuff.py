import re


def test_always_pass():
    assert True


def test_values_are_equal():
    assert 1 == 1
    assert "one" == "one"

    some_value = [1, 2, "3"]
    assert [1, 2, "3"] == some_value


def test_comments():
    """adding a comment or docstring makes it appear with pyspec"""
    pass


# Example exercise: given the has_only_digits function below, test that it behaves as expected for inputs with only digits, and inputs that have other characters.
def has_only_digits(input_string: str) -> bool:
    re_match = re.fullmatch(r"[0-9]+", input_string)
    return bool(re_match)


# Example tests that meaningfully test the function
def test_only_digits_single():
    assert has_only_digits("0")


def test_only_digits_long():
    assert has_only_digits("003495839445")


def test_only_digits_space():
    assert has_only_digits("0 ") is False


def test_only_digits_decimal():
    assert has_only_digits("1.1") is False


def test_only_digits_empty_string():
    assert has_only_digits("") is False
