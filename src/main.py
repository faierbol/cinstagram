'''

    Title: Ceddit

    Desc: This project is just a reddit clone. The reason I am not putting a
          MIT license on the source code is because this is just an educational
          project for me and I want it to stay it that way.

    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com

'''

import psycopg2
import string
import random


from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#######################################################################
#                       self functions                                #
#######################################################################
def generate_random_key():
    return str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20)))



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
migrate = Migrate(app, db)


class Programmer(db.Model):
    __tablename__ = "programmer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    key = db.Column(db.String(20))

    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    key = db.Column(db.String(20))

    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)


# Create your tables -note : this is deprecated since now i am using f-migrate
# db.create_all()
# db.session.commit()


# process the login form
# db.session.query(Programmer).delete()
# db.session.commit()


#######################################################################
#  URL Paths  (change these views in to their own modules later on)   #
#######################################################################
@app.route("/")
def index():
    # delete all sessions regarding to the admin or programer (super-users)
    session.pop("programmer_username", None)

    return "index page"


@app.route('/programmer_panel/signup', methods=['POST', 'GET'])
def programmer_panel_signup():
    '''
        programmer panel signup: is the view where a new programmer to the
        company can signup their accounts
    '''
    # Deleting any sessions regarding any type of users
    session.pop("programmer_username", None)

    invalid_credentials = False
    empty_credentials = False

    # process the signup form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        key = generate_random_key()

        # check if any of the input is empty
        if bool(username) is False or bool(username.strip()) is False or \
           bool(password) is False or bool(password.strip()) is False:
            empty_credentials = True
        else:
            # If it is not empty check if the username exists, if it does
            # do not create a new user
            if Programmer.query.filter_by(username=username).first() is None:
                # User does not exists
                new_programmer = Programmer(username, password, key)
                db.session.add(new_programmer)
                db.session.commit()
                return redirect(url_for('programmer_panel_login'))
            else:
                # User exists
                invalid_credentials = True

    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
    }
    return render_template(
        'programmer_panel/programmer_panel_signup.html', data=data
    )


@app.route('/programmer_panel/login', methods=['POST', 'GET'])
def programmer_panel_login():
    '''
        programmer panel login: is where the login gate is located
    '''
    invalid_credentials = False

    # Processing the Login Form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        key = request.form["key"]
        # check if the user exists, with the given input
        if Programmer.query.filter_by(
            username=username, password=password, key=key
        ).first() is None:
            # User does not exists therefore inputs are given wrong creds
            invalid_credentials = True
        else:
            # edit the session to the user logged in
            session['programmer_username'] = username
            return redirect(url_for("programmer_panel_index"))

    data = {
        "invalid_credentials": invalid_credentials,
    }
    return render_template(
        'programmer_panel/programmer_panel_login.html', data=data
    )


@app.route('/programmer_panel/index', methods=['POST', 'GET'])
def programmer_panel_index():
    '''
        programmer panel index: is where the programmer sees a overview of all
        of the parts of the application.
    '''
    invalid_credentials = False
    empty_credentials = False

    # Admin-user CRUD operations
    # Create
    if request.form.get('create_admin_user_button'):
        username = request.form["username"]
        password = request.form["password"]
        key = generate_random_key()
        # check if any of the input is empty
        if bool(username) is False or bool(username.strip()) is False or \
           bool(password) is False or bool(password.strip()) is False:
            empty_credentials = True
        else:
            # If it is not empty check if the username exists, if it does
            # do not create a new user
            if Admin.query.filter_by(username=username).first() is None:
                # User does not exists
                new_admin = Admin(username, password, key)
                db.session.add(new_admin)
                db.session.commit()
                return redirect(url_for('programmer_panel_index'))
            else:
                # User exists
                invalid_credentials = True
    # Read
    all_admins = Admin.query.order_by(Admin.id).all()

    # Update ... I skipped this funcionality for now, will add in the future

    # Delete
    if request.form.get("delete_admin_user_button"):
        username = request.form["username"]
        # check if the admin exists
        if Admin.query.filter_by(username=username).first() is None:
            # User does not exists so do nothing
            print("user does not exists")
        else:
            selected_admin = Admin.query.filter_by(username=username).first()
            db.session.delete(selected_admin)
            db.session.commit()
            return redirect(url_for('programmer_panel_index'))

    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
        "all_admins": all_admins,
    }
    return render_template(
        'programmer_panel/programmer_panel_index.html', data=data
    )


# RUNNING THE APPLICATION ##################################################
if __name__ == "__main__":
    app.run(
        debug=True
    )
