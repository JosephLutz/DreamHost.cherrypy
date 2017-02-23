#!/bin/bash
rm -rf $(pwd)/env
virtualenv $(pwd)/env
source $(pwd)/env/bin/activate
pip install -Iv \
  cherrypy==3.8.0 \
  Mako==1.0.4 \
  WTForms==2.1 \
  iptools==0.6.1 \
  cython \
  pyOpenSSL \

openssl genrsa -out privkey.pem 2048
openssl req -new -x509 -days 365 -key privkey.pem -out cert.pem

