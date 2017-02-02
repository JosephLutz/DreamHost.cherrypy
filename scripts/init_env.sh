#!/bin/bash
rm -rf $(pwd)/env
virtualenv $(pwd)/env
source $(pwd)/env/bin/activate
pip install -Iv \
  cherrypy==3.8.0 \
  Mako==1.0.4 \
  WTForms==2.1 \
  MySQL-python \
  iptools==0.6.1 \

