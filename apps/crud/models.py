from datetime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash


#db.Model을 상속한 클래스 작성
class User(db.Model):
    __tablename__ = "users"
    #컬럼명 정의
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, index = True)
    email = db.Column(db.String, index = True)
    # userid = db.Column(db.String, index = True)
    password = db.Column(db.String)
    create_at = db.Column(db.DateTime, default = datetime.now)  
    update_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

class User_auth(db.Model):
    __tablename__ = "users_auth"
    #컬럼명 정의
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, index = True)
    email = db.Column(db.String, index = True)
    # userid = db.Column(db.String, index = True)
    password = db.Column(db.String)
    create_at = db.Column(db.DateTime, default = datetime.now)  
    update_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)