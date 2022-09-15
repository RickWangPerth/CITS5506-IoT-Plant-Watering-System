from app.sensors.camera import Camera
from app.sensors.moisture_sensor import MoistureSensor
from app.sensors.temperature_sensor import TemperatureSensor
from app.sensors.water_level_sensor import WaterLevelSensor
import ExpanderPi
from app.models import History
from datetime import datetime

class CollectSensors:
    moisture = None
    temperature = None
    water_present = None

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
        self.PHOTOS_FOLDER = '/home/cits5506/plant_photos'
        self.KEEP_PHOTOS = 10

        self.camera = Camera(self.PHOTOS_FOLDER, self.KEEP_PHOTOS)
        self.moisture_sensor = MoistureSensor(self.adc, self.REF_VOLTAGE, self.MOISTURE_PIN)
        self.temperature_sensor = TemperatureSensor(self.adc, self.TEMPERATURE_PIN)
        self.water_level_sensor = WaterLevelSensor(self.io, self.WATER_LEVEL_PIN)

        # Get initial readings
        self.update()
    
    def update(self):
        self.moisture = self.moisture_sensor.get_moisture()
        self.temperature = self.temperature_sensor.get_temp()
        self.water_present = self.water_level_sensor.water_detected()
        self.camera.save_picture()
    
    def get_current(self):
        self.update()
        return self.moisture, self.temperature, self.water_present
    
    def update_database(self):
        self.update()
        history = History(datetime.now(), self.moisture, self.temperature, 0, self.water_present)
        self.db.session.add(history)
        self.db.session.commit()