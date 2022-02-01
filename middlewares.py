'''
Usage:
    --------------------------------------------------------------------------
    from src.apps.notification import middlewares
    # Get the current request object:
    request = middlewares.get_current_request()
    # You can get the current user directly with:
    user = middlewares.get_current_user()
    --------------------------------------------------------------------------
'''
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

_thread_locals = local()

def get_request():
    """ returns the request object for this thread """
    return getattr(_thread_locals, "request", None)

def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_request()
    if request:
        return getattr(request, "user", None)

class RequestMiddleware(MiddlewareMixin):
    """ Simple middleware that adds the request object in thread local storage."""

    def process_request(self, request):
        _thread_locals.request = request

    def process_response(self, request, response):
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
        return response

    def process_exception(self, request, exception):
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request