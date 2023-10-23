from rest_framework.response import Response

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

import platform


class HostNameMiddleWare:
    '''
    Adds the host name to the header
    '''
    def __init__(self, get_response) -> None:
        if not settings.DEBUG:
            raise MiddlewareNotUsed
        self.get_response = get_response

    def __call__(self, request) -> Response:
        response = self.get_response(request)
        response['Node-Name'] = platform.node()
        return response
