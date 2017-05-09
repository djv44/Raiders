import unittest

import raiders


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = raiders.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self): #tests homepage we are building
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'Raiders Website' in rv.data #looks for this phrase

if __name__ == '__main__':
    unittest.main() #unit test for main