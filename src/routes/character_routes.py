from flask import Blueprint
from src.models.episodes_model import Episode
from src.models.character_model import Character

character_bp = Blueprint("character_bp",__name__)

@character_bp.route("/", methods=["GET"])
def hellworld():
    print("Hello World")