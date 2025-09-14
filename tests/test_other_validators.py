from validators import (
    validate_last_name, validate_username, validate_email,
    validate_password, validate_confirm_password
)


def test_last_name_ok_and_bad():
    """
    Test last name validation.
    - A valid last name (with apostrophe) should pass.
    - Too short (1 character) should fail.
    """
    assert validate_last_name("O'Neil") == []   # valid
    assert validate_last_name("A")              # invalid (too short)


def test_username_rules():
    """
    Test username validation.
    - A valid email-like string should pass.
    - Invalid cases: too short or containing spaces should fail.
    """
    assert validate_username("ok_name_123") == []  # valid email-like username
    assert validate_username("ab")                 # invalid (too short / not email format)
    assert validate_username("bad name")           # invalid (space not allowed)


def test_email_rules():
    """
    Test email validation.
    - A correct email should pass.
    - Missing '@' symbol should fail.
    """
    assert validate_email("me@example.com") == []  # valid
    assert validate_email("no-at.com")             # invalid


def test_password_and_confirm():
    """
    Test password and confirmation rules.
    - Valid length (≥12 characters) should pass.
    - Too short should fail.
    - Confirmation must match original password.
    """
    assert validate_password("abcdefghijkl") == []     # valid (12 chars)
    assert validate_password("short")                  # invalid (too short)

    assert validate_confirm_password("aaa", "bbb")     # invalid (not matching)
    assert validate_confirm_password("aaa", "aaa") == []  # valid (matching)
