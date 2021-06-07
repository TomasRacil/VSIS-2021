from flask import request
from flask_restx import Resource

from ..util.dto import UtvarDto
#from ..util.decorator import access_control
from ..service.utvar_service import get_a_utvar, remove_object, save_new_utvar, get_all_utvar

api = UtvarDto.api
_utvar_post = UtvarDto.utvar_post
_utvar_get = UtvarDto.utvar_get


@api.route('/')
class UtvarList(Resource):
    @api.doc('list_of_registered_utvaru')
    @api.marshal_list_with(_utvar_get, envelope='data')
    def get(self):
        """List all registered utvaru"""
        return get_all_utvar()

    @api.response(200, 'Utvar successfully created.')
    @api.doc('create a new utvar')
    @api.expect(_utvar_post, validate=True)
    def post(self):
        """Creates a new Utvar"""
        data = request.json
        return save_new_utvar(data=data)


@api.route('/<cislo_vu>')
@api.param('cislo_vu', 'Utvar identifier')
class Utvar(Resource):
    @api.doc('delete user')
    def delete(self, cislo_vu):
        utvar = get_a_utvar(cislo_vu)
        if not utvar:
            api.abort(404)
        else:
            return remove_object(utvar), 200
