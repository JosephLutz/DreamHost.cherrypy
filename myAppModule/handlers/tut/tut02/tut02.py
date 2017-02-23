import os
import random
import string

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut02(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut02.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 02'
        }

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))
