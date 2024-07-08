from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    origin_name = db.Column(db.Text, nullable=False)
    origin_url = db.Column(db.Text, nullable=False)
    location_name = db.Column(db.Text, nullable=False)
    location_url = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    created = db.Column(db.Text, nullable=False)

#
# CREATE TABLE "character" (
# "id" bigint,
#  "name" text,
#  "status" text,
#  "species" text,
#  "type" text,
#  "gender" text,
#  "origin.name" text,
#  "origin.url" text,
#  "location.name" text,
#  "location.url" text,
#  "image" text,
#  "episode" json,
#  "url" text,
#  "created" text
#);
