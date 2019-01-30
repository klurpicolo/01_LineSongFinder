from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Eamil', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    summit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Eamil', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    summit = SubmitField('Login')


class SearchForm(FlaskForm):
    query_text = StringField('query_text', validators=[DataRequired('Please Input Something!!!')])
    summit = SubmitField('Search')
