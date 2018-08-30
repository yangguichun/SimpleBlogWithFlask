import os, sys

class Config(object):
    SECRET_KEY = 'DJFKDJFK'

    #,postgresql+psycopg2://user:password@host:port/dbname
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(sys.path[0], 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:00@127.0.0.1:5432/helloflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
