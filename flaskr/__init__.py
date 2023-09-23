from flask import Flask, current_app

def create_app(config_filename="config.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile(config_filename)

    # database
    from .models import db
    db.init_app(app)
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
    "PLN": "zł", # Polish złoty
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


    # blueprints
    from .homepage.views import homepage
    from .settings.views import settings
    app.register_blueprint(homepage)
    app.register_blueprint(settings)

    return app
