import cherrypy

class SecureHeaders(cherrypy.Tool):

    def __init__(self, priority=60):
        super(SecureHeaders, self).__init__(
            point='before_finalize', callable=self._add_headers,
            name='secureheaders', priority=priority)
    
    def _add_headers(self):
        cherrypy.log('adding secure headers',
            context='TOOLS.SECUREHEADERS.SECUREHEADERS')
        headers = cherrypy.response.headers
        headers['X-Frame-Options'] = 'DENY'
        headers['X-XSS-Protection'] = '1; mode=block'
        headers['Content-Security-Policy'] = "default-src='self'"
