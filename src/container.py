from dependency_injector import containers, providers

from .user.v1.internal.biz.service.user_service import UserService
from .user.v1.internal.adapter.repo.user_repo import UserRepo
from .recipe.v1.internal.biz.service.recipe_service import RecipeService
from .auth.v1.internal.biz.service.auth_service import AuthService
from .recipe.v1.internal.adapter.repo.recipe_repo import RecipeRepo
from .auth.v1.internal.adapter.repo.auth_repo import AuthRepo

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=[
        "src/recipe/v1/config/config.yml", 
        "src/auth/v1/config/config.yml",
        "src/user/v1/config/config.yml"
    ])
    
    recipe_repo = providers.Singleton(RecipeRepo, mongo_config=config.recipe.mongo)
    recipe_service = providers.Factory(RecipeService, repo=recipe_repo)

    auth_repo = providers.Singleton(AuthRepo, mongo_config=config.auth.mongo)
    auth_service = providers.Factory(AuthService, oauth_config=config.auth.google, auth_repo=auth_repo)

    user_repo = providers.Singleton(UserRepo, mongo_config=config.user.mongo, recipe_service=recipe_service)
    user_service = providers.Factory(UserService, user_repo=user_repo)