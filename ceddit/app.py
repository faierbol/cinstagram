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

# the app is defined above url blueprint imports in order
# to avoid circular imports
app = Flask(__name__)

app.config["static_folder"] = "./static"
app.config["template_folder"] = "./templates"
app.secret_key = "changeThisInProduction"
app.debug = True

# Database configs
postgresql_URI = "postgresql://demir@localhost:5432/ceddit"
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_URI

# SQLAlchemy and Migrate(alembic) configs
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Url blueprint imports
from .programmer_panel.views import programmer_panel
from .authentication.views import authentication


# Programmer Panel
# ----------------
# This is where the neccessary views regarding the programmer panel app of the
# site is included, the programmer_panel is a dashboard and a control panel
# for the programmers(super-users) of the site, yes the "admin" is a superuser
# too but admin mostly deals with the content of the site, where the programm-
# -ers deal with site-realibity, graphs of the bandwith usage, ... etc.
app.register_blueprint(programmer_panel)


# Authentication
# ----------------
# These blueprints contains the user authentication system for the end users
# of the site such as the "average joe" and not admin, top tier user ... etc.
app.register_blueprint(authentication)


@app.route("/")
def index():
    return "index page"
