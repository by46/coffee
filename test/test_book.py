import unittest
from json import loads

from flask.wrappers import Response

from demo import create


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create('test')

    def tearDown(self):
        del self.app

    def test_book_get(self):
        with self.app.app_context():
            response = self.app.test_client().get("/demo/book/1")  # type:Response
            self.assertEqual(200, response.status_code)
            self.assertEqual({"ID": 1, "Title": "Python program"}, loads(response.data))
