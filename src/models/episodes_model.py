from configs.database import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(100), nullable=False)
    episode = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    created = db.Column(db.String(100), nullable=False)
    characters = db.Column(db.JSON)

    # Relacionamento entre Character_Episode
    characters = db.relationship('CharacterEpisode', backref='episode', lazy=True)

## "Characters" json será utilizado dentro de outro Model
#CREATE TABLE "episodes" (
#  "id" bigint,
#  "name" String(100),
#  "air_date" String(100),
#  "episode" String(100),
#  "characters" json,
#  "url" String(100),
#  "created" String(100)
#);