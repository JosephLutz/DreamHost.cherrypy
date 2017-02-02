import mako
import mako.lookup

import config

def render(template, context=None):
    render_context = {
        }
    if context is not None:
        render_context.update(context)
    makoTemplateLookup = mako.lookup.TemplateLookup(
        directories=config.MAKO_TEMPLATE_PATHS,
        module_directory=config.config.MAKO_TEMPLATE_CACHE,
        collection_size=500)
    try:
        mako_template = makoTemplateLookup.get_template(template)
        return mako_template.render_unicode().encode('utf-8', 'replace')
    except:
        return mako.exceptions.html_error_template().render()

