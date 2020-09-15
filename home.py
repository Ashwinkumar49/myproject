#import pyrebase
from flask import Flask, render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm
from firebase_admin import firestore, credentials, initialize_app


app = Flask(__name__)
app.config['SECRET_KEY'] = '1223334444555550'

config = {
    "apiKey": "AIzaSyA6NFMVF62loNByiQzT642AVDCj0yVz6TA",
    "authDomain": "myproject-7d8b4.firebaseapp.com",
    "databaseURL": "https://myproject-7d8b4.firebaseio.com",
    "projectId": "myproject-7d8b4",
    "storageBucket": "myproject-7d8b4.appspot.com",
    "messagingSenderId": "437888766667",
    "appId": "1:437888766667:web:58d362fa20fc531d1e814e",
    "measurementId": "G-VV57XPJV9X"
    }

cred = credentials.Certificate("service.json")
default_app = initialize_app(cred)


db = firestore.client()
#firebase = pyrebase.initialize_app(config)

#auth=firebase.auth()

@app.route("/",methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password.data
        reg=db.collection('register').document(username)
        doc={'username':username, 'email':email, 'password':password}
        #auth.create_user_with_email_and_password(email,password)
        reg.set(doc)


        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        #if auth.sign_in_with_email_and_password(email,password):
         #   flash('Login successfull', 'success')
         #   return redirect(url_for('home'))
        #else:
          #  flash('Login failed', 'warning')
    return render_template('login.html', form=form)

@app.route("/test", methods=['GET','POST'])
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)