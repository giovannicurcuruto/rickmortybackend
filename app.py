from flask import Flask
from src.routes.character_routes import character_bp
from configs.database import init_db

def create_app():
    app = Flask(__name__)
    init_db(app)
    app.register_blueprint(character_bp, url_prefix="/character")
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)