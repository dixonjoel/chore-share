from database import db

_DAILY_SCHEDULE = 'daily'
_WEEKLY_SCHEDULE = 'weekly'
_MONTHLY_SCHEDULE = 'monthly'

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frequency = db.Column(db.String(10), nullable=False)
    chore_id = db.Column(db.Integer, db.ForeignKey('chore.id'), nullable=False)
    assignments = db.relationship('Assignment', backref='schedule', lazy=True)