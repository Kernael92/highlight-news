from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_articles,search_source
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

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('search',source_name = search_source))
    else:
        return render_template('index.html', title=title, sports = sports_source, business=business_source, entertainment=entertainment_source, technology=technology_source, politics=politics_source)

@app.route('/article/<id>')
def article(id):
    '''
    View article page function that returns the articles details page and its data
    '''
    article = get_articles(id)
    title = f'NH | {id}'
    return render_template('article.html', title = title, article=article)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results.
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    return render_template('search.html',title=title,sources = searched_sources)


