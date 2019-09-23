'''

    Title: Ceddit

    Desc: This project is just a reddit clone. The reason I am not putting a
          MIT license on the source code is because this is just an educational
          project for me and I want it to stay it that way.

    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com

'''

# core python modules

from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy

# views for url pathing
'''
from programmer_panel_app.views import programmer_panel_login
from programmer_panel_app.views import programmer_panel_signup
from programmer_panel_app.views import programmer_panel_dashboard
'''


#######################################################################
#                       Configuration                                 #
#######################################################################
app = Flask(__name__)
app.config["static_folder"] = "./static"
app.config["template_folder"] = "./templates"
app.config["secret_key"] = "change-this-in-production"
app.config["debug"] = True
app.config["host"] = "127.0.0.1"
app.config["port"] = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"


#######################################################################
#                           ORM                                       #
#######################################################################
db = SQLAlchemy(app)


class programmers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    key = db.Column(db.String(10))

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)


#######################################################################
#  URL Paths  (change these views in to their own modules later on)   #
#######################################################################
@app.route("/")
def index():
    return "hello"


@app.route('/programmer_panel/signup', methods=['POST', 'GET'])
def programmer_panel_signup():
    '''
        programmer panel signup: is the view where a new programmer to the
        company can signup their accounts
    '''

    # process the signup form
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['password'])
        print(request.form['key'])

    data = {

    }
    return render_template(
        'programmer_panel/programmer_panel_signup.html', data=data
    )


# RUNNING THE APPLICATION
if __name__ == "__main__":
    app.run()
