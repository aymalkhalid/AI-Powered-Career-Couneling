# Dundar init file
#"""Files named __init__.py are used to mark directories on disk as Python package directories"""
from flask import Flask
from .commands import create_tables
from .models import User
from .extensions import db, login_manager
from .routes.auth import auth
from .routes.main import main
#by default the config_file is settings.py(Which we create for the app configuration settings like database etc)
def create_app(config_file='settings.py'):
#Creating a application factory function (create_app), Instantiating Flask.
    app =Flask(__name__)
#Specifying config file.
    app.config.from_pyfile(config_file)
# Registering DataBase.
    db.init_app(app)
# Registering Login Manager.
    login_manager.init_app(app) 
# Registering BluePrint(Architecture) of Main,and Authentication flask python files with Flask(AICC) App
    app.register_blueprint(main)
    app.register_blueprint(auth)
# Terminaal Command to create tables
    app.cli.add_command(create_tables)
#Flask Returing Main App
    return app

#-------------------------------------------------
#-------------------------------------------------
# Flask Login  Manager For the Login View. 
login_manager.login_view = 'auth.login'

#Flask Login User_loader or Request_loader.
@login_manager.user_loader
def load_user(user_id):
#Loding Users By thier Id.
    return User.query.get(user_id)


#.flaskenv file is used to specify the development environment, Flask python pacakge folder
#FLASK_ENV=development
#FLASK_APP=flask_qa