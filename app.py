# Imports 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])

def form(): 
    return render_template(
        "form.html", 
        title = "Registrierung",
        errors = {},
        success = False
    )

if __name__ == "__main__": 
    app.run(debug=True)