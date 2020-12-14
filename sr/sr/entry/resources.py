import json
from flask_restful import Resource, reqparse, Api
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity


from sr.entry.models import Entry as EntryModel
from sr.user.models import User
from sr.user.utils import has_permissions_api


blueprint = Blueprint('entry_api', __name__, url_prefix='/api/entry')
api = Api(blueprint)


list_parser = reqparse.RequestParser()
list_parser.add_argument('q')

create_parser = reqparse.RequestParser()
create_parser.add_argument('title', type=str, required=True)
create_parser.add_argument('content', type=str, required=True)


class EntryList(Resource):
    @jwt_required
    def get(self):
        args = list_parser.parse_args()
        return json.dumps(EntryModel.search(args.get('q')))

    @has_permissions_api(['entry.create'])
    def post(self):
        username = get_jwt_identity()
        user = User.by_username(username)
        args = create_parser.parse_args()
        EntryModel.create(args['title'], args['content'], user)
        return '', 201


class Entry(Resource):
    @has_permissions_api(['entry.update'])
    def put(self, id):
        entry = EntryModel.by_id(id)
        args = create_parser.parse_args()
        entry.update(args['title'], args['content'])
        return '', 201

    @has_permissions_api(['entry.delete'])
    def delete(self, id):
        entry = EntryModel.by_id(id)
        entry.delete()
        return '', 201


api.add_resource(EntryList, '')
api.add_resource(Entry, '/<int:id>')
