#!/usr/bin/python
"""
This module defines the routes for handling post-related actions in the BlogPost application.

Imports:
    - render_template: Renders a template with the given context.
    - url_for: Generates URLs to the given endpoint.
    - flash: Displays a message to the user.
    - redirect: Redirects the user to a different endpoint.
    - request: Handles request data in routes.
    - abort: Aborts a request with a given status code.
    - Blueprint: Registers a group of routes.
    - current_user: Gets the currently logged-in user.
    - login_required: Ensures a route is accessed only by logged-in users.
    - db: Database instance from the BlogPost application.
    - Post: Post model from the BlogPost application.
    - PostForm: Form for creating and updating post-entries.
"""

from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blogpost import db
from blogpost.models import Post
from blogpost.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """Renders the post creation form, processes submission, creates a new
    Post object, and redirects to the home page.

    Returns:
        str: The rendered post creation template with form.
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    """Retrieves a Post object by ID, renders its details.

    Args:
        post_id (int): The ID of the Post object to retrieve.

    Returns:
        str: The rendered post details template.
    """
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """Retrieves a Post object, renders the update form, processes submission,
    updates the object, and redirects to the post details page.

    Args:
        post_id (int): The ID of the Post object to update.

    Returns:
        str: The rendered post update template with form.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """Retrieves a Post object, deletes it, and redirects to the home page.

    Args:
        post_id (int): The ID of the Post object to delete.

    Returns:
        str: Redirection to the home page.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
