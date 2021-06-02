from flask import request
from flask_restx import Resource

from ..service.test_service import HelloWorld

from ..util.dto import TestDto

api = TestDto.api
_test = TestDto.test


@api.route('/')
class Test(Resource):
    @api.doc('get a test message')
    @api.marshal_with(_test)
    def get(self):
        """Return test message"""
        return HelloWorld()
