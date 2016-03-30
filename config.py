import os

DEBUG = False
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True