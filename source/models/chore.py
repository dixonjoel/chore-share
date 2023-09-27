from database import db

class Chore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    schedule = db.relationship('Schedule', backref='chore', lazy=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id