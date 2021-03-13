# click is what the command line does
import click
#with_appcontext any command we run can use the configuration in the app 
from flask.cli import with_appcontext
from .extensions import db
#import all the database models(table Name) to create them
from .models import User
from .models import Question

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()