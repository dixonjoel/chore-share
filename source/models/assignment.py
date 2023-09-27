from database import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=False)

    def __init__(self, member_id, schedule_id):
        self.member_id = member_id
        self.schedule_id = schedule_id