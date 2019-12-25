from flask import Flask, request, render_template, redirect, session, url_for
from flask import Blueprint

from .models import UserPhoto, UserPhotoComment, UserPhotoLike, UserPhotoBookmark
from ..authentication.models import User

from ..app import db


# Blue prints
media_upload = Blueprint("media_upload", __name__)


@media_upload.route("/media_upload", methods=["POST", "GET"])
def upload_page():
    """
        This page lets the user upload an image or vide and than lets it select
        a filter for it. And at the end the form promprts the user to add
        hashtags, captions, locations ... etc.
    """
    # Deleting any sessions regarding top-tier type of users
    session.pop("programmer_username", None)
    session.pop("programmer_logged_in", None)
    # admin user session pop
    # admin user session pop

    empty_credentials = False

    current_user = User.query.filter_by(
                        email=session["cinstagram_user_email"]
                   ).first()

    # Media Upload Validation
    if request.form.get("media_upload_submit_btn"):
        photo = request.files["upload_file"]
        caption = request.form["caption"]
        location = request.form["location"]

        # check if the file input is empty
        if bool(photo) is False:
            empty_credentials = True
        else:
            photo.save(photo.filename)
            new_photo = UserPhoto(current_user.id, photo.filename,
                                  caption, location)
            db.session.add(new_photo)
            db.session.commit()

    # dont forget to change the templates permission for no outsider visiblity
    data = {
        "empty_credentials": empty_credentials,
    }
    return render_template("media_upload/upload.html", data=data)
