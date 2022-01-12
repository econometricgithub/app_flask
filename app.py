#importing necessary library
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,flash, request
from wtforms import Form, StringField, validators, SubmitField, SelectField
from bioinfokit.analys import get_data, stat
#Importing SQLAlcheny
from flask_sqlalchemy import SQLAlchemy
#from custom_validators import height_validator, weight_validator

app = Flask(__name__)
app.secret_key="manbearpig_MUDMAN888"

@app.route("/")
def index():
    flash("What's your name")
    return render_template("main.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']+ ", greet to see you!"))
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)

