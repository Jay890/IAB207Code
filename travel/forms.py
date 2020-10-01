from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

# our destinationform is a FlaskForm (inheritance) is a type
class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired('Country is required')])
    image = StringField('Image', validators=[InputRequired('Image is required')])
    description = TextAreaField('Description', validators=[InputRequired('Description is required'), Length(min=10, max=300, message='Description is too short or too long')])
    currency = StringField('Currency', validators=[InputRequired('Currency is required')])
    submit = SubmitField('Create')


class LoginForm(FlaskForm):
    user_name = StringField('User name', validators=[InputRequired('User name is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])
    submit = SubmitField('Create')


class RegisterForm(FlaskForm):
    user_name = StringField('User name', validators=[InputRequired('User name is required')])
    email = StringField('Email', validators=[InputRequired('Email is required'), Email('Email is not valid')])
    password = PasswordField('Enter Password', validators=[InputRequired("Password is required")])
    confirm_password = PasswordField('Enter same password', validators=[InputRequired('Password is required'), EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Register')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired("Please add comment"), Length(min=5, max=100, message='Comment is too long or too short')])
    submit = SubmitField('Add Comment')