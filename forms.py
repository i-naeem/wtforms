from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired


class RegistrationForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=25)])
    password = StringField("Password",
                           validators=[DataRequired(), Length(min=2, max=25)])

    agreement = BooleanField("I agree to terms and condition",
                             validators=[InputRequired()])

    submit = SubmitField("Sign up")
