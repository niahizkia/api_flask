from flask import Flask, request
from flask_restful import Resource, Api
import models
from resources.messages import messages_api
from resources.users import users_api

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.register_blueprint(messages_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

# api = Api(app)
# api.add_resource(messages.MessageList, '/messages')

# ACCESS TOKEN JWT
app.config['SECRET_KEY'] = 'rjdhakjfniufreo39487598_ew8ruu9r894thj'
jwt = JWTManager(app)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)