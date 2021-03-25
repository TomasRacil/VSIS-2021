from flask import request
from flask_restx import Resource

from ..util.dto import OsobaDto
#from ..util.decorator import access_control
from ..service.osoba_service import save_new_osoba

api = OsobaDto.api
_osoba = OsobaDto.osoba


@api.route('/')
class UserList(Resource):
    @api.response(200, 'User successfully created.')
    @api.doc('create a new osoba')
    @api.expect(_osoba, validate=True)
    def post(self):
        """Creates a new Osoba """
        data = request.json
        return save_new_osoba(data=data)