from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse
import models

class MessageList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'content',
            required = True,
            help     = 'konten wajib ada',
            location = ['form']
        )
        self.reqparse.add_argument(
            'published_at',
            required = True,
            help     = 'published_at/waktu wajib ada',
            location = ['form']
        )
        super().__init__()

    def get(self):
        # get data from database
        messages = {}
        query = models.Message.select()

        for row in query:
            messages[row.id] = {'content': row.content,
                                'published_at' : row.published_at}
        return jsonify({'messages':messages})

    def post(self):
        args = self.reqparse.parse_args()
        message = models.Message.create(**args)
        return jsonify({'success': 'True', 'message':message.content})


class Message(Resource):

    def get(self, id):
        message = models.Message.get_by_id(id)
        return jsonify({'messages':message.content})


messages_api = Blueprint('resources/messages', __name__)
api          = Api(messages_api)


api.add_resource(MessageList, '/messages', endpoint='messages')
api.add_resource(Message, '/message/<int:id>', endpoint='message')