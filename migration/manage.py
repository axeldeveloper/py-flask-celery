from flask_script import Manager
from app import app

manager = Manager(app)

import os
from flask_script import Manager
from flask_migrate import Migrate
from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

# migrate = Migrate(app, db)
migrate = Migrate(app, db, command='migrate')

#db = SQLAlchemy()
#migrate = Migrate()

def create_app():
    #app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    return app





if __name__ == '__main__':
    manager.run()