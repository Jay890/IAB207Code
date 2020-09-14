from flask import Blueprint, render_template
from travel.models.comment import Comment
from datetime import datetime

# create an instance of the destinations_blueprint
destinations_blueprint = Blueprint('destination', __name__, url_prefix='/destinations')
# any routes defined in destinations_blueprint will start with /destinations
# eg http://127.0.0.1:5000/destinations/

# route

@destinations_blueprint.route('/<id>')
# by setting the id parameter to id, we have to then provide a parameter in the route
# eg. http://127.0.0.1:5000/destinations/value or http://127.0.0.1:5000/destinations/1
def show(id):
    comment_instance = Comment('Bob', 'The food here is pretty good!', datetime.now())
    return render_template('destinations/show.html', comment=comment_instance)
    # the key value pair of key=id will be found and replaced in destinations/show.html (value in url) to provide some server side rendering

 