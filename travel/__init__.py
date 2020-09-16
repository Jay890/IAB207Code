from flask import Flask
from travel.views import main_blueprint
from travel.destinations import destinations_blueprint
from flask_bootstrap import Bootstrap
from travel.authentication import authentication_blueprint

def create_app() -> Flask:
    print(__name__)
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(destinations_blueprint)
    app.register_blueprint(authentication_blueprint)
    app.secret_key = 'some_random_value'
    bootstrap = Bootstrap(app)
    return app

 