from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=25)])
    password = StringField("Password",
                           validators=[DataRequired(), Length(min=2, max=25)])

    submit = SubmitField("Sign up")
