from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import secrets
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Session config
app.permanent_session_lifetime = timedelta(minutes=30)
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Demo users (hashed passwords)
users = {
    "admin": generate_password_hash("Admin@123"),
    "lale": generate_password_hash("Lale@123"),
    "test": generate_password_hash("Test@123")
}

# Username validation
def validate_username(username):
    return bool(re.match(r"^[A-Za-z0-9_]{3,20}$", username))

# Password policy validation
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        return False
    return True

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Input validation
        if not validate_username(username):
            return render_template("login.html", error="Invalid username format ❌")
        if username not in users:
            return render_template("login.html", error="Wrong username or password ❌")
        if not validate_password(password):
            return render_template("login.html", error="Password does not meet policy ❌")

        # Check hashed password
        if check_password_hash(users[username], password):
            session.permanent = True
            session["user"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Wrong username or password ❌")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
