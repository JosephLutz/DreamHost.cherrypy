import os

# import the apps configuration
from myAppModule import config



# Register the Secure Header tool
import myAppModule.tools.secureheaders

# import handler after initializing all the tools
from root import Root















# create the root handler object
rootHandler = Root()
