from flask import Flask
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

mail = Mail()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oJ0Re6Al7CaNeb1W'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#create instances
login_manager = LoginManager(app)
login_manager.login_view = 'login'


'''
IMPORT FROM ENVIRONMENT VARIABLE - TESTING
email_admin = os.environ.get('email_admin')
''' 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =  '*******'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



from lucasreader_realestate import routes


