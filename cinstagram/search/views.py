from flask import Flask, request, render_template, redirect, session, url_for
from flask import Blueprint

from ..app import db


# Blue prints
search = Blueprint("search", __name__)


@search.route("/search/account_search", methods=['POST', 'GET'])
def account_search():
    ''' ...  '''
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("search/account_search.html", data=data)


@search.route("/search/hashtag_search", methods=['POST', 'GET'])
def hashtag_search():
    ''' ...  '''
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("search/hashtag_search.html", data=data)


@search.route("/search/location_search", methods=['POST', 'GET'])
def location_search():
    ''' ...  '''
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("search/location_search.html", data=data)
