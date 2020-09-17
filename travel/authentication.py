from flask import Blueprint, session, redirect, url_for, render_template

from travel.forms import LoginForm
from travel.forms import RegisterForm

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
        return redirect(url_for('authentication.login'))
    return render_template('authentication/register.html', form = register_form_instance )

@authentication_blueprint.route('/logout')
def logout():
    session.clear()
    return render_template('authentication/logout.html')