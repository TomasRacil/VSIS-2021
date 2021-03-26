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
    api = Namespace('osoba', description='enpoint pro upravu osob')
    osoba=api.model('osoba', {
        'jmeno': fields.String(required=True, description='krestni jmeno vojáka', example='Josef'),
        'prijmeni': fields.String(required=True, description='prijmeni vojáka', example='Omáčka'),
        'osobni_cislo': fields.Integer(required=True, description='osobní číslo vojáka', example=123456789),
        'hodnost': fields.String(required=True, description='hodnost vojáka', example='vojín'),
        #'hodnost_id':fields.Integer(required=True,description='id hodnosti vojáka', example=0),
        'utvar_id': fields.Integer(required=True, description='id vojakova utvar',example=2994)
    })