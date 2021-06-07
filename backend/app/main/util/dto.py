from flask_restx import Namespace, fields, cors
import datetime


class UserDto:
    api = Namespace('user', description='user related operations', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    user_register = api.model('user_register', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        # 'public_id': fields.Ïnteger(description='user Identifier')
    })
    user_get = api.model('user_get', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        # 'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(required=True, description='user Identifier')
    })
    user_update = api.model('user_update', {
        'email': fields.String(required=False, description='user email address'),
        'username': fields.String(required=False, description='user username'),
        'current_password': fields.String(required=True, description='old user password'),
        'password': fields.String(required=False, description='new user password')
    })
    user_delete = api.model('user_delete', {
        'current_password': fields.String(required=True, description='old user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class OsobaDto:
    api = Namespace('osoba', description='enpoint pro upravu osob', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    osoba_post = api.model('osoba_post', {
        'jmeno': fields.String(required=True, description='krestni jmeno vojáka', example='Josef'),
        'prijmeni': fields.String(required=True, description='prijmeni vojáka', example='Omáčka'),
        'osobni_cislo': fields.Integer(required=True, description='osobní číslo vojáka', example=123456789),
        # je potřeba aby hodnost byla totožná s uloženou v tabulce!! TODO
        'hodnost': fields.String(required=True, description='hodnost vojáka', example='Vojín'),
        # 'hodnost_id':fields.Integer(required=True,description='id hodnosti vojáka', example=0),
        'utvar': fields.Integer(required=True, description='id vojakova utvaru', example=2994)
    })
    osoba_get = api.model('osoba_get', {
        'id': fields.Integer(description='identifikator', example=1),
        'jmeno': fields.String(required=True, description='krestni jmeno vojáka', example='Josef'),
        'prijmeni': fields.String(required=True, description='prijmeni vojáka', example='Omáčka'),
        'osobni_cislo': fields.Integer(required=True, description='osobní číslo vojáka', example=123456789),
        'hodnost': fields.String(required=True, description='hodnost vojáka', example='Vojín'),
        # 'hodnost_id':fields.Integer(required=True,description='id hodnosti vojáka', example=0),
        'utvar': fields.Integer(required=True, description='id vojakova utvaru', example=2994)
    })

class TestDto:
    api = Namespace('test', description='endpoint for testing')
    test = api.model('test', {
        'message': fields.String(required=True, description='message to send', example='Hello!')
    })


class KurzDto:
    api = Namespace('kurz', description='enpoint pro upravu kurzu', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    kurz_post = api.model('kurz_post', {
        'nazev': fields.String(required=True, description='uplný nazev kurzu', example='Strukturovaná kabeláž'),
        'misto': fields.String(required=True, description='kde kurz probíhá', example='Brno'),
        # 'vedouci': fields.String(required=True, description='celé jméno vedoucího', example='Antonín Voříšek'),
        'voj_oznaceni': fields.String(required=True, description='vojenské označení', example='SK_3098'),
        # required=True, DateTime
        'zacatek_kurzu': fields.DateTime(description='začátek kurzu', example=str(datetime.datetime.now())),
        # required=True, DateTime, TODO
        'konec_kurzu': fields.DateTime(description='konec kurzu', example=str(datetime.datetime.now()))
    })
    kurz_get = api.model('kurz_get', {
        'id': fields.Integer(description='identifikator', example=1),
        'nazev': fields.String(required=True, description='uplný nazev kurzu', example='Strukturovaná kabeláž'),
        'misto': fields.String(required=True, description='kde kurz probíhá', example='Brno'),
        # 'vedouci': fields.String(required=True, description='celé jméno vedoucího', example='Antonín Voříšek'),
        'voj_oznaceni': fields.String(required=True, description='vojenské označení', example='SK_3098'),
        # required=True, DateTime
        'zacatek_kurzu': fields.DateTime(description='začátek kurzu', example=str(datetime.datetime.now())),
        # required=True, DateTime, TODO
        'konec_kurzu': fields.DateTime(description='konec kurzu', example=str(datetime.datetime.now()))
    })


class UtvarDto:
    api = Namespace('utvar', description='enpoint pro upravu utvaru', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    utvar_post = api.model('utvar_post', {
        'nazev_utvaru': fields.String(required=True, description='uplný nazev utvaru', example='UNOB'),
        'lokace': fields.String(required=True, description='kde se utvar nachází', example='Brno'),
        'cislo_vu': fields.Integer(required=True, description='cislo utvaru', example=2994),
    })
    utvar_get = api.model('utvar_get', {
        'nazev_utvaru': fields.String(required=True, description='uplný nazev utvaru', example='UNOB'),
        'lokace': fields.String(required=True, description='kde se utvar nachází', example='Brno'),
        'cislo_vu': fields.Integer(required=True, description='cislo utvaru', example=2994),
    })


class HodnostDto:
    api = Namespace('hodnost', description='enpoint pro upravu hodnosti', decorators=[
                    cors.crossdomain(origin="http://localhost:3000")])
    hodnost_post = api.model('hodnost_post', {  # změnit na post
        'nazev': fields.String(required=True, description='uplný nazev hodnosti', example='Poručík'),
        'hodnostni_sbor': fields.String(required=True, description='hodnostní sbor do kterého je zařazena hodnost', example='Nižší důstojník'),

    })
    hodnost_get = api.model('hodnost_get', {
        'id': fields.Integer(description='identifikator', example=1),
        'nazev': fields.String(required=True, description='uplný nazev hodnosti', example='Poručík'),
        'hodnostni_sbor': fields.String(required=True, description='hodnostní sbor do kterého je zařazena hodnost', example='Nižší důstojník'),

    })
