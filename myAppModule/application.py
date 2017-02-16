import sys
import atexit

import cherrypy

import config
from myAppModule.handlers import rootHandler

cherrypy.config.update(config.global_conf)

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

application = cherrypy.Application(
    root=rootHandler,
    script_name='',
    config=config.conf)

#application = cherrypy.tree.mount(root, "/", config=cp_config)



#from cherrypy import wsgiserver
#
#def my_crazy_app(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type','text/plain')]
#    start_response(status, response_headers)
#    return ['Hello world!']
#
#server = wsgiserver.CherryPyWSGIServer(
#            ('0.0.0.0', 8070), my_crazy_app,
#            server_name='www.cherrypy.example')
#server.start()
