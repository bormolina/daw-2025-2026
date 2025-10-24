import os
import sqlite3
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")
DB_PATH = os.environ.get("DB_PATH", "/data/app.db")

def db_conn():
    return sqlite3.connect(DB_PATH)

def get_user(username: str):
    """Devuelve una tupla (id, username, password_hash, role) o None si no existe."""
    with db_conn() as conn:
        cur = conn.execute(
            "SELECT id, username, password_hash, role FROM users WHERE username = ? LIMIT 1",
            (username,),
        )
        return cur.fetchone()

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        row = get_user(username)
        if row and check_password_hash(row[2], password):
            session["user"] = row[1]
            return redirect(url_for("user_profile", username=row[1]))
        else:
            error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error)

@app.route("/user/<username>")
def user_profile(username):
    """Página protegida: solo accesible si el usuario está logueado y coincide."""
    if session.get("user") != username:
        return redirect(url_for("login"))
    row = get_user(username)
    role = row[3] if row else "desconocido"
    return render_template("user.html", username=username, role=role)

@app.route("/logout")
def logout():
    """Cierra la sesión del usuario."""
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("FLASK_RUN_PORT", 5051)),
        debug=os.environ.get("FLASK_DEBUG", "0") == "1",
    )