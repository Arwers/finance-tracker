from flask import Flask, current_app


def create_app(config_filename="config.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile(config_filename)

    # database
    from .models import db

    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.app_context().push()

    # context variables
    current_app.limit = 2000
    current_app.categories = [
        "food",
        "car",
        "house",
        "health",
        "taxes",
        "other",
    ]
    current_app.currencies = {
        "PLN": "zł",  # Polish złoty
        "USD": "$",  # United States Dollar
        "EUR": "€",  # Euro
        "JPY": "¥",  # Japanese Yen
        "GBP": "£",  # British Pound Sterling
        "AUD": "A$",  # Australian Dollar
        "CAD": "C$",  # Canadian Dollar
        "CHF": "CHF",  # Swiss Franc
        "CNY": "¥",  # Chinese Yuan
        "SEK": "kr",  # Swedish Krona
        "NZD": "NZ$",  # New Zealand Dollar
        "MXN": "Mex$",  # Mexican Peso
        "SGD": "S$",  # Singapore Dollar
        "HKD": "HK$",  # Hong Kong Dollar
        "NOK": "kr",  # Norwegian Krone
        "KRW": "₩",  # South Korean Won
        "TRY": "₺",  # Turkish Lira
        "INR": "₹",  # Indian Rupee
        "BRL": "R$",  # Brazilian Real
        "ZAR": "R",  # South African Rand
    }
    # current chosen currency
    current_app.currency = "PLN"
    current_app.total_costs = {key: 0 for key in ["total"] + current_app.categories}

    # blueprints
    from .home.views import home
    from .settings.views import settings
    from .insights.views import insights

    app.register_blueprint(home)
    app.register_blueprint(settings)
    app.register_blueprint(insights)

    return app
