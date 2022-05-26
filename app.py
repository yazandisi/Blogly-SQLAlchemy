from crypt import methods
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Yaz'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_users():
    """Show list of users"""
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/<int:user_id>')
def show_user(user_id):
    """show details about a user"""  
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/new')
def add_user():
    """Add new user"""
    return render_template('new_user.html')

@app.route('/new', methods=["POST"])
def create_user():
    fname = request.form["fname"]
    lname = request.form["lname"]
    img_url = request.form["img"]

    new_user = User(first_name=fname, last_name=lname, img_url=img_url)

    db.session.add(new_user)
    db.session.commit()
    return redirect(f'/{new_user.id}')

@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    """Edit a user profile"""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)
    
@app.route('/edit_user/<int:user_id>', methods=["POST"])
def update_user(user_id):
    """update user"""
    fname = request.form["fname"]
    lname = request.form["lname"]
    img_url = request.form["img"]
    updated_user = User.query.get(user_id)
    updated_user.first_name = fname
    updated_user.last_name = lname
    updated_user.img_url = img_url

    db.session.add(updated_user)
    db.session.commit()
    return redirect(f'/{updated_user.id}')

@app.route('/delete_user/<int:user_id>', methods=["POST"])
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/')

