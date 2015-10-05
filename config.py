from datetime import timedelta
import os


PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = 'iQfPvB6sZaNHqVFI5CJa9rM1xOEVHKIM0LwifT04yLsPlZhSSvaDuZXOgJFSpJVq'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'gW2ZmkEc5cIc2Uhn'
    SECURITY_TRACKABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    JWT_EXPIRATION_DELTA = timedelta(days=7)
    DATABASE = {
        'name': 'database.db',
        'engine': 'peewee.SqliteDatabase',
    }

    @staticmethod
    def init_app(app):
        pass


f = os.path.join(PROJECT_APP_PATH, "local_config.py")
if os.path.exists(f):
    exec(open(f, "rb").read())


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


configs = {
    'dev': DevConfig,
    'testing': TestConfig,
    'prod': ProdConfig,
    'default': Config
}
