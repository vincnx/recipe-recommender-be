from  ...adapter.repo.recipe_repo import RecipeRepo
from ...biz.model.recipe_model import PaginatedResponse, TypeRecipe
from bson import ObjectId

class RecipeService():
    def __init__(self, repo: RecipeRepo) -> None:
        self.repo = repo

    def paginate_recipes(self, page=1, limit=10) -> PaginatedResponse[TypeRecipe]:
        return self.repo.paginate_recipes(page, limit)

    def list_recipes(self, recipe_ids: list[ObjectId] = None):
        return self.repo.find_recipes(recipe_ids)

    def get_recipe(self, recipe_id: ObjectId) -> TypeRecipe:
        return self.repo.find_recipe(recipe_id)
    
    def get_recommendations(self, user_input, num_recommendations=9) -> list[TypeRecipe]:
        return self.repo.get_recommendations(user_input, num_recommendations)