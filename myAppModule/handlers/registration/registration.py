import os

import cherrypy
from wtforms import Form
from wtforms import BooleanField
from wtforms import StringField
from wtforms import validators

from myAppModule.utils.simplemultidict import SimpleMultiDict

handler_name = os.path.basename(os.path.dirname(__file__))

class Registration(object):

    @cherrypy.expose
    @cherrypy.tools.rendertemplate(templateName='registration.index.html')
    def index(self, **kwargs):
        pageData = {}
        # body    = cherrypy.request.body.read()
        # rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        pageData['form'] = RegistrationForm(SimpleMultiDict(kwargs))
        if not (cherrypy.request.method == 'POST' and pageData['form'].validate()):
            # display the form
            return pageData
        # process the form
        if pageData['form'].save():
            # redirect after successful save
            raise cherrypy.HTTPRedirect('/{0}'.format(handler_name))
        return pageData

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    
    def save(self):
        # saving the user data
        pass
        # save the username
        # save the email
        return True
