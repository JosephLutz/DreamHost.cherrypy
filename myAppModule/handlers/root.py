import cherrypy

class Root(object):

    def __init__(self):
        # /home
        from myAppModule.handlers.home import homeHandler
        self.home = homeHandler
        # /contact
        from myAppModule.handlers.contact import contactHandler
        self.contact = contactHandler
        # /tut
        from myAppModule.handlers.tut import tutHandler
        self.tut = tutHandler
        # /registration
        from myAppModule.handlers.registration import registrationHandler
        self.registration = registrationHandler

    @cherrypy.expose
    def index(self):
        from myAppModule.handlers.home import handler_name as home_handler_name
        raise cherrypy.HTTPRedirect('/{0}'.format(home_handler_name))
