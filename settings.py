import os

SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
#Its annoying when SQLALCHEMy is Running so turning it off.
SQLALCHEMY_TRACK_MODIFICATIONS = False