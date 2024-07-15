from flask import Blueprint
from src.models.episodes_model import Episode
from src.models.character_model import Character

from src.Schema.schemas import CharacterModel

character_bp = Blueprint("character_bp",__name__)

@character_bp.route("/", methods=["GET"])
def hellworld():
    print("Hello World")

@character_bp.route("/allc",methods=['GET'])
def get_characters():
    allcharacters = Character.query.all()
    allcharacters_schema = CharacterModel(many=True)
    return allcharacters_schema.jsonify(allcharacters)