from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db


# Blue prints
profile = Blueprint("profile", __name__)


@profile.route("/profile/posts_page", methods=["POST", "GET"])
def profile_posts_page():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/posts_page.html", data=data)


@profile.route("/profile/SinglePostPageId", methods=["POST", "GET"])
def profile_post_page():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/post_page.html", data=data)


@profile.route("/profile/followers", methods=["POST", "GET"])
def profile_followers():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/followers.html", data=data)


# add following


@profile.route("/profile/likers", methods=["POST", "GET"])
def profile_likers():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/likers.html", data=data)


@profile.route("/profile/saved", methods=["POST", "GET"])
def profile_saved():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/saved_page.html", data=data)


@profile.route("/profile/tagged", methods=["POST", "GET"])
def profile_tagged():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile/tagged_page.html", data=data)


# -------------------- OTHER USER PROFILES -----------------------

# ...


# -------------------- PRIVATE USER PROFILES ---------------------

# ...
