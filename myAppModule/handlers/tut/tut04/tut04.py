import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut04(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut04.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 04'
        }
