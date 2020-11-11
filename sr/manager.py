from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app, db)
manager.add_command('db', MigrateCommand)

manager.run()
