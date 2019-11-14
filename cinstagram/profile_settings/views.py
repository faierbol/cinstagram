from flask import Flask, request, render_template, redirect, session, url_for
from flask import Blueprint

from ..app import db


# Blue prints
profile_settings = Blueprint("profile_settings", __name__)


@profile_settings.route("/profile_settings/change_password", methods=["POST", "GET"])
def profile_settings_change_password():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile_settings/change_password.html", data=data)


@profile_settings.route("/profile_settings/edit_profile", methods=["POST", "GET"])
def profile_settings_edit_profile():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile_settings/edit_profile.html", data=data)


@profile_settings.route("/profile_settings/email_sms", methods=["POST", "GET"])
def profile_settings_email_sms():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile_settings/email_sms.html", data=data)


@profile_settings.route("/profile_settings/privacy_security", methods=["POST", "GET"])
def profile_settings_privacy_security():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("profile_settings/privacy_security.html", data=data)
