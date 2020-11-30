from sqlalchemy.orm import joinedload

from sr.db import db
from sr.user.models import User


class Entry(db.Model):
    TITLE_LENGTH = 30
    CONTENT_LENGTH = 100

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(TITLE_LENGTH))
    content = db.Column(db.String(CONTENT_LENGTH))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='entries', lazy=True) 

    @classmethod
    def create(cls, title, content, user):
        entry = cls(title=title, content=content, user_id=user.id)
        db.session.add(entry)
        db.session.commit()
        return entry

    @classmethod
    def list(cls):
        return cls.query.options(joinedload(cls.user)).all()
