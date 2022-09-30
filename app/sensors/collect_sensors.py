from sys import platform
if platform == "linux":
    from app.sensors.camera import Camera
    import ExpanderPi
    from app.sensors.moisture_sensor import MoistureSensor
    from app.sensors.temperature_sensor import TemperatureSensor
    from app.sensors.water_level_sensor import WaterLevelSensor
    from app.models import Setting, History
    from datetime import datetime
    from app.sensors.VEML6030.PiicoDev_VEML6030 import PiicoDev_VEML6030

class CollectSensors:
    moisture = None
    temperature = None
    water_present = None
    light_value = None

    moisMin = None
    moisMax = None
    tempMin = None
    tempMax = None
    lightMin = None
    lightMax = None

    moisAlert = None
    tempAlert = None
    lightAlert = None
    waterLevelAlert = 0


    def __init__(self, db):
        self.db = db

        # Analog I/O
        self.REF_VOLTAGE = 4.096
        self.adc = ExpanderPi.ADC()  # create an instance of the ADC
        self.adc.set_adc_refvoltage(self.REF_VOLTAGE)
        self.MOISTURE_PIN = 2
        self.TEMPERATURE_PIN = 1

        # Digital I/O
        self.WATER_LEVEL_PIN = 3
        self.io = ExpanderPi.IO()

        # Camera
        self.PHOTOS_FOLDER = '/home/cits5506/CITS5506-IoT-Plant-Watering-System/app/static/images/plant_photos'
        self.KEEP_PHOTOS = 10

        self.camera = Camera(self.PHOTOS_FOLDER, self.KEEP_PHOTOS)
        self.moisture_sensor = MoistureSensor(self.adc, self.REF_VOLTAGE, self.MOISTURE_PIN)
        self.temperature_sensor = TemperatureSensor(self.adc, self.TEMPERATURE_PIN)
        self.water_level_sensor = WaterLevelSensor(self.io, self.WATER_LEVEL_PIN)
        self.light_sensor = PiicoDev_VEML6030()

        # Get initial readings
        self.update()
    
    def update(self):
        self.get_setting()
        self.moisture = self.moisture_sensor.get_moisture()
        self.temperature = self.temperature_sensor.get_temp()
        self.water_present = self.water_level_sensor.water_detected()
        self.light_value = self.light_sensor.read()
        self.camera.save_picture()

        if self.moisture < self.moisMin:
            self.moisAlert = 1
        elif self.moisture >= self.moisMin and self.moisture<=self.moisMax:
            self.moisAlert = 0
        else:
            self.moisAlert = 2
        
        if self.temperature < self.tempMin:
            self.tempAlert = 1
        elif self.temperature >= self.tempMin and self.temperature <= self.tempMax:
            self.tempAlert = 0
        else:
            self.tempAlert = 2

        if self.light_value < self.lightMin:
            self.lightAlert = 1
        elif self.light_value >= self.lightMin and self.light_value <= self.lightMax:
            self.lightAlert = 0
        else:
            self.lightAlert = 2
    
    def get_current(self):
        self.update()
        return self.moisture, self.temperature, self.water_present
    
    def get_setting(self):
        setting = Setting.query.first()
        if setting is None:
            self.moisMin = 20
            self.moisMax = 70
            self.tempMin = 5
            self.tempMax = 35
            self.lightMin = 2
            self.lightMax = 5
            return True
        self.moisMin = setting.moisMin
        self.moisMax = setting.moisMax
        self.tempMin = setting.tempMin
        self.tempMax = setting.tempMax
        self.lightMin = setting.lightMin
        self.lightMax = setting.lightMax
        return True
    
    def update_database(self):
        self.update()
        #history = History(datetime.now(), self.moisture, self.temperature, self.light_value, self.water_present)
        history = History(datetime.now(), self.moisture, self.temperature, self.light_value, self.water_present, self.moisAlert, self.tempAlert, self.lightAlert, self.waterLevelAlert)
        self.db.session.add(history)
        self.db.session.commit()
        History.delete_expired()
