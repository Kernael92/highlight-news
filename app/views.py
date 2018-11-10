from flask import render_template
from app import app
from .request import get_sources
#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''


    #Getting sports source
    sports_source = get_sources('sports')

    
    title = 'Home-Welcome to the best News Article Website online'
    return render_template('index.html', title=title, sports = sports_source)