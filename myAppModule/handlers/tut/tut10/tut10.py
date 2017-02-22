import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut10(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut10.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 10'
        }
