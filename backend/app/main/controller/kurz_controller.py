from flask import request
from flask_restx import Resource

from ..util.dto import KurzDto
#from ..util.decorator import access_control
from ..service.kurz_service import save_new_kurz, get_all_kurz, get_a_kurz, remove_object

api = KurzDto.api
_kurz_post = KurzDto.kurz_post
_kurz_get = KurzDto.kurz_get


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_kurzy')
    @api.marshal_list_with(_kurz_get, envelope='data')
    def get(self):
        """List all registered kurzy"""
        return get_all_kurz()

    @api.response(200, 'Kurz successfully created.')
    @api.doc('create a new kurz')
    @api.expect(_kurz_post, validate=True)
    def post(self):
        """Creates a new Kurz"""
        data = request.json
        return save_new_kurz(data=data)

@api.route('/<id>')
@api.param('id', 'Kurz identifier')
class Kurz(Resource):
    @api.doc('delete kurz')
    def delete(self, id):
        kurz = get_a_kurz(id)
        if not kurz:
            api.abort(404)
        else:
            return remove_object(kurz), 200