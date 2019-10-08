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
