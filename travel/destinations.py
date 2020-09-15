from flask import Blueprint, render_template
from travel.models.comment import Comment
from datetime import datetime
from travel.models.destination import Destination
from travel.forms import DestinationForm

# create an instance of the destinations_blueprint
destinations_blueprint = Blueprint('destination', __name__, url_prefix='/destinations')
# any routes defined in destinations_blueprint will start with /destinations
# eg http://127.0.0.1:5000/destinations/

# route

@destinations_blueprint.route('/<id>')
# by setting the id parameter to id, we have to then provide a parameter in the route
# eg. http://127.0.0.1:5000/destinations/value or http://127.0.0.1:5000/destinations/1
def show(id):
    # comment_instance = Comment('Bob', 'The food here is pretty good!', datetime.now())
    destination_instance = database_get_destination_details()
    return render_template('destinations/show.html', destination = destination_instance)
    # return render_template('destinations/show.html', comment=comment_instance)
    # the key value pair of key=id will be found and replaced in destinations/show.html (value in url) to provide some server side rendering

@destinations_blueprint.route('/create')
def create():
    destination_form_instance = DestinationForm()
    return render_template('destinations/create.html', form=destination_form_instance)
 



# So we need to create an instance of destination
# Create some comments
# Create a list of comments
# We need to pass the comments through the instance of destination 

# dummy database call
def database_get_destination_details() -> Destination:
    comment_instance1 = Comment('Bob', 'The food here is pretty good!', datetime.now())
    comment_instance2 = Comment('John', 'This place is pretty nice!', datetime.now())
    comment_instance3 = Comment('Dude', 'There are many different restuarants here!', datetime.now())
    comment_instance4 = Comment('Brock', 'Hey, Ash!', datetime.now())

    mylist = list()
    mylist.append(comment_instance1)
    mylist.append(comment_instance2)
    mylist.append(comment_instance3)
    mylist.append(comment_instance4)

    destination_instance = Destination("Tivoli", "Small town of Rome!!", "https://www.planetware.com/wpimages/2019/04/italy-from-rome-to-tivoli-best-ways-to-get-there-rome-tivoli-by-train.jpg","EUR", mylist)

    return destination_instance