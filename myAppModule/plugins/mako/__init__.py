import cherrypy
from template_lookup import MakoTemplateLookup
from myAppModule import config

template_collection = MakoTemplateLookup(
    bus=cherrypy.engine,
    base_dir=config.MAKO_TEMPLATE_PATHS,
    base_cache_dir=config.config.MAKO_TEMPLATE_CACHE, 
    collection_size=config.config.MAKO_TEMPLATE_COLLECTION_SIZE,
    encoding=config.config.MAKO_TEMPLATE_ENCODING
    )
template_collection.subscribe()
