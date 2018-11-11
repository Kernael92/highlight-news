import unittest
from  app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("",'Emilio Janus','Charlie Shrem Wins Latest Battle in Winklevoss Twins $32M Lawsuit' 'Charlie Shrem scored an important first goal in his ongoing legal match against the Winklevoss twins.','http://bitcoinist.com/charlie-shrem-wins-latest-battle-in-winklevoss-twins-32m-lawsuit/','https://bitcoinist.com/wp-content/uploads/2016/12/shremmm-e1482063859855.jpg','2018-11-09T14:00:55Z','Charlie Shrem scored an important first goal in his ongoing legal match against the Winklevoss twins.')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
if __name__ == '__main__':

    unittest.main()