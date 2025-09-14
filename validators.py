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