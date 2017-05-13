from flask import render_template, flash, redirect,Flask
from app import app,User,db
#import app

app = Flask(__name__)

@app.route('/')
def add_user():
    user1 = User('ethan', 'ethan@example.com')
    user2 = User('admin', 'admin@example.com')
    user3 = User('guest', 'guest@example.com')
    user4 = User('joe', 'joe@example.com')
    user5 = User('michael', 'michael@example.com')
 
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
 
    db.session.commit()
 
    return "<p>add succssfully!"

if __name__=='__main__':
    app.run(debug = True)

