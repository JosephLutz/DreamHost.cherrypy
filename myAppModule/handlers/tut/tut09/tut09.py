import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut09(object):

    def __init__(self):
        # /tut/tut09/generator
        from generator import strGenHandler
        self.generator = strGenHandler

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut09.index.html')
    def index(self):
        return {}
