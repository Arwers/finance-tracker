from flask import Blueprint, render_template, request, redirect, url_for
from .utils import *
from ..models import db, Expenses, add_record, delete_record
from datetime import date
homepage = Blueprint(
    "homepage", __name__, template_folder="templates", static_folder="static"
)

categories = [
    "food",
    "car",
    "house",
    "health",
    "taxes",
    "other",
]

expenses = {}
all_costs = {}
limit = 2000


@homepage.route("/")
def index():
    return render_template(
        "index.html",
        expenses=Expenses.query.all(),
        all_costs=all_costs,
        limit=limit,
        categories=categories,
    )


@homepage.route("/add", methods=["POST"])
def add():
    # gather data
    name = request.form["name"]
    cost = int(request.form["cost"])
    day = date.fromisoformat(request.form["date"])
    category = request.form["category"]
    
    # add record to db
    record = Expenses(name, cost, day, category)
    add_record(record)

    return redirect(url_for("homepage.index"))


@homepage.route("/delete/<int:id>")
def delete(id):
    record = db.get_or_404(Expenses, id)
    delete_record(record)

    return redirect(url_for("homepage.index"))


@homepage.route("/add_limit", methods=["POST"])
def add_limit():
    global limit
    limit = request.form["limit"]

    return redirect(url_for("homepage.index"))

