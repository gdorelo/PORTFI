#!/usr/bin/python3
"""Script that starts a Flask web application"""
import api.models as models
from api.models.Portfolio import Portfolio
from flask import Flask
from flask import render_template
from flask import request
from api.models.engine.db_storage import DBStorage
from datetime import datetime

app = Flask(__name__)
storage = DBStorage()

@app.route('/test', strict_slashes=False)
def test_route():
    return {'name' : 'Hola'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
