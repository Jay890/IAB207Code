from flask import Blueprint, session, redirect, url_for, render_template, flash
from travel.models.user import User
from travel.forms import LoginForm
from travel.forms import RegisterForm
from travel import db
from werkzeug.security import generate_password_hash, check_password_hash

authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')



@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form_instance = LoginForm()
    if login_form_instance.validate_on_submit(): 
        session['email'] = login_form_instance.user_name.data
        # return the name of the blueprint and the name of controller
        return redirect(url_for('authentication.login'))
    return render_template('authentication/login.html', form=login_form_instance )

@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register(): 
    register_form_instance = RegisterForm()
    if register_form_instance.validate_on_submit():
        # TODO

        #Check to see if the username is unique as in the validator we have not done that only 'required'
        existing_user = User.query.filter_by(name=register_form_instance.user_name.data).first()

        if existing_user:
            flash('User already exists')
            return redirect(url_for('authentication.register'))

        # if user does not exist
        # create the user
        # map the fields (mapping)
        user = User()
        user.email = register_form_instance.email.data
        user.name = register_form_instance.user_name.data
        user.password_hash = generate_password_hash(register_form_instance.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('authentication.login'))
    return render_template('authentication/register.html', form = register_form_instance )

@authentication_blueprint.route('/logout')
def logout():
    session.clear()
    return render_template('authentication/logout.html')