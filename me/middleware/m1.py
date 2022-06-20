from django.conf import settings
from django.http import HttpResponsePermanentRedirect

class SecureRequiredMiddlewarebase(object):

    def __init__(self,get_response=None):
        self.get_response = get_response

        self.paths = getattr(settings, 'SECURE_REQUIRED_PATHS')

        self.enabled = self.paths and getattr(settings, 'HTTPS_SUPPORT')
    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        print('test')
        return response

class SecureRequiredMiddleware(SecureRequiredMiddlewarebase):
    def process_request(self, request):
        if self.enabled and not request.is_secure():

            for path in self.paths:
                if request.get_full_path().startswith(path):
                    request_url = request.build_absolute_uri(request.get_full_path())
                    secure_url = request_url.replace('http://', 'https://')
                    print (secure_url)
                    return HttpResponsePermanentRedirect(secure_url)
        return None