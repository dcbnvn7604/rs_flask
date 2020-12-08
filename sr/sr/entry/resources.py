import json
from flask_restful import Resource, reqparse, Api
from flask import Blueprint, request
from flask_jwt_extended import jwt_required


from sr.entry.models import Entry


blueprint = Blueprint('entry_api', __name__, url_prefix='/api/entry')
api = Api(blueprint)


entry_list_parser = reqparse.RequestParser()
entry_list_parser.add_argument('q')


class EntryList(Resource):
    @jwt_required
    def get(self):
        return json.dumps(Entry.search(request.args.get('q')))


api.add_resource(EntryList, '')
