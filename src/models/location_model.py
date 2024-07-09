from configs.database import db

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    dimension = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    created = db.Column(db.String(100), nullable=False)

##CREATE TABLE "locations" (
#  "id" bigint,
#  "name" String(100),
#  "type" String(100),
#  "dimension" String(100),
#  "residents" json,
#  "url" String(100),
#  "created" String(100)
##)