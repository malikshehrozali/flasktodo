from flask import Blueprint, request, redirect, url_for, render_template, session, flash
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def loginUser():
    if session.get('user_id'):
        flash('You are already logged in!', 'danger')
        return redirect(url_for('todo.home_page'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username and username != '':
            flash('Username cannot be empty!', 'danger')
            return redirect(url_for('login'))
            
        if not password and password != '':
            flash('Password cannot be empty!', 'danger')
            return redirect(url_for('login'))
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('todo.home_page'))
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def registerUser():
    if session.get('user_id'):
        flash('You are already logged in!', 'danger')
        return redirect(url_for('todo.home_page'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username and username != '':
            flash('Username cannot be empty!', 'danger')
            return redirect(url_for('login'))
            
        if not password and password != '':
            flash('Password cannot be empty!', 'danger')
            return redirect(url_for('login'))
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('todo.home_page'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logoutUser():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('todo.home_page'))