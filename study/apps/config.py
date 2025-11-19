from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    SECRET_KEY = "2AZSMss3p5OPbcY2hb5J" # セキュリティのための秘密鍵
    WTF_CSRF_SECRET_KEY = "Auwzsy2Su5usgKN7KZs6f" # CSRF対策のための秘密鍵

class TestingConfig(BaseConfig):
    db_config = {
    'user' : "test_user",
    'password' : "test_password",
    'host' : "localhost",
    'db_name' : "test_db"
  }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**db_config),
    # 追跡機能を無効
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    db_config = {
    'user' : "test_user",
    'password' : "test_password",
    'host' : "localhost",
    'db_name' : "test_db"
  }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**db_config),
    # 追跡機能を無効
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# config変数にマッピングする
config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
}