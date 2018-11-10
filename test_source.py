import unittest
from  app.models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('espn','ESPN','ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.','http://espn.go.com','sports','en','us')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))



    def test_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'espn')
        self.assertEqual(self.new_source.name,'ESPN')
        self.assertEqual(self.new_source.description,'ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.')
        self.assertEqual(self.new_source.url,'http://espn.go.com')
        self.assertEqual(self.new_source.country,'us')
        self.assertEqual(self.new_source.language,'en')
if __name__ == '__main__':
    unittest.main()
