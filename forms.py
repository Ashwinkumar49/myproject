from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=18)])
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password' ,validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')