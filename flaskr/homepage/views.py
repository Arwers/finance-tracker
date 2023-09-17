from flask import Blueprint, render_template, request, redirect, url_for
from .utils import *
from ..models import db, Expenses, add_record, delete_record

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
all_costs = 444
limit = 2000

@homepage.route("/")
def index():
    return render_template(
        "index.html",
        expenses=expenses,
        all_costs=all_costs,
        limit=limit,
        categories=categories,
    )


@homepage.route("/add", methods=["POST"])
def add():
    # gather data
    name = request.form["name"]
    cost = int(request.form["cost"])
    date = request.form["date"]
    category = request.form["category"]

    # add record to db
    record = Expenses(name, cost, date, category)
    add_record(record)

    return redirect(url_for("homepage.index"))


@homepage.route("/add_limit", methods=["POST"])
def add_limit():
    global limit
    limit = request.form["limit"]

    return redirect(url_for("homepage.index"))


@homepage.route("/delete/<int:index>")
def delete(id):
    try:
        record = db.get_or_404(Expenses, id)
        delete_record(record)
    except 404:
        pass
    
    return redirect(url_for("homepage.index"))
