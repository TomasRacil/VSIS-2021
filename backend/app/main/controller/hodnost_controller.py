from flask import request
from flask_restx import Resource

from ..util.dto import HodnostDto
from ..service.hodnost_service import save_new_hodnost, get_all_hodnost

api = HodnostDto.api
_hodnost = HodnostDto.hodnost


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_osob')
    @api.marshal_list_with(_hodnost, envelope='data')
    def get(self):
        """List all registered osob"""
        return get_all_hodnost()

    @api.response(200, 'User successfully created.')
    @api.doc('create a new hodnost')
    @api.expect(_hodnost, validate=True)
    def post(self):
        """Creates a new Hodnost"""
        data = request.json
        return save_new_hodnost(data=data)