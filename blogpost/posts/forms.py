#!/usr/bin/python3
"""
This module defines the forms used in the BlogPost application.

Classes:
    - PostForm: A form for creating and updating post entries.

Imports:
    - FlaskForm: Base form class from Flask-WTF.
    - StringField: A field for input of string values.
    - SubmitField: A field for form submission.
    - TextAreaField: A field for input of multi-line text.
    - DataRequired: A validator ensuring data is provided.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """
    PostForm

    This class represents a Flask-WTF form for blog posting.

    Attributes:
        title (wtforms.StringField): A StringField representing the title of the post.
            Required by DataRequired validator.
        content (wtforms.TextAreaField): A TextAreaField representing the contents of the post.
            Required by DataRequired validator.
        submit (wtforms.SubmitField): A SubmitField for submitting the form.
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')