import psycopg2
import string
import random

from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from .models import Programmer, Admin
from ..app import app, db


# Blue prints
programmer_panel = Blueprint('programmer_panel', __name__)


# Helper functions are defined below here such as
# generating random keys, specific printing, ... etc.
def generate_random_key():
    return str(
        ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(20)
        )
    )


@programmer_panel.route("/programmer_panel/signup", methods=['POST', 'GET'])
def programmer_panel_signup():
    '''
        programmer panel signup: is the view where a new programmer to the
        company can signup their accounts
    '''
    # Deleting any sessions regarding any type of users
    session.pop("programmer_username", None)
    session.pop('programmer_logged_in', None)

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


@programmer_panel.route('/programmer_panel/login', methods=['POST', 'GET'])
def programmer_panel_login():
    '''
        programmer panel login: is where the login gate is located
    '''
    # Deleting any sessions regarding any type of users
    session.pop("programmer_username", None)
    session.pop('programmer_logged_in', None)

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
            session['programmer_logged_in'] = True
            return redirect(url_for("programmer_panel_index"))

    data = {
        "invalid_credentials": invalid_credentials,
    }
    return render_template(
        'programmer_panel/programmer_panel_login.html', data=data
    )


@programmer_panel.route('/programmer_panel/index', methods=['POST', 'GET'])
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
