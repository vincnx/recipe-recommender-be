from flask import Flask, request
from src.recipe.v1.internal.adapter.handler import recipe_handler
from src.container import Container
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(recipe_handler.recipe_blueprint)

    container = Container()
    container.wire(
        modules=[recipe_handler.__name__]
    ) 

    return app

if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, host='0.0.0.0', port=8080)