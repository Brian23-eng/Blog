from flask import render_template
from . import main

@main.route('/')
def index():
    
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | Blog post pages"
    
    return render_template("index.html", title = title)
    