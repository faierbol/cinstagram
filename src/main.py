'''

    Title: Ceddit

    Desc: This project is just a reddit clone. The reason I am not putting a
          MIT license on the source code is because this is just an educational
          project for me and I want it to stay it that way.

    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com

'''

import psycopg2

from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

# Part: Programmer Panel
'''
from programmer_panel_app.views import programmer_panel_login
from programmer_panel_app.views import programmer_panel_signup
from programmer_panel_app.views import programmer_panel_dashboard
'''
# models will be here too


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


#######################################################################
#  ORM (module these into the models.py part of the modules)          #
#######################################################################
# app-ORM configs
postgresql_URI = "postgresql://demir@localhost:5432/ceddit"
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_URI
db = SQLAlchemy(app)


class Programmer(db.Model):
    __tablename__ = "programmer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    key = db.Column(db.String(10))

    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)


# Create your tables
db.create_all()
db.session.commit()


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
    invalid_credentials = False

    # process the signup form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        key = request.form['key']
        # check if the programmer already exists if not create new one
        print(Programmer.query.filter_by(username=username).first().exists())
        new_programmer = Programmer(username, password, key)
        db.session.add(new_programmer)
        db.session.commit()

        return redirect(url_for('programmer_panel_login'))

    data = {
        # ...
    }
    return render_template(
        'programmer_panel/programmer_panel_signup.html', data=data
    )


@app.route('/programmer_panel/login', methods=['POST', 'GET'])
def programmer_panel_login():
    '''
        programmer panel login: is where the login gate is located
    '''

    # process the login form

    data = {

    }
    return "login gate is here"


# RUNNING THE APPLICATION ##################################################
if __name__ == "__main__":
    app.run(
        debug=True
    )
