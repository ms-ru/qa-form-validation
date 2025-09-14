from validators import (
    validate_last_name, validate_username, validate_email,
    validate_password, validate_confirm_password
)

def test_last_name_ok_and_bad():
    assert validate_last_name("O'Neil") == []
    assert validate_last_name("A")  

def test_username_rules():
    assert validate_username("ok_name_123") == []
    assert validate_username("ab")          
    assert validate_username("bad name")   

def test_email_rules():
    assert validate_email("me@example.com") == []
    assert validate_email("no-at.com")      

def test_password_and_confirm():
    assert validate_password("abcdefghijkl") == []
    assert validate_password("short")        
    assert validate_confirm_password("aaa","bbb")  
    assert validate_confirm_password("aaa","aaa") == []
