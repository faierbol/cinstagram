from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db


# Blue prints
api_web = Blueprint("api_web", __name__)


@api_web.route("/api_web", methods=["POST", "GET"])
def api_web_landing_page():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("api_web/index_page.html", data=data)


@api_web.route("/api_web/register", methods=["POST", "GET"])
def api_web_register():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("api_web/register_page.html", data=data)


@api_web.route("/api_web/PostIdPath", methods=["POST", "GET"])
def api_web_post_page():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("api_web/post_page.html", data=data)
