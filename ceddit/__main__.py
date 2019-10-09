#
#    Title: Ceddit
#
#    Desc: This project is just a reddit clone. The reason I am not putting a
#          MIT license on the source code is because this is just an education
#          -al project for me and I want it to stay it that way.
#
#    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com
#

from flask import Flask
from .views.programmer_panel import programmer_panel

app = Flask(__name__)

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
