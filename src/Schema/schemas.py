from configs.schema_config import ma

class GetAllCharactersSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()

class CharacterModelSchema(GetAllCharactersSchema):
    type = ma.String()
    gender = ma.String()
    origin_location = ma.Nested("LocationModelSchema")
    present_location_location = ma.Nested("LocationModelSchema")

class EpisodeModelSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.String()
    episode = ma.String()

class LocationModelSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()



#Schema do GetALL
#Schema menor e páginação     

