from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField


class RegistrationForm(FlaskForm):
    email = StringField("Email")
    username = StringField("Username")
    password = StringField("Password")

    submit = SubmitField("Sign up")
