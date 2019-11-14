#
#    Title: Cinstagram
#
#    Desc: This project is just a instagram clone. The reason I am not putting
#          a MIT license on the source code is because this is just an educati-
#          -onal project for me and I want it to stay it that way.
#
#    Author: Demir Antay (@demirantay) -- demir99antay@gmail.com
#

import psycopg2  # needed for database configs

from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# the app is defined above url blueprint imports in order
# to avoid circular imports
app = Flask(__name__)

app.config["static_folder"] = "./static"
app.config["template_folder"] = "./templates"
app.secret_key = "changeThisInProduction"
app.debug = True

# Database configs
postgresql_URI = "postgresql://demir@localhost:5432/cinstagram"
app.config["SQLALCHEMY_DATABASE_URI"] = postgresql_URI

# SQLAlchemy and Migrate(alembic) configs
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Url blueprint imports
from .programmer_panel.views import programmer_panel
from .admin_panel.views import admin_panel
from .help_centre.views import help_centre
from .about.views import about
from .api_web.views import api_web
from .authentication.views import authentication
from .profile_settings.views import profile_settings
from .media_upload.views import media_upload
from .profile.views import profile
from .chat.views import chat
from .home.views import home
from .search.views import search
from .explore.views import explore


# Programmer Panel
# ----------------
# This is where the neccessary views regarding the programmer panel app of the
# site is included, the programmer_panel is a dashboard and a control panel
# for the programmers(super-users) of the site, yes the "admin" is a superuser
# too but admin mostly deals with the content of the site, where the programm-
# -ers deal with site-realibity, graphs of the bandwith usage, ... etc.
app.register_blueprint(programmer_panel)


# Admin Panel
# -----------------
# This is the admin panel where the staff (admins) of the company oversee the
# content that is being entered to the site, polices it, limits it ... etc.
# The difference between programmer panel is that admins are more oriented
# towards user entries and not sysadmin control
app.register_blueprint(admin_panel)


# Help Centre
# -----------------
# This is the app where the staff (admin) of the company updates the certain
# information regarding the usage of the site, what are new or how to use them
app.register_blueprint(help_centre)


# About
# -----------------
# This app shows the history, who they are, goals of the company ... etc. The
# most important functionality in this app is the job postings and the jobs
app.register_blueprint(about)


# API Website
# -----------------
# This app is just the GUI web interface for the usage of the API of the site.
# It does not contain any code that creates the API code. It is just a read-
# -only site
app.register_blueprint(api_web)


# Authentication
# ----------------
# These blueprints contains the user authentication system for the end users
# of the site such as the "average joe" and not admin, top tier user ... etc.
app.register_blueprint(authentication)


# Profile Settings
# ----------------
# This is the app where the user of the site can change their accoutns Settings
# such as changing the password, allowing email and sms messages ... etc.
app.register_blueprint(profile_settings)

# Media Upload
# ----------------
# This is kinda the core of the application where the users upload pictures
# or videos. Self note for future: I will need to update the image recognition
# so that the site will not be NSFW
app.register_blueprint(media_upload)

# Profile
# ----------------
# This app contains the landing page of the user, followers, likers, tagged,
# bookmarked photos single post pages ... etc. Everything that is related to
# a user with private, public viewing options ... etc.
app.register_blueprint(profile)

# Chat
# ----------------
# This is the chat application where the users can chat with each other. It is
# pretty self explanatory
app.register_blueprint(chat)

# Home
# ----------------
# This is the home page which is just actually a single contianer that includes
# user specific feeds, alerts, notifications ... etc.
app.register_blueprint(home)

# Search Pages
# ----------------
# search pages include three search indexes 1 - account searches, 2 - hashtag
# searches and finally 3 - location searches
app.register_blueprint(search)

# Explore
# ----------------
# Explore page is a simple container just like the home page it consists of new
# and unseen and suggested account pictures videos to the current user
app.register_blueprint(explore)


@app.route("/")
def temporary_control_panel():
    """
    This view will be removed once I am done with the first version of the
    app which can support itself without any crutches
    """

    # HELP CENTRE
    # -------------

    # ABOUT APP
    # -------------

    # Authentication
    # ---------------

    # Profile Settings
    # ----------------

    # Photo & Video Upload
    # ----------------

    # Profile
    # ----------------

    # Chat
    # ----------------

    # Home
    # ----------------

    # Search Indexes
    # ----------------

    # Explore
    # ----------------

    data = {}
    return render_template("temp_control_panel.html", data=data)
