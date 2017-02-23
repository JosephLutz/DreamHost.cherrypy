import os

# maximum cached templates per handler collection
MAKO_TEMPLATE_COLLECTION_SIZE = 5

MAKO_TEMPLATE_ENCODING = 'utf-8'

MAKO_TEMPLATE_CACHE = os.path.join(os.getcwd(), 'template.cache')
if not os.path.lexists(MAKO_TEMPLATE_CACHE):
    os.makedirs(MAKO_TEMPLATE_CACHE)

MAKO_TEMPLATE_PATHS = [os.path.abspath(
    os.path.join(__file__, '..', '..', 'common.templates')),
]

USE_CHERRYPY_HTTPS = True
USE_CHERRYPY_HTTPS = False

conf = {
}

global_conf = {
    'global': {
        'tools.encode.on': False,
        'tools.sessions.on': True,
        'tools.sessions.httponly': True,
        # secureheaders tool
        'tools.secureheaders.on': True,
        # rendertemplate tool
        'tools.rendertemplate.on': True,
        'tools.rendertemplate.debug': False,
    },
}
