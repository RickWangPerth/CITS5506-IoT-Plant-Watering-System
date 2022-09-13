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
    wateringTime = db.Column(db.Integer,index=True)

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