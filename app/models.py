from email.policy import default
from app import db
from sqlalchemy.sql import func
import datetime

class Setting(db.Model):
    """
    The Setting table in the database. Stores the minimum and maximum values for moisture, temperature and light.
    Also stores the photo frequency and for how long to pump water onto the plant when it is required.
    """
    __tablename__ = "setting"
    id = db.Column(db.Integer, primary_key=True, default=1)
    moisMin = db.Column(db.Integer,index=True, default=20)
    moisMax = db.Column(db.Integer,index=True, default=95)
    tempMin = db.Column(db.Integer,index=True, default=5)
    tempMax = db.Column(db.Integer,index=True, default=35)
    lightMax = db.Column(db.Integer,index=True, default=2)
    lightMin = db.Column(db.Integer,index=True, default=5)
    wateringTime = db.Column(db.Integer,index=True, default=2)
    pictureFrequency = db.Column(db.Integer,index=True, default=2)

    def __repr__(self):
        # Converts a Setting object to a string
        return '[id;{},moisMin:{}, moisMax:{}, tempMin:{}, tempMax:{}, lightMax:{}, lightMin:{}, wateringTime:{}, pictureFrequency: {}]'.format(
            self.id,
            self.moisMin,
            self.moisMax,
            self.tempMin,
            self.tempMax,
            self.lightMax,
            self.lightMin,
            self.wateringTime,
            self.pictureFrequency)

    def to_dict(self):
        # Converts a Setting object to a dictionary
        return {
            'id': self.id,
            'moisMin': self.moisMin,
            'moisMax': self.moisMax,
            'tempMin': self.tempMin,
            'tempMax': self.tempMax,
            'lightMax': self.lightMax,
            'lightMin': self.lightMin,
            'wateringTime':self.wateringTime,
            #'alertMessage':self.alertMessage
            'pictureFrequency':self.pictureFrequency
        }


class History(db.Model):
    """
    The History table in the database.
    Stores a row for each time the sensor data is recorded.
    Values are the time, temperature, moisture, ambient light, water level and corresponding alerts at the time.
    """

    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now(), primary_key=True)
    moisture = db.Column(db.REAL,index=True)
    temperature = db.Column(db.REAL,index=True)
    light = db.Column(db.REAL,index=True)
    waterLevel = db.Column(db.Boolean, index=True)
    moistureAlert = db.Column(db.REAL, index=True, default=0.0)
    temperatureAlert = db.Column(db.REAL, index=True, default=0.0)
    lightAlert = db.Column(db.REAL, index=True, default=0.0)
    waterLevelAlert = db.Column(db.Integer, index=True, default=0)

    def __init__(self, timestamp, moisture, temperature, light, waterLevel, moistureAlert, temperatureAlert, lightAlert, waterLevelAlert):
        self.timestamp = timestamp
        self.moisture = moisture
        self.temperature = temperature
        self.light = light
        self.waterLevel = waterLevel
        self.moistureAlert = moistureAlert
        self.temperatureAlert = temperatureAlert
        self.lightAlert = lightAlert
        self.waterLevelAlert = waterLevelAlert
    
    @classmethod
    def delete_expired(cls, minutes=1):
        """
        Deletes expired historical data that is too old.
        @param minutes: How long to keep historical data for.
        """
        expiration = datetime.timedelta(minutes=minutes)
        limit = datetime.datetime.now() - expiration
        cls.query.filter(cls.timestamp <= limit).delete()
        db.session.commit()

    def __str__(self):
        # Converts a History object to a string
        return str((self.timestamp, self.moisture, self.temperature, self.light, self.waterLevel, self.alertMessage))