import os

_HERE = os.path.dirname(__file__)

class Config:

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
