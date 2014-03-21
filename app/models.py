from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(100), index = True, unique = True)

    
