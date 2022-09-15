from email.policy import default
from app import db
from sqlalchemy.sql import func

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=1)
    moisMin = db.Column(db.Integer,index=True, default=20)
    moisMax = db.Column(db.Integer,index=True, default=70)
    tempMin = db.Column(db.Integer,index=True, default=5)
    tempMax = db.Column(db.Integer,index=True, default=35)
    lightMax = db.Column(db.Integer,index=True, default=2)
    lightMin = db.Column(db.Integer,index=True, default=5)
    wateringTime = db.Column(db.Integer,index=True, default=2)

    def __repr__(self):
        return '[id;{},moisMin:{}, moisMax:{}, tempMin:{}, tempMax:{}, lightMax:{}, lightMin:{}, wateringTime:{}]'.format(
            self.id,
            self.moisMin,
            self.moisMax,
            self.tempMin,
            self.lightMax,
            self.lightMin,
            self.wateringTime)

    def to_dict(self):
        return {
            'id': self.id,
            'moisMin': self.moisMin,
            'moisMax': self.moisMax,
            'tempMin': self.tempMin,
            'tempMax': self.tempMax,
            'lightMax': self.lightMax,
            'lightMin': self.lightMin,
            'wateringTime':self.wateringTime
        }
class History(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now(), primary_key=True)
    moisture = db.Column(db.REAL,index=True)
    temperature = db.Column(db.REAL,index=True)
    light = db.Column(db.REAL,index=True)
    waterLevel = db.Column(db.Boolean, index=True)
    