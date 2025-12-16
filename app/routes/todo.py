from flask import Blueprint, request, redirect, url_for, render_template,flash, session
from app import db
from app.models import Todo

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/', methods=['GET', 'POST'])
def home_page():
    if session.get('user_id'):
        if request.method == 'POST':
            title = request.form.get('title')
            status = request.form.get('status')
            user_id = session['user_id']
            if not title and title != '':
                flash('Title cannot be empty!', 'danger')
                return redirect(url_for('home_page'))
            todo = Todo(title=title, status=status, user_id=user_id)
            db.session.add(todo)
            db.session.commit()
            flash('Todo added successfully!', 'success')
            return redirect(url_for('todo.home_page'))
        todos = Todo.query.filter_by(user_id=session['user_id']).all()
        return render_template('home.html', todos=todos)
    return redirect(url_for('auth.loginUser'))