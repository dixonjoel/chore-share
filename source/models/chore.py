from database import db

class Chore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    schedule = db.relationship('Schedule', backref='chore', lazy=True)

    def __init__(self, name):
        self.name = name
