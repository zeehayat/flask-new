from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
db=SQLAlchemy(app)
migrate=Migrate(app,db)
import routes, models
if __name__ == '__main__':
    app.run()
