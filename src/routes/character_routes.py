from flask import Blueprint, jsonify, request
from src.models.character_model import Character
from src.models.episodes_model import Episode
from src.models.location_model import Location

from src.schema.schemas import CharacterModelSchema


character_bp = Blueprint("character_bp",__name__)

@character_bp.route("/",methods=['GET'])
def get_characters():
    numPage = int(request.args.get('page',1))
    name_search = request.args.get('name', None)
    limitForPage = 20

    charactersQuery = Character.query.filter(Character.name.ilike(f'%{name_search}%'))

    pagination = charactersQuery.paginate(page=numPage ,per_page=limitForPage)
    char_pagination = pagination.items

    characters_schema = CharacterModelSchema(many=True)    
    resultOfDump = characters_schema.dump(char_pagination)    

    return jsonify({
        'current_page' : pagination.page,
        'total_pages' : pagination.pages,        
        'data' : resultOfDump
    }),200

@character_bp.route("/find/<int:id>", methods=['GET'])
def get_characters_by_id(id):
    char = Character.query.get(id)
    char_schema = CharacterModelSchema()
    char_dump = char_schema.dump(char)
    return jsonify(char_dump), 200
    
