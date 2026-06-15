import nltk
from flask import Flask
from flask_cors import CORS

from src.auth.v1.internal.adapter.handler import auth_handler
from src.container import Container
from src.recipe.v1.internal.adapter.handler import recipe_handler
from src.recipe.v1.internal.adapter.repo import recipe_repo
from src.user.v1.internal.adapter.handler import user_handler
from src.user.v1.internal.adapter.repo import user_repo


def init_models():
    from pathlib import Path

    import gdown

    MODEL_PATH = Path("models/word2vec.model")
    RECIPE_VECTORS = Path("models/recipe_vectors.pkl")
    RECIPE_DF = Path("models/recipes_df.pkl")

    if not RECIPE_VECTORS.exists():
        gdown.download(
            "https://drive.google.com/file/d/18MkDVQonAdYZ8f7jFN58XabBmZx2tE5b/view?usp=drive_link",
            str(RECIPE_VECTORS),
            quiet=False,
        )
    if not RECIPE_DF.exists():
        gdown.download(
            "https://drive.google.com/file/d/13oCmTJO_8JM-Ar1LlPteW87V7DDnQ1DU/view?usp=drive_link",
            str(RECIPE_DF),
            quiet=False,
        )
    if not MODEL_PATH.exists():
        gdown.download(
            "https://drive.google.com/file/d/1EH0CUhFyqIvsFLHqeIUufkuc_BNbx5aX/view?usp=drive_link",
            str(MODEL_PATH),
            quiet=False,
        )


def create_app() -> Flask:
    app = Flask(__name__)
    init_models()
    nltk.download("punkt_tab")
    # TODO: move this
    app.secret_key = "your_secret_key"
    app.config.update(
        SESSION_PERMANENT=False,
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_SAMESITE="None",
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_DOMAIN=None,
    )

    CORS(app, supports_credentials=True)

    app.register_blueprint(recipe_handler.recipe_blueprint)
    app.register_blueprint(auth_handler.auth_blueprint)
    app.register_blueprint(user_handler.user_blueprint)

    container = Container()
    container.wire(
        modules=[
            recipe_handler.__name__,
            auth_handler.__name__,
            user_handler.__name__,
            user_repo.__name__,
            recipe_repo.__name__,
        ]
    )

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, host="0.0.0.0", port=8080)
