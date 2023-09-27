from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db
from models.member import Member
from models.chore import Chore
from models.schedule import Schedule
from models.assignment import Assignment
import webbrowser

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/members')
def show_members():
    members = Member.query.all()
    return render_template('members.html', members=members)

@app.route('/chores')
def show_chores():
    chores = Chore.query.all()
    return render_template('chores.html', chores=chores)

def _initialize_fake_members(db):
    db.session.add(Member(name='Alice'))
    db.session.add(Member(name='Bob'))
    db.session.add(Member(name='Carol'))
    db.session.add(Member(name='Dan'))
    db.session.add(Member(name='Eve'))
    db.session.commit() 

def _clear_members_table(db):
    db.session.query(Member).delete()
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        _clear_members_table(db)
        _initialize_fake_members(db)
    webbrowser.open('http://localhost:5000')
    app.run()