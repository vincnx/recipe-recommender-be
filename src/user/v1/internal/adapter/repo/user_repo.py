from dependency_injector.wiring import Provide, inject
from pymongo import MongoClient
from bson import ObjectId
from ......recipe.v1.internal.biz.service.recipe_service import RecipeService
from ...biz.model import PaginatedResponse, TypeUser, TypeRecipe

class UserRepo():
    def __init__(self, mongo_config) -> None:
        self.mongo = None
        self._load_mongo(mongo_config)

    def find_user_by_id(self, user_id: ObjectId) -> TypeUser:
        collection = self.db.users

        result = collection.find_one({"_id": user_id})
        return result
    
    def update_recipe_collections(self, user_id: ObjectId, recipe_ids: list[str]) -> None:
        collection = self.db.users

        collection.update_one(
            {"_id": user_id},
            {"$addToSet": {
                "collections": {
                    "$each": recipe_ids
                }
            }}
        )

        return
    
    @inject
    def paginate_recipes(
        self, 
        page: int, 
        limit: int, 
        recipe_service: RecipeService = Provide["recipe_service"]
    ) -> PaginatedResponse[TypeRecipe]:
        return recipe_service.paginate_recipes(page, limit)

    def _load_mongo(self, mongo_config) -> None:
        client = MongoClient(mongo_config['uri'])
        self.db = client[mongo_config['db_name']]