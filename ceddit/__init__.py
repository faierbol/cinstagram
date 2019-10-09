#
#    Title: Ceddit
#
#    Desc: This project is just a reddit clone. The reason I am not putting a
#          MIT license on the source code is because this is just an education
#          -al project for me and I want it to stay it that way.
#
#    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com
#

import psycopg2  # needed for database configs

from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .programmer_panel.views import programmer_panel

app = Flask(__name__)
# SQLAlchemy and Migrate(alembic) configs
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["static_folder"] = "./static"
app.config["template_folder"] = "./templates"
app.secret_key = "changeThisInProduction"
app.debug = True

# Database configs
postgresql_URI = "postgresql://demir@localhost:5432/ceddit"
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_URI


# Programmer Panel
# ----------------
# This is where the neccessary views regarding the programmer panel app of the
# site is included, the programmer_panel is a dashboard and a control panel
# for the programmers(super-users) of the site, yes the "admin" is a superuser
# too but admin mostly deals with the content of the site, where the programm-
# -ers deal with site-realibity, graphs of the bandwith usage, ... etc.
app.register_blueprint(programmer_panel)


@app.route("/")
def index():
    return "index page"
