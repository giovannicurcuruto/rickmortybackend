from configs.database import db

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    origin_name = db.Column(db.String(100), nullable=False)
    origin_url = db.Column(db.String(100), nullable=False)
    location_name = db.Column(db.String(100), nullable=False)
    location_url = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    created = db.Column(db.String(100), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"))
    
    # Relacionamento entre Character_Episode
    episodes = db.relationship('CharacterEpisode', backref='character', lazy=True)

#
# CREATE TABLE "character" (
# "id" bigint,
#  "name" String(100),
#  "status" String(100),
#  "species" String(100),
#  "type" String(100),
#  "gender" String(100),
#  "origin.name" String(100),
#  "origin.url" String(100),
#  "location.name" String(100),
#  "location.url" String(100),
#  "image" String(100),
#  "episode" json,
#  "url" String(100),
#  "created" String(100)
#);
