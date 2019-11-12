from ..app import db


# HELP CENTRE POST
class HelpCentrePost(db.Model):
    __tablename__ = "help centre post"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, unique=False, nullable=False)
    header = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.String, unique=False, nullable=True)

    def __init__(self, category, header, content):
        pass

    def __str__(self):
        pass
