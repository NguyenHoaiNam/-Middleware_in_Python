from webob import Response
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp
 
 
@wsgify
def application(req):
    return Response('Hello World')
 
 
@wsgify.middleware()
def my_filter(req, app):
    # just print a message to the console
    print('my_filter was called')
    return app(req)
 
 
def app_factory(global_config, **local_config):
    return application
 
 
def filter_factory(global_config, **local_config):
    return my_filter
 
 
wsgi_app = loadapp('config:/home/stack/github/Middleware_in_Python/example_one/PythonProjects/MiddlewareExample/src/paste.ini')
httpserver.serve(wsgi_app, host='0.0.0.0', port=3007)
