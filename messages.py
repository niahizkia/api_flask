from flask import jsonify
from flask_restful import Resource, Api
import models

class MessageList(Resource):
    def get(self):
        # get data from database
        messages = {}
        query = models.Message.select()

        for row in query:
            messages[row.id] = {'content': row.content,
                                'published_at' : row.published_at}

        return jsonify({'messages':messages})
