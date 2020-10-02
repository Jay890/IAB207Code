from flask import Blueprint, render_template, url_for, redirect
from travel.models.comment import Comment
from datetime import datetime
from travel.models.destination import Destination
from travel.forms import DestinationForm, CommentForm
from travel import db
from werkzeug import secure_filename
import os
from flask_login import login_required, current_user

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
    # destination_instance = database_get_destination_details()
    destination = Destination.query.filter_by(id=id).first()
    # destination.description = 'This is additional content in memory'
    comment_form_instance = CommentForm()
    return render_template('destinations/show.html', destination=destination, form=comment_form_instance)
    # return render_template('destinations/show.html', comment=comment_instance)
    # the key value pair of key=id will be found and replaced in destinations/show.html (value in url) to provide
    # some server side rendering


@destinations_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = DestinationForm()
    if form.validate_on_submit():

        # save the image to the 'static/image' folder
        target_folder = 'static/image'

        file = form.image.data

        BASE_PATH = os.path.dirname(__file__)
        full_path = os.path.join(BASE_PATH, target_folder, secure_filename(file.filename))
        file.save(full_path)

        relative_path = '/' + target_folder + '/' + secure_filename(file.filename)

    # destination_form_instance = DestinationForm()
    # if destination_form_instance.validate_on_submit():

        # write the data to the database/ save the destination to the database
        destination = Destination()

        destination.name = form.name.data
        destination.currency = form.currency.data
        # destination.image_url = destination_form_instance.image.data
        destination.image_url = relative_path
        destination.description = form.description.data

        db.session.add(destination)
        db.session.commit()

        print('form is not valid')
        return redirect(url_for('destination.create'))
    else:
        return render_template('destinations/create.html', form=form)


@destinations_blueprint.route('/<id>/comment', methods=['POST'])
@login_required
def comment(id):
    comment_form_instance = CommentForm()
    if comment_form_instance.validate_on_submit():
        destination = Destination.query.filter_by(id=id).first()
        # note current_user is not a method its static - we don't actually invoke the method call
        user = current_user
        # write operation to database - first create an instance of comment
        comment = Comment()

        comment.text = comment_form_instance.comment.data
        comment.destination = destination
        comment.user = user
        # comment.destination_id = id

        db.session.add(comment)
        db.session.commit()

        print(f'Comment form is valid. The comment was {comment_form_instance.comment.data}')
    else:
        print("Comment form invalid")
    return redirect(url_for('destination.show', id=id))

# So we need to create an instance of destination
# Create some comments
# Create a list of comments
# We need to pass the comments through the instance of destination 

# dummy database call
# def database_get_destination_details() -> Destination:
#     comment_instance1 = Comment('Bob', 'The food here is pretty good!', datetime.now())
#     comment_instance2 = Comment('John', 'This place is pretty nice!', datetime.now())
#     comment_instance3 = Comment('Dude', 'There are many different restuarants here!', datetime.now())
#     comment_instance4 = Comment('Brock', 'Hey, Ash!', datetime.now())
#
#     mylist = list()
#     mylist.append(comment_instance1)
#     mylist.append(comment_instance2)
#     mylist.append(comment_instance3)
#     mylist.append(comment_instance4)
#
#     destination_instance = Destination("Tivoli", "Small town of Rome!!", "https://www.planetware.com/wpimages/2019/04/italy-from-rome-to-tivoli-best-ways-to-get-there-rome-tivoli-by-train.jpg","EUR", mylist)
#
#     return destination_instance
