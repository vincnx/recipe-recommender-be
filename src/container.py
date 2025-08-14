from dependency_injector import containers, providers
from .recipe.v1.internal.biz.service.recipe_service import RecipeService
from .recipe.v1.internal.adapter.repo.recipe_repo import RecipeRepo

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["src/recipe/v1/config/config.yml"])
    
    recipe_repo = providers.Singleton(RecipeRepo, mongo_config=config.mongo)
    
    recipe_service = providers.Factory(
        RecipeService,
        repo=recipe_repo
    )