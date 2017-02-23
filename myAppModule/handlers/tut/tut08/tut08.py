import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut08(object):

    def __init__(self):
        # /tut/tut08/generator
        from generator import strGenHandler
        self.generator = strGenHandler

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut08.index.html')
    def index(self):
        return {}
