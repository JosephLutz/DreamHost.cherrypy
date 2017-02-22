import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Tut02(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='tut02.index.html')
    def index(self):
        return {
            'msg': 'Tutorial 02'
        }
