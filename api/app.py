import os

from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

app = FlaskAPI(__name__)

app.config.from_object(os.environ.get("APP_SETTINGS"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models.models import Food

@app.route("/add")
def add_food():
    name=request.args.get('name')
    count=request.args.get('count')
    try:
        food=Food(
            name=name,
            count=count,
        )
        db.session.add(food)
        db.session.commit()
        return "Food added. food id={}".format(food.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    """Get all food elements"""
    try:
        food=Food.query.all()
        return  jsonify([e.serialize() for e in food])
    except Exception as e:
        return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    """Get food by id"""
    try:
        food=Food.query.filter_by(id=id_).first()
        return jsonify(food.serialize())
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    app.run()
