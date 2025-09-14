```
Kleines Demo-Projekt für **serverseitige Formular-Validierung** (Vor-/Nachname, Username, E-Mail, Passwort + Bestätigung) mit **Flask** und **pytest**.  

Zeigt: saubere Validatoren (Python), Fehler-Rendering (Jinja2), Unit- & Integrationstests, sowie optional CI via GitHub Actions.

![tests](https://github.com/ms-ru/qa-form-validation/actions/workflows/tests.yml/badge.svg)

## Features
- Responsives 2-Spalten-Layout (mobil 1 Spalte → Desktop 2 Spalten)
- Felder: First/Last Name, Username, E-Mail, Password, Confirm Password
- Serverseitige Validierung mit klaren Fehlermeldungen
- A11y: `aria-invalid`, `aria-describedby`
- Tests: **pytest** (Unit für Validatoren, Integration via Flask `test_client`)
- CI (optional): GitHub Actions (pytest auf Push/PR)

## Tech-Stack
- Python 3.12, Flask, Jinja2
- pytest
- (optional) GitHub Actions

## Setup
```bash
python3 -m venv .venv-form-validation
source .venv-form-validation/bin/activate
pip install -r requirements.txt
python app.py
# → http://127.0.0.1:5000

## Tests
```bash
pytest -q
```

## Endpunkt
- `GET /`  – Formular anzeigen  
- `POST /` – Eingaben prüfen, Fehler/Erfolg rendern (keine Persistenz)

## Validierungsregeln (Kurz)
- **First/Last Name:** required, Länge **2–40**, nur Buchstaben (inkl. Umlaute), Leerzeichen, `'` und `-`
- **Username:** required, **3–20**, Regex `^[A-Za-z0-9_]{3,20}$`
- **E-Mail:** required, simples Format-Pattern
- **Password:** required, **12–50** Zeichen
- **Confirm Password:** muss dem Passwort entsprechen

## Projektstruktur
```text
.
├── app.py
├── validators.py
├── templates/
│   ├── base.html
│   └── form.html
├── static/
│   ├── styles.css
│   └── script.js
└── tests/
    ├── conftest.py
    ├── test_first_name.py
    ├── test_app_get.py
    └── test_other_validators.py
```

## Hinweise
- Keine Datenbank/Persistenz – Fokus ist Validierung & Testbarkeit.
- **(Next Steps):**
  - POST→Redirect→GET (PRG-Pattern) einbauen
  - „Passwort anzeigen“-Toggle (kleines JS + CSS)
  - Live-Hinweise clientseitig (progressive enhancement)

## Lizenz
MIT – frei nutzbar zu Demo-/Lernzwecken.
