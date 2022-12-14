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
        """
        Manages and collects data from the sensors:
        - Temperature sensor
        - Moisture sensor
        - Light sensor
        - Water level sensor
        - Camera

        @param db: The database object to use to store data
        """
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
        self.KEEP_PHOTOS = 100

        self.camera = Camera(self.PHOTOS_FOLDER, self.KEEP_PHOTOS)
        self.moisture_sensor = MoistureSensor(self.adc, self.REF_VOLTAGE, self.MOISTURE_PIN)
        self.temperature_sensor = TemperatureSensor(self.adc, self.TEMPERATURE_PIN)
        self.water_level_sensor = WaterLevelSensor(self.io, self.WATER_LEVEL_PIN)
        self.light_sensor = PiicoDev_VEML6030()

        # Get initial readings
        self.update_sensors()
    
    def update_sensors(self):
        """
        Updates the sensor data and calculates alerts.
        Also takes a picture.
        The picture is saved and the updated sensor data is stored in the object.
        """
        self.get_setting()
        self.moisture = self.moisture_sensor.get_moisture()
        self.temperature = self.temperature_sensor.get_temp()
        self.water_present = self.water_level_sensor.water_detected()
        self.light_value = self.light_sensor.read()
        self.camera.save_picture()

        if self.moisture < self.moisMin:
            self.moisAlert = self.moisture - self.moisMin
        elif self.moisture >= self.moisMin and self.moisture<=self.moisMax:
            self.moisAlert = 0.0
        else:
            self.moisAlert = self.moisture - self.moisMax
        
        if self.temperature < self.tempMin:
            self.tempAlert = self.temperature - self.tempMin
        elif self.temperature >= self.tempMin and self.temperature <= self.tempMax:
            self.tempAlert = 0.0
        else:
            self.tempAlert = self.temperature - self.tempMax

        if self.light_value < self.lightMin:
            self.lightAlert = self.light_value - self.lightMin
        elif self.light_value >= self.lightMin and self.light_value <= self.lightMax:
            self.lightAlert = 0.0
        else:
            self.lightAlert = self.light_value - self.lightMax
    
    def get_current(self):
        """
        Gets the current sensor data
        @return: moisture, temperature, water_present, light_value
        """
        self.update_sensors()
        return self.moisture, self.temperature, self.water_present, self.light_value
    
    def get_setting(self):
        """
        Retrieves the settings from the database for minimum and maximum moisture, temperature and light.
        If they don't exist, default values are used.
        """
        try:
            setting = Setting.query.first()
        except:
            setting = None
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
        """
        Gets the latest sensor data and writes a new row in the database.
        Also deletes entries in the database that are now too old.
        """
        self.update_sensors()
        history = History(datetime.now(), 
                            int(self.moisture), 
                            round(self.temperature, 1), 
                            int(self.light_value), 
                            self.water_present,
                            int(self.moisAlert),
                            int(self.tempAlert),
                            int(self.lightAlert),
                            int(self.waterLevelAlert))

        self.db.session.add(history)
        self.db.session.commit()
        History.delete_expired()
