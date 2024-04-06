# Add any form classes for Flask-from here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Title', validators = [InputRequired()])
    description = TextAreaField('Description', validators = [InputRequired()])
    poster = FileField('Poster', validators = [FileField(), FileAllowed(['jpg', 'png'], 'Movie Posters Only!')])