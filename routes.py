from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', data=users)

@main.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Create a new User object
        new_user = User(name=name, email=email, password=password)
        
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        
        # Redirect to the home page
        return redirect(url_for('main.index'))
    
    return render_template('adduser.html')

@main.route('/edituser/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edituser.html', user=user)

@main.route('/deleteuser/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('main.index'))
