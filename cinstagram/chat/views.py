from flask import Flask, request, render_template, redirect, session, url_for, Blueprint

from ..app import db


# Blue prints
chat = Blueprint("chat", __name__)


@chat.route("/chat", methods=["POST", "GET"])
def chat_index():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("chat/index_page.html", data=data)


@chat.route("/chat/new_chat", methods=["POST", "GET"])
def new_chat():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("chat/new_chat.html", data=data)


@chat.route("/chat/singChatIdWillBeHere", methods=["POST", "GET"])
def single_chat():
    """ ...  """
    # Deleting any sessions regarding top-tier type of users

    data = {}
    return render_template("chat/signle_chat.html", data=data)
