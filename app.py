# Imports
from flask import Flask, render_template, request

# Import custom validation functions from validators.py
from validators import (
    validate_first_name, validate_last_name,
    validate_username, validate_email,
    validate_password, validate_confirm_password
)

# Initialize Flask application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    """
    Handle the registration form.
    - GET: show empty form
    - POST: validate submitted data
    """
    # Store validation errors for each field
    errors: dict[str, list[str]] = {}
    # Store submitted values to refill the form after POST
    values: dict[str, str] = {}
    # Flag to check if form submission was successful
    success = False

    # Check if user submitted the form
    if request.method == "POST":

        # Collect form values (with defaults if missing)
        values = {
            "user_first_name":   request.form.get("user_first_name", ""),
            "user_last_name":    request.form.get("user_last_name", ""),
            "username":          request.form.get("username", ""),
            "user_mail_address": request.form.get("user_mail_address", ""),
        }
        # Password fields are handled separately
        pwd = request.form.get("user_password", "")
        pwd2 = request.form.get("confirm_user_password", "")

        # --- Validations ---

        # First name
        e = validate_first_name(values["user_first_name"])
        if e:
            errors["user_first_name"] = e

        # Last name
        e = validate_last_name(values["user_last_name"])
        if e:
            errors["user_last_name"] = e

        # Username
        e = validate_username(values["username"])
        if e:
            errors["username"] = e

        # E-Mail address
        e = validate_email(values["user_mail_address"])
        if e:
            errors["user_mail_address"] = e

        # Password
        e = validate_password(pwd)
        if e:
            errors["user_password"] = e

        # Password confirmation
        e = validate_confirm_password(pwd, pwd2)
        if e:
            errors["confirm_user_password"] = e

        # Form is successful if no errors exist
        success = not errors

    # Render the form template with current state
    return render_template(
        "form.html",
        title="Registrierung",  # Page title shown in the template
        errors=errors,          # Validation messages
        values=values,          # Refilled input values
        success=success,        # Success flag
    )


if __name__ == "__main__":
    # Run the Flask app in debug mode 
    app.run(debug=True)
