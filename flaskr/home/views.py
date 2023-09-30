# Standard library imports
from datetime import date

# Third-party imports
from flask import Blueprint, render_template, request, redirect, url_for, current_app

# Local file imports
from ..models import db, Expenses, add_record, delete_record
from .utils import *


home = Blueprint(
    "home", __name__, template_folder="templates", static_folder="static", static_url_path="/flaskr/home"
)
temp_expenses = Expenses.query.all()
all_costs = {key: 0 for key in ["total"] + current_app.categories}
all_costs = set_all_costs(all_costs, temp_expenses)


@home.route("/")
def index():
    return render_template(
        "index.html",
        expenses=Expenses.query.all(),
        all_costs=all_costs,
        limit=current_app.limit,
        categories=current_app.categories,
        currency_symbol=current_app.currencies[current_app.currency]
    )


@home.route("/add", methods=["POST"])
def add():
    # gather data
    name = request.form["name"]
    cost = int(request.form["cost"])
    day = date.fromisoformat(request.form["date"])
    category = request.form["category"]

    # add record to db
    record = Expenses(name, cost, day, category)
    add_record(record)

    # update all_costs
    all_costs["total"] += cost
    all_costs[category] += cost

    return redirect(url_for("home.index"))


@home.route("/delete/<int:id>")
def delete(id):
    record = db.get_or_404(Expenses, id)

    # update all_costs
    all_costs["total"] -= record.cost
    all_costs[record.category] -= record.cost

    delete_record(record)

    return redirect(url_for("home.index"))


@home.route("/add_limit", methods=["POST"])
def add_limit():
    global limit
    limit = request.form["limit"]

    return redirect(url_for("home.index"))
