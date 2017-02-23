import cherrypy

# import the apps configuration
from myAppModule import config






# import handler after initializing all the tools
from generator import StringGeneratorWebService
from generator import handler_name







# set config options for /home handler
config.conf.update({
    '/tut/tut09/{0}'.format(handler_name): {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        # response_headers tool
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        # secureheaders tool
        'tools.secureheaders.on': False,
        # rendertemplate tool
        'tools.rendertemplate.on': False,
    },
})

# create a handler for /tut/tut09/generator
strGenHandler = StringGeneratorWebService()
