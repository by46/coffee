from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Shell

from app import create_app
from app import db
from app.models import Coffee
from app.models import Vendor

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app,
                db=db,
                Vendor=Vendor,
                Coffee=Coffee)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
