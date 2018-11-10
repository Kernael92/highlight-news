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
        self.assertEquals(self.new_source_id,'espn')
        self.assertEquals(self.new_source_name,'ESPN')
        self.assertEquals(self.new_source_description,'ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.')
        self.assertEquals(self.new_source_url,'http://espn.go.com')
        self.assertEquals(self.new_source_country,'us')
        self.assertEquals(self.new_source_language,'en')
if __name__ == '__main__':
    unittest.main()
