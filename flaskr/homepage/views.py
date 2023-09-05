from flask import Blueprint, render_template, request, redirect, url_for
from .utils import *


homepage = Blueprint(
    "profile", __name__, template_folder="templates", static_folder="static"
)


@homepage.route("/")
def index():
    return render_template("index.html", expenses=expenses, total_cost=total_cost)


@homepage.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    cost = int(request.form["cost"])
    date = request.form["date"]

    expenses.append({"name": name, "cost": cost, "date": date})
    total_cost_update(cost)

    return redirect(url_for("index"))


@homepage.route("/delete/<int:index>")
def delete(index):
    delated_cost = -expenses[index]["cost"]
    total_cost_update(delated_cost)

    del expenses[index]
    return redirect(url_for("index"))
