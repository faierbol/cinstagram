from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from ..app import db

# Blue prints
about = Blueprint('about', __name__)


@about.route("/about", methods=['POST', 'GET'])
def about_landing_page():
    '''
        ...
    '''
    # Deleting any sessions regarding top-tier type of users

    

    data = {

    }
    return render_template("authentication/signup.html", data=data)
