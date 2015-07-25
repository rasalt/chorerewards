import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/chorerewards"
    DEBUG = True
    SECRET_KEY = os.environ.get("CHOREREWARDS_SECRET_KEY", "")