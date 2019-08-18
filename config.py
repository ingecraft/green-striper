import os


class Config:
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    STRIPE_TEST_KEY = os.environ.get('STRIPE_TEST_KEY')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
    STRIPE_TEST_KEY = os.environ.get('STRIPE_TEST_KEY')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    STRIPE_TEST_KEY = os.environ.get('STRIPE_KEY')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
