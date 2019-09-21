'''

    Title: Ceddit

    Desc: This project is just a reddit clone. The reason I am not putting a
          MIT license on the source code is because this is just an educational
          project for me and I want it to stay it that way.

    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com

'''

# core python modules

from flask import Flask, request, render_template, redirect, session

# views for url pathing
from programmer_panel_app.views import programmer_panel_login
from programmer_panel_app.views import programmer_panel_signup
from programmer_panel_app.views import programmer_panel_dashboard


#######################################################################
#                       Configuration                                 #
#######################################################################
app = Flask(
    __name__,
    static_folder="./static",
    template_folder="./templates"
)

app.secret_key = "change this in production"
app.debug = True
app.host = "127.0.0.1"
app.port = 5000


#######################################################################
#                       URL Paths                                     #
#######################################################################
@app.route("/")
def index():
    return "hello"


# Programming Panel url paths
app.add_url_rule('/programmer_panel/login', 'programmer_panel_login', programmer_panel_login)
app.add_url_rule('/programmer_panel/signup', 'programmer_panel_signup', programmer_panel_signup)
app.add_url_rule('/programmer_panel/dashboard', 'programmer_panel_dashboard', programmer_panel_dashboard)


# RUNNING THE APPLICATION
if __name__ == "__main__":
    app.run()
