from flask_restful import Resource, reqparse, Api
from flask import Blueprint
from flask_jwt_extended import create_access_token

from sr.user.models import User
from sr.user.exceptions import APIUnauthenticatedException, UnauthenticatedException


blueprint = Blueprint('user_api', __name__, url_prefix='/api/user')
api = Api(blueprint)


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True)
login_parser.add_argument('password', required=True)


class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        try:
            user = User.authenticate(args['username'], args['password'])
            token = create_access_token(identity=user.username)
            return {'token': token}
        except UnauthenticatedException:
            raise APIUnauthenticatedException()

api.add_resource(Login, '/login')
