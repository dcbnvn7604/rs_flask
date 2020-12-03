import bcrypt

from sr.db import db
from sr.user.exceptions import UnauthenticatedException


user_permission = db.Table('user_permission',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id')),
    db.UniqueConstraint('user_id', 'permission_id')
)


class User(db.Model):
    USERNAME_LENGTH = 128
    PASSWORD_LENGTH = 89

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(89))
    permissions = db.relationship('Permission', secondary=user_permission, lazy='select')

    @classmethod
    def by_id(cls, id):
        return cls.query.filter_by(id=id).one()

    @classmethod
    def create(cls, username, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        user = cls(username=username, password=(hashed_password + salt))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()

        if user is None:
            raise UnauthenticatedException()
        bpassword = user.password
        salt = bpassword[60:]
        hashed_password = bcrypt.hashpw(password.encode(), salt.encode())
        if hashed_password.decode() != bpassword[:60]:
            raise UnauthenticatedException()
        return user


    @classmethod
    def exists(cls, username):
        return bool(cls.query.filter_by(username=username).first())

    def has_permissions(self, permission_names):
        return not bool(set(permission_names) - set([
            permission.name
            for permission in self.permissions
        ]))


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
