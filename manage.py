from flask_script import Manager
from bootstrap import create_app


app = create_app()

manager = Manager(app)

@manager.command
def seed():
    from seeds import seed_data
    seed_data()

@manager.command
def hello():
     print('test')

if __name__ == "__main__":
    manager.run()