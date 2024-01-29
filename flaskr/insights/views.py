# Standard library imports

# Third-party imports
from flask import Blueprint, render_template, request, redirect, url_for, current_app

# Local file imports


insights = Blueprint(
    "insights", __name__, template_folder="templates", static_folder="static",
)

@insights.route("/insights")
def index():
    return render_template(
        "insights/index.html",
        limit=current_app.limit,
        categories=current_app.categories,
        currency_symbol=current_app.currencies[current_app.currency],
        total_costs=current_app.total_costs
    )