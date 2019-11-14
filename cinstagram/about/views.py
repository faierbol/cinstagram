from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db

# Blue prints
about = Blueprint("about", __name__)


@about.route("/about", methods=["POST", "GET"])
def about_landing_page():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("about/about_index.html", data=data)


@about.route("/job/postings", methods=["POST", "GET"])
def about_job_postings():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("about/job_postings.html", data=data)


@about.route("/about/job/thisWillChangeForPostId", methods=["POST", "GET"])
def about_job_post():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("about/jobs_post_page.html", data=data)


@about.route("/about/legal", methods=["POST", "GET"])
def about_legal():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("about/legal.html", data=data)
