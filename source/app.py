from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/chores/add', methods=['GET', 'POST'])
def add_chore():
    if request.method == 'POST':
        name = request.form['name']
        chore = Chore(name=name)
        db.session.add(chore)
        db.session.commit()
        theurl = url_for('show_chores')
        return redirect(theurl)
    else:
        return render_template('add_chore.html')
    
@app.route('/chores/delete/<int:chore_id>', methods=['POST'])
def delete_chore(chore_id):
    chore = Chore.query.get(chore_id)
    if chore:
        db.session.delete(chore)
        db.session.commit()
    return redirect(url_for('show_chores'))

def _initialize_fake_members(db):
    db.session.add(Member(name='Alice'))
    db.session.add(Member(name='Bob'))
    db.session.add(Member(name='Carol'))
    db.session.add(Member(name='Dan'))
    db.session.add(Member(name='Eve'))
    db.session.commit() 

# def _initialize_fake_chores(db):
#     db.session.add(Chore(name='Dishes'))
#     db.session.add(Chore(name='Vacuum'))
#     db.session.add(Chore(name='Clean Bathroom'))
#     db.session.add(Chore(name='Laundry'))
#     db.session.commit()

def _clear_members_table(db):
    db.session.query(Member).delete()
    db.session.commit()

def _clear_chores_table(db):
    db.session.query(Chore).delete()
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        _clear_members_table(db)
        _initialize_fake_members(db)
        # _clear_chores_table(db)
        # _initialize_fake_chores(db)
    webbrowser.open('http://localhost:5000')
    app.run()