import cherrypy
from myAppModule.handlers import home

class Root(object):
    def __init__(self):
        self.home = home.Home()
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/home')

