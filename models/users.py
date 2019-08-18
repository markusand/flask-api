from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from db import db


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.String(32), primary_key=True)
	username = db.Column(db.String(32), unique=True, nullable=False)
	password = db.Column(db.String(128), unique=False, nullable=False)
	email = db.Column(db.String(128), unique=True, nullable=False)
	name = db.Column(db.String(15), nullable=False)
	surname = db.Column(db.String(20), nullable=False)
	gender = db.Column(db.Boolean)
	region = db.Column(db.String(20))
	birthday = db.Column(db.DateTime)
	avatar = db.Column(db.String)
	role = db.Column(db.String(10))
	ts = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	def set_password(self, password):
		self.password = generate_password_hash(password, 'sha256')

	def check_password(self, password):
		return check_password_hash(self.password, password)
