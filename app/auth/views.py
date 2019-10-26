from flask import render_template, redirect, url_for, flash, request
from ..models import User
from . import auth
from flask_login import login_user, login_required, logout_user, current_user
from ..import db
from .forms import RegistrationForm, LoginForm, ResetPassword, NewPassword
import os


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user.login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        
        flash('Invalid username or password')
        
    title = "Login | BlogPost Pages"
    return render_template("auth/login.html", login_form=login_form, title=title)