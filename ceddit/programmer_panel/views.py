from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint


# Blue prints
programmer_panel = Blueprint('programmer_panel', __name__)


@programmer_panel.route("/programmer_panel/signup", methods=['POST', 'GET'])
def programmer_panel_signup():

    return "programmer panel signup"
