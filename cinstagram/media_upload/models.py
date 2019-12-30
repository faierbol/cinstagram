from ..app import db
from datetime import datetime


# User Photos
# -------------
# This model holds the videos that the user uploads to its own profile.
class UserPhoto(db.Model):
    __tablename__ = "user_photos"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("cinstagram_user.id"))
    photo = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    caption = db.Column(db.String(2200), unique=False, nullable=True)
    comments = db.relationship("UserPhotoComment")
    likes = db.relationship("UserPhotoLike")
    bookmarks = db.relationship("UserPhotoBookmark")

    def __init__(self, user_id, photo, creation_date, caption):
        self.user_id = user_id
        self.photo = photo
        self.creation_date = datetime.now()
        self.caption = caption

    def __str__(self):
        return "Photo user: " + str(self.user_id) + "| Photo id: " + str(self.id)


# User Photo Comments
# -------------
# This model holds the comments belong to a single UserPhoto post
class UserPhotoComment(db.Model):
    __tablename__ = "user_photo_comments"
    id = db.Column(db.Integer, primary_key=True)
    commented_photo_id = db.Column(db.Integer, db.ForeignKey("user_photos.id"))
    comment_owner_id = db.Column(db.Integer, db.ForeignKey("cinstagram_user.id"))
    text = db.Column(db.String(2200), unique=False, nullable=True)
    comment_time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, commented_photo_id, comment_owner_id, text):
        self.commented_photo_id = commented_photo_id
        self.comment_owner_id = comment_owner_id
        self.text = text
        self.comment_time = datetime.now()

    def __str__(self):
        return (
            "Comment owner id: "
            + str(self.comment_owner_id)
            + "comment photo id "
            + str(self.commented_photo_id)
        )


# User Photo Likes
# -----------------
# This model holds the likes that belong toa single UserPhoto post
class UserPhotoLike(db.Model):
    __tablename__ = "user_photo_likes"
    id = db.Column(db.Integer, primary_key=True)
    liked_photo_id = db.Column(db.Integer, db.ForeignKey("user_photos.id"))
    like_owner_id = db.Column(db.Integer, db.ForeignKey("cinstagram_user.id"))

    def __init__(self, liked_photo_id, like_owner_id):
        self.liked_photo_id = liked_photo_id
        self.like_owner_id = like_owner_id

    def __str__(self):
        return (
            "Liker: "
            + str(self.like_owner_id)
            + " Liked Photo: "
            + str(self.liked_photo_id)
        )


# User Photo Bookmarks
# -----------------
# This model holds the bookmarks that belong toa single UserPhoto post
class UserPhotoBookmark(db.Model):
    __tablename__ = "user_photo_bookmarks"
    id = db.Column(db.Integer, primary_key=True)
    bookmarked_photo_id = db.Column(db.Integer, db.ForeignKey("user_photos.id"))
    bookmarker_id = db.Column(db.Integer, db.ForeignKey("cinstagram_user.id"))

    def __init__(self, bookmarked_photo_id, bookmarker_id):
        self.bookmarked_photo_id = bookmarked_photo_id
        self.bookmarker_id = bookmarker_id

    def __str__(self):
        return "Bookmarker: " + str(self.bookmarker_id)
