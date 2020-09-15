from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length

# our destinationform is a FlaskForm (inheritance) is a type
class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired('Country is required')])
    image = StringField('Image', validators=[InputRequired('Image is required')])
    description = TextAreaField('Description', validators=[InputRequired('Description is required'), Length(min=10, max=300, message='Description is too short or too long')])
    currency = StringField('Currency', validators=[InputRequired('Currency is required')])
    submit = SubmitField('Create')


 