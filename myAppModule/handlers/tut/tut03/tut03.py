import os
import random
import string

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut03(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut03.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 03'
        }

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))
