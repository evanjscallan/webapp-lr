from flask import render_template, url_for, redirect, request, flash
from lucasreader_realestate import app, db, bcrypt, Mail, Message, mail
from lucasreader_realestate.forms import RegistrationForm, LoginForm, ListingForm
from lucasreader_realestate.models import User, Listing
from flask_login import login_user, current_user, logout_user, login_required
from functools import wraps
import sqlite3 as sql
import os





#DUMMY DATA - REMOVE 'listings' data later
"""listings = [
	{
		'address': '1234 Fake Street',
		'price': '10000000'
	},
	{
		'address': '1234 Noob Street',
		'price': '99999'
	}

]"""

@app.route('/')
@app.route('/index')
def index():
	listings = Listing.query.all()
	return render_template('index.html', listings=listings)


@app.route('/', methods=['POST','GET'])
def contact_card():
	user_contact = request.form['user-input-name']
	user_email = request.form['user-input-email']
	user_phone = request.form['user-input-phone']
	user_message = request.form['user-input-message']
	msg = Message(f"Let's make moves. New client message from {user_contact}.", sender='evanjscallan@gmail.com', body=f"Sent from:{user_contact}\nEmail:{user_email}\nPhone:{user_phone}\nMessage:{user_message}", recipients=['evanjscallan@gmail.com'])
	mail.send(msg)
	return redirect(url_for('index'))

@app.route('/lr_register',  methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('admin'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your Account has been created.')
		return redirect(url_for('login'))
	return render_template('lr_register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		#connect user with bcrypt, forms
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			#now redirect to home page
			return redirect(url_for('admin'))
		else:
			flash('Login Unsuccessful. Please check email and password.')
	return render_template('login.html', title='Login', form=form)



@app.route('/admin', methods=['GET', 'POST'])
#decorator to limit access to logged in users
@login_required
def admin():
	form = ListingForm()
	listings = Listing.query.all()
	if form.validate_on_submit():
		listing = Listing(address=form.address.data, price=form.price.data)
		db.session.add(listing)
		db.session.commit()
		flash('Property Uploaded.')
	return render_template('admin.html', form=form, listings=listings)

#dummy page for house listing test
@app.route('/dummy', methods=['GET', 'POST'])
def dummy():
	return render_template('dummypage.html', title='dummy')


#logout function
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route("/listings")
def listings():
	listings = Listing.query.all()
	return render_template('listings.html', listings=listings)




