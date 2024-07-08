from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

## "Characters" json será utilizado dentro de outro Model

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    air_date = db.Column(db.Text, nullable=False)
    episode = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    created = db.Column(db.Text, nullable=False)

## "Characters" json será utilizado dentro de outro Model
#CREATE TABLE "episodes" (
#  "id" bigint,
#  "name" text,
#  "air_date" text,
#  "episode" text,
#  "characters" json,
#  "url" text,
#  "created" text
#);