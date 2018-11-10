class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_SOURCES_BASE_URL = 'http://newsapi.org/v2/sources?category={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True