import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask import Flask
from app.ext import db, migrate
from app.blueprints import home


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # Extensions
    db.configure(app)
    migrate.configure(app)

    # Blueprints
    home.configure(app)

    return app
