from flask import Blueprint, session, redirect, url_for, render_template

from travel.forms import LoginForm

authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')



@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form_instance = LoginForm()
    if login_form_instance.validate_on_submit(): 
        # return the name of the blueprint and the name of controller
        return redirect(url_for('authentication.login'))
    return render_template('authentication/login', form=login_form_instance )

@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return ""

@authentication_blueprint.route('/logout')
def logout():
    session.clear()
    return ""