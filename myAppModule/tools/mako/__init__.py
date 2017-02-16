# Register the Mako lookup plugin
import myAppModule.plugins.mako

import cherrypy
from template_render import MakoTemplateRender

# Register the Mako template rendering tool
cherrypy.tools.rendertemplate = MakoTemplateRender(priority=10)
