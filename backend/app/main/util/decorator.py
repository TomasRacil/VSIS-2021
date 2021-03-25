from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth


def access_control(authorized_role):
    def decorated(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            data, status = Auth.get_logged_in_user(request)
            token = data.get('data')
            print(data, status)
            if not token:
                print(data,status)
                return data, status
            elif authorized_role in token['roles']:
                return f(*args, **kwargs)
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Unauthorized access to endpoint.'
                }
                return response_object, 401

        return wrapper
    return decorated