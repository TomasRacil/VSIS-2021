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

class KurzDto:
    api = Namespace('kurz', description='enpoint pro upravu kurzu')
    kurz=api.model('kurz', {
        'nazev': fields.String(required=True, description='uplný nazev kurzu', example='Strukturovaná kabeláž'),
        'misto': fields.String(required=True, description='kde kurz probíhá', example='Brno'),
        'vedouci': fields.String(required=True, description='celé jméno vedoucího', example='Antonín Voříšek'),
        'voj_oznaceni': fields.String(required=True, description='vojenské označení', example='SK_3098'),
        'zacatek_kurzu': fields.String(description='začátek kurzu', example='1.1.1989'), #required=True, DateTime
        'konec_kurzu': fields.String(description='konec kurzu', example='1.1.1989') #required=True, DateTime, TODO
    })


class UtvarDto:
    api = Namespace('utvar', description='enpoint pro upravu utvaru')
    utvar=api.model('utvar', {
        'nazev_utvaru': fields.String(required=True, description='uplný nazev utvaru', example='UNOB'),
        'lokace': fields.String(required=True, description='kde se utvar nachází', example='Brno'),
        'cislo_vu': fields.Integer(required=True, description='cislo utvaru', example=2994),
    })

class HodnostDto:
    api = Namespace('hodnost', description='enpoint pro upravu hodnosti')
    hodnost=api.model('hodnost', {
        'jmeno': fields.String(required=True, description='uplný nazev hodnosti', example='Poručík'),
        'hodnostni_sbor': fields.String(required=True, description='hodnostní sbor do kterého je zařazena hodnost', example='Nižší důstojník'),
    })