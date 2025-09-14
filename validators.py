# Imports
import re  # Regular expressions for pattern-based string validation


def _is_blank(v: str | None) -> bool:
    """
    Helper function to check if a string is empty or None.
    Returns True if the value is None, empty, or only whitespace.
    """
    return v is None or v.strip() == ""


def validate_first_name(v: str | None) -> list[str]:
    """
    Validate a first name.
    Rules:
    - Required (cannot be empty)
    - Must be 2–40 characters long
    - Allowed characters: letters, spaces, hyphens, apostrophes (including accents/umlauts)
    """
    if _is_blank(v):
        return ["First name is required"]

    v = v.strip()
    errors: list[str] = []

    if not (2 <= len(v) <= 40):
        errors.append("First name must be 2-40 characters.")

    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ' -]+", v):
        errors.append(
            "First name may only contain letters, spaces, hyphens or apostrophes."
        )

    return errors


def validate_last_name(v: str | None) -> list[str]:
    """
    Validate a last name.
    Rules:
    - Required (cannot be empty)
    - Must be 2–40 characters long
    - Allowed characters: letters, spaces, hyphens, apostrophes (including accents/umlauts)
    """
    if _is_blank(v):
        return ["Last name is required"]

    v = v.strip()
    errors: list[str] = []

    if not (2 <= len(v) <= 40):
        errors.append("Last name must be 2-40 characters.")

    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ' -]+", v):
        errors.append(
            "Last name may only contain letters, spaces, hyphens or apostrophes."
        )

    return errors


def validate_username(v: str | None) -> list[str]:
    """
    Validate a username.
    Rules:
    - Required (cannot be empty)
    - Must follow a valid email format
    """
    if _is_blank(v):
        return ["Username is required."]

    v = v.strip()

    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v):
        return []

    return ["E-mail format looks invalid."]


def validate_email(v: str | None) -> list[str]:
    """
    Validate an email address.
    Rules:
    - Required (cannot be empty)
    - Must follow a valid email format
    """
    if _is_blank(v):
        return ["E-Mail is required."]

    v = v.strip()

    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", v):
        return []

    return ["E-Mail looks invalid."]


def validate_password(v: str | None) -> list[str]:
    """
    Validate a password.
    Rules:
    - Required (cannot be empty)
    - Must be 12–50 characters long
    """
    if _is_blank(v):
        return ["Password is required."]

    if 12 <= len(v or "") <= 50:
        return []

    return ["Password must be 12-50 characters."]


def validate_confirm_password(password: str | None, confirm: str | None) -> list[str]:
    """
    Validate the confirmation password.
    Rules:
    - Must match the original password exactly
    """
    return [] if (password or "") == (confirm or "") else ["Passwords do not match."]
