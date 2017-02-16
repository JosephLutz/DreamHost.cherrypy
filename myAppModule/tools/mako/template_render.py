import cherrypy
from mako import exceptions

class MakoTemplateRender(cherrypy.Tool):
    
    def __init__(self, priority=10):
        super(MakoTemplateRender, self).__init__(
            point='before_finalize', callable=self._render,
            name='rendertemplate', priority=priority)

    def _render(self, templateName=None, templateCollection=None, debug=False):
        if cherrypy.response.status > 399:
            return
        # retrieve the data returned by the handler
        data = cherrypy.response.body or {}
        if not isinstance(data, dict):
            return
        cherrypy.log(
            'Rendering template: {0} from collection: {1} [debug={2}])'.format(
                templateName, templateCollection, debug),
            context='TOOLS.MAKO.TEMPLATE_RENDER')
        # get the template used to render
        template = cherrypy.engine.publish(
            'Mako-Template-Lookup', templateName, templateCollection).pop()
        if not template:
            return
        # dump the template using data dictionary
        if debug:
            try:
                cherrypy.response.body = template.render(**data)
            except:
                cherrypy.response.body = exceptions.html_error_template().render()
        else:
            cherrypy.response.body = template.render(**data)
