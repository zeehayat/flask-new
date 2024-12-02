import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:azeemi47@localhost/flask_movie_recommendation"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'sandbox.smtp.mailtrap.io'
    MAIL_SERVER =  'sandbox.smtp.mailtrap.io'
    #MAIL_PORT = os.environ.get('MAIL_PORT') or 25
    MAIL_PORT = 25
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = 1
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'bdc8b0cefd6655'
    MAIL_USERNAME = 'bdc8b0cefd6655'
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'c459339e76a988'
    MAIL_PASSWORD = 'c459339e76a988'
    #ADMINS = os.environ.get('ADMINS') or 'admin@gmail.com'
    ADMINS = 'admin@gmail.com'
    UPLOAD_FOLDER = 'uploads'


