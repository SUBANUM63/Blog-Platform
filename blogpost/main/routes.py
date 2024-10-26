#!/usr/bin/python3
"""
main

This module defines the main Blueprint for the blog post application, handling home and about pages.

Functions:
    home(): Renders the home page, paginating posts.
    about(): Renders the about page.
"""

from flask import render_template, request, Blueprint
from blogpost.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """Renders the home page, paginating posts.

        Args:
            page (int, optional): The page number for pagination. Defaults to 1.

        Returns:
            str: The rendered home page template with paginated posts.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    """Renders the about page.

       Returns:
           str: The rendered about page template.
    """
    return render_template('about.html', title='About')
