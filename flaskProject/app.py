from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import SMTPHandler
from config import Config
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
db=SQLAlchemy(app)
migrate=Migrate(app,db)
import routes, models, errors
if __name__ == '__main__':
    app.run()
if app.config['MAIL_SERVER']:
    auth=None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure=None
        if app.config['MAIL_USE_TLS']:
            secure = None
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),fromaddr='noreply'+app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='SUCC',credentials=auth,secure=secure)


        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
