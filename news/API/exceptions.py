from rest_framework.exceptions import APIException


class InvalidAPIQuery(APIException):
    status_code = 500
    default_detail = 'An invalid query parameter was provided'
