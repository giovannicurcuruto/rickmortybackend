from configs.database import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episodes'
    
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), primary_key=True)
