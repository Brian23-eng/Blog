from app import create_app,db
from flask_script import Manager, Server



# Instances for creating the app
app = create_app('development')
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db)

@manager.command
def test():
    '''
    Run the unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__=='__main__':
    manager.run()