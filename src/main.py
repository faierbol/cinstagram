#
#    Title: Ceddit
#
#    Desc: This project is just a reddit clone. The reason I am not putting a
#          MIT license on the source code is because this is just an educational
#          project for me and I want it to stay it that way.
#
#    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com
#

import psycopg2
import string
import random

from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import development_config

from .views.programmer_panel import programmer_panel


# Configuration
# -------------------------------
# This is where the application's configuration settings's (dict key's) are set
app = Flask(__name__)

development_config(app)

# SQLAlchemy and Migrate(alembic) configs
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# URL PATHS OF THE APPLICATION
# -------------------------------
@app.route("/")
def index():
    # delete all sessions regarding to the admin or programer (super-users)
    #session.pop("programmer_username", None)
    #session.pop('programmer_logged_in', None)

    return "index page"


# Programmer Panel
# ----------------
# This is where the neccessary views regarding the programmer panel app of the
# site is included, the programmer_panel is a dashboard and a control panel
# for the programmers(super-users) of the site, yes the "admin" is a superuser
# too but admin mostly deals with the content of the site, where the programm-
# -ers deal with site-realibity, graphs of the bandwith usage, ... etc.
app.register_blueprint(programmer_panel)
