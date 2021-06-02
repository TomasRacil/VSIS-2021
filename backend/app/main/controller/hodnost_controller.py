from flask import request
from flask_restx import Resource

from ..util.dto import HodnostDto
#from ..util.decorator import access_control
from ..service.hodnost_service import save_new_hodnost, get_all_hodnost

api = HodnostDto.api
_hodnost_post = HodnostDto.hodnost_post
_hodnost_get = HodnostDto.hodnost_get



@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_hodnosti')
    @api.marshal_list_with(_hodnost_get, envelope='data')
    def get(self):
        """List all hodnosti"""
        return get_all_hodnost()

    @api.response(200, 'Hodnost successfully created.')
    @api.doc('create a new hodnost')
    @api.expect(_hodnost_post, validate=True)
    def post(self):
        """Creates a new Hodnost"""
        data = request.json
        return save_new_hodnost(data=data)