from database import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    chores = db.relationship('Chore', backref='member', lazy=True)

    def __init__(self, name):
        self.name = name