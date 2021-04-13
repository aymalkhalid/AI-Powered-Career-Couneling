from flask import Blueprint, render_template ,request,redirect,url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user
from flask_qa.extensions import db
from flask_qa.models import User
from flask import flash
auth=Blueprint('auth',__name__)


@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        unhashed_password=request.form['password']
        user = User(name=name,email=email,unhashed_password=unhashed_password,admin=False,expert=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        
        user=User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Could not Login, Please check and Try again')
        
        else:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 
