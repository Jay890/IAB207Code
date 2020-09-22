from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# constuctor for SQLAlchemy class
db = SQLAlchemy()
# note when we define a variable inside __init__.py file we have access to that variable everywhere
# E.g. import db object in other files and we have access to it... from travel import db
def create_app() -> Flask:
    print(__name__)
    app = Flask(__name__)

    app.secret_key = 'some_random_value'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    bootstrap = Bootstrap(app)
    db.init_app(app)

    from travel.views import main_blueprint
    from travel.destinations import destinations_blueprint
    from travel.authentication import authentication_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(destinations_blueprint)
    app.register_blueprint(authentication_blueprint)

    return app

 