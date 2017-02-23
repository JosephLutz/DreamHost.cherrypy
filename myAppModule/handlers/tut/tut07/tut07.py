import os
import random
import string

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut07(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['TUT07string']

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['TUT07string'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['TUT07string'] = another_string

    def DELETE(self):
        cherrypy.session.pop('TUT07string', None)
