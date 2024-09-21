from flask import Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User_auth
from apps.crud.forms import UserForm

auth = Blueprint(
    "auth", __name__,
    template_folder = "templates",
    static_folder = "static"    
)

@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/users/new", methods = ["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User_auth(   
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.users"))
    return render_template("auth/create.html", form = form)

@auth.route('/users')
def users():
    users = User_auth.query.all()
    return render_template('auth/index.html', users = users)

@auth.route('/users/<user_id>',methods=["GET","POST"])
def edit_user(user_id):
    form = UserForm()
    user = User_auth.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data    
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.users'))
    return render_template('auth/edit.html',user=user, form=form)

@auth.route('/user/<user_id>/delete', methods = ["POST"])
def delete_user(user_id):
    user = User_auth.query.filter_by(id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.users'))