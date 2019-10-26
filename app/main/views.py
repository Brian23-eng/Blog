from flask import render_template
from . import main
from ..request import get_quote

@main.route('/')
def index():
    
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | Blog post pages"
    quote = get_quote()
    
    return render_template("index.html", title = title, quote=quote)
    