from flask import Flask, render_template, request
from validators import validate_first_name

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    # 1) Container vorbereiten
    errors: dict[str, list[str]] = {}
    values: dict[str, str] = {}
    success = False

    # 2) Bei POST: Wert holen und prüfen
    if request.method == "POST":
        values["user_first_name"] = request.form.get("user_first_name", "")
        e = validate_first_name(values["user_first_name"])
        if e:
            errors["user_first_name"] = e
        success = (len(errors) == 0)

    # 3) Template mit Daten rendern
    return render_template(
        "form.html",
        title="Registrierung",
        errors=errors,
        values=values,
        success=success,
    )

if __name__ == "__main__":
    app.run(debug=True)
