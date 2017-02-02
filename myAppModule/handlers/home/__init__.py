import os

from myAppModule import config
from home import Home

config.MAKO_TEMPLATE_PATHS.append(os.path.join(
    os.getcwd(),
    os.path.dirname(__file__),
    'templates'))

