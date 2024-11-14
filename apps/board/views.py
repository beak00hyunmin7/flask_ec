from flask import Blueprint, render_template, redirect, url_for
from app import db
from apps.board.models import Boards
from apps.board.forms import BoardForm
from flask_login import login_required

#blueprint로 curd 앱을 생성
board = Blueprint(
    "board",
    __name__,
    template_folder = "templates",
    static_folder = "static"
)   

@board.route("/")
def index():
    board = Boards.query.all()
    return render_template("board/index.html", board = board)

# @board.route('/board/new', methods = ["GET", "POST"])
# @login_required
# def create_user():
#     form = BoardForm()
#     if form.validate_on_submit():
#         user = User(
#             id = form.id.data,
#             title = form.title.data,
#             content = form.content.data,
#             author_id = form.author_id.data,
#             view = form.view.data,
#             create_at = form.create_at.data,
#             update_at = form.update_at.data,
#             author = form.author.data,         
#         )
#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for("board.users"))
#     return render_template("board/create.html", form = form)

# @crud.route('/users')
# def users():
#     users = User.query.all()
#     return render_template('crud/index.html', users = users)

# @crud.route('/users/<user_id>',methods=["GET","POST"])
# @login_required 
# def edit_user(user_id):
#     form = UserForm()
#     user = User.query.filter_by(id=user_id).first()
#     if form.validate_on_submit():
#         user.username = form.username.data
#         user.email = form.email.data
#         user.password = form.password.data
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('crud.users'))
#     return render_template('crud/edit.html',user=user, form=form)

# @crud.route('/user/<user_id>/delete', methods = ["POST"])
# def delete_user(user_id):
#     user = User.query.filter_by(id = user_id).first()
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for('crud.users'))

