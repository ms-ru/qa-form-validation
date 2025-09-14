# Imports 
from flask import Flask, render_template, request

from validators import (
    validate_first_name, validate_last_name,
    validate_username, validate_email,
    validate_password, validate_confirm_password
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def form():
    
    errors: dict[str, list[str]] = {}
    values: dict[str, str] = {}
    success = False

    if request.method == "POST":
        
        values = {
            "user_first_name":   request.form.get("user_first_name", ""),
            "user_last_name":    request.form.get("user_last_name", ""),
            "username":          request.form.get("username", ""),
            "user_mail_address": request.form.get("user_mail_address", ""),
        }
        pwd  = request.form.get("user_password", "")
        pwd2 = request.form.get("confirm_user_password", "")

        # Validations
        
        # First name 
        e = validate_first_name(values["user_first_name"])
        if e: 
            errors["user_first_name"] = e
        
        # Last name
        e = validate_last_name(values["user_last_name"])
        if e: 
            errors["user_last_name"]  = e
        
        # User name
        e = validate_username(values["username"])
        if e: 
            errors["username"]        = e
        
        # E-Mail address 
        e = validate_email(values["user_mail_address"])
        if e:
            errors["user_mail_address"] = e
        
        # Password
        e = validate_password(pwd)
        if e: 
            errors["user_password"]   = e
        
        # Password confirmation 
        e = validate_confirm_password(pwd, pwd2)
        if e:
            errors["confirm_user_password"] = e

        success = not errors

    return render_template(
        "form.html",
        title="Registrierung",
        errors=errors,
        values=values,
        success=success,
    )

if __name__ == "__main__":
    app.run(debug=True)
