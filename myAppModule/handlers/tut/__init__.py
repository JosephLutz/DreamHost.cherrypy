

# import the apps configuration
from myAppModule import config






# import handler after initializing all the tools
from tut import Tut
from tut import handler_name







# set config options for /home handler
config.conf.update({
    '/{0}'.format(handler_name): {
        # secureheaders tool
        'tools.secureheaders.on': False,
        # rendertemplate tool
        'tools.rendertemplate.on': False,
    },
})

# create a handler for /tut/tut06
tutHandler = Tut()
