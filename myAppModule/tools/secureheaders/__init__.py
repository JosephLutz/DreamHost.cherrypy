import cherrypy

from secureheaders import SecureHeaders

# Set some header security options
#   Set XFrame options
#   Enable XSS Protection
#   Set the Content Security Policy
cherrypy.tools.secureheaders = SecureHeaders(priority=60)
