from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from lucasreader_realestate.models import User, Listing


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=100)])
	confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
	submit = SubmitField('Register Account')

	#custom validation function
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user: 
			raise ValidationError('That username is taken. Please choose a different one.')
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user: 
			raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class ListingForm(FlaskForm):
	address = StringField('Address', validators=[DataRequired()])
	price = IntegerField('Price', validators=[DataRequired()])
	submit = SubmitField('Upload')






	"""def validate_address(self, address):
		user = User.query.filter_by(address=address.data).first()
		if address: 
			raise ValidationError('That address is taken. Please choose a different one.')
	def validate_price(self, price):
		user = User.query.filter_by(price=price.data).first()
		if user: 
			raise ValidationError('That price is taken. Please choose a different one.')
			#DONT USE THIS, TESTING PURPOSE ONLY"""

