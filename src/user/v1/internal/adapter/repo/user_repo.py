from pymongo import MongoClient
from bson import ObjectId
from ......recipe.v1.internal.biz.service.recipe_service import RecipeService
from ...biz.model import PaginatedResponse, TypeUser, TypeRecipe

class UserRepo():
    def __init__(self, mongo_config, recipe_service: RecipeService) -> None:
        self.mongo = None
        self.recipe_service = recipe_service
        self._load_mongo(mongo_config)

    def find_user_by_id(self, user_id: ObjectId) -> TypeUser:
        collection = self.db.users

        result = collection.find_one({"_id": user_id})
        return result
    
    def paginate_recipes(self, page: int, limit: int) -> PaginatedResponse[TypeRecipe]:
        return self.recipe_service.paginate_recipes(page, limit)

    def _load_mongo(self, mongo_config) -> None:
        client = MongoClient(mongo_config['uri'])
        self.db = client[mongo_config['db_name']]