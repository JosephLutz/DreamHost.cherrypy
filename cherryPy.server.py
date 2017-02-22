#!/bin/env python

import os
import sys
import logging
from logging.handlers import RotatingFileHandler

class StdLogger(object):
    def __init__(self, logLevel):
        self.logger = logging.getLogger(__name__)
        self.logLevel = logLevel
    def setLevel(self, logLevel):
        self.logLevel = logLevel
    def write(self, buf):
        self.logger.log(self.logLevel, buf.rstrip())
hold_stdout = sys.stdout
hold_stderr = sys.stderr
sys.stdout = StdLogger(logging.INFO + 1)
sys.stderr = StdLogger(logging.ERROR + 1)

import cherrypy

from myAppModule import config
from myAppModule.handlers import rootHandler

DEBUG = False
_cp_log_to_stdout = True
_cp_logfmt = False

if __name__ == "__main__":
    cwd = os.getcwd()
    SUB_DOMAIN = os.path.basename(cwd)
    LOG_FILENAME = os.path.join(cwd, 'logs', 'passanger', 'passenger_wsgi.log')
    VIRTUALENV = os.path.join(cwd, 'env')
    logLevel = logging.INFO
    if DEBUG:
        logLevel = logging.NOTSET

    logger = logging.getLogger(__name__)
    logger.setLevel(1)
    if _cp_log_to_stdout:
        stdoutHandler = logging.StreamHandler(stream=hold_stdout)
        stdoutHandler.setLevel(logLevel)
        if _cp_logfmt:
            stdoutHandler.setFormatter(cherrypy._cplogging.logfmt)
        else:
            stdoutHandler.setFormatter(logging.Formatter('[%(levelname)s]  %(message)s'))
        logger.addHandler(stdoutHandler)
    logHandler = RotatingFileHandler(
        filename=LOG_FILENAME,
        mode='a',
        maxBytes=5000000,
        backupCount=5,
        encoding=None,
        delay=0)
    logHandler.setLevel(logLevel)
    if _cp_logfmt:
        logHandler.setFormatter(cherrypy._cplogging.logfmt)
    else:
        logHandler.setFormatter(logging.Formatter('[%(levelname)s]  %(message)s'))
    logger.addHandler(logHandler)
    logger.debug('RotatingFileHandler logging started')

    # verify we are in the virtual environment
    if sys.prefix != VIRTUALENV:
        logger.debug('Detected wrong sys.prefix: {path}'.format(path=sys.prefix))
        execfile(
            os.path.join(VIRTUALENV, 'bin', 'activate_this.py'),
            dict(__file__=os.path.join(VIRTUALENV, 'bin', 'activate_this.py')))

    # setup the standalone server config options
    config.conf.update({
            '/': {
                'tools.staticdir.root': os.path.join(cwd, 'public'),
            },
            '/favicon.ico': {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': os.path.join(cwd, 'public',
                    'favicon.ico'),
            },
            '/favicon.gif': {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': os.path.join(cwd, 'public',
                    'favicon.gif'),
            },
            '/images': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'images',
            },
            '/css': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'css',
            },
            '/js': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'js',
            },
            '/tut': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'tut',
            },
            '/pages.html': {
                'tools.staticfile.on': True,
                'tools.staticfile.filename': os.path.join(cwd, 'public',
                    'pages.html'),
            },
        })

    # update the global config
    cherrypy.config.update(config.global_conf)
    # get the application instance
    application = cherrypy.tree.mount(
        root=rootHandler,
        script_name='',
        config=config.conf)

    # configure a common logging system
    # do not log to StdOut/StdErr
    application.log.screen = False
    # Remove the default FileHandlers if present.
    application.log.error_file = ""
    application.log.access_file = ""
    # Add the handler for logging
    application.log.error_log.addHandler(logHandler)
    application.log.access_log.addHandler(logHandler)

    # run the standalone server and block
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()
