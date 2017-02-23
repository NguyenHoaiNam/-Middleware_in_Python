from webob import Response
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp
 

class AppExample(object):

    @wsgify
    def application(self, req):
        a = req
        return Response('Hello World')

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls().application
 
 
@wsgify.middleware()
def my_filter(req, app):
    # just print a message to the console
    print('my_filter was called')
    return app(req)

 
def filter_factory(global_config, **local_config):
    return my_filter


if __name__ == '__main__':
    wsgi_app = loadapp('config:/nam/my-git/'
                       'Middleware_in_Python/example_two/paste.ini')
    httpserver.serve(wsgi_app, host='0.0.0.0', port=3007)
