from flask import Blueprint, render_template


# define a blueprint
main_blueprint = Blueprint('main', __name__)

# define a route
# wsgi server matches the route as the MITM from the incoming request, sends it to the controller
@main_blueprint.route('/')
# define the controller to be the index controller
def index_controller():
    return "<h1>hello world</h1>" #view 

# Now we need to register the blueprint and tell the application that using this Blueprint (__init__.py)

@main_blueprint.route('/new')
def new_controller():
    str = "<h2>Well hello there!</h2>"
    return str

@main_blueprint.route('/login')
def login_controller():
    return render_template('login.html')