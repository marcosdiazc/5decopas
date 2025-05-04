from flask import Flask, render_template, request, redirect, session, url_for, flash
import os
from db import get_connection

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")  # para sesiones

# Admin hardcodeado
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            flash("Sesión iniciada correctamente", "success")
            return redirect("/admin")
        else:
            flash("Usuario o contraseña incorrectos", "error")
            return redirect("/login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    flash("Sesión cerrada", "info")
    return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("admin_logged_in"):
        flash("Tenés que iniciar sesión", "error")
        return redirect("/login")

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        position = request.form.get("position")
        genero = request.form.get("genero")
        equipo = request.form.get("equipo")

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO jugadores (name, email, position, genero, equipo)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, position, genero, equipo))
        conn.commit()
        cur.close()
        conn.close()

        flash("Jugador agregado con éxito", "success")
        return redirect("/admin")

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
