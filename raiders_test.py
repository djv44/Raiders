import unittest #imports the unit test

import raiders #imports the raiders.py file we created


class FlaskrTestCase(unittest.TestCase): #tests our functions

    def setUp(self):
        self.app = raiders.app.test_client() #raiders app we are making

    def tearDown(self): 
        pass

    def test_home_page(self): #tests homepage we are building
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'Raiders Website' in rv.data #looks for this phrase

    def test_main_page(self): #tests main page
        rv = self.app.get('/main')#fetchs main
        assert b'main' in rv.data #looks for this this phrase

    def test_topic_page(self):
        rv = self.app.get('/my-topic') #fetches this
        assert b'Raiders' in rv.data # looks for this

if __name__ == '__main__':
    unittest.main() #unit test for main