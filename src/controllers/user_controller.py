# controllers/User_controller.py
from flask import request, session, redirect, url_for, render_template, flash
from config.database import db
from models.all_models import User
from werkzeug.security import generate_password_hash, check_password_hash

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return render_template('register.html')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')

    return render_template('register.html')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return render_template('index.html',username=user.username)
        
        flash('Invalid username or password')
    
    return render_template('login.html')

def logout():
    session.pop('user_id', None)
    return render_template('login.html')
