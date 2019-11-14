from flask import Flask, request, render_template, redirect, session, \
                  url_for, Blueprint

from ..app import db


# Blue prints
admin_panel = Blueprint("admin_panel", __name__)


@admin_panel.route("admin_panel/dashboard", methods=['POST', 'GET'])
def admin_panel_dashboard():

    return "This will be edited "
