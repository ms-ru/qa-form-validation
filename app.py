from flask import Flask, render_template, request
from validators import validate_first_name

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    
    errors: dict[str, list[str]] = {}
    values: dict[str, str] = {}
    success = False

    if request.method == "POST":
        values["user_first_name"] = request.form.get("user_first_name", "")
        e = validate_first_name(values["user_first_name"])
        if e:
            errors["user_first_name"] = e
        success = (len(errors) == 0)

    return render_template(
        "form.html",
        title="Registrierung",
        errors=errors,
        values=values,
        success=success,
    )

if __name__ == "__main__":
    app.run(debug=True)
