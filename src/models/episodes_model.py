from configs.database import db

class Episode(db.Model):
    __tablename__ = 'episode'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(100), nullable=False)
    episode = db.Column(db.String(100), nullable=False)

    # Relacionamento entre Character_Episode
    characters = db.relationship('Character', secondary='character_episodes', back_populates="episodes", uselist=True, lazy=True)

