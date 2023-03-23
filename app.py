from flask import Flask, request
from flask_restful import Resource, Api
import models
from resources.messages import messages_api
from resources.users import users_api

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt

app = Flask(__name__)
app.register_blueprint(messages_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

# api = Api(app)
# api.add_resource(messages.MessageList, '/messages')

# ACCESS TOKEN JWT
app.config['SECRET_KEY']                    = 'rjdhakjfniufreo39487598_ew8ruu9r894thj'
app.config['JWT_BLACKLIST_ENABLE']          = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS']    = ['access', 'refresh']


jwt = JWTManager(app)


blocklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    return jti in blocklist

@app.route('/api/v1/user/logout')
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    blocklist.add(jti)
    return{'msg':'berhasil logout.....'}

if __name__ == '__main__':
    models.initialize()
    app.run(debug=True)