from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db


# Blue prints
home = Blueprint("home", __name__)


@home.route("/home", methods=["POST", "GET"])
def home():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("home/home.html", data=data)
