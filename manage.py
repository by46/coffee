import os
import os.path

from flask_assets import ManageAssets
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Shell
from pygments.formatters.html import HtmlFormatter

from app import assets
from app import create_app
from app import db
from app.models import Coffee
from app.models import Role
from app.models import User
from app.models import Vendor

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)


def init_pygments():
    path = 'app/static/css/pygments.css'
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open('app/static/css/pygments.css', 'wb') as writer:
        writer.write(HtmlFormatter(style='colorful').get_style_defs('.highlight'))


def make_shell_context():
    return dict(app=app,
                db=db,
                Vendor=Vendor,
                Coffee=Coffee,
                init_pygments=init_pygments)


@manager.command
def init():
    default_role = Role()
    default_role.name = 'default'
    db.session.add(default_role)

    admin_role = Role()
    admin_role.name = 'admin'
    db.session.add(admin_role)

    user = User()
    user.name = 'by46'
    user.password = '123456'
    user.roles.append(default_role)
    db.session.add(user)
    db.session.commit()


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('assets', ManageAssets(assets))

if __name__ == '__main__':
    manager.run()
