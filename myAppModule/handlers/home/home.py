import cherrypy
from myAppModule import tools

class Home(object):
    @cherrypy.expose
    def index(self):
        return tools.render('home.html', {})

