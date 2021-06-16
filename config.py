import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRE_URI') or 'postgresql://user:password@localhost:5432/flask_test_api'
    SALT = os.environ.get('SALT') or 'my_sJHLHLHKLаваыпuper_s!alt_#4$4344'
