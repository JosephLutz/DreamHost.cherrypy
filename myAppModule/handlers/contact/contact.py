import os

import cherrypy

handler_name = os.path.basename(os.path.dirname(__file__))

class Contact(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='contact.index.html')
    def index(self):
        return {
            'msg': 'This is our contact info...'
        }
