from rest_framework.response import Response

class SuccessResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type='application/json'):
        super().__init__(data, status, template_name, headers, exception, content_type)
   

class ErrorResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type='application/problem+json'):
        # error_message = {

        # }
        super().__init__(data, status, template_name, headers, exception, content_type)
