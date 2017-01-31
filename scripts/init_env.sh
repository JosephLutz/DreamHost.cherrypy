#!/bin/bash
rm -rf $(pwd)/env
virtualenv $(pwd)/env
source $(pwd)/env/bin/activate
pip install \
  cherrypy \
  Mako \
  WTForms \
  MySQL-python \
  iptools \

