from flask import Blueprint
from src.models.character_model import Character

from src.schema.schemas import CharacterModelSchema

character_bp = Blueprint("character_bp",__name__)

@character_bp.route("/", methods=["GET"])
def hellworld():
    print("Hello World")

@character_bp.route("/character",methods=['GET'])
def get_characters():
    allcharacters = Character.query.all()
    allcharacters_schema = CharacterModelSchema(many=True)
    return allcharacters_schema.jsonify(allcharacters)