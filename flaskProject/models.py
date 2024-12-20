from datetime import datetime
from hashlib import md5

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager

from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(128), nullable=False)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    website=db.Column(db.String(140))
    picture=db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def avatar(self, size):
        digest=md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest,size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Netflix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(120))
    title=db.Column(db.String(120))
    director=db.Column(db.String(120))
    cast=db.Column(db.String(120))
    country=db.Column(db.String(200))
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
    release_year=db.Column(db.String(200))
    rating=db.Column(db.Integer)
    duration=db.Column(db.Integer)
    listed_in=db.Column(db.String(200))
    description=db.Column(db.Text)
    timestamp=db.Column(db.DateTime, default=datetime.utcnow)

class UserWatchPreferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    netflix_id = db.Column(db.Integer, db.ForeignKey('netflix.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<UserWatchPreferences {}>'.format(self.netflix_id)

