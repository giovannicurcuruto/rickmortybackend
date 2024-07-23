from configs.database import db

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=True)
    species = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    origin_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    present_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    image = db.Column(db.String(100), nullable=True)
    
    # Relacionamento entre Character_Episode
    episodes = db.relationship('Episode',secondary='character_episodes',back_populates="characters", uselist=True, lazy=True)

    # Relacionamento entre Character e Location
    origin_location = db.relationship('Location', foreign_keys=[origin_id], back_populates='origin_character', uselist=False, lazy=True)   
    present_location_location = db.relationship('Location', foreign_keys=[present_location_id], back_populates='present_location_character', uselist=False, lazy=True)

