from dependency_injector import containers, providers
from .recipe.v1.internal.biz.service.recipe_service import RecipeService
from .recipe.v1.internal.adapter.repo.recipe_repo import RecipeRepo

class Container(containers.DeclarativeContainer):
    recipe_repo = providers.Singleton(RecipeRepo)
    
    recipe_service = providers.Factory(
        RecipeService,
        repo=recipe_repo
    )