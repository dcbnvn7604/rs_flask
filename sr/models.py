from flask_sqlalchemy import SQLAlchemy
import bcrypt


db = SQLAlchemy()

class UnauthorizedException(Exception):
	pass


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(128), unique=True)
	password = db.Column(db.String(89))

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
			raise UnauthorizedException()
		bpassword = user.password
		salt = bpassword[60:]
		hashed_password = bcrypt.hashpw(password.encode(), salt.encode())
		if hashed_password.decode() != bpassword[:60]:
			raise UnauthorizedException()
