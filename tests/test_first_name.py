import pytest
from validators import validate_first_name

@pytest.mark.parametrize("v", ["", " ", None])
def test_required(v):
    assert "required" in " ".join(validate_first_name(v)).lower()

@pytest.mark.parametrize("v", ["A", "Z"*41])
def test_length(v):
    msg = " ".join(validate_first_name(v))
    assert "2-40" in msg

@pytest.mark.parametrize("v", ["J0hn", "Ann@", "Max_"])
def test_invalid_chars(v):
    msg = " ".join(validate_first_name(v))
    assert "letters" in msg  # Hinweistext enthält 'letters'

def test_ok():
    assert validate_first_name("Max") == []
    assert validate_first_name("Jean-Luc") == []
    assert validate_first_name("O'Connor") == []
