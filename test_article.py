import unittest
from  app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('espn','ESPN','ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.','http://espn.go.com','sports','en','us')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))