from sys import platform
if platform == "linux":
    from app.sensors.camera import Camera
    import ExpanderPi
    from app.sensors.moisture_sensor import MoistureSensor
    from app.sensors.temperature_sensor import TemperatureSensor
    from app.sensors.water_level_sensor import WaterLevelSensor
    from app.models import History
    from datetime import datetime
    from app.sensors.VEML6030.PiicoDev_VEML6030 import PiicoDev_VEML6030

class CollectSensors:
    moisture = None
    temperature = None
    water_present = None
    light_value = None

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
        self.KEEP_PHOTOS = 100

        self.camera = Camera(self.PHOTOS_FOLDER, self.KEEP_PHOTOS)
        self.moisture_sensor = MoistureSensor(self.adc, self.REF_VOLTAGE, self.MOISTURE_PIN)
        self.temperature_sensor = TemperatureSensor(self.adc, self.TEMPERATURE_PIN)
        self.water_level_sensor = WaterLevelSensor(self.io, self.WATER_LEVEL_PIN)
        self.light_sensor = PiicoDev_VEML6030()

        # Get initial readings
        self.update_sensors()
    
    def update_sensors(self):
        self.moisture = self.moisture_sensor.get_moisture()
        self.temperature = self.temperature_sensor.get_temp()
        self.water_present = self.water_level_sensor.water_detected()
        self.light_value = self.light_sensor.read()
    
    def get_current(self):
        self.update_sensors()
        return self.moisture, self.temperature, self.water_present, self.light_value
    
    def update_database(self):
        self.update_sensors()
        history = History(datetime.now(), 
                            int(self.moisture), 
                            round(self.temperature, 1), 
                            int(self.light_value), 
                            self.water_present)
        self.db.session.add(history)
        self.db.session.commit()
        History.delete_expired()
