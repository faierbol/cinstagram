from ..app import db
from ..media_upload.models import UserPhoto, UserPhotoComment, UserPhotoLike
from ..media_upload.models import UserPhotoBookmark


# User Model
# ----------------
# This model is the basic user (average joe) of the site. It will be constantly
# imporved in each fucntionality added to the site that the suer can use
class User(db.Model):
    __tablename__ = "cinstagram_user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    full_name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    # Relationships
    photos = db.relationship("UserPhoto")
    comments = db.relationship("UserPhotoComment")
    likes = db.relationship("UserPhotoLike")
    bookmarks = db.relationship("UserPhotoBookmark")

    def __init__(self, email, full_name, username, password):
        self.email = email
        self.full_name = full_name
        self.username = username
        self.password = password

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)
