from datetime import timedelta


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


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


configs = {
    'dev': DevConfig,
    'testing': TestConfig,
    'prod': Config,
    'default': Config
}
