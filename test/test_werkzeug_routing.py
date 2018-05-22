from werkzeug.routing import Map
from werkzeug.routing import Rule
from werkzeug.routing import Subdomain

import unittest


class MapTestCase(unittest.TestCase):
    def test_map_build(self):
        m = Map([
            Rule("/", endpoint='static/index'),
            Rule('/about', endpoint='static/about'),
            Rule('/help', endpoint='static/help'),
            Subdomain('kb', [
                Rule('/', endpoint='kb/index'),
                Rule('/browse', endpoint='kb/browse'),
                Rule('/browse/<int:id>', endpoint='kb/browse'),
                Rule('/browse/<int:id>/<int:page>', endpoint='kb/browse')
            ])
        ], default_subdomain='www')
        c = m.bind('newegg.com')
        url = c.build('kb/browse', dict(id=12))
        self.assertEqual('http://kb.newegg.com/browse/12', url)

        self.assertEqual('/about', c.build('static/about'))
        self.assertEqual('http://www.newegg.com/about', c.build('static/about', force_external=True))

        print(c.match('/about'))

        c = m.bind('newegg.com', '/', subdomain='kb')
        print(c.build('kb/browse', dict(id=21)))
        print(c.match('/browse'))
