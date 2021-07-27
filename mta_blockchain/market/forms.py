import logging

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, BooleanField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User, Bet


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already Exist, Please try a diffrent username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already Exist, Please try a diffrent address')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if not user:
            logging.warning("user isn't  exists")
            raise ValidationError('Username doesn`t exist, Please try a different username or sign-up')

    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class SearchForm(FlaskForm):
    contractId = StringField(label='Contract Id:')
    sportType = StringField(label='Type of Sport:')
    date = DateTimeField(label='date of game:')
    search = SubmitField(label="Go!")


class CreateStepOne(FlaskForm):
    # contract info:
    public = BooleanField(label='Is the bet it public:')
    numberOfParticipants = IntegerField(label='Number of particpants:',validators=[DataRequired()])
    sportType = StringField(label='Type of Sport:')
    # toA = SubmitField(label='next')
# just for now, in the future get REST API:
#     # ----------------------------
    date = DateTimeField(label='Date of the game:')
    hour = StringField(label='Starting hour of the game:', validators=[DataRequired()])
    teamA = StringField(label='First team', validators=[DataRequired()])
    teamB = StringField(label='Second team', validators=[DataRequired()])
#     # ------------------------------------
#     ratioLabel = "what is the ration between {1} to {2}", CreateStepTwo.teamA, CreateStepTwo.teamB
    ratio = StringField(label='what is the ration between the teams?', validators=[DataRequired()])
    maxParticipants = IntegerField(label='max people:', validators=[DataRequired()])
    minParticipants = IntegerField(label='min people:', validators=[DataRequired()])
    minVal = IntegerField(label='Minimum cash in:', validators=[DataRequired()])
    maxVal = IntegerField(label='Maximum cash in:', validators=[DataRequired()])
    Create = SubmitField(label='Create a bet')

# class CreateStepTwo(CreateStepOne):
#     # just for now, in the future get REST API:
#     # ----------------------------
#     datetime = DateTimeField(label='Date of the game:')
#     hour = StringField(label='Starting hour of the game:', validators=[DataRequired()])
#     teamA = StringField(label='First team', validators=[DataRequired()])
#     teamB = StringField(label='Second team', validators=[DataRequired()])
#     # ------------------------------------
#     toB = SubmitField(label='next')
#
#
# class CreateStepThree(CreateStepTwo):
#     ratioLabel = "what is the ration between {1} to {2}", CreateStepTwo.teamA, CreateStepTwo.teamB
#     ratio = StringField(label=ratioLabel, validators=[DataRequired()])
#     maxParticipants = IntegerField(label='max people:', validators=[DataRequired()])
#     minParticipants = IntegerField(label='min people:', validators=[DataRequired()])
#     minVal = IntegerField(label='Minimum cash in:', validators=[DataRequired()])
#     maxVal = IntegerField(label='Maximum cash in:', validators=[DataRequired()])
#     Create = SubmitField(label='Create a bet')
