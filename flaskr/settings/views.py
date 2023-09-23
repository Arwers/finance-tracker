# Standard library imports

# Third-party imports
from flask import Blueprint, render_template, request, redirect, url_for

# Local file imports


settings = Blueprint(
    "settings", __name__, template_folder="templates", static_folder="static", static_url_path="/flaskr/settings"
)


