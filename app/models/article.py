class Article:
    '''
    Article class to define Source objects
    '''
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.author = author
        self.title= title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt