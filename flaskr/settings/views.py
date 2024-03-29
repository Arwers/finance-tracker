# Standard library imports

# Third-party imports
from flask import Blueprint, render_template, request, redirect, url_for, current_app

# Local file imports


settings = Blueprint(
    "settings",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@settings.route("/settings")
def index():
    return render_template(
        "settings/index.html",
        limit=current_app.limit,
        categories=current_app.categories,
        currency=current_app.currency,
        currencies=current_app.currencies,
    )


@settings.route("/settings/add_limit", methods=["POST"])
def add_limit():
    current_app.limit = request.form["limit"]

    return redirect(url_for("settings.index"))


@settings.route("/settings/add_currency", methods=["POST"])
def add_currency():
    current_app.currency = request.form["currency_option"]

    return redirect(url_for("settings.index"))
