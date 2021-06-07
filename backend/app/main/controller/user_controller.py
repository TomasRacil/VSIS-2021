from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..util.decorator import access_control
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_user, delete_user

api = UserDto.api
_user_get = UserDto.user_get
_user_register = UserDto.user_register
_user_update = UserDto.user_update
_user_delete = UserDto.user_delete


@api.route('/')
class UserList(Resource):
    # @access_control('admin')
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user_get, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user_register, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user_get)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

    # @api.response(200, 'User successfully updated.')
    @api.response(401, 'Passwords does not match')
    @api.doc('update user')
    @api.expect(_user_update, validate=True)
    @api.marshal_with(_user_get)
    def patch(self, public_id):
        """Update user given its identifier and data"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            data = request.json
            return update_user(user=user, data=data), 200

    @api.response(401, 'Passwords does not match')
    @api.doc('update user')
    @api.expect(_user_delete, validate=True)
    @api.marshal_with(_user_get)
    def delete(self, public_id):
        """Delete user given its identifier and current password"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            data = request.json
            return delete_user(user=user, data=data), 200
