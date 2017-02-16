import tempfile

import cherrypy
from cherrypy.process import plugins
from mako.lookup import TemplateLookup

class MakoTemplateLookup(plugins.SimplePlugin):
    
    def __init__(self, bus, base_dir=None, base_cache_dir=None, 
                 collection_size=50, encoding='utf-8'):
        super(MakoTemplateLookup, self).__init__(bus=bus)
        if not isinstance(base_dir, list):
            base_dir = [base_dir]
        self.base_cache_dir = base_cache_dir
        self.encoding = encoding
        self.collection_size = collection_size
        self.lookup = None
        self.template_paths = {
            None: base_dir,
        }
    
    def start(self):
        self.bus.log('Setting up Mako Template Lookup resources')
        self.lookup = {}
        for collection in self.template_paths:
            dirs = list(set(self.template_paths[None] + self.template_paths[collection]))
            self.lookup.setdefault(collection,
                                   TemplateLookup(
                                       directories=dirs,
                                       module_directory=self.base_cache_dir,
                                       input_encoding=self.encoding,
                                       output_encoding=self.encoding,
                                       collection_size=self.collection_size))
        self.bus.subscribe("Mako-Template-Lookup", self.get_template)
    
    def stop(self):
        self.bus.log('Freeing up Mako Template Lookup resources')
        self.bus.unsubscribe("Mako-Template-Lookup", self.get_template)
        self.lookup = None
    
    def get_template(self, templateName, template_collection=None):
        self.bus.log('lookup template {0} from collection {1}'.format(
            templateName, template_collection))
        return self.lookup[template_collection].get_template(templateName)
    
    def add_collection(self, collection, base_dir):
        if not isinstance(base_dir, list):
            base_dir = [base_dir]
        self.template_paths.setdefault(collection, base_dir)
        return self.template_paths[collection] == base_dir
