from flask import Blueprint, jsonify, request
from ...biz.service.recipe_service import RecipeService
from ......container import Container
from dependency_injector.wiring import Provide

recipe_blueprint = Blueprint('recipe_blueprint', __name__, url_prefix="/v1/recipes")

recipe_service: RecipeService = Provide[Container.recipe_service]

@recipe_blueprint.route('', methods=['POST'])
def get_recipes():
    recipes = recipe_service.get_recommendations(' '.join(request.json['ingredients']))
    return jsonify(recipes), 200