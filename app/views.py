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
    business_source = get_sources('business')
    entertainment_source = get_sources('entertainment')
    technology_source = get_sources('technology')
    politics_source = get_sources('politics')

    
    title = 'Home-Welcome to the best News Article Website online'
    return render_template('index.html', title=title, sports = sports_source, business=business_source, entertainment=entertainment_source, technology=technology_source, politics=politics_source)