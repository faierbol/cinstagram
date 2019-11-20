from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from .models import User
from ..app import db

# Blue prints
authentication = Blueprint("authentication", __name__)


@authentication.route("/auth/signup", methods=["POST", "GET"])
def auth_signup():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("authentication/signup.html", data=data)


@authentication.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("authentication/login.html", data=data)


# Forgot password link will be added


# Static page of terms and legal will be added (not linking to about i will add
# a new single simple single web page)
