from ..app import db


# Programmer Model

# This model contains the neccessary data regarding the Programmer Model which
# is a super-user that overseas every action and every data that is happening
# on the site.
class Programmer(db.Model):
    __tablename__ = "programmer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    key = db.Column(db.String(20))

    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)


# Admin Model
# ----------------
# The admin model of the application contains the admin-user description. The
# admin is like the programmer a super-user however it has a lot less accsess
# or influence over the site. It mostly deals with the content of the site.
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    key = db.Column(db.String(20))

    def __init__(self, username, password, key):
        self.username = username
        self.password = password
        self.key = key

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)
