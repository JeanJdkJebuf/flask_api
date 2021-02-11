from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

def api_display():
    """Returns api"""
    # Doing database first. Oups forgot.
    pass

if __name__ == "__main__":
    app.run(debug=True)
