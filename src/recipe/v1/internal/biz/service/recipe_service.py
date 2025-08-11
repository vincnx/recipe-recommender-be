from  ...adapter.repo.recipe_repo import RecipeRepo
from ...biz.model.recipe_model import TypeRecipe

class RecipeService():
    def __init__(self, repo: RecipeRepo) -> None:
        self.repo = repo
    
    def get_recommendations(self, user_input, num_recommendations=5) -> list[TypeRecipe]:
        return self.repo.get_recommendations(user_input, num_recommendations)