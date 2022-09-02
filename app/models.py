from app import db
from sqlalchemy.sql import func

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moisMin = db.Column(db.Integer,index=True)
    moisMax = db.Column(db.Integer,index=True)
    tempMin = db.Column(db.Integer,index=True)
    tempMax = db.Column(db.Integer,index=True)
    lightMax = db.Column(db.Integer,index=True)
    lightMin = db.Column(db.Integer,index=True)
    waterTime = db.Column(db.Integer,index=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

