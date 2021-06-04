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


@app.route('/', strict_slashes=False)
@app.route('/', methods=["GET", "POST"])
def dashboard_form():
    if request.method == "POST":
        if verify_input() == True:
            return render_template("index.html", portfolio=models.portfolio, bechmarck=models.bechmarck)
    return render_template("index.html", portfolio=models.portfolio, bechmarck=models.bechmarck)
        # ticker = request.form.get("ticker").upper()
        # if ticker == "":
        #     ticker = "AAPL"  # PENSAR QUE VAMOS HACER SI ESTA VACIO?
        # weight = 0.0
        # try:
        #     weight = float(request.form.get("weight"))
        # except:
        #     pass
        
        # start = request.form.get('start')
        # end = request.form.get('end')
        # # verificar ticker y weight
        # if verify_weight(ticker, weight, models.portfolio.assets):
        #     models.portfolio.get_data_API(start, end)
        #     models.bechmarck.get_data_API(start, end)
        #     models.portfolio.calculate_available()
        #     return render_template("index.html", portfolio=models.portfolio, bechmarck=models.bechmarck)

        #SALVA LA INFORMACION DEL PORTFOLIO Y LAS RELACIONES CON EL USUARIO EN LA BD
        # models.bechmarck.save_data(models.user_admin)
        # models.portfolio.save_data(models.user_admin)
    


def verify_weight(ticker, weight, assets):
    '''verfify that weight do not exceed 100%'''
    total = 0
    if weight == 0:
        return False
    for value in assets.values():
        total += value
    if total + weight <= 1:
        models.portfolio.assets[ticker] = weight
        total += weight
        return True
    return False

def verify_input():
    """Verifies the Input of the User"""
    # if ticker == "":
    #     ticker = "AAPL"  # PENSAR QUE VAMOS HACER SI ESTA VACIO?
    weight = 0.0
    try:
        ticker = request.form.get("ticker").upper()
        if ticker == None:
            return False
        weight = float(request.form.get("weight"))
    except:
        return False
    
    
    start = request.form.get('start')
    end = request.form.get('end')
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')
    if end < start or start > end or end > datetime.today():
        return False
    # verificar ticker y weight
    if verify_weight(ticker, weight, models.portfolio.assets):
        models.portfolio.get_data_API(start, end)
        models.bechmarck.get_data_API(start, end)
        models.portfolio.calculate_available()
        return True
    return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
