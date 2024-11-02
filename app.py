from flask import Flask, Blueprint
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = "acct.signup"
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)
    
    #앱의 config 설정
    app.config.from_object(config[config_key])
    # SQLAlchemy와 앱을 연계
    db.init_app(app)
    # Migrate와 앱을 연계
    Migrate(app, db)
    #csrf와 앱을 연계
    csrf.init_app(app)

    #login_manager 앱을 연결
    login_manager.init_app(app)

    #crud 앱 연결
    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix = "/crud")

    #auth 앱 연결
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix = "/auth")

    #login 앱 연결
    from apps.acct import views as acct_views
    app.register_blueprint(acct_views.acct, url_prefix = "/acct")

    #login 앱 연결
    from apps.main import views as main_views
    app.register_blueprint(main_views.main, url_prefix = "/main")
    
    return app