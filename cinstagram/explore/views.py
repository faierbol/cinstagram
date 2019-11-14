from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from ..app import db


# Blue prints
explore = Blueprint("explore", __name__)


@explore.route("/explore", methods=['POST', 'GET'])
def explore():
    ''' ...  '''
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("explore/explore.html", data=data)
