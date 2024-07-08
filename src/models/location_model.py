from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    dimension = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    created = db.Column(db.Text, nullable=False)


##CREATE TABLE "locations" (
#  "id" bigint,
#  "name" text,
#  "type" text,
#  "dimension" text,
#  "residents" json,
#  "url" text,
#  "created" text
##)