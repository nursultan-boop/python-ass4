import os
from flask import Flask, render_template, request, url_for, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlalchemy
# create the Flask app
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
db.init_app(app)

class nft(db.Model):
    adrs = db.Column(db.String, primary_key=True)
    meta_data = db.Column(db.String, nullable=False)

class User(db.Model):
    login = db.Column(db.String, primary_key=True)
    pswrd = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()
@app.route('/test')
def test():
    return render_template('test_login.html')

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        returnValue=""
        address = request.form['address']
        nft_obj = nft.query.filter_by(adrs=address).first()
        if(nft_obj is None):
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)
            headers = {
                "accept": "application/json",
                "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z"
            }
            returnValue = requests.get(url, headers=headers).text            
            user = nft(
            adrs=address,
            meta_data=returnValue,
            )
            db.session.add(user)
            db.session.commit()
        else:   
            return render_template('meta_data.html', meta_data=nft_obj.meta_data)

    return render_template('nft_styles.html')
    
    # otherwise handle the GET request   

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        logged_user = User.query.filter_by(login=request.form['username']).first()
        logged_pass = User.query.filter_by(pswrd=request.form['username']).first()
        if logged_user is None:
            return render_template('sign_in_up.html', error='No such user is registered')
        elif logged_pass is None:
            return render_template('sign_in_up.html', error='Incorrect password')
        else:
            return redirect('/')    
    return render_template('sign_in_up.html',login="yes", signup=None)

@app.route('/signup', methods=["GET", "POST"])
def user_create():
    error=None
    if request.method == "POST":
        logged_user = User.query.filter_by(login=request.form['username']).first()
        if logged_user is None:
            user = User(
                login=request.form['username'],
                pswrd=request.form['password'],
            )
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        else:
            return render_template('sign_in_up.html',error='this user already exists, go to login instead')
    return render_template('sign_in_up.html', signup="yes", login=None)    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


