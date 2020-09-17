from flask import Blueprint, render_template, request, session


# define a blueprint
main_blueprint = Blueprint('main', __name__)

# define a route
# wsgi server matches the route as the MITM from the incoming request, sends it to the controller
@main_blueprint.route('/')
# define the controller to be the index controller
def index_controller():
    # if 'email' in session: #if the email is in session aka user has logged in
    #     return f"<h1>Hello World {session['email']}</h1>"
    # else:
    #     return "<h1>hello world anonymous</h1>" #view 
    return render_template('index.html')

# Now we need to register the blueprint and tell the application that using this Blueprint (__init__.py)

# @main_blueprint.route('/new')
# def new_controller():
#     str = "<h2>Well hello there!</h2>"
#     return str

# @main_blueprint.route('/login', methods=['GET', 'POST'])
# def login_controller():
#     # print(request)
#     # print(request.values.get('email')) #so we can get values grabbing their id. E.g. this is the id set for the email in the login.html
#     # print(request.values.get('pwd'))
#     session['email'] = request.values.get('email')
#     return render_template('login.html')

 
# @main_blueprint.route('/logout')
# def logout_controller():
#     #  session.pop('email', None)
#     session.clear()
#     return "Session is cleared you have been logged out safely."
# # now register the blueprint in __init__.py 
     