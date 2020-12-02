from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from app import create_app
from sr.db import db
from sr.user.models import User
from sr.entry.models import Entry


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app, db)
manager.add_command('db', MigrateCommand)

manager.run()
