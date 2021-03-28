from flask import request
from flask_restx import Resource

from ..util.dto import UtvarDto
#from ..util.decorator import access_control
from ..service.utvar_service import save_new_utvar, get_all_utvar

api = UtvarDto.api
_utvar = UtvarDto.utvar


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_utvar')
    @api.marshal_list_with(_utvar, envelope='data')
    def get(self):
        """List all registered utvar"""
        return get_all_utvar()

    @api.response(200, 'User successfully created.')
    @api.doc('create a new utvar')
    @api.expect(_utvar, validate=True)
    def post(self):
        """Creates a new Utvar"""
        data = request.json
        return save_new_utvar(data=data)