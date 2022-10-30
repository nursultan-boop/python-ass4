from flask import Flask, render_template, redirect, url_for, request
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlalchemy
from flask import bootstrap
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap5(app)


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
db.init_app(app)

class User(db.Model):
    login = db.Column(db.String, primary_key=True)
    pswrd = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/signup', methods=["GET", "POST"])
def user_create():
    error=None
    success=None
    if request.method == "POST":
        user = User(
            login=request.form['username'],
            pswrd=request.form['password'],
        )
        db.session.add(user)
        db.session.commit()
        #return redirect(url_for("/home"))
        return render_template('signup.html',success="user succefully created")
    return render_template('signup.html')    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        logged_user = User.query.filter_by(login=request.form['username']).first()
        logged_pass = User.query.filter_by(pswrd=request.form['username']).first()
        if logged_user is None:
            return render_template('login.html', error='No such user is registered')
        elif logged_pass is None:
            return render_template('login.html', error='Incorrect password')
        else:
            return redirect(url_for('/home'))    
    return render_template('login.html',error=error)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
