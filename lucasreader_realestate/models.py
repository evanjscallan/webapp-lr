from lucasreader_realestate import db, login_manager
from datetime import datetime
from flask_login import UserMixin

#load user for login
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)


	def __repr__(self):
		return f"User('{self.username}','{self.email}')"

class Listing(db.Model):
	
	address = db.Column(db.String(100), unique=True, primary_key=True)
	price = db.Column(db.Integer, unique=True, nullable=False)


	def __repr__(self):
		return f"User('{self.address}','{self.price}')"
