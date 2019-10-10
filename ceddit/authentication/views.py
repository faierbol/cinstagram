from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from .models import User
from ..app import db

# Blue prints
authentication = Blueprint('authentication', __name__)


@authentication.route("/authentication/signup", methods=['POST', 'GET'])
def authentication_signup():
    '''
        Signup system that is built just for the end-user's (e.g. customers)
    '''
    # Deleting any sessions regarding top-tier type of users
    session.pop("programmer_username", None)
    session.pop('programmer_logged_in', None)
    # add admin session removals ...

    # Signup Form Processing 


    data = {

    }
    return render_template("authentication/signup.html", data=data)
