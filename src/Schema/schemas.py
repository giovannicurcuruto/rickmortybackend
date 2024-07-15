from configs.schema_config import ma
from models import character_model, episodes_model


class CharacterModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = character_model

class EpisodeModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = episodes_model