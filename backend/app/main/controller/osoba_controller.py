from flask import request
from flask_restx import Resource

from ..util.dto import OsobaDto
#from ..util.decorator import access_control #tohle je zatím příprava na pozdější kontrolu??? TODO
from ..service.osoba_service import save_new_osoba, get_all_osoba

api = OsobaDto.api
_osoba_post = OsobaDto.osoba_post
_osoba_get = OsobaDto.osoba_get


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_osob')
    @api.marshal_list_with(_osoba_get, envelope='data')
    def get(self):
        """List all registered osob"""
        return get_all_osoba()

    @api.response(200, 'Osoba successfully created.')
    @api.doc('create a new osoba')
    @api.expect(_osoba_post, validate=True)
    def post(self):
        """Creates a new Osoba """
        data = request.json
        return save_new_osoba(data=data)