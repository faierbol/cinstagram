from flask import Flask, request, render_template, redirect, session, url_for
from flask import Blueprint

from .models import User
from ..app import db

# Blue prints
authentication = Blueprint("authentication", __name__)


@authentication.route("/auth/signup", methods=["POST", "GET"])
def auth_signup():
    """
        auth_signup: is the page that seperates the curious noisy anon users
        from the real users. You cannot see other than public profiles if you
        are not signed in the the app.
    """
    # Deleting any sessions regarding top-tier type of users
    session.pop("programmer_username", None)
    session.pop("programmer_logged_in", None)
    # admin user session pop
    # admin user session pop
    # normal user session pop
    # normal user session pop

    invalid_credentials = False
    empty_credentials = False

    # Signup Form Validation
    if request.form.get("signup_submit_btn"):
        email = request.form["email"]
        full_name = request.form["fullName"]
        username = request.form["username"]
        password = request.form["password"]

        # check if the inputs are empty or not
        if (
            bool(email) is False
            or bool(email.strip()) is False
            or bool(full_name) is False
            or bool(full_name.strip()) is False
            or bool(username) is False
            or bool(username.strip()) is False
            or bool(password) is False
            or bool(password.strip()) is False
        ):
            empty_credentials = True
        else:
            # If it is not empty check if the username exists, if it does
            # do not create a new user
            if (
                User.query.filter_by(username=username).first() is None
                or User.query.filter_by(email=email).first() is None
            ):
                # User does not exist
                new_user = User(email, full_name, username, password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("authentication.auth_login"))
            else:
                # User exists
                invalid_credentials = True

    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
    }
    return render_template("authentication/signup.html", data=data)


@authentication.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    """
        There is no need to explain a lot about it this the login for users
    """
    # Deleting any sessions regarding top-tier type of users
    session.pop("programmer_username", None)
    session.pop("programmer_logged_in", None)
    # admin user session pop
    # admin user session pop
    # normal user session pop
    # normal user session pop

    invalid_credentials = False
    empty_credentials = False

    # Login Form Validation
    if request.form.get("login_submit_btn"):
        email = request.form["email"]
        password = request.form["password"]
        # check if the inputs are empty or not
        if (
            bool(email) is False
            or bool(email.strip()) is False
            or bool(password) is False
            or bool(password.strip()) is False
        ):
            empty_credentials = True
        else:
            # Check if the user credits are right and if they
            # are log the user into the system and add sessions
            if User.query.filter_by(email=email, password=password).first() is None:
                # User does not exist
                invalid_credentials = True
            else:
                # Add the session variables than redirect the user
                session["cinstagram_user_email"] = email
                session["cinstagram_user_logged_in"] = True
                return redirect(url_for("home.home_page"))
    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
    }
    return render_template("authentication/login.html", data=data)


# Thank you for signig up will be added

# Setting up acount will be added

# Forgot password link will be added


# Static page of terms and legal will be added (not linking to about i will add
# a new single simple single web page)
