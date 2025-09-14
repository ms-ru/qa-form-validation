# Imports 
import re


def _is_blank(v: str | None) -> bool: 
    return v is None or v.strip() == ""


def validate_first_name(v: str | None) -> list[str]:
    """
    Rules: 
    - required 
    - length 2-40 chars 
    - only letters + space (inkl. Umlaute)
    """
    
    if _is_blank(v): 
      return ["First name is required"]
    
    v = v.strip() 
    errors: list[str] = []
    
    if not (2 <= len(v) <= 40):
        errors.append("First name must be 2-40 characters.")
    
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ' -]+", v):
        errors.append("First name may only contain letters, spaces, hyphens or apostrophes.")

    return errors

def validate_last_name(v: str | None) -> list[str]: 
    """
    Rules: 
    - required 
    - length 2-40 chars 
    - only letters + space (inkl. Umlaute)
    """
    
    if _is_blank(v): 
        return ["Last name is required"]
    
    v = v.strip()
    errors: list[str] = []
    
    if not (2 <= len(v) <= 40):
        errors.append("Last name must be 2-40 characters.")
    
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ' -]+", v):
        errors.append("Last name may only contain letters, spaces, hyphens or apostrophes.")
    
    return errors

def validate_username(v: str | None) -> list[str]: 
    
    if _is_blank(v): 
        return ["Username is required."]
    
    v = v.strip()
    
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v): 
        return []
    
    return ["E-mail format looks invalid."]

def validate_email(v: str | None) -> list[str]:
    if _is_blank(v): 
        return ["E-Mail is required."]
    
    v = v.strip()
    
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v): 
        return []
    
    return["E-Mail looks invalid."]


def validate_password(v: str | None) -> list[str]:
    
    if _is_blank(v):
        return ["Password is required."]
    
    if 12 <= len(v or "") <= 50:
        return []
    return ["Password must be 12-50 characters."]

def validate_confirm_password(password: str | None, confirm: str | None) -> list[str]:
    
    return [] if (password or "") == (confirm or "") else ["Passwords do not match."]