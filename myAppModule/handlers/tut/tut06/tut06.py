import os
import random
import string

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut06(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut06.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 06'
        }

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['TUT06string'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['TUT06string']
