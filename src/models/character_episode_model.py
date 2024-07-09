from configs.database import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episodes'
    
    character_id = db.Column(db.BigInteger, db.ForeignKey('character.id'), primary_key=True)
    episode_id = db.Column(db.BigInteger, db.ForeignKey('episodes.id'), primary_key=True)

###
#CREATE TABLE character_episodes (
#    character_id bigint,
#    episode_id bigint,
#    FOREIGN KEY (character_id) REFERENCES "character" (id),
#    FOREIGN KEY (episode_id) REFERENCES episodes (id)
#);