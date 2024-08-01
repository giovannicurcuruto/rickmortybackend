from flask import Flask
from flask_cors import CORS
from src.routes.character_routes import character_bp
from configs.database import init_db
from configs.schema_config import init_ma

from flask_swagger_ui import get_swaggerui_blueprint

def init_swagger(app):
    SWAGGER_URL = '/swagger'
    API_URL = './swagger_api.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Rick n Morty Backend's"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = True
    CORS(app)
    init_db(app)
    init_ma(app)
    init_swagger(app)
    app.register_blueprint(character_bp, url_prefix="/character")
    
    return app

app = create_app()
    
if __name__ == "__main__":
    app.run(debug=True)