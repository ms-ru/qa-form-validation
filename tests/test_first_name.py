import pytest
from validators import validate_first_name


@pytest.mark.parametrize("v", ["", " ", None])
def test_required(v):
    """
    Test that first name is required.
    - Empty string, whitespace, or None should trigger a 'required' error message.
    """
    assert "required" in " ".join(validate_first_name(v)).lower()


@pytest.mark.parametrize("v", ["A", "Z"*41])
def test_length(v):
    """
    Test first name length validation.
    - Too short (1 character) or too long (41 characters) should trigger '2-40' error.
    """
    msg = " ".join(validate_first_name(v))
    assert "2-40" in msg


@pytest.mark.parametrize("v", ["J0hn", "Ann@", "Max_"])
def test_invalid_chars(v):
    """
    Test invalid characters in first name.
    - Numbers, special characters like '@' or '_' should trigger 'letters' error.
    """
    msg = " ".join(validate_first_name(v))
    assert "letters" in msg  # error message must mention "letters"


def test_ok():
    """
    Test valid first names.
    - Should pass validation and return an empty error list.
    """
    assert validate_first_name("Max") == []
    assert validate_first_name("Jean-Luc") == []
    assert validate_first_name("O'Connor") == []
