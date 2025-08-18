from flask import Blueprint, jsonify, request, session
from ......container import Container
from dependency_injector.wiring import Provide
from bson import ObjectId
from ...biz.service.auth_service import AuthService

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix="/v1/auth")

auth_service: AuthService = Provide[Container.auth_service]

@auth_blueprint.route('google/login', methods=['GET'])
def google_login():
    state = request.args.get('state')
    authorization_url, _ = auth_service.get_authorization_url(state)
    
    return jsonify({
        'authorization_url': authorization_url
    }), 200

@auth_blueprint.route('google/callback', methods=['GET'])
def google_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({
            'error': 'No code provided'
        }), 400
    
    return jsonify(auth_service.google_login(code))

@auth_blueprint.route('me', methods=['GET'])
def get_current_user():
    return jsonify(auth_service.get_current_user()), 200

@auth_blueprint.route('logout', methods=['POST'])
def logout():
    return jsonify(auth_service.logout()), 200