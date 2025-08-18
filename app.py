from flask import Flask, request
from src.recipe.v1.internal.adapter.handler import recipe_handler
from src.auth.v1.internal.adapter.handler import auth_handler
from src.container import Container
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)
    # TODO: move this
    app.secret_key = 'your_secret_key'
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_SAMESITE='None',
        SESSION_COOKIE_HTTPONLY=True,
    )

    CORS(app, supports_credentials=True)

    app.register_blueprint(recipe_handler.recipe_blueprint)
    app.register_blueprint(auth_handler.auth_blueprint)

    container = Container()
    container.wire(
        modules=[recipe_handler.__name__, auth_handler.__name__]
    ) 

    return app

if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, host='0.0.0.0', port=8080)