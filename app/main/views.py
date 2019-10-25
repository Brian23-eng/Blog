from flask import render_template
from . import main



@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    
    '''
    title = "Welcome | BlogPost"
    
    return render_template("index.html", title=title)