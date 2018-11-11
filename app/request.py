from app import app
import urllib.request,json
from .models import source
from .models import article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting the source base url
sources_url = app.config['NEWS_SOURCES_BASE_URL']
# Getting the article base_url
articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response  to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    
    return source_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url= source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language= source_item.get('language')

        source_object = Source(id,name,description,url,category,country,language)
        source_results.append(source_object)

    return source_results
def get_articles(id):
    '''
    Function that gets the json response to our url
    '''
    get_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['article']:
            article_results_list = get_articles_response['article']
            article_results = process_articles(article_results_list)
    
    return article_results

def process_articles(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
		
        if urlToImage:
            article_object = Article(id,author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)	
    return  article_results
def search_source(source_name):
    search_source_url = 'http://newsapi.org/v2/search/everything?language=en&sources?&apiKey={}&query{}'.format(api_key,source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['articles']:
            search_source_list = search_source_response['articles']
            search_source_results = process_results(search_source_list)


    return search_source_results
    

    




