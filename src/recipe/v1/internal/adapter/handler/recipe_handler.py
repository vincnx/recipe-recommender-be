from flask import Blueprint, jsonify, request
from ...biz.service.recipe_service import RecipeService
from ......container import Container
from dependency_injector.wiring import Provide
from bson import ObjectId

recipe_blueprint = Blueprint('recipe_blueprint', __name__, url_prefix="/v1/recipes")

recipe_service: RecipeService = Provide[Container.recipe_service]

@recipe_blueprint.route('', methods=['GET'])
def list_recipes():
    ids = request.args.get('ids')
    id_list = [ObjectId(i.strip()) for i in ids.split(",")] if ids else None
    
    data = recipe_service.list_recipes(id_list)
    
    for item in data:
        item['_id'] = str(item['_id'])
    
    return jsonify(data), 200

@recipe_blueprint.route('', methods=['POST'])
def get_recipes():
    recipes = recipe_service.get_recommendations(' '.join(request.json['ingredients']))
    return jsonify(recipes), 200

@recipe_blueprint.route('seed', methods=['GET'])
def seed_data():
    recipe_service.seed_data()
    return jsonify({"message": "success"}), 200

