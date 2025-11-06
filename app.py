from flask import Flask, render_template, request, redirect, url_for, flash
from library import Library

app = Flask(__name__)
app.secret_key = "dev-key"
lib = Library()

def seed_if_empty():
    if not lib.books:
        lib.add_book("Shelly")
        lib.add_book("Colt")
        lib.add_book("Bull")
        lib.add_book("Jessie")
        lib.add_book("Nita")

@app.route("/")
def index():
    seed_if_empty()
    totals = {
        "books": lib.total_votes(),  # total de votos
        "members": lib.total_voters(),  # personas que votaron
        "available": lib.unique_brawlers_voted()  # brawlers únicos votados
    }
    active_loans = 0  # ya no se usa
    return render_template("index.html", totals=totals, active_loans=active_loans)

@app.route("/books", methods=["GET", "POST"])
def books():
    seed_if_empty()
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Nombre del brawler requerido.", "error")
        else:
            lib.add_book(title)
            flash("Brawler agregado.", "success")
            return redirect(url_for("books"))
    return render_template("books.html", books=lib.books, q="")

@app.route("/members", methods=["GET", "POST"])
def members():
    seed_if_empty()
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        brawler_id = int(request.form.get("brawler_id"))
        if not name:
            flash("Nombre requerido.", "error")
        else:
            lib.add_member(name, brawler_id)
            flash("Voto registrado.", "success")
            return redirect(url_for("members"))
    return render_template("members.html", members=lib.members, books=lib.books)

@app.route("/loans")
def loans():
    return redirect(url_for("index"))  # ya no se usa

    

