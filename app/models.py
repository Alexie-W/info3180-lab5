# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class movies(db.Model):
    __tablename__ = 'Movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    poster = db.Column(db.String(128), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return f"MovieProfile(id={self.id}, title='{self.title}', description={self.description}, poster={self.poster}, created_at={self.created_at})"