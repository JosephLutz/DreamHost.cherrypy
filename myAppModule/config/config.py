import os

MAKO_TEMPLATE_CACHE = os.path.join(os.getcwd(), 'template.cache')
MAKO_TEMPLATE_PATHS = []

if not os.path.lexists(MAKO_TEMPLATE_CACHE):
    os.makedirs(MAKO_TEMPLATE_CACHE)

conf = {
}

