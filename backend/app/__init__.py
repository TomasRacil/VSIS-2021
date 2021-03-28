from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.osoba_controller import api as osoba_ns
from .main.controller.kurz_controller import api as kurz_ns
from .main.controller.utvar_controller import api as utvar_ns
from .main.controller.hodnost_controller import api as hodnost_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(osoba_ns, path='/osoba')
api.add_namespace(kurz_ns, path='/kurz')
api.add_namespace(utvar_ns, path='/utvar')
api.add_namespace(hodnost_ns, path='/hodnost')
