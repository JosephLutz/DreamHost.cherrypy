import os

# import the apps configuration
from myAppModule import config

# Register the Mako tool
import myAppModule.tools.mako
# Register the Secure Header tool
import myAppModule.tools.secureheaders

# import handler after initializing all the tools
from tut10 import Tut10
from tut10 import handler_name

# add a new template collection to the template_lookup plug-in
from myAppModule.plugins.mako import template_collection
template_collection.add_collection(
    collection=handler_name,
    base_dir=os.path.join(os.getcwd(), os.path.dirname(__file__), 'templates'))

# set config options for /home handler
config.conf.update({
    '/tut/{0}'.format(handler_name): {
        'tools.rendertemplate.templateCollection': handler_name,
    },
})

# create a handler for /tut/tut10
tut10Handler = Tut10()
