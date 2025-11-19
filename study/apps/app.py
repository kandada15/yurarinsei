from flask import Flask
from flask_login import LoginManager # Flask-Loginをインポート
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config

# DBを他のアプリよりアクセス可能に
db = SQLAlchemy()
# CSRF対策
csrf = CSRFProtect()

login_manager = LoginManager()


def create_app():
  # Flaskアプリケーション
  app = Flask(__name__)
  app.config.from_object("apps.config.TestingConfig")
  db.init_app(app)
  csrf.init_app(app)
  migrate = Migrate(app, db)

  return app

  

