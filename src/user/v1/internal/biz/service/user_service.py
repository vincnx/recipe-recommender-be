from this import d
from bson import ObjectId

from ..model import PaginatedResponse, TypeRecipe

from ...adapter.repo.user_repo import UserRepo

class UserService():
    def __init__(self, user_repo: UserRepo) -> None:
        self.repo = user_repo

    def get_recipe_collections(self, user_id: ObjectId, page: int = 1, limit: int = 10) -> (PaginatedResponse[TypeRecipe], int):
        user = self.repo.find_user_by_id(user_id)
        collections = user['collections']

        data = self.repo.paginate_recipes(page, limit)
        recipes = data['items']

        for idx, recipe in enumerate(recipes):
            if recipe['_id'] in collections:
                continue

            data['items'][idx] = {
                "_id": data['items'][idx]["_id"],
                "ingredient_item": "",
                "instructions": "",
                "title": "",
            }

        return data, len(collections)