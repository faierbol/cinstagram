from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db


# Blue prints
media_upload = Blueprint("media_upload", __name__)


@media_upload.route("/media_upload", methods=["POST", "GET"])
def media_upload():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("media_upload/upload.html", data=data)
