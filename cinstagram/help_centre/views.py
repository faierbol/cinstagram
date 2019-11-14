from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

# from .models import
from ..app import db


# Blue prints
help_centre = Blueprint("help_centre", __name__)


@help_centre.route("/help_centre/index", methods=["POST", "GET"])
def help_centre_index():
    """

    """
    # Deleting any sessions regarding programmer user and normal users

    data = {}
    return render_template("help_centre/main_page.html", data=data)


@help_centre.route("/help_centre/topic/using_instagram", methods=["POST", "GET"])
def help_centre_using_instagram():
    """

    """

    # Deleting any sessions regarding programmer user and normal users

    data = {}
    return render_template("help_centre/topic_page.html", data=data)


# HELP CENTRE POST VIEW WILL BE ADDED
