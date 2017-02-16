import cherrypy

handler_name = ''


class Root(object):

    def __init__(self):
        # /home
        from myAppModule.handlers.home import homeHandler
        self.home = homeHandler
        # /contact
        from myAppModule.handlers.contact import contactHandler
        self.contact = contactHandler
    
    @cherrypy.expose
    def index(self):
        from myAppModule.handlers.home import handler_name
        raise cherrypy.HTTPRedirect('/{0}'.format(handler_name))
