from flask import jsonify, Blueprint, abort
from flask_restful import Resource, Api, reqparse, fields, marshal, marshal_with
import models


class User:
    pass


users_api = Blueprint('resources/users', __name__)
api          = Api(users_api)


api.add_resource(User, '/users', endpoint='users')