import sys

def application(environ, start_response):
    status = '200 OK'
    output = []
    output += ['Hello World!']
    output += ['Running python:']
    output += ['  executable: "{exe}"']
    output += ['  version: "{ver}"']
    output += ['  prefix: "{prfx}"']
    output += ['\n']
    output = '\n'.join(output).format(
        exe=sys.executable,
        ver=sys.version,
        prfx=sys.prefix)
    response_headers = [('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

#def application(environ, start_response):
#    start_response('200 OK', [('Content-type', 'text/plain')])
#    return ["Hello, world!"]

