from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..request import get_quote
from flask_login import current_user, login_required
from .. import db
from ..models import Post
from .forms import PostForm


@main.route('/')
def index():
    
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | Blog post pages"
    quote = get_quote()
    
    return render_template("index.html", title = title, quote=quote)
@main.route("/home")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        
        db.session.add(post)
        db.session.commit()
        
        flash('You post has been created!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('create_post.html', title='New Post | Welcome to BlogPost', form=form)

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id) 
    if post.author!= current_user:
        abort(403)
        
    form = PostForm()
    if form.validate_on_submit():
        
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.post', post_id=post.id))
    
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        
    return render_template('create_post.html', title='Update Post | Welcome to BlogPost', form=form)

@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author !=current_user:
        abort(403)
        
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))