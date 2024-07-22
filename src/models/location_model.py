from configs.database import db

class Location(db.Model):
    __tablename__ = 'location'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    dimension = db.Column(db.String(100), nullable=False)

