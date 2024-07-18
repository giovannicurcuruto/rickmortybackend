from configs.database import db

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=True)
    species = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    origin_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    present_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    image = db.Column(db.String(100), nullable=True)
    
    # Relacionamento entre Character_Episode
    episodes = db.relationship('episode',secondary='character_episodes',back_populates="character", uselist=True, lazy=True)

    # Relacionamento entre Character e Location
    origin_location = db.relationship('locations', foreign_keys=[origin_id], backref='origin_locations', uselist=False, lazy=True)   
    present_location_location = db.relationship('locations', foreign_keys=[present_location_id], backref='present_location_locations',uselist=False, lazy=True)

