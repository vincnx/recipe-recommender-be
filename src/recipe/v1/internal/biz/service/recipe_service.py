from  ...adapter.repo.recipe_repo import RecipeRepo
from ...biz.model.recipe_model import TypeRecipe
from bson import ObjectId

class RecipeService():
    def __init__(self, repo: RecipeRepo) -> None:
        self.repo = repo

    def list_recipes(self, recipe_ids: list[ObjectId] = None):
        return self.repo.find_recipes(recipe_ids)
    
    def get_recommendations(self, user_input, num_recommendations=5) -> list[TypeRecipe]:
        return self.repo.get_recommendations(user_input, num_recommendations)

    def seed_data(self):
        return self.repo.seed_data()