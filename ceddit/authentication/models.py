from ..app import db


# User Model
# ----------------
# This model is the basic user (average joe) of the site. It will be constantly
# imporved in each fucntionality added to the site that the suer can use
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)
