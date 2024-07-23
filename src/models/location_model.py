from configs.database import db

class Location(db.Model):
    __tablename__ = 'location'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    dimension = db.Column(db.String(100), nullable=False)

    origin_character = db.relationship('Character', foreign_keys='Character.origin_id', back_populates='origin_location', uselist=False, lazy=True)
    present_location_character = db.relationship('Character', foreign_keys='Character.present_location_id', back_populates='present_location_location', uselist=False, lazy=True)