import os

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy

app = FlaskAPI(__name__)

app.config.from_object(os.environ.get("APP_SETTINGS"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models.models import Food

@app.route("/api")
def api_details():
    """Returns api"""
    # Doing database first. Oups forgot.
    return {
        random : "test"
    }

if __name__ == "__main__":
    app.run()
