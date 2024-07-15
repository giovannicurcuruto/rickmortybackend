from flask import Flask
from src.routes.character_routes import character_bp
from configs.database import init_db
from configs.schema_config import init_ma

def create_app():
    app = Flask(__name__)
    init_db(app)
    init_ma(app)
    app.register_blueprint(character_bp, url_prefix="/character")
    
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)