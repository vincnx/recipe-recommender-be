from bson import ObjectId
from dependency_injector.wiring import Provide
from flask import Blueprint, jsonify, request, session
from ......container import Container
from ...biz.service.user_service import UserService


user_blueprint = Blueprint('user_blueprint', __name__, url_prefix="/v1/user")

user_service: UserService = Provide[Container.user_service]

@user_blueprint.route('collections', methods=['GET'])
def get_recipe_collections():
    user = session.get('user')

    if not user:
        return jsonify(), 401
    
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))

    data, num_collection = user_service.get_recipe_collections(ObjectId(user['_id']), page, limit)
    data['num_collection'] = num_collection

    return jsonify(data), 200