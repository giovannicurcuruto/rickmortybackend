from configs.schema_config import ma

class CharacterModelSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    type = ma.String()
    gender = ma.String()
    origin_id = ma.String()
    present_location_id = ma.String()
    image = ma.String()

    

class EpisodeModelSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()



