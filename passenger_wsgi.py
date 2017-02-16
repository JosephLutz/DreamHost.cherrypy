import os
import sys
import logging
from logging.handlers import RotatingFileHandler

DEBUG = False

cwd = os.getcwd()
SUB_DOMAIN = os.path.basename(cwd)
LOG_FILENAME = os.path.join(cwd, 'logs', 'passanger', 'passenger_wsgi.log')
VIRTUALENV = os.path.join(cwd, 'env')
logLevel = logging.INFO
if DEBUG:
    logLevel = logging.NOTSET

logger = logging.getLogger(__name__)
logger.setLevel(1)
logHandler = RotatingFileHandler(
    filename=LOG_FILENAME,
    mode='a',
    maxBytes=5000000,
    backupCount=5,
    encoding=None,
    delay=0)
logHandler.setLevel(logLevel)
logHandler.setFormatter(logging.Formatter('[%(levelname)s]  %(message)s'))
logger.addHandler(logHandler)
logger.debug('RotatingFileHandler logging started')

# verify we are in the virtual environment
if sys.prefix != VIRTUALENV:
    logger.debug('Detected wrong sys.prefix: {path}'.format(path=sys.prefix))
    execfile(
        os.path.join(VIRTUALENV, 'bin', 'activate_this.py'),
        dict(__file__=os.path.join(VIRTUALENV, 'bin', 'activate_this.py')))

out  = ['Running python:']
out += ['  executable: "{exe}"']
out += ['  version: "{ver}"']
out += ['  prefix: "{prfx}"']
logger.debug('\n'.join(out).format(
    exe=sys.executable,
    ver=sys.version,
    prfx=sys.prefix))

class StdLogger(object):
    def __init__(self, logLevel):
        self.logger = logging.getLogger(__name__)
        self.logLevel = logLevel
    def setLevel(self, logLevel):
        self.logLevel = logLevel
    def write(self, buf):
        for line in buf.rstrip():
            self.logger.log(self.logLevel, line)

sys.stdout = StdLogger(logging.INFO)
sys.stderr = StdLogger(logging.ERROR)

# import web application
sys.path.append(cwd)
try:
    import myAppModule
except ImportError as err:
    logger.exception('Error importing module: "{e}"'.format(e=err))

# start the application
def application(environ, start_response):
    results = []
    logger.debug('Application called')
    if DEBUG:
        out = ['environ:']
        for k in environ:
            out.append('  {k!r}: {val!r}'.format(k=k, val=environ[k]))
        logger.debug('\n'.join(out))
    try:
        results = myAppModule.application(environ, start_response)
        logger.debug('Application executed successfully')
    except Exception, inst:
        logger.exception('Error: {0}'.format(type(inst)))
    logger.debug('Application call done')
    if DEBUG:
        logHandler.flush()
    return results

logger.debug('Application initilization compleated')

