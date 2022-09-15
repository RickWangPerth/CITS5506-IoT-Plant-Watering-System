from camera import Camera
from moisture_sensor import MoistureSensor
from temperature_sensor import TemperatureSensor
from water_level_sensor import WaterLevelSensor
import ExpanderPi
import time

class CollectSensors:
    moisture = None
    temperature = None
    water_present = None

    def __init__(self):
        # Analog I/O
        self.REF_VOLTAGE = 4.096
        self.adc = ExpanderPi.ADC()  # create an instance of the ADC
        self.adc.set_adc_refvoltage(self.REF_VOLTAGE)
        self.MOISTURE_PIN = 2
        self.TEMPERATURE_PIN = 1

        # Digital I/O
        self.WATER_LEVEL_PIN = 1
        self.io = ExpanderPi.IO()

        self.camera = Camera()
        self.moisture_sensor = MoistureSensor(self.adc, self.REF_VOLTAGE, self.MOISTURE_PIN)
        self.temperature_sensor = TemperatureSensor(self.adc, self.TEMPERATURE_PIN)
        self.water_level_sensor = WaterLevelSensor(self.io, self.WATER_LEVEL_PIN)

        # Get initial readings
        self.update()
    
    def update(self):
        self.moisture = self.moisture_sensor.get_moisture()
        self.temperature = self.temperature_sensor.get_temp()
        self.water_present = self.water_level_sensor.water_detected()
    
    def get_current(self):
        self.update()
        return self.moisture, self.temperature, self.water_present

if __name__ == "__main__":
    sensors = CollectSensors()
    while True:
        print(sensors.get_current())
        time.sleep(0.3)