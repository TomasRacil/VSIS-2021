from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        #'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class OsobaDto:
    api = Namespace('osoba', description='enpoint pro =upravu osob')
    osoba=api.model('osoba', {
        'jmeno': fields.String(required=True, description='user email address'),
        'prijmeni': fields.String(required=True, description='user username'),
        'osobni_cislo': fields.Integer(required=True, description='user password'),
        'hodnost_id': fields.Integer(description='user Identifier')
    })