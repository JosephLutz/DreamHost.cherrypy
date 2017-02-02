import config
from myAppModule.handlers import root

import cherrypy

application = cherrypy.Application(
    root.Root(),
    script_name='',
    config=config.conf)

