from flask import Blueprint, jsonify
from src.models.character_model import Character
from src.models.episodes_model import Episode
from src.models.location_model import Location

from src.schema.schemas import CharacterModelSchema


character_bp = Blueprint("character_bp",__name__)

@character_bp.route("/", methods=["GET"])
def hellworld():
    print("Hello World")

@character_bp.route("/character",methods=['GET'])
def get_characters():
    allcharacters = Character.query.all()
    allcharacters_schema = CharacterModelSchema(many=True)
    allcharacters_dump = allcharacters_schema.dump(allcharacters)
    return jsonify(allcharacters_dump),200

@character_bp.route("/find/<int:id>", methods=['GET'])
def get_characters_by_id(id):
    char = Character.query.get(id)
    char_schema = CharacterModelSchema()
    char_dump = char_schema.dump(char)
    return jsonify(char_dump), 200
    